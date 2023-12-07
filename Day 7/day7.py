lines = [x.strip() for x in open('data.txt').readlines()]

def card_sort_key(card):
	if card == 'A':
		return 14
	if card == 'K':
		return 13
	if card == 'Q':
		return 12
	if card == 'J':
		return 11
	if card == 'T':
		return 10
	return int(card)

def make_hand_rank(hand):
	hand_set = list(set(hand))
	hand_rank = 7
	if len(hand_set) == 1:
		hand_rank = 7 # five of a kind
	elif len(hand_set) == 2:
		if hand.count(hand_set[0]) == 4 or hand.count(hand_set[0]) == 1:
			hand_rank = 6 # four of a kind
		else:
			hand_rank = 5 # full house
	elif len(hand_set) == 3:
		if hand.count(hand_set[0]) == 3 or hand.count(hand_set[1]) == 3 or hand.count(hand_set[2]) == 3:
			hand_rank = 4 # three of a kind
		else:
			hand_rank = 3 # two pair
	elif len(hand_set) == 4:
		hand_rank = 2 # pair
	else:
		hand_rank = 1 # high card
		
	card_ranks = (card_sort_key(c) for c in hand)
	
	return (hand_rank,) + tuple(card_ranks)

ranked_bids = []

for l in lines:
	hand, bid = l.split(' ')
	ranked_bids.append((make_hand_rank(hand), int(bid), hand))

ranked_bids.sort()

winnings = 0
for i in range(len(ranked_bids)):
	winnings += (i + 1) * ranked_bids[i][1]

print('Part 1:', winnings)

def card_sort_key_2(card):
	if card == 'A':
		return 14
	if card == 'K':
		return 13
	if card == 'Q':
		return 12
	if card == 'J':
		return 1
	if card == 'T':
		return 10
	return int(card)

def convert_jokers(hand):
	if 'J' not in hand:
		return hand
	
	# Find most common other card.
	# Replace Js with that
	filtered_hand = hand.replace('J', '')
	if not filtered_hand:
		return hand
	filtered_hand = sorted(list(filtered_hand), key=lambda x: filtered_hand.count(x), reverse=True)
	converted_hand = hand.replace('J', filtered_hand[0])
	return converted_hand

def make_hand_rank_2(hand):
	converted_hand = convert_jokers(hand)
	hand_set = list(set(converted_hand))
	hand_rank = 7
	if len(hand_set) == 1:
		hand_rank = 7 # five of a kind
	elif len(hand_set) == 2:
		if converted_hand.count(hand_set[0]) == 4 or converted_hand.count(hand_set[0]) == 1:
			hand_rank = 6 # four of a kind
		else:
			hand_rank = 5 # full house
	elif len(hand_set) == 3:
		if converted_hand.count(hand_set[0]) == 3 or converted_hand.count(hand_set[1]) == 3 or converted_hand.count(hand_set[2]) == 3:
			hand_rank = 4 # three of a kind
		else:
			hand_rank = 3 # two pair
	elif len(hand_set) == 4:
		hand_rank = 2 # pair
	else:
		hand_rank = 1 # high card
		
	card_ranks = (card_sort_key_2(c) for c in hand)
	
	return (hand_rank,) + tuple(card_ranks)

ranked_bids = []

for l in lines:
	hand, bid = l.split(' ')
	ranked_bids.append((make_hand_rank_2(hand), int(bid), hand))
	
ranked_bids.sort()

winnings = 0
for i in range(len(ranked_bids)):
	winnings += (i + 1) * ranked_bids[i][1]
	
print('Part 2:', winnings)