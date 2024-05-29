
# Calculates the range of
# a provided data set,
# this can also be used
# for interquartile range ( IQR )
def find_range(data_set):
    # Return the last item subtracting the
    # first item in data set assuming that
    # the data set is already sorted
    return data_set[-1] - data_set[0]


# Example usage:

# Define data set
data_set = [1,5,5,12,17,11,11,6,4]

# First copy the data set
copy = data_set

# THen, order the data set
copy.sort()

# Find the range
r = find_range(copy)

# Print out the range
print(f"Range of {data_set}\nis: {r}")