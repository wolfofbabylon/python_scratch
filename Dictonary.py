student = {'name:': 'John' , 'age:' :25, 'courses:' : ['Math', 'CompSci'] }

#student.update({'name': 'Jane', 'age': 26, 'phone': '5556666'})        
#print (student.get('phone'))
#print (student.get('name'))

#age = student.pop('age')
#print(student)
#print(age)

#print(student.keys())
#print(student.items())


for key, value in student.items():
    print(key, value)