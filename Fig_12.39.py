from numpy import *
from matplotlib.pyplot import *


def input(r_values):
	def f(x):
		return r*x*(1-x)
	def g(x):
		return f(f(x))
	a=0
	b=1
	h=0.01
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
		plot(xpoints,gpoints,label='g(x)',linestyle='dashed')
		title(('r={0}'.format(r)))
		plot(xpoints,xpoints,label='x vs x')
		legend(loc='best')
		xlabel('xt')
		ylabel('xt+1')
		grid()
		savefig(('r={0}.pdf'.format(r)))
		show()
input([2.8,3.0,3.4])


