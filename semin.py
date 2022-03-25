import numpy as np
import matplotlib.pyplot as plt
from rando import fi,thet,rad_ran,geom,disc,ef
from numba import jit


@jit(nopython=True)
def aut(n,lam,a,b,c):
#Angulos coord Esfericas
    f=fi(n)
    t=thet(n)
#Discriminar de acuerdo a la configuracion geometrica
    an=disc(n,a,b,c,f,t)
#longitud de decaimiento aleatorio
    r=rad_ran(len(an[0,:]),lam)
    return ef(an[0,:],an[1,:],r,120,100,300,100,100) #Inicial
    #return ef(an[0,:],an[1,:],r,90,60,170,70,50) #Actual

#Configuracion Actual 
#geo=geom(50,170,70,90,60)

#Configuracion Inicial
geo=geom(100,300,100,120,100)

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

##############################################################
"""
Se producirian 1E8 Bosones de Higgs de los cuales decaerian
siguiendo el Branching Ratio arbitrario
que se encuentra [0.1, 0.01, 0.001, 0.0001]
"""
br=0.001
n=int(1e8*br)

l=np.logspace(2,4,20) #Longitudes de decaimiento [100-10000] metros
res=[]
st=[]
for j in l:
    a=[]
    for i in range(1000): #1E4 repeticiones 
        a.append(aut(n,1/j,geo[0],geo[1],geo[2]))
    res.append(np.mean(a))
    st.append(np.std(a))

print(res)
print(st)

"""               
plt.errorbar(l,res,yerr=st)
plt.title("Eficiencia")
plt.xlabel("ct [m]")
plt.ylabel("0 < efic < 1")
plt.show()
"""