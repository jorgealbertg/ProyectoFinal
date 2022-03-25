# Entrega Final Semana tec

### Integantes
- Giuliana Sofia Islas Carbaja
- Jose Pablo Gonzalez Poblette
- Jorge Alberto Garcia Estudillo

# Objetivo

El objetivo de esta entrega es aplicar filtros a una imagen cualuiera mediante la implementacion de funciones kernel en python.

# Desarrollo
La mayoria de los filtros usan matriz de convolución. Con este filtro, se pueden personalizar de distintas formas. El filtro matriz de convolución usa una primera matriz que es la imagen que será tratada. La imagen es una colección bidimensional de píxeles en coordenada rectágular y el kernel usado dependerá del efecto deseado.
El filtro examina, sucesivamente, cada píxel de la imagen, para cada uno de ellos, que llamaremos “píxeles iniciales”, se multiplica el valor de este píxel y el valor de los 8 circundantes por el valor correspondiente del kernel. Entonces se añade el resultado, y el píxel inicial se regula en este valor resultante final.

Un ejemplo simple: 

![](https://drive.google.com/uc?id=1n7LrbggZCoIGxtJVRtNf3adKo4j0kEll)
A la izquierda, la imagen de la matriz: cada píxel está marcado con su valor. El píxel inicial tiene un borde rojo. El área de acción del kernel tiene un borde verde. En el medio, el kernel, y a la derecha, el resultado de convolución.

Para poder hacer la actividad, primero tuvimos que investigar que tipos de filtro kernel queriamos aplicar y con que ecuaciones se puede lograr. Posteriormente las implementamos en python y mediante un codigo main mandamos a llamar todas y asi desplegar las imagenes.

# Kernel 1
### Mexican Hat
Para el desarrollo de este kernel, se utiliza la ecuacion de Ricker Wavelet:
![](https://drive.google.com/uc?id=1cOwp_l9uLp3ITVvf6hAoy2vWqjQI9sbb)

La cual si la graficas nos da un efecto parecido al de un sombrero mexicano

![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/MexicanHatMathematica.svg/1200px-MexicanHatMathematica.svg.png)

Dicha ecacion la implementamos en una funcion en python y se la aplicamos a la imagen.

```python
def calc_ker(I, Is, K, sigma, verbose=False):
    #Matriz de ceros
    KR = np.zeros((K,K))

    mitad = K // 2

    for x in range(K):
        for y in range(K):
            X = x - mitad
            Y = y - mitad

            KR[x][y] = (1/(np.pi*sigma*4)) * ((1-(1/2))((X*2+Y2)/sigma2)) * np.exp( - ((X2+Y2)/(2*sigma*2)))
    
    J1 = ndimage.convolve(I, KR, mode='constant', cval=0.0)
    plt.figure(figsize = (20,20))

    plt.subplot(3,3,1)
    plt.imshow(Is)
    plt.xlabel('Input Image')

    plt.subplot(3,3,2)
    plt.imshow(J1)
    plt.xlabel('Mexican Hat filter')
    return KR
```
Imagen con filtro:
![](https://drive.google.com/uc?id=1a0dPkrE4EzmGNYDOzvCRP9uRm155evOt)

# Kernel 2
#### Gaussian Blur
En el procesamiento de imágenes, el “Gaussian Blur” es el resultado de desenfocar una imagen mediante una función gaussiana (llamada así por el matemático y científico Carl Friedrich Gauss).
Es un efecto muy utilizado en el software de gráficos, normalmente para reducir el ruido de la imagen y reducir los detalles. El efecto visual de esta técnica es un suave desenfoque que se asemeja al de ver la imagen a través de una pantalla translúcida.
El “Gaussian Blur” también se utiliza como etapa de preprocesamiento en los algoritmos de visión por ordenador para mejorar las estructuras de la imagen a diferentes escalas.


Ecuacion Gaussian Blur:
```python
$g(x,y) = \frac{1}{2\pi\sigma^2} e^{-\frac{x^2+y^2}{2\sigma^2}}$
```
Funcion de python:
```python
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
```
Imagen con filtro:

![](https://drive.google.com/uc?id=1ZFsQTEpm1bzw824ukytbrz5hPDTfYkL2)

# Kernel 3
#### Sharpen
“Sharpening” es otra de las operaciones de imagen más comunes. Esta técnica se utiliza para resaltar los detalles de una imagen mejorando el contraste de los píxeles en los bordes. El kernel puede construirse añadiendo la imagen de origen a la salida del detector de bordes, produciendo una imagen en la que los bordes son más aparentes. El efecto de nitidez puede controlarse introduciendo un parámetro de cantidad que escala la contribución:

Kernel:
![](https://drive.google.com/uc?id=1f-Z_yW2X-sWLGVfVOASuwnNl6s3CtBGB)

Funcion python:
```python
def gaussian(I, Is, sigma, size):
    A= numpy.zeros((size,size))
    
    for x in range(-size//2,size//2+1):
      for y in range (-size//2,size//2+1):
        A[x][y] = 1/(2*numpy.pi*sigma*2)(numpy.exp(-(x*2 + y2)/(2*sigma*2)))

    Ig = ndimage.convolve(I, A, mode='constant', cval=0.0)

    plt.figure(figsize = (15,15))

    plt.subplot(2,2,1)
    plt.imshow(Is)
    plt.xlabel('Input Image')

    plt.subplot(2,2,2)
    plt.imshow(Ig)
    plt.xlabel('Gaussian Blur Kernel')

    return A
```
Imagen con filtro:

![](https://drive.google.com/uc?id=1EjeemMzIzGKEA4KmOgAJ-eB0g_ruvGXi)
# Main
El codigo main es bastante simple, lo unico que hacemos es establecer una imagen a modificar y mandar a llamar los demas archivos donde estan las funciones con cada filtro . Ya por ultimo es le aplica  cada filtro a la imagen y se desplega.

Codigo main:
```python
import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage

import kernel_sharpen 
import gaussian
import kernel_MexicanHat

Is = Image.open('img.png');
I = Is.convert('L');
I = numpy.asarray(I);
I = I / 255.0;

kernel_sharpen.kernel_1(I,Is);
gaussian.gaussian(I,Is,15,15);
kernel_MexicanHat.calc_ker(I,Is,5,2);
```
# End

