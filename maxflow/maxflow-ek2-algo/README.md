# maxflow using edmonds-karp algorithm

## How to run
```python flows.py <function-name> <input-file-name.txt>```

where ```<function-name>``` can be ```gold``` or ```rounding``` and sample input files are provided in the ```examples``` folder.

## Explanation
This is a 3-part question wherein we write the following functions in the ```flows.py``` file.

#### 1) Compute Maxflow using Edmonds-Karp algorithm
- This is done by using a breadth-first search to find augmenting paths by finding shortest path (in terms of number of edges) from source to sink
- After determining if an augmenting path exists, push flow across this path, while also adding the residual edges. Whenever you push flow along the edge (x, y), residual edge flow with the same amount of capacity along the edge (y, x) must be added. Similarly, if after pushing a flow, an edge has 0 remaining capacity, it is removed from the graph so that the BFS routine does not use it.
- After doing this until edges outgoing from source are saturated, compute maxflow as a summation of every flow that was pushed through each augmenting path.

#### 2) Determine matching gold of bullion tiles using Maximal Bipartite Matching
In the ruins of Pompeii one finds the House of the Tragic Poet which has a famous mosaic floor proclaiming visitors to ``Beware of the Dog." In Boston, a less tragic but wealthier poet has commissioned a mosaic using 1kg bars of solid gold, specifically the type CreditSuisse mints in the dimension 80mmx40mm.

The input will consist of a file that gives the coordinates of the squares on an imaginary grid that should be covered by goldbars. These coordinates will be in the range [1,2000] in both the x and y directions. The output should consists of a list of tiles, one per line. Each tile should be designated by one of its coordinates, followed by ‘–>’ followed by the second coordinate. The tiles can be presented in any order, as our autograder will ensure that the entire input is covered. If the input cannot be tiled, then your program should output ‘No solution exists’.

An example input and output:
```
$ cat gold.3.txt
2 3
2 4
2 5
3 5
4 5
4 6
4 7
4 8
4 9
5 5
$ python3 flows.py gold gold.3.txt
2 4 --> 2 3
3 5 --> 2 5
4 6 --> 4 7
4 8 --> 4 9
5 5 --> 4 5
```

Design an algorithm that takes such a specification as input and determines if the indicated squares in the design can be entirely covered with gold bullion bars. Note that gold bars can never be split in half. Each gold bar covers exactly two of the squares.

The idea behind this algrothm is as follows:
- We are going to make a bipartite graph out of the design and then check whether it has a maximal matching. If it has a maximal matching, then the design can be tiled. 
- To construct the bipartite graph, imagine the design is inscribed in a checkerboard (i.e. the design fits into some j x j region). 
- The left side of this bipartite graph will consist of all the white squares of the checkerboard that are part of the design. 
- The right side consists of all of the black squares of the checkerboard that are part of the design. 
- Draw an edge from every white square to the black squares that are adjacent. This forms the bipartite graph.

#### 3) Determine if matrix values can be rounded
Suppose we are given a large matrix ```A[1...r][1...c]``` of population data (each entry is a non-negative number). We want to publish matrix ```A```, but need to simplify it for the public by rounding the entries into tens by replacing each entry x in A with either ```ceil(x/10)``` or ```floor(x/10)``` (the same trick can be used to round to thousands, etc). However, the matrix represents important statistical data, and we do not want to change the sums of entries in any row or column.

Sample input and output:
```
$ cat 3.3.txt 
12  34  24
39  40  21
79  16  5

$ python3 flows.py rounding 3.3.txt
20 30 20
40 40 20
70 20 10
```

To solve this:
- The algorithm should check if any row or column sums to a value that is not divisible by 10. If so, then there is no solution since it is not possible to round without changing that particular row/column sum and the program should output 'No solution exists'. If all rows and columns have sums that are divisible by 10, then the algorithm proceeds to use max flow to check if rounding is possible.
- Then, construct a graph similar to the bipartite matching problem. Create vertices $r_1$, ..., $r_m$ representing a row of $A$ and vertices $c_1$, ..., $c_n$ representing a column of $A$. We have a directed edge from $r_i$ to $c_j$ if and only if $A[i][j]$ is not divisible by 10. The capacity of the edge (if it exists) is $c(r_i, c_j)$ = 10.
- Additionally we add a source vertex $s$ and a sink vertex $t$. There is an edge from $s$ to every row vertex $r_i$ with capacity $c(s, r_i)$ = Sum of all $A[i][j]$ mod 10 i.e. sum of the remainders of entries in row $i$. There is also an edge from every column vertex $c_j$ to $t$ with capacity $c(c_j, t)$ = Sum of all $A[i][j]$ mod 10 i.e. sum of the remainders of entries in column $j$.
- Refer the comments in the code for further explanation.

## Runtime
Edmonds Karp algorithm runs in O($VE^2$) time.

## References
```simplegraphs.py``` by Adam Smith

