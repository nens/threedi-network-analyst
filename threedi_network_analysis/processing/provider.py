from qgis.core import QgsProcessingProvider
from threedi_network_analysis.processing.algorithms import CrossSectionalDischargeAlgorithm


class ThreeDiNetworkAnalysisProvider(QgsProcessingProvider):
    """Loads the Processing Toolbox algorithms"""
    def __init__(self):
        """
        Default constructor.
        """
        QgsProcessingProvider.__init__(self)

    def loadAlgorithms(self, *args, **kwargs):
        self.addAlgorithm(CrossSectionalDischargeAlgorithm())

    def id(self, *args, **kwargs):
        """The ID of your plugin, used for identifying the provider.

        This string should be a unique, short, character only string,
        eg "qgis" or "gdal". This string should not be localised.
        """
        return "threedi_network_analysis"

    def name(self, *args, **kwargs):
        """The human friendly name of your plugin in Processing.

          This string should be as short as possible (e.g. "Lastools", not
        "Lastools version 1.0.1 64-bit") and localised.
        """
        return self.tr("3Di Network Analysis")

    def icon(self):
        """Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        return QgsProcessingProvider.icon(self)