import pandas as pd
import numpy as np
from src.TP3.rungekutta import runge_kutta

OVEN_CONST = 0.25
STEP = 0.1


def newtons_cooling_law(r, tm):
    return lambda x, y: - r * (y - tm)


def get_env_temp(matrix, x, y):
    point_amt = 8
    acum = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i is not 0 and j is not 0:
                acum += matrix[x + i][y + j]
    return acum / point_amt


def temp_map_at(dataframe, ti, t):
    shape = dataframe.shape
    new_map = pd.DataFrame(np.zeros(shape))
    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            y_ti = dataframe[i][j]
            if i is 0 or i is shape[0] - 1 or \
               j is 0 or j is shape[1] - 1:
                new_map[i][j] = y_ti
            else:
                func = newtons_cooling_law(OVEN_CONST, get_env_temp(dataframe, i, j))
                new_map[i][j] = runge_kutta(ti, y_ti, STEP, t, func)
    return new_map


def make_csvs(initial, time_step, n):
    frame_i = initial
    ti = 0
    for i in range(1, n + 1):
        frame_i = temp_map_at(frame_i, ti, ti + time_step)
        ti += time_step
        frame_i.to_csv('csv/t{}.csv'.format(i), header=False, index=False)

if __name__ == '__main__':
    data = pd.read_csv('csv/t0.csv', header=None)
    make_csvs(data, 1, 10)