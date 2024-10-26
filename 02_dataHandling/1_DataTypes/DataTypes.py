
# 1) NUMBERS
# Integers
'''
print(bool(1))
print(bool(0))
# complex numbers
a = 33 + 3.1j
b = 1.5 + 2j
print(a.real)
print(b.imag)
'''


# 2) STRINGS
'''
name = 'John'
print(name[-4])
# first char [0] index -length
print(len(name))
# name[0] = 'p'     #Error
'''
# 3) Lists & Tuples
# Lists[] -> Arrays ---mutable---
const  = [1,'john',56.787,2+3.4j,3.5E03]
const[2] = 'amulet'
print(const)

# Tuples[] ->  ---immutable--- cannot be changed
p = (1,2,3,4,5)
# p[3] = 56   #Error
print(p)

# 4) Dictionary -> Objects ---mutable---
vowels = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5
}

print(vowels['o'])
