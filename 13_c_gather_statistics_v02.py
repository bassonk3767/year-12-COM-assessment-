# Calculates the mean
# of a data set / sample
def find_mean(data_set):
    result = sum(data_set)

    return result / len(data_set)


# Calculates the summation
# of each data point in a sample
def find_sum(data_set, mean):
    result = 0

    for x in data_set:
        result += (x - mean) ** 2

    return result


# calculates the median
# of the provided data set
def find_median(data_set):

    # Initialize rough value as the
    # beginning of the calculation
    # ( the index for the median )
    index = float(len(data_set)) / 2

    # Put index into a string in
    # order to determine if it
    # should be rounded
    index_to_str = f"{index}"

    # Check if index has a ".5" present
    if ".5" in index_to_str:

        # If so, subtract
        # ".5" and add 1
        index -= 0.5
        index += 1

    # Convert index into
    # an integer
    index = int(index)

    # Return the median
    # using the processed
    # index from calculation
    return data_set[index-1]


# Calculates the range of
# a provided data set,
# this can also be used
# for interquartile range ( IQR )
def find_range(data_set):
    # Return the last item subtracting the
    # first item in data set assuming that
    # the data set is already sorted
    return data_set[-1] - data_set[0]


# Calculates the lower/upper
# quartile of a given data set,
# similar to the range function
def find_lower_quartile(data_set):

    # First, order the data set
    # from lowest to greatest
    data_set.sort()

    # Second, find the median
    # of the data set
    median = find_median(data_set)

    # Initialize the array that stores
    # the data that leads up to the
    # median of the data set
    to_median = []

    # Initialize a counter used
    # for correctly locating the
    # median of the data set
    j = 0

    # Loop to get the new array
    # of the data that leads up
    # to the median of the data set
    for i in data_set:
        j += 1

        if j != data_set.index(median) + 1:
            to_median.append(i)
        else:
            to_median.append(i)
            break

    # Calculate the lower
    # quartile as a
    # rough calculation first
    lower_quartile = find_median(to_median)

    return lower_quartile


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
            print("\n\n\nPlease enter a name before attempting"
                  " to\nproceed with the program")

        elif response == "xxx":
            return 0
        else:

            # append the name to  the
            # array of data sets
            data_sets.append(response)


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

        return 0


# Calculates and creates an array of
# summaries on the data given by the user
def gather_statistics(data_sets):

    # Initialize the array
    # used for the file export
    # function with the string
    # version of the calculations
    data_summaries = []

    # If user did not exit the program,
    # continue with gathering data
    # for each data set
    if data_sets != 0:

        # An iterator used for correctly
        # assigning valid data
        i = 0

        while True:
            data = input("\n\n\nPlease enter the data of\n the "
                         "'{data_sets[i]}' dataset\n(ie 1,2,3,4)\n\n~~~ ")

            converted_data = create_dataset(data)

            # If fhe data is valid, increment
            # the iterator variable by 1
            if converted_data != 0:
                i += 1

    # If the given data sets are
    # assigned with 0, return 0
    else:
        return 0


# Example usage:

# Get names of data set(s)
data_sets = gather_datasets()

# Calculate data summaries
gather_statistics(data_sets)