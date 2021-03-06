#José Alejandro V
# h = 0.1
import numpy as np
import math
import matplotlib.pyplot as plt
n = 50
a = 0
b = 5 # Este es propuesto
h = 0.1
x = np.linspace(a,b,n)
print(x,h)
y0 = 1

def fprima(x,y):
    return 2*x*y

def euler(h,x,y0):
    y = []
    y.append(y0)
    for i in range(1,len(x)):
        y.append(y[i-1] + h*fprima(x[i-1],y[i-1]))
    return y

y = euler(h,x,y0)
print(y)
plt.plot(x,y,'b')
print("La respuesta es:",y[15])