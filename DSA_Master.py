#comment
def binarySearch(array,item):
    n = len(array)
   
    start = 0
    end = n - 1
    while start <= end:
        mid = ( start + end ) // 2
        if array[mid] == item:
            return mid
        elif array[mid]>item:
            end = mid - 1
        else:
            start = mid + 1
    return -1


a = [1,2,3,4,5,6,7,8,9,10]
print(binarySearch(a,10))
