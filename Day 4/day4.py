lines = [x.strip().replace("   ", " ").replace("  ", " ") for x in open("data.txt").readlines()]

total = 0

card_cache = {}
def card_score(card):
	id, nums = card.split(": ")
	if id in card_cache:
		return card_cache[id]
	
	winning_nums, card_nums = nums.split(" | ")
	winning_set = {int(x) for x in winning_nums.split(" ")}
	card_set = {int(x) for x in card_nums.split(" ")}
	
	intersect = winning_set.intersection(card_set)
	
	score = 0
	if len(intersect) != 0:
		score = 2**(len(intersect) - 1)
	
	card_cache[id] = score
	return score

matches_cache = {}
def card_matches(card):
	id, nums = card.split(": ")
	if id in matches_cache:
		return matches_cache[id]
	
	winning_nums, card_nums = nums.split(" | ")
	winning_set = {int(x) for x in winning_nums.split(" ")}
	card_set = {int(x) for x in card_nums.split(" ")}
	
	intersect = winning_set.intersection(card_set)
	
	score = len(intersect)
		
	matches_cache[id] = score
	return score

# Part 1
for card in lines:
	total += card_score(card)
print(total)

# Part 2
added_cache = {}
def added_cards(card):
	id, nums = card.split(": ")
	id = int(id.split(" ")[1])-1
	if id in added_cache:
		return added_cache[id]
	
	score = card_matches(card)
	
	new_card_ids = list(range(id+1, min(id+1+score, len(lines))))
	
	added_cache[id] = new_card_ids
	return new_card_ids

card_counts = {x: 1 for x in range(len(lines))}

for id in range(len(lines)):
	count = card_counts[id]
	new_cards = added_cards(lines[id])
	for nc in new_cards:
		card_counts[nc] += count

print(sum(card_counts.values()))
#cards_done = 0
#cards_to_count = list(range(len(lines)))
#while len(cards_to_count) > 0:
#	card_id = cards_to_count.pop(0)
#	cards_done += 1
#	new_cards = card_score(lines[card_id])
#	for i in range(card_id+1, min(card_id+1+new_cards, len(lines)-1)):
#		cards_to_count.append(i)
#print(cards_done)