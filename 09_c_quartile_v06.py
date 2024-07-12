# Import...

import statistics as stcs

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


# Calculates the lower/upper
# quartile of a given data set,
# similar to the range function
def find_lower_quartile(data_set):

    # First, order the data set
    # from lowest to greatest
    data_set.sort()

    # Second, find the median
    # of the data set
    median = stcs.median(data_set)

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
    lower_quartile = stcs.median(to_median)

    return lower_quartile


# A function that calculates
# the upper quartile of a
# given data set
def find_upper_quartile(data_set):

    # Find the median
    # of the data set
    median = stcs.median(data_set)

    # Create an array that starts from
    # the median to the last piece of data
    med_to_last = data_set[data_set.index(median):-1]

    # Find the upper quartile
    upper_quartile = stcs.median(med_to_last)

    return upper_quartile

# Example usage:

# Define data set
data_set = [1,5,5,12,17,11,11,6,4]

# Sort the data
data_set.sort()

# Calculate the lower and upper quartile
lower_quartile = find_lower_quartile(data_set)
upper_quartile = find_upper_quartile(data_set)

# Print out the lower and
# upper quartile
print(f"\n\n\nLower quartile of {data_set}\nis: {lower_quartile}")
print(f"\n\nUpper quartile of {data_set}\nis: {upper_quartile}")