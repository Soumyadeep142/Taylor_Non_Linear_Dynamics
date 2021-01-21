from numpy import *
from matplotlib.pyplot import *

w=2*pi
w0=1.5*w
beta=w0/4

def f(r,t,gamma):
	phi=r[0]
	omega=r[1]
	fphi=omega
	fomega=gamma*(w0)**2*cos(w*t)-(w0)**2*sin(phi)-2*beta*fphi
	return array([fphi,fomega], float)

def bif_diagram(phi_start,omega_start,skip,iteration,step=0.0001,gamma_min=1.03):
	
	omegapoints=[]
	gamma_values=arange(gamma_min,1.53,step)
	t_initial=1
	t_final=201
	N=20000
	h=(t_final-t_initial)/N
	phi_0=phi_start
	omega_0=omega_start
	tpoints=arange(t_initial,t_final,h)
	G=[]
	omega=[]
	Gamma=[]
	Omega=[]
	tp=[]
	for gamma in gamma_values:
		print(gamma)
		r=array([phi_0,omega_0],float)
		for t in tpoints:
			omegapoints.append(r[1])
			k1=h*f(r,t,gamma)
			k2=h*f(r+0.5*k1,t+0.5*h,gamma)
			k3=h*f(r+0.5*k2,t+0.5*h,gamma)
			k4=h*f(r+k3,t+h,gamma)
			r+=(k1+2*k2+2*k3+k4)/6.0
			x=(round(t,2))
			if x==int(t):
				G.append(gamma)
				omega.append(r[1])
				tp.append(t)
	j=0
	for x in tp:
		if (x>skip and x<skip+iteration+1):
			Gamma.append(G[j])
			Omega.append(omega[j])
		j+=1
	
	plot(Gamma,Omega,ls='',marker=',', color='black')
	xlabel(r'$\gamma$')
	ylabel(r'$\phi.(t)$')
	title('Bifurcation Diagram of DDP')
	savefig('Fig: 12.18.pdf')
	
	show()
	
bif_diagram(-pi/2,0,100,20)
