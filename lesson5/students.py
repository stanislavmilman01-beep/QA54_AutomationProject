'''
Read data from a CSV file

Создайте файл students.csv со следующим содержимым:

name,age
Anna,21
Tom,19
Kate,22

Напишите функцию read_students(filename)
которая выводит информацию в виде

Student: Anna (21)
Student: Tom (19)
Student: Kate (22)

Use csv.DictReader().
'''
import csv

# with open('students1.csv','w',encoding='utf-8') as file:
#     file.write(
#         '''name,age
# Anna,21
# Tom,19
# Kate,22
#         '''
#     )

def read_students(filename):
    with open('students1.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for raw in reader:
            print(f"Student:{raw['name']}({raw['age']})")

read_students('students1.csv')