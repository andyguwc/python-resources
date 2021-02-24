##################################################
# gzip
##################################################

'''
writing compressed data
'''

# https://pymotw.com/3/gzip/index.html

# gzip.open creates an instance of the file like GzipFile. 

# To write data into a compressed file, open the file with mode 'wb'. This example wraps the GzipFile with a TextIOWrapper from the io module to encode Unicode text to bytes suitable for compression.

import gzip
import io

outfilename = 'example.txt.gz'

with gzip.open(outfilename, 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.write('Contents of the example file go here.\n')

print(outfilename, 'contains', os.stat(outfilename).st_size, 'bytes')
os.system('file -b --mime {}'.format(outfilename))


# Also includes writelines()
import gzip
import io
import itertools
import os

with gzip.open('example_lines.txt.gz', 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.writelines(itertools.repeat('The same line, over and over.\n',10))
        
os.system('gzcat example_lines.txt.gz')


'''
reading compressed data
'''
# read data back from compressed file, open the file with binary read mode ('rb) so no text-based translation of line / unicode encoding is performed

import gzip
import io

with gzip.open('example.txt.gz', 'rb') as input_file:
    # using TextIOWrapper to decode the text after it is decompressed
    with io.TextIOWrapper(input_file, encoding='utf-8') as dec:
        print(dec.read())


##################################################
# tarfile
##################################################

'''
read tar files
'''
# https://pymotw.com/3/tarfile/index.html
# read/write access to Unix tar archives, including compressed files
import tarfile

for filename in ['README.txt', 'example.tar']:
    try:
        print('{:15} {}'.format(filename, tarfile.is_tarfile(filename)))
    except IOError as err:
        print('{:>15}  {}'.format(filename, err))


# read the names of files in an existing archive
import tarfile
with tarfile.open('example.tar', 'r') as t:
    print(t.getnames())


# metadata about the archive members
import tarfile
import time

with tarfile.open('example.tar', 'r') as t:
    for member_info in t.getmembers():
        print(member_info.name)
        print(member_info.type)


'''
extracting files from an archive
'''

import tarfile

with tarfile.open('example.tar', 'r') as t:
    for filename in ['README.txt', 'here.txt']:
        try:
            f = t.extractfile(filename)
        except KeyError:
            print('Error: did not find {} in tar archive'.format(filename))
        else:
            print(filename, ':')
            print(f.read().decode('utf-8'))

# To unpack the archive and write the files to the file syste,. use extract() or extractall()
import tarfile
import os

os.mkdir('outdir')
with tarfile.open('example.tar', 'r') as t:
    t.extract('README.txt', 'outdir')
print(os.listdir('outdir'))



'''
create archives
'''

import tarfile

with tarfile.open('tarfile_add.tar', mode='w') as out:
    print('adding README.txt')
    out.add('README.txt')
    # using a different name
    info = out.gettarinfo('README.txt', arcname='RENAMED.txt')
    out.addinfo(info)


##################################################
# zipfile
##################################################

# https://pymotw.com/3/zipfile/index.html

'''
read zipfile
'''

# is_zipfile indicates whether the filename is a valid zip file
import zipfile

for filename in ['example.zip', 'example.txt']:
    print('{:>15} {}').format(filename, zipfile.is_zipfile(filename))

# reading metadata from an Archive
import zipfile

with zipfile.ZipFile('example.zip', 'r') as zf:
    print(zf.namelist())

# get metadata 
with zipfile.ZipFile('example.zip') as zf:
    for filename in ['READEME.txt', 'nothere.txt']:
        try:
            info = zf.getinfo(filename)
        except KeyError:
            print('Error: did not find {} in zip file'.format(filename))
        else:
            print('{} is {} bytes'.format(info.filename, info.file_size))


'''
write zipfile
'''
import zipfile

with zipfile.ZipFile('example.zip') as zf:
    for filename in ['Filename.txt']:
        try:
            data = zf.read(filename)
        except KeyError:
            print('Did not find {}'.format(filename))
        else:
            print(data)
        print()


# appending to data
with zipfile.ZipFile('file.zip', mode='a') as zf:
    zf.write('README.txt')



