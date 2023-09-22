input_string = input("Enter a word:")
if (len(input_string)) > 10:
    print ("Long")
elif (len(input_string)) == 10:
    print ("OK")
else:  #(len(input_string)) < 10
    print ("Short")