from TP2.interpolation import *
from TP2.plot import *


if __name__ == '__main__':
    points = get_interpolated_points()
    heights = []
    latitudes = []
    longitudes = []
    for point in points:
        heights.append(point.height)
        latitudes.append(point.latitude)
        longitudes.append(point.longitude)

    plot_2d(heights, longitudes, 'height', 'longitude')
    plot_2d(heights, latitudes, 'height', 'latitude')
    plot_3d(longitudes, latitudes, heights, 'longitude', 'latitude', 'height', 'Asteroid Path')