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
### Sections
The tool has four sections. From top to bottom: Inputs, Settings, Target Nodes, and Outputs. This manual first describes the most basic use of the tool and explains how the advanced options in these sections can be used.

### Most basic use of the tool
* In the Inputs section, select a 'results_3di.nc' file as input for '3Di results NetCDF'.
* If the corresponding gridadmin.h5 file is located in the same folder, it will automatically be found
* You may leave the 3Di model sqlite input empty, this is an optional input
* After selecting the inputs, the tool preprocesses your model results. This may take a few seconds (up to half a minute for very large models).
* When the preprocessing is finished, click the button 'Click on Canvas' in the Target Nodes section.
* Now click on a target node on the map canvas. The upstream cells, area and 1D connections will be added to the result layers.

### Inputs section
#### 3Di results NetCDF
#### 3Di gridadmin file
#### 3Di model sqlite (optional)
### Settings section
#### Threshold (m3)
#### Start and end time (s)

### Target Nodes section
This section offers you three different ways to select the target nodes for which to compute the upstream and downstream areas.

#### Click on canvas
#### Catchment for selected nodes
#### Target nodes in polygons
### Outputs section
#### Upstream and downstream checkboxes
#### Single cells checkbox
#### Flow pattern checkbox
#### Browse result sets
#### Clear results







