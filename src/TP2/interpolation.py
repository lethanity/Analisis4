from sympy import *
import numpy
import pandas as pd

POINTS_FILE = "geo_pos.csv"
INTERPOLATED_POINTS_FILE = "geo_pos_interpolated.csv"
LAGRANGE_LIMIT = 10


def lagrange(points):
    """
    :param points: numpy 2-dimensional array [xi,yi]
    :return: a lambda expression that is the function
    """
    x = Symbol("x")
    l = zeros(1, points.shape[0])
    i = 0

    for p in points:
        numerator = 1
        denominator = 1
        j_points = numpy.delete(points, i, 0)  # remove the i point
        r = 0
        for j in j_points:
            r = r + 1
            if r > 60:  # avoid overflow
                numerator = horner(numerator)
                denominator = horner(denominator)
                r = 0
            numerator = numerator * (x - j[0])
            denominator = denominator * (p[0] - j[0])

        l[i] = numerator / denominator
        i = i + 1

    p = 0
    for i in range(len(points)):
        p = p + l.multiply(points[i, 1])[i]
    return lambdify(x, p, 'numpy')


def interpolate_file():
    data = pd.read_csv(POINTS_FILE)
    row_num = data.shape[0]
    interpolated_points = []
    for i in range(0, row_num, LAGRANGE_LIMIT - 1):
        sliced_data = data.iloc[i:i+LAGRANGE_LIMIT]
        latitude_by_height = numpy.column_stack((sliced_data.height, sliced_data.latitude))
        longitude_by_height = numpy.column_stack((sliced_data.height, sliced_data.longitude))
        first = sliced_data.height.iloc[0]
        if sliced_data.shape[0] < LAGRANGE_LIMIT:
            last = -1
        else:
            last = sliced_data.height.iloc[-1]
        lat_by_height_fun = lagrange(latitude_by_height)
        long_by_height_fun = lagrange(longitude_by_height)
        for height in range(first, last, -1):
            interpolated_points.append([height, lat_by_height_fun(height), long_by_height_fun(height)])
    return interpolated_points


def generate_interpolated_file():
    points = interpolate_file()
    with open(INTERPOLATED_POINTS_FILE, 'wb') as file:
        file.write(bytes("height,latitude,longitude\n", "UTF-8"))
        numpy.savetxt(file, points, delimiter=',')


def get_interpolated_points():
    return get_points(INTERPOLATED_POINTS_FILE)


def get_non_interpolated_points():
    return get_points(POINTS_FILE)


def get_points(path):
    return pd.read_csv(path).itertuples()


if __name__ == '__main__':
    generate_interpolated_file()
