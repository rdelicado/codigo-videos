# Drones: procesos, no hilos

Vídeo: **Drones: procesos, no hilos** (The Farmer Was Replaced).

Cada dron se porta como un proceso: tiene su propia memoria, lo que le pasas con `spawn_drone` se copia y solo puede
devolverte algo al acabar, con `wait_for`. Por eso el policultivo del vídeo 7 se reparte en dos fases por vuelta: todos
los drones plantan las principales de su trozo y apuntan pedidos, el primero los junta, y luego cada uno planta las
compañeras de su trozo. Cada casilla tiene un solo dueño en cada fase, así que no hay carreras.

El programa mira `get_world_size()` y `max_drones()`, así que funciona igual con 1, 4 o 32 drones y en cualquier granja.
Medido con zanahorias en 6 × 6: con 1 dron, 39 por segundo; con 4 drones, 127 (unas 3 veces más). En 32 × 32 con 32
drones y árboles, unos 60 millones de madera por vuelta.

`estadisticas_drones` hace `import policultivo_drones`: el nombre del archivo importa.

| Archivo | Qué hace |
|---|---|
| [`policultivo_drones.py`](policultivo_drones.py) | El policultivo repartido entre todos los drones. |
| [`estadisticas_drones.py`](estadisticas_drones.py) | 10 vueltas: recurso, sustancia rara, segundos y energía de cada una. |
