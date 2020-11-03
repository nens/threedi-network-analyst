from zipfile import ZipFile
import os

ROOT_DIR_FILES = [
    '__init__.py',
    'icon.png',
    'metadata.txt',
    'ogr2qgis.py',
    'resources.py',
    'resources.qrc',
    'smoothing.py',
    'threedi_network_analysis.py',
    'threedi_network_analysis_dockwidget.py',
    'threedi_network_analysis_dockwidget_base.ui',
    'threedigrid_networkx.py'
]

DIRECTORIES = [
    'style',
    'threedi_result_aggregation'
]


def zipdir(path, ziph, path_in_zip):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            zip_file_path = os.path.join(path_in_zip, file_path )
            ziph.write(file_path, zip_file_path)


# create a ZipFile object
try:
    os.remove('threedi_network_analysis.zip')
except FileNotFoundError:
    pass
zip = ZipFile('threedi_network_analysis.zip', 'w')

# Files in root
for file in ROOT_DIR_FILES:
    zip.write(file, os.path.join('threedi_network_analysis', os.path.basename(file)))

# Folders in root
for directory in DIRECTORIES:
    zipdir(directory, zip, 'threedi_network_analysis')

# close the Zip File
zip.close()