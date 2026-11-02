# Laberintos: mano derecha contra DFS

Vídeo: **Mano derecha contra DFS: el laberinto que atrapa a uno de los dos** (The Farmer Was Replaced).

Dos programas para resolver laberintos, cada uno con solo lo necesario para crear un laberinto y resolverlo: la regla de la
mano derecha y la búsqueda en profundidad (DFS), que apunta en un `set` las casillas donde ya ha estado. Otros dos archivos
los importan para medirlos y para reutilizar el mismo laberinto 100 veces.

En 10 laberintos nuevos de 6 × 6 empatan: 5 539,7 ticks la mano derecha y 5 532,8 DFS, 0,91 s de media los dos. Al reutilizar el laberinto caen
paredes y aparecen caminos en círculo: DFS encuentra los 100 tesoros y la mano derecha se quedó dando vueltas en el 25.

Los nombres de los archivos importan: `estadisticas` y `reutilizar` hacen `import mano_derecha` e `import dfs`, y el juego
busca esos nombres.

| Archivo | Qué hace |
|---|---|
| [`mano_derecha.py`](mano_derecha.py) | Crea un laberinto y lo resuelve con la mano derecha. |
| [`dfs.py`](dfs.py) | Crea un laberinto y lo resuelve con DFS y el set `visitadas`. |
| [`estadisticas.py`](estadisticas.py) | Mide los dos en 10 laberintos: ticks, segundos y oro. |
| [`reutilizar.py`](reutilizar.py) | Usa el mismo laberinto 100 veces con uno de los dos. |
