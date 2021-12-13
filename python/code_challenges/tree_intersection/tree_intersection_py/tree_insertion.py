
def tree_intersection(firstTree,secondTree):

    if(firstTree.root and secondTree.root):
        list1=firstTree.pre_order(firstTree.root)
        list2=secondTree.pre_order(secondTree.root)
        array=[]
        for value in list1:
            for value2 in list2:
                if value==value2:
                    array.append(value)
        if array:
            return array
        else:
            return 'no intersection'

