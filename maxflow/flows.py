#!/usr/local/bin/python3
############################################################
# Starter code for solving flow problems in graphs
# April 2022
# 
############################################################
import sys
import numpy as np
import simplegraphs as sg

MAX_WIDTH = 2000
MAX_HEIGHT = 2000

def gold(coords):
    # write your code here
    def are_adjacent_tiles(x1, y1, x2, y2):
        if x1 == x2 and abs(y1 - y2) == 1:
            return True
        elif y1 == y2 and abs(x1 - x2) == 1:
            return True
        return False

    white_tiles = {}
    black_tiles = {}

    # Determine whether tile coordinates provided
    # as input are white or black tiles of an 
    # infinite checkerboard
    for idx, coord in enumerate(coords):
        if ((coord[0] % 2) == (coord[1] % 2)):
            white_tiles[idx + 1] = coord
        else:
            black_tiles[idx + 1] = coord

    # If the number of white and black tiles are
    # not equal, then no solution is possible
    if (len(white_tiles) != len(black_tiles)):
        print('No solution exists')
        return []

    # Create a new graph with all tiles 
    # plus source and sink nodes 
    G = sg.emptyGraph(len(coords) + 2)
    
    source = 0
    sink = len(coords) + 1
    
    # Make unit edge weight connections from source
    # to all nodes in left half of bipartite graph
    for l, vertex in white_tiles.items():
        sg.addDirEdge(G, source, l, 1)

    # Make unit edge weight connections from every node 
    # in left half to every node in right help where the 
    # node in left half is a tile adjacent to the the node 
    # in right half that it is being connected to
    for u, left_tile in white_tiles.items():
        for v, right_tile in black_tiles.items():
            if are_adjacent_tiles(left_tile[0], left_tile[1], right_tile[0], right_tile[1]):
                sg.addDirEdge(G, u, v, 1)

    # Make unit edge weight connections from all 
    # nodes in right half of bipartitie graph to the sink
    for r, vertex in black_tiles.items():
        sg.addDirEdge(G, r, sink, 1)

    # Run Maxflow (EK algorithm)
    aug_paths, flow_in_edges, maxflow_value, newG = maxflow(G, source, sink)

    for key, val in flow_in_edges.items():
        if key in flow_in_edges and key[::-1] in flow_in_edges:
            flow_in_edges[key] = 0
            flow_in_edges[key[::-1]] = 0

    # Consider all middle edges. For every 
    # middle edge with flow = 1, a matching exists
    bipartite_matching = {}
    for edge, flow in flow_in_edges.items():
        if flow == 0:
            continue
        elif edge[0] == source or edge[1] == sink:
            continue
        else:
            bipartite_matching[edge[0]] = edge[1]

    # Print the matching obtained
    for vert in bipartite_matching:
        print(str(coords[vert-1][0]) 
        + " " 
        + str(coords[vert-1][1]) 
        + " --> " 
        + str(coords[bipartite_matching[vert]-1][0]) 
        + " " 
        + str(coords[bipartite_matching[vert]-1][1]))

    return []


def rounding(matrix):
    # write your code here
    G = sg.emptyGraph(0)
    
    source = "s"
    sink = "t"
    
    r = len(matrix)
    c = len(matrix[0])

    # Check if solution is even possible by 
    # checking if sum of row and column 
    # values is divisible by 10.
    for row in matrix:
        if (sum(row) % 10) != 0:
            print("No solution exists")
            return matrix
    for col in np.array(matrix).T:
        if (sum(col) % 10) != 0:
            print("No solution exists")
            return matrix
    
    # Create middle edges of bipartite graph
    # by adding an edge from ri to cj if and 
    # only if  is not divisible by 10.
    for i in range(r):
        for j in range(c):
            if ((matrix[i][j] % 10) != 0):
                sg.addDirEdge(G, str("r" + str(i)), str("c" + str(j)), 10)
    
    # Create connections from source to left 
    # half of graph with capacity values equal 
    # to sum of remainders when divided by 10
    for i in range(r):
        capacity = 0
        for j in range(c):
            capacity += (matrix[i][j] % 10)
        sg.addDirEdge(G, source, str("r" + str(i)), capacity)
    
    # Create connections from right half
    # of graph to sink with capacity values 
    # equal to sum of remainders divided by 10
    for j in range(c):
        capacity = 0
        for i in range(r):
            capacity += (matrix[i][j] % 10)
        sg.addDirEdge(G, str("c" + str(j)), sink, capacity)

    # Run Maxflow (EK algorithm)
    aug_paths, flow_in_edges, maxflow_value, newG = maxflow(G, source, sink)

    # Solution exists only if all edges 
    # from source are saturated
    round_ceil = []
    if (len(newG["adj"][source]) == 0):
        for i in flow_in_edges:
            if (i[0] != source) and (i[1] != sink) and (i[::-1] not in flow_in_edges):
                u = i[0]
                v = i[1]
                # if flow_in_edges[i] == G["adj"][u][v]:
                round_ceil.append((int(u[1:]), int(v[1:])))
        
        for i in range(r):
            for j in range(c):
                if (i, j) in round_ceil:
                    matrix[i][j] = matrix[i][j] + 10 - ((matrix[i][j]) % 10)
                else:
                    matrix[i][j] = matrix[i][j] - ((matrix[i][j]) % 10)
        
        return matrix
    
    else:
        print("No solution exists")
        return matrix

