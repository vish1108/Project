def binarySearch(arr, target):
    start = 0                       #starting position of element
    end = len(arr) - 1              #ending position of element
    while start <= end:
        mid = (start + end)//2      #if we get target on middle it will return the middle position
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:     #if the target is smaller that middle element then the new ending position will be  end = mid - 1
            end = mid - 1 
        else:
            start = mid + 1         #if the target is bigger that middle element then the new strting position will be  start = mid + 1
    return -1   # Return -1 if the target is not found

arr = [2, 4, 7, 13, 15, 21, 34]
target = 15
result = binarySearch(arr, target)
print(result)

#in this algorithm we just make sersch space smaller