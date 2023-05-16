#!/usr/bin/python3
def element_at(my_list, idx):
    
    if idx < 0:
        return (None)

    leng = len(my_list)

    if idx > leng:
        return (None)
    
    return (my_list[idx-1])
