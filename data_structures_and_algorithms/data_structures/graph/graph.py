class Node:
    def __init__(self, value):
        self.value = value


class Graph:
    def __init__(self):
        self.adjacency = {}


    def add_node(self ,value):
        node = Node(value)
        self.adjacency[node] = []
        return node.value

    
    def add_edge(self, first_node, second_node, weight=1):
        flag = False
        for i in self.adjacency.keys():
            if str(i.value) == str(first_node):
                
                flag = True
                break
            else:
                
                flag = False
        
        for i in self.adjacency.keys():
            if str(i.value) == str(second_node):
                
                flag = True
                break
            else:
                flag = False
       
        if flag:
            for i in self.adjacency.keys():
                if str(i.value) == str(first_node):
                
                    self.adjacency[i].append([weight,second_node])

                    break
                else:
                
                    continue
            # self.adjacency[Node(first_node)].append([weight,second_node])
            
        else:
            return 'Node does not exist'
        

    def get_nodes(self , start_node):
        if self.bft(start_node):
            return self.bft(start_node)
        else:
            return 'Node does not exist'


    def get_neighbors(self,node):
        if self.bft(node):
            for i in self.adjacency.keys():
                if str(i.value) == str(node):
                
                    return self.adjacency[i]

                    
                else:
                
                    continue
        else:
            return 'Node does not exist'



    def size(self):
        first_node = list(self.adjacency.keys())[0].value

        if self.bft(first_node):
            return len(self.bft(first_node))
        else:
            return 'Node does not exist'




    def bft(self,node):
        nodes=set([])
        queue = [node]
        values = []
        while len(queue) >0:
            front_node = queue.pop(0)
            nodes.add(front_node)
            
            for i in self.adjacency.keys():
                if str(i.value) == str(front_node):
                
                    values.append(self.adjacency[i])

                    break
                else:
                
                    continue
            
            if len(values) > 0:
                for n in values[0]:
                    if n[1] not in nodes:
                        queue.append(n[1])
                        nodes.add(n[1])
            else:
                return False
        return nodes


        

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
    print(graph.get_nodes('a'))
    print(graph.get_neighbors('a'))
    print(graph.size())
    print(graph.get_neighbors('v'))