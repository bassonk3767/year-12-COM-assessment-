# Imports...
import pandas as pd
import math as ma

# Functions...

# Calculates the range of
# a provided data set,
# this can also be used
# for interquartile range ( IQR )
def find_range(data_set):

    # First, sort the data set
    # from minimum to maximum
    ordered = sorted(data_set)

    return ordered[-1] - ordered[0]


# Calculates the summation
# of each data point in a sample
def find_sum(data_set, mean):
    result = 0

    for x in data_set:
        result += (x - mean) ** 2

    return result


# Calculates the mean
# of a data set / sample
def find_mean(data_set):
    result = sum(data_set)

    return result / len(data_set)


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


# Calculates the standard deviation
# for a sample of a population
def standard_sample_deviation(data_set):

    # Acquire the length of the
    # provided data set
    length = len(data_set)

    # calculate the mean
    mean = find_mean(data_set)

    # Convert the mean into a string
    # for conditional checking
    mean_to_str = f"{mean}"

    # Assign variable type accordingly
    if float(mean) and mean_to_str[-2 | -1] == "0":
        mean = int(mean)
    else:
        mean = round(mean, 2)

    summation = calculate_sum(data_set, mean)

    # Calculate the standard deviation
    deviation = ma.sqrt(summation / (length - 1))

    # Return deviation
    # rounded to 2dp
    return round(deviation, 2)


# Main routine...
