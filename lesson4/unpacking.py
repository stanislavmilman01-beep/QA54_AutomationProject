def login(username,password):
    print(username,password)

data = ["admin","897654"]
login(data[0],data[1])

(login(*data)) #* дублируемые аргументы
user = {
    "username":"admin",
    "password":"987654",
}
login(**user) #

user = {
    "username":"admin",
    "password":"987654",
    "remember_me":True
}
login(**user)