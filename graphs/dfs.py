import sys
import simplegraphs as sg
import numpy as np

def main(args = []):
    if len(args) < 1:
        print('Too few arguments! Usage: python3 dfs.py <filename>')
        return
    graph_file = args[0]
    G = sg.readGraph(graph_file) # Read the graph from disk
    print(G)
    discovered, finished, parent = sg.DFS(G)
    print(discovered)
    print(finished)
    print(parent)
    return

if __name__ == "__main__":
    main(sys.argv[1:]) 