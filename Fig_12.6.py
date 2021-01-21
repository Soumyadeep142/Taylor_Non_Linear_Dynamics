from numpy import *
from matplotlib.pyplot import *

w=2*pi
w0=1.5*w
gamma=1.077
beta=w0/4

def f(r,t):
	phi=r[0]
	omega=r[1]
	fphi=omega
	fomega=gamma*(w0)**2*cos(w*t)-(w0)**2*sin(phi)-2*beta*fphi
	return array([fphi,fomega], float)

t_initial=0
t_final=16

N=5000
h=(t_final-t_initial)/N
phi_0=0
omega_0=0
tpoints=arange(t_initial,t_final,h)
phipoints=[]
r=array([phi_0,omega_0],float)

for t in tpoints:
	phipoints.append(r[0])
	k1=h*f(r,t)
	k2=h*f(r+0.5*k1,t+0.5*h)
	k3=h*f(r+0.5*k2,t+0.5*h)
	k4=h*f(r+k3,t+h)
	r+=(k1+2*k2+2*k3+k4)/6.0

plot(tpoints,phipoints)
grid()
xlabel('time')
ylabel(r'$\phi$')
title(r'$\gamma$=1.077',fontsize=15)
savefig('Fig: 12.6.pdf')
show()

