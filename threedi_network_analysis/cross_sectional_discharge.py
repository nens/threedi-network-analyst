import numpy as np
from pathlib import Path
from typing import List, Tuple, Union

from osgeo import ogr

from shapely import wkb
from shapely.geometry import Point, LineString, MultiLineString, MultiPoint
from threedigrid.admin.gridresultadmin import GridH5ResultAdmin
from threedigrid.admin.lines.models import Lines

from .threedigrid_networkx import Q_NET_SUM
from .threedi_result_aggregation.base import time_aggregate
from .threedi_result_aggregation.threedigrid_ogr import threedigrid_to_ogr

# Calculate the net cumulative flow through all flowlines in the model
# Make a directional Graph (NetworkX object) from this

# Select flowlines that intersect the gauge line
# It would be easier to implement this in pyqgis


def intersected_segments(line: Union[LineString, MultiLineString], intersecting_line: LineString) -> List[LineString]:
    """
    Returns the segments of `line` that are intersected by `intersecting_line`.

    If a line segment is intersected multiple times, it is returned multiple times.
    """
    if not line.intersects(intersecting_line):
        return []
    if type(line) == MultiLineString:
        lines = line.geoms
    elif type(line) == LineString:
        lines = [line]
    else:
        raise TypeError("line is not a LineString or MultiLinestring")
    for single_line in lines:
        line_segments = [
            LineString([single_line.coords[i], single_line.coords[i+1]]) for i in range(len(single_line.coords) - 1)
        ]
        intersection = single_line.intersection(intersecting_line)
        intersection_points = intersection.geoms if type(intersection) == MultiPoint else [intersection]
        result = []
        for line_segment in line_segments:
            for point in intersection_points:
                if point.distance(line_segment) < 10e-9:
                    result.append(line_segment)
    return result


def is_left_of_line(point: Point, line: LineString) -> Union[bool, None]:
    """
    Is `point` to the left of `line`?

    Returns None if `point` intersects `line`

    Based on https://stackoverflow.com/questions/1560492/how-to-tell-whether-a-point-is-to-the-right-or-left-side-of-a-line

    :param point: the Point to analyse
    :param line: LineString with 2 vertices
    """
    assert len(line.coords) == 2
    if point.intersects(line):
        return None
    start, end = [Point(coord) for coord in line.coords]
    return ((end.x - start.x)*(point.y - start.y) - (end.y - start.y)*(point.x - start.x)) > 0


def flowline_start_nodes_left_of_line(flowlines: Lines, gauge_line: LineString):
    result = []
    for i in range(flowlines.count):
        line_coords = flowlines.line_coords[:, i]
        shapely_flowline = LineString(
            [
                Point((line_coords[0], line_coords[1])),
                Point((line_coords[2], line_coords[3]))
            ]
        )
        gauge_line_segments = intersected_segments(
            line=gauge_line,
            intersecting_line=shapely_flowline
        )
        if len(gauge_line_segments) == 0:
            continue
        elif len(gauge_line_segments) > 1:
            raise ValueError(f"Gauge line intersects flowline {flowlines.id[i]} multiple times")
        else:
            gauge_line_segment = gauge_line_segments[0]
        shapely_flowline_start_point = Point(flowlines.line_coords[0:2, i])
        result.append(is_left_of_line(shapely_flowline_start_point, gauge_line_segment))
    return result


def left_to_right_discharge(
        gr: GridH5ResultAdmin,
        gauge_line: LineString,
        start_time: float = None,
        end_time: float = None
) -> Tuple[Lines, np.array, float]:
    """
    Calculate the total net discharge from the left of a `gauge_line` to the right of that gauge line

    :returns: tuple of: Lines that intersect `gauge_line`,
    sum of net discharge per flowline in left -> right direction,
    total left -> right discharge
    """
    intersecting_lines = gr.lines.filter(line_coords__intersects_geometry=gauge_line)
    q_net_sum = time_aggregate(
        nodes_or_lines=intersecting_lines,
        start_time=start_time,
        end_time=end_time,
        aggregation=Q_NET_SUM
    )
    is_left_to_right = flowline_start_nodes_left_of_line(
        flowlines=intersecting_lines,
        gauge_line=gauge_line
    )
    direction = np.where(is_left_to_right, 1, -1)
    q_net_sum_left_to_right = q_net_sum * direction
    summed_vals = np.nansum(q_net_sum_left_to_right)

    return intersecting_lines, q_net_sum_left_to_right, summed_vals


