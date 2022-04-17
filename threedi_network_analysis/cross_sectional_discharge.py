import numpy as np
from pathlib import Path
from typing import List, Tuple, Union

from osgeo import ogr

from shapely import wkb
from shapely.geometry import Point, LineString, MultiPoint
from threedigrid.admin.gridresultadmin import GridH5ResultAdmin

from threedigrid_networkx import Graph3Di
from threedi_result_aggregation.threedigrid_ogr import threedigrid_to_ogr

# Calculate the net cumulative flow through all flowlines in the model
# Make a directional Graph (NetworkX object) from this

# Select flowlines that intersect the gauge line
# It would be easier to implement this in pyqgis


def intersected_segments(line: LineString, intersecting_line: LineString) -> List[LineString]:
    """
    Returns the segments of `line` that are intersected by `intersecting_line`.

    If a line segment is intersected multiple times, it is returned multiple times.
    """
    if not line.intersects(intersecting_line):
        return []
    line_segments = [LineString([line.coords[i], line.coords[i+1]]) for i in range(len(line.coords) - 1)]
    intersection = line.intersection(intersecting_line)
    intersection_points = intersection.geoms if type(intersection) == MultiPoint else [intersection]
    result = []
    for line_segment in line_segments:
        for point in intersection_points:
            if point.intersects(line_segment):
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


def discharge_smart_sum(
        graph_3di: Graph3Di,
        flowline_ids: List[int]
) -> Tuple[List[id], List[bool], List[float], float]:
    """
    Sum discharge through a list of flowlines, without double-counting water that flows multiple times through
    different flowlines in that list.

    Example: if the list is [1,2,3,4,5], and flowline 5 is upstream of flowline 2, flowline 2 is included in the sum,
    but flowline 5 is not.

    :returns: [flowline_ids], [is_included], [value], summed_values
    """
    upstream_side_flowline_nodes = graph_3di.flowlines_node_ids(flowline_ids=flowline_ids, upstream=True)
    upstream_nodes = graph_3di.upstream_nodes(upstream_side_flowline_nodes)
    upstream_flowline_ids = graph_3di.flowlines_between_nodes(upstream_nodes)
    included_flowlines = set(flowline_ids) - set(upstream_flowline_ids)
    ignored_flowlines = set(flowline_ids) - included_flowlines
    included = graph_3di.get_aggregate_values(list(included_flowlines))
    ignored = graph_3di.get_aggregate_values(list(ignored_flowlines))
    summed_vals = np.nansum(included[:, 1])
    ids = []
    is_included = []
    values = []
    for id, val in included:
        ids.append(id)
        is_included.append(True)
        values.append(val)
    for id, val in ignored:
        ids.append(id)
        is_included.append(False)
        values.append(val)

    return ids, is_included, values, summed_vals


def discharge_smart_sum_ogr(
        graph_3di: Graph3Di,
        flowline_ids: List[int],
        tgt_ds: ogr.DataSource
) -> float:
    """
    Sum discharge through a list of flowlines, without double-counting water that flows multiple times through
    different flowlines in that list.

    Example: if the list is [1,2,3,4,5], and flowline 5 is upstream of flowline 2, flowline 2 is included in the sum,
    but flowline 5 is not.

    Writes the flowlines with attributes 'is_included' and 'value' to provided `tgt_ds`

    :returns: summed values
    """
    ids, is_included, values, summed_vals = discharge_smart_sum(graph_3di=graph_3di, flowline_ids=flowline_ids)
    lines = graph_3di.gr.lines.filter(id__in=ids)
    attributes = {
        "is_included": is_included,
        "value": values
    }
    attr_data_types = {
        "is_included": bool,
        "value": float
    }
    threedigrid_to_ogr(threedigrid_src=lines, tgt_ds=tgt_ds, attributes=attributes, attr_data_types=attr_data_types)
    return summed_vals


if __name__ == "__main__":
    DATA_DIR = Path("C:/Users/leendert.vanwolfswin/OneDrive - Nelen & Schuurmans/Documents 1/wayne/q_networkx_20220412")
    GPKG_DRIVER = ogr.GetDriverByName("GPKG")

    gridadmin = str(DATA_DIR / "gridadmin.h5")
    results_3di = str(DATA_DIR / "results_3di.nc")
    gauge_lines_fn = str(DATA_DIR / "lanyang2022_st61_line3826.shp")
    output_ds = GPKG_DRIVER.CreateDataSource(str(DATA_DIR / "test_out_32_1.gpkg"))

    gr = GridH5ResultAdmin(gridadmin, results_3di)

    # Do not draw a gauge line across two different streams that are flowing in opposite direction but not connected to each other
    ogr_gauge_lines_ds = ogr.Open(gauge_lines_fn)
    ogr_gauge_lines_layer = ogr_gauge_lines_ds.GetLayer()
    feature = ogr_gauge_lines_layer.GetFeature(32)
    wkb_geom = feature.GetGeometryRef().ExportToWkb()
    shapely_linestring = wkb.loads(wkb_geom)
    intersecting_lines = gr.lines.filter(line_coords__intersects_geometry=shapely_linestring).only('id')

    graph_3di = Graph3Di(
        gr=gr,
        start_time=0,
        end_time=24*3600,  # real simulation duration is 72 h
        threshold=float(1)
    )

    total_discharge = discharge_smart_sum_ogr(
        graph_3di=graph_3di,
        flowline_ids=list(intersecting_lines.id),
        tgt_ds=output_ds
    )
    print(total_discharge)

