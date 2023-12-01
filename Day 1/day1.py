lines = [x.strip() for x in open("data.txt").readlines()]

sum = 0
for l in lines:
	num = ''
	for c in l:
		if c.isnumeric():
			num += c
			break
	for c in l[::-1]:
		if c.isnumeric():
			num += c
			break
	
	if num:
		sum += int(num)

print(sum)

# part 2
num_strs = {
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9',
}
sum = 0
for l in lines:
	print(l, end=': ')
	num = ''
	
	found = False
	for i, c in enumerate(l):
		if c.isnumeric():
			num += c
			break
		for s, n in num_strs.items():
			chunk = l[i:]
			if chunk.startswith(s):
				num += n
				found = True
				break
		if found:
			break
		
	found = False
	for i in range(1, len(l)+1):
		c = l[-i]
		if c.isnumeric():
			num += c
			break
		for s, n in num_strs.items():
			chunk = l[-i:]
			if chunk.startswith(s):
				num += n
				found = True
				break
		if found:
			break
			
	
	
	print(num)
	sum += int(num)
print(sum)

# 54937 too low
