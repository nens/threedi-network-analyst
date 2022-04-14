from pathlib import Path

from osgeo import ogr
from shapely.geometry import LineString
from shapely import wkb

from threedigrid_networkx import *

# Calculate the net cumulative flow through all flowlines in the model
# Make a directional Graph (NetworkX object) from this

# Select flowlines that intersect the gauge line
# It would be easier to implement this in pyqgis


def discharge_smart_sum(graph_3di: Graph3Di, flowline_ids: List[int]):
    """Sum discharge trough a set of flowlines, without double-counting water that flows through the same flowlines"""
    # Do not draw a gauge line across two different streams that are flowing in opposite direction but not connected to each other

    # For each selected flowline, find the upstream node id. I think this is super easy, as in the Graph, the flowline is called an 'edge', which is a tuple of two nodes. The first one is the upstream node, the second one the downstream.
    upstream_side_flowline_nodes = [flowline[0] for flowline in graph_3di.edges_by_flowline_id(flowline_ids=flowline_ids)]
    # print(f"upstream_side_flowline_nodes: {upstream_side_flowline_nodes}")

    # For each upstream node, find the 'ancestors' as it is called in NetworkX. These are the nodes upstream from that node
    upstream_nodes = graph_3di.upstream_nodes(upstream_side_flowline_nodes)
    # print(f"upstream_nodes: {upstream_nodes}")

    # List all flowlines (edges) that connect these upstream nodes
    upstream_flowline_ids = graph_3di.flowlines_between_nodes(upstream_nodes)
    # print(f"upstream_flowline_ids: {upstream_flowline_ids}")

    # select flowlines that are not upstream of other flowlines
    non_upstream_flowlines = list(set(flowline_ids) - set(upstream_flowline_ids))
    # print(f"non_upstream_flowlines: {non_upstream_flowlines}")

    ignored_flowlines = list(set(flowline_ids) - set(non_upstream_flowlines))
    # Sum up all net cumulative flow through the flowlines that intersect the gauge line, ignoring all flowlines in the list of upstream flowlines
    vals = graph_3di.get_aggregate_values(non_upstream_flowlines)[:, 1]
    # print(f"vals: {vals}")

    summed_vals = np.nansum(vals)

    result = {
        "included_flowlines": non_upstream_flowlines,
        "ignored_flowlines": ignored_flowlines,
        "total_discharge": summed_vals
    }

    return result


if __name__ == "__main__":
    DATA_DIR = Path("C:/Users/leendert.vanwolfswin/OneDrive - Nelen & Schuurmans/Documents 1/wayne/q_networkx_20220412")

    gridadmin = str(DATA_DIR / "gridadmin.h5")
    results_3di = str(DATA_DIR / "results_3di.nc")
    gauge_lines_fn = str(DATA_DIR / "lanyang2022_st61_line3826.shp")

    gr = GridH5ResultAdmin(gridadmin, results_3di)

    # The intersects_geometry expects a shapely geometry
    ogr_gauge_lines_ds = ogr.Open(gauge_lines_fn)
    ogr_gauge_lines_layer = ogr_gauge_lines_ds.GetLayer()
    feature = ogr_gauge_lines_layer.GetFeature(31)
    wkb_geom = feature.GetGeometryRef().ExportToWkb()
    shapely_linestring = wkb.loads(wkb_geom)
    print(shapely_linestring.wkt)
    intersecting_lines = gr.lines.filter(line_coords__intersects_geometry=shapely_linestring).only('id')
    print(intersecting_lines.id)

    graph_3di = Graph3Di(
        gr=gr,
        start_time=0,
        end_time=24*3600,  # real simulation duration is 72 h
        threshold=float(1)
    )

    print(discharge_smart_sum(graph_3di=graph_3di, flowline_ids=list(intersecting_lines.id)))

