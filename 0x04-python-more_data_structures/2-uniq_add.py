#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = []
    for i in my_list:
        if i not in newlist:
            newlist.append(i)
    return sum(newlist)