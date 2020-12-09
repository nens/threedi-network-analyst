# 3Di Network Analyst
 Network Analysis for 3Di results

## Introduction
3Di Network Analyst is a QGIS Plugin that allows you to find what is upstream and downstream of any point or area in a [3Di](https://3diwatermanagement.com/) simulation result. Upstream or downstream elements include surface areas (2D cells), sewerage and open water system flow (1D flowlines) and impervious surfaces (0D inflow). If there is a significant net flow from the element to the target location, the element is included in the upstream result set; for the downstream area, this is based on flow from the target node(s) to the downstream elements. These connections may consist of any (combination of) type of flowline included in the model (pumplines and breaches are not yet implemented).

## Installation
Install the 3Di Modeller Interface or the 3Di Toolbox QGIS plugin first, [instructions here](https://docs.3di.lizard.net/d_qgis_plugin.html#modeller-interface)

Download threedi_network_analysis.zip from the [latest release](https://github.com/nens/threedi-network-analyst/releases).

In QGIS: Main Menu > Plugins > Manage and Install Plugins... > Install from ZIP.

After installation, you will find the plugin at Main Menu > Plugins > 3Di Network Analyst, or the X button in the toolbar.

### Known issues during installation
_ImportError_: 

This plugin depends on python libraries SciPy and NetworkX. These are included in full installs of QGIS (using the standalone installer or, through the OSGeo4W Network Installer, qgis-full / qgis-ltr-full). If you encounter any Python ImportErrors related to these packages, install them using `pip install scipy` / `pip install networkx` in the OSGeo4W shell.

## User manual
The tool has four sections. From top to bottom: Inputs, Settings, Target Nodes, and Outputs. This manual first describes the most basic use of the tool and explains how the advanced options in these sections can be used.

### Most basic use of the tool
* In the Inputs section, select a 'results_3di.nc' file as input for '3Di results NetCDF'.
* If the corresponding gridadmin.h5 file is located in the same folder, it will be found automatically.
* You may leave empty the input '3Di model sqlite'; this is an optional input.
* After selecting the inputs, the tool preprocesses your model results. This may take a few seconds (up to half a minute for very large models).
* When the preprocessing is finished, click the button 'Click on Canvas' in the Target Nodes section.
* Now click on a target node on the map canvas. The upstream cells, area and 1D connections will be added to the result layers.

### Inputs section
#### 3Di results NetCDF
Results of a 3Di simulation (results_3di.nc file). More information about this file type can be found in the [3Di documentation](https://docs.3di.lizard.net/c_results.html#data-format-results-3di-nc). Required input.

#### 3Di gridadmin file
Grid administration (gridadmin.h5) file. If this file is located in the same folder as the results_3di.nc file, it will be found automatically. Required input.

#### 3Di model sqlite (optional)
The 3Di model sqlite (.sqlite file) is an optional input, required only for visualizing which v2_impervious_surface features are upstream of the target node(s).

### Settings section
#### Threshold (m<sup>3</sup>)
Determines which flowlines are included in the network used for calculating upstream or downstream connectivity. Only flowlines that have a cumulative discharge above the threshold included. 

More specifically, the threshold applies to the _absolute net cumulative_ discharge. E.g., if the time window is 30 minutes (1800 s) and the discharge is -1.0 m<sup>3</sup>/s, the net cumulative discharge is 1800 m<sup>3</sup>. If flow direction changes during the simulation, the discharge may be -1.0 m<sup>3</sup>/s in the first 15 minutes (900 s) and 0.5 m<sup>3</sup>/s in the last 15 minutes, the absolute net cumulative discharge = abs(-900 + 450) = 450 m<sup>3</sup>

#### Start and end time (s)
This setting allows to analyse the flow during part of the simulation time instead of the full simulation time. 

Please note that if an area is marked as upstream or downstream of a node for the chosen time window, it does not mean that water can flow to that point within that time window. E.g. if you'd select the source of the Nile as target node and a time window of 10 minutes, there would still be a fully connected network of flowlines all the way down to the Mediterrean, but this does not mean that a drop of water can flow all that distance within ten minutes.

### Target Nodes section
Target nodes are the node(s) for which to compute the upstream and/or downstream cells, areas, flowlines and impervious surfaces. The tool allows you to select target nodes in three different ways.

#### Click on canvas
Click the 'Click on Canvas' button, then click on a target node on the map canvas. This works in a way comparable to the Identify tool. Using Click on Canvas, you will always select only one target node.

Please note that if you zoom in and click too far away from any target node, nothing will happen.

#### Catchment for selected nodes
First use the Select tool to select one or more target nodes, then click 'Catchment for selected nodes'.

Please note that if you have not selected any target nodes and click this button, nothing will happen.

#### Target nodes in polygons
Use this option to select target nodes based on their intersection with polygons in a layer of your choice. 
* Add the polygon layer to your QGIS project
* Select the layer in the dropdown menu below 'Target nodes in polygons'
* Click the button 'Catchment for Polygons'

If you want to perform the calculation for only a subset of the polygons in the polygon layer, first select the polygons you want to include in the analysis and check the box 'Selected polygons only'

### Outputs section
#### Upstream and downstream checkboxes
Control whether only upstream, only downstream or both types of cells/areas/flowlines/impervious surfaces are calculated by checking the upstream and/or downstream boxes.

#### Single cells checkbox
_This option is not yet implemented (always on)_. In addition to the catchments, the 'raw' single cells are included in the result set. The catchments are made from these single cells by dissolving them, removing the holes from the resulting polygons, and then smoothing them. This is more visually attractive, but the single cells are more precise.

#### Flow pattern checkbox
_This option is not yet implemented (always off)_. When implemented and switched on, arrows showing the flow pattern within the catchments will be included in the result set.

#### Browse result sets
If you have generated two or more result sets, it may be helpful to browse through them one by one. 
* Check the box 'Browse result sets'
* Use the spinbox up/down arrows to go from one result set to the next.

#### Clear results
If you want to delete the results you have generated so far, the button 'clear results' can be used (rather than deleting all features from all result layers).

## Algorithm
_TBD_
Please note: pumplines (pumping stations that pump from one location in the model to another) are not taken into account in the network analysis. 




