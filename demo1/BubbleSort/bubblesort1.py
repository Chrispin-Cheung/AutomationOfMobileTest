# -*- coding:UTF-8 -*-
# Author:iotrookie
# Function:传统方法实现冒泡排序（C语言版移植到Python版）
# Create Time:
# Edit Author:
# Edit Function:
# Edit CreateTime:
array = [10,67,21,31,56,9]
# 单次循环将最大数冒泡到列表末尾
# for i in range(len(array)):
#     for j in range(i):
#         if array[j] > array[j + 1]:
#             array[j], array[j + 1] = array[j + 1], array[j]

# 冒泡排序：输入一个无序的序列，比如10，67，21，31，56，9
#         输出升序排序或降序排序
#         举例：升序：9，10，21，31，56，67
#         三重循环实现 算法复杂度O(n3)，n3代表n的三次方
def bubblesort(lst):
    for n in range(len(lst)):
        for i in range(len(lst)):
            for j in range(i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
    print(array)

# 冒泡排序：输入一个无序的序列，比如10，67，21，31，56，9
#         输出升序排序或降序排序
#         举例：升序：9，10，21，31，56，67
#         二重循环实现 算法复杂度最差为O(n2),n2代表n的平方
def bubblesort1(lst):
    for i in range(len(lst)):
        for j in range(1,len(lst)-i):
            if array[j-1] > array[j]:
                 array[j-1],array[j] = array[j],array[j-1]
    print (array)

bubblesort(array)