# def discharge_smart_sum(
#         graph_3di: Graph3Di,
#         flowline_ids: List[int]
# ) -> Tuple[List[id], List[bool], List[float], float]:
#     """
#     Sum discharge through a list of flowlines, without double-counting water that flows multiple times through
#     different flowlines in that list.
#
#     Example: if the list is [1,2,3,4,5], and flowline 5 is upstream of flowline 2, flowline 2 is included in the sum,
#     but flowline 5 is not.
#
#     :returns: [flowline_ids], [is_included], [value], summed_values
#     """
#     upstream_side_flowline_nodes = graph_3di.flowlines_node_ids(flowline_ids=flowline_ids, upstream=True)
#     upstream_nodes = graph_3di.upstream_nodes(upstream_side_flowline_nodes)
#     upstream_flowline_ids = graph_3di.flowlines_between_nodes(upstream_nodes)
#     included_flowlines = set(flowline_ids) - set(upstream_flowline_ids)
#     ignored_flowlines = set(flowline_ids) - included_flowlines
#     included = graph_3di.get_aggregate_values(list(included_flowlines))
#     ignored = graph_3di.get_aggregate_values(list(ignored_flowlines))
#     summed_vals = np.nansum(included[:, 1])
#     ids = []
#     is_included = []
#     values = []
#     for id, val in included:
#         ids.append(id)
#         is_included.append(True)
#         values.append(val)
#     for id, val in ignored:
#         ids.append(id)
#         is_included.append(False)
#         values.append(val)
#
#     return ids, is_included, values, summed_vals
#
#
def left_to_right_discharge_ogr(
        gr: GridH5ResultAdmin,
        gauge_line: LineString,
        tgt_ds: ogr.DataSource,
        start_time: float = None,
        end_time: float = None,
        gauge_line_id: int = None
) -> float:
    """
    Calculate the total net discharge from the left of a `gauge_line` to the right of that gauge line

    Writes the flowlines with attribute 'q_net_sum' to provided `tgt_ds`

    :returns: total left -> right discharge
    """
    intersecting_lines, q_net_sum_left_to_right, summed_vals = left_to_right_discharge(
        gr=gr,
        gauge_line=gauge_line,
        start_time=start_time,
        end_time=end_time
    )
    gauge_line_ids = [gauge_line_id] * intersecting_lines.count
    attributes = {"gauge_line_id": gauge_line_ids, "q_net_sum": q_net_sum_left_to_right}
    attr_data_types = {"gauge_line_id": ogr.OFTInteger, "q_net_sum": ogr.OFTReal}
    threedigrid_to_ogr(
        threedigrid_src=intersecting_lines,
        tgt_ds=tgt_ds,
        attributes=attributes,
        attr_data_types=attr_data_types
    )
    return summed_vals


if __name__ == "__main__":
    DATA_DIR = Path("C:/Users/leendert.vanwolfswin/OneDrive - Nelen & Schuurmans/Documents 1/wayne/q_networkx_20220412")
    GPKG_DRIVER = ogr.GetDriverByName("GPKG")

    gridadmin = str(DATA_DIR / "gridadmin.h5")
    results_3di = str(DATA_DIR / "results_3di.nc")
    gauge_lines_fn = str(DATA_DIR / "lanyang2022_st61_line3826.shp")
    output_ds = GPKG_DRIVER.CreateDataSource(str(DATA_DIR / "test_out_32_5.gpkg"))

    gr = GridH5ResultAdmin(gridadmin, results_3di)
    print(gr.epsg_code)
    ogr_gauge_lines_ds = ogr.Open(gauge_lines_fn)
    ogr_gauge_lines_layer = ogr_gauge_lines_ds.GetLayer()
    feature = ogr_gauge_lines_layer.GetFeature(32)
    wkb_geom = feature.GetGeometryRef().ExportToWkb()
    shapely_linestring = wkb.loads(wkb_geom)

    print(
        left_to_right_discharge_ogr(gr=gr, gauge_line=shapely_linestring, tgt_ds=output_ds, gauge_line_id=32)
    )

    # graph_3di = Graph3Di(
    #     gr=gr,
    #     start_time=0,
    #     end_time=24*3600,  # real simulation duration is 72 h
    #     threshold=float(1)
    # )
    #
    # total_discharge = discharge_smart_sum_ogr(
    #     graph_3di=graph_3di,
    #     flowline_ids=list(intersecting_lines.id),
    #     tgt_ds=output_ds
    # )
    # print(total_discharge)

