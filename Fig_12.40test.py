from scipy import optimize
from numpy import *
from matplotlib.pyplot import *

a,b,h=0,5,0.01


def f(x):
	return (x-r*x*(1-x))
def g(x):
	return (x-f(f(x)))
def ff(x):
	return (1-r*(1-2*x))


roots=[]
r_values=arange(a,b+h,h)
guess=5
xspoints=[]
xdpoints=[]
rspoints=[]
rdpoints=[]
xpoints=[]
rpoints=[]
x_values=arange(0,1,0.001)
for r in r_values:
	#for x in x_values:
		#while round(x-f(x),3)==0:
	'''	
root=optimize.newton(f, guess, fprime=lambda x:1-r*(1-2*x))
			
	if abs(r*(1-2*root))<1: #stable points
		xspoints.append(root)
		rspoints.append(r)
	else:
		xdpoints.append(root)
		rdpoints.append(r)'''
	for x in x_values:
		if x!=0:
			if f(x)==0:
				xpoints.append(x)
				rpoints.append(r)
plot(rpoints,xpoints)
	
'''
			xpoints.append(x)
			rpoints.append(r)
scatter(rpoints,xpoints)
#while x=g(x):
show()
'''
'''
plot(rspoints,xspoints,color='black',linestyle='solid')
plot(rdpoints,xdpoints,color='black',linestyle='dashed')
xlabel('r')
ylabel('x*')
'''
savefig('Fig: 12.36.pdf')
show()

