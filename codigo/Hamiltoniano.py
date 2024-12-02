#!/usr/bin/env python

import numpy as np
import scipy.sparse as sp

def crear_Hamil(epsilon, t_enr):
    """Generador de un Hamiltoniano tridiagonal de dimensión epsilon.size

    Esta función crear un Hamiltoniano de manera dispersa pues tiene la característica
    de ser tridiagonal. Los valores de un "vector" epsilon forman la diagonal principal y 
    las otras diagonales son formadas por los valores de un "vector" t_enr. 
    En caso que los valores no coincidan con los tamaños de las diagonales respectivas, 
    la función levanta una excepción `ValueError`.

    Examples:
        >>> import numpy as np
        >>> import scipy.sparse as sp
        >>> crear_Hamil(np.array([1.0, 2.0, 3.0, 4.0]), np.array([1.0 ,2.0 ,3.0])).toarray()
        array([[1. 1. 0. 0.],
               [1. 2. 2. 0.],
               [0. 2. 3. 3.],
               [0. 0. 3. 4.]])

    Args:
        epsilon (ndarray): Primer argumento. Valores energéticos que son asignados a la diagonal principal.
        t_enr (ndarray): Segundo argumento. Valores energéticos que son asignados a las diagonales secundarias.

    Raises:
        ValueError: Si t_enr.size no es igual a epsilon.size - 1.

    Returns:
        hamiltoniano (ndarray): Devuelve el Hamiltoniano de manera dispersa (elementos no nulos) si los valores coinciden
    """
 
    if (t_enr.size == epsilon.size - 1):
        hamiltoniano = sp.diags([t_enr, epsilon, t_enr], offsets = [-1, 0, 1], shape = (epsilon.size, epsilon.size))
        return hamiltoniano

    else:
        raise ValueError ("Valores energéticos no coinciden con el tamaño del Hamiltoniano.")

#print(help(crear_Hamil))

