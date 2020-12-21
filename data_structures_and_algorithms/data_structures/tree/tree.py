
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.output = []


    def preOrder(self):
        node = self.root

        def _walk(node):
            self.output.append(node.data)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(node)
        return self.output

    def inOrder(self):
        node = self.root

        def _walk(node):
            if node.left:
                _walk(node.left)
            self.output.append(node.data)
            if node.right:
                _walk(node.right)

        _walk(node)
        return self.output

    def postOrder(self):
        node = self.root

        def _walk(node):
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            self.output.append(node.data)

        _walk(node)
        return self.output

    def find_maximum_value(self):
        self.x = self.root.data
        node = self.root

        def _walk(node):
            if self.x < node.data:
                self.x = node.data
            
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(node)
        return self.x


    def breadth_first(self):
        self.queue = [self.root]
        self.output = []
        
        while len(self.queue) > 0:
            front_node = self.queue.pop(0)
            self.output +=[front_node.data]
            if front_node.left:
                self.queue+=[front_node.left]
            if front_node.right:
               
                self.queue+=[front_node.right]

        return self.output









class BinarySearchTree(BinaryTree):
    def add(self,value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node

        else:
            current = self.root
            def _walk(current):
                if current.data > value:
                    if current.left:
                        _walk(current.left)

                    else:
                        current.left = new_node
                        return

                else :
                    if current.right:
                        _walk(current.right)

                    else:
                        current.right = new_node
                        return

            _walk(current)

    def contains(self,value):
        try:
            if not self.root:
                return False
            else:
                current = self.root
                
                def _walk(current):
                    if value == current.data:
                        return True
                    elif value < current.data:
                        current = current.left
                        if current:
                            return _walk(current)
                    elif value > current.data:
                        current = current.right
                        if current:
                            return _walk(current)
                        
                if _walk(current) == True:
                    return True

                else:
                    return False

        except:
            return "ValueError"




    
if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    print(bt.find_maximum_value())
    print(bt.breadth_first())
    # bst = BinarySearchTree()
    # bst.add(4)
    # bst.add(9)
    # bst.add(-1)
    # bst.add(6)
    # bst.add(3)
    # bst.add(8)
    # bst.add(5)
    # print(bst.contains('sdfkz'))
    # assert bt.root.data == 4
    # assert bt.root.left.data == -1
    # assert bt.root.right.data == 9
    # assert bt.root.left.right.data == 3
    # assert bt.root.right.left.left.data == 5
    # print('=====All passed======')