# importing math library
# for square-root function
import math as ma


# Functions...

# Calculates the summation
# of each data point in a sample
def calculate_sum(data_set, mean):
    result = 0

    for x in data_set:
        result += (x - mean) ** 2

    return result


# Calculates the mean
# of a data set / sample
def find_mean(data_set):
    result = sum(data_set)

    return result / len(data_set)


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


# Calculates the standard deviation
# for a entire population
def standard_population_deviation(data_set):
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
    deviation = ma.sqrt(summation / length)

    # Return deviation
    # rounded to 2dp
    return round(deviation,2)


# Example usage:

# Define data set
data_set = [1,5,5,12,17,11,11,6,4]

# calculate deviations
sample_deviation = standard_sample_deviation(data_set)
population_deviation = standard_population_deviation(data_set)

# Print deviations
print(f"\n\nStandard sample deviation: {sample_deviation}")
print(f"Standard population deviation: {population_deviation}")