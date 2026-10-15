#only perform calculations
def calculator(a:float,b:float,o:str):
    if o =="+":
        return a+b
    elif o=='-':
        return a-b
    elif o=='*':
        return a*b
    elif o=='/': #ZeroDivisionEror
        return a/b
    raise ValueError('Invalid operator')
#вызывает исключение типо восстань

print(calculator(2,2,'*'))
print()

#parsing convert string into numbers
def pars(a_str:str,b_str:str,o:str):
    a = float(a_str) #ValueEror
    b = float(b_str) #ValueEror
    return calculator(a,b,o)

#dialog: input 1st num, 2d num
def run():
    try:
        a = input("Enter a 1st num: ")
        b = input('Enter 2d num: ')
        o = input("Enter action(+,-,*,/: ")
        result = pars(a,b,o)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except ZeroDivisionError:
        print(f"Cannot divide by zero")

run()
