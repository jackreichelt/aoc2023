lines = [x.strip() for x in open("data.txt").readlines()]

nodes = {}

class Node:
	def __init__(self, id, left=None, right=None):
		self.id = id
		self.left = left
		self.right = right
		self.last_found = 0
		self.interval = 0
	
	def l(self):
		return nodes[self.left]
	
	def r(self):
		return nodes[self.right]
	
current_nodes = []
end_nodes = []

for n in lines[2:]:
	node_id, node_children = n.split(' = ')
	left, right = node_children[1:-1].split(', ')
	new_node = Node(node_id, left, right)
	nodes[node_id] = new_node
	
	if node_id[-1] == 'A':
		current_nodes.append(new_node)
	if node_id[-1] == 'Z':
		end_nodes.append(new_node)
	
instructions = lines[0]
steps = 0

while True:
	new_current_nodes = []
	for current in current_nodes:
		if instructions[steps % len(instructions)] == 'R':
			new_current_nodes.append(current.r())
		else:
			new_current_nodes.append(current.l())
	steps += 1
	for n in new_current_nodes:
		if n.id[-1] == 'Z':
			if not n.last_found:
				n.last_found = steps
			elif not n.interval:
				n.interval = steps - n.last_found
				print('Interval found')
	
	if all([x.interval for x in end_nodes]):
		break
		
	current_nodes = new_current_nodes

print(steps)
print([x.last_found for x in end_nodes])
print([x.interval for x in end_nodes])

intervals = [x.interval for x in end_nodes]
smallest = min(intervals)

mult = 2
while True:
	steps = smallest * mult
	mods = [steps % x.interval == 0 for x in end_nodes]
#	if sum(mods) > 2:
#		print(sum(mods))
	if all(mods):
		break
	mult += 1
print(steps)