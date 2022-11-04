# Write a Python program to triple 
# all numbers of a given list of integers. 
# Use Python map.
# sample list: [1, 2, 3, 4, 5, 6, 7]
# Triple of list numbers:
# [3, 6, 9, 12, 15, 18, 21]
# Must use map to find the expected output - 30
l=[1, 2, 3, 4, 5, 6, 7]
l1=map(lambda x:x*3,l)
print(list(l1))

