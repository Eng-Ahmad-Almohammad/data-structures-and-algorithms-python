class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    This class will insert a value to linked list in the head by calling insert method
    and it will search about any value if it exsist in the linked list by calling includes method
    and it has a __str__ method return a string with all linde list content.
    """

    # put your LinkedList implementation here
    def __init__(self):
        self.head = None

    def insert(self, value):
        if value == None or value == '':
            raise Exception('You should insert a value')

        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def includes(self, value):

        if self.head == None:
            return False
        else:
            current = self.head
            while current:

                if current.value == value:
                    return True
                current = current.next

            return False

    def append(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = node

    def insert_before(self, value, newVal):
        node = Node(newVal)
        if self.head.value == value:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            while current.next:
                if current.next.value == value:
                    node.next = current.next
                    current.next = node
                    break

                current = current.next
            if current.next == None:
                raise ValueError(f'{value} it is not founded')

    def insert_after(self, value, newVal):
        node = Node(newVal)
        if self.head == None:

            self.head = node
        else:
            current = self.head
            while current:
                if current.value == value:
                    node.next = current.next
                    current.next = node
                    break
                current = current.next

            if current == None:
                raise ValueError(f'{value} it is not founded')

    def __str__(self):
        string = ''
        current = self.head
        while current:
            string += f'{{{current.value}}}->'
            current = current.next
            if current == None:
                string += 'NULL'

        return (string)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(2)
    ll.insert_before(2, 9)
    print(ll)
