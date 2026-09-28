def greet(name):
    return f'Hello,{name}!'

result =greet('Stanislav')
print(result)
#argument exist
# result2 = greet()
# print(result2)
#argument not exist
def create_user (name,role = 'user'):
    return {
        'name': name,
        'role': role
            }
print(create_user('Alex'))
print(create_user('Kris','admin'))

def cal_discount(price,discount=20):
    return price - (price * discount/100)

print(cal_discount(100))
print(cal_discount(100, 25))


# def foo(a=2,b=3):
#     return a+b
# print(foo(5))
#when argument not accorded - first one will be changed

def add_tests(name, results =None):
    if results is None:
        results = []
    results.append(name)
    #.append is Append object to the end of the list.
    return results

print(add_tests('test_reg'))
print(add_tests('test_log'))

def create_user2(username,email,role):
    return f"{username} ({email}) - {role}"
print(create_user2('Stas', 'test@gm.com','manual'))

print(create_user2(role='Project',username='Alex',email='test2@gm.com'))

print(create_user2('Yula', role='QA',email='qa@gm.com'))
