from trees.node import Node

class BinaryTree :
    def __init__(self) -> None:
        self.root = None


    def pre_order (self,root,stack = []) :

        stack.append(root.value)
        if root.left != None :
            self.pre_order(root.left,stack)
        if root.right !=None :
            self.pre_order(root.right,stack)

        return stack


    def in_order(self,root, stack = []):
        if root.left != None :
            self.in_order(root.left,stack )

        stack.append(root.value)

        if root.right !=None :
            self.in_order(root.right , stack)

        return stack

    def post_order (self,root ,stack=[]) :

            if root.left != None :
                self.post_order(root.left , stack)
            if root.right != None :
                self.post_order(root.right , stack)
            stack.append(root.value)

            return stack
    def is_empty(self):
        return self.root == None


class BinarySearchTree(BinaryTree) :
    def __init__(self) -> None:
        super().__init__()


    def add(self,value):
           new_Node = Node(value)
           if self.root==None :
                  self.root= new_Node
           else:
                  self._add(new_Node,self.root)


    def _add(self, new_Node, root):
           if(root.value > new_Node.value):
                  if(root.left==None):
                         root.left=new_Node

                  else:
                         self._add(new_Node,root.left)
           else:
                   if(root.right==None):
                         root.right=new_Node
                   else:
                         self._add(new_Node,root.right)




    def contains(self,value):
        if self.root :
           contain= self._contains(value,self.root)
        return contain

    def  _contains(self,value,root):
        if root.value == value :
                return True
        elif root.value > value :
                self._contains(value,root.left)
        elif root.value < value:
                self._contains(value,root.right)
        else :
            return False





    def tree_max(self):
        if self.root :
           max=self.getMax(self.root)
        return max
    def getMax(self,root):
        if root.right:
            return self.getMax(root.right)
        return root.value






    """ # MaxValue
    def tree_max(self) :
       max = self.root.value
       max_value= self._tree_max(max,self.root)
       return max_value

    def _tree_max(self,max,root):
         if root.left :
           if root.left.value > max :
               max = root.left.value
           else :
               self._tree_max(max ,root.left)


         else :
            if root.right.value > max :
               max = root.right.value
            else :
               self._tree_max(max ,root.right)
         return max """



