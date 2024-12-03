# Resultados

La dinámica del fermión depende totalmente de sus parámetros enérgeticos. A continuación, se observarán algunos casos con energías diferentes para estudiar su comportamiento. Tome en cuenta que $\epsilon$ representa la energía potencial y  $t$ la energía cinética.

## $\epsilon_i = 1$ y $t_i = 10$

En este caso, hay mucha energía cinética en comparación con la energía potencial.
<video width="560" height="315" controls>
  <source src="https://github.com/FabianC010/Proyecto-Computacional/raw/main/docs/videos/dinamica_rk4T10.mp4" type="video/mp4">
</video>

<video width="560" height="315" controls>
  <source src="https://github.com/FabianC010/Proyecto-Computacional/raw/main/docs/videos/dinamica_DiagT10.mp4" type="video/mp4">
</video>

Como podemos observar, las probabilidades de encontrar el fermión en una posición están muy distribuidas y además van cambiando a gran velocidad. Esto se debe a que hay mucha energía cinética, que es la "energía del movimiento".

Por otro lado, se ve que la onda se refleja cuando llega al final de la grilla. No obstante, este comportamiento no es real, solo ocurre porque para el programa no existe espacio más allá de la grilla.

## $\epsilon_i = 10$ y $t_i = 1$

En este caso, hay mucha energía potencial en comparación a la energía cinética.
<video width="560" height="315" controls>
  <source src="https://github.com/FabianC010/Proyecto-Computacional/raw/main/docs/videos/dinamica_rk4E10.mp4" type="video/mp4">
</video>

<video width="560" height="315" controls>
  <source src="https://github.com/FabianC010/Proyecto-Computacional/raw/main/docs/videos/dinamica_DiagE10.mp4" type="video/mp4">
</video>

Se puede observar que la onda se mueve mucho más lento que antes. Esto se debe a la baja energía cinética. Aunque igual, las posiciones en las que es más probable encontrar al fermión se van alejando del centro de la grilla conforme pasa el tiempo.

Por otra parte, el resultado obtenido con el método RK4 difiere un poco con el que se obtuvo con el método de diagonalización. Es más confiable el segundo, ya que el método es un poco más exacto dado la naturaleza tridiagonal del Hamiltoniano. La diferencia puede ser generada por errores de aproximación. Para resolverlo, se pudieron haber usado pasos temporales más pequeños. Aunque, en general, ambos métodos permiten observar la dinámica del sistema bastante bien. 

## $\epsilon_i = 5$ y $t_i = 5$ con un potencial en medio de la grilla

Ahora, el valor del enegía cinética es igual al de la energía potencial, excepto en el medio de la grilla, donde hay más energía potencial.
<video width="560" height="315" controls>
  <source src="https://github.com/FabianC010/Proyecto-Computacional/raw/main/docs/videos/dinamica_rk4E15.mp4" type="video/mp4">
</video>

<video width="560" height="315" controls>
  <source src="https://github.com/FabianC010/Proyecto-Computacional/raw/main/docs/videos/dinamica_DiagE15.mp4" type="video/mp4">
</video>

Como se puede observar, es más probable encontrar el fermión donde está el potencial. La mayoría de la probabilidad se mantiene ahí, aunque igual hay una pequeña parte que se va a alejando del centro de la grilla. Esto se debe a que esa energía potencial forma un especie de pozo, llamado pozo de potencial. En este caso, ese pozo es pequeño, por lo que el fermión tiene suficiente energía para superarlo.

## $\epsilon_i = 5$ y $t_i = 5$ con un potencial significativo en medio de la grilla

Por último, se estudiará el mismo caso anterior pero ahora con un potencial más significativo en el medio de la grilla.

<video width="560" height="315" controls>
  <source src="https://github.com/FabianC010/Proyecto-Computacional/raw/main/docs/videos/dinamica_rk4E25.mp4" type="video/mp4">
</video>

<video width="560" height="315" controls>
  <source src="https://github.com/FabianC010/Proyecto-Computacional/raw/main/docs/videos/dinamica_DiagE25.mp4" type="video/mp4">
</video>

Como se puede observar, el comportamiento fue casi el mismo que con el potencial anterior. Lo que cambió es que ahora no hay una parte de las probabilidades que se van alejando del centro de la grilla. En este caso, el pozo de potencial es muy grande, entonces el fermión no tiene suficiente energía para superarlo. Por esta razón, el fermión siempre se encuentra ahí.
