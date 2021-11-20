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
            self.pre_order(root.left,stack )

        stack.append(root.value)

        if root.right !=None :
            self.pre_order(root.right , stack)

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
        if self.root.value == value:
            return True
        else :
            self._contains(value,self.root)

    def  _contains(self,value,root):
        if root.value > value :
            if root.left.value == value :
                return True
            else :
                self._contains(value,root.left)
        else :
            if root.right.value == value :
                return True
            else :
                self._contains(value,root.right)

