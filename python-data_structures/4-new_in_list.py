#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    leng = len(my_list)

    for i in range(leng-1):
        newlist[i] = my_list[i]

    if idx < 0:
        return (newlist)

    if idx > leng-1:
        return (newlist)

    newlist[idx] = element

    return (new_list)
