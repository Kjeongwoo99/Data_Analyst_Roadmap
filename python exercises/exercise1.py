# Python exercise 1 

print('hello world')

name = "Jeongwoo Kim"  
branch = "Data Analysis"  
age = "25"  
print("My name is: ", name)  
print("My age is: ", age) 

list1 = [1,2,3,4,5]
for i in list1:
    print(i)
    if i == 4:
        break
print('End of for loop')

# variables
name = "Devansh"  
age = 20  
marks = 80.50  
  
print(name)  
print(age)  
print(marks) 

x=y=z=50 # 50, 50, 50
a,b,c=5,10,15 # 5, 10, 15

# local variables
def add():
    a = 20
    b = 30
    c = a +b
    print('The sum is: ', c)
add()

# global variables
x = 101 
def mainFunction():
    # print a global variable 
    global x
    print(x)
    x = 'Welcome to my Python journey'
    print(x)
mainFunction()

# data types 
a = 5  
print("The type of a", type(a))  
  
b = 40.5  
print("The type of b", type(b))  
  
c = 1+3j  
print("The type of c", type(c))  
print(" c is a complex number", isinstance(1+3j,complex))  

str1 = 'hello javatpoint' #string str1    
str2 = ' how are you' #string str2    
print (str1[0:2]) #printing first two character using slice operator    
print (str1[4]) #printing 4th character of the string    
print (str1*2) #printing the string twice    
print (str1 + str2) #printing the concatenation of str1 and str2    

tup  = ("hi", "Python", 2)    
# Checking type of tup  
print (type(tup))    
  
#Printing the tuple  
print (tup)  
  
# Tuple slicing  
print (tup[1:])    
print (tup[0:1])

d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'} 
print(d.keys())
print(d.values())

def the_outer_function():  
    var = 10  
    def the_inner_function():  
        nonlocal var  
        var = 14  
        print("The value inside the inner function: ", var)  
    the_inner_function()  
    print("The value inside the outer function: ", var)  
the_outer_function()

def the_outer_function():  
    var = 10  
    def the_inner_function():  
        var = 14  
        print("Value inside the inner function: ", var)  
    the_inner_function()  
    print("Value inside the outer function: ", var)  
the_outer_function()  

# Program to show the use of keywords for, while, break, continue
for i in range(15):
    print(i+4, end=" ")
    # breaking the loop when i=9
    if i == 9:
        break 
print()

# Iteration Keywords: for, while, break, continue
i = 0
while i < 15:
    # When i has value 9, loop will jump to next iteration using continue. It will not print  
    if i == 9:
        i += 3
        continue 
    else:
        # when i is not equal to 9, adding 2 and printing the value  
        print(i + 2, end = " ")  
    i += 1 

# Exception Handling Keywords - try, except, raise, finally, and assert 
var1 = 4  
var2 = 0  
# Exception raised in the try section 
try:
    d == var1//var2 # this will raise a "divide by zero" exception.
    print(d)
# this section will handle exception raised in try block 
except ZeroDivisionError: 
    print('We cannot divide by zero')
finally:
    # If exception is raised or not, this block will be executed every time
    print("This is inside finally block")
# by using assert keyword we will check if var2 is 0  
#print ("The value of var1 / var2 is : ")  
# assert var2 != 0, "Divide by 0 error"  
#print (var1 / var2)

class passed_class:  
    pass

# string
text1='hello'    
print(text1) 

str2='''welcome  
to  
SSSIT'''    
print(str2)