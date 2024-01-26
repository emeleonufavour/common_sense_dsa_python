

def countdown(n):
    """Countdown from n recursively"""
    if n == 0:
        return

    print(n)
    countdown(n - 1)


def count_x(array):
    """This function finds all the x that occurs in an array"""
    if len(array) == 1:
        if array[0] == "x":
            return 1
        else:
            return 0

    if array[0] == "x":
        return 1 + count_x(array[1:])
    else:
        return count_x(array[1:])


def factorial(n):
    """Calculate a factorial recursively"""
    if n == 1:
        return 1
    return n * factorial(n-1)


def print_every_other(low, high):
    """Print numbers from low to high in 2 steps"""
    if low > high:
        return
    if low <= high:
        print(low)
        print_every_other(low=low + 2, high=high)


dummy_array = [1, 2, 3,
               [4, 5, 6],
               7,
               [8,
                [9, 10, 11,
                 [12, 13, 14]
                 ]],
               [15, 16, 17, 18, 19,
                [20, 21, 22,
                 [23, 24, 25,
                  [26, 27, 29]
                  ], 30, 31], 32
                ], 33]

xs = list("xbxcxd")


def print_elements_array(your_array):
    """Print all numbers in array"""
    for i in your_array:
        if isinstance(i, list):
            print_elements_array(i)
        else:
            print(i)


counts = count_x(xs)
print(f"Counts ==> {counts}")
