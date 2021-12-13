class Node :
    def __init__(self,value ) -> None:
         self.value = value
         self.left = None
         self.right = None


class BinaryTree :
    def __init__(self) -> None:
        self.root = None



    def pre_order (self,root) :
        _root = root
        stack = []
        def _fun(_root):
            stack.append(_root.value)
            if _root.left != None :
                _fun(_root.left)
            if _root.right !=None :
                _fun(_root.right)
            return stack
        _fun(_root)
        return stack



    def in_order(self,root):
        stack = []
        _root = root
        def _fun(_root):

            if _root.left != None :
                _fun(_root.left)
            stack.append(_root.value)

            if _root.right !=None :
                _fun(_root.right)
            return stack
        _fun(_root)
        return stack
