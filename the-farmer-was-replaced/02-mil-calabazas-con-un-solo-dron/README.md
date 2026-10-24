# Mil calabazas con un solo dron

Vídeo: **Mil calabazas con un solo dron: el código explicado** (The Farmer Was Replaced).

Con un solo dron y una granja de 6x6: planta todas las calabazas apuntando cada casilla en una
lista de pendientes, vuelve solo a las que faltan por el camino más corto (`ir_a`, aprovechando que
la granja da la vuelta por los bordes) y repite con dos listas, `pendientes` y `siguen`, hasta que
todas han crecido. Entonces se forma la calabaza gigante: 6 × 6 × 6 = 216 calabazas.

| Archivo | Qué hace |
|---|---|
| [`calabazas.py`](calabazas.py) | Planta, revisa y cosecha una calabaza gigante. |

Cada ejecución cosecha una gigante: con cinco ya tienes el logro de las mil calabazas.
