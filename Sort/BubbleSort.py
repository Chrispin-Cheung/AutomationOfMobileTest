# -*- coding:utf-8 -*-
array = [3,5,8,2,1]
def BubbleSort(lst):
    for i in range(len(lst)-1,0,-1):
        print (i)
        for j in range(i):
            print (j)
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    print(lst)

BubbleSort(array)

