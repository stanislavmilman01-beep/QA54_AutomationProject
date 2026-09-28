#task
"""
Write a function longest_word(words). Find and return the longest word in the list.
If several words have the same maximum length, return the first one. Do not use max().
"""

list = ['apple','pineapple','pineapplepen','applepen','abaabagalamaga']

def longest_word(words:list):
    con = ''
    for word in words:
        if len(word) > len(con):
            con = word
    return con

print(longest_word(list))
