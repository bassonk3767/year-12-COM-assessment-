
# Calculates the range of
# a provided data set,
# this can also be used
# for inter-quartile range ( IQR )
def find_range(data_set):

    # First, sort the data set
    # from minimum to maximum
    ordered = sorted(data_set)

    return ordered[-1] - ordered[0]


# Example usage:

# Define data set
data_set = [1,5,5,12,17,11,11,6,4]

# Find the range
r = find_range(data_set)
