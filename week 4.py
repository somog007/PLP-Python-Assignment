def modify_content(content):
    """Example modification function - you can customize this"""
    # Convert to uppercase as an example modification
    return content.upper()

def modify_content(content):
    # Add your own modification logic here
    # Example: Reverse each line
    return '\n'.join([line[::-1] for line in content.split('\n')])

def main():
    print("File Modifier Program")
    print("---------------------")
    
    # Get input filename from user
    while True:
        input_filename = input("Enter the name of the file to read: ")
        try:
            # Try to open and read the file
            with open(input_filename, 'r') as file:
                content = file.read()
            break  # Exit loop if file was successfully read
        except FileNotFoundError:
            print(f"Error: The file '{input_filename}' does not exist.")
        except PermissionError:
            print(f"Error: Permission denied when trying to read '{input_filename}'.")
        except IOError as e:
            print(f"Error: Unable to read file '{input_filename}'. {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
    
    # Modify the content
    modified_content = modify_content(content)
    
    # Get output filename from user
    while True:
        output_filename = input("Enter the name for the new modified file: ")
        if output_filename.strip() == "":
            print("Error: Output filename cannot be empty.")
            continue
        if output_filename == input_filename:
            print("Error: Output filename cannot be the same as input filename.")
            continue
        
        try:
            # Try to write to the new file
            with open(output_filename, 'w') as file:
                file.write(modified_content)
            print(f"Success! Modified content written to '{output_filename}'")
            break
        except PermissionError:
            print(f"Error: Permission denied when trying to write to '{output_filename}'.")
        except IOError as e:
            print(f"Error: Unable to write to file '{output_filename}'. {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
