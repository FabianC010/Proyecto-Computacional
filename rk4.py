#!/usr/bin/env python
import numpy as np
import scipy as sp
import Hamiltonian as Hm
import time

startTime = time.time()

def dynGenerator(oper, state):
    """Evaluación de la dinámica de un sistema.

    Examples:
        >>> dynGenerator(np.array([[1,1], [1,0]]), np.array([[1,0], [0,0]]))
       [[0.+1.j 0.+0.j]
        [0.+0.j 0.+0.j]] 

    Args:
        hamiltonian (array): Primer argumento. Es el operador lineal que ayudará a evaluar la dinámica del sistema. 
        state (array): Segundo argumento. Es el estado en el que se encuentra el sistema a la hora de evaluarlo. 

    Returns:
       (array): Retorna la multiplicación de la constante compleja por el operador lineal y el estado del sistema.

    """
    return 1.0j * oper * state

def rk4(func, oper, state, h):
    """Evaluación del estado de un sistema dinámico con respecto al anterior.

    Examples:
        >>> rk4(dynGenerator, np.array([[1,1], [1, 0]]),  np.array([[1,0], [1,0]]), 1.0)
        [[0.54166667+0.83333333j 0.        +0.j        ]
         [0.54166667+0.83333333j 0.        +0.j        ]]

    Args:
        func (function): Primer argumento. Es la función que genera la dinámica del sistema.
        oper (array: Segundo argumento. Es el operador lineal.
        state (array): Tercer argumento. Es el estado del sistema dinámico.
        h (float): Cuarto argumento. Es el tiempo trascurrido desde el estado anterior hasta el que se está calculando.

    Returns:        
        (array): Retorna la suma del estado anterior más un sexto de h por la suma del k_1 + 2*k_2 + 2*k_3 + k_4.
    """
    k1 = func(oper, state)
    k2 = func(oper, state + h*(k1)/2.0)
    k3 = func(oper, state + h*(k2)/2.0)
    k4 = func(oper, state + h*(k3))
    return state + (1.0/6.0) * h* (k1 + 2.0*k2 + 2.0*k3 + k4)



t_enr = np.array([1.0, 2.0, 3.0, 4.0, 5.0]) # Se otorgan los valores energéticos de la diagonal del hamiltoniano.
epsilon = np.array([1.0, 2.0, 3.0, 4.0])  # Se otorgan los valores energéticos a las diagonales secundarias. 
H = Hm.crear_Hamil(5, t_enr, epsilon) # Se construye el hamiltoniano.
times = np.linspace(1.0, 10.0, 100) # Se crea el arreglo de los valores temporales.
h = times[1] - times[0] # Se calcula el tiempo transcurrido entre cada entrada.

psi = np.array([1.0, 1.0, 1.0, 1.0, 1.0]) # Se construye el vector del estado inicial.
stateQuant = np.zeros(times.size, dtype = object) # Se crea el vector que va a contener los estados del sistema para
                                                  # cada tiempo respectivo

for tt in range(times.size):
    stateQuant[tt] = psi.real # Se guarda el estado del sistema en el tiempo respectivo.
    psi = rk4(dynGenerator, H, psi, h) # Se calcula el nuevo estado del sistema
                                       # para ser guardado en el siguiente valor temporal.

endTime = time.time() 
duration = endTime - startTime
print(f"Duration: {duration} seconds")
