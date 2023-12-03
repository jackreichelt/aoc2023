lines = [x.strip() for x in open("data.txt").readlines()]

sum = 0
for y in range(len(lines)):
	current_num = ''
	current_start_index = -1
	for x in range(len(lines[y])):
		c = lines[y][x]			
		if c == '.':
			if current_num:
				# check if part number

				part = False
				if current_start_index != 0:
					if lines[y][current_start_index-1] != '.':
						part = True
				if y != 0:
					for i in range(current_start_index-1, x+1):
						if lines[y-1][i] != '.' and not lines[y-1][i].isnumeric():
							part = True
				if y != len(lines) - 1:
					for i in range(current_start_index-1, x+1):
						if lines[y+1][i] != '.' and not lines[y+1][i].isnumeric():
							part = True
				
				if part:
					sum += int(current_num)
				
				current_num = ''
				current_start_index = -1
		elif c.isnumeric():
			current_num += c
			if current_start_index == -1:
				current_start_index = x
		else:
			if current_num:
				sum += int(current_num)
				current_num = ''
				current_start_index = -1
	if current_num:
		part = False
		if current_start_index != 0:
			if lines[y][current_start_index-1] != '.':
				part = True
		if y != 0:
			for i in range(current_start_index-1, x+1):
				if lines[y-1][i] != '.' and not lines[y-1][i].isnumeric():
					part = True
		if y != len(lines) - 1:
			for i in range(current_start_index-1, x+1):
				if lines[y+1][i] != '.' and not lines[y+1][i].isnumeric():
					part = True
					
		if part:
			sum += int(current_num)
			
	current_num = ''
	current_start_index = -1
			
print(sum)

# 529183 wrong
# 535168 wrong
# 530570 wrong
# 529618 right

ratio_sum = 0
potential_gears = []

for y in range(len(lines)):
	for x in range(len(lines[y])):
		if lines[y][x] == '*':
			potential_gears.append((x, y))

adjacent_deltas = [
	(1, 0),
	(1, 1),
	(0, 1),
	(-1, 1),
	(-1, 0),
	(-1, -1),
	(0, -1),
	(1, -1)
	
]

for x, y in potential_gears:
	adjacent_nums = []
	# check left
	if lines[y][x-1].isnumeric():
		num = ''
		k = x-1
		while k >= 0 and lines[y][k].isnumeric():
			num = lines[y][k] + num
			k -= 1
		adjacent_nums.append(int(num))
	
	# check right
	if lines[y][x+1].isnumeric():
		num = ''
		k = x+1
		while k < len(lines[y]) and lines[y][k].isnumeric():
			num += lines[y][k]
			k += 1
		adjacent_nums.append(int(num))
	
	# check above middle
	if lines[y-1][x].isnumeric():
		num = ''
		# walk left
		k = x
		while k >= 0 and lines[y-1][k].isnumeric():
			num = lines[y-1][k] + num
			k -= 1
		# walk right
		k = x+1
		while k < len(lines[y-1]) and lines[y-1][k].isnumeric():
			num += lines[y-1][k]
			k += 1
		adjacent_nums.append(int(num))
	else:
		# check above left
		if lines[y-1][x-1].isnumeric():
			num = ''
			k = x-1
			while k >= 0 and lines[y-1][k].isnumeric():
				num = lines[y-1][k] + num
				k -= 1
			adjacent_nums.append(int(num))
		# check above right
		if lines[y-1][x+1].isnumeric():
			num = ''
			k = x+1
			while k < len(lines[y-1]) and lines[y-1][k].isnumeric():
				num += lines[y-1][k]
				k += 1
			adjacent_nums.append(int(num))
	
	# check below middle
	if lines[y+1][x].isnumeric():
		num = ''
		# walk left
		k = x
		while k >= 0 and lines[y+1][k].isnumeric():
			num = lines[y+1][k] + num
			k -= 1
		# walk right
		k = x+1
		while k < len(lines[y+1]) and lines[y+1][k].isnumeric():
			num += lines[y+1][k]
			k += 1
		adjacent_nums.append(int(num))
	else:
		# check below left
		if lines[y+1][x-1].isnumeric():
			num = ''
			k = x-1
			while k >= 0 and lines[y+1][k].isnumeric():
				num = lines[y+1][k] + num
				k -= 1
			adjacent_nums.append(int(num))
		# check below right
		if lines[y+1][x+1].isnumeric():
			num = ''
			k = x+1
			while k < len(lines[y+1]) and lines[y+1][k].isnumeric():
				num += lines[y+1][k]
				k += 1
			adjacent_nums.append(int(num))
	
	print(f"Gear at {x}, {y}")
	print(f"{adjacent_nums = }")
	if len(adjacent_nums) == 2:
		gear_power = adjacent_nums[0] * adjacent_nums[1]
		print(f"{gear_power = }")
		ratio_sum += gear_power

print(ratio_sum)