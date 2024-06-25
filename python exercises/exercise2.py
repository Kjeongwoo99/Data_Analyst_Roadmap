# If else, loops, for loop, while loop, break, continue, pass, strings, lists, tuples, dictionary, array 

# if statement
num = int(input("enter the number: "))
if num%2==0:
    print("the given number is an even number")

# if-else statement
age = int(input("enter your age:"))
if age >= 18:
    print("you're eligible to vote")
else:
    print("you're not eligible to vote")

# if elif statement
marks = int(input("Enter the marks? ")) 
if marks > 85:
    print("Congrats ! you scored grade A")
elif marks > 75 and marks <= 85:
    print("You scored grade B+")
elif marks > 65 and marks <= 75:
    print("You scored grade B") 
elif marks > 55 and marks <= 65:
    print("You scored grade C")
else:
    print("You did not pass")

# for loop 
numbers = [4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 2]  
square = 0
squares = []
for n in numbers:
    square = n**2
    squares.append(square)
numbers = [4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 2]  

numbers_ = [3, 5, 23, 6, 5, 1, 2, 9, 8] 
sum_ = 0

for num in numbers_:
    sum_ = sum_ + num ** 2 
print("The sum of squares is: ", sum_)

string = 'Python loop'
for s in string:
    if s == 'o':
        print("if block")
    print(s)

# range function 
my_list = [3, 5, 6, 8, 4]
for iter_var in range(len(my_list)):
    my_list.append(my_list[iter_var] + 2)
print(my_list)

# while loop
counter = 0
while counter < 10:
    counter += 3 
    print('python loops')

i=1  
while i<=10:  
    print(i, end=' ')  
    i+=1

m=1  
while m<51:  
    if m%5 == 0 or m%7==0 :  
        print(i, end=' ')  
    m+=1 

nums = [34, 12, 54, 23, 75, 34, 11] 
def prime_number(number):
    condition= 0
    iteration = 2
    while iteration <= number/ 2:
        if number % iteration == 0:
            condition = 1 
            break
        iteration += 1 
    if condition == 0:
        print(f"{number} is a PRIME number")   
    print(f"{number} is not a PRIME number") 
for i in nums:  
    prime_number(i) 

for string in "While Loops":  
    if string == "o" or string == "i" or string == "e":  
         continue  
    print('Current Letter:', string)

# continue
for string in "Python Loops":
    if string == 'o' or string == 'p' or string == 't':
        continue 
    print("current letter:", string)

for iterator in range(10, 21):
    if iterator == 15:
        continue
    print(iterator)

# break - stops the execution of the loop when the break statement is reached 
for string in "Python Loops":
    if string == 'L':
        break 
    print("current letter:", string)

# break statement example  
my_list = [1, 2, 3, 4]  
count = 1  
for item in my_list:  
    if item == 4:  
        print("Item matched")  
        count += 1  
        break  
print("Found at location", count) 

# string

str = "Hello"     
str1 = " world"    
print(str*3) # prints HelloHelloHello    
print(str+str1)# prints Hello world     
print(str[4]) # prints o                
print(str[2:4]); # prints ll                    
print('w' in str) # prints false as w is not present in str    
print('wo' not in str1) # prints false as wo is present in str1.     
print(r'C://python37') # prints C://python37 as it is written    
print("The string str : %s"%(str)) # prints The string str : Hello

# escaping single quotes  
print('They said, "What\'s going on?"')  
  
# escaping double quotes  
print("They said, \"What's going on?\"")  

# Using Curly braces  
print("{} and {} both are the best friend".format("Devansh","Abhishek"))  
  
#Positional Argument  
print("{1} and {0} best players ".format("Virat","Rohit"))  
  
#Keyword Argument  
print("{a},{b},{c}".format(a = "James", b = "Peter", c = "Ricky"))  

# list 
list1 = [12, 14, 16, 39, 40]  
# iterating  
for i in list1:   
    print(i) 

list1 = [1,2,2,3,55,98,65,65,13,29]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

# function
def function(n1, n2):
    print("number 1 is: ", n1)    
    print("number 2 is: ", n2)
print("Passing out of order arguments" )    
function(30, 20)

print( "Passing only one argument" )    
try:    
    function( 30 )    
except:    
    print( "Function needs two positional arguments" ) 


