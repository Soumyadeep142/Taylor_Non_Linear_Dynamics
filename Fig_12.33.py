from numpy import *
from matplotlib.pyplot import *

#J-shaped graph
r=2
n0=4#initial population
n=n0
def f(n):
	return	r*n

t_ini=0
t_final=8
h=1
tpoints=arange(t_ini,t_final+h,h)
npoints=[]
for t in tpoints:
	npoints.append(n)
	n=f(n)
plot(tpoints,npoints,label='J-shaped curve',color='green')
scatter(tpoints,npoints,color='black')
xlabel('years')
ylabel('population')


#S-shaped graph
n=n0
N=1000
def g(n):
	return	r*n*(1-n/N)

t_ini=0
t_final=14
h=1
tpoints=arange(t_ini,t_final+h,h)
npoints=[]
for t in tpoints:
	npoints.append(n)
	n=g(n)
plot(tpoints,npoints,label='S-shaped curve', color='red')
scatter(tpoints,npoints,color='black')
legend(loc='best')

grid()
title('Exponential and Logistic Growth')
savefig('Fig: 12.33.pdf')
show()
