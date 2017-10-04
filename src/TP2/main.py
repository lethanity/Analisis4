from TP2.interpolation import *
from TP2.plot import *


if __name__ == '__main__':
    points = get_interpolated_points()
    heights = [point.height for point in points]
    latitudes = [point.latitude for point in points]
    longitudes = [point.longitude for point in points]

    plot_2d(heights, longitudes, 'height', 'longitude')
    plot_2d(heights, latitudes, 'height', 'latitude')
    plot_3d(longitudes, latitudes, heights, 'longitude', 'latitude', 'height', 'Asteroid Path')
