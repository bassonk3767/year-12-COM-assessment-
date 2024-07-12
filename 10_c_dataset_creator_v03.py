# Creates an array with the
# data given by the user as
# a string data type
def create_dataset(response):

    # A try block for checking
    # if the user has entered
    # a valid data set (as string)
    try:

        # Initialize an array
        # for storing each value
        # from the given set
        # (rough collection)
        rough_data = response.split(",")

        # Create the data set
        # by looping through
        # the rough data set
        data_set = [float(num) for num in rough_data]

        # Return the data set
        return data_set

    # If the given data set
    # does not contain an
    # integer, ask the user
    # to enter the data again
    except ValueError:
        print("\n\nPlease enter a valid dataset "
              "that consists of integers and comas")


# Example usage

# Get data set from the user
response = input("\n\n\nPlease enter a dataset "
             "(ie 1,2,3,4)\n~~~ ")

data_set =  create_dataset(response)

print(f"\n\n\nDataset: {data_set}")