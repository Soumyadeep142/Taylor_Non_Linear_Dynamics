from numpy import *
from matplotlib.pyplot import *


a,b,h=0,600,1
c,d,f=0,4,0.001
tpoints=arange(a,b+h,h)
r_values=arange(c,d+f,f)
def f(x):
	return	r*x*(1-x)

xtpoints=[]
rpoints=[]
xt1points=[]
xt2points=[]
r1points=[]
for r in r_values:
	x=0.0001
	xpoints=[]
	for t in tpoints:
		xpoints.append(x)
		x=f(x)
	for n in range(500,600):
		if xpoints[n-1]==xpoints[n]:
			xtpoints.append(xpoints[n])
			rpoints.append(r)
		elif xpoints[n-2]==xpoints[n]:
			xt1points.append(xpoints[n])
			xt2points.append(xpoints[n-1])
			r1points.append(r)
			if len(xt1points)>1:
				if xt1points[-1]<xt1points[-2]:
					xt1points[-1],xt2points[-1]=xt2points[-1],xt1points[-1]
		
			
	
plot(rpoints,xtpoints,color='red')
plot(r1points,xt1points,color='red')
plot(r1points,xt2points,color='red')
xlabel('r')
ylabel('x')
savefig('Fig: 12.40.pdf')
show()

