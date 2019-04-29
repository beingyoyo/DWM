import copy
import math

def findRank(iter_no):
    temp_u = copy.deepcopy(u)
    temp_v = copy.deepcopy(v)

    print("\nIteration %d: " % (iter_no))
    print("Hub rank:")
    for i in range(0, num_page):
        print("Rank {0}: {1}  Value: {2}".format(i + 1, characters[temp_u.index(max(temp_u))], max(temp_u)))
        if sorted(temp_u)[-1] == sorted(temp_u)[-2]:
            print("**Tie**")
        temp_u[temp_u.index(max(temp_u))] = 0

    print("\nAuthority rank:")
    for i in range(0, num_page):
        print("Rank {0}: {1}  Value: {2}".format(i + 1, characters[temp_v.index(max(temp_v))], max(temp_v)))
        if sorted(temp_v)[-1] == sorted(temp_v)[-2]:
            print("**Tie**")
        temp_v[temp_v.index(max(temp_v))] = 0


num_page = int(input("Enter number of pages: "))

characters = list(map(chr, range(ord('A'), ord('A') + num_page)))
print(characters)
matrix = [[0 for i in range(0, num_page)] for j in range(0, num_page)]
transpose = [[0 for i in range(0, num_page)] for j in range(0, num_page)]

for i in range(0, num_page):
    for j in range(0, num_page):
        matrix[i][j] = int(input("Is there a link from {0} to {1}: ".format(characters[i], characters[j])))
        transpose[j][i] = matrix[i][j]

# print(transpose)
# print(matrix)
iter_no = 1

iterations = int(input("Enter number of iterations: "))

u = [1] * num_page # hub weight vector
v = [0] * num_page # authority weight vector

for i in range(0, num_page):
    total = 0
    for j in range(0, num_page):
        total += transpose[i][j] * u[j]
    v[i] = total

for i in range(0, num_page):
    total = 0
    for j in range(0, num_page):
        total += matrix[i][j] * v[j]
    u[i] = total

findRank(iter_no)

for i in range(0, iterations):
    prev_u = copy.deepcopy(u)
    prev_v = copy.deepcopy(v)

    new_u = sum(map(lambda x: x * x, u))
    u = list(map(lambda x: round(x / math.sqrt(new_u), 3), u))

    new_v = sum(map(lambda x: x * x, v))
    v = list(map(lambda x: round(x / math.sqrt(new_v), 3), v))

    iter_no += 1

    findRank(iter_no)

    if prev_u == u and prev_v == v:
        break
