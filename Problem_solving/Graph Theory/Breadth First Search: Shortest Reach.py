""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 13-08-2022 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Prepare>Algorithms>Graph Theory>Breadth First Search: Shortest Reach
#problem link: https://www.hackerrank.com/challenges/bfsshortreach/problem

from collections import defaultdict

queue = []  # Initialize a queue
def bfs(visited, queue, graph, root, num_of_node):  # function for BFS
    visited.append(root)
    queue.append(root)
    level=[None]*(num_of_node+1)
    level[root]=0
    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        # print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                level[neighbour]=level[m]+1
                visited.append(neighbour)
                queue.append(neighbour)
    return level
# main code 
TEST=int(input())
for _ in range(TEST):
    graph=defaultdict(list)
    num_of_node, num_of_edge=map(int, input().split())
    for _ in range(num_of_edge):
        u,v=map(int, input().split())
        if u not in graph[v]:
            graph[v].append(u)
        if v not in graph[u]:
            graph[u].append(v)
    root=int(input())
    # print(graph)
    visited=[]
    queue = []  # Initialize a queue
    level=bfs(visited, queue, graph, root, num_of_node)
    # print(level)
    for i in range(1,num_of_node+1):
        if i==root:
            continue
        elif level[i]==None:
            print('-1', end=' ')
        else:
            print(level[i]*6, end=' ')
    print(end='\n')