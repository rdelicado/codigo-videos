# Estadísticas: mano derecha contra DFS (The Farmer Was Replaced)
# Mide los dos programas sin tocarlos: los importa, resuelve 10 laberintos nuevos con cada uno
# y escribe los ticks, los segundos y el oro de cada laberinto y la media.
# Para que funcione, los archivos tienen que llamarse mano_derecha y dfs en el juego:
# import busca la ventana por su nombre.

import mano_derecha
import dfs

vueltas = 10

# medir llama a resolver() sin nada dentro, así que cada programa va envuelto en una función
# sin parámetros. dfs necesita su set vacío en cada laberinto.
def derecha():
	mano_derecha.mano_derecha()

def profundidad():
	dfs.dfs(set())

# resolver es una función: se pasa entera, sin paréntesis, y se ejecuta aquí dentro.
def medir(nombre, resolver):
	total_ticks = 0
	total_s = 0
	oro = num_items(Items.Gold)
	for i in range(vueltas):
		clear()
		mano_derecha.crear_laberinto()
		# El reloj antes y después de resolver: solo cuenta lo que tarda el algoritmo.
		t0 = get_tick_count()
		s0 = get_time()
		resolver()
		ticks = get_tick_count() - t0
		s = get_time() - s0
		harvest()
		total_ticks += ticks
		total_s += s
		quick_print(nombre, i + 1,
			"| ticks:", ticks, "| s:", s)
	quick_print("MEDIA", nombre,
		"| ticks:", total_ticks / vueltas,
		"| s:", total_s / vueltas,
		"| oro:", num_items(Items.Gold) - oro)

medir("mano derecha", derecha)
medir("dfs", profundidad)
