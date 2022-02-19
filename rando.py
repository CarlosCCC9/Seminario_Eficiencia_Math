#Funciones a usar

import numpy as np
from numba import jit

#Variable fi aleatoria coord. esf.

@jit(nopython=True)
def fi(n):
	u=np.random.uniform(0,1,n)
	fi=2*np.pi*u
	return fi

#variable thet coord. esf.

@jit(nopython=True)
def thet(n):
    z=np.pi*np.random.uniform(0,1,n)
    gam=1/(np.sqrt(1-0.9*0.9))
    y=np.sin(z)/(gam*((0.9/0.77)+np.cos(z)))
    thet=np.pi/2-np.arctan(y)
    return thet

#Radios aleatorios de acuerdo a la longitud de decaimiento

@jit(nopython=True)
def rad_ran(n,lam):
	w=np.random.uniform(0,1,n)
	r=-1*np.log(1-w)/lam
	return r

#Configuracion geometrica del detector

@jit(nopython=True)
def geom(x0,ymax,ymin,zmax,zmin):
	alf=np.arctan(x0/ymin)
	bet1=np.arctan(ymin/zmax)
	bet2=np.arctan(ymax/zmin)
	geo=[alf,bet1,bet2]
	return geo

# Considerar particulas dentro del "rango de vision" del detector

@jit(nopython=True)
def disc(n,alf,b1,b2,fi,thet):
	t,f=[],[]
	for i in range(n):
		if(fi[i] > (np.pi/2.0 - alf) and fi[i] < (np.pi/2.0 + alf) and thet[i]>b1 and thet[i] <  b2 ):
			t.append(thet[i])
			f.append(fi[i])
	ang=[t,f]
	an=np.asarray(ang)
	return an

# Calculo de la eficiencia

@jit(nopython=True)
def ef(thet,fi,r,zmax,zmin,ymax,ymin,x0):
    x=r*np.sin(thet)*np.cos(fi)
    y=r*np.sin(thet)*np.sin(fi)
    z=r*np.cos(thet)
    con=0
    for i in range(len(z)):
        if(z[i]<zmax and z[i]>zmin and y[i]<ymax and y[i]>ymin and x[i]>-x0 and x[i]<x0):
            con=con+1
    #return con
    return con/len(z)


@jit(nopython=True)
def efi(thet,fi,r,zmax,zmin,ymax,ymin,x0):
    x=r*np.sin(thet)*np.cos(fi)
    y=r*np.sin(thet)*np.sin(fi)
    z=r*np.cos(thet)
    hit=(z<zmax and z>zmin and y<ymax and y>ymin and x>-x0 and x<x0)
    hits=np.sum(hit)
    pas=(z>zmin and y>ymin and x<x0 and x>-x0)
    n_pas=np.sum(pas)
    return hits/n_pas