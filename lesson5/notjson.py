#dumps() - use py file and transform it in json:str
#loads() - json -> python objects str
#dump() - save py object in json format
#load() - file.json -> py
import json

user = {
    "username":'stanislav',
    "age":25,
    'is_admin':True
}

json_str = json.dumps(user)
print(json_str)
print(type(json_str))

user = json.loads(json_str)
print()
print(type(user))
print(user["username"])

test_config = {
    "url":"http://127.0.0.1:8800",
    'username':'stas',
    'password':'Aa12345',
    'timeout':20
}

with open('test_config.json','w',encoding='utf-8') as file:
    json.dump(test_config,file,indent=2,ensure_ascii=False)
#аски - это стандарт кодировки иферный А-65,а-95
#а индент формат кодировки юникода. если 2 то будет 2 пробела. исп для читабельности

with open('test_config.json','r') as file:
    config = json.load(file)
    print(config)
    print(config["url"])
    print(config["username"])

'''
Save a profile to a JSON file

Напишите функцию save_profile(name, age, city)
Функция должна создать файл profile.json со следующим содержимым:
save_profile("Maria", 30, "Haifa")
Ожидаемое содержимое файла profile.json:
{
    "name": "Maria",
    "age": 30,
    "city": "Haifa"
}

Use a dictionary and json.dump().
'''

def save_profile(name,age,city):
    profile = {
        'name':name,
        'age':age,
        'city':city
    }
    with open('profile.json', 'w', encoding='utf-8') as file:
        json.dump(profile, file, indent=4, ensure_ascii=False)
save_profile('stas',29,'Rishon')
