from data_structures_and_algorithms.data_structures.tree.tree import *

def tree_intersection(tree1, tree2):
    if tree1.root and tree2.root:
        arr1 = set(tree1.preOrder())
        arr2 = tree2.preOrder()
        output = []
        for i in arr2:
            if i in arr1:
                output.append(i)
        return set(output)
    else:
        return ('tree is empty')




if __name__ == '__main__':
    bt = BinaryTree()
    bt.root = Node(150)
    bt.root.right = Node(250)
    bt.root.left = Node(100)
    bt.root.left.left = Node(75)
    bt.root.left.right = Node(160)
    bt.root.left.right.left = Node(125)
    bt.root.left.right.right = Node(175)
    bt.root.right.left = Node(200)
    bt.root.right.right = Node(350)
    bt.root.right.right.left = Node(300)
    bt.root.right.right.right = Node(500)


    bt1 = BinaryTree()
    bt1.root = Node(42)
    bt1.root.right = Node(600)
    bt1.root.left = Node(100)
    bt1.root.left.left = Node(15)
    bt1.root.left.right = Node(160)
    bt1.root.left.right.left = Node(125)
    bt1.root.left.right.right = Node(175)
    bt1.root.right.left = Node(200)
    bt1.root.right.right = Node(350)
    bt1.root.right.right.left = Node(4)
    bt1.root.right.right.right = Node(500)

    print(tree_intersection(bt,bt1))