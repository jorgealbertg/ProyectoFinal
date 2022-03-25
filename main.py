import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage

import kernel_sharpen 
import kernel_gaussian
import kernel_MexicanHat

Is = Image.open('Img.png');
I = Is.convert('L');
I = numpy.asarray(I);
I = I / 255.0;

kernel_sharpen.kernel_1(I,Is);
kernel_gaussian.kernel_gaussian(I,Is);
kernel_MexicanHat.kernel_MexicanHat(I,Is);