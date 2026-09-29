#task 1 clean_name
from xmlrpc.client import FastParser


def clean_name(name):
    return name.strip().title()

print(clean_name('    AnNNA SMIth   '))
print(clean_name('DAVID COHEN'))

#task 2 normilize email
def normilize_email(email):
    return email.lower().strip()

print(normilize_email('    Aaaw@gmail.coM  '))

#task3 check a file name: function return bool, function work with registr
def is_python_file(filename) -> bool:
    py = filename.lower().strip()
    return py.endswith('.py')

print(is_python_file('hw.py'))
print(is_python_file('HW.PY'))
print(is_python_file('hw.txt'))

#task4 fix massage: replacing all words "bad" with "good", must return both massages
def fix_message(massage):
    result = massage.replace("bad","good")
    return result

massage = "bad weather,bad mood"
result = fix_message(massage)
print(result)
print(massage)

#task 5 count()
def count_letter(text,letter):
    text = text.lower()
    letter = letter.lower()
    return text.count(letter)

print(count_letter("Programming is very imPortant", 'P'))
print(count_letter("PrograMming is very imPortant", 'm'))

#task 6 login creator
def create_login(first_name:str,last_name:str):
    #first_name = first_name.lower().strip()
    #last_name = last_name.lower().strip()
    return "_".join([first_name.lower().strip(), last_name.lower().strip()])
    #return "_".join([first_name,last_name])

print(create_login('ANNA  ', '   SMIth '))

#task 7*
def split_name(full_name) ->list:
    return full_name.strip().split(' ')

print(split_name("   ANNA SMITH   "))
print('')
#task 8**
def check_password(psw):
    if len(psw) >= 8:
        return psw.isalnum()
    else:
        return False

print(check_password('phython123'))
print(check_password('phython'))
print(check_password('phy1234'))
print(check_password('phy 1234'))