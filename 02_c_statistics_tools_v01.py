# This function is used for calculating
# the factorial of the number of items
# in an array. (strings, integers, etc)
def factorial_arr(data):

    # Get the number of items
    # found within array
    length = len(data)

    # Initialize result as 0
    result = 0

    # Performing a for loop in order to
    # compute the factorial value
    for i in range(0, length):
        if length > 1:
            if result == 0:
                result = length*(length-1)
            else:
                result = result*(length-1)
        length -= 1

    return result


# This function is used for calculating
# the factorial of a single integer value
def factorial_int(num):

    # Get the number of items
    # found within array
    length = num

    result = 0

    for i in range(0, length):
        if length > 1:
            if result == 0:
                result = length*(length-1)
            else:
                result = result*(length-1)
        length -= 1

    return result


def factorial_text(text):
    words = text.split(" ")
    return factorial_arr(words)


i = input("Press button?\n~~~ ")

if i.lower() != "no":
    print("\n\nInitiating nuclear warheads")
    print()
    print()
    print()
    print("ACTIVATED: NORTH KOREA MOCK 17~11Y")
    print("ACTIVATED: PAKISTAN 9847KY ")
    print("ACTIVATED: UNN 22W1&")
else:
    print("\n\nOk...")