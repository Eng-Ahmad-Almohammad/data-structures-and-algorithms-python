# Table of Contents 

|Challenge No. | Name of challenge|
|:---------: |:--------------:|
|1|[Reverse an Array](data_structures_and_algorithms/challenges/array_reverse/array_reverse.py)
|2|[Shift an Array](data_structures_and_algorithms/challenges/array_shift/array_shift.py)
|3|[Binary Search ](data_structures_and_algorithms/challenges/array_binary_search/array_binary_search.py)
|5|[Linked List ](data_structures_and_algorithms/data_structures/linked_list/linked_list.py)
|8|[ll-zip ](data_structures_and_algorithms/challenges/ll_zip/ll_zip.py)
|10|[Stack and Queue ](data_structures_and_algorithms/data_structures/stacks_and_queues/stacks_and_queues.py)
|11|[Queue using two Stacks ](data_structures_and_algorithms/challenges/queue_with_stacks/queue_with_stacks.py)
|12|[fifo_animal_shelter ](data_structures_and_algorithms/challenges/fifo_animal_shelter/fifo_animal_shelter.py)
|13|[Bracket Validation ](data_structures_and_algorithms/challenges/multi_bracket_validation/multi_bracket_validation.py)
|15|[Tree ](data_structures_and_algorithms/data_structures/tree/tree.py)





# Reverse an Array
<!-- Short summary or background information -->
I should creat a function which take one arrgument as list and retun a reverse list for it 

## Challenge
<!-- Description of the challenge -->
I should creat a function which take one arrgument as list and retun a reverse list for it 
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I used on of index properety for lists to solve this challenge which is the shortest and easist way to solve it (O(1))
## Solution
![image](assets/array-reverse.jpg)



# Shift an Array
<!-- Short summary or background information -->
I should creat a function which take two arrguments one is array and the second is value and return a new array have that value in the middle of it without using any build-in methods.
## Challenge Description
<!-- Description of the challenge -->
I should creat a function which take two arrguments one is array and the second is value and return a new array have that value in the middle of it without using any build-in methods.
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I will split the array to two array  and append the new value the first part and then merage them again
## Solution
<!-- Embedded whiteboard image -->
![image](assets/challemge02.jpg)




# Binary Search 

<!-- Short summary or background information -->
I should creat a function take two arrguments sorted array and key value and return the index of value inside the array and equal the value of key and retirn -1 if it does not exsit.
## Challenge Description
<!-- Description of the challenge -->
I should creat a function take two arrguments sorted array and key value and return the index of value inside the array and equal the value of key and retirn -1 if it does not exsit.
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I will compare between the mid value inside the array and the key then I will specify if it is in the left of right then compare with the middle of the half..etc
## Solution
<!-- Embedded whiteboard image -->
![image](assets/Binary_search.jpg)



# Singly Linked List
<!-- Short summary or background information -->
A Linked List is a sequence of Nodes that are connected/linked to each other. The most defining feature of a Linked List is that each Node references the next Node in the link.

## Challenge
<!-- Description of the challenge -->
I should create a method to insert in the Head of a linked list and another method to find if the value exsist in the linked list and all of that without using any build-in method.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I used the classes to create a linked list or to insert a new value to it, in addition to find if a spsefic value exsist or not.
my class was O(1)

## API
<!-- Description of each method publicly available to your Linked List -->
For insert method I created a new Node and then assigned the head to the next value after that I but the head on my new Node.
For includes method I assigned the head to the current to make sure that i am starting from the beginning then I will loop over the content and return True if it exsist and False if it is not exsist.



# Linked list 
<!-- Short summary or background information -->
A Linked List is a sequence of Nodes that are connected/linked to each other. The most defining feature of a Linked List is that each Node references the next Node in the link.
## Challenge Description
<!-- Description of the challenge -->
I should to create three methods one to append in the end of the linked list and one to insert before a specific value and the last one to append after a specific value
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
For appending in the end I will loop over the list then I will stop on the last value in the list then add my new node

For inserting before a value I will loop over the linked list and I will stop on the previous target value and I will append the value of the node for its next value and pointing the new node to the target value.

for inserting after a value it the same of inserting before but insted of stoping on previous node I will stop on the target value

Big O for this is O(1)
## Solution
<!-- Embedded whiteboard image -->
https://miro.com/welcomeonboard/l6ziM3FAemgdqMsZHMqXmLMOaxUHJG3sooELkmBlW1O7qy8Q1vFKtaYi9EUmkEgi



# Linked list 
<!-- Short summary or background information -->
A Linked List is a sequence of Nodes that are connected/linked to each other. The most defining feature of a Linked List is that each Node references the next Node in the link.
## Challenge Description
<!-- Description of the challenge -->
I should to create a method take k as argument and return the value of the node that have k index but reverse 
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I will loop over the list to get its length then I will subtract the k from the length then I will loop over the list until arrive to the node which have the subtraction value index

