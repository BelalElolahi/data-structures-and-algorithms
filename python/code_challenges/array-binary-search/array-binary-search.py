
list = [1,2,3,4,5,6,7,10,50,60]
def binary_search(arr , val) :
    low = 0
    high = len(arr) -1
    mid = 0

    while low <= high :
       mid = (low + high) // 2

       if arr[mid] < val :
           low = mid + 1
       elif arr[mid] > val :
           high = mid -1
       else :

            return mid

    return -1

if __name__ =="__main__" :

    binary_search(list , 100)
