# Q1. Algos CS 5800 - Abhi Shelat - HW 2

def get_routes_to_planets(n):
    arr = [i for i in range(1, n+1)]
    res = [] # to hold all route segments
    low = 0
    high = n-1
    # mid = (low + high)//2
    # for i in range(0, (mid+1)):
    #     res.append((arr[i], arr[high]))
    res = mergeSort(arr, low, high, res)
    print(len(res))
    print(res)
    print(len(list(set(res))))

def merge(arr, l, m, r, res):
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
    i = 0	 # Initial index of first subarray
    j = 0	 # Initial index of second subarray
    k = l	 # Initial index of merged subarray
    
    # # Connect from left subarray all elements to first element of right subarray
    # while i < n1 and j < n2:
    #     res.append((L[i], R[j]))
    #     #print((L[i], R[j]))
    #     if L[i] < R[j]:
    #         arr[k] = L[i]
    #         i += 1
            
    #     else:
    #         arr[k] = R[j]
    #         j += 1
            
    #     k += 1
        
    # Connect from left subarray all elements to first element of right subarray
    for ii in range(0, n1):
        if (L[ii], R[j]) not in res:
            res.append((L[ii], R[j]))
            # print((L[ii], R[j]))
    
    # Connect from right subarray first element to all other elements of right subarray
    for jj in range(1, n2):
        if (R[j], R[jj]) not in res:
            res.append((R[j], R[jj]))
            # print((R[j], R[jj]))

    # Copy the remaining elements of R[] to merged array for next merge
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

	# Copy the remaining elements of R[] to merged array for next merge
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r, res):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
        
        # Sort first and second halves
        mergeSort(arr, l, m, res)
        mergeSort(arr, m+1, r, res)
        merge(arr, l, m, r, res)
        
    return res


get_routes_to_planets(16)