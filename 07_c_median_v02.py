
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


# Example usage:

# Define data set
data_set = [1,5,5,12,17,11,11,6,4]

# Calculate the median
median = find_median(data_set)

# Print out the median
print(f"\n\nMedian of {data_set}"
      f"\nis: {median}")