#!/usr/bin/python3
def no_c(my_string):

    noc = my_string.copy()

    leng = len(noc)

    for i in range(leng):
        
        if noc[i] == "c" or noc[i] == "C":
            noc[i] = ""

    return (noc)
