# 3Di Network Analyst
 Network Analysis for 3Di results

## Installation
Install the 3Di Modeller Interface or the 3Di Toolbox QGIS plugin first, [instructions here](https://docs.3di.lizard.net/d_qgis_plugin.html#modeller-interface)

Download threedi_network_analysis.zip from the [latest release](github.com/nens/threedi-network-analyst/releases).
In QGIS: Main Menu > Plugins > Manage and Install Plugins... > Install from ZIP

This plugin depends on python libraries SciPy and NetworkX. These are included in full installs of QGIS (using the standalone installer or, through the OSGeo4W Network Installer, qgis-full / qgis-ltr-full). If you encounter any Python ImportErrors related to these packages, install them using `pip install scipy` / `pip install networkx` in the OSGeo4W shell.
