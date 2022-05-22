size_of_grid = 0
b = 0
a = 0
cnt = 0
arr = [[0 for i in range(128)] for j in range(128)]

def place(x1, y1, x2, y2, x3, y3):
	global cnt
	cnt += 1
	arr[x1][y1] = cnt;
	arr[x2][y2] = cnt;
	arr[x3][y3] = cnt;
	
def tile(n, x, y):
	global cnt
	r = 0
	c = 0
	if (n == 2):
		cnt += 1
		for i in range(n):
			for j in range(n):
				if(arr[x + i][y + j] == 0):
					arr[x + i][y + j] = cnt
		return 0;
	for i in range(x, x + n):
		for j in range(y, y + n):
			if (arr[i][j] != 0):
				r = i
				c = j
	# upper left
	if (r < x + n / 2 and c < y + n / 2):
		place(x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2), y + int(n / 2), x + int(n / 2) - 1, y + int(n / 2))
	# upper right
	elif(r >= x + int(n / 2) and c < y + int(n / 2)):
		place(x + int(n / 2) - 1, y + int(n / 2), x + int(n / 2), y + int(n / 2), x + int(n / 2) - 1, y + int(n / 2) - 1)
	# lower left
	elif(r < x + int(n / 2) and c >= y + int(n / 2)):
		place(x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2), y + int(n / 2), x + int(n / 2) - 1, y + int(n / 2) - 1)
	# lower right
	elif(r >= x + int(n / 2) and c >= y + int(n / 2)):
		place(x + int(n / 2) - 1, y + int(n / 2), x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2) - 1, y + int(n / 2) - 1)
	
	tile(int(n / 2), x, y + int(n / 2)); # lower left
	tile(int(n / 2), x, y); # upper left
	tile(int(n / 2), x + int(n / 2), y); # upper right
	tile(int(n / 2), x + int(n / 2), y + int(n / 2)); # lower right
	
	return 0

size_of_grid = 8
a = 7
b = 7
arr[a][b] = -1
tile(size_of_grid, 0, 0)

for i in range(size_of_grid):
	for j in range(size_of_grid):
		print(arr[i][j], end=" ")
	print()

d = {}
for i in range(size_of_grid):
	for j in range(size_of_grid):
			if arr[i][j] in d.keys():
				d[arr[i][j]].append((i, j))
			else:
				d[arr[i][j]] = []
				d[arr[i][j]].append((i, j))
	print()

print()
# print(cnt)
# print(len(d.values()))

## -1 will denote the empty square that cannot be tiled by trominos