from collections import defaultdict

queue = []  # Initialize a queue
def bfs(visited, graph, node):  # function for BFS
    visited.append(node)
    queue.append(node)

    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# main code 
TEST=int(input())
for _ in range(TEST):
    graph=defaultdict(list)
    num_of_node, num_of_edge=map(int, input().split())
    for _ in range(num_of_edge):
        u,v=input().split()
        if u not in graph[v]:
            graph[v].append(u)
        if v not in graph[u]:
            graph[u].append(v)
    print(graph)