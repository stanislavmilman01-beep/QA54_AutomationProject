#task1 print list reverse

def print_list_reverse(lst):
    if lst is None or not isinstance(lst, list) or len(lst) == 0:
        print('Wrong list')
    else:
        #print(lst[::-1])
        reversed_copy = list(reversed(lst))
        print(reversed_copy)

print_list_reverse([1,2,3,4,5])
print_list_reverse([])
print_list_reverse('12345')
print_list_reverse([None])

#task 2 is_point_valid?
def is_valid_point(point:tuple):
    if point is isinstance(point, tuple) or len(point) != 2:
        return False
    if point is None or point == ():
        return None
    a, b = point
    if a is int or float and b is int or float:
        return True

print(is_valid_point((3, 5)))     # True
print(is_valid_point((3, "5")))   # False
print(is_valid_point([3, 5]))    # False
print(is_valid_point((1, 2, 3)))  # False
print(is_valid_point(()))          # None
print(is_valid_point(None))       # None

