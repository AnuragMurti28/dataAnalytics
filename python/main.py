print("List and tuple examples")
# Example of a list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Example of a tuple
my_tuple = (00 ,10, 20, 30, 40, 50, 60, 70, 80, 90)
# Accessing elements
print("First element of tuple:", my_tuple[0])


try:
    my_tuple[0] = 10    
except TypeError as e:
    print("Error:", e)
# Printing the tuple
print("My list:", my_list) 
print("Tuple remains unchanged:", my_tuple) 
# Demonstrating the immutability of tuple

# slicing my_list
print("Slicing the list:[2:5]", my_list[2:5])  # Output: [2, 3, 4]
print("Slicing  the list: [:5]", my_list[:5])  # Output: [0, 1, 2, 3, 4]
print("Slicing  the list: [5:]", my_list[5:]) # Output: [5, 6, 7, 8, 9]
print("Slicing the list:[-3:]", my_list[-3:])  # Output: [7, 8, 9]
print("Slicing the list:[-3:-5]", my_list[-3:-5]) # Output: []
print("Slicing the list:[-3:-5]", my_list[-3:-8]) # Output: []
print("Slicing the list:[3:-2]", my_list[3:-2]) # Output: [3, 4, 5, 6, 7]
print("Slicing the list:[4:-3]", my_list[4:-3]) # Output: [3, 4, 5, 6, 7]
print("Slicing the list:[4:-8]", my_list[4:-8]) # Output: []
print("[-8]:", my_list[-8]) # Output: 1
print("[-7]:", my_list[-7]) # Output: 2

print("Slicing the list:[:-8]:", my_list[:-8]) # Output: [0, 1]
print("Slicing the list:[:-7]:", my_list[:-7]) # Output: [0, 1, 2]
print("Slicing the list:[-8:]:", my_list[-8:]) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Slicing the list:[-7:]:", my_list[-7:]) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# slicing my_tuple
print("my_tuple:", my_tuple )
print("Slicing the tuple:[2:5]", my_tuple[2:5])  # Output: (20, 30, 40)
print("Slicing the tuple: [:5]", my_tuple[:5])  # Output: (0, 10, 20, 30, 40)
print("Slicing the tuple: [5:]", my_tuple[5:]) # Output: (50, 60, 70, 80, 90)
print("Slicing the tuple:[-3:]", my_tuple[-3:])  # Output: (70, 80, 90)
print("Slicing the tuple:[-3:-5]", my_tuple[-3:-5]) # Output: ()
print("Slicing the tuple:[-3:-8]", my_tuple[-3:-8]) # Output: ()
print("Slicing the tuple:[3:-2]", my_tuple[3:-2]) # Output: (30, 40, 50, 60, 70)
print("Slicing the tuple:[4:-3]", my_tuple[4:-3]) # Output: (40, 50, 60, 70)
print("Slicing the tuple:[4:-8]", my_tuple[4:-8]) # Output: ()
print("[-8]:", my_tuple[-8]) # Output: 10   
print("[-7]:", my_tuple[-7]) # Output: 20
print("Slicing the tuple:[:-8]:", my_tuple[:-8]) # Output: (0, 10)
print("Slicing the tuple:[:-7]:", my_tuple[:-7]) # Output: (0, 10, 20)
print("Slicing the tuple:[-8:]:", my_tuple[-8:]) # Output: (10, 20, 30, 40, 50, 60, 70, 80, 90)
print("Slicing the tuple:[-7:]:", my_tuple[-7:]) #  Output: (10, 20, 30, 40, 50, 60, 70, 80, 90)
