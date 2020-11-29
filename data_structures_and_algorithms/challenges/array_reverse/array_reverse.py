def reverse_array(arr):
   
    return arr[::-1]


def reverse_array_alt(arr):
   
    temp = []
    while arr:
        temp.append(arr.pop())
    arr=temp
    
    return temp



if __name__=='__main__':
    
    print(reverse_array([1,2,3,4,5])) 
    print(reverse_array_alt([1,2,3,4,5])) 
    
