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

    def add (self,value):
        if self.root == None :
            self.root = Node(value)

        if value < self.root.value :


                self.root.left = Node(value)


        else:
               self.root.left = Node(value)



    def contains(value):
        pass
