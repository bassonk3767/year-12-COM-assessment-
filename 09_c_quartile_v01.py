
# Functions..

# Calculates the range of
# a provided data set,
# this can also be used
# for interquartile range ( IQR )
def find_range(data_set):

    # First, sort the data set
    # from minimum to maximum
    ordered = sorted(data_set)

    return ordered[-1] - ordered[0]


# Calculates the lower/upper
# quartile of a given data set,
# similar to the range function
def find_quartile(data_set):

    # First, find the median
    # of the data set
    pass

