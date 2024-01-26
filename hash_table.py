
array_1 = [1, 2, 3, 4, 5]
array_2 = [0, 2, 4, 6, 8]
string_array = ["a", "b", "c", "d", "c", "e", "f"]


def intersection(array1, array2):
    """Function to find intersection of 2 arrays"""
    hash_map = {}
    list_intersection = []
    for num in array1:
        hash_map[num] = True
    for num2 in array2:
        if num2 in hash_map:
            list_intersection.append(num2)
    return list_intersection


def duplicate_string(array):
    """"Function to find duplicate string in an array"""
    hash_map = {}
    for letter in array:
        if letter in hash_map:
            return letter
        else:
            hash_map[letter] = True
    return ""


d = duplicate_string(string_array)
print(d)
