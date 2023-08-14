import whitebox_workflows as wbw
import rasterio as rs
from rasterio.plot import show
import matplotlib.pyplot as plt

wbe = wbw.WbEnvironment()
wbe.verbose = False
wbe.working_directory = r'D:\PhD career\05 SCI papers\05 Lundtoftegade AKB\Lundtoftegade_optimization\00_data_source'

# web read DEM data
dem = wbe.read_raster('DEM_demo_d8.tif')

# slope analysis
basins = wbe.extract_streams(dem, threshold=83)
wbe.write_raster(basins, 'DEM_demo_basin.tif', compress=True)



# visualization
path_03 = '../00_data_source/DEM_demo_basin.tif'
data_03 = rs.open(path_03)

fig, ax = plt.subplots(figsize=(8, 8))
show(data_03, title='DEM_demo_basin', ax=ax)

plt.ticklabel_format(style='plain')
# ax.get_xaxis().get_major_formatter().set_scientific(False)  # 关闭科学计数法
# ax.get_yaxis().get_major_formatter().set_scientific(False)  # 关闭科学计数法
# grid and show plot
ax.grid(True,  linestyle='--', color='grey')
plt.show()


# value
'''Basin_value = []
for row in range(basins.configs.rows):
    for col in range(basins.configs.columns):
        elev = basins[row, col]
        if elev != basins.configs.nodata:
            Basin_value.append(elev)

# print(Slope_value)
print(max(Basin_value))
print(min(Basin_value))'''