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


# Example usage:

# Define data set
data_set = [1,5,5,12,17,11,11,6,4]

mean = find_mean(data_set)

# Convert the mean into a string
# for conditional checking
mean_to_str = f"{mean}"

if float(mean) and mean_to_str[-2|-1] == "0":
    mean = int(mean)
else:
    mean = round(mean,2)


result = calculate_sum(data_set, mean)

print(result)
c