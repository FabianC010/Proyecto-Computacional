# Tutorial

## Planteamiento inicial

Vamos a trabajar con una grilla de tamaño 100 $\times$ 100 y con un único fermión que se encontrará en el medio de la grilla. Lo primero que se debe hacer es crear un vector `psi`, cuyo tamaño representa el tamaño de la grilla y el valor de la norma al cuadrado de la entrada $c_i$, la probabilidad de encontrar al fermión en dicho punto. Para realizar las operaciones se necesita de la biblioteca `numpy`, por eso hay que importarla junto al resto de módulos que ocupamos. Usaremos elementos de tipo _float_ para una mejor representación de las probabilidades.

``` py
import numpy as np
import Hamiltoniano as hm
import as rk
import Diag as dg.
import calculo_norma as cn
```

``` py
psi = np.zeros(100, dtype = float)
psi[100//2] = 1.0
```

La condición inicial es que $t = 0$, la probabilidad de encontrar al fermión en el medio de la grilla es $= 1$, esto implica que en el resto de la grilla es de 0. En la segunda línea derreferenciamos el elemento `100//2` de _psi_. Los índices de las listas son _integers_, por eso es necesario usar el operador $//$ que realiza una división de enteros y su resultado es el cociente de la división sin el resto. Una vez construido el estado inicial del sistema, debemos crear el hamiltoniano, cuyas características principales son ser tridiagonal y cuadrado. Para ello, se invoca a la función **crear_Hamil** del módulo `Hamiltoniano`. Sin embargo, primero debemos definir los valores que toman los $\epsilon_i$ y $t_i$ que construyen el hamiltoniano del sistema ([Índice](index.md)). En este ejemplo, planteamos un sistema donde estos valores son similares. 

``` py
epsilon = np.full(100, 2.0)
t_enr = np.full (99, 1.0)
hamiltoniano = hm.crear_Hamil(epsilon, t_enr)
```

La función **full** genera un _ndarray_ cuyos elementos son todos iguales al segundo parámetro que recibe. Ahora bien, vamos a plantear el tiempo de estudio del sistema. Tomaremos desde 0 hasta 10 segundos para ver cómo es la evolución temporal de las probabilidades de encontrar al fermión en los distintos espacios de la grilla. La función **linspace** del módulo de `numpy` es la elegida para crear un arreglo cuyos elementos tienen una diferencia homogénea entre sí. Dividiremos los 10 segundos en 1000 momentos temporales.

``` py
times = np.linspace(0.0, 10.0, 1000)
temp_dif = times[1] - times[0]
``` 

Cómo se mencionó anteriormente, **linspace** genera elementos con una diferencia entre ellos, `temp_dif` se encarga de almacenar esta diferencia ya que es importante para los cálculos posteriores. 

Seguidamente, veremos cómo resolver el problema con las dos metodologías elegidas.

## RK4

Para encontrar la solución mediante el método de Runge-Kutta de orden 4, utilizaremos el módulo `rk4` (importado al principio), el cual contiene la implementación del método y la función que genera la dinámica según lo plantea la ecuación de Schrödinger ([Explicación](explanation.md)). Con esto dicho, es necesario crear un contenedor donde se guarden las probabilidades de ocupación por el fermión de cada espacio de la grilla por cada instante temporal:

``` py
state_quantr = np.zeros(times.size, dtype = object)
```

La _r_ al final de `state_quantr` es para denotar el método que se está usando. Presenta `dtype = object` porque contienen vectores.

Bien, es momento de iniciar la evaluación del comportamiento del sistema. Para ello, vamos a iniciar un _for loop_ para evaluar cada momento temporal e invocamos a la función **rk4** de `rk`. Nuevamente, lo que queremos visualizar son las probabilidades de encontrar al fermión, las cuales son representadas por la norma al cuadrado de cada entrada de `psi`, para esto llamamos a **norma_Cuadrada** del módulo `calculo_norma`. El procedimiento sería el siguiente:

``` py
for tt in range(times.size):
    psi = rk.rk4(rk.dynGenerator, hamiltoniano, psi, temp_dif) # Se calcula el nuevo estado del sistema
    state_quantr[tt] = cn.norma_Cuadrada(psi)
``` 

En el instante _tt_ se calcula el estado del sistema un paso adelante en el tiempo y `psi` adquiere las propiedades de ese sistema. Se realiza el cálculo de las normas al cuadrado, las probabilidades se guardan en el contenedor y se repite para todos los tiempos.

## Diagonalización 

También, se puede encontrar la solución mediante el método de diagonalización. Para esto utilizaremos el módulo `Diag`, el cual contiene la implementación del método y la función que genera la dinámica según lo plantea la solución de la ecuación de Schr&#xF6;dinger ([Explicación](explanation.md)). Ahora, hacemos un proceso análogo al que hicimos con **RK4**.

``` py
psi = np.zeros(100, dtype = float)
psi[100//2] = 1.0
```

Esto lo volvemos a hacer para volver a tener el arreglo del estado inicializado con valores de 0.0 y un 1.0 en medio de la grilla. No importa borrar los datos que contenía porque los que interesan ya están guardados en state_quantr.

``` py
state_quantd = np.zeros(times.size, dtype = object)
```

Se crea un arreglo para contener las probabilidades de ocupación del fermión en cada instante temporal para este método. Ahora, ocupamos calcular los autovectores y autovalores del Hamiltoniano. Para ello, utilizaremos la función **eigh** de ``np.linalg``, la cual nos hace el cálculo.

``` py
eigVals, eigVecs = np.linalg.eigh(hamiltoniano)
``` 

Con esto listo, tenemos todas las variables necesarias para evaluar la dinámica del sistema con esta metodología numérica. Para ello, vamos a iniciar un _for loop_ para evaluar cada momento temporal e invocamos a la función **sol_Vector** de ``dg``. Al igual que en **RK4** lo que ocupamos son las probabilidades de encontrar al fermión, entonces ocupamos a la función **norma_Cuadrada** del módulo ``calculo_norma``. El procedimiento sería el siguiente:

``` py
for tt in range(times.size):
  psi = dg.sol_Vector(eigVecs, eigVals, hamiltonian, psi, temp_dif)
  state_quantd[tt] = cn.norma_cuadrada(psi)
```

En el _for loop_ se calculó el estado del sistema avanzado en el tiempo. Luego, se calculó la norma de cada entrada y se guardó en el contenedor. Esto se repitió para todos los tiempos.

## Animación
Ya teniendo el comportamiento del sistema, se pueden hacer animaciones en las que se grafiquen las probabilidades de encontrar al fermión en los diferentes puntos de la grilla. Esta gráfica va cambiando para cada tiempo.





La documentación de estas funciones se ecuentran en el apartado de [referencias](reference.md)
