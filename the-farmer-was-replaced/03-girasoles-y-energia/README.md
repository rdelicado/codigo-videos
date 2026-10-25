# Girasoles y energía

Vídeo: **El triple de energía con los mismos girasoles** (The Farmer Was Replaced).

Con un solo dron y una granja de 6x6: en una primera vuelta planta los girasoles y mide sus pétalos,
guardándolos en un diccionario (clave = pétalos, valor = lista de posiciones); en la segunda los cosecha
del de 15 pétalos al de 7 con `ir_a`, para cobrar el bonus de 8 veces más energía. En el vídeo da unas
215 de energía por vuelta, frente a 67 cosechando en orden.

Necesita desbloqueados los girasoles y los diccionarios.

| Archivo | Qué hace |
|---|---|
| [`girasoles.py`](girasoles.py) | Planta, mide, recoge en orden y repite en bucle. |
