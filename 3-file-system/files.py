##################################################
# File System
##################################################


'''
os.path
'''
# https://pymotw.com/3/file_access.html

# platform independent manipulation of filenames

os.curdir # the path component that refers to the current directory
os.sep # separator between portions of the path
os.split # the split function breaks the path into two separate paths and returns a tuple with the results. The second element of the tuple is the last component of the path

# split
# split based on directory separator
import os.path
path = '/one/two/three'
print(os.path.split(path))
# ('/one/two', 'three')

# basename
print(os.path.basename(path))

# splitext
# splitext() works like split(), but divides the path on the extension separator, rather than the directory separator.

path = '/path/to/filename.txt'
os.path.splitext(path)
# ('/path/to/filename', '.txt')

# join 
# build paths

parts = ['/', 'one', 'two']
os.path.join(*parts)
# '/one/two

parts = ['one', 'two']
os.path.join(*parts)
# 'one/two'

# expanduser
# convert ~ to the home directory
os.path.expanduser('~/')
# '/Users/username/'

# cleanup with normpath
path = 'one//two//.three'
os.path.normpath(path)
# 'one/two/.three'

# testing files
file = './broken_link'
os.path,isfile(file)
os.path.isdir(file)
os.path.exists(file)



'''
io
'''
# The io module provides access to the classes used to implement Python’s file-based input and output. For testing code that depends on reading or writing data from files, io provides an in-memory stream object that behaves like a file, but does not reside on disk.



'''
pathlib
'''
# https://pymotw.com/3/pathlib/index.html

# The pathlib module provides an object-oriented API for working with file system paths. Using it instead of os.path provides some conveniences because it operates at a higher level of abstraction.

# pathlib includes classes for managing filesystem paths formatted using either the POSIX standard or Microsoft Windows syntax. It includes so called “pure” classes, which operate on strings but do not interact with an actual filesystem, and “concrete” classes, which extend the API to include operations that reflect or modify data on the local filesystem.
import pathlib
usr = pathlib.PurePosixPath('usr')
usr_local = usr / 'local'
print(usr_local) # 'usr/local'

# resolve path
usr_local = pathlib.Path('/usr/local')
share = usr_local / '..' / 'share'
print(share.resolve()) # /usr/share

# parsing paths
p = pathlib.PurePosixPath('/usr/local')
print(p.parts)
# ('/', 'usr', 'local')


# directory contents
# iterdir() is a generator, yielding a new Path instance for each item in the containing directory

p = pathlib.Path('.')
for f in p.iterdir():
    print(f)

# using glob to find only files mathcing a pattern
import pathlib

p = pathlib.Path('..')

for f in p.glob('*.rst'):
    print(f)


# file properties

import pathlib
import sys

if len(sys.argv) == 1:
    filename = __file__
else:
    filename = sys.argv[1]

p = pathlib.Path(filename)
stat_info = p.stat()

# information regarding owner of a file
# use owner() and group()



'''
glob
'''
# https://pymotw.com/3/glob/index.html
# Build a list of filenames from a pattern
# To create a list of filenames that all have a certain extension, prefix, or any common string in the middle, use glob instead of writing custom code to scan the directory contents.

# * matches zero or more characters in a segment of a name
import glob
for name in sorted(glob.glob('dir/*')):
    print(name)

# matches any single character in that position in the name
for name in sorted(glob.glob('dir/file?.txt')):
    print(name)


# character ranges
# Use a character range ([a-z]) instead of a question mark to match one of several characters. This example finds all of the files with a digit in the name before the extension.

import glob
for name in sorted(glob.glob('dir/*[0-9].*')):
    print(name)


'''
fnmatch
'''
# compares a singal filename against a pattern and return a boolean, indicating whether or not they match

import fnmatch
import os

pattern = 'fn_*.py'
files = os.listdir('.')
for name in sorted(files):
    print(fnmatch.fnmatch(name, pattern))


# filter for list of files matching pattern
fnmatch.filter(files, pattern)



'''
tempfile
'''
# https://pymotw.com/3/tempfile/index.html

