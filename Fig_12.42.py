from numpy import *
from matplotlib.pyplot import *

def f(r,x):
	return r*x*(1-x)

def eq(start,r,iteration,fig):
	x=start
	xt=[]
	T=[]
	t=0
	for i in range(iteration):
		xt.append(x)
		T.append(t)
		t+=1
		x=f(r,x)

	plot(T,xt)
	scatter(T,xt,color='black')
	xlabel('time')
	ylabel('xt')
	xlim(100,120)
	title('r={0}'.format(r))
	grid()
	savefig(fig)
	show()

eq(0.2,3.5,120,'fig 1.pdf')
eq(0.2,3.84,120,'fig 2.pdf')
