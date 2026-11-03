# La serpiente en zigzag (The Farmer Was Replaced)
# Sigue siempre el camino de camino.py, esté donde esté la manzana. Es seguro (nunca choca),
# pero lento: si ya ha pasado la manzana, da la vuelta entera a la granja para llegar.

from camino import hacer_camino

def zigzag():
	# Granja vacía y el dron en la esquina (0, 0): donde empieza el camino.
	clear()
	camino = hacer_camino(get_world_size())
	# Al ponerse el sombrero, compra una manzana con cactus y la deja debajo.
	change_hat(Hats.Dinosaur_Hat)
	# i es el paso del camino por el que va.
	i = 0
	# move devuelve False cuando ya no hay sitio: la serpiente ha llenado la granja.
	while move(camino[i]):
		# El resto de dividir: después del último paso, vuelve al 0.
		i = (i + 1) % len(camino)
	# Quitarse el sombrero cobra los huesos: el largo de la cola al cuadrado.
	change_hat(Hats.Straw_Hat)

# Solo si se ejecuta esta ventana; al importarla (medir_serpiente.py) no se ejecuta sola.
if __name__ == "__main__":
	zigzag()
