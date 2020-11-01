import threedigrid
from threedigrid_networkx import *

ga = 'C:\\Users\\leendert.vanwolfswin\\Documents\\rotterdam\\v0247\\resultaat\\hoek van holland\\v0247_hoek_van_holland_rev2_100mm_2u\\gridadmin.h5'
res = 'C:\\Users\\leendert.vanwolfswin\\Documents\\rotterdam\\v0247\\resultaat\\hoek van holland\\v0247_hoek_van_holland_rev2_100mm_2u\\results_3di.nc'

gr = GridH5ResultAdmin(ga, res)

TARGET_AREA = Polygon([
    [109300.0, 518201.2], [108926.5, 518201.2], [108935.6, 517871.7], [109300.0, 518201.2]
])

result = catchment_from_node_ids(node_ids= [31627], gr=gr, threshold=10)
print('Done')
