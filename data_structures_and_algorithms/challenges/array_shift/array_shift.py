import math

def insertShiftArray(arr,value):
    x =math.ceil(len(arr)/2)
    arr1 = arr[:x]
    arr1+=[value]
    arr2 = arr[x:]
    return arr1+arr2

print(insertShiftArray([1,2,3,4,5],6))