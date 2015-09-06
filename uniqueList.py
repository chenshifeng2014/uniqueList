#######################################################################
# File Name: uniqueList.py
# Author: fypp
# mail: fypp2014@yeah.net
# Created Time: 2015-09-06 20:48:38
#########################################################################

#!/usr/bin/env python
# coding=utf-8

test_list = [{'A':2,'B':3,'C':4},{'A':2,'B':4,'C':5},{'A':2,'B':3,'C':5},{'A':2,'B':3,'C':6}]
del_id = [] 
for i in range(len(test_list)):
    j = i+1;
    while(j and j!=len(test_list)):
        if (test_list[j]['A'] == test_list[i]['A']) and  (test_list[j]['B'] == test_list[i]['B']):
            del_id.append(j)
            j = 0
        else:
            j = j+1
de = 0
for item in del_id:
    id_de = item - de
    del test_list[id_de]
    de += 1
print test_list

