def skiracing(start, end):
    i = 0
    curstart = 8
    curend = 8
    curendidx = 0
    # sort by start times
    zipped = sorted(list(zip(start, end)), key = lambda x : x[0])
    (start, end) = ([ i for i, j in zipped ], [ j for i, j in zipped ])
    print(start)
    print(end)
    rangestart = start[0]
    
    solution = []
    while (rangestart < 20):
        curstart = start[i]
    
        if (curstart <= rangestart):
            if (end[i] > curend):
                curend = end[i]
                curendidx = i
            if i == len(start)-1:
                solution.append(curendidx)
                break
        else:
            solution.append(curendidx)
            rangestart = end[curendidx]
            i -= 1
            
        i += 1
    
    print("Instructor schedules chosen:")
    for i in solution:
        print(start[i], end[i])
    return len(solution)
    
start = [8, 8, 8, 10, 13, 15, 19]
end = [10, 13, 16, 11, 18, 20, 20]
print("Number of instructors needed is: " + str(skiracing(start, end)))
