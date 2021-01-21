from scipy import optimize
from numpy import *
from matplotlib.pyplot import *

a,b,h=0,5,0.01


def f(x):
	return (x-r*x*(1-x))
roots=[]
r_values=arange(a,b+h,h)
guess=[5,-5]

for guess in guess:
	xspoints=[]
	xdpoints=[]
	rspoints=[]
	rdpoints=[]
	for r in r_values:
		root=optimize.newton(f, guess, fprime=lambda x:1-r*(1-2*x))
		if abs(r*(1-2*root))<1: #stable points
			xspoints.append(root)
			rspoints.append(r)
		else:
			xdpoints.append(root)
			rdpoints.append(r)
	plot(rspoints,xspoints,color='black',linestyle='solid')
	plot(rdpoints,xdpoints,color='black',linestyle='dashed')
xlabel('r')
ylabel('x*')
ylim(0,1)
savefig('Fig: 12.36.pdf')
show()

