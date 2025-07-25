import array

# Arrays are linear data structures that store elements in a sequential manner.
# In Python, we can use lists to represent arrays.
my_array = [1, 2, 3, 4, 5]

print(my_array[2])

# Create an integer array
# this array is immutable
# and only can store integers
numbers = array.array('i', [10, 20, 30, 40, 50])
print(numbers[3])
