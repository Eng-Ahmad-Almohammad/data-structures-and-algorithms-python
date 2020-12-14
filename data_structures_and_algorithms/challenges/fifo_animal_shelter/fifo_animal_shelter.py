


class Cat():
    def __init__(self,name):
        self.name = name
        self.type = 'c'
        self.next = None
    
   
class Dog():
    def __init__(self,name):
        self.name = name
        self.type = 'd'
        self.next = None


class AnimalShelter():
   
    def __init__(self):
        self.front= None
        self.rear = None

    def enqueue(self,data):
        new_node= data
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = new_node
            self.rear = new_node

    def dequeue(self,pref=None):
        try:
            if pref == 'cat':

                temp = self.front
                while temp:
                    if temp.type == 'c':
                        self.front = self.front.next
                        return temp.name
                    else:
                        temp = temp.next
            elif pref == 'dog':

                temp = self.front
                while temp:
                    if temp.type == 'd':
                        self.front = self.front.next
                        return temp.name
                    else:
                        temp = temp.next
            else:
                temp = self.front
                self.front = self.front.next
                return temp.name
              
               

        except:
            return 'Queue is empty'

    def __str__(self):
        temp = self.front
        string = ''
        if temp == None:
            string = 'NULL'
        
        while temp:
            string += f'{{{temp.name}}}->'
            temp = temp.next
            if temp == None:
                string += 'NULL'
        return (string)








if __name__ == "__main__":
    queue = AnimalShelter()
    queue.enqueue(Cat('hadi'))
    queue.enqueue(Dog('Ahmad'))
    print(queue)
    print(queue.dequeue())
    
    # queue.enqueue('rear')
    # print(queue.peek())
    # print(queue)
    # queue.dequeue()
    # queue.dequeue()
    # print(queue)
    # print(queue.is_empty())