# Import pandas for creating
# the table for the statistics output
import pandas as pd


# Creates a table for
# the file output
def create_table(names,un_sorted):

    # Initialize the dictionary
    data_summary_dict = {}

    # Initialize the iterator used
    # for retrieving data
    j = 0

    # loop through the names to get
    # each piece of data for data sets
    for i in names:

        data_summary_dict[i] = un_sorted[j]
        j += 1

    # Define the indexes
    # of the table
    indexes = ["Mean (Average)","Median",
               "Minimum value","Maximum value",
               "Range","Lower quartile",
               "Upper quartile","Interquartile range",
               "Standard deviation"]

    # Create the data frame
    df = pd.DataFrame(data_summary_dict, index=indexes, columns=data_summary_dict.keys())

    # Return the data frame
    return df


# Example usage:

# Define the name of each group
names = ["Group A Stats","Group B Stats"]
un_sorted = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
             [1, 2, 3, 4, 5, 6, 7, 8, 9]]

table = create_table(names,un_sorted)

print(table)