# tempfile is useful for cases that need to create scratch files to hold data temporarily, or before moving it to a permanent location. It provides classes to create temporary files and directories safely and securely. Names are guaranteed to be unique, and include random components so they are not easily guessable.

# Applications that need temporary files to store data, without needing to share that file with other programs, should use the TemporaryFile() function to create the files. The function creates a file, and on platforms where it is possible, unlinks it immediately. This makes it impossible for another program to find or open the file, since there is no reference to it in the file system table. The file created by TemporaryFile() is removed automatically when it is closed, whether by calling close() or by using the context manager API and with statement.

import tempfile

# without using tempfile
filename = 'tmp/somefile.txt'
with open(filename, 'w+b') as temp:
    print(temp)
    print(temp.name)
os.remove(filename)

# using tempfile
with tempfile.TemporaryFile() as temp:
    temp.write(b'Some data')
    temp.seek(0)
    print(temp.read())

# After writing, the file handle must be “rewound” using seek() in order to read the data back from it.

# NamedTemporaryFile
# There are situations where having a named temporary file is important. For applications spanning multiple processes, or even hosts, naming the file is the simplest way to pass it between parts of the application.
with tempfile.NamedTemporaryFile() as temp:
    print(temp.name)
    f = pathlib.Path(temp.name)

print(f.exists())


'''
shutil
'''
# The shutil module includes high-level file operations such as copying and archiving.

# copy file
# copyfile() copies the contents of the source to the destination and raises IOError if it does not have permission to write to the destination file.

import shutil
shutil.copyfile('source_file.py', 'source_copy.py')


# copy fileobj
# arguments to copyfileobj are open file handles
import io

input_str = '''some test string'''
input = io.StringIO(input_str)

output = io.StringIO()
shutil.copyfileobj(input, output)

print(output.getvalue())

buf = StringIO()
with open ('file.xml', 'w') as fd:
    buf.seek(0)
    shutil.copyfileobj (buf, fd)

# copy 
# interprets the output name like the Unix command line tool cp. If the named destination refers to a directory instead of a file, a new file is created in the directory using the base name of the source

os.mkdir('example')
shutil.copy('shutil_copy.py', 'example')
print(glob.glob('example/*'))


# copy directory trees
# copytree to copy a directory from one place to another

import glob
import pprint
import shutil

pprint.pprint(glob.glob('/tmp/example/*'))

shutil.copytree('../shutil', '/tmp/example')

pprint.pprint(glob.glob('/tmp/example/*'))

# move 
# semantics similar to the Unix command mv - if the source and destinations are within the same file system, the source is renamed. Otherwise source is copied to the destination and source is removed
# To move a file or directory from one place to another, use move().

with open('example.txt', 'wt') as f:
    f.write('contents')

shutil.move('example.txt', 'example.out')



# zip file
# make_archive to create a new archive
# Its inputs are designed to best support archiving an entire directory and all of its contents, recursively. By default it uses the current working directory, so that all of the files and subdirectories appear at the top level of the archive. 

import shutil
import tarfile

# use root_dir to move to a new relative position, and base_dir to specify a directory to add to the archive

shutil.make_archive(
    'example', 'gztar',
    root_dir='..',
    base_dir='shutil',
    logger=logger,
)

# print out file names
with tarfile.open('example.tar.gz', 'r') as t:
    for n in t.getnames():
        print(n)



##############################################
# Working with Data Files
##############################################

open(filename,'r')	# Open a file called filename and use it for reading. This will return a reference to a file object.
open(filename,'w')	# Open a file called filename and use it for writing. This will also return a reference to a file object.
filevariable.close() # File use is complete.

# File Reading Methods
write filevar.write(astring)	# Add astring to the end of the file. filevar must refer to a file that has been opened for writing.
read(n)	filevar.read()	# Reads and returns a string of n characters, or the entire file as a single string if n is not provided.
readline(n)	filevar.readline()	# Returns the next line of the file with all text up to and including the newline character. If n is provided as a parameter than only n characters will be returned if the line is longer than n. Note the parameter n is not supported in the browser version of Python, and in fact is rarely used in practice, you can safely ignore it.
readlines(n) filevar.readlines()	# Returns a list of strings, each representing a single line of the file. If n is not provided then all lines of the file are returned. If n is provided then n characters are read but n is rounded up so that an entire line is returned. Note Like readline readlines ignores the parameter n in the browser.


