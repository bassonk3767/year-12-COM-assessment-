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
        data_set = [int(num) for num in rough_data]

        # Return the data set
        return data_set

    # If the given data set
    # does not contain an
    # integer, ask the user
    # to enter the data again
    except ValueError:
        print("\n\nPlease enter a valid dataset "
              "that consists of integers and comas")


# Collects the data
# specified by the user
def collect_data():
    data_sets = []

    # Loop to retrieve data
    while True:
        response = input("\n\n\nPlease enter the "
                         "name of the dataset\n"
                         "(exit with xxx, continue program with ccc)"
                         "\n\n~~~ ")

        response.lower()

        if response == "ccc" and len(data_sets) > 0:
            return data_sets
        elif response == "ccc" and len(calculations) == 0:
            print("\n\n\nPlease enter a dataset before attempting"
                  " to\nproceed with the program")

        elif response == "xxx":
            return 0
        else:

            # Create a data set
            # with the given data
            data_set = create_dataset(response)

            # Push the data set to the
            # array of data sets
            data_sets.append(data_set)


print(collect_data())