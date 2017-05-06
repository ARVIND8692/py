'''
Created on 06-May-2017

@author: arvindks
'''
#dictionaries are like hashmap
import ClassAndObject


phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)




phonebook2 = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook2)


for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

#can be deleted either by 'del' or iten.pop
del phonebook["John"]
print(phonebook)


phonebook["John"] = 938477566
print(phonebook)

phonebook.pop("John")
print(phonebook)

if "Jack" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

print(ClassAndObject.car1.value)