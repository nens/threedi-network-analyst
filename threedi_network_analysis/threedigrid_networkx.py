# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 12:14:14 2020

@author: leendert.vanwolfswinkel

Network analysis for 3Di
3Di models and results are networks that can be analysed using generic network analysis algorithms. 
This notebook uses network analysis to determine the areas that contribute to water accumulation in the model.

README:
    For many purposes it is more interesting to analyse the results as a directed network,\
        where the directions of the edges are determined by the mean velocity. 
        In this case we use the mean velocity with a threshold value.
     
        Because the network is directional, 
        all velocities are positive. 
        We first add all positive velocities,
        then we take the negative velocities, 
        flip the node pairs and then add them to the Network model.

"""

# System imports
import os

# Grid imports
# from threedigrid.admin.gridresultadmin import GridH5ResultAdmin
# from threedigrid.admin.gridadmin import GridH5Admin

# Third-party imports
from threedigrid.admin.gridresultadmin import GridH5ResultAdmin

import ogr
import numpy as np
import networkx as nx
from shapely.geometry import Polygon
from shapely import wkb

# Local imports
try:
    from threedi_result_aggregation import *
except ImportError:
    from .threedi_result_aggregation import *

Q_NET_SUM = Aggregation(variable=AGGREGATION_VARIABLES.get_by_short_name('q'),
                        method=AGGREGATION_METHODS.get_by_short_name('sum'),
                        sign=AggregationSign('net', 'Net')
                        )

ogr.UseExceptions()


class Graph3Di:
    def __init__(self,
                 gr: GridH5ResultAdmin = None,
                 subset: str = None,
                 start_time: int = None,
                 end_time: int = None,
                 aggregation: Aggregation = Q_NET_SUM,
                 threshold: float = 0):
        self._gr = gr
        self._subset = subset
        self._start_time = start_time
        self._end_time = end_time
        self._aggregation = aggregation
        self._threshold = threshold
        self._aggregate = None
        self._graph = None
        self.calculate_aggregate()
        self.update_graph()

    @property
    def gr(self):
        return self._gr

    @gr.setter
    def gr(self, gr):
        if not isinstance(gr, GridH5ResultAdmin):
            raise TypeError
        self._gr = gr
        self.calculate_aggregate()
        self.update_graph()

    @property
    def subset(self):
        return self._subset

    @subset.setter
    def subset(self, subset):
        if not (isinstance(subset, str) or subset is None):
            raise TypeError
        self._subset = subset
        self.calculate_aggregate()
        self.update_graph()

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        if start_time is None:
            self._start_time = None
        else:
            self._start_time = int(start_time)
        self.calculate_aggregate()
        self.update_graph()

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        if end_time is None:
            self._end_time = None
        else:
            self._end_time = int(end_time)
        self.calculate_aggregate()
        self.update_graph()

    @property
    def aggregation(self):
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        self._aggregation = aggregation
        self.calculate_aggregate()
        self.update_graph()

    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        if isinstance(threshold, float) or threshold is None:
            self._threshold = threshold
        self.update_graph()

    @property
    def lines_subset(self):
        if self.subset is None:
            return self.gr.lines
        else:
            return self.gr.lines.subset(self.subset)

    @property
    def aggregate(self):
        return self._aggregate

    @property
    def graph(self):
        return self._graph

    @property
    def isready(self):
        return isinstance(self.graph, nx.MultiDiGraph)

    def calculate_aggregate(self):
        """Calculate the aggregate with current attributes"""
        # Split from update_graph because this is not necessary when just the threshold changes
        if isinstance(self.gr, GridH5ResultAdmin) \
                and isinstance(self.start_time, int) \
                and isinstance(self.end_time, int) \
                and isinstance(self.aggregation, Aggregation):
            self._aggregate = time_aggregate(nodes_or_lines=self.lines_subset,
                                             start_time=self.start_time,
                                             end_time=self.end_time,
                                             aggregation=self.aggregation)
            self._graph = None  # to prevent a mismatch between aggregate and graph

        else:
            print('calculate aggregate not performed')
            print(f'gr type: {type(self.gr)}')
            print(f'start time = {self.start_time} type: {type(self.start_time)}')
            print(f'end time = {self.end_time} type: {type(self.end_time)}')
            print(f'aggregation type: {type(self.aggregate)}')

    def update_graph(self):
        """Create NetworkX MultiDiGraph object if necessary properties have valid values"""
        if isinstance(self.aggregate, np.ndarray) \
                and isinstance(self.threshold, float) \
                and isinstance(self.gr, GridH5ResultAdmin):
            # Get flowlines with positive flow
            pos_mask = np.squeeze(self.aggregate > self.threshold)
            pos_flows = self.lines_subset.line.T[pos_mask]
            pos_flows_ids = list(self.lines_subset.id.T[pos_mask])

            # Get flowlines with negative flow
            neg_mask = np.squeeze(self.aggregate < -1 * self.threshold)
            neg_flows = self.lines_subset.line.T[neg_mask]
            neg_flows_flipped = np.fliplr(neg_flows)
            # now negative flows have become positive flows, because node pairs are flipped
            neg_flows_ids = list(self.lines_subset.id.T[neg_mask])

            # read the threedi result into a directional MultiDiGraph based on the filtering above
            self._graph = nx.MultiDiGraph()
            edges = []
            flows = list(map(tuple, pos_flows))
            flows += list(map(tuple, neg_flows_flipped))
            ids = pos_flows_ids + neg_flows_ids
            for i, line in enumerate(flows):
                edges.append((line[0], line[1], {'id': ids[i]}))

            self._graph.add_edges_from(edges)

    def _upstream_or_downstream_nodes(self, target_node_ids, upstream: bool):
        result_node_ids = set()
        for id_i in target_node_ids:
            if id_i in self.graph.nodes:
                if upstream:
                    result_node_ids_i = nx.ancestors(self.graph, id_i)
                else:
                    result_node_ids_i = nx.descendants(self.graph, id_i)
                result_node_ids.update(result_node_ids_i)
        return result_node_ids

    def upstream_nodes(self, target_node_ids):
        """
        Calculate the upstream area(s) of a set of nodes in a 3Di result

        :param target_node_ids: catchment pour point node id's (iterable of integers)
        :returns: ids of the upstream nodes
        :rtype: set
        """
        return self._upstream_or_downstream_nodes(target_node_ids=target_node_ids, upstream=True)

    def downstream_nodes(self, target_node_ids):
        """
        Calculate the downstream area(s) of a set of nodes in a 3Di result

        :param target_node_ids: catchment pour point node id's (iterable of integers)
        :returns: ids of the upstream nodes
        :rtype: set
        """
        return self._upstream_or_downstream_nodes(target_node_ids=target_node_ids, upstream=False)

    def flowlines_between_nodes(self, node_ids):
        """Return list of flowline ids that connect the input nodes"""
        edges = self.graph.subgraph(nodes=node_ids).edges.data('id')
        flowline_ids = [edge[2] for edge in edges]
        return flowline_ids

    def _upstream_or_downstream_flowlines(self, target_node_ids, upstream: bool):
        nodes = self._upstream_or_downstream_nodes(target_node_ids=target_node_ids, upstream=upstream)
        nodes.update(set(target_node_ids))
        return self.flowlines_between_nodes(nodes)

    def upstream_flowlines(self, target_node_ids):
        return self._upstream_or_downstream_flowlines(target_node_ids=target_node_ids, upstream=True)

    def downstream_flowlines(self, target_node_ids):
        return self._upstream_or_downstream_flowlines(target_node_ids=target_node_ids, upstream=False)

    def cells_as_multipolygon(self, cell_ids: set):
        """Dissolve cells to multipolygon

        WARNING! May result in memory error if somehwat large set of cells is given as input
        """
        upstream_cells = self._gr.cells.filter(id__in=list(cell_ids))
        cell_drv = ogr.GetDriverByName('MEMORY')
        cell_ds = cell_drv.CreateDataSource('')
        threedigrid_to_ogr(threedigrid_src=upstream_cells,
                           tgt_ds=cell_ds,
                           attributes={},
                           attr_data_types={}
                           )
        cell_layer = cell_ds.GetLayerByName('cell')
        cells_multipolygon = ogr.Geometry(ogr.wkbMultiPolygon)
        for cell in cell_layer:
            cells_multipolygon.AddGeometry(cell.GetGeometryRef())

        result = cells_multipolygon.UnionCascaded()

        return result


if __name__ == "__main__":
    pass

# def catchment_from_polygon(target_area: ogr.Geometry,
#                            gr: GridH5ResultAdmin,
#                            threshold=0.01,
#                            first_ts=0,
#                            last_ts=14400,
#                            quiet=True):
#     # get node ids from ids
#     # The intersects_geometry expects a shapely geometry for which the intersection will be determined:
#
#     target_area_shapely = wkb.loads(target_area.ExportToWkb())
#     ids = gr.cells.filter(cell_coords__intersects_geometry=target_area_shapely).id
#
#     return catchment_from_node_ids(node_ids=ids,
#                                    gr=gr,
#                                    threshold=threshold,
#                                    first_ts=first_ts,
#                                    last_ts=last_ts,
#                                    quiet=quiet
#                                    )
