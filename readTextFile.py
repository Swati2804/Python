# Open the file in read mode
file_path = "example.txt"

try:
    with open(file_path, "r") as file:
        # Read the entire content of the file
        content = file.read()

        # Alternatively, you can read line by line using a for loop
        # lines = file.readlines()

        # Print the content of the file
        print(content)

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"Error occurred: {e}")
