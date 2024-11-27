#!/usr/bin/env python

import numpy as np

def crear_Hamil(epsilon, t_enr):
    """Generador de un Hamiltoniano tridiagonal de dimensión epsilon.size

    Esta función crear un Hamiltoniano con la característica de ser tridiagonal
    con los valores de un "vector" epsilon en la diagonal principal y en las otras
    diagonales los valores de un "vector" t_enr. En caso que los valores no 
    coincidan con los tamaños de las diagonales se imprime un mensaje de error.

    Examples:
        >>> crear_Hamil(np.array([1.0, 2.0, 3.0, 4.0]), np.array([1.0 ,2.0 ,3.0]))
        [[1. 1. 0. 0.]
        [1. 2. 2. 0.]
        [0. 2. 3. 3.]
        [0. 0. 3. 4.]]

    Args:
        epsilon (ndarray): Valores energéticos que son asignados a la diagonal principal.
        t_enr (ndarray): Valores energéticos que son asignados a las diagonales secundarias.

    Returns:
        ndarray: Devuelve el Hamiltoniano tridiagonal si los valores coinciden
    """ 
    Hamiltoniano = np.zeros((epsilon.size, epsilon.size))

    if (t_enr.size == epsilon.size -1):
        Hamiltoniano += np.diagflat(epsilon) + np.diagflat(t_enr, 1) + np.diagflat(t_enr, -1)
        return Hamiltoniano

    else:
        print("Valores energéticos no coinciden con el tamaño del Hamiltoniano.")
        return Hamiltoniano

