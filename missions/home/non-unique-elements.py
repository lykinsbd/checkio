#!/usr/bin/env python3

# Your optional code here
# You can import some modules or create additional functions


def checkio(data):
    # Your code here
    # It's main function. Don't remove this function
    # It's used for auto-testing and must return a result for check.

    """
    Evaluate a given list to find/return only non-unique items

    :param data:
    :return non-unique-items:
    """
    # Iterate the list, add to new list if count is > 2
    new_data = []
    for i in data:
        if data.count(i) >= 2:
            new_data.append(i)
    print(new_data)
    # quit()
    return new_data


# Some hints
# You can use list.count(element) method for counting.
# Create new list with non-unique elements
# Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
