from math import ceil, floor, sqrt

times, distances = [[int(val) for val in x.strip().split()[1:]] for x in open("data.txt").readlines()]

def range_to_win(time, distance):
	press_a = (time + sqrt(time**2 - 4 * distance))/2
	press_b = (time - sqrt(time**2 - 4 * distance))/2
	
	answer = sorted([press_a, press_b])
	answer = [ceil(answer[0] + 0.1), floor(answer[1] - 0.1)] # add and remove small buffer to ensure a win. Probably smarter ways to do this
	return answer
	
product = 1
for i in range(len(times)):
	time = times[i]
	dist = distances[i]
	winning_range = range_to_win(time, dist)
	margin = winning_range[1] - winning_range[0] + 1
	product *= margin

print(product)

big_time = int(''.join([str(x) for x in times]))
big_distance = int(''.join([str(x) for x in distances]))

winning_range = range_to_win(big_time, big_distance)
margin = winning_range[1] - winning_range[0] + 1
print(margin)