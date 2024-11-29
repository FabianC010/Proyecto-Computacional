# Tutorial

## Planteamiento inicial

Vamos a trabajar con una grilla de tamaño 100 $\times$ 100 y con un único fermión que se encontrará en el medio de la grilla. Lo primero que se debe hacer es crear un vector `psi` que contendrá las probabilidades de encontrar al fermión en un espacio de la grilla. Para realizar las operaciones se necesita de la biblioteca `numpy`, por eso hay que importarla junto al resto de módulos que ocupamos. Usaremos elementos de tipo _float_ para una mejor representación de las probabilidades.

``` py
import numpy as np
import Hamiltoniano as hm
import as rk
import Diag as dg.
import calculo_norma as cn
```

``` py
psi = np.zeros(100, dtype = float)
psi[N//2] = 1.0
```

En la segunda línea dereferenciamos el elemento `N//2` de _psi_. Los índices de las listas son _integers_, por eso es necesario usar el operador $//$ que realiza una división de enteros y su resultado es el cociente de la división sin el resto. Una vez construído el estado inicial del sistema, debemos crear el hamiltoniano, cuyas características principales son ser tridiagonal y cuadrado. Para ello, se invoca a la función **crear_Hamil** del módulo `Hamiltoniano`. Sin embargo, primero debemos definir los valores que toman los `epsilon` y `t_enr` que construyen el hamiltoniano del sistema. En este ejemplo, planteamos un sistema donde esto valores son similares. 

``` py
epsilon = np.full(100, 2.0)
t_enr = np.full (99, 1.0)
hamiltoniano = hm.crear_Hamil(epsilon, t_enr)
```

Ahora, vamos a plantear el tiempo de estudio del sistema. Tomaremos desde 0 hasta 10 segundos para ver cómo es la evolución temporal de las probabilidades de encontrar al fermión en los distintos espacios de la grilla. La función **linspace** del módulo de `numpy` es la elegida para crear un arreglo cuyos elementos tienen una diferencia homogénea entre si. Dividiremos los 10 segundos en 100 momentos temporales.

``` py
times = np.linspace(0.0, 10.0, 100)
temp_dif = times[1] - times[0]
``` 

Cómo se mencionó anteriormente, **linspace** genera elementos con una diferencia entr ellos, `temp_dif` se encarga de almacenar esta diferencia ya que es importante para los cálculos posteriores. 

Seguidamente, veremos cómo resolver el problema con las dos metodologías elegidas.

## RK4


## Diagonalización 

