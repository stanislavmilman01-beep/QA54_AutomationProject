# def div_int(a,b):
#     return a/b
# print('start program')
# result = div_int(10,0)
# print(result)
# print('end program')
#
#try/except
print('hello world')
try:
    result = 10/0
    print(result)
except Exception as e:
    print('an error ocured: ',e)
#print('BY')
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result: ",result)
except ValueError:
    print("Error: Please enter a valid number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
