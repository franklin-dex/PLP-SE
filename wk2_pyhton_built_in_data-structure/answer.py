#!/usr/bin/python3

''' create an empty list 'my_list' '''

my_list = []

'''Append 10, 20, 30 to the list'''

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

'''insert value 15 at the second position of the list'''

my_list.insert(1, 15)

"""Extend list with another list [50, 60, 70]"""

my_list.extend([50, 60, 70])

'''remove the last element from the list'''

my_list.pop()

'''sort mylist in ascending order'''

my_list.sort()

'''find and print the index of the value 30 in my list'''

index_30 = my_list.index(30)
print("index value of 30:", index_30)