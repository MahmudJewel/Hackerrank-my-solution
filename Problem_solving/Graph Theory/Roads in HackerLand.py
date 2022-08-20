""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 14-08-2022 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#problem name: Prepare>Algorithms>Graph Theory>Roads in HackerLand
#problem link: https://www.hackerrank.com/challenges/johnland/problem?isFullScreen=false

from collections import defaultdict

def bfs(visited, queue, graph,weights, root):  # function for BFS
    visited.append(root)
    queue.append(root)
    sum=0
    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")
        temp=500
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                # shortest path
                print('values=> ', weights[m,neighbour])
                if weights[m,neighbour]<temp:
                    temp=weights[m,neighbour]
        sum=sum+temp
    return sum

cities, roads=map(int, input().split())
graph=defaultdict(list)
weights={}
for i in range(roads):
    x,y,w=map(int, input().split())
    if x not in graph[y]:
        graph[x].append(y)
        weights[x,y]=w
    if y not in graph[x]:
        graph[y].append(x)
        weights[y,x]=w
graph2=sorted(graph.values(), key=lambda ky:ky)
# print(graph.items())
# print(graph.keys())
# print('Graph-1 => ',graph)
# print('Graph-2 => ',graph2)
# print(weights)
visited=[]
queue=[]
root=1
sum=bfs(visited, queue, graph,weights, root)
print(sum)


