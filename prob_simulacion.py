from student import student
import random

students = student
student_selected = students

list = []
resp= 'Y'

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

while resp=='y' or resp=='Y':
    print ('Ingrese el numero de simulaciones que desea realizar')
    numero= input()
    times=int(numero)

    for i in range(times):
        x = random.randrange(len(list))
        list[x].prob = list[x].prob + 1

    escodigo= random.randrange(len(list))
    
    print ('El estudiante escogido es: ', list[escodigo].name, 'con ', list[escodigo].prob, 'veces escogido en', times , 'simulaciones.')
    for j in range(len(list)):
        list[j].prob= 0
    print('Desea hacer otra simulacion? y=si / n=no')
    resp= input()
