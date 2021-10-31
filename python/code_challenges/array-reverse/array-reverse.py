list =[1,2,3,4,5,6]
def reverse(list) :
    start_index = 0
    end_index= len(list)-1

    while end_index  > start_index :
      list[start_index],list[end_index] = list[end_index],list[start_index]
      start_index = start_index+1
      end_index =end_index -1

if __name__=="__main__" :
    reverse(list)
    print(list)

