#comment
def binarySearch(array,item):  # 5min
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


def move0and1s(array):  # 11min
    n = len(array)
    start = 0
    end = n - 1
    mid = start
    while start < end and mid < end:
        if array[mid]==0:
            array[start],array[mid] = array[mid],array[start]
            start += 1
            mid += 1
        elif array[mid]==2:
            array[end],array[mid] = array[mid], array[end]
            end -= 1
        else:
            mid += 1
    return array
    


a = [1,1,1,2,2,0,0,1,2,0,2,1]
print(move0and1s(a))




def helper(array,start,end):  #30MIN
    p = array[end]
    i = start
    j = end - 1
    while i<j:
        while array[i]<p:
            i+=1
        while array[j]>p:
            j-=1
        array[i],array[j] = array[j],array[i]
    array[end],array[j] = array[j],array[end]
    return j
    

def quickSort(array,start,end):   #10 MIN
    if start<end:
        pi = helper(array,start,end)# call 
        quickSort(array,start,pi-1)
        quickSort(array,pi+1,end)
        

a = [22,11,77,99,33,56,31,57]
n = len(a)-1
quickSort(a,0,n)
print(a)





