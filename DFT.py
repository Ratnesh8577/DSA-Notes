#Write a python program of DFT(Depth first traversal)
#function definition
def depthFirstTraversel(visited,graph,Node):
    if Node not in visited:
        print(Node,end=" ")
        visited.add(Node)
        for adjacentNodes in  graph[Node]:
            if adjacentNodes not in visited:
                depthFirstTraversel(visited,graph,adjacentNodes)

#Driver code 
#String the data of the graph using adjacency list
visited = set()
#Directed graph
graph = {
    '5': ['3','7'],
    '3': ['2','4'],
    '7': ['8'],
    '2': [''],
    '4': ['18'],
    '8': ['']
}
depthFirstTraversel(visited,graph,'5')