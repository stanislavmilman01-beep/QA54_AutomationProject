'''
1. Напишите функцию:
get_product(products, index)
Функция должна возвращать товар из списка по переданному индексу.
Если такого индекса нет, вернуть:
Product index is out of range
Примеры:
products = ["coffee", "tea", "milk"]
print(get_product(products, 0))
# coffee
print(get_product(products, 7))
# Product index is out of range
Обработайте IndexError.
'''
def get_product(product, index:int):
    try:
        #if type(product) is list:
            data = product[index]
            return data

    except IndexError:
        return 'Product index is out of range'

products = ["coffee", "tea", "milk"]
print(get_product(products, 0))
print(get_product(products, 7))
print()
'''
2. Напишите функцию:
get_settings_value(settings, key)
Функция должна возвращать значение из словаря по ключу.
Если ключ отсутствует, вернуть:
Setting was not found
Примеры:
settings = {
"language": "English",
"theme": "dark"
}
print(get_settings_value(settings, "theme"))
# dark
print(get_settings_value(settings, "font"))
# Setting was not found
Обработайте KeyError.
'''

def get_settings_value(settings,key):
    try:
        word = settings[key]
        return word
    except KeyError:
        return 'Setting was not found'

settings = {
"language": "English",
"theme": "dark"
}

print(get_settings_value(settings, "theme"))
#dark
print(get_settings_value(settings, "font"))
#Setting was not found
print()

'''
3. Напишите функцию:
calculate_total_price(price, quantity)
Функция получает два значения, преобразует их в числа и возвращает результат умножения.
Обработайте отдельно:
ValueError, если значение невозможно преобразовать в число.
TypeError, если передан неподходящий тип данных.
Примеры:
print(calculate_total_price("12.5", "4"))
# 50.0
print(calculate_total_price("coffee", "4"))
# Value must be a number
print(calculate_total_price(None, 4))
# Invalid data type
Не используйте один общий except Exception.
'''

def calculate_total_price(price, quantity):
    try:
        price_int = float(price)
        quantity_int = float(quantity)
        total = price_int*quantity_int
        return total
    except TypeError:
        return 'Invalid data type'
    except ValueError:
        return 'Value must be a number'

print(calculate_total_price("12.5", "4"))
# 50.0
print(calculate_total_price("coffee", "4"))
# Value must be a number
print(calculate_total_price(None, 4))
# Invalid data type

'''
4. Напишите функцию:
def read_temperature():
Функция должна:
Запросить у пользователя температуру с помощью input().
Преобразовать значение в float.
Если преобразование прошло успешно, вывести:
Temperature was entered successfully
Если пользователь ввёл неправильное значение, вывести:
Invalid temperature
Независимо от результата всегда вывести:
Program finished
'''

def read_temperature():
    temp = input('Enter current t*: ')
    try:
        if type(temp) is float:
            print('Temperature was entered successfully')
            return 'Programm finished'
    except TypeError:
        print('Invalid temperature')
        return 'Programm finished'
    except ValueError:
        print('Invalid temperature')
        return 'Programm finished'

print(read_temperature())