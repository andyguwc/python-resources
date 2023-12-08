##################################################
# Loop
##################################################

'''
while loop
'''
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)

min_length = 2

while True:
    name = input("Please enter a name: ")
    if len(name) >= min_length and name.isprintable() and name.isalpha():
        break


l = [1,2,3,4]
found = False
idx = 0

while idx < len(l):
    if l[idx] == 3:
        found = True
        break
    idx += 1

'''
for loop
'''