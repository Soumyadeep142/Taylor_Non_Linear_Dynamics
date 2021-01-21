from numpy import *
from matplotlib.pyplot import *
a,b,h=0,30,1

tpoints=arange(a,b+h,h)
r=3.2

def f(x):
	return	r*x*(1-x)

x=0.1
xpoints=[]
for t in tpoints:
	xpoints.append(x)
	x=f(x)
plot(tpoints,xpoints,color='red')
scatter(tpoints,xpoints,color='black')
title(('r={0}'.format(r)))
grid(color='blue')
xlabel('t')
ylabel('xt')
savefig('Fig: 12.37.pdf')

show()

