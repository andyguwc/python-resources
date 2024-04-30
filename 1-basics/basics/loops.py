

##################################################
# Loops 
##################################################
# for loop
for name in ['a','b','c']:
    print(name)

# accumulator pattern
nums = [1,2,3,4]
res = 0
for w in nums:
    res = res + w 
print(res)

# traversal
for counter, item in enumerate(['a','b','c']):
    print(counter, item)

for n in range(len(fruit)):
    print(n, fruit[n])

# enumeration
# return an iterable. using for loop then index, value
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

for i, item in enumerate(my_items):
    print(f'{i}:{item}')



# while loop
def sumTo(aBound):
    """ Return the sum of 1+2+3 ... n """
    theSum  = 0
    aNumber = 1
    while aNumber <= aBound:
        theSum = theSum + aNumber
        aNumber = aNumber + 1
    return theSum

# break and continue
while True:
    print("this phrase will always print")
    break
    print("Does this phrase print?")

print("We are done with the while loop.")

# continue is the other keyword that can control the flow of iteration. Using continue allows the program to immediately “continue” with the next iteration. 
# The program will skip the rest of the iteration, recheck the condition, and maybe does another iteration depending on the condition set for the while loop.

for name in student_names:
    if name == "mark":
        print('found him'+name)
        break
    print("currently testing "+name)

for name in student_names:
    if name == "bort":
        continue # continue to the next iteration
        print("found him"+name)
    print("currently testing"+name)


# two approach to break out of the loop if found item
#  - return early 
def coprime(a, b):
    for i in range(2, min(a,b)+1):
        if a % i == 0 and  b % i == 0:
            return False 
    return True 

#  - have a result variable indicating if found and break out of the loop if found
def coprime2(a, b):
    is_coprime = True
    for i in range(2, min(a,b)+1):
        if a % i == 0 and b % i == 0:
            is_coprime = False 
            break 
    return is_coprime 

