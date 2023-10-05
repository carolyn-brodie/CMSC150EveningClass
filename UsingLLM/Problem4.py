def integer_counter(divisor1,divisor2):
    """Write a function that takes two integer
    parameters and returns how many three-digit
    numbers (100 – 999) are divisible by both of them

    """
    count = 0
    for number in range(100,1000):
        if number % divisor1 == 0 and number % divisor2 == 0:
            count += 1
    return count

def main():
    print(integer_counter(2,3), 150)
    print(integer_counter(3,5), 60)
    print(integer_counter(7,3), 43)

if __name__ == "__main__":
    main()

