import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


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
