#!/usr/bin/env python
import numpy as np
import scipy as sp
import Hamiltoniano as Hm
import time

def exps(eigenValues, h, oldState):
    """Evaluacion del exponencial de los valores diagonales del hamiltoniano.

    Examples:
        >>> exps(np.array([-1.41473988,  0.39770187,  1.97266549,  4.74988177,  9.29449075]), 1, np.array([0,  0,  1,  0,  0]))
    [ 0.        +0.j         0.        +0.j        -0.39113927-0.9203315j
      0.        +0.j         0.        -0.j  ] 
    
    Args:
        eigValues (array): Autovalores de Hamiltoniano inicial.
        h (float): Valor del paso temporal del estado anterior al actual.
        oldState (array): La daga del estado con la que se va a calcular la daga del nuevo estado del sistema. 

    Returns:
        array: Devuelve los valores de la daga del estado viejo multiplicados por el exponencial de los valores 
               de la diagonal del hamiltoniano multiplicador por el paso temporal y el opuesto de la constante 
               imaginaria.
    """ 
    state = np.exp(-1.0j*eigenValues*h)*oldState # Se usa * y no np.dot() porque los autovalores se guardan como un 
                                                 # vector, no como una matriz diagonal.
    return state






startTime = time.time()                          # Se empieza a tomar el tiempo.

epsilon = np.array([1.0, 2.0, 3.0, 4.0, 5.0])    # Valores energéticos de la diagonal principal.
t_enr = np.array([1.0, 2.0, 3.0, 4.0])           # Valores energéticos de las diagonales secundarias.
H = Hm.crear_Hamil(epsilon, t_enr)               # Se crea el hamiltoniano con los valores enérgeticos asignados.

eigVals, eigVecs = np.linalg.eigh(H)             # np.linalg.eigh consigue los autovalores y 
                                                 # autovectores del hamiltoniano.

psi = np.array([0.0, 0.0, 1.0, 0.0, 0.0])        # Declaramos el vector del estado inicial.
psi_t = eigVecs.conjugate().transpose().dot(psi) # Declaramos el vector del estado inicial pero en la nueva base.
                                                 # Para eso multiplicamos la daga de la matriz de autovectores por
                                                 # el estado inicial en la base original.

times = np.linspace(0.0, 10.0, 100, dtype = float)  # Se crea el arreglo de tiempos.
h = times[1] - times[0]                             # Se calcula el paso temporal que hay entre cada uno de ellos.

#Se declaran los distintos estados
stateQuant0 = np.zeros(times.size, dtype = object)
stateQuant1 = np.zeros(times.size, dtype = object)
stateQuant2 = np.zeros(times.size, dtype = object)
stateQuant3 = np.zeros(times.size, dtype = object)
stateQuant4 = np.zeros(times.size, dtype = object)

for tt in range(times.size):
    stateQuant0[tt] = psi[0] 
    stateQuant1[tt] = psi[1]
    stateQuant2[tt] = psi[2]
    stateQuant3[tt] = psi[3]
    stateQuant4[tt] = psi[4]
    psi_t = exps(eigVals, h, psi_t) # Se calcula el nuevo estado pero en la base "diagonal".
    psi = eigVecs.dot(psi_t) # Se convierte a la base original para guardar sus entradas.

endTime = time.time() # Se calcula el tiempo después de finalizar.
duration = endTime - startTime # Se obtiene la diferencia entre el tiempo final e inicial.
print(f"Duration: {duration} seconds") # Se imprime la duración.
