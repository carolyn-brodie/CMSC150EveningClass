

def isLessThan(num, numList):
    """Write function that takes one number and a
    list of numbers as parameters.  The function
    should return True if ANY of the numbers in the
    list are less than or equal to the number.
    103       [27, 76, 101, 98] should return True
    100       [127, 176, 101, 198]  should return False
    580      [250, 580, 300]        should return True """

    for i in numList:
        if i <= num:
            return True
    return False

def main():
    print(isLessThan(103, [27, 76, 101, 98]), True)
    print(isLessThan(100, [127, 176, 101, 198]), False)
    print(isLessThan(580, [250, 580, 300]), True)

if __name__ == "__main__":
    main()


