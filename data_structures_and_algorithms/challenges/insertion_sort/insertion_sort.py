def insertion_sort(arr):
    n = len(arr)
    if n > 0:
        for i in range(n):
            minn = i 
            nextt = i+1
            if i == n-1:
                break
            for j in range(n-1):
                
                if arr[nextt] < arr[minn]:
                    minn = nextt
                nextt +=1
                if nextt > n-1:
                    break
            temp = arr[minn]
            arr[minn] = arr[i]
            arr[i] = temp
            
        return arr
    else:
        raise Exception('Please insert valid list')
if __name__ == "__main__":
    print(insertion_sort([8,4,23,42,16,15]))
    print(insertion_sort([20,18,12,8,5,-2]))
    print(insertion_sort([5,12,7,5,5,7]))
    print(insertion_sort([2,3,5,7,13,11]))
    print(insertion_sort([]))




