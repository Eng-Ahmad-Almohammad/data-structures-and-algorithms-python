from data_structures_and_algorithms.data_structures.graph.graph import Graph

def get_edge(graph,cities):
    graph_nodes = graph.bft(cities[0])

    flag = False
    for i in graph_nodes:
        if i == cities[1]:
            flag = True
    if flag:
            for i in graph.adjacency.keys():
                if str(i.value) == str(cities[0]):
                
                   if len(graph.adjacency[i]) > 0:
                       for j in graph.adjacency[i]:
                           if j[1] == cities[1]:
                               return [True, f'${j[0]}']
                else:
                
                    continue
    return [False,'$0']

if __name__=='__main__':
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')
    graph.add_edge('a','b',4)
    graph.add_edge('a','d',9)
    graph.add_edge('a','c',3)
    graph.add_edge('b','a',4)
    graph.add_edge('c','a',3)
    graph.add_edge('c','d',6)
    graph.add_edge('d','a',9)
    graph.add_edge('d','b',5)
    graph.add_edge('d','c',6)
    print(get_edge(graph,['c','b']))
    print(get_edge(graph,['t','b']))
    print(get_edge(graph,['a','b']))

