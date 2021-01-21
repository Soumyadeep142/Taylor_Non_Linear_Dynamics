from numpy import *
from matplotlib.pyplot import *

def input(r_values):
	def f(x):
		return	r*x*(1-x)
	a=0
	b=1
	h=0.01


	for r in r_values:
		xpoints=arange(a,b+h,h)
		xtpoints=[]
		for x in xpoints:
			x=f(x)
			xtpoints.append(x)
		plot(xpoints,xtpoints,label=r)
	plot(xpoints,xpoints,label='x vs x')
	legend(loc='best')
	xlabel('xt')
	ylabel('xt+1')
	grid()
	savefig('Fig: 12.35.pdf')
	show()
input([0.8,1.5,10/3])

