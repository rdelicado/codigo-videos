# La serpiente: zigzag contra atajos

Vídeo: **La serpiente sin chocar nunca: zigzag contra atajos** (The Farmer Was Replaced).

El sombrero de dinosaurio convierte al dron en una serpiente que crece con cada manzana. Para que nunca choque con su cola,
los dos programas siguen el mismo ciclo hamiltoniano en zigzag (`camino.py`): uno lo sigue siempre y el otro toma atajos
hacia la manzana sin adelantar a la cola, y pasa al zigzag cuando ocupa un tercio de la granja.

Medidos en una granja de 12 × 12 (con `set_world_size(12)`): el zigzag tarda 552 214 ticks (90,9 s) y el de atajos
351 010 ticks (57,78 s), con los mismos 654 368 huesos (con las mejoras de los dinosaurios al nivel 6). En 6 × 6 apenas se
nota la diferencia. El camino en zigzag necesita un lado par.

Los nombres de los archivos importan: los programas hacen `from camino import hacer_camino` y `medir_serpiente` hace
`import serpiente_zigzag` e `import serpiente_atajos`.

| Archivo | Qué hace |
|---|---|
| [`camino.py`](camino.py) | El ciclo en zigzag: una dirección por casilla. |
| [`serpiente_zigzag.py`](serpiente_zigzag.py) | Sigue siempre el camino hasta llenar la granja. |
| [`serpiente_atajos.py`](serpiente_atajos.py) | Atajos hacia la manzana hasta un tercio de la granja, luego zigzag. |
| [`medir_serpiente.py`](medir_serpiente.py) | Mide los dos: ticks, segundos y huesos. |
