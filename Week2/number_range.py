# Ask the user for an integer
# convert to an int
# if test <= 50
# else if test > 50 and less than 100
# else case of 100 or greater

number = int(input("Enter a number: "))
if number <= 50:
    print("Small numbers")
elif number < 100:
    print("In the middle ")
#elif number >= 100:
else:
    print("Big number")

