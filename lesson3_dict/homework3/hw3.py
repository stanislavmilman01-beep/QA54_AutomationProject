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
print()

#task 2 is_point_valid?
def is_valid_point(point: tuple):
    if point is None or point == ():
        return None
    #if not isinstance(point, tuple):
    #    return False
    #if type(point) is not tuple:
     #   return False
    if len(point) != 2:
        return False
    a, b = point
    if type(a) in (int,float) and isinstance(b, (int, float)):
        return True
    return False

print(is_valid_point((3, 5)))
print(is_valid_point((3, "5")))
print(is_valid_point([3, 5]))
print(is_valid_point((1, 2, 3)))
print(is_valid_point(()))
print(is_valid_point(None))
print(is_valid_point((True,False)))
print()

#task3 function take tuple start and fin. print reversed st-fin tuple
def print_sublist_reverse(lst, start, finish):
    if lst is None or not isinstance(lst, list) or len(lst) == 0:
        print("Wrong args")
        return
    if not isinstance(start, int) or not isinstance(finish, int):
        print("Wrong args")
        return
    if start < 0 or finish >= len(lst) or start > finish:
        print("Wrong args")
        return
    result = lst[:start] + lst[start:finish+1][::-1] + lst[finish+1:]
    print(result)

print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)
print_sublist_reverse([1, 2, 3], "0", 2)
print_sublist_reverse(None, 1, 2)
print_sublist_reverse([], 0, 1)
print_sublist_reverse([1, 2, 3], 2, 1)
print()

#task 4
def get_students_by_grade(students):
    if students is None or not isinstance(students, dict) or len(students) == 0:
        return {}
    result = {}
    for name, grade in students.items():
        if grade in result:
            result[grade].append(name)
        else:
            result[grade] = [name]
    return result

print(get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85}))
print(get_students_by_grade(None))
print(get_students_by_grade({}))
print(get_students_by_grade("hi"))

#task5