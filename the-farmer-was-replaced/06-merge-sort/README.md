# Merge sort contra bubble e insertion sort

Vídeo: **Merge sort: ¿gana el algoritmo más famoso?** (The Farmer Was Replaced). Tercero y último de la serie de
ordenación con cactus.

El mismo programa que el de [insertion sort](../05-bubble-contra-insertion), cambiando solo `ordenar_linea`: ahora es
merge sort, con `ordenar` y `mezclar` recursivos y `ir_a` para que el dron no camine de más. En la granja no hay lista
auxiliar: mezclar por vecinos es insertar, uno a uno, los cactus del trozo derecho en el izquierdo. `main` mide los ticks y
los segundos que tarda en ordenar el campo, como en el vídeo anterior.

Necesita desbloqueados los cactus y Timing (`get_tick_count` y `get_time`).

| Archivo | Qué hace |
|---|---|
| [`cactus_merge_sort.py`](cactus_merge_sort.py) | Planta, ordena con merge sort midiendo el tiempo, cosecha y repite. |
| [`merge_sort_listas.py`](merge_sort_listas.py) | El merge sort clásico con listas, que se escribe igual en Python, C y otros lenguajes. |

Los dos son O(n log n) en todos los casos y necesitan una lista auxiliar del mismo tamaño; el de la granja no, porque
cambia cactus vecinos. En la granja de 6×6 gana insertion sort: el coste está en lo que camina el dron.