Big O for this is O(2n)
## Solution
<!-- Embedded whiteboard image -->
https://miro.com/welcomeonboard/1oPMXT0QE5fxxAfjJ8p3iVbJmp9TxWY8Q0DBrVWLIJKSi9NbGZts0xslegJOHV76




# ll-zip
<!-- Short summary or background information -->
It is ordring the lists item in new list 
## Challenge Description
<!-- Description of the challenge -->
Write a function called zipLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Creating a new list and taking the items from another lists then returning anew list 
O(n) 
## Solution
<!-- Embedded whiteboard image -->
https://miro.com/welcomeonboard/Am0PG3pApIrnaozuwY3q5Ib68j55GtGJb84UrhqJlm2XhVhYcAgsf9XkIB0mlcFa





# Stacks and Queues
<!-- Short summary or background information -->
Stack and Queue is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.

## Challenge
<!-- Description of the challenge -->
For stack:
Create a Stack class that has a top property. It creates an empty Stack when instantiated.

This object should be aware of a default empty value assigned to top when the stack is created.

Define a method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.

Define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value. Should raise exception when called on empty stack.

Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack. Should raise exception when called on empty stack.

Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the stack is empty.

For Queue:
Create a Queue class that has a front property. It creates an empty Queue when instantiated.

This object should be aware of a default empty value assigned to front when the queue is created.

Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.

Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value. Should raise exception when called on empty queue.

Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue. Should raise exception when called on empty queue.

Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the queue is empty.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
For stack every node pointing to the next node and the last one called the top which I can append any new node for it and put it as top. Big O is O(1)

For queue evry node pointing to the next node and the first node called front and last one called rear so I can easily enqueue and dequeue. Big O is O(1)
## API
<!-- Description of each method publicly available to your Stack and Queue-->
For stack:
push: it will push a node to the top of the stack.
pop: it will remove the the top of the stack and return its value
peek: it will return the value of the top without removing it from stack
is_empty : it will return a boolean telling you if the stack is empty 

For queue:
enqueue: it will push a node to the rear of the queue.
dequeue: it will remove the the front of the queue and return its value
peek: it will return the value of the front without removing it from queue
is_empty : it will return a boolean telling you if the queue is empty 




# Queue using two Stacks
<!-- Short summary or background information -->
Stack and Queue is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.
## Challenge Description
<!-- Description of the challenge -->
I should to create a class which have two stacks as inistances and it should have a enqueue method and dequeue method.
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I will push the new items inside first stacks that for enqueue and for dequeue I will loop over first stack and pop all its item and push them inside the second stack.
Big O is O(n)
## Solution
<!-- Embedded whiteboard image -->
https://miro.com/welcomeonboard/To5rgivtB9nKE2Kmm5hAvs9q0o4gWUA8sLBIRjbibD2xPgWPzi06qxgo7CtdG1Cx



# fifo_animal_shelter
<!-- Short summary or background information -->
Stack and Queue is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.

## Challenge
<!-- Description of the challenge -->
Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I will check first item if it is like pref I will return it but if not I will loop to find it and take its value and skip it
## API
<!-- Description of each method publicly available to your Stack and Queue-->
enqueue will add a cat or dog inside the queue
dequeue will return the first cat or dog find it related to pref and if pref was None so it will return the first pet.





# Bracket Validation
<!-- Short summary or background information -->
Checking brackets is one of mort important checking in programming languages which can make uxpected errors or results
## Challenge Description
<!-- Description of the challenge -->
Write a function to validate the brackets
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Loop over string and check if its an open brackets then push it to the stack else if it is close bracket get its index and then get the open bracket with same index and compare it with last value inside the stack
## Solution
<!-- Embedded whiteboard image -->
https://miro.com/welcomeonboard/hy0zRjyAtT0Ou3rLufOP7t4QLGwqd48lxu0f7tfxVYgAObUqctUIOfsdMQFjfLsS




# Trees
<!-- Short summary or background information -->
I am using here Binary Tree where each node have only two or less children

## Challenge
<!-- Description of the challenge -->
Crete two classes one to traverse during a tree and the second one to add and find a value
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
In this two classes I use recursion eather for traversing or for adding and checking 
the Big O for the two classes is log(n)
## API
<!-- Description of each method publicly available in each of your trees -->
I created a class called BinaryTree which travers during the tree with three methods preOrder(root ==> left ==> right) or inOrder(left ==> root ==> right) or postOrder(left ==> right ==> root)
There is another class called BinarySearchTree where you can use add() method to create your tree and if you want to chack if the tree have a spesific value you can use contains() method


# Find maximum value in a tree 
<!-- Short summary or background information -->
I am using here Binary Tree where each node have only two or less children
## Challenge Description
<!-- Description of the challenge -->
Write a function to return maximum value inside the tree
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I used recursion using preorder method tho go thorght the tree and compare each value with a varibale where I gave it first time the root value and then it will change if it find larger data
## Solution
<!-- Embedded whiteboard image -->
https://miro.com/welcomeonboard/LN13ANWem6KOOvvRpJpAwiLJ31Gaf27cOs5E5h9sdQFFZ978Y0pzcEIpwGrfjGgo