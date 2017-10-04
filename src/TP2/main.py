from TP2.interpolation import *
from TP2.plot import *


if __name__ == '__main__':
    points = get_interpolated_points()
    heights = [float(point.height) for point in points]
    latitudes = [float(point.latitude) for point in points]
    longitudes = [float(point.longitude) for point in points]

    plot_3d(heights, longitudes, latitudes)
