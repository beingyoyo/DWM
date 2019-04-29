import collections
import copy

def rank(i):
	inbound_list = [characters.index(k) for k in links[characters[i]]['inbound']]
	outbound_count = [len(links[characters[k]]['outbound']) for k in inbound_list]
	pg_rank = 0

	for j,k in zip(inbound_list,outbound_count):
		if(k == 0):
			continue
		pg_rank += page_rank[j]/k
		# print(j,k)
	return pg_rank


num_page = int(input("Enter number of pages: "))

matrix = [[0 for i in range(0,num_page)] for j in range(0,num_page)]

characters = list(map(chr,range(ord('A'),ord('A')+num_page)))
# print(characters)

links = collections.OrderedDict()

for i in characters:
	links[i] = {}
	links[i]['inbound'] = []
	links[i]['outbound'] = []

for i in range(0,num_page):
	for j in range(0,num_page):
		matrix[i][j] = int(input("Is there a link from {0} to {1}: ".format(characters[i],characters[j])))
		if(matrix[i][j] == 1):
			links[characters[i]]['outbound'].append(characters[j])
			links[characters[j]]['inbound'].append(characters[i])

# print(links)

damping_factor = float(input("\nEnter the damping factor: "))

prev_page_rank = []

#Initialize by 1/no. of pages 
# page_rank = [1/num_page] * num_page

#Initialize by 1
page_rank = [1] * num_page

# print(page_rank)

iterations = int(input("\nEnter number of iterations: "))

for n in range(0,iterations):
	prev_page_rank = copy.deepcopy(page_rank)
	for i in range(0,len(characters)):
		page_rank[i] = round((1 - damping_factor) + damping_factor * rank(i),3)
	print("Iteration {0}: {1}".format(n+1,page_rank))
	if(prev_page_rank == page_rank):
		break

print("\n")

for i in range(0,num_page):
	print("Rank {0}: {1}".format(i+1,characters[page_rank.index(max(page_rank))]))
	page_rank[page_rank.index(max(page_rank))] = 0
