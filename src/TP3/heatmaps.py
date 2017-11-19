from matplotlib import pyplot as plt
import pandas as pd


def map_csv(path):
    data = pd.read_csv(path, header=None).as_matrix()
    plt.imshow(data, cmap='hot')
    plt.colorbar()


if __name__ == '__main__':
    for i in range(0, 11):
        map_csv('csv/t{}.csv'.format(i))
        plt.savefig('heatmap/t{}.png'.format(i))
        plt.clf()