# Open New Lines
olypmicsfile = open("olypmics.txt","r")

for aline in olypmicsfile.readlines():
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olypmicsfile.close()

# Find the files 
# If your file and your Python program are in the same directory you can simply use the filename.
open('data1.txt','r')

# If your file and your Python program are in different directories, however, then you need to specify a path. 
open('../myData/data2.txt','r')

open('/Users/joebob01/myFiles/allProjects/myData/data2.txt','r')


# Using With for Files
# Context manager, equivalent to just having ...close() at the end
with open('mydata.txt', 'r') as md:
    for line in md:
        print(line)
# continue on with other code



# Reading Text Files 
fname = "yourfile.txt"
with open(fname, 'r') as fileref:         # step 1
    lines = fileref.readlines()           # step 2
    for lin in lines:                     # step 3
        #some code that references the variable lin
#some other code not relying on fileref   # step 4


filename = "squared_numbers.txt"
outfile = open(filename, "w")

for number in range(1, 13):
    square = number * number
    outfile.write(str(square) + "\n")

outfile.close()

infile = open(filename, "r")
print(infile.read()[:10])


# Read from CSV

fileconnection = open("olympics.txt", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    vals = row.strip().split(',')
    if vals[5] != "NA":
        print("{}: {}; {}".format(
                vals[0],
                vals[4],
                vals[5]))


olympians = [("John Aalberg", 31, "Cross Country Skiing"),
            ("Minna Maarit Aalto", 30, "Sailing"),
            ("Win Valdemar Aaltonen", 54, "Art Competitions"),
            ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv","w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()



##################################################
#  Files
##################################################

'''
read / write basics
'''

# Open a file called filename and use it for reading. This will return a reference to a file object.
# open(filename,'r')

# Open a file called filename and use it for writing. This will also return a reference to a file object.
# open(filename,'w')

# iterating over lines in a file 
# for line in myFile.readlines():

olympicsfile = open("olympics.txt", "r")
for aline in olympicsfile.readlines():
    # or just use the simpler for aline in olymicsfile
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])
olympicsfile.close()

# using with for files 
# context manager with ensures closing file automatically 
# iterate over the lines 
with open('mydata.txt', 'r') as mydata:
    for line in mydata:
        print(line)

# use rt for text file 
# read the entire file as a single string
with open('somefile.txt', 'rt') as f:
    data = f.read()

# write chunks of text data 
with open('somefile.txt', 'wt') as f:
    f.write(text)

# mode 'at'
# to append at the end of an existing file use open with mode at 

# mode 'xt
# write data to file only if it doesn't already exist on the filesystem

# writing out files 
filename = "squared_numbers.txt"
outfile = open(filename, "w")

for number in range(1,13):
    square = number * number
    outfile.write(str(square)+"\n")
outfile.close()

infile = open(filename,"r")
print(infile.read()[:10])
infile.close()


'''
read / write binary data
'''
# read entire file as a single byte string
with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

# write binary data to a file 
# make sure to supply data as byte strings/arrays
with open('somefile.bin', 'wb') as f:
    text = 'hello world'
    f.write(text.encode('utf-8'))
    # f.write(b'hello world')



'''
printing to file 
'''
# redirect the output of the print() function to a file 
with open('somefile.txt', 'rt') as f:
    print('Hello world', file=f)


'''
serializing python objects
'''
# pickle.load() should never be used on untrusted data. As a side effect
# of loading, pickle will automatically load modules and make instances.

import pickle 

some_data = ["a list", "containing"]
# dump serializes data to a file 
with open("pickled_list", 'wb') as file:
    pickle.dump(some_data, file)

# load reads a serialized object from a file-like object 
with open("pickled_list", 'rb') as file:
    loaded_data = pickle.load(file)
print(loaded_data)
assert loaded_data == some_data

# restore from a string
data = pickle.loads(s)


##################################################
#  CSV 
##################################################

