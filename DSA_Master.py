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



def mergeSort(a):  # 30 min
    n = len(a)
    # print(a)
    if n<=1:
        return 
    left = a[:n//2]
    right = a[n//2:]
    
    mergeSort(left)
    mergeSort(right)
    ans = []
    i = 0
    j = 0
    n = len(left)
    m = len(right)
    while i<n and j < m:
        if left[i]<=right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
    while i < n:
        ans.append(left[i])
        i+=1
    while j< m:
        ans.append(right[j])
        j+=1
    for k in range(n+m):
        a[k] = ans[k]





a = [22, 11, 77, 99, 33, 56, 31, 57] 
mergeSort(a)
print(a)




        
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self,head=None):
        self.head = head
    def construct(self,array):
        for element in array:
            currentNode = Node(element)
            
            if not self.head:
                self.head = currentNode
            else:
                prevNode.next = currentNode 
            prevNode = currentNode
    def pretyPrint(self):
        current = self.head
        while current.next:
            print(current.data,end=" => ")
            current = current.next
        print(current.data)
    
    def deleteAspecificData(self,data):
        if self.head.data == data:
            self.head = self.head.next
            return 
        curr = self.head
        while curr.next:
            if curr.data == data:
                prev.next = curr.next
            prev = curr
            curr = curr.next
        if curr.data == data:
            prev.next = curr.next
    
    def reverse(self):
        curr = self.head
        prev = None
        while curr.next:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        curr.next = prev
        self.head = curr
    
    def checkForCycle(self):
        slow = self.head
        fast = slow
        start = True
        while slow.next and fast.next and fast.next.next:
            if (not start) and fast == slow:
                return True
            start = False
            slow = slow.next
            fast = fast.next.next
        return False
        
    def get(self,data):
        curr = self.head 
        while curr.next:
            if curr.data == data:
                return curr
        if curr.data == data:
            return curr
        return Node(-1)

a = [11, 22, 31, 33, 56, 57, 77, 99]

l = LinkedList()
l.construct(a)
l.pretyPrint()
# l.deleteAspecificData(11)
l.reverse()
l.pretyPrint()
print(l.checkForCycle())
l.get(99).next = l.head
print(l.checkForCycle())



