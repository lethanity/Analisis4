import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_3d(x_val, y_val, z_val, x_label, y_label, z_label, line_label):
    mpl.rcParams['legend.fontsize'] = 10

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot(x_val, y_val, z_val, label=line_label)
    ax.legend()
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)
    plt.show()


def plot_2d(x_val, y_val, x_label, y_label):
    plt.plot(x_val, y_val)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
