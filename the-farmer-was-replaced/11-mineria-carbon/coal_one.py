# One drone: probes go down together; every coal found is followed along its vein.
# The probes are a few cells spread out over the farm. They all go down one block per pass,
# so no shaft gets ahead of the others: no deep holes, no craters, and the vein never falls unmined.

# The opposite of each direction: to undo a step after following a branch of the vein.
opposite = {North: South, East: West, South: North, West: East}

# Shortest path to (x, y): the farm wraps around, so going the other way round the edge
# is shorter when the target is more than half the farm away.
def go_to(x, y):
	n = get_world_size()
	east = (x - get_pos_x() + n) % n
	if east <= n // 2:
		for _ in range(east):
			move(East)
	else:
		for _ in range(n - east):
			move(West)
	north = (y - get_pos_y() + n) % n
	if north <= n // 2:
		for _ in range(north):
			move(North)
	else:
		for _ in range(n - north):
			move(South)

# Where the probes go: every 3 cells, starting at 1.
# Each probe checks its own cell and the 4 around it (a cross), so every 3 cells they cover
# the farm without overlapping, and starting at 1 puts the probe in the middle of its patch.
# On 6 x 6 that is 4 probes: (1, 1), (1, 4), (4, 1) and (4, 4).
def probe_points():
	n = get_world_size()
	points = []
	for x in range(1, n, 3):
		for y in range(1, n, 3):
			points.append([x, y])
	return points

# Mines the whole vein from here: coal below -> dig; coal on a side -> go there and do the same.
# It calls itself because every coal may have more coal next to it; get_ground_type(d) looks
# at the next cell without moving (it needs Underground Senses). After each branch it steps back
# with opposite[d], to check the next side from the same cell.
def mine_vein():
	if get_ground_type() == Grounds.Coal:
		dig()
	for d in [North, East, South, West]:
		if get_ground_type(d) == Grounds.Coal:
			move(d)
			mine_vein()
			move(opposite[d])

# One pass: at every probe, look for the vein first and then dig to go down one.
# Looking before digging means every level is checked before it is left behind.
def probe_pass(points):
	for point in points:
		x, y = point
		go_to(x, y)
		mine_vein()
		dig()

# Goes down pass after pass until coal comes in or until -15 (there is no coal below that).
# With Coal at level 1 there is only one vein, so as soon as the coal count changes we stop:
# carrying on to the bottom took longer than starting again with clear().
def dig_down(points):
	coal = num_items(Items.Coal)
	while get_pos_z() > -15 and num_items(Items.Coal) == coal:
		probe_pass(points)

# One round: clear() takes the drone back up and makes a brand new underground with new coal.
def coal_round():
	clear()
	dig_down(probe_points())

# Only when this file is run directly; coal_drones imports it without starting this loop.
if __name__ == "__main__":
	while True:
		coal_round()
