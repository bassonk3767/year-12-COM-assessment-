
# Checks if a user enters one of the provided options
# represented as integers given in an array
# as the second argument for the function
#
# (e.g. [1,2,3,4] gives 4 options)
def integer_checker(input, options_arr):

    # Check if input exists in array
    if input in options_arr:

        # Return true to signify
        # that the user has
        # entered valid option
        return True
    else:

        # Else, return false
        # to signify an
        # invalid option
        return False

# Example usage:

# Define the options
options_arr = [1,2]

# print options
print("\n\nWoyld you like to calculate:\n"
      "[standard sample deviation]> 1, "
      "[standard population deviation]> 2"
      "\n\n~~~ ")