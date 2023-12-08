##################################################
# New Lines
##################################################
# Physical new line vs. logical newline
# physical lines of code end with a physical newline character
# logocal lines end with a logical NEWLINE token
# physical newlines are ignored in order to combine multiple physical lines into a single logical line of code terminated by a logical NEWLINE token

'''
implicit
'''
# implicit support of multi-lines
# [], (), {} literals
[
    1, # inline comment
    2,
    3
]
# function arguments and parameters

'''
explicit
'''
# break up statements over multiple lines explicitly, using the \ backslash character
if "a" \
    and "b" \
    and "c":
    pass


##################################################
# Multi-line String Literals
##################################################

# Multi-line string literals can be created using triple delimiters ('' or "")
# It is the same as the regular string
'''a multiline
string
'''

# to be unindented in the display

def my_func():
    a = """a multi-line string
that is indented into the second line
    """
    return a 

print(my_func())
