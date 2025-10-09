import argparse

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-dataType", choices=["long", "line", "word"])
args = parser.parse_args()
calculation_flag = args.dataType if args.dataType else "word"
data = []


def get_input(input_type):
    while True:
        try:
            if input_type == "long":
                for num in input().split():
                    data.append(int(num))
            elif input_type == "word":
                for word in input().split():
                    data.append(word)
            else:
                for line in input().splitlines():
                    data.append(line)
        except EOFError:
            break


if calculation_flag == "long":
    get_input("long")
elif calculation_flag == "word":
    get_input("word")
else:
    get_input("line")

print(data)
# Calculations
total = len(data)
greatest = max(data) if calculation_flag == "long" else max(data, key=len)
greatest_occurrences = data.count(greatest)

# Result presentation
topic = "numbers" if calculation_flag == "long" else "lines" if calculation_flag == "line" else "words"
top = "greatest number" if calculation_flag == "long" else "longest line" if calculation_flag == "line"\
    else "longest word"
result_string = f"""Total {topic}: {total}.
The {top}: {greatest} ({greatest_occurrences} time(s))."""

print(result_string)
