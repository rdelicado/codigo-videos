# Mide los dos programas de la serpiente (The Farmer Was Replaced)
# Importa los dos y ejecuta cada uno las veces que diga vueltas. Escribe en la ventana de
# salida los ticks, los segundos y los huesos de cada vuelta.
# Los nombres importan: el juego busca las ventanas serpiente_zigzag y serpiente_atajos.

import serpiente_zigzag
import serpiente_atajos

vueltas = 3

# programa es la función, sin ejecutar: se le pasa sin paréntesis y aquí se llama.
def medir(nombre, programa):
	for i in range(vueltas):
		huesos = num_items(Items.Bone)
		t0 = get_tick_count()
		s0 = get_time()
		programa()
		quick_print(nombre, i + 1,
			"| ticks:", get_tick_count() - t0,
			"| s:", get_time() - s0,
			"| huesos:", num_items(Items.Bone) - huesos)

medir("zigzag", serpiente_zigzag.zigzag)
medir("atajos", serpiente_atajos.serpiente)
