# Write a Python program to square the 
# elements of a list using map() function.
# Sample List: [4, 5, 2, 9]
# Square the elements of the list:
# [16, 25, 4, 81]
# Must have list as the input - 15
# Must Use map() function to solve the problem - 15
# Must give the expected output - 10

l=(map(int,input("Enter numbers ").split()))
l=(map(lambda x:x*x,l))
print(list(l))



