# All drones: each drone takes its own probes and digs down at the same time as the others.
# It reuses probe_points and dig_down from coal_one: the file name matters for the import.
from coal_one import probe_points, dig_down

# The probes of one drone: its own (first) and then every max_drones() after it.
# On 6 x 6 with 4 drones, one probe each; with fewer drones, some take more than one.
def my_points(points, first):
	mine = []
	for i in range(first, len(points), max_drones()):
		mine.append(points[i])
	return mine

def coal_round():
	clear()
	points = probe_points()
	drones = []
	# One new drone for every extra drone we have, each with dig_down and its probes.
	# If there are more drones than probes, the extra ones don't spawn: they would have nothing to dig.
	for i in range(1, max_drones()):
		if i < len(points):
			drones.append(spawn_drone(dig_down, my_points(points, i)))
	# The main drone keeps the first probes and works too.
	dig_down(my_points(points, 0))
	# Nobody tells the others that the vein was found: the inventory is shared, so when one drone
	# mines coal the count changes for all of them and every dig_down stops.
	# Wait for all of them before the next clear(), because clear() removes the other drones
	# and would cut off the one still mining the vein.
	for drone in drones:
		wait_for(drone)

if __name__ == "__main__":
	while True:
		coal_round()
