################################################
# Regex
################################################

# Regular expressions are text matching patterns described with a formal syntax. The patterns are interpreted as a set of instructions, which are then executed with a string as input to produce a matching subset or modified version of the original.

# https://pymotw.com/3/re/index.html


'''
search
'''
# if match, return Match object with bunch of attributes
# if not, returns None

import re

pattern = 'this'
text = 'Does this text pattern match'
match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
    match.re.pattern, match.string, s, e, text[s:e]))

# Found "this"
# in "Does this text match the pattern?"
# from 5 to 9 ("this")


'''
compiling expressions
'''
# more efficient to compile expressions if use it frequently
# module level functions maintain a cache of compiled expressions, but the size of the cache is limited and using expressions directly avoids the overhead associated with cache lookup
import re

regexes = [
    re.compile(p)
    for p in ['this', 'that']
]
text = 'Does this text match the pattern'

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern),
          end=' ')
        
    if regex.search(text):
        print('Match')
    else:
        print('No match')

# Seeking "this" -> Match!
# Seeking "that" -> No match


'''
multiple matches
'''
# findall() function returns all of the substrings of the input that match the pattern without overlapping

import re
text = 'abbaaabbbbaaaaa'
pattern = 'ab'
for match in re.findall(pattern, text):
    print('Found {!r}'.format(match))

# The finditer() function returns an iterator that produces Match instances instead of the strings returned by findall().
for match in re.finditer(pattern, text):
    print('Found {!r} at {:d}:{:d}'.format(
        text[s:e], s, e))

'''
regex pattern syntax
'''
# repetition
'ab*' (a followed by zero or more b)

  'abbaabbba'
  'abb'
  ...'a'
  ....'abbb'
  ........'a'

'ab+' (a followed by one or more b)

  'abbaabbba'
  'abb'
  ....'abbb'

'ab?' (a followed by zero or one b)

  'abbaabbba'
  'ab'
  ...'a'
  ....'ab'
  ........'a'

'ab{3}' (a followed by three b)

  'abbaabbba'
  ....'abbb'

'ab{2,3}' (a followed by two to three b)

  'abbaabbba'
  'abb'
  ....'abbb'


# character sets
# a group of characters, any one of which can match at that point in the pattern

'[ab]' (either a or b)

  'abbaabbba'
  'a'
  .'b'
  ..'b'
  ...'a'
  ....'a'
  .....'b'
  ......'b'
  .......'b'
  ........'a'

'a[ab]+' (a followed by 1 or more a or b)

  'abbaabbba'
  'abbaabbba'

'a[ab]+?' (a followed by 1 or more a or b, not greedy)

  'abbaabbba'
  'ab'
  ...'aa'

# character ranges
'[a-z]+' (sequences of lowercase letters)
'[A-Z]+' (sequences of uppercase letters)
'[a-zA-Z]+' (sequences of letters of either case)
'[A-Z][a-z]+' (one uppercase followed by lowercase)


# escapte code

Code	Meaning
\d	a digit
\D	a non-digit
\s	whitespace (tab, space, newline, etc.)
\S	non-whitespace
\w	alphanumeric
\W	non-alphanumeric


'\d+' (sequence of digits)

  'A prime #1 example!'
  .........'1'

'\D+' (sequence of non-digits)

  'A prime #1 example!'
  'A prime #'
  ..........' example!'

'\w+' (alphanumeric characters)

  'A prime #1 example!'
  'A'
  ..'prime'
  .........'1'
  ...........'example'

# anchoring
# the relative location can be specified in the input text where the pattern should appear by using anchoring instructions
^ start of the string, or line
$ end of string, or line


# groups

'a(ab)' (a followed by literal ab)

  'abbaaabbbbaaaaa'
  ....'aab'

'a(a*b*)' (a followed by 0-n a and 0-n b)

  'abbaaabbbbaaaaa'
  'abb'
  ...'aaabbbb'
  ..........'aaaaa'

'a(ab)*' (a followed by 0-n ab)

  'abbaaabbbbaaaaa'
  'a'
  ...'a'
  ....'aab'
  ..........'a'
  ...........'a'
  ............'a'
  .............'a'
  ..............'a'

'a(ab)+' (a followed by 1-n ab)

  'abbaaabbbbaaaaa'
  ....'aab'


'''
search options
'''

# case insensitive matching

pattern = r'\bT\w+'
with_case = re.compile(pattern)
without_case = re.compile(pattern, re.IGNORECASE)

    

'''
Modifying String with Patterns
'''

# sub 
# Use sub() to replace all occurrences of a pattern with another string.

bold = re.compile(r'\*{2}(.*?)\*{2}')
text = 'Make this **bold**.  This **too**.'

print('Text:', text)
# References to the text matched by the pattern can be inserted using the \num syntax used for back-references.
print('Bold:', bold.sub(r'<b>\1</b>', text))

# Text: Make this **bold**.  This **too**.
# Bold: Make this <b>bold</b>.  This <b>too</b>.

# limit the number of substitutions performed
print('Bold:', bold.sub(r'<b>\1</b>', text, count=1))


# split
# returns a list
# Two or more newline characters mark a separator point between paragraphs in the input string.
text = '''Paragraph one
on two lines.

Paragraph two.


Paragraph three.'''
for num, para in enumerate(re.split(r'\n{2,}', text)):
    print(num, repr(para))
    print()

# 0 'Paragraph one\non two lines.'

# 1 'Paragraph two.'

# 2 'Paragraph three.'


