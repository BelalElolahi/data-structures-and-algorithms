
def insertShift(arr, val) :
    mid = len(arr) // 2
    if len(arr) % 2 != 0 :
        mid += 1
    arr[mid:mid] = [val]
    return arr

if __name__=="__main__" :

    arr =[1,2,3,4,5,6]
    print('\n')
    print(arr)
    insertShift(arr,9)
    print("after insert 9 at the middle")
    print(arr)


    print('\n')
    insertShift(arr,10)
    print("after insert 10 at the middle")
    print(arr)


    print('\n')
    insertShift(arr,30)
    print("after insert 30 at the middle")
    print(arr)
    print('\n')
