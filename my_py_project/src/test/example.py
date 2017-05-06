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

    
