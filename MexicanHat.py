

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy import ndimage

# !gdown https://drive.google.com/uc?id=1cJ_XzTbiIKiuMCraz0ZSgGnByiOOxpYN

# !ls -ltr

Is = Image.open('sudoku.png');
I = Is.convert('L');
I = np.asarray(I);
I = I / 255.0;

def calc_ker(K, sigma, verbose=False):
    #Matriz de ceros
    KR = np.zeros((K,K))

    mitad = K // 2

    for x in range(K):
        for y in range(K):
            X = x - mitad
            Y = y - mitad

            KR[x][y] = (1/(np.pi*sigma**4)) * ((1-(1/2))*((X**2+Y**2)/sigma**2)) * np.exp( - ((X**2+Y**2)/(2*sigma**2)))
    
    plt.imshow(KR, interpolation='none',cmap='gray')
    plt.title("Kernel - Mexican Hat")
    plt.show()
    return KR


calc_ker(5,2)
