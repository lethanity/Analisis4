from TP2.interpolation import *
from TP2.plot import *


if __name__ == '__main__':
    points = list(get_interpolated_points())
    _, heights, latitudes, longitudes = zip(*points)  # python overload

    plot_2d(heights, longitudes, 'height', 'longitude')
    plot_2d(heights, latitudes, 'height', 'latitude')
    plot_3d(longitudes, latitudes, heights, 'longitude', 'latitude', 'height', 'Asteroid Path')