#!/usr/bin/env python

import numpy as np

def norma_Cuadrada(psi):
    """Cálculo de la norma al cuadrado de cada componente de un vector psi.

    La función recibe un vector psi (cuyos componentes pueden ser complejos),y calcula 
    la norma de cada uno de sus componentes, y devuelve un arreglo, un nuevo vector 
    cuyos componentes son las normas al cuadrado de cada entrada del vector original.

    Examples:
        >>> import numpy as np
        >>> norma_cuadrada(np.array([1.0 - 1.0j, 2.0 - 2.0j, 3.0]))
        [2.0, 8.0, 9.0]

    Args:
        psi (ndarray): Vector que contiene la dinámica del sistema.
       
    Returns:
        (ndarray): Devuelve un arreglo cuyas entradas corresponden a la norma al cuadrado
                 de los corresponientes componentes del vector que recibe como argumento.                 
    """

    return np.abs(psi)**2

#print(help(norma_Cuadrada))