'''
reading
'''
# https://pymotw.com/3/csv/index.html
import csv
import sys

# As it is read, each row of the input data is parsed and converted to a list of strings.

with open('3-file-system/test.csv', 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        # each row is a list
        print(row)

# print headers
# using namedtuple 
import csv 
with open('sample_data.csv') as f: 
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # process row 
        
# read in data from a csv file 
fileconnection = open("olympics.txt", "r")
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    vals = row.strip().split(',')
    if vals[5] != "NA":
        print("{}:{};{}", format(
            vals[0],
            vals[4],
            vals[5]
        ))

# using namedtuple 
from collections import namedtuple
with open('sample_data.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        # process row 

# read in as a sequence of dictionaries with DictReader
# rows are returned as OrderedDict instances instead of lists or tuples
import csv 
with open('sample_data.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row)

'''
writing 
'''
# writing files to a csv file
# csv does not try to interpret the data or convert it to a type other than a string.
olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]
outfile = open("reduced_olympics.csv", "w")
outfile.write('Name,Age, Sport')
outfile.write('\n')
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    # row_string = ','.join(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()


# using csv.writer

import csv
import sys

with open(sys.argv[1], 'wt') as f:
    writer = csv.writer(f)
    writer.writerow(('Title 1', 'Title 2', 'Title 3', 'Title 4'))
    for i in range(3):
        row = (
            i + 1,
            chr(ord('a') + i),
            '08/{:02d}/07'.format(i + 1),
            unicode_chars[i],
        )
        writer.writerow(row)

print(open(sys.argv[1], 'rt').read())


# Steps to create a CSV writer:
# 1. Open a file with the newline option set to "". This will support the (possibly)
# nonstandard line ending for CSV files.
# 2. Create a CSV writer object. In this example, we created the DictWriter
# instance because it allows us to easily create rows from dictionary objects.
# 3. Put a header in the first line of the file. This makes data exchange slightly
# simpler by providing some hint as to what's in the CSV file.

# Once writer object has been prepared, we can use the writer's writerow() method
# to write each dictionary to the CSV file. We can, to an extent, simplify this slightly
# by using the writerows() method.

# write a series of object to file
with open("blackjack.stats","w",newline="") as target:
writer= csv.DictWriter( target, GameStat._fields )
writer.writeheader()
for gamestat in gamestat_iter( Player_Strategy_1, Martingale_Bet):
    writer.writerow(gamestat._asdict())


# convert from csv to object
with open("blackjack.stats","r",newline="") as source:
    reader= csv.DictReader( source )
    for gs in ( GameStat(**r) for r in reader ):
        print( gs )

with open("blackjack.stats","r",newline="") as source:
    reader= csv.DictReader( source )
    assert set(reader.fieldnames) == set(GameStat._fields)
    for gs in gamestat_iter(reader):
        print( gs )




##################################################
#  JSON
##################################################

import json 

# turn python data structure into JSON string
data = {
    'name': 'ABC',
    'shares': 100,
    'price': 99
}

json_str = json.dumps(data)

# >>> json.dumps(False)
# 'false'
# >>> d = {'a': True,
# ... 'b': 'Hello',
# ... 'c': None}
# >>> json.dumps(d)
# '{"b": "Hello", "c": null, "a": true}'


# turn a JSON-encoded string back into a Python data structure
data = json.loads(json_str)

# if working with files instead of strings, use the dump() and load()
# writing json data 
with open('data.json', 'w') as f:
    json.dump(data, f)
# reading data back 
with open('data.json', 'r') as f:
    data = json.load(f)

# pretty print using pprint module 
from urllib.request import urlopen
import json
u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
resp = json.loads(u.read().decode('utf-8'))
from pprint import pprint
pprint(resp)

# json deocding typically creates dicts or lists from the supplied data.
# if you want different objects, supply the object_pairs_hook to json.loads()
s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
# OrderedDict([('name', 'ACME'), ('shares', 50), ('price', 490.1)])


'''
compressed datafiles
'''
# read / write data in a file with gzip or bz2 compression 

# gzip compression
import gzip
with gzip.open('somefile.gz','rt') as f:
    text = f.read()

