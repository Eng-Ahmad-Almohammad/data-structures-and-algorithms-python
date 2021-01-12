class Node:
    def __init__(self , key , value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self , key, value):
        node = Node(key,value)
        if self.head == None:
           
            self.head = node
        else:
            node.next = self.head
            self.head = node
            
    def __str__(self):
        string = ''
        current = self.head
        while current:
            string += f'{{{current.key}}}: {{{current.value}}} ->'
            current = current.next
            if current == None:
                string += 'NULL'

        return (string)
  
        
  


class Hashtable:
    def __init__(self , size):
        self.size = size
        self.map = [None]*size

    def add(self,key , value):
        position = self.hash(key)
        
        if  self.map[position] == None:
            
            self.map[position] = LinkedList()
            self.map[position].insert(key,value)
       
        else:
           
            self.map[position].insert(key,value)  
       
            


    def get(self , key):
        position = self.hash(key)
        if self.map[position] == None:
            return self.map[position]
        else:
            current = self.map[position].head
            while current:
                if current.key == key:
                    return current.value
                current = current.next
                
        

    def contains(self , key):
        position = self.hash(key)
        if self.map[position] != None:
            return True
        return False




    def hash(self , key):
        hashing = 0 
        for char in key:
            hashing+= ord(char)

        hashing*= 11

        hashing %= self.size
        return hashing
   

if __name__ == '__main__':
    things = Hashtable(1024)
    things.add('name', 'Ahmad')
    things.add('color', 'red')
    things.add('num', 3)
    things.add('could', 67)
    things.add('cloud', 34)
    things.add('coldu', 344)
    print(things.get('cloud'))
    print(things.contains('could'))
    print(things.contains('hadi'))
    print(things.map)
    
    