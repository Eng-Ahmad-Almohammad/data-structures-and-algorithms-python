from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import *


class PseudoQueue:
    def __init__(self):
        self.stack1= Stack()
        self.stack2= Stack()

    def enqueue(self,item):
        
        self.stack1.push(item)
        return self.stack1
        
    def dequeue(self):

        
        current = self.stack1.top
        while current:
            self.stack2.push(self.stack1.pop())
            current = current.next

        return self.stack2.pop()

        

   



if __name__ == "__main__":
    stack = PseudoQueue()
    stack.enqueue(5)
    stack.enqueue(7)
    stack.enqueue(4)
    print(stack.dequeue())
    print(stack.dequeue())
    print(stack.dequeue())
    print(stack.dequeue())
    