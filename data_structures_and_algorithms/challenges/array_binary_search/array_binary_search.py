

def sorting(arr):
    arr.sort()
    return arr


def BinarySearch(arr,v):
    if not v in arr:
        return -1
    else:
        count = 0
        for i in arr:
            if i == v:
                break
            else:
                count+=1

        return count



print(BinarySearch(sorting([-1,-3,-2]),5))


