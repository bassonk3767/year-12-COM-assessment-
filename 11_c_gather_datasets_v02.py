
# Collects the data
# specified by the user
def gather_datasets():

    # Initialize the array of
    # names used to define the
    # names for each data set
    data_sets = []

    # Loop to retrieve data
    while True:

        # Get the name of the data set
        response = input("\n\n\nPlease enter the "
                         "name of the dataset\n"
                         "(exit with xxx, continue program with ccc)"
                         "\n\n~~~ ")

        # Lower the case of the response
        response.lower()

        # Check if the name of the data set
        # contains any special conditions
        if response == "ccc" and len(data_sets) > 0:
            return data_sets
        elif response == "ccc" and len(dat_sets) == 0:
            print("\n\n\nPlease enter a dataset before attempting"
                  " to\nproceed with the program")

        elif response == "xxx":
            return 0
        else:

            # append the name to  the
            # array of data sets
            data_sets.append(response)


# Example usage:

# Collect name(s) of
# data sets and print
# the array to the console
print(gather_datasets())