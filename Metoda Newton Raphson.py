import sys
import matplotlib.pyplot as plt
import numpy as np


def Newton_Raphson(f, df, x0, max_iter, eps):
    i=1
    while i<= max_iter:
        x1=x0- f(x0)/ df(x0)
        if np.abs(x1-x0) < eps:
            return x1, i
        x0=x1
        i+=1
    print(f'Metoda Newton_raphson nu a atins convergenta dupa {i-1} ietratii')
    sys.exit(1)

def function(x):
    y=-x**3-2*np.cos(x)
    return y


def dfunction(x):
    y=-3*x**2+2*np.sin(x)
    return y

def plot_function(interval, functions, fig_num=0, title=None, points=None):
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
    plt.ylabel("values")
    plt.xlabel("points")
    plt.grid()
    plt.legend()
    if title is not None:
         plt.title(title)

    plt.show()

def ex_NR():
    EPS=1e-5
    MAX_iter=1000
    X0=-3.
    x_num, steps=Newton_Raphson(f=function, df=dfunction, x0=X0, max_iter=MAX_iter, eps=EPS)
    print(f'Solutia ecuatiei f(x) = 0 cu metoda Newton-Raphson este x_sol = {x_num:.8f} gasita in N = {steps} pasi.')
    print('-' * 72)
    plot_function(interval=[-3, 3],
                  functions=[
                      (function, 'f(x)'),
                      (dfunction, 'df(x)')
                  ],
                  title='Metoda Newpton_raphson',
                  points=[(x_num, 'x_aprox')]

    )


if __name__=='__main__':
    ex_NR()





