import argparse

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-dataType", choices=["long", "line", "word"])
args = parser.parse_args()
calculation_flag = args.dataType if args.dataType else "word"


def long_calculations():
    while True:
        try:
            for num in input().split():
                data.append(int(num))
        except EOFError:
            break


# Input gathering
data = []
if calculation_flag == "long":
    long_calculations()
else:
    print("TBD")

# Calculations
total_numbers = len(data)
greatest_number = max(data)
greatest_number_occurrences = data.count(greatest_number)

# Result presentation
result_string = f"""Total numbers: {total_numbers}.
The greatest number: {greatest_number} ({greatest_number_occurrences} time(s))."""

print(result_string)
