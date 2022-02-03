"""
Input: DirectedGraph graph = (Verticies V, Edges E)
Output: The strongly connected components of the graph, SCCs.

Pseudocode
tarjans(G=V,E):
    global Stack stack
    global int vertex_count

    for each v in V do:
        strongConnect(v)
    end for
end tarjans

strongConnect(v):
    stack.push(v)
    v.index = vertex_count
    v.lowlink = vertex_count
    vertex_count += 1

    for each w in v.neighbours:
        if w.is_undefined:
            strongConnect(w)
            v.lowlink = min(w.lowlink, v.lowlink)
        endif
        elif w.is_on_stack:
            v.lowlink = min(w.index, v.lowlink)
        endelif
    endfor

    SCC = []
    do:
        x = stack.pop()
        SCC.add(x)
    while (v != x)
    
    print(SCC)
"""

"""
Example Graph 1.
0: 1
1: 2
2: 0
"""

from collections import deque


def tarjan(graph):
    n_verticies = len(graph)
    INDEX = 0
    LOWLINK = 1
    UNDEFINED = 2
    ONSTACK = 3

    stack = deque()
    vertex_data = [[0,0,True,False] for x in range(n_verticies)]
    i = 0 

    
    
    def strong_connect(v, i):
        stack.append(v)
        print(stack)
        vertex_data[v][INDEX] = i
        vertex_data[v][LOWLINK] = i
        vertex_data[v][UNDEFINED] = False
        vertex_data[v][ONSTACK] = True
        i += 1

        for w in graph[v]:
            if vertex_data[w][UNDEFINED]:
                strong_connect(w, i)
                vertex_data[v][LOWLINK] = min(vertex_data[v][LOWLINK], vertex_data[w][LOWLINK])
            elif vertex_data[w][ONSTACK]:
                vertex_data[v][LOWLINK] = min(vertex_data[v][LOWLINK], vertex_data[w][INDEX])

        SCC = []
        if vertex_data[v][LOWLINK] == vertex_data[v][INDEX]:
            while True:
                x = stack.pop()
                vertex_data[x][ONSTACK] = False
                SCC.append(x)

                if v == x:
                    break

            print(SCC)

    for v in range(n_verticies):
        if vertex_data[v][UNDEFINED]:
            strong_connect(v, i)

adjcency_list = [[1], [2], [0]]
print(tarjan(adjcency_list))









    
