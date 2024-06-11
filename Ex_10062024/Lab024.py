# Task 1
# Explain difference between = & ==
# Explain use of ** operator & how it is used
# What does ^ operator does & in what context it is commonly used

# = is used to assign value on the right hand side to the variable on left hand side
# == is used to compare two values if both are equal or not, it returns Boolean

age = 50
print(age)
age2 = 49
c = (age == age2)
print(c)
################################################

# ** is used to take power of no. on left hand side with the no. on right hand side
value = 3**3
print(value)
value1 = 10**2
print(value1)
################################################

# ^ is an EXOR operator used in mostly binary system, It follow truth table of EXOR gate
a = 0b1010
b = 0b0101
c = a^b
print(bin(c))
x = 0b110
y = 0b010
z = x^y
print(bin(z))
p = 10
q = 4
r = p^q
print(r)