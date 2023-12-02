lines = [x.strip() for x in open("data.txt").readlines()]

MAXES = {
	"red": 12,
	"green": 13,
	"blue": 14
}

sum = 0
power_sum = 0
for l in lines:
	game, data = l.split(": ")
	game_id = int(game.split(' ')[-1])
	
	draws = data.split('; ')
	invalid = False
	mins = {
		'red': 0,
		'green': 0,
		'blue': 0
	}
	for d in draws:
		colours = d.split(', ')
		for c in colours:
			count, colour = c.split(' ')
			mins[colour] = max(mins[colour], int(count))
			if int(count) > MAXES[colour]:
				invalid = True
	if not invalid:
		sum += game_id
	
	power = mins['red'] * mins['green'] * mins['blue']
	power_sum += power
	
		
print(sum)
print(power_sum)