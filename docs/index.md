# Índice

## Modelo de _TIGHT BINDING_

El modelo de *tight binding* es uno de los modelos más fundamentales en ciencia de materiales, con capacidad de predicción en sistemas como el grafeno. Un Hamiltoniano en mecánica cuántica, representa el observable de energía de un sistema. El Hamiltoniano unidimensional fermiónico para partículas sin espín con condiciones no periódicas está dado por:

$$
\begin{equation}
\hat{H} = \sum_{i=1}^{N-1} t_i \left( \hat{c}_i^\dagger \hat{c}_{i+1} + \hat{c}_{i+1}^\dagger \hat{c}_i \right) + \sum_{i=1}^{N} \epsilon_i \hat{c}_i^\dagger \hat{c}_i
\end{equation}
$$

donde los $\hat{c}_i$ son operadores de destrucción fermiónica y los $\hat{c}_i^\dagger$ operadores de creación para el sitio de la grilla
$i$. Para el caso de un solo fermión en la grilla, este Hamiltoniano es una matriz de dimensión N de carácter tridiagonal. El comportamiento del sistema depende de los parámetros energéticos $t_i$ y $\epsilon_i$. En este proyecto, el estado inicial del sistema consiste en un fermión en el medio de la grilla.

_Para ver la documentación completa, visite_ [github.com](https://github.com/FabianC010/Proyecto-Computacional.git)
