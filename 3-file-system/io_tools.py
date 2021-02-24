##################################################
# I/O tools
##################################################

'''
In-memory Streams with StringIO
'''
# working with text in memory using read, write (file API)
# in memory stream buffers are useful for testing

import io

# writing to a buffer
output = io.StringIO()
output.write('This goes into the buffer')
print('And this', file=output)

# retrive value written
print(output.getvalue())

output.close() # discard buffer memory


# Initialize a read buffer
input = io.StringIO('Inital value for read buffer')

# Read from the buffer
print(input.read())


'''
Raw Bytes with BytesIO
'''

# writing to a buffer

output = io.BytesIO()
output.write('This goes into the buffer.'.encode('utf-8'))
output.write('ÁÇÊ'.encode('utf-8'))


