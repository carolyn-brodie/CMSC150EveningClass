
def is_even(number):
    """Write a function that takes a number as a parameter
    and returns True if the number is even, False if not"""

    if number % 2 == 0:
        return True
    else:
        return False

def create_even_lst(lst):
    """A function that takes a list of integers as a formal parameter and returns
    a list containing only the even numbers from the input list.  """
    even_lst = []
    for number in lst:
        if is_even(number):
            even_lst.append(number)
    return even_lst

def main():
   print(create_even_lst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
   print(create_even_lst([1, 3, 7]))
   print(create_even_lst([ ]))
   print(create_even_lst([4,8,10]))

if __name__ == "__main__":
    main()