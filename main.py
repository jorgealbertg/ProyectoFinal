import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage

import kernel_sharpen 
import gaussian
import kernel_MexicanHat

Is = Image.open('Img.jpg');
I = Is.convert('L');
I = numpy.asarray(I);
I = I / 255.0;

kernel_sharpen.kernel_1(I,Is);
kernel_gaussian.gaussian(I,Is,15,15);
kernel_MexicanHat.calc_ker(I,Is,5,2);
