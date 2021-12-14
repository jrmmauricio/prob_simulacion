from student import student
import random

students = student
student_selected = students
count = None
times = random.randrange(1,1000)
list = []

list.append(students('Mauricio', 0))
list.append(students('Enrique', 0))
list.append(students('Norlie', 0))
list.append(students('Ashly', 0))
list.append(students('Cesar', 0))
list.append(students('Diego', 0))
list.append(students('Estefano', 0))
list.append(students('Jose Agreda', 0))
list.append(students('Jose Diaz', 0))
list.append(students('Maria', 0))
list.append(students('Edermar', 0))
list.append(students('Jose Angel', 0))
list.append(students('Hector Salazar', 0))
list.append(students('Jose Manuel', 0))


for i in range(random.randrange(1,1000)):
    x = random.randrange(len(list))
    list[x].prob = list[x].prob + 1

for obj in list:
    if (count is None or obj.prob > count):
        count = obj.prob
        student_selected = obj

print ('El estudiante escogido es: ', student_selected.name, 'con ', student_selected.prob, 'veces escogido en', times , 'simulaciones.')
