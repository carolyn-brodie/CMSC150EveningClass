#Create a list
list1 = [4, 9, 12, 15, 11]
# Create accumulator variable
sum = 0
#loop through the list
for number in list1:
    if number % 3 == 0:
        sum += number
print(sum)


# if number divisible by 3 then add it to accumulator
# at end of list print sum