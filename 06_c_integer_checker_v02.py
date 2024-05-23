
# Checks if a user enters one of the provided options
# represented as integers given in an array
# as the second argument for the function
#
# (e.g. [1,2,3,4] gives 4 options)
def valid_integer(response, options_arr):

    # Check if input exists in array
    if response in options_arr:

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

# Array for options chosen
options_chosen_arr = ["\n\nYou have chosen standard sample deviation...",
                      "\n\nYou have chosen standard population deviation..."]

# Enter loop
while True:

    # A try block used for
    # detecting strings being
    # entered by the user

    try:

        # print options
        response = int(input("\n\nWould you like to calculate:\n"
                             "[standard sample deviation]> 1, "
                             "[standard population deviation]> 2"
                             "\n\n~~~ "))

        # Check if input is valid
        if valid_integer(response,options_arr):
            print(options_chosen_arr[response-1])
        else:
            print("\n\nPlease select an option by number"
                  " that is pressent in the options")

    except ValueError:
        print("\n\nPlease select an option that"
              " isn't in the form of text")