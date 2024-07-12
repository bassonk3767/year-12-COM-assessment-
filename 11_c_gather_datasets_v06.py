
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
                         "\n\n~~~ ")

        # Lower the case of the response
        lower_cased = response.lower()

        # Check if the name of the data set
        # contains any special conditions, or
        # if the name is given as blank
        if lower_cased == "ccc" and len(data_sets) > 0:
            return data_sets
        elif lower_cased == "ccc" and len(data_sets) == 0:
            print("\n\n\nPlease enter a name before attempting"
                  " to\nproceed with the program")
        elif response == "":
            print("\n\n\nPlease enter a name that is not blank")
        elif response == "xxx":
            return 0
        else:
            
            # Check if user enters 
            # the same name twice
            if response in data_sets:
                # Add name to array, but
                # add a number ID next to the 
                # name to indicate it's new 
                
                # Create the dataset ID
                id = str("".join(data_sets).count(response)+1)

                # Add the new name of dataset to the array
                data_sets.append(response+" "+id)
            else:
                # append the name to the
                # # array of data sets
                data_sets.append(response)


# Example usage:

# Collect name(s) of
# data sets and print
# the array to the console
print(gather_datasets())