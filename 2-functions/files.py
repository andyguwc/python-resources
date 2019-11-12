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
#  CSV Data 
##################################################

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

# read in data as a sequence of tuples 
import csv 
with open('sample_data.csv') as f: 
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # process row 

# using namedtuple 
from collections import namedtuple
with open('sample_data.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        # process row 

# read in as a sequence of dictionaries 
import csv 
with open('sample_data.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        # process row  

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



##################################################
#  Path / Directory 
##################################################

'''
encoding 
'''
# replace bad characters
f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
r.read()

# printing with a different separator or line ending 
print('ACME', 50, 91.5, sep=',', end='!!\n')
# ACME,50,91.5!!


'''
compressed datafiles
'''
# read / write data in a file with gzip or bz2 compression 

# gzip compression
import gzip
with gzip.open('somefile.gz','rt') as f:
    text = f.read()


'''
paths and directories 
'''
# maniulate path names 
# Get the last component of the path
os.path.basename(path)

# Get the directory name
os.path.dirname(path)

# Join path components together
os.path.join('tmp', 'data', os.path.basename(path))

# testing for the existence of a file 
import os 
os.path.exists('/etc/passwd')

# is a regular file 
os.path.isfile('/etc/passwd')

# directory listing 
# raw directory listing including all files, subdirectories, etc.
import os 
names = os.listdir('somedir')

import os.path 
# get all regular files 
names = [name for name in os.listdir('somedir')
         if os.path.isfile(os.path.join('somedir', name))]
# Get all dirs
dirnames = [name for name in os.listdir('somedir')
            if os.path.isdir(os.path.join('somedir', name))]
# filter for specific file types 
pyfiles = [name for name in os.listdir('somedir')
if name.endswith('.py')]



