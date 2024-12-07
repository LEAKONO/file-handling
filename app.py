def read_and_write_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.readlines()

        modified_content = [line.upper() for line in content]

        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"Modified content written to '{output_filename}' successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for file '{input_filename}' or '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

input_file = "input.txt"
output_file = "output.txt"
read_and_write_file(input_file, output_file)

def handle_file_reading():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

handle_file_reading()
