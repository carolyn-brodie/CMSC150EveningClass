
score = int(input("What is your total score? "))
if score > 90:
    print("Your grade is A")
    print("Good for you")
elif score > 80:
    print("Your grade is a B")
    print("You missed an A by", 100 - score)
elif score > 70:
    print("Your grade is a C")
else:
    print("Better luck next time")

print("Going on")


