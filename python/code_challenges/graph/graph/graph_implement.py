
class Vertex :
    def __init__(self,value) :
        self.value = value

    def __str__(self) -> str:
        return self.value


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
                    self.adjacency[key].append(second_vertex)


    def get_nodes(self):
       list= []
       for key in self.adjacency :
           list.append(key.value)
       print(list)

       if len(list) == 0:
           return "Null"
       return list


    def get_neighbors(self,node):
        if len(list(self.adjacency)) != 0 :

            for key in self.adjacency :
                if str(key.value) == node :
                    return self.adjacency[key]
            return "not exist"
        else :
            return "Null"


    def size(self):
       if len(list(self.adjacency)) != 0 :
           return self.__length

       return "Null"

