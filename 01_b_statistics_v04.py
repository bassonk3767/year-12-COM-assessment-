# imports...

# Import pandas for creating
# tables for data summaries
import pandas as pd

# Import math for standard
# deviation calculation
import math as ma

# Functions...

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


# A function that calculates
# the upper quartile of a
# given data set
def find_upper_quartile(data_set):

    # Find the median
    # of the data set
    median = find_median(data_set)

    # Create an array that starts from
    # the median to the last piece of data
    med_to_last = data_set[data_set.index(median):-1]

    # Find the upper quartile
    upper_quartile = find_median(med_to_last)

    return upper_quartile


# Calculates the standard deviation
# for a sample of a population
def standard_sample_deviation(data_set):

    # Sort the data set from
    # lowest to greatest
    data_set.sort()

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

    summation = find_sum(data_set, mean)

    # Calculate the standard deviation
    deviation = ma.sqrt(summation / (length - 1))

    # Return deviation
    # rounded to 2dp
    return round(deviation, 2)


# Calculates the standard deviation
# for a entire population
def standard_population_deviation(data_set):

    # Sort the data set from
    # lowest to greatest
    data_set.sort()

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

    summation = find_sum(data_set, mean)

    # Calculate the standard deviation
    deviation = ma.sqrt(summation / length)

    # Return deviation
    # rounded to 2dp
    return round(deviation,2)


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
        lower_cased = response.lower()

        # Check if the name of the data set
        # contains any special conditions, or
        # if the name is given as blank
        if lower_cased == "ccc" and len(data_sets) > 0:
            return data_sets
        elif lower_cased == "ccc" and len(data_sets) == 0:
            print("\n\n\nPlease enter a name before attempting"
                  " to\nproceed with the program")
        elif response == "":
            print("\n\n\nPlease enter a name that is not blank")
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


# Calculates and creates an array of
# summaries on the data given by the user
def gather_statistics(data_sets):

    # Initialize the array
    # used for the data sent to
    # the file export function
    un_sorted = []

    # If user did not exit the program,
    # continue with gathering data
    # for each data set
    if data_sets != 0:

        # An iterator used for correctly
        # assigning valid data
        i = 0

        while i < len(data_sets):
            data = input("\n\n\nPlease enter the data of\n the "
                         f"'{data_sets[i]}' dataset\n(ie 1,2,3,4)\n\n~~~ ")

            converted_data = create_dataset(data)

            # If fhe data is valid, increment
            # the iterator variable by 1
            if converted_data != 0:
                i += 1

                # Order the data from
                # minimum to maximum
                converted_data.sort()

                # Define the options
                options_arr = [1, 2]

                # Enter loop
                while True:

                    # A try block used for
                    # detecting strings being
                    # entered by the user
                    try:

                        # print options and get response
                        response = int(input("\n\nWould you like to calculate:\n"
                                             "[standard sample deviation]> 1, "
                                             "[standard population deviation]> 2"
                                             "\n\n~~~ "))

                        # Check if input is valid
                        if valid_integer(response, options_arr):
                            # Check what type of deviation
                            # was chosen for a data set
                           if response == 1:
                                deviation = standard_sample_deviation(converted_data)
                                break
                           else:
                                deviation = standard_population_deviation(converted_data)
                                break
                        else:
                             print("\n\nPlease select an option by number"
                                   " that is pressent in the options")

                    # If an unexpected value is entered,
                    # return an error to the user
                    except ValueError:
                        print("\n\nPlease select an option that"
                              " isn't in the form of text")

                # Get statistics
                mean = find_mean(converted_data)

                # Convert the mean into a string
                # for conditional checking
                mean_to_str = f"{mean}"

                if float(mean) and mean_to_str[-2 | -1] == "0":
                   mean = int(mean)
                else:
                    mean = round(mean, 2)

                median = find_median(converted_data)
                minimum = converted_data[0]
                maximum = converted_data[-1]
                range = find_range(converted_data)
                lower_quartile = find_lower_quartile(converted_data)
                upper_quartile = find_upper_quartile(converted_data)
                interquartile_range = upper_quartile-lower_quartile

                # Define the unsorted array of
                # statistics that can be used for
                # the table creation
                # (sorts statistics, Sub array in larger array)
                un_sorted_sub = [mean, median, minimum,
                                 maximum, range, lower_quartile,
                                 upper_quartile, interquartile_range,
                                 deviation]

                # Add the sub array to the
                # unsorted array
                un_sorted.append(un_sorted_sub)

        # Create the data frame
        table = create_table(data_sets,un_sorted)

        # Return the table
        # for file output
        return table

    # If the given data sets are
    # assigned with 0, return 0
    else:
         return 0


# Sends data frames to a file
def send_to_file(filename,data):

    # Open the selected file
    f = open(filename,"a")

    # Send th table to
    # the selected file
    # With visual formatting
    f.write(f"\n\n{data}\n\n")

    # Then, close the file
    f.close()


# Main routine...

# Get names of data set(s)
data_sets = gather_datasets()

# Calculate data summaries
table = gather_statistics(data_sets)

# Print out the table
print(table)

# Send the table to the file
send_to_file("Data_summary.txt",table)