# program below reads the content of the input file performs operations on it and outputs it to output file based on
# min max and ave.

with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
    for line in input_file:
        operation, numbers = line.strip().split(":")   # split into operations and numbers

        numbers = list(map(int, numbers.split(",")))   # converts numbers into integers

        if operation == "min":
            result = min(numbers)
            output_file.write(f"The Min of : {numbers} is  {result}. \n")

        elif operation == "max":
            result = max(numbers)
            output_file.write(f"The Max of : {numbers} is {result}. \n")

        elif operation == "avg":
            def average(numbers):
                return sum(numbers) / len(numbers)
            avg = average(numbers)
            result = avg
            output_file.write(f"The Average of: {numbers} is {result}. \n")
