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

# binary
bin(10) # '0b1010'
oct(10) # '0O12'
hex(10) # '0xa'

a = 0b1010 # a = 10
a = 0O12 # a = 10
a = 0xA # a = 10

'''
rational numbers
'''
# fractions of integers
# fractions.Fraction


'''
real numbers
'''
import decimal
float
decimal.Decimal # more control over the precision


'''
complex numbers
'''

complex