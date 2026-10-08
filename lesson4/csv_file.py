import csv

with open('user_1.csv','w',encoding='utf-8',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name','email','role'])
    writer.writerow(['Stas','stas@gm.com','QA'])
    writer.writerow(['Jula','u@gm.com','trainie'])

with open('user_1.csv') as file:
    reader = csv.reader(file)
    print(type(reader))
    for row in reader:
        print(row)

with open('user_1.csv','r',encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        print(row['name'],'-',row['role'])