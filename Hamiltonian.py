#!/usr/bin/env python

import numpy as np
import scipy as sp

def crear_Hamil(size, t_enr, epsilon):
    """Generador de un Hamiltoniano tridiagonal de dimensión size

    Esta función crear un Hamiltoniano con la característica de ser tridiagonal
    con los valores de un "vector" t_enr en la diagonal principal y en las otras
    diagonales los valores de un "vector" epsilon. En caso que los valores no 
    coincidan con los tamaños de las diagonales se imprime un mensaje de error.

    Examples:
        >>> crear_Hamil(4, np.array([1,2,3,4]), np.array([1,2,3]))
        [[1. 1. 0. 0.]
        [1. 2. 2. 0.]
        [0. 2. 3. 3.]
        [0. 0. 3. 4.]]

    Args:
        size (int): Dimensión del Hamiltoniano.
        t_ener (ndarray): Valores energéticos que son asignados a la diagonal principal.
        epsilon (ndarray): Valores energéticos que son asignados a las diagonales secundarias.

    Returns:
        ndarray: Devuelve el Hamiltoniano tridiagonal si los valores coinciden
    """ 
    Hamiltoniano = np.zeros((size, size))

    if (t_enr.size == size) and (epsilon.size == size - 1):
        Hamiltoniano += np.diagflat(t_enr) + np.diagflat(epsilon, 1) + np.diagflat(epsilon, -1)
        return Hamiltoniano

    else:
        print("Valores energéticos no coinciden con el tamaño del Hamiltoniano.")
        return Hamiltoniano

t_enr = np.array([1,2,3,4,5])   # ¿Usar linspace? 
epsilon = np.array([1,2,3,4])   # =     = 

#t_enr = np.linspace(0.0, 50.0, num=8)
#epsilon = np.linspace(0.0, 50.0, num=7)

H = crear_Hamil(5, t_enr, epsilon)

