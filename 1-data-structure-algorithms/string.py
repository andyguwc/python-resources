##################################################
# Strings and Text
##################################################


'''
String Operations
'''
# Count and Index
a = "I have had an apple on my desk before!"
print(a.count("e"))

z = ['atoms', 4, 'neutron', 6, 'proton', 4, 'electron', 4, 'electron', 'atoms']
print(z.count("4"))

# split
song = "this is a song"
wds = song.split()
print(wds)

# join
wds = ["red", "blue", "green"]
glue = ';'
s = glue.join(wds)
print(s)

ss = "Hello, World"
els = ss.count("l")

'''
Encoding
'''

# ascii
# serialize data as ascii

# ord() converts a character to an integer unicode 
# chr() converts an integer unicode into a single character string

# unicode 
# If you are encoding text and don't know which encoding to use, it is best to use
# the UTF-8 encoding. UTF-8 is able to represent any Unicode character. In modern
# software, it is a de facto standard encoding to ensure documents in any language—or
# even multiple languages—can be exchanged.

characters = "cliché"
print(characters.encode("UTF-8"))
print(characters.encode("ascii"))


'''
Regular Expressions (regex)
'''
# matching patterns 

# regular expressions
import re
search_string = "hello world"
pattern = "hello world"
match = re.match(pattern, search_string)
if match:
	print("regex matches")

import re
pattern = sys.argv[1]
search_string = sys.argv[2]
match = re.match(pattern, search_string)
if match:
	template = "'{}' matches pattern '{}'"
else:
	template = "'{}' does not match pattern '{}'"
print(template.format(search_string, pattern))

. # any character as long as not empty
'hel o world' matches pattern 'hel.o world'
'helo world' does not match pattern 'hel.o world'

[] # a set of characters as long as matches one of them
'hello world' matches pattern 'hel[lp]o world'
'hello 2 world' matches pattern 'hello [a-zA-Z0-9] world'

* # the previous character zero or many times
'heo' matches pattern 'hel*o'
'helllllo' matches pattern 'hel*o' # can be zero or more times 

# \. matches . escaping 

# repeat sequence of patterns
'abcabcabc' matches pattern '(abc){3}'

'abccc' matches pattern 'abc{3}'

# get information from it
# re.search
# re.findall

# making repeated regular expressions efficient
re.compile 

# specify multiple patterns for the separator 
# use the re.split() method 
line = 'asdf fjdk; afed, fjek,asdf, foo'

import re
re.split(r'[;,\s]\s*', line)

# matching test 
str.startswith()
str.endswith()
filename = 'spam.txt'
filename.endswith('.txt')

# Normally, fnmatch() matches patterns using the same case-sensitivity rules as the system’s underlying filesystem
import os 
filenames = os.listdir('.')
filenames
[name for name in filenames if name.endswith(('.c','.h'))]
[name for name in names if fnmatch(name, 'Dat*.csv')]

# replacing text 
text = 'yeah, but not, yeah'
text.replace('yeah', 'yep')

# for more complicated patterns, use the sub() function
# The first argument to sub() is the pattern to match and the second argument is the replacement pattern. 
# Backslashed digits such as \3 refer to capture group numbers in the pattern.
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

# strip chracters from strings 
s = ' hello world \n'
s.strip()
# >>> t = '-----hello====='
# >>> t.lstrip('-')
# 'hello====='
# >>> t.strip('-=')
# 'hello'

text = 'Hello World'
format(text, '=>20s')
# '=========Hello World'
format(text, '*^20s')
# '****Hello World*****'

# combining and concatenating string 
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
' '.join(parts)

a = 'Is Chicago'
b = 'Not Chicago?'
print('{} {}'.format(a,b))  
# Is Chicago Not Chicago?

','.join(str(d) for d in data)
print(a, b, c, sep=':')


'''
format (interpolating values in strings)
'''

# format
s = '{name} has {n} messages'
s.format(name='Hello', n=37)

name = 'Guido'
n = 37
'%(name) has %(n) messages.' % vars()

# container lookup 
# we can access complex objects (indexes, variables of arrays, lists, etc.) from the format string
emails = ("a@example.com", "b@example.com")
message = {
    'subject': "You Have Mail!",
    'message': "Here's some mail for you!"
}
template = """
From: <{0[0]}>
To: <{0[1]}>
Subject: {message[subject]}
{message[message]}"""
print(template.format(emails, message=message))
# so 0[0] maps to emails[0], in the emails tuple

# object lookup
# We can pass arbitrary objects as parameters, and use the dot notation to look up attributes on those objects.
class EMail:
    def __init__(self, from_addr, to_addr, subject, message):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self.message = message
email = EMail("a@example.com", "b@example.com",
"You Have Mail!",
"Here's some mail for you!")

template = """
From: <{0.from_addr}>
To: <{0.to_addr}>
Subject: {0.subject}
{0.message}"""
print(template.format(email))

'{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii')

x = 1.23456
format(x, '0.2f')
format(x, '0.3f')
'value is {:0.3f}'.format(x)


print("Sub: ${0:0.2f} Tax: ${1:0.2f} "
      "Total: ${total:0.2f}".format(subtotal, tax, total=total))


def greet(name, question):
    return f"Hello {name}! How is {question}"


# use Template Strings to avoid user injected data 


'''
byte strings
'''
# byte strings support most of the operations for regular strings 
data = b'Hello World'
data[0:5]
data.startwith(b'Hello')

data = b'FOO:BAR,SPAM'
re.split(b'[:,]',data) # pattern as bytes





'''
datetime
'''
from datetime improt timedelta 
a = timedelta(days=2, hours=6)