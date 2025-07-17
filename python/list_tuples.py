print("List and tuple examples")
# Example of a list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Example of a tuple
my_tuple = (00 ,10, 20, 30, 40, 50, 60, 70, 80, 90)
my_list2 =[23, 25, 28, 27, 24, 29, 26, 22, 21, 20]
# Accessing elements
print("First element of tuple:", my_tuple[0])


try:
    my_tuple[0] = 10    
except TypeError as e:
    print("Error:", e)
# Printing the tuple
print("My list:", my_list) 
print("my_list[::-1]:", my_list[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print("My tuple:", my_tuple)
print("my_tuple[::-1]:", my_tuple[::-1])  # Output: (90 

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
# #######################################################
################## List and Tuple Operations Completed ##################
# #######################################################
print("List and tuple operations completed successfully.")
# #######################################################
# #######################################################

print("List and tuples methods")
# List methods

print("my_list2:", my_list2)
print("List methods:")
print("Append 30 to my_list2 my_list2.append(30):")
my_list2.append(30)
print("After appending 30:", my_list2)  # Output: [23, 25, 28, 27, 24, 29, 26, 22, 21, 20, 30]
print("Insert 100 at index 2  my_list2.insert(2, 100):")  
my_list2.insert(2, 100)
print("After inserting 100 at index 2:", my_list2)  # Output: [23, 25, 100, 28, 27, 24, 29, 26, 22, 21, 20, 30]
print("Remove 100 from my_list2 my_list2.remove(100):")
my_list2.remove(100)
print("After removing 100:", my_list2)  # Output: [23, 25, 28, 27, 24, 29, 26, 22, 21, 20, 30]
print("Pop the last element from my_list2| my_list2.pop():") 
popped_element = my_list2.pop()
print("Popped element:", popped_element)  # Output: 30
print("After popping the last element:", my_list2)  # Output: [23, 25, 28, 27, 24, 29, 26, 22, 21, 20]
print("Count occurrences of 22 in my_list2 | my_list2.count(22):")    
count_22 = my_list2.count(22)
print("Count of 22:", count_22)  # Output: 1
print("Index of 21 in my_list2 | my_list2.index(21):")
index_21 = my_list2.index(21)
print("Index of 21:", index_21)  # Output: 8
print("Sort my_list2 in ascending order | my_list2.sort():")
my_list2.sort()
print("After sorting:", my_list2)  # Output: [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
print("Sort my_list2 in descending order | my_list2.sort(reverse=True):")
my_list2.sort(reverse=True)
print("After sorting in descending order :", my_list2)  # Output: [29, 28, 27, 26, 25, 24, 23, 22, 21, 20]

print("Reverse my_list2")
my_list2.reverse()
print("After reversing:", my_list2)  # Output: [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

print("sorting can be also applied to strings")
my_string_list = ["banana", "apple", "cherry", "date"]
print("Original string list:", my_string_list)  
my_string_list.sort()
print("Sorted string list:", my_string_list)  # Output: ['apple', 'banana', 'cherry', 'date']
my_string_list.sort(reverse=True)
print("Sorted string list in descending order:", my_string_list)  # Output: ['date', 'cherry', 'banana', 'apple']
print("List methods completed successfully.")

my_list2.remove(22)  # Remove the first occurrence of 22
print("After removing 22:", my_list2)  # Output: [20, 21, 23, 24, 25, 26, 27, 28, 29]
# #######################################################
# #######################################################
my_list2.pop(3)  # Pop the element at index 3
print("After popping my_list2.pop(3) the element at index 3:", my_list2)  # Output: [20, 21, 23, 25, 26, 27, 28, 29]    
print("my_list2 after popping the element at index 3:", my_list2)  # Output: [20, 21, 23, 25, 26, 27, 28, 29]
# #######################################################
# #######################################################



# Tuple methods
print("Tuple methods:")
print("Tuples are immutable, so they do not have methods like append, insert, remove, pop, sort, or reverse.")
print("However, you can convert a tuple to a list, perform operations, and convert it back to a tuple.")
# Example of converting a tuple to a list and back
my_tuple_list = list(my_tuple)
print("Converted tuple to list:", my_tuple_list)  # Output: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
my_tuple_list.append(100)
print("After appending 100 to the list:", my_tuple_list)  # Output: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
my_tuple = tuple(my_tuple_list)
print("Converted list back to tuple:", my_tuple)  # Output: (0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print("Tuple methods completed successfully.")
# #######################################################
# #######################################################
test_tuple1 = (50);
print("Test_tuple1:", test_tuple1)  # Output: (50,)
print("Type of test_tuple1:", type(test_tuple1))  # Output: <class 'int  '>
test_tuple2 = (50,) # Adding a comma to make it a tuple 
print("Test_tuple2:", test_tuple2)  # Output: (50,)
print("Type of test_tuple2:", type(test_tuple2))  # Output: <class 'tuple'>
testStr_tuple = ("Anurag",)
print("TestStr_tuple:", testStr_tuple)  # Output: ('Anurag',)   

print("Type of testStr_tuple:", type(testStr_tuple))  # Output: <class 'tuple'> 

testStr_tuple2 = ("Anurag")  # Without a comma, it's a string
print("TestStr_tuple2:", testStr_tuple2)  # Output: Anurag  
print("Type of testStr_tuple2:", type(testStr_tuple2))  # Output: <class 'str'>

# #######################################################   

# #######################################################
print("List and tuple examples completed successfully.")    
# #######################################################
# #######################################################
print("End of list and tuple examples.")
# #######################################################
# #######################################################
#Sample logic building question
print("Sample logic building question:")


#Write a program to enter names of their 3 favourite movies and store them in a list.
movies = []
print("Enter the names of your favourite movies:")
movie1 = input("Movie 1: ")
movie2 = input("Movie 2: ")
movie3 = input("Movie 3: ")

movies.append(movie1)
movies.append(movie2)       
movies.append(movie3)

print("Your favourite movies are:", movies)
# #######################################################

movies2 = []
print("Enter the names of your favourite movies:")
mov = input("Movie 1: ")
movies2.append(mov) 
mov = input("Movie 2: ")
movies2.append(mov)
mov = input("Movie 3: ")
movies2.append(mov)
print("Your favourite movies2 are:", movies2)

movies2.append((input("Movie 4: ")))
movies2.append((input("Movie 5: ")))    
print("Your favourite movies2 after adding two more movies are:", movies2)
# #######################################################
# #######################################################
print("write program to check palindrome using list[]")
palindrome_list = [22, "Anurag", "Anurag", 22]
print("Palindrome list:", palindrome_list)

# Function to check if a list is a palindrome
# A palindrome is a sequence that reads the same backward as forward
def is_palindrome(lst):
    return lst == lst[::-1] #reverses the list by traversing it from the end to the start

print("Checking if the palindrome list is a palindrome:")
is_palindrome_result = is_palindrome(palindrome_list)
print("Is the palindrome list a palindrome?", is_palindrome_result)  # Output: True


palindrome2_list = [22, "Anurag", "HS", 22]
print("Palindrome2 list:", palindrome2_list)

# Function to check if a list is a palindrome using reverse()   
def is_palindrome_reverse(lst):
    reversed_list = lst.copy()  # Create a copy of the list
    reversed_list.reverse()  # Reverse the copied list
    return lst == reversed_list  # Compare the original and reversed lists
print("Checking if the palindrome2 list is a palindrome using reverse():")
is_palindrome_reverse_result = is_palindrome_reverse(palindrome2_list)
print("Is the palindrome2 list a palindrome using reverse()?", is_palindrome_reverse_result)  # Output: False

#####Palindrome check using a function complete##########
#####Write a program to check counting students in a class using tuple scored Grade A ######
def count_students_with_grade_A(students):
    # Count the number of students with grade A
    grade_A_count = students.count("A") 
    return grade_A_count 

# Example tuple of students and their grades
grade = ("A", "B", "A", "C", "A", "B", "A", "C", "D", "B","D", "A")
print("Grade tuple:", grade)
count_gradeA= count_students_with_grade_A(grade)
print("Number of students with grade A:", count_gradeA)  # Output: 4

####Store above tuple in a list  & sort from A to D ######
def list_sort_grades(grades):
    # Convert the tuple to a list
    grades_list = list(grades)
    # Sort the list in ascending order
    grades_list.sort()  # Sorts the list in ascending order
    # Convert the sorted list back to a tuple
    sorted_grades = tuple(grades_list)
    return sorted_grades
# Example tuple of grades
sorted_grades = list_sort_grades(grade)
print("Sorted grades tuple:", sorted_grades)  # Output: ('A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'D', 'D')
# #######################################################







