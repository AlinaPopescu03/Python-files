import sys
import numpy as np
import matplotlib.pyplot as plt


def Metoda_Pozitiei_False(f, x0, x1, eps, max_iter):
    i=2
    y0=f(x0)
    y1=f(x1)
    while i <= max_iter:
        x_star=x1-(x1-x0)/(y1-y0)
        if np.abs(x_star-x1)<eps:
            return x_star, i
    i+=1
    y_star=f(x_star)
    if y_star*y1 <0:
        x0=x1
        y0=y1
    x1=x_star
    y1=y_star

    print(f'Metoda Pozitiei false nu a atins convergenta dupa {i} iteratii')
    sys.exit(1)


def function(x):
    y=-x**3-2*np.cos(x)
    return y


def plot_function(interval, function, points=None, title=None, fig_num=3):
    plt.figure(fig_num)
    x=np.linspace(start=interval[0], stop=interval[1])

    for element in functions:
        y=element[0](x)
        label_table=element[1]
        plt.plot(x, y, label=label_table)

    if points is not None:
        for point in points:
            plt.scatter(point[0], 0, label=point[1])

    plt.axhline(0, c='black')
    plt.axvline(0, c='black')
    plt.xlabel('points')
    plt.ylabel('values')
    plt.grid()


    if title is not None:
        plt.title(title)

    plt.show()

def ex_Metoda_Pozitiei_False():
    EPS=1e-5
    X0=-3.
    X1=3.
    MAX_ITER=1000
    x_num, steps=Metoda_Pozitiei_False(f=function, x0=X0, x1=X1, eps=EPS, max_iter=MAX_ITER)
    print(f'Metoda Pozitiei false a atins convergenta in punctul {x_num} dupa {i} iteratii')
    print('-----------------------------------------')
    plot_function(interval=[-3,3],
                  functions=[(function, 'f(x)')],
                  points=[(x_num, 'X_aprox')],
                  title='Metoda Pozitiei False'


    )



if __name__=='__main__':
    ex_Metoda_Pozitiei_False()
