def bfs(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked 
    queue = [start]
    # keep looping until there are nodes still to be checked
    while queue: #WHILE QUEUE IS NOT EMPTY
        # pop shallowest node (first node) from queue
        node = queue.pop(0) #REMOVE VERY FIRST NODE
        if node not in explored: #IF NODE IS DESTINATION, THEN THERE IS A PATH
            # add node to list of checked nodes
            explored.append(node)#MARK IT AS VISITED
            neighbours = graph[node]#FOR EACH NODE IN GRAPH, ADD TO NEIGHBORS

            # add neighbours of node to queue
            for neighbour in neighbours: #FOR EACH PATH IN NEIGHBORS
                queue.append(neighbour) # ADD TO QUEUE
    return explored

# Driver Code
graph = {'A': set(['B', 'C', 'E']),
         'B': set(['A','D', 'E']),
         'C': set(['A', 'F', 'G']),
         'D': set(['B']),
         'E': set(['A', 'B','D']),
         'F': set(['C']),
         'G': set(['C'])}


paths = bfs(graph,"G") # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']
print(paths)

