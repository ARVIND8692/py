'''
Created on 06-May-2017

@author: arvindks
'''
from builtins import str

if __name__ == '__main__':
    print('Hello World')
print("This line will be printed.")

myint=7
myfloat=myint+1.3
myString='dskfsdjf'

mylist=[];

mystring,myint,myfloat,mychar='dds',23,34.2323,'d'
print(myString,mystring,myfloat,mychar)

if isinstance(myint, int):
    print ("this is awesome")

mylist.append("sjsd")
mylist.append(343)
mylist.append(3.2323)
mylist.append('w')

print(mylist)

for x in mylist:
    print(x,"dsdssd")
    
print(11+3%2)
print(mylist*4)

name = "John"
print("Hello, %s!" % name)


x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False


print(not False) # Prints out True
print((not False) == (False)) # Prints out False

print("-----------------------------------------------------")

# change this code
number = 10
second_number = 10
first_array =[]
second_array = [1,2,3]

if number > 15:
    print("1")
else:
    print("-1")

if first_array:
    print("2")
else:
    print("-2")

if len(second_array) == 2:
    print("3")
else:
    print("-3")

if len(first_array) + len(second_array) == 5:
    print("4")
else:
    print("-4")

if first_array and first_array[0] == 1:
    print("5")
else:
    print("-5")
if not second_number:
    print("6")
else:
    print("-6")

print("+++++++++++++for loops")
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7,    this input here is steps to toggle
for x in range(3, 8, 2):
    print(x)
    
print("while loops================")
# Prints out 0,1,2,3,4
def my_function(a,b):
    print("Hello From My Function!",a,b)
    
count = 0
while count < 5:
    print(count)
    my_function(2,4)
    count += 1  # This is the same as count = count + 1
    
    


    
