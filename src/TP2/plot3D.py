import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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


def plot_3d(x_val, y_val, z_val):
    mpl.rcParams['legend.fontsize'] = 10

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot(x_val, y_val, z_val, label='Asteroid path')
    ax.legend()

    plt.show()


def plot_2d(x_val, y_val, x_label, y_label, title):
    plt.plot(x_val, y_val)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


if __name__ == '__main__':
    plot_2d([1, 2, 3, 4, 5], [2, 3, 4, 5, 6], 'x', 'y', 'x+1')
