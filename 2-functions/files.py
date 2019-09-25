##################################################
#  Files
##################################################
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
# context manager
with open('mydata.txt', 'r') as mydata:
    for line in mydata:
        print(line)

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

# writing files to a csv file
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

