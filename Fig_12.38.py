from numpy import *
from matplotlib.pyplot import *

r_values=[0.8,2.6]
def f(x):
	return	r*x*(1-x)
def g(x):
	return f(f(x))
a=0
b=1
h=0.01
Fig=['Fig 1.pdf', 'Fig 2.pdf']

for r in r_values:
	xpoints=arange(a,b+h,h)
	fpoints=[]
	gpoints=[]

	for x in xpoints:
		x=f(x)
		fpoints.append(x)
	plot(xpoints,fpoints,label='f(x)')
	title(('r={0}'.format(r)))
	for x in xpoints:
		x=g(x)
		gpoints.append(x)
	plot(xpoints,gpoints,label='g(x)')
	title(('r={0}'.format(r)))
	plot(xpoints,xpoints,label='x vs x')
	legend(loc='best')
	xlabel('xt')
	ylabel('xt+1')
	grid()
	savefig(('r={0}.pdf'.format(r)))
	show()


