from data_structures_and_algorithms.data_structures.linked_list.linked_list import *


def zipLists(list1, list2):
    current1 = list1.head
    current2 = list2.head
    list3 = LinkedList()
    while True:
        if current1 != None:
            list3.append(current1.value)
            current1 = current1.next

        if current2 != None:
            list3.append(current2.value)
            current2 = current2.next

        if current1 == None and current2 == None:
            break

    return list3


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.append(5)
    
    ll2 = LinkedList() 
    ll2.append(4)
    ll2.append(9)
    print(ll1)
    print(ll2)
    print(zipLists(ll1,ll2))
        
       


