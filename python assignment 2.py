print('Q1')
A='Python is a case sensitive language'
length=len(A)#length of A
print('length:',length)
print(A[length::-1])#slicing
print(A[10:26])
print(A[:9]+' object oriented'+A[26:35])
print(A.find('a'))
print(A.replace(' ',''))#replace

print('Q2')# printing sentence
name="Harshit Thakur"
SID=21104100
department_name="EE"
CGPA="9.9"

print("Hey,%s Here!"%(name))
print("My SID is %d"%(SID))
print("I am from %s department and my CGPA is %s"%(department_name,CGPA))

print('Q3')#bitwise operators
a=56 
b=10
print('a&b:',a&b)#AND
print('a|b:',a|b)#OR
print('a^b:',a^b)#XOR
print('a and b are shifted 2 bits to left:',a<<2,'and',b<<2)#shifting of bits
print('a is shifted 2 bits and b is shifted 4 bits to right:',a>>2,'and',b>>4)

print('Q4')
'''Finding the largest number'''
print('To find largest of 3 input numbers')
First_Number=float(input('Enter the first number:'))
Second_Number=float(input('Enter the second number:'))
Third_Number=float(input('Enter the third number:'))
if First_Number>=Second_Number and  First_Number>= Third_Number:
  Greatest_Number=First_Number #conditional operators
elif Second_Number>=First_Number and  Second_Number>= Third_Number:
     Greatest_Number=Second_Number
else:
     Third_Number>=Second_Number and  Third_Number>= First_Number
     Greatest_Number=Third_Number

print('The largest number is:',Greatest_Number)

print('Q5')
A=input('Enter the Sentence:')#boolean
if 'name' in A: 
 print('Yes')
else:
 print('No')

print('Q6')
'''Checking Validity of Triangle'''
print('Checking Validity of Triangle')

side1 = input('Enter the Length of first side:')
side2 = input('Enter the Length of second side:')
side3 = input('Enter the Length of third side:')

if (int(side2) + int(side3) <= int(side1)) or (int(side1) + int(side2) <= int(side3)) or (int(side2) + int(side3) <= int(side1)):  #condition to check if any of the three lengths is greater than the sum of other two.
    print('No, Triangle Cannot be formed.')
else:
    print('Yes,Triangle Can Be formed.')
    
