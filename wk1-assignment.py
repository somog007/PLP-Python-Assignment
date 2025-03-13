def main():
    """
    Main function to handle user input, calculation, and output.
    """
    while True:  # Start an infinite loop to allow multiple calculations
        try:
            num1 = float(input("Enter the first number (or 'q' to quit): "))  # Get the first number from the user, convert to float
            num2 = float(input("Enter the second number: "))  # Get the second number from the user, convert to float
            operation = input("Enter the operation (+, -, *, /): ")  # Get the operation from the user

            result = calculate(num1, num2, operation)  # Call the calculate function to perform the operation

            if isinstance(result, str):  # Check if the result is a string (error message)
                print(result)  # Print the error message
            else:
                print(f"Here is your result {num1} {operation} {num2} = {result}")  # Print the calculation result

        except ValueError:  # Handle the case where the user enters non-numeric input
            user_input = input("Invalid input. Enter 'q' to quit or any other key to retry: ") #prompt the user to either quit or retry.
            if user_input.lower() == 'q': # If the user enters 'q' (case-insensitive)
                break  # Exit the loop and end the program
            else:
                continue # go to the beginning of the while loop

        except KeyboardInterrupt:  # Handle the case where the user presses Ctrl+C
            print("\nCalculation interrupted by user.")  # Print a message indicating interruption
            break  # Exit the loop and end the program

        except Exception as e:  # Handle any other unexpected errors
            print(f"An unexpected error occurred: {e}") #Print the error message.
            break #exit the loop.

def calculate(num1, num2, operation):
    """
    Function to perform the calculation based on the given operation.
    """
    if operation == '+':  # Check if the operation is addition
        return num1 + num2  # Return the sum of the two numbers
    elif operation == '-':  # Check if the operation is subtraction
        return num1 - num2  # Return the difference of the two numbers
    elif operation == '*':  # Check if the operation is multiplication
        return num1 * num2  # Return the product of the two numbers
    elif operation == '/':  # Check if the operation is division
        if num2 == 0:  # Check if the second number is zero
            return "Error: Division by zero not allowed."  # Return an error message
        return num1 / num2  # Return the quotient of the two numbers
    else:  # If the operation is not recognized
        return "Error: Invalid operation. Please use +, -, *, or /."  # Return an error message

if __name__ == "__main__":
    main()  # Call the main function to start the program
