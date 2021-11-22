from collections import deque

def breadth_first(tree):

    que_breadth = deque()
    breadth = []


    que_breadth.append(tree.root)
    while que_breadth :
        curr=que_breadth.popleft()
        breadth.append(curr.value)

        if curr.left  :
            que_breadth.append(curr.left)
        if curr.right :
            que_breadth.append(curr.right)
    return breadth







