##dict

dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
print(dict_sample)
##acess to elements 1
dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
print(dict_sample['Company'])

##acess to elements 2
dict = {'Name': 'Mercy', 'Age': 23, 'Course': 'Accounting'}
print("Student Name:", dict['Name'])
print("Course:", dict['Course'])
print("Age:", dict['Age'])
##double_dicts
dict_sample = {
1: {'student1': 'Nicholas', 'student2': 'John', 'student3': 'Mercy'}, 
2: {'course1': 'Computer Science', 'course2': 'Mathematics', 'course3': 'Accounting'}
}

print(dict_sample[1]['student1'])
##adding
dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
dict_sample["Capacity"] = "1800CC"
print(dict_sample)
##adding 2
MyDictionary = {}
MyDictionary['Values'] = 1, "Pairs", 4
print("\n3 elements have been added: ")
print(MyDictionary)

##updating elements
dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}

dict_sample["year"] = 2014

print(dict_sample)

##deleting elements
dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
del dict_sample["year"]
print(dict_sample)

##clear the dist

dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
dict_sample.clear()
print(dict_sample)


## len()

dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
print(len(dict_sample))

##copy()
dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
x = dict_sample.copy()

print(x)

##items()
dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}

for k, v in dict_sample.items():
    print(k, v)

##fromkeys()
name = ('John', 'Nicholas', 'Mercy')
age = 25

dict_sample = dict.fromkeys(name, age)

print(dict_sample)

##setdefault()
dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}

x = dict_sample.setdefault("color", "Gray")
print(x)

##keys()
dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
x = dict_sample.keys()

print(x)
