# Read and write Challenge
def modify_file(input_file):
    try:
        # Automatically generate the output file name (you can customize this)
        output_file = "output.txt"

        # Open and read the input file
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{output_file}' successfully.")
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found. Please check the file path and try again.")
    except IOError:
        print(f"Error: The file '{input_file}' could not be read. Please check the file and permissions.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Error handling lab
# Asks the user for the input file path and ensures the file exists and can be read
def get_input_file():
    while True:
        input_file_path = input("Enter the input file path: ")

        # Checks if the file exists and is readable
        try:
            with open(input_file_path, 'r'):
                break  # If File exists and can be read, exit the loop
        except FileNotFoundError:
            print(f"Error: File '{input_file_path}' not found. Please try again.")
        except IOError:
            print(f"Error: The file '{input_file_path}' could not be read. Please check the file and permissions.")
    
    return input_file_path

# Gets the input file from the user
input_file_path = get_input_file()

# Call the function with the valid input file path
modify_file(input_file_path)
