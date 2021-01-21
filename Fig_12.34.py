from numpy import *
from matplotlib.pyplot import *


r_values=[0.8,1.5]
x_values=[0.5,0.1]

def f(x):
	return	r*x*(1-x)

t_initial=0
t_final=20
h=1
tpoints=arange(t_initial,t_final+h,h)
for r in r_values:
	for x in x_values:
		xpoints=[]
		for t in tpoints:
			xpoints.append(x)
			x=f(x)
		plot(tpoints,xpoints)
		scatter(tpoints,xpoints,color='black')
		title(('r={0}'.format(r)))
	grid(color='green')
	savefig('r={}.pdf'.format(r))
	xlabel('t')
	ylabel('x')
	show()
	

