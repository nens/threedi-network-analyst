# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 12:14:14 2020

@author: ivar.lokhorst
@edits: chris.kerklaan

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
#from threedigrid.admin.gridresultadmin import GridH5ResultAdmin
#from threedigrid.admin.gridadmin import GridH5Admin

# Third-party imports
import ogr
import numpy as np
import networkx as nx

# Local imports
from base.gis.vector import Vector, create_mem_layer

    
def sources(areas, gridh5admin, gridh5resultsadmin,  
            statistic='velocity',threshold = 0.01,
            first_ts=0, last_ts=14400,
             quiet=True):
    """
    Drainage areas calculates the drainage areas of polygons within a Threedi
    model.
    
    It either uses the average velocity or the summed discharge.
    
    Note: It uses only 2d lines, not 1d
    
    Parameters
    ----------
    areas_path : Vector object
        File in which is defined for what areas the source is calculated
    gridh5admin : threedigrid.admin.gridadmin
    gridh5resultsadmin : threedigrid.admin.gridresultadmin
    statistic : TYPE, optional
        Can be discharge (m3/s) or velocity (m/s).
    threshold : TYPE, optional
        Everything below this treshold is not taken into account. The default is 0.01. Unit is dependent on the statistic
    result_path : TYPE, optional
        The default is "source_areas.shp".
    first_ts : TYPE, optional
        Timestep filtering in model. The default is 0.
    last_ts : TYPE, optional
        Timestep filtering in model. The default is 14400.

    Returns
    -------
    In memory Vector object target_node_layer, coupled to areas with their feature id.

    """
    
    if not quiet:
        print('Starting sources derivation')

    ga = gridh5admin
    gr = gridh5resultsadmin
    
    # Get timeseries and lines velocity from netcdf
    lines_subset = gr.lines.subset("2d_all").timeseries(
        start_time=first_ts, end_time=last_ts
    )
    
    if statistic == 'velocity':
        lines_subset = lines_subset.u1
        
        # Get mean velocity of each line over each timestep
        mean_line = np.nanmean(lines_subset, axis=0)

        
    elif statistic == 'discharge':
        lines_subset = lines_subset.q
        
        # Get mean velocity of each line over each timestep
        mean_line = np.nansum(lines_subset, axis=0)

    # Make mask array to be able to select positive flows
    pos_mask = np.squeeze(mean_line > threshold)

    # Apply that mask to the lines, get all links with positive velocity
    pos_flows = ga.lines.subset("2d_all").line.T[pos_mask]

    # Negative flows get a similar treatment...
    neg_mask = np.squeeze(mean_line < -1 * threshold)
    
    # note that pos_mask nor neg_mask include flows that are 0 !
    neg_flows = ga.lines.subset("2d_all").line.T[neg_mask]

    # .. except we flip the pairs
    neg_flows_flipped = np.fliplr(neg_flows)

    # read the threedi result into a directional MultiDiGraph based on the filtering above
    G = nx.MultiDiGraph()
    G.add_edges_from(list(map(tuple, pos_flows)))
    G.add_edges_from(list(map(tuple, neg_flows_flipped)))
    if not quiet:
        print("3Di result is now a NetworkX MultiDiGraph.")
        print("number of nodes: " + str(G.number_of_nodes()))

    # Raw filtering of subset to bbox of geometry
    node_ids_in_bb = []
    for area in areas:
        minx, maxx, miny, maxy = area.geometry().GetEnvelope()
        node_ids_in_bb.extend(
            ga.nodes.filter(coordinates__in_bbox=[minx, miny, maxx, maxy]).id
        )
    ga.nodes.subset("2d_all").filter(id__in=node_ids_in_bb).reproject_to(
        "28992"
    ).to_shape("/vsimem/nodes_ruw.shp")

    # Smooth filtering to geomery
    nodes_in_bb = Vector("/vsimem/nodes_ruw.shp", index=True)
    knelpunt_nodes = {}
    for area in areas:
        fids = nodes_in_bb.within(area.geometry())
        ids = [nodes_in_bb[fid]['nod_id'] for fid in fids]
        knelpunt_nodes[area.GetFID()] = ids

    # Derive contributing areas
    contributing_area = {key: [] for key, value in knelpunt_nodes.items()}
    for key, value in knelpunt_nodes.items():
        for value in knelpunt_nodes[key]:
            if value in G.nodes:
                contributing_area[key].append(list((nx.ancestors(G, value))))

    # remove duplicate nodes from contributing area dictionary
    for key, value in contributing_area.items():
        contributing_area[key] = sum(contributing_area[key], [])
        contributing_area[key] = list(dict.fromkeys(contributing_area[key]))

    # create output file
    output = Vector(create_mem_layer("", ogr.wkbMultiPolygon, 28992))
    output.add_field("id", ogr.OFTInteger)
    
    # loop over the contributing nodes per feature that's analyzed
    for key, value in contributing_area.items():
        if len(contributing_area[key]) != 0:
            dataset = ga.cells.subset("2d_all").filter(id__in=value)
            dataset.reproject_to("28992").to_shape("/vsimem/cells.shp")
            cell = Vector("/vsimem/cells.shp")
            for c in cell:
                geom = c.geometry()           
                output.add_feature(geom, {"id": int(key)})  
            cell.close()
    output.dissolve(field='id')
            

    if not quiet:
        print('generating final output')
    
    return output



if __name__ == "__main__":
    pass
    # os.chdir("C:/Users/chris.kerklaan/Documents/Projecten/IJburg")

    # areas = Vector("data/wadis.shp")

    # ga = GridH5Admin("results/v0105_realistisch_custom/gridadmin.h5")
    # gr = GridH5ResultAdmin(
    #     "results/v0105_realistisch_custom/gridadmin.h5",
    #     "results/v0105_realistisch_custom/results_3di.nc",
    # )
    
    
    
    # thresholds = [0.000001, 0.00001, 0.0001, 0.001, 0.01]
    # for threshold in thresholds:
    #     s = sources(areas, ga, gr, 
    #              statistic='discharge',
    #              first_ts=0, 
    #              last_ts=14400,
    #              threshold = threshold # m3/s 
    #              )
    
    #     s.write('discharge_{}.shp'.format(threshold))
    
    #     s =  sources(areas, ga, gr, 
    #                  statistic='velocity',
    #                  first_ts=0, 
    #                  last_ts=14400,
    #                  threshold = threshold# m/s
    #                  )
        
    #     s.write('velocity_{}.shp'.format(threshold))
    
    
    
    