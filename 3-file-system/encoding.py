##################################################
# String Encoding
##################################################

'''
Unicode Intro
'''
# https://pymotw.com/3/codecs/index.html
# https://docs.python.org/3/howto/unicode.html

# The Unicode standard describes how characters are represented by code points. A code point value is an integer in the range 0 to 0x10FFFF

# A Unicode string is a sequence of code points, which are numbers from 0 through 0x10FFFF (1,114,111 decimal). This sequence of code points needs to be represented in memory as a set of code units, and code units are then mapped to 8-bit bytes. The rules for translating a Unicode string into a sequence of bytes are called a character encoding, or just an encoding.


'''
utf-8
'''

# UTF-8 has several convenient properties:

# It can handle any Unicode code point.

# A Unicode string is turned into a sequence of bytes that contains embedded zero bytes only where they represent the null character (U+0000). This means that UTF-8 strings can be processed by C functions such as strcpy() and sent through protocols that can’t handle zero bytes for anything other than end-of-string markers.

# A string of ASCII text is also valid UTF-8 text.

# UTF-8 is fairly compact; the majority of commonly used characters can be represented with one or two bytes.

# If bytes are corrupted or lost, it’s possible to determine the start of the next UTF-8-encoded code point and resynchronize. It’s also unlikely that random 8-bit data will look like valid UTF-8.

# UTF-8 is a byte oriented encoding. The encoding specifies that each character is represented by a specific sequence of one or more bytes. This avoids the byte-ordering issues that can occur with integer and word oriented encodings, like UTF-16 and UTF-32, where the sequence of bytes varies depending on the hardware on which the string was encoded.




'''
Python encoding
'''

# CPython 3.x differentiates between text and byte strings. bytes instances use a sequence of 8-bit byte values. In contrast, str strings are managed internally as a sequence of Unicode code points. The code point values are saved as a sequence of 2 or 4 bytes each, depending on the options given when Python was compiled.

# When str values are output, they are encoded using one of several standard schemes so that the sequence of bytes can be reconstructed as the same string of text later. The bytes of the encoded value are not necessarily the same as the code point values, and the encoding defines a way to translate between the two sets of values. Reading Unicode data also requires knowing the encoding so that the incoming bytes can be converted to the internal representation used by the unicode class.

# The most common encodings for Western languages are UTF-8 and UTF-16, which use sequences of one and two byte values respectively to represent each code point. Other encodings can be more efficient for storing languages where most of the characters are represented by code points that do not fit into two bytes.


>>> text = 'français'
>>> text.encode('utf-8')
b'fran\xc3\xa7ais'
>>> import binascii
>>> binascii.hexlify(b'fran\xc3\xa7ais')
b'6672616ec3a7616973'


# The result of encoding a str is a bytes object.
# Given a sequence of encoded bytes as a bytes instance, the decode() method translates them to code points and returns the sequence as a str instance.
text = 'français'
encoded = text.encode('utf-8')
decoded = encoded.decode('utf-8')

'''
encoding / decoding error
'''

>>> b'\x80abc'.decode("utf-8", "strict")  
Traceback (most recent call last):
    ...
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 0:
  invalid start byte
>>> b'\x80abc'.decode("utf-8", "replace")
'\ufffdabc'
>>> b'\x80abc'.decode("utf-8", "backslashreplace")
'\\x80abc'
>>> b'\x80abc'.decode("utf-8", "ignore")
'abc'


##################################################
# base64 Encoding
##################################################

# https://pymotw.com/3/base64/index.html

# The base64 module contains functions for translating binary data into a subset of ASCII suitable for transmission using plaintext protocols.

import base64
import textwrap

with open(__file__, 'r', encoding='utf-8') as input:
	raw = input.read()
  	initial_data = raw.split('#end_pymotw_header')[1]

byte_string = initial_data.encode('utf-8')
encoded_data = base64.b64encode(byte_string)

# base64 decoding
encoded_data = b'VGhpcyBpcyB0aGUgZGF0YSwgaW4gdGhlIGNsZWFyLg=='
decoded_data = base64.b64decode(encoded_data)
print('Encoded :', encoded_data)
print('Decoded :', decoded_data)


