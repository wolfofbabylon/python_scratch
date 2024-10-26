course = ['history','math', 'physics']
course2 = ['Art', 'Education']

print(course)

print (course[1:])


course.append('Art')
print (course)

course.insert(0,'Art')
print (course)



course.extend(course2)
print (course)

course.remove('math')
print(course)

course.sort()
print(course)

sorted(course)
print(course)

sorted_courses=sorted(course)
print(sorted_courses)

for index, course in enumerate(course):
    print(index, course)

course_str = '- ' . join(course)
print(course_str)

