
# Functions..

# Calculates the range of
# a provided data set,
# this can also be used
# for interquartile range ( IQR )
def find_range(data_set):

    # Return the last item subtracting the
    # first item in data set assuming that
    # the data set is already sorted
    return data_set[-1] - data_set[0]


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


# A function that calculates
# the upper quartile of a
# given data set
def find_upper_quartile(data_set):
    pass


# Example usage:

# Define data set
data_set = [1,5,5,12,17,11,11,6,4]

# Calculate the lower quartile
lower_quartile = find_lower_quartile(data_set)

print(f"Lower quartile of {data_set}\nis: {lower_quartile}")