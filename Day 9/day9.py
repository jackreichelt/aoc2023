lines = [[int(y) for y in x.strip().split()] for x in open("data.txt").readlines()]

def sequence_differences(seq):
	diffs = []
	for i in range(1, len(seq)):
		diffs.append(seq[i]-seq[i-1])
	return diffs

def expand(lower, upper):
	upper.append(upper[-1] + lower[-1])

def expand_back(lower, upper):
	upper.insert(0, upper[0] - lower[0])

total = 0
left_total = 0

for l in lines:
	layers = [l]
	while sum(layers[-1]):
		layers.append(sequence_differences(layers[-1]))
	
	layers[-1].append(0)
	layers[-1].insert(0, 0)
	
	for i in range(len(layers)-2, -1, -1):
		expand(layers[i+1], layers[i])
		expand_back(layers[i+1], layers[i])
	
	
	total += layers[0][-1]
	left_total += layers[0][0]

print(total)
print(left_total)
		