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

def bif_diagram(phi_start,omega_start,skip,iteration,step=0.0001,gamma_min=1.0600):
	
	phipoints=[]
	gamma_values=arange(gamma_min,1.087,step)
	t_initial=1
	t_final=601
	N=60000
	h=(t_final-t_initial)/N
	phi_0=phi_start
	omega_0=omega_start
	tpoints=arange(t_initial,t_final,h)
	G=[]
	phi=[]
	Gamma=[]
	Phi=[]
	tp=[]
	for gamma in gamma_values:
		print(gamma)
		r=array([phi_0,omega_0],float)
		for t in tpoints:
			phipoints.append(r[0])
			k1=h*f(r,t,gamma)
			k2=h*f(r+0.5*k1,t+0.5*h,gamma)
			k3=h*f(r+0.5*k2,t+0.5*h,gamma)
			k4=h*f(r+k3,t+h,gamma)
			r+=(k1+2*k2+2*k3+k4)/6.0
			x=(round(t,2))
			if x==int(t):
				G.append(gamma)
				phi.append(r[0])
				tp.append(t)
	j=0
	for x in tp:
		if (x>skip and x<skip+iteration+1):
			Gamma.append(G[j])
			Phi.append(phi[j])
		j+=1
	
	plot(Gamma,Phi,ls='',marker=',', color='black')
	xlabel(r'$\gamma$')
	ylabel(r'$\phi(t)$')
	title('Bifurcation Diagram of DDP')
	
	vlines(1.0663,ymin=-0.7,ymax=0.0,linestyle='--')
	vlines(1.0793,ymin=-0.7,ymax=0.0,linestyle='--')
	vlines(1.0829,ymin=-0.7,ymax=0.0,linestyle='--')


	text(1.064,-0.6,r'$\gamma_{1}$ = 1.0663',size=13,color = 'red')
	text(1.077,-0.6,r'$\gamma_{2}$ = 1.0793',size=13,color = 'blue')
	text(1.0832,-0.68,r'$\gamma_{c}$ = 1.0829',size=13,color = 'green')

	savefig('Fig: 12.17.pdf')
	
	show()
	
bif_diagram(-pi/2,0,500,100)
