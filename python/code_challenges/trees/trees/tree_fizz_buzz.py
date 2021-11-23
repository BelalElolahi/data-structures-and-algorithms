from trees.tree import BinarySearchTree


def fizz_buzz_tree (tree):
     _root = tree.root
     fizz_buzz_list = []


     def _fun(_root):
         if _root.value % 3 == 0 and _root.value % 5 ==0 :
             fizz_buzz_list.append('FizzBuzz')
         elif _root.value % 3 == 0 :
             fizz_buzz_list.append('Fizz')
         elif _root.value % 5 == 0 :
             fizz_buzz_list.append('Buzz')
         else :
             fizz_buzz_list.append(str(_root.value))

         if _root.left != None :
            _fun(_root.left)
         if _root.right !=None :
             _fun(_root.right)

         return fizz_buzz_list
     _fun(_root)


     Fizz_Buzz_Tree  = BinarySearchTree()
     for value in fizz_buzz_list :
         Fizz_Buzz_Tree.add(value)

     return Fizz_Buzz_Tree

