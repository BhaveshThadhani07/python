# immutable
'''
a = 5
print(a)
print(id(a) == id(5))
'''

# mutable
'''
Chk = [2,4,6]
print(Chk)
print(id(Chk))
print(id(Chk) == id([2,4,6]))

Chk[1] = 23
print(Chk)
print(id(Chk))  #'ll get same id as above which shows that lists are mutable(unchangable)
'''

# variable internals
b = 5
print(type(b))
myStr = 'bhavesh'
print(type(myStr))
Chk = [2,4,6]
print(type(Chk))
vowels = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5
}
print(type(vowels))
p = (1,2,3,4,5)
print(type(p))
TF = bool(True)
print(type(TF))
