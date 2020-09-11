##################################################
# Conditionals
##################################################
# conditionals
# if 
# elif 
# else 

# in and not in operators
print('p' in 'apple')
print(9 in [3,6,9]) # use the in and not in operators on lists

x =15
if x%2 == 0:
    print(x, "is even")
else:
    print(x, "is odd")

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y must be equal")

# accumulator pattern with conditionals
# initialize, iterate over, update step
phrase = "hello world"
tot = 0
for char in phrase:
    if char != " ":
        tot = tot+1
print(tot)

# string format
origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${} discounted by {}% is ${}.'.format(origPrice, discount, newPrice)
print(calculation)


