import numpy as np
import matplotlib.pyplot as plt
from rando import fi,thet,rad_ran,geom,disc,ef
from numba import jit

n=50000
lam=0.007847

@jit(nopython=True)
def aut(n,lam,a,b,c):
#Angulos coord Esfericas
	f=fi(n)
	t=thet(n)
	an=disc(n,a,b,c,f,t)
	r=rad_ran(len(an[0,:]),lam)
	return ef(an[0,:],an[1,:],r,90,60,170,70,50)

geo=geom(50,170,70,90,60)

"""
Limite Central

N=10000000
res=[]
for i in range(N):
     res.append(aut(1000,lam,geo[0],geo[1],geo[2]))

mu=np.mean(res)
sigma=np.std(res)
count, bins, ignored = plt.hist(res, 50, density=True)

plt.plot(bins,1/(sigma*np.sqrt(2*np.pi))*np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
plt.title(f"Limite Central {N} repeticiones")
plt.xlabel("Efic")
plt.ylabel("Probabilidad")
"""



"""
Numeros grandes
    y su grafica
    
f=np.logspace(2,5,100)
res=[]
for i in f:
    j=int(i)
    res.append(aut(j,lam,geo[0],geo[1],geo[2]))
    
plt.scatter(f,res)
plt.title("Numeros grandes")
plt.xlabel("N repeticiones")
plt.ylabel("efi")
plt.show()
"""



l=np.logspace(2,3,20)
res=[]
for j in l:
    a=[]
    for i in range(10000):
        a.append(aut(n,1/j,geo[0],geo[1],geo[2]))
    res.append(np.mean(a))

               
plt.scatter(l,res)
plt.title("Prueba")
plt.xlabel("ct [m]")
plt.ylabel("efic")
plt.show()
