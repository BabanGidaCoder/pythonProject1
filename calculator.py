import os

""" The program below is a simple calculator application that asks a user to enter two numbers
and the operation, that they'd like to perform on the numbers. It uses defensive programming to write this 
program that is robust and catches unexpected events and user inputs  """


def calculate(num1, num2, operator):
    """
    Function taking the two numbers and operations

    """

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        raise ValueError("Invalid operator entered. Only +, -, * are allowed.")


def write_to_file(eq_str, result):
    """
    Code to write results to calculations.txt file
    """
    if not os.path.exists("calculations.txt"):
        with open("calculations.txt", "w") as file:
            file.write("Equation, Result\n")
    with open("calculations.txt", "a") as file:
        file.write(f"{eq_str}, {result}\n")


while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Oops! You have not entered a valid number, Try again...")
        operator = input("Enter the operator (+, -, *): ")
        result = calculate(num1, num2, operator)
        print(f"The answer is: {result}")
        eq_str = f"{num1} {operator} {num2} = {result}"
        write_to_file(eq_str, result)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print("An unexpected error occurred. Please try again later.")
