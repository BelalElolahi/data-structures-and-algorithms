def left_join(firsthash,secoedhash):
    list=[]
    for key in firsthash:
        value1 = firsthash[key]
        if key in secoedhash:
            value2 = secoedhash[key]

        else:
            value2 = None

        list.append([key,value1,value2])

    return list



