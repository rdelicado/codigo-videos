# 32 drones, 32 laberintos

Vídeo: **32 drones, 32 laberintos: Como conseguir 100M de oro** (The Farmer Was Replaced).

La granja se divide en cuadrados de 5x5 con un laberinto y un dron en cada uno, todos a la vez.
Cada dron busca su tesoro con BFS sobre su propio mapa (lo que no ha visto lo da por libre),
reutiliza el laberinto hasta 300 veces y después crea otro en el mismo sitio. Cuando se acaba la
energía, planta girasoles y los cosecha del de más pétalos al de menos.

| Archivo | Qué hace |
|---|---|
| [`laberintos.py`](laberintos.py) | El programa principal: reparte los drones y resuelve los laberintos. |
| [`girasoles.py`](girasoles.py) | Recarga la energía con girasoles. `laberintos.py` lo importa. |

Los dos archivos tienen que estar en la misma partida, con estos nombres. Ejecuta `laberintos`.
