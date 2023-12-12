##################################################
# Numerics
##################################################

'''
integers
'''

# intergers are presented internally using base-2 digits, not decimal

# if we use 32 bits to store
# one bit used to store the sign
# range is [- 2^(32-1), 2^(32-1) - 1]

# memory spaces (bytes) are limited by their address number - addresses themselves are limited to a 32 bit integer

# how large an integer can be depends on how many bits are used to store the number

# some languages like Java provide multiple distinct integer data types that use a fixed number of bits
# byte signed 8 bit number -128, 127
# short signed 16-bit numbers
# int signed 32-bit numbers
# long signed 64-bit numbers

# Python is different
# the int object uses a variable number of bits
# theoretically limited only by the amount of memory available

'''
integer operations
'''

# integers support all standard arithemetic operations
# int + int -> int
# int / int -> float


10 // 3 # floor division
10 % 3 # modulo operator
# always satisfy: n = d * (n // d) + (n % d)

# note floor and truncate are not the same thing, for negative numbers


'''
integer constructors and bases
'''
# an integer number is an object - an instance of the `int` class
# the int class provides multiple constructors
a = int(10)
a = int(-1.8) # -1, truncated

# booleans are integer types
a = int(True) # 1
a = int(False) # 0

# strings that can be pased to be a number
a = int("10")

# specify the base in the number
int("123") # 123 base 10 by default
int("1010", 2) # base 2 integer
int("A12F", 16) # base 16 number
int("ff", 16) # base 16, 16*15 + 15 = 255

# binary
bin(10) # '0b1010'
oct(10) # '0O12'
hex(10) # '0xa'

a = 0b1010 # a = 10
a = 0O12 # a = 10
a = 0xA # a = 10

'''
Fractions
'''
# rational numbers are fractions of integers

# any real number with a finite number of digits after the decimal point is also a rational number

# rational numbers can be represented using the Fracion class
from fractions import Fraction
x = Fraction(3, 4)
y = Fraction(22, 7)

# negative sign is always attached to the numerator
x = Fraction(1, -4) # turns to Fraction(-1, 4) 
x.numerator = -1
x.denominator = 4

# constructors
Fraction(numerator=0, denominator=1)
Fraction(float)
Fraction('10') # -> Fraction(10, 1)
Fraction('0.125') # -> Fraction(1, 8)
Fraction('22/7') # -> Fraction(22, 7)


# given a fraction number, find an approximate equivalent fraction with a constrained denominator
# using the limit_denominator(max_denominator=100000) method
x = Fraction(math.pi)
x.limit_denominator(10)


'''
Floats
'''
# float class is used as defaults for representing real numbers
# the float uses a fixed number of bytes
# - 8 bytes or 64 bits (CPython 64 bit)
# 64 bits are used up as follows:
# - sign (1 bit)
# - exponent (11 bits, range [-1022, 1023])
# - significant digits (52 bits, 15-17 significant base 10 digits. Significant digits are all digits except leading and trailing zeros
# any float can be written as a fraction

# some numbers with a finite decimal representation (like 0.1) do not have a finite binary representation
# (0.75)10 = (0.11)2
format(0.1, '.25f') # '0.1000000000000000055511151'

# foats - equality testing
# 0.1 can not be represented with a finite binary representations
a = 0.1 + 0.1 + 0.1
b = 0.3
a == b # false

# use an absolute tolerance - an appropriate range within which two numbers are deemed equal
# use a relative tolerance


# coercing floats to integers
# will incur data loss - for various ways
#  - truncation: ignores everything after the decimal point
#   - the int constructor will accept a float and uses truncation
#  - floor 
#   - the largest integer <= the number
#   - for positive numners, floor and truncation are equivalent
#   - a // b == floor(a / b)
#  - ceiling
#   - the ceiling of a number is the smallest integere >= the number
#  - rounding
#   - round(x, n=0) round the number x to the closets multile of 10^-n
#   - round(x) -> alwawys get an int back
#   - round(x, n) same type as x
#   - with ties, round away from 0, round(1.25, 1) -> 1.3, round(-1.25, 1) -> -1.3






'''
Decimals
'''
# representing numbers using decimals

import decimal
decimal.Decimal # more control over the precision



'''
complex numbers
'''

complex