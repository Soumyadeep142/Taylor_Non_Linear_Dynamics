from numpy import *
from matplotlib.pyplot import *

def f(r,x):
	return r*x*(1-x)

def bif_diagram(start,skip,iteration,step=0.0001,r_min=0):
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
	plot(R,X,ls='',marker=',',color='black')
	xlabel('r')
	ylabel('x')
	xlim(3.84,3.855)
	ylim(0.45,0.55)
	savefig('Fig: 12.44.pdf')
	
	show()

bif_diagram(0.2,2000,1000,r_min=3.84)
