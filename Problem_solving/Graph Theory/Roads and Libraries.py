# Error 
'''
5 3 6 1
1 2
1 3
1 4

output=> 15 ???? how????
'''

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 21-08-2022 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# problem name: Prepare>Algorithms>Graph Theory> Roads and Libraries
# problem link: https://www.hackerrank.com/challenges/torque-and-development/problem?isFullScreen=false

# Can be solved using BFS and DFS


from collections import defaultdict
# dfs for connected component
def dfs(visited, graph, root, path):
    if root not in visited:
        path.append(root)  # path for connected components
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited, graph, neighbour, path)
    return path  # return each connected components


q = int(input())
for i in range(q):
    num_cities, num_roads, c_lib, c_road = map(int, input().split())
    graph = defaultdict(list)
    for i in range(num_roads):
        x, y = map(int, input().split())
        if y not in graph[x]:
            graph[x].append(y)
        if x not in graph[y]:
            graph[y].append(x)
    min_cost = 0
    if c_lib >= c_road:
        min_cost = num_cities*c_lib
    else:
        visited = set()  # used as stack
        for i in range(1, num_cities):
            if i not in visited:
                path = []
                connected_component = dfs(visited, graph, i, path)
                ln = len(connected_component)
                # print('Component=> ', connected_component)
                if ln==1:
                    continue
                cost_per_comp = (ln-1)*c_road+c_lib
                min_cost = min_cost+cost_per_comp
    print(min_cost)
