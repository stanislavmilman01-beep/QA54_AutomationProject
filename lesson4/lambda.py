#lambda - make fuction "anonym" function
def double(x):
    return x*2

double_lambda = lambda x:x*2 # double dot: like return in function
double_lambda2 = lambda x:x*2 if x>0 else -x

print(double_lambda(2))
print(double(2))
print(double_lambda2(-2))
print()
add = lambda x,y:x+y
print(add(3,4))

is_even = lambda p:p%2 == 0
print(is_even(8))

grades = [90,75,88,63,100,81]
even = list(filter(lambda x:x%2 == 0, grades))
odd = list(filter(lambda x:x%2!=0,grades))

print('even grades',even)
print('odd grades',odd)