'''
Created on 06-May-2017

@author: arvindks
'''

class MyClass:
    variable = "blah"

    def function1(self):
        print("This is a message inside the class.")
        
myobject1=MyClass() 
myobjecty=MyClass()

print(myobject1.variable)

myobjecty.variable = "yackity"
print(myobjecty.variable)

myobject1.function1()


# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1=Vehicle()
car2=Vehicle()
car2.value=120

# test code
print(car1.description())
print(car2.description())