def next_x(x,y):
    return math.sqrt(10-x*y)

def next_y(x,y):
    return math.sqrt((57-y)/(3*x))

x0 = 1.5
y0 = 3.5

E = 0.01

for k in range(100):
    xi = next_x(x0, y0)
    yi = next_y(x0,y0)
    Ex = abs(x0-xi)
    Ey = abs(y0-yi)
    x0 = xi
    y0 = yi
    if Ex<E and Ey<E:
        break
        
print("La solucion es {0}".format((x0,y0)))
