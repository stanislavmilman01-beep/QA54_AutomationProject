#task1 count_vovels
def count_vovels(s):
    counter = 0
    if not isinstance(s, str) or s== "":
        return -1
    for i in s:
        if i.lower() in 'aeoiu':
            counter +=1
    return counter

print(count_vovels('  Hello  '))
print(count_vovels(''))
print(count_vovels(1))
print()

#task2
def is_palindrome(s):
    if not isinstance(s,str) or s == "":
        return False
    s = s.strip().lower().replace(' ','')
    rev = s[::-1]
    if rev == s:
        return True
    else:
        return False

print(is_palindrome('level'))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("hello"))
print(is_palindrome(None))
print()

#task3
def mask_email(email):
    if not isinstance(email,str) or email == '':
        return 'Invalid email'
    key,sep,value = email.partition('@')
    if not sep:
        return 'Invalid email'
    key = f'{key}'

    print(f'{key}{sep}{value}')

print(mask_email('stanislavm@gmail.com'))
print(mask_email('qa@test.com'))
print(mask_email('qaagmail.ocm'))