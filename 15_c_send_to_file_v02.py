
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


# Example usage: (without table)

# Define the data that needs to
# be sent to the file
data_to_send = "Hello, world!!"

# Send data
send_to_file("Test.txt",data_to_send)
