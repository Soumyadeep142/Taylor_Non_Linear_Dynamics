from numpy import *
from matplotlib.pyplot import *

def f(r,x):
	return r*x*(1-x)

def bif_diagram(start,skip,iteration,step=0.001,r_min=0):
	R=[]
	X=[]
	r_values=arange(r_min,4,step)
	
	for r in r_values:
		x=start
		for i in range(skip+iteration+1):
			if i>=skip:
				R.append(r)
				X.append(x)
			x=f(r,x)
	plot(R,X,ls='',marker=',')
	xlabel('r')
	ylabel('x')
	savefig('Fig: 12.41.pdf')
	
	show()

bif_diagram(0.2,400,100)
