from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import *

open_list = ["[","{","("] 
close_list = ["]","}",")"] 
  
# Function to check parentheses 
def multi_bracket_validation(myStr): 
    stack = Stack() 
    for i in myStr: 
        if i in open_list: 
            stack.push(i) 
            print(stack)
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((stack.top) and (open_list[pos] == stack.peek())):
                stack.pop() 
                print(stack.peek())
            else: 
                return False
    if stack.top== None: 
        return True
    else: 
        return False
  
  




print(multi_bracket_validation('({((()[[Extra Characters]]))})'))