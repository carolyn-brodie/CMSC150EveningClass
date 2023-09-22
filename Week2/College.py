

# 3.	Write a program that asks the user
# what college they are attending and prints out a strong
# congratulations if it's Simpson, a strong condemnation if it's
# Central, a mild congratulations if it's Drake or Coe, and a neutral ' \

#'message if it's any other college.

college = input("What college do you attend: ")

if college == "Simpson":
    print("Congratulations")
elif college == "Central":
    print("Boo")
elif college == "Drake" or college == "Coe":
    print("That's ok")
else:
    print("ok")
major = input("Enter your major")

