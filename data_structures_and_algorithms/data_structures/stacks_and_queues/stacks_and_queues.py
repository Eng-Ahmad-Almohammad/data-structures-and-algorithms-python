class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        new_node = Node(data)
        if self.top :
            new_node.next = self.top

        self.top= new_node

    def pop(self):
        try:
            if self.top:
                temp = self.top
                self.top = self.top.next
                return temp.data
            else:
                raise Exception ('Stack is empty')
        except:
            return 'Stack is empty'

    
    def peek(self):
        try:
            if self.top:
                return self.top.data
            else:
                raise Exception('Stack is empty')

        except:
            return 'Stack is empty'



    def is_empty(self):
        if self.top:
            return False

        else:
            return True 

    def __str__(self):
        temp = self.top
        string = ''
        if temp == None:
            string = 'NULL'
        
        while temp:
            string += f'{{{temp.data}}}->'
            temp = temp.next
            if temp == None:
                string += 'NULL'
        return (string)



class Queue:
    def __init__(self):
        self.front= None
        self.rear = None

    def enqueue(self,data):
        try:
            new_node= Node(data)
            if self.rear:
                self.rear.next = new_node
                self.rear = new_node
            else:
                self.front = new_node
                self.rear = new_node
        except:
            raise Exception('an error')
    def dequeue(self):
        try:
            temp = self.front
            if temp:
                self.front = self.front.next
                return temp.data
            else:
                raise Exception('Queue is empty')

        except:
            return 'Queue is empty'




    def peek(self):
        try:
            if self.front:
                return self.front.data
            else: 
                raise Exception('Queue is empty')

        except:
            return 'Queue is empty'
        





    def is_empty(self):
        if self.front:
            return False

        else:
            return True 

    def __str__(self):
        temp = self.front
        string = ''
        if temp == None:
            string = 'NULL'
        
        while temp:
            string += f'{{{temp.data}}}->'
            temp = temp.next
            if temp == None:
                string += 'NULL'
        return (string)








if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(7)
    print(stack)
    print(stack.pop())
    print(stack)
    stack.push('top')
    print(stack)
    print(stack.peek())
    print(stack)
    stack.pop()
    stack.pop()
    print(stack)
    print(stack.is_empty())

    # queue = Queue()
    # queue.enqueue(5)
    # queue.enqueue(7)
    # print(queue)
    # print(queue.dequeue())
    # print(queue)
    # queue.enqueue('rear')
    # print(queue.peek())
    # print(queue)
    # queue.dequeue()
    # queue.dequeue()
    # print(queue)
    # print(queue.is_empty())




