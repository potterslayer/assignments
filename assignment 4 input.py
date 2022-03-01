print("Question 1")
'''Tower of Hanoi with 3 disks'''
def Tower_Of_Hanoi(n , start_rod, end_rod, middle_rod):
	if n == 0:
		return
	Tower_Of_Hanoi(n-1, start_rod, middle_rod, end_rod)
	print("Move disk",n,"from rod",start_rod,"to rod",end_rod)
	Tower_Of_Hanoi(n-1, middle_rod,end_rod,start_rod)
n = 3    #defining number of disks
Tower_Of_Hanoi(n,'A','C','B')
print("Question 2")
"""Printing Pascal Triangle using recursive and iterative methods"""

print("Recursive Method")#recursive method

def pascal_triangle(n):
    if n == 0:
        return []

    elif n == 1:
        return [[1]]

    else:
        next_row = [1]
        result = pascal_triangle(n - 1)
        last_row = result[-1]

        for i in range(len(last_row) - 1):
            next_row.append(last_row[i] + last_row[i + 1])

        next_row += [1]
        result.append(next_row)
        return result

N = int(input("Enter the number of rows you want:"))

if N< 0:        # Condition to check if the number of rows entered are positive.
    print("Error!: Number of rows cannot be -ve.")
    exit()

arr = pascal_triangle(N)
width = len(str(arr[-1])) - 2

for i in arr:
    strng = ""

    for h in i:
        strng += (f"{h}" + "   ")

    print(strng.center(width, " "))

print("Iterative Method")#Iterative Method

N= int(input("Enter the number of rows you want:"))

if N< 0:     #Checking if number of rows are negative.
    print("Error!: Number of rows cannot be -ve.")
    exit()

arr = [[1]]

while len(arr) < N:   #using while loop

    next_row = [1]
    last_row = arr[-1]

    for i in range(len(last_row) - 1):
        next_row.append(last_row[i] + last_row[i + 1])

    next_row += [1]
    arr.append(next_row)

width = len(str(arr[-1])) - 2
for i in arr:
    string = ""

    for k in i:
        string += (f"{k}" + "   ")

    print(string.center(width, " "))

print("Question 3")
num1, num2 = map(int,input("Enter 2 numbers: ").split())#taking input of numbers
Quotient = num1 // num2
Remainder = num1 % num2
#Checking if values are callable
print("(a) Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))
#Checking if all values are non zeros
if (Quotient == 0):
    print("(b) The quotient is zero")
if (Remainder == 0):
    print("(b) The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("(b) All the values are non zero")
#part(c)
list = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]
result = []
for i in range(len(list)):
    if list[i] > 4:
        result.append(list[i])
print(f"(c) Filtered out numbers that are greater than 4 are : {result}")
#part (d)
setresult = set(result)
print("(d) Set:",setresult)
#Converting it to immutable set
immutableSet = frozenset(setresult) 
print("(e) Immutable set:",immutableSet)
#hashing out the max value of the above set
print("(f) Hash value of max value:", hash(max(immutableSet)))

print("Question 4")
# Creating a class named Student.
class Student:

    def __init__(self, _name: str, _roll_number: int):
    
        self.name = _name
        self.roll_number = _roll_number

    def __del__(self):                      #Deleting Objects
        print("All the objects deleted")

# Creating an instance named Harshit.
Student_1 = Student("Harshit", 21104100)

# Printing out values assigned to instance variables.
print(f"Name ={Student_1.name}\nRoll_no = {Student_1.roll_number}")

print("Question 5")
class Employee:
    def __init__(self, _name, _salary):
        self.name = _name
        self.salary = _salary 
#creating instances of class Employee
Mehak = Employee("Mehak", 40000)
Ashok = Employee("Ashok", 50000)
Viren = Employee("Viren", 60000)

# updating salary of Mehak to 70000
Mehak.salary = 70000
print(f"(a) The updated salary of {Mehak.name} is {Mehak.salary} ")
#part (b) deleting a record
print("(b)Record of Viren deleted", end='')
del Viren
print("\n")
print("Question 6")
X=input("Word by George:  ").lower()        #taking input of words
Y=input("Word by Barbie:  ").lower()
def word(a):             #defining a function
    if a == "":
        return [a]
    else:
        ans = []
        for w in word(a[1:]):
            for b in range(len(w)+1):
                ans.append(w[:b]+a[0]+w[b:])
        return ans

if X in word(Y):
    print("True Friendship")      #if length and letters equal then true friendship
else:
    print("False Friendship")
