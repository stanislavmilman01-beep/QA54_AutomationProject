def clean_name(name):
    return name.strip().title()
print(clean_name('     anna smith    '))
#Anna Smith
print(clean_name('DAVID COHEN'))
#David Cohen

#Task2

def normalize_email(email):
    return email.strip().lower()

print(normalize_email(' Anna.Smith@Example.COM'))

#Task3
def is_python_file(filename):
    return filename.lower().endswith(".py")

print(is_python_file('HOmeWoRK.py'))

#Task4
def fix_message(message):
    return message.replace('bad','good')

message = 'bad weather, bad mood'
result = fix_message(message)
print(result)
print(message)

#task5
def count_letter(text,letter):
    return text.lower().count(letter.lower())

print(count_letter('Programming','Counting'))

#task6
def create_login(first_name, last_name):
    return f"{first_name.strip().lower()},{last_name.strip().lower()}"
print(create_login('Anna','SMITH'))
print()

#task7
def split_name(full_name):
    return full_name.strip().split()

print(split_name(' ANNA      SMITH'))
print()

#task8
def check_password(password):
    if len(password)<8:
        return False
    if " " in password:
        return False
    if password.isalpha():
        return False
    return True

