from graph.vertex import Vertex


class Graph :

    def __init__(self) -> None:
        self.adjacency= {}
        self.__length = 0



    def add_node(self,value) :
         node = Vertex(value)
         self.adjacency[node] = []
         self.__length += 1
         return node




    def add_edge(self, first_vertex, second_vertex, weight=1):

            for key in self.adjacency.keys():
                if str(key.value) == str(first_vertex):
                    self.adjacency[key].append([second_vertex,weight])


    def get_nodes(self):
       list= []
       for key in self.adjacency :
           list.append(key.value[0])
       print(list)

       if len(list) == 0:
           return "Null"
       return list


    def get_neighbors(self,node):
        if len(list(self.adjacency)) != 0 :

            for key in self.adjacency :
                if str(key.value[0]) == node :
                    return self.adjacency[key]
            return "not exist"
        else :
            return "Null"


    def size(self):
       if len(list(self.adjacency)) != 0 :
           return self.__length

       return "Null"




    """
       Write the following method for the Graph class:

        breadth first
        Arguments: Node
        Return: A collection of nodes in the order they were visited.
        Display the collection

    """
    def BFS (self,start_vettex):
        queue = []
        result = []
        visited = set()

        queue.append(start_vettex)
        visited.add(start_vettex)
        result.append(start_vettex)

        while queue :
            current_vertex = queue.pop(0)
            neighbors = self.get_neighbors(current_vertex)

            for neighbor in neighbors :
                if neighbor[0] not in visited :
                    queue.append(neighbor[0])
                    visited.add(neighbor[0])
                    result.append(neighbor[0])



        return result


    """
   Write the following method for the Graph class:

        Name: Depth first
        Arguments: Node (Starting point of search)
        Return: A collection of nodes in their pre-order depth-first traversal order
        Program output: Display the collection
    """
    def DFS(self , start_vertex):
        list = []
        visited = set()

        def _func( start_vertex):
            list.append(start_vertex)
            visited.add(start_vertex)
            neighbors = self.get_neighbors(start_vertex)
            for neighbor in neighbors :
                _func(neighbor[0])

        _func(start_vertex)
        return list





