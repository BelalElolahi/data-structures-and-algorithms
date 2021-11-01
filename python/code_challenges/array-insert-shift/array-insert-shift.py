from typing import List


list =[1,2,3,4,5,7,2,8,5,10]
def insertShift(list,value) :
    mid = len(list) //2

    if len(list) % 2 != 0 :
        mid +=1
        
    list[mid:mid]=[value]
    return list




if __name__=="__main__" :
     insertShift(list,10)
     print(list)


