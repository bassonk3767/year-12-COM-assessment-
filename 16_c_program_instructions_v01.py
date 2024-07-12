
# Gives the user instructions 
# on how they should use the calculator
def give_instructions():

    # Use hardcoded information
    # for the purpose of this program
    header = "Statistics Calculator instructions"

    # Create underline for the header
    header_underline = "^"*len(header)

    # Provide the steps to the program
    steps_of_program = ["[1]> Give the name of dataset, press <enter> when done with name\n",
                        "[2]> Enter 'ccc' to continue with the rest of the program\n",
                        "[3]> Provide data for the/each dataset with numbers and commas separating them\n",
                        "[4]> Select whether you want standard sample or population deviation"]
    
    # Create underline for the steps
    steps_underline = "^"*len(steps_of_program[2])

    # Explain the difference between 
    # standard sample and population deviation
    deviation_explanation = ["Sample deviation:     deviation of a sample\n",
                             "Population deviation: deviation of a population as a whole\n"
                             "                      assuming your data represents the population"]
    
    # Print out the instructions
    print(f"\n\n{header}")
    print(header_underline)
    print(f"\n\n{''.join(steps_of_program)}")
    print(steps_underline)
    print(f"\n{''.join(deviation_explanation)}")


# Example usage:

# Ask usewr if they would like 
# to read the instructions
while True:
    response = input("\n\n\nWould you like to "
                     "read the instructions?\n~~~ ")
    
    # Lower the casing of
    # The user's response
    response.lower()

    # Check if they said yes or now
    if response == "y" or response == "yes":
        give_instructions()
        break
    elif response == "n" or response == "no":
        break
    else:
        print("\n\nPlease enter with yes or no")