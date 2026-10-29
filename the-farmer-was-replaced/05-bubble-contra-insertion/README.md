# Bubble sort contra insertion sort

Vídeo: **Bubble sort contra insertion sort: ¿cuál ordena antes?** (The Farmer Was Replaced). Segundo de la serie de
ordenación con cactus.

El mismo programa que el de [bubble sort](../04-cactus-bubble-sort), cambiando solo `ordenar_linea` por insertion
sort, y con una `main` que mide los ticks y los segundos que tarda en ordenar el campo. Para comparar los dos en
igualdad, pon esta misma `main` en el programa de bubble sort.

Los dos son O(n²) en el caso medio y en el peor, y O(n) si la línea ya está ordenada. Hacen los mismos cambios (uno
por cada pareja desordenada, porque solo se cambia con el vecino), pero insertion sort compara menos y el dron camina
menos.

Necesita desbloqueados los cactus y Timing (`get_tick_count` y `get_time`).

| Archivo | Qué hace |
|---|---|
| [`cactus_insertion_sort.py`](cactus_insertion_sort.py) | Planta, ordena con insertion sort midiendo el tiempo, cosecha y repite. |
