print("Question 1")  #Counting the occurances in string
a=str(input("ENTER ANY STRING: ")) 
list=a.split() 
dict={} 
if list.__len__()==1:   #if only one character then tell occurrance of each alphabet
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
else:                   
    for i in list:        #if multiple characters then tell occurrance of each word           
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
    
print("Question 2") #date finder
def is_leap(a):
  
    if a % 4 == 0:                #finding the leap year
        if a % 100 == 0:
            if a % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    return leap

Day = int(input("Enter the Day:"))
Month = int(input("Enter the Month:"))
Year = int(input("Enter the Year:"))

if Day < 1 or Day > 31:
    print("Date does not exist.")
    exit()

elif Month < 1 or Month > 12:
    print("Date does not exist")
    exit()

elif Year < 1800 or Year > 2025:
    print("Date does not exist.")
    exit()

Final_Day = Day
Final_Month = Month
Final_Year = Year

if Month in [1, 3, 5, 7, 8, 10]:
    if Day == 31:
        Final_day = 1
        Final_Month += 1
    else:
        Final_Day += 1

elif Month == 12:
    if Day == 31:
        output_day = 1
        output_month = 1
        Final_Year += 1

elif Month in [4, 6, 9, 11]:
    if Day == 30:
        output_day = 1
        Final_Month += 1
    else:
        Final_Day += 1

elif Month == 2:                       #special case of february in leap year
    if is_leap(Year):
        if Day > 29:
            print("Date does not exist")

        elif Day == 29:
            Final_Day = 1
            Final_Month += 1
        else:
            Final_Day += 1
    else:
        if Day > 28:
            print("Date does not exist")

        elif Day == 28:
            output_day = 1
            Final_Month += 1
        else:
            Final_Day += 1

Result = f"{Final_Day}/{Final_Month}/{Final_Year}"
print("The next Date is :",Result )

print("Question 3")         #creating tuples with elements of number and its square
input_list = input('Enter elements of list(separated by space):')
user_list = input_list.split()
print('list: ', input_list)

for a in range(len(user_list)):
    user_list[a] = int(user_list[a]) #creating list containing only int elements
result =[(user_list[a], user_list[a]**2) for a in range(len(user_list))] 
print(result)

print("Question 4")#program for grades and performances

grades= int(input("Enter the Grade:"))

if grades< 4 or grades> 10:
    print("Error")#error in grades
else:
    # Formation of dictionary for storing grades

    dictionary = {4: ['D', 'Poor'], 5: ['C', 'Below Average'], 6: ['C+', 'Average'], 7: ['B', 'Good'],
                            8: ['B+', 'Very Good'],
                            9: ['A', 'Excellent'], 10: ['A+', 'Outstanding']}

    print(f"Your Grade is {dictionary[grades][0]}"
          f", and {dictionary[grades][1]} performance")
 
print("Question 5")   #printing the pattern
h=0
X="ABCDEFGHIJK"
for h in range(6):
    i=h
    while (i>0):
        print(" ",end="")
        i=i-1
    k=0
    for k in range (len(X)-2*h):#removing characters from the string
        print(X[k],end="") 
    print("\n")    
print("Question 6")                                                                  
SID=int(input("Enter your SID:")) #sorting and searching using dictionaries
name=input("Enter name: ")
students={SID:name}

while True:
    option=input("Are you interested in entering another student entry(Y or N):").upper()
    if option=='Y':
        SID=int(input("Enter SID: "))
        name=input("Enter name: ")
        students[SID]=name
    elif option=='N':
        break
    else:
        print("Invalid input!")

print(students)#part a

print({k:v for k,v in sorted(students.items(), key=lambda x:x[1])})#part b

print({k:v for k,v in sorted(students.items())})#part c

SID=int(input("Search Name with SID:"))#part d
print(students[SID])

print("Question 7") #Printing fibonacci sequence and its average
def fibonacci_term(n):#defining a function
    if n<=1:
        return n
    else:
        return(fibonacci_term(n-1)+fibonacci_term(n-2))
number=int(input("NUMBER OF TERMS IN SERIES:"))
if number <=0:
    print("Error")
else:
    print("Fibonacci sequence:")
    sum=0
    for i in range(number):
        print(fibonacci_term(i))
        sum=sum+fibonacci_term(i)
average=float(sum/number)  #average
print("AVERAGE OF THE FIBONACCI SERIES IS:",average)

print("Question 8")
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}

#part a
Set_a = Set1 ^ Set2

# Part b
Set_b = Set_b = (Set1 - (Set2 | Set3)) | (Set2 - (Set1 | Set3)) | (Set3 - (Set1 | Set2))

# Part c
Set_c = (Set1 & Set2)|(Set2 & Set3)|(Set3 & Set1)
# Part d
Set_d = set(range(1,11)) - Set1

# Part e
Set_e = set(range(1,11)) - Set1 - Set2 - Set3

print("GIVEN SETS:")
print("Set1 is ", Set1)
print("Set2 is ", Set2)
print("Set3 is ", Set3)
print("Set of Elements that are in Set1 and Set2 but not in both:", Set_a)
print("Set of Elements that are exactlyin only Set:", Set_b)
print("Set of Elements that are exactly in two Sets:", Set_c)
print("Set of integers from 1 to 10 that are not in Set1:", Set_d)
print("Set of integers from 1 to 10 that are not in all the three Sets:", Set_e)
