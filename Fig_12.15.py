from numpy import *
from matplotlib.pyplot import *

w=2*pi
w0=1.5*w
gamma=1.503
beta=w0/4

def f(r,t):
	phi=r[0]
	omega=r[1]
	fphi=omega
	fomega=gamma*(w0)**2*cos(w*t)-(w0)**2*sin(phi)-2*beta*fphi
	return array([fphi,fomega], float)

t_initial=0
t_final=25

N=5000
h=(t_final-t_initial)/N
phi_0=-pi/2
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
ylabel(r'$\phi(t)$')
title(r'$\gamma$={0}'.format(gamma),fontsize=15)
t=-25*pi
d=-25
ticks=[]
labels=[]
while t<=max(phipoints):
	ticks.append(t)
	labels.append("{0} $\pi$".format(d))
	t+=5*pi
	d+=5
yticks(ticks,labels)
savefig('Fig: 12.15(a).pdf')
show()

phi_0=[-pi/2,-pi/2-0.001]
omega_0=0
phipoints_1=[]
phipoints_2=[]
phipoints=[phipoints_1,phipoints_2]
for p in phi_0:
	r=array([p,omega_0],float)
	for t in tpoints:
		phipoints[phi_0.index(p)].append(r[0])
		k1=h*f(r,t)
		k2=h*f(r+0.5*k1,t+0.5*h)
		k3=h*f(r+0.5*k2,t+0.5*h)
		k4=h*f(r+k3,t+h)
		r+=(k1+2*k2+2*k3+k4)/6.0
phipoints_diff=abs(array(phipoints_2)-array(phipoints_1))
log_phipoints_diff=log10(phipoints_diff)
plot(tpoints,log_phipoints_diff,label='$\gamma$={0}and $\delta$$\phi$ is={1}'.format(gamma,phi_0[1]-phi_0[0]))
legend(loc='best')
grid()
xlabel('time')
ylabel('log|$\delta$$\phi$(t)|')
title('Logarithmic Plot of log|$\delta$$\phi$(t)|')
xlim(0,15)
savefig('Fig: 12.15(b).pdf')
show()