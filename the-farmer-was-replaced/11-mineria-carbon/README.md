# Carbón con drones: la veta entera en 16 segundos

Vídeo: **Carbón con drones: la veta entera en 16 segundos** (The Farmer Was Replaced, DLC de minería). Primer vídeo de la
serie de minería.

El carbón sale en vetas: una capa de un bloque de grosor, a una sola profundidad, entre 2 y 15 bloques bajo la superficie.
Cavar un pozo en una casilla hace un cráter que tira la veta sin minarla, y bajar capa a capa por toda la granja es muy
lento. Por eso el programa usa **sondas**: unas pocas casillas repartidas (cada 3) que bajan todas a la vez, un bloque por
pasada. En cada parada la sonda mira su casilla y las cuatro de al lado, y si ve carbón sigue la veta entera con
`mine_vein`, que se llama a sí misma.

Con todos los drones, cada dron se lleva sus sondas. Nadie avisa a los demás de que ha encontrado la veta: el inventario
es de todos, así que cuando cambia el carbón todos paran.

Medido en la partida `tutorial` (6 × 6, 4 drones, Coal en nivel 1), 3 vueltas de cada:

| Programa | Segundos por vuelta | Carbón por vuelta |
|---|---|---|
| Un dron | 47,36 · 26,23 · 55,07 (media 42,9) | 11 · 18 · 17 |
| 4 drones | 14,55 · 13,87 · 19,29 (media 15,9) | 15 · 15 · 16 |

El mismo carbón, casi 3 veces más rápido. Empieza en 6 × 6: en 3 × 3 y 4 × 4 sale una sola sonda y solo trabaja un dron.

`coal_drones` y `measure_coal` hacen `import coal_one`: el nombre del archivo importa.

| Archivo | Qué hace |
|---|---|
| [`coal_one.py`](coal_one.py) | Un dron: sondas que bajan a la vez y siguen la veta. |
| [`coal_drones.py`](coal_drones.py) | El mismo programa repartido entre todos los drones. |
| [`measure_coal.py`](measure_coal.py) | 3 vueltas de cada programa: ticks, segundos y carbón. |
