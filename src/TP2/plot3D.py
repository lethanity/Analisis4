import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
'''
import csv 
def plot():  
        with open('geo_pos.csv', 'r') as csvfile:
            posreader = csv.reader(csvfile)
    
            x_list = []
            y_list = []
            z_list = []
    
            k = 0  # Counter to avoid row 0 (crappy, effective)
            for row in posreader:
                if k != 0:
                    x_list.append(row[1])
                    y_list.append(row[2])
                    z_list.append(row[0])
                k = k+1 '''


def plot(x_val, y_val, z_val):
    mpl.rcParams['legend.fontsize'] = 10

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x_val, y_val, z_val, label='Asteroid path')
    ax.legend()

    plt.show()
