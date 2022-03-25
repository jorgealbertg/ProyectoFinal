import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage
'''
Is = Image.open('Sample.png');
I = Is.convert('L');
I = numpy.asarray(I);
I = I / 255.0;
'''
def kernel_1(I, Is):
    k1 = numpy.array([[0,-1,0],[-1,7,-1],[0,-1,0]])

    J1 = ndimage.convolve(I, k1, mode='constant', cval=0.0)

    plt.figure(figsize = (20,20))

    plt.subplot(3,3,1)
    plt.imshow(Is)
    plt.xlabel('Input Image')

    plt.subplot(3,3,2)
    plt.imshow(J1)
    plt.xlabel('Sharpen filter')
    
    return k1