def maxflow(G, s, t):
    Gf = sg.copyGraph(G)
    # write your code below this point
    augmenting_paths = []
    flow_through_edges = {}
    maxflow = 0

    sink = t
    while(True):
        path = list()
        t = sink

        distances, parents, layers = sg.BFS(Gf, s)
        try:
            while(parents[t] != None):
                path.append((parents[t], t))
                t = parents[t]
        except:
            break
        if len(path) == 0:
            break

        bottleneck_cap = float("inf")

        path = path[::-1]
        augmenting_paths.append(path)

        # Find bottleneck capacity of the augmenting path
        for edge in path:
            bottleneck_cap = min(bottleneck_cap, Gf["adj"][edge[0]][edge[1]])

        # Record the flow through every edge
        for edge in path:
            if edge in flow_through_edges:
                flow_through_edges[edge] += bottleneck_cap
            else:
                flow_through_edges[edge] = bottleneck_cap

        # Remove critical edges and reduce capacities of 
        # edges through which some flow has already passed
        for edge in path:
            u = edge[0]
            v = edge[1]

            # If edge becomes critical and reaches full 
            # capacity, add a back edge in the opposite 
            # direction with capacity equal to the flow
            if Gf["adj"][u][v] == bottleneck_cap:
                sg.delEdge(Gf, u, v)
                sg.addDirEdge(Gf, v, u, bottleneck_cap)
            else:
                Gf["adj"][u][v] -= bottleneck_cap
        
        maxflow += bottleneck_cap

    return augmenting_paths, flow_through_edges, maxflow, Gf

############################################################
#
# The remaining functions are for reading and writing outputs, and processing
# the command line arguments. You shouldn't have to modify them.  You can use them to 
# help you test
# 
############################################################

def main(args = []):
    # Expects 2 command-line arguments:
    # 1) name of a file describing the graph
    if len(args) < 2:
        print("Too few arguments! There should be at least 4.")
        print("flows.py <cmd> <file>")
        return

    task = args[0]
    if task == "gold":
        coords = read_input(args[1])
        gold(coords)   
    elif task == "rounding":
        matrix = read_input(args[1])
        nm = rounding(matrix)
        if compare_matrix(matrix, nm):
            print_matrix(nm)
    elif task == "maxflow":
        # the following may help you test your maxflow solution
        graph_file = args[1]
        s = int(args[2])
        t = int(args[3])
        G = sg.readGraph(graph_file) # Read the graph from disk
        flow = maxflow(G, s, t)
        print(flow)

    return


def read_input(filename):
    with open(filename, 'r') as f:
        blocks = [[int(x) for x in s.split()] for s in f.read().splitlines()]
    return blocks

def print_matrix(matrix):
    for r in matrix:
        print(*r)

# verifies that two matricies have the same size, same row and column sums
def compare_matrix(m1,m2):
    r1 = len(m1)
    r2 = len(m2)
    c1 = len(m1[0])
    c2 = len(m2[0])
    if r1!=r2 or c1!=c2:
        print('Sizes are different')
        return False

    for ri in range(0,r1):
        rs1 = sum(m1[ri])
        rs2 = sum(m2[ri])
        if rs1 != rs2:
            print('Row sum {ri} differ: {rs1} != {rs2}')
            return False

    for cj in range(0,c1):
        cs1 = 0
        cs2 = 0
        for i in range(0,r1):
            cs1 += m1[i][cj]
            cs2 += m2[i][cj]
        if cs1 != cs2:
            print('Col sum {cj} differ: {cs1} != {cs2}')
            return False

    return True

if __name__ == "__main__":
    main(sys.argv[1:])