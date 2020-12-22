from data_structures_and_algorithms.data_structures.tree.tree import *

def FizzBuzzTree(tree):
    new_tree = tree
    node = new_tree.root
    output =[]
    def _walk(node):
        if isinstance(node.data, int):
            if node.data%5==0 and node.data%3==0:
                output.append('FizzBuzz')
                
            elif node.data%3==0:
                output.append('Fizz')
                
            elif node.data%5==0:
                output.append('Buzz')
                
            else:
                output.append(node.data)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
        else:
            output.append(node.data)
    _walk(node)
    return output



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
    bt.root.right.right.left = Node('hi')
    print(FizzBuzzTree(bt))
    print(bt.preOrder())