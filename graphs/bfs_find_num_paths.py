import sys
import heapq
import queue
import numpy as np
import simplegraphs as sg

def BFS(G, s):
    # G is a dictionary with keys "n", "m", "adj" representing an unweighted graph
    # G["adj"][u][v] is True if (u,v) is present. Otherwise, v is not in G["ad"][u].
    distances = [float('inf') for i in range(G["n"])]
    paths = [0 for i in range(G["n"])]
    # finalized = {} # set of discovered nodes
    # parents = {} # lists parent of node in SP tree
    # layers = [[] for d in range(G["n"])] # lists of nodes at each distance.
    Q = queue.Queue()
    distances[s] = 0
    paths[s] = 1
    visited = [False for i in range(G["n"])]
    visited[s] = True
    Q.put(s)
    while not(Q.empty()): #Q not empty
        u = Q.get()
        for v in G["adj"][u]:
            if visited[v] == False:
                Q.put(v)
                visited[v] = True
            if distances[v] > distances[u] + 1:
                distances[v] = distances[u] + 1
                paths[v] = paths[u]
            elif distances[v] == distances[u] + 1:
                paths[v] = paths[v] + paths[u]
    
    for idx, i in enumerate(paths):
        print("Number of shortest paths from " + str(s) + " to " + str(idx) + " : " + str(i))            

    #     if u not in finalized: #if u was already finalized, ignore it.
    #         finalized[u] = True
    #         layers[distances[u]].append(u) 
    #         for v in G["adj"][u]:
    #             # record v's distance and parent and add v to the queue if  
    #             # this is the first path to v,  
    #             if (v not in distances): # first path to v
    #                 distances[v] = distances[u] + 1
    #                 parents[v] = u
    #                 Q.put(v)
    # return distances, parents, layers

def main(args = []):
    if len(args) < 1:
        print('Too few arguments! Usage: python3 bfs_find_num_paths.py <filename>')
        return
    graph_file = args[0]
    G = sg.readGraph(graph_file) # Read the graph from disk
    source = 0
    BFS(G, source)
    return

if __name__ == "__main__":
    main(sys.argv[1:])