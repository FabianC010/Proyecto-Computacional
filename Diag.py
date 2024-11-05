#!/usr/bin/env python
import numpy as np
import scipy as sp
import Hamiltonian as Hm
import time
start_time = time.time()
def exps(EigVal,t):
    """Evaluacion del exponencial de los valores diagonales del hamiltoniano

    Examples:
        >>> exps([-1.41473988  0.39770187  1.97266549  4.74988177  9.29449075],1)
        [ 0.15542379+0.98784789j  0.92195349-0.3873006j  -0.39113927-0.9203315j 0.037484  +0.99929723j -0.99152462-0.12991892j]

    Args:
        Eigval (array): Autovalores de Hamiltoniano inicial
        t (double): valor del tiempo

    Returns:
        array: Devuelve el exponencial de los va
    """ 
    iConst = 1.0j
    exponenciales = np.exp(-iConst*EigVal*t)
    return exponenciales

t_enr = np.array([1,2,3,4,5])   
epsilon = np.array([1,2,3,4])   #
H = Hm.crear_Hamil(5, t_enr, epsilon)


#np.linalg.eigvalsh consige los autovalores del hamiltoniano, con estos podemos diagonalizar el Hamiltoniano
EigVal= np.linalg.eigvalsh(H)
#Declaramos la matriz de estado inicial
psi=[1,1,1,1,1]
#se determina el intervalo del tiempo
times=np.linspace(0,10,100)
#Se declaran los distintos estados
statequant0=np.zeros(times.size)
statequant1=np.zeros(times.size)
statequant2=np.zeros(times.size)
statequant3=np.zeros(times.size)
statequant4=np.zeros(times.size)

for tt in range(times.size):
    statequant0[tt]=psi[0].real
    statequant1[tt]=psi[1].real
    statequant2[tt]=psi[2].real
    statequant3[tt]=psi[3].real
    statequant4[tt]=psi[4].real
    
    psi=exps(EigVal,times[tt])

end_time = time.time()
duration = end_time - start_time
print(f"Duration: {duration} seconds")
