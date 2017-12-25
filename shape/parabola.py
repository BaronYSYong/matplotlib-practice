import matplotlib.pyplot as plt
import decimal

def drange(x, y, jump):
    while x < y:
        yield float(x)
        x += decimal.Decimal(jump)

def parabola(a,b,c,x):
    y = []
    for i in x:
        y.append(a*pow(i,2)+b*i+c)
    return y



x = list(drange(-10,0.1,'0.1'))
print 'x', len(x)
y = parabola(1,10,-1,x)
print 'y', len(y)
plt.plot(x,y,'g')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
