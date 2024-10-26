# 1) ARITHMETIC

    # unary
'''
a = 0   #in python 0 means false
print(-a)
print(not a)
b = False
print(not b)    
'''

#binary
'''
dividend = int(input('Enter Dividend: '))
divisor = int(input('Enter Divisor: '))

print('Original Result: ', dividend/divisor)

print('Flooring the Result: ', dividend//divisor)

remainder = dividend%divisor
print('Remainder: ', remainder)

if remainder>0 :
    print('Instead of',dividend,'you should enter',dividend-remainder,'to get 0 as a remainder')
'''

#Exercise -> Area of circle of radius 3.75 metres
'''
radOrDia = input('Would you like to enter radius or diameter of the circle? ')
if radOrDia == 'radius':
    radius = int(input('Enter radius of the circle: '))
    area = 3.14*radius**2
    print('Area of Circle of Radius =', radius, 'm = ', area)


elif radOrDia == 'diameter':
    diameter = int(input('Enter diameter of the circle: '))
    diameterRadius = diameter/2
    area = 3.14*diameterRadius**2
    print('Area of Circle of Diameter =', diameter, 'm = ', area)
'''    

# 2) RELATIONAL
print(bin(5))





