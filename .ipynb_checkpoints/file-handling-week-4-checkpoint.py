# File Read and Write Program

# Open the original file and read its content
with open("input.txt", "r") as file:
    content = file.read()

# Modify the content (example: convert to uppercase)
modified_content = content.upper()

# Write the modified content to a new file
with open("output.txt", "w") as file:
    file.write(modified_content)

print("File has been read and modified successfully!")
filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()

    # Modify content
    modified_content = content.upper()

    # Write to new file
    with open("modified_" + filename, "w") as new_file:
        new_file.write(modified_content)

    print("File processed successfully!")

except FileNotFoundError:
    print("Error: The file does not exist.")

except PermissionError:
    print("Error: You don't have permission to read this file.")

except Exception as e:
    print("An unexpected error occurred:", e)