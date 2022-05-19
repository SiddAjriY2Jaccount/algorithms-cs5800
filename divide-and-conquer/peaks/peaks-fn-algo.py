# The algorithm here is a slight tweak of the Merge Sort algorithm. The
# merge function has been changed to include a hashmap, to increment a counter
# for when element in right subarray is added to the merged array, then increment
# the count of that element in the hashmap by index 'i' which corresponds to index
# of left subarray. That way, the hashmap would give us the count of number of
# higher peaks to the left of every element. Applying this process again to the
# reversed array would fetch us the count of number of higher peaks to the right
# of every element. Summing up all these counts will give us the total sum of the
# alpine function.

# Runtime: O(n log n) [same as Merge Sort]

def merge(arr, l, m, r, counter_dict):
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0  # Initial index of first subarray
	j = 0  # Initial index of second subarray
	k = l  # Initial index of merged subarray

	while i < n1 and j < n2:
		if L[i] < R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]; counter_dict[R[j]] += i
			j += 1

		k += 1

	# Copy the remaining elements of L[], if there are any
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there are any
	while j < n2:
		arr[k] = R[j]; counter_dict[R[j]] += i
		j += 1
		k += 1

# l is for left index and r is right index of the sub-array of arr to be sorted


def mergeSort(arr, l, r, counter_dict):
    
	if l < r:

		# Same as (l+r)//2, but avoids overflow for large l and h
		m = l+(r-l)//2

		# Sort first and second halves
		mergeSort(arr, l, m, counter_dict)
		mergeSort(arr, m+1, r, counter_dict)
		merge(arr, l, m, r, counter_dict)


# Driver code to test above functions
arr = [1, 5, 3, 10, 12, 8, 4, 9]
n = len(arr)
print("Given array is:")
for i in range(n):
	print("%d" % arr[i], end=" ")

# initialize dictionary to store counts
counter_dict = {}
for ele in arr:
    counter_dict[ele] = 0

mergeSort(arr, 0, n-1, counter_dict)

print("\n\nSorted array is:")
for i in range(n):
	print("%d" % arr[i], end=" ")

print()
print("Counter:")
print(counter_dict)
print("ANSWER:")
print(sum(list(counter_dict.values())))