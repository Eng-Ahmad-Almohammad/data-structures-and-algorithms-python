from data_structures_and_algorithms.data_structures.graph.graph import Graph



def depth_first(graph , start_node):
    flag = False
    for i in graph.adjacency.keys():
        if str(i.value) == str(start_node):
                
            flag = True
            break
        else:
                
            flag = False
        
    if flag:
        visited = set([])
        nodes = [start_node]
        output = [start_node]
        visited.add(start_node)
        while len(nodes) > 0:
            # print(nodes)
            last_node = nodes[len(nodes)-1]
            # print(last_node)
            for i in graph.adjacency.keys():
                if str(i.value) == str(last_node):
                    for j in graph.adjacency[i]:
                        # print(j)
                        if not j[1] in visited:
                            nodes.append(j[1])
                            # print(nodes)
                            visited.add(j[1])
                            output.append(j[1])
                        else:
                            if len(nodes) >0:
                                nodes.pop()
                    break
                        
                else:
                    continue
                
        return output

    else:
        return "Invalid Input"


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
    print(depth_first(graph,'a'))