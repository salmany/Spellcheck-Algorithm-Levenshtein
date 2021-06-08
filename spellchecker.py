def spell_check (word, dictionary): #Levenshtein's Algorithm
	costs = [[0 for x in range(len(word)+1)] for x in range(len(dictionary)+1)]
	for x in range(len(costs)):
		costs[x][0] = x*5
	for x in range(len(costs[0])):
		costs[0][x] = x*5

	for x in range(1,len(dictionary)+1):
		for y in range(1,len(word)+1):
			if word[y-1] == dictionary[x-1]:
				price = 0
			else:
				price = 25
			costs[x][y] = min(costs[x-1][y]+20,costs[x][y-1]+20, costs[x-1][y-1]+price)
	print(costs)
