
def enter_graph():
	n = int(input("Enter Number of nodes: "))
	g = {}
	for i in range(n):
		node = input("Enter node " + str(i) + " -> ")
		l = list(input("Enter adjacency nodes (format: X,Y,Z..... for node " + node+ "->").split(","))
		if l == ['']:
			l = []
		g[node] = l
	print("Entered Graph:-> " + str(g))
	return g

def bfs_trav(visited, graph, node, l):
	visited.append(node)
	queue.append(node)
	while queue:
		s = queue.pop(0)
		l.append(s)
		for neighbour in graph[s]:
			if neighbour not in visited:
				visited.append(neighbour)
				queue.append(neighbour)
	return l

visited = [] # List to keep track of visited nodes.
queue = [] # Initialize a queue
graph = enter_graph()
start_node = list(graph.keys())[0]
l = bfs_trav(visited, graph, start_node, l=[])
print("BFS traversal for the given graph -> ", str(l))
ser = input("Enter Node to be searched -> ")
if ser in l:
	print("Node exists in the given graph.")
else:
	print("Node doesn't exist in the given graph.")
