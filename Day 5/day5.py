almanac = open("data.txt").read()

min_location = 29164888782916488878
min_seed = 0

class Mapper:
	def __init__(self, data):
		self.map = {}
		self.sorted_spans = []
		for d in data:
			dest, src, ran = d.split(' ')
			dest = int(dest)
			src = int(src)
			ran = int(ran)
			map_min = src
			map_max = src + ran - 1
			self.map[(map_min, map_max)] = dest
			self.sorted_spans.append((map_min, map_max))
		
		self.sorted_spans.sort()
	
	def convert(self, init_val):
		for map_min, map_max in self.map:
			if map_min <= init_val <= map_max:
				offset = init_val - map_min
				return self.map[(map_min, map_max)] + offset
		
		return init_val
	
	def direct_convert(self, init_val, map_min, map_max):
		offset = init_val - map_min
		return self.map[(map_min, map_max)] + offset
	
	def convert_range(self, init_val, span):
		current_val = init_val
		remaining_span = span
		new_spans = []
		for map_min, map_max in self.sorted_spans:
			# three options:
			if map_max < current_val: # if map below current_seed
				continue # keep iterating to find intersect
			
			if map_min > current_val + remaining_span: # if map above seed span
				# add all remaining seed span
				new_spans.append((current_val, remaining_span))
				return new_spans
				
			# map intersects seed span
				# cut off below map
			if current_val < map_min:
				new_span = map_min - current_val
				new_spans.append((current_val, new_span))
				current_val = map_min
				remaining_span -= new_span
			
			# add new chunk of intersect
			intersect_span = map_max - current_val + 1
			new_spans.append((self.direct_convert(current_val, map_min, map_max), min(remaining_span, intersect_span)))
			
			# maybe continue
			if remaining_span > intersect_span:
				current_val = map_max + 1
				remaining_span -= intersect_span
			else:
				return new_spans
		new_spans.append((current_val, remaining_span))
		return new_spans
				
				
	"""
	1 2 3 4 5 6 7 8 9
			5 6 7
	"""
		

seeds, maps = almanac.split("\n\n", 1)

maps = maps.split('\n\n')

seed_to_soil = Mapper(maps[0].split('\n')[1:])
soil_to_fert = Mapper(maps[1].split('\n')[1:])
fert_to_water = Mapper(maps[2].split('\n')[1:])
water_to_light = Mapper(maps[3].split('\n')[1:])
light_to_temp = Mapper(maps[4].split('\n')[1:])
temp_to_humid = Mapper(maps[5].split('\n')[1:])
humid_to_loc = Mapper(maps[6].split('\n')[1:])

def convert_seed(seed):
	soil = seed_to_soil.convert(seed)
	fert = soil_to_fert.convert(soil)
	water = fert_to_water.convert(fert)
	light = water_to_light.convert(water)
	temp = light_to_temp.convert(light)
	humid = temp_to_humid.convert(temp)
	loc = humid_to_loc.convert(humid)
	return loc

for s in seeds.split(' ')[1:]:
	s = int(s)
	seed_loc = convert_seed(s)
	if seed_loc < min_location:
		min_location = seed_loc
		min_seed = s

print(f'{min_seed=}, at {min_location=}')

# Reset for part 2
min_location = 29164888782916488878

def convert_seed_ranges(init_seed, seed_span):
	soil_ranges = seed_to_soil.convert_range(init_seed, seed_span)
	fert_ranges = []
	for soil, span in soil_ranges:
		fert_ranges += soil_to_fert.convert_range(soil, span)
	water_ranges = []
	for fert, span in fert_ranges:
		water_ranges += fert_to_water.convert_range(fert, span)
	light_ranges = []
	for water, span in water_ranges:
		light_ranges += water_to_light.convert_range(water, span)
	temp_ranges = []
	for light, span in light_ranges:
		temp_ranges += light_to_temp.convert_range(light, span)
	humid_ranges = []
	for temp, span in temp_ranges:
		humid_ranges += temp_to_humid.convert_range(temp, span)
	loc_ranges = []
	for humid, span in humid_ranges:
		loc_ranges += humid_to_loc.convert_range(humid, span)
	
	return loc_ranges

seeds_line = [int(x) for x in seeds.split(' ')[1:]]
for i in range(0, len(seeds_line), 2):
	init_seed = seeds_line[i]
	seed_span = seeds_line[i+1]
	
	loc_ranges = convert_seed_ranges(init_seed, seed_span)
	min_loc_from_range = sorted(loc_ranges)[0][0]
	
	if min_loc_from_range < min_location:
		min_location = min_loc_from_range

print(f'{min_location=}')

# 127453946 too high