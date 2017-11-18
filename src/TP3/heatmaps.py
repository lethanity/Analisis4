from matplotlib import pyplot as plt
import pandas as pd


def map_csv(path):
    data = pd.read_csv(path).as_matrix()
    data_norm = (data - data.mean()) / (data.max() - data.min()) # Normalize matrix
    heatmap = plt.imshow(data_norm, cmap='hot',interpolation='nearest')
    heatmap.show()

map_csv('csv/t1.csv')
