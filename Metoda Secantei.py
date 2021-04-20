import numpy as np
import matplotlib.pyplot as plt
import sys


def Metoda_Secantei(f, x0, x1, eps, max_iter ):
    i=2
    y0=f(x0)
    y1=f(x1)
    while i<= max_iter:
        x_star=x1-y1*(x1-x0)/(y1-y0)
        if np.abs(x_star-x1)<eps:
            return x_star, i
        i+=1
        x0=x1
        x1=x_star
        y0=y1
        y1=f(x_star)
    print(f'Metoda secantei nu a atins convergenta dupa {i} iteratii')
    sys.exit(1)


def function(x):
    y=-x**3-2*np.cos(x)
    return y


def plot_function(interval, functions, points=None, title=None, fig_num=1):
    plt.figure(fig_num)  # Initializare figura
    x=np.linspace(start=interval[0], stop=interval[1])

    for element in functions:
        y=element[0](x)
        label_function=element[1]
        plt.plot(x, y, label=label_function)

    if points is not None:
        for point in points:
            plt.scatter(point[0], 0,label=point[1])



    plt.axhline(0, c='black')
    plt.axvline(0, c='black')
    plt.xlabel("points")
    plt.ylabel("values")
    plt.grid()
    plt.legend()
    if title is not None:
        plt.title(title)
    plt.show()

def ex_Metoda_Secantei():
    EPS=1e-5
    X0=-3.
    X1=3.
    Max_iter=1000
    x_num, steps=Metoda_Secantei(f=function, x0=X0, x1=X1, eps=EPS, max_iter=Max_iter)
    print(f'Prin Metoda Secantei s-a atins convergenta dupa {steps} iteratii in punctul {x_num}')
    plot_function( interval=[-3,3],
                   functions=[(function, 'f(x)' )],
                   points=[(x_num, 'x_aprox')],
                   title='Metoda Secantei'

    )










if __name__=='__main__':
    ex_Metoda_Secantei()


