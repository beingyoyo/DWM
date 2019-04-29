import collections
import statistics
import copy

# data = [2,4,6,3,31,12,15,16,38,35,14,21,23,25,30]
data = []
n = int(input("Enter no. of inputs: "))

for i in range(0,n):
	inp = int(input("Enter input %d: " % (i+1))) 
	data.append(inp)
no_of_clusters = int(input("Enter no. of clusters: "))
d = collections.OrderedDict()

for i in range(0,no_of_clusters):
	c = int(input("Enter c%d: " % (i+1)))
	d[c] = []
# print(d)
new_mean = [0 for i in range(0,no_of_clusters)]
old_mean = [1 for i in range(0,no_of_clusters)]

while new_mean != old_mean:
	for i in d.keys():
		d[i] = []
	for i in data:
		minimum = 999999
		index = 0
		for j in d.keys():
			temp = abs(j-i)
			if temp < minimum:
				minimum = temp
				index = j
		d[index].append(i)
	old_mean = copy.deepcopy(new_mean)
	k = 0
	for j in d.keys():
		new_mean[k] = statistics.mean(d[j]) 
		k += 1
	print(old_mean)	
	print(new_mean)
	print()
print(d)
k = 1
for i in d.keys():
	print("Cluster %d: " % (k),end="")
	print(d[i])