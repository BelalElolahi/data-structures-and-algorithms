
def business_trip(graph , city_names):
    state=True
    cost=0
    y=city_names[0]

    niegh=[city_names[0]]
    for city in city_names:
        if city not in  niegh:
            return [False,0]
        neighbors=graph.get_neighbors(city)
        niegh=[]
        for neighbor in neighbors:
            niegh.append(neighbor[0])
    neighbors=graph.get_neighbors(y)

    for city in city_names[1:]:
        for neighbor in neighbors:
            if city ==neighbor[0]:
                cost+=neighbor[1]
        neighbors=graph.get_neighbors(city)
    return [state,cost]
