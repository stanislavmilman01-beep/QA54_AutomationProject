with open('user.txt','w',encoding='utf-8') as file:
    file.write('Kristina\n')
    file.write('Alex\n')

    #read() - reading whole file
with open('user.txt','r',encoding='utf-8') as file:
    content = file.read()
    print(content)

    #readlines()
with open('user.txt','r',encoding='utf-8') as file:
    lines = file.readlines()
    print(lines)
    #зачем надо? - чтобы брать данные из файла и раюотать с ним!
    for line in lines:
        print(line.strip())

with open('user.txt','r',encoding='utf-8') as file:
    for line in file:
        print(line.strip())