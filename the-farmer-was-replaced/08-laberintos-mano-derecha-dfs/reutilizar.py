# Reutilizar el laberinto (The Farmer Was Replaced)
# Crea un laberinto y lo usa muchas veces: al echar Sustancia Rara sobre el tesoro, el tesoro
# cambia de sitio y pueden caer paredes, así que aparecen caminos en círculo. DFS lo resuelve
# siempre; la mano derecha puede quedarse dando vueltas para siempre.
# Para que funcione, los archivos tienen que llamarse mano_derecha y dfs en el juego.

import mano_derecha
import dfs

veces = 100

# Cada programa envuelto en una función sin parámetros, para pasarla a reutilizar.
def derecha():
	mano_derecha.mano_derecha()

def profundidad():
	dfs.dfs(set())

def reutilizar(resolver):
	clear()
	dfs.crear_laberinto()
	# La misma cantidad de sustancia con la que se creó: es la que mueve el tesoro.
	nivel = num_unlocked(Unlocks.Mazes)
	sustancia = get_world_size() * 2 ** (nivel - 1)
	for i in range(veces):
		resolver()
		quick_print("tesoro", i + 1)
		use_item(Items.Weird_Substance, sustancia)
	# El último tesoro sí se cosecha: harvest acaba con el laberinto.
	resolver()
	harvest()

# Cambia profundidad por derecha para ver a la mano derecha atascarse.
reutilizar(profundidad)
