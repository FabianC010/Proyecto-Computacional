#!/usr/bin/env python
import numpy as np
import Hamiltoniano as Hm

def dynGenerator(oper, state):
    """Evaluación de la dinámica de un sistema.

    Examples:
        >>> dynGenerator(np.array([[1.0, 1.0], [1.0, 0.0]]), np.array([[1.0, 0.0], [0.0, 0.0]]))
       [[0.+1.j 0.+0.j]
        [0.+0.j 0.+0.j]] 

    Args:
        hamiltonian (array): Primer argumento. Es el operador lineal que ayudará a evaluar la dinámica del sistema. 
        state (array): Segundo argumento. Es el estado en el que se encuentra el sistema a la hora de evaluarlo. 

    Returns:
       (array): Retorna la multiplicación de la constante compleja por el operador lineal y el estado del sistema.

    """
    return -1.0j * oper.dot(state)

def rk4(func, oper, state, h):
    """Evaluación del estado de un sistema dinámico con respecto al anterior.

    Examples:
        >>> rk4(dynGenerator, np.array([[1.0, 1.0], [1.0, 0.0]]),  np.array([[1.0, 0.0], [1.0, 0.0]]), 1.0)
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

