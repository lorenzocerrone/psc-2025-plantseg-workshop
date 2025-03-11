import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


def plot_image(image: np.ndarray, title: str = "Image"):
    _, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.imshow(image, cmap='gray')
    ax.set_title(title)
    ax.axis('off')
    plt.show()
    
    
def plot_comparison(image1: np.ndarray, image2: np.ndarray, title1: str = "Image 1", title2: str = "Image 2"):
    _, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].imshow(image1, cmap='gray')
    ax[0].set_title(title1)
    ax[1].imshow(image2, cmap='gray')
    ax[1].set_title(title2)
    
    for _ax in ax:
        _ax.axis('off')
    plt.show()
    
    
def plot_label(image: np.ndarray, label: np.ndarray, title: str = "Label"):
    random_cmap = np.random.rand(1000, 3)
    random_cmap[0] = 0
    cmap = ListedColormap(random_cmap)
    
    _, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.imshow(image, cmap='gray')
    ax.imshow(label, alpha=0.5, cmap=cmap)
    ax.set_title(title)
    ax.axis('off')
    plt.show()