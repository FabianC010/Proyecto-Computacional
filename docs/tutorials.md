# Tutorial

## Planteamiento inicial

Vamos a trabajar con una grilla de tamaño 100 $\times$ 100 y con un único fermión que se encontrará en el medio de la grilla. Asimismo, vamos a plantear que los valores que toman los $\epsilon_i$ y $t_i$ que construyen el hamiltoniano del sistema ([Índice](index.md)), son homogéneos entre sus iguales.Lo primero que se debe hacer es importar los módulos necesarios que contienen las funciones apropiadas para evaluar la dinámica del sitema cuántico. Entre ellos se encuentran `numpy` y `scipy`. 

``` py
import numpy as np
import scipy.sparse as sp
import Hamiltoniano as hm
import as rk
import Diag as dg
import calculo_norma as cn
import simulacion as sm
```

Seguidamente, vamos a invocar a la función **inicialización** del módulo simulación. Esta función requiere de 5 parámetros: el tamaño de la grilla, el valor que toman los $\epsilon_i$, el valor de los $t_i$, el tiempo final del estudio del sistema y la cantidad de momentos temporales que se desean evaluar. Para este ejemplo utilizaremos $\epsilon = 2.0$ y $t = 1.0$. Asimismo, evaluaremos 20 segundos divididos en 1000 momentos temporales

Las condiciones iniciales son que el tiempo inicie en 0 y la probabilidad de encontrar al fermión en el medio de la grilla es $= 1$, esto implica que en el resto de la grilla es de 0. Dentro de la función antes mencionada, se genera un vector con dichas características y también se crea un Hamiltoniano con la característica de ser tridiagonal y cuadrado. Para el manejo de memoria, el Hamiltoniano se crea como una _matriz dispersa_, lo que implica que solo se guardan las entradas no nulas con sus respectivas "coordenadas". Ahora bien, la función devuelve el vector con el fermión en medio de la grilla, el Hamiltoniano que describe la dinámica del sistema, una lista con los instantes temporales deseados y por último, la separación que existe entre cada instante.

``` py
psi, hamiltoniano, times, h = inicializacion(100, 2.0, 1.0, 20.0, 1000)
```

Elementos a tomas en cuenta:

1. Si se desea poner valores específicos de $\epsilon_i$ y $t_i$, se debe de hacer manualmente. Se puede hacer de manera sencilla con las opereaciones [a:b] de las listas.
2. El elemento $h$ debe ser bastante pequeño en comparación al tamaño de la grilla para RK4, de otros modos el método  presenta fallos.

Con las variables asociadas a los valores deseados, veremos cómo resolver el problema con las dos metodologías elegidas.

## RK4

Para encontrar la solución mediante el método de Runge-Kutta de orden 4, utilizaremos nuevamente el módulo `sm` (importado al principio) y su función **simulacion_Rk**. Esta función toma como argumento las cuatro variables antes definidas. Dentro de sí, llama a la implementación del método RK4 y a la función que genera la dinámica según lo plantea la ecuación de Schrödinger ([Explicación](explanation.md)), ambas forman parte del módulo `rk4`. Con esto dicho, es necesario crear un contenedor donde se guarden los resultados, que son las probabilidades de ocupación por el fermión de cada espacio de la grilla por cada instante temporal:

``` py
state_quantr = simulacion_Rk(psi, hamiltoniano, times, h)
```

La _r_ al final de `state_quantr` es para denotar el método que se está usando. Lo que se obtiene es un _object_ que contiene listas de las probabilidades en cada momento.

## Diagonalización 

También, se puede encontrar la solución mediante el método de diagonalización del Hamiltoniano. Para este caso, invocamos a la función de `sm` **simulacion_Diag**, que recibe los mismos argumentos que su contraparte del método RK4. En su interior, realiza llamados a las funciones **exps** (solución formal a la ecuación de Schrödinger [Explicación](explanation.md)) y **sol_Vector** del módulo `Diag`. Con este método, atacamos el problema con la base donde el Hamiltoniano es diagonal. Por ello, la función tiene que reconstruir el Hamiltoniano en su totalidad para obtener todos los autovalores y autovectores de este mismo. 

Volvemos a definir un contenedor que tendrá los valores de probabilidad en cada instante temporal 

``` py
state_quantd = simulacion(psi, hamiltoniano, times, h)
```

La documentación de todas las funciones empleadas se ecuentran en el apartado de [referencias](reference.md)

## Animaciones
Ya teniendo el comportamiento del sistema, se pueden hacer animaciones en las que se grafiquen las probabilidades de encontrar al fermión en los diferentes puntos de la grilla. Esta gráfica va cambiando para cada tiempo.


### Runge-Kutta 4

<video width="560" height="315" controls>
  <source src="https://github.com/FabianC010/Proyecto-Computacional/raw/main/docs/videos/dinamica_rk4_tutorial.mp4" type="video/mp4">
</video>


### Diagonalización

<video width="560" height="315" controls>
  <source src="https://github.com/FabianC010/Proyecto-Computacional/raw/main/docs/videos/dinamica_diag_tutorial.mp4" type="video/mp4">
</video>

