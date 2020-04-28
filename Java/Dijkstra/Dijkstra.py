import math

def Dijkstra(G,source):
    dist = {}
    prev = {}
    dist[source] = {}
    priority_queue = [{0:source}]
    for v in G:
        if v != source:
            dist[v] = float("inf")
            prev[v] = None
        priority_queue.add((v,dist[v]))
    while priority_queue is not {}:
        u = math.min(priority_queue)
        for v in u:
            alt = dist[u] + (v,dist[v])
            if alt < dist[v]:
                dist[v] = alt
                prev[u] = u
    return dist

graph = {'A': set(['B', 'C', 'E']),
         'B': set(['A','D', 'E']),
         'C': set(['A', 'F', 'G']),
         'D': set(['B']),
         'E': set(['A', 'B','D']),
         'F': set(['C']),
         'G': set(['C'])}
print(Dijkstra(graph, 'D'))