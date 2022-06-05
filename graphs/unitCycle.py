############################################################
# Starter code for finding cycles in graphs
# March 2022
# 
# This code is inspired heavily by 
# @adamdavisonsmith, Boston University 
############################################################



import sys
import os
import heapq
import queue
import numpy as np
import simplegraphs as sg


############################################################
#
# CODE FOR PART 1
#
############################################################


def DFSFindCycle(G):
    
    # This function should return a list containing the nodes in a cycle, or the empty list if no cycles exist.
    cycle = []
    # --- place your code here -----
    color = {}
    parent = {}
    for u in G["adj"]:
        color[u] = "white"
        parent[u] = None

    def DFSVisit(u, G, cycle, color):
        if len(cycle) > 0:
            return
        color[u] = "gray"
        for v in G["adj"][u]:
            if color[v] == "white":
                    parent[v] = u
                    DFSVisit(v, G, cycle, color)
            if len(cycle) > 0:
                return
            elif color[v] == "gray":
                if len(cycle) > 0:
                    return
                node = u
                while node != v and node != None:
                    cycle.append(node)
                    node = parent[node]
                if node == v:
                    cycle.append(node)
                    return
                else:
                    cycle = []
        color[u] = "black"
        return

    for u in G["adj"]:
        if color[u] == "white":
            DFSVisit(u, G, cycle, color)
            if len(cycle) > 0:
                return cycle[::-1]
    
    return cycle[::-1]

############################################################
#
# The remaining functions are for reading and writing outputs, and processing
# the command line arguments. You shouldn't have to modify them.
# 
############################################################

def main(args = []):
    # Expects 2 command-line arguments:
    # 1) name of a file describing the graph
    # 2) name of a file where the output should be written
    if len(args) < 2:
        print("Too few arguments! There should be at least 2.")
        return
    graph_file = args[0]
    out_file = args[1]
    G = sg.readGraph(graph_file) # Read the graph from disk

    cycles = DFSFindCycle(G)
    with open(out_file, 'w') as f:
        if len(cycles) > 0:
            print(cycles)
            f.write(f'{cycles}')
        else:
            print("no cycle found")
            f.write(f'no cycle found')

    return

if __name__ == "__main__":
    main(sys.argv[1:])