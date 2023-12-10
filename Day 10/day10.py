lines = [x.strip() for x in open("data.txt").readlines()]

CONNECTIONS = {
	'|': ((0, 1), (0, -1)),
	'-': ((-1, 0), (1, 0)),
	'L': ((0, -1), (1, 0)),
	'J': ((0, -1), (-1, 0)),
	'7': ((0, 1), (-1, 0)),
	'F': ((0, 1), (1, 0)),
}

NEIGHBOURS = [
	(-1, 0),
	(-1, 1),
	(0, 1),
	(1, 1),
	(1, 0),
	(1, -1),
	(0, -1),
	(-1, -1)
]

grid = {}
start = None

for y, row in enumerate(lines):
	for x, spot in enumerate(row):
		grid[(x, y)] = spot
		if spot == 'S':
			start = (x, y)

def find_appropriate_pipe(x, y):
	for pipe, links in CONNECTIONS.items():
		connects = True
		for l in links:
			if (x+l[0], y+l[1]) in grid and grid[(x+l[0], y+l[1])] in CONNECTIONS:
				other_pipe = grid[(x+l[0], y+l[1])]
				if (-l[0], -l[1]) not in CONNECTIONS[other_pipe]:
					connects = False
					break
			else:
				connects = False
				break
		if connects:
			return pipe

	return '.'

def find_pipe_length(x, y):
	length = 0
	current_spot = (x, y)
	current_pipe = grid[current_spot]
	links = CONNECTIONS[current_pipe]
	next = (x + links[0][0], y + links[0][1])
	path_points = [current_spot]
	
	while next != (x, y):
		path_points.append(next)
		length += 1
		last = current_spot
		current_spot = next
		current_pipe = grid[current_spot]
		links = CONNECTIONS[current_pipe]
		
		next = (current_spot[0] + links[0][0], current_spot[1] + links[0][1])
		if next == last:
			next = (current_spot[0] + links[1][0], current_spot[1] + links[1][1])
	
	return length + 1, path_points

def find_enclosed_area(path_points):
	interior = set()
	exterior = set()
	
	for i, point in enumerate(path_points):
		prev = path_points[i-1]
		next = path_points[(i+1) % len(path_points)]
		
		next_delta = (next[0] - point[0], next[1] - point[1])
		prev_delta = (prev[0] - point[0], prev[1] - point[1])
		
		int_stop_index = NEIGHBOURS.index(prev_delta)
		ext_stop_index = NEIGHBOURS.index(next_delta)
		
		neighbour_index = ext_stop_index + 1
		while neighbour_index != int_stop_index:
			neighbour = (point[0] + NEIGHBOURS[neighbour_index][0], point[1] + NEIGHBOURS[neighbour_index][1])
			if neighbour not in path_points:
				interior.add(neighbour)
			neighbour_index += 1
			neighbour_index %= len(NEIGHBOURS)
		
		while neighbour_index != ext_stop_index:
			neighbour = (point[0] + NEIGHBOURS[neighbour_index][0], point[1] + NEIGHBOURS[neighbour_index][1])
			if neighbour not in path_points:
				exterior.add(neighbour)
			neighbour_index += 1
			neighbour_index %= len(NEIGHBOURS)
		
	all_cells = set()
	for y in range(len(lines)):
		for x in range(len(lines[0])):
			all_cells.add((x, y))
			
	all_cells.difference_update(set(path_points))
	all_cells.difference_update(interior)
	all_cells.difference_update(exterior)
	
	added = True
	while added:
		added = False
		for c in all_cells:
			for n in NEIGHBOURS:
				if (c[0] + n[0], c[1] + n[1]) in interior:
					interior.add(c)
					added = True
					break
		all_cells.difference_update(interior)
	
	return len(interior), len(exterior) + len(all_cells)
			
		

grid[start] = find_appropriate_pipe(start[0], start[1])
length, path_points = find_pipe_length(start[0], start[1])
midpoint = length // 2
print('Part 1:', midpoint)

total_space = len(lines) * len(lines[0]) - length
print(find_enclosed_area(path_points))
print(total_space, 'total space')
