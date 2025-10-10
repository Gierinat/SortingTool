import argparse

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-dataType", choices=["long", "line", "word"], default="word")
args = parser.parse_args()
calculation_flag = args.dataType
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

# Calculations
total = len(data)
greatest = max(data) if calculation_flag == "long" else max(data, key=len)
greatest_occurrences = data.count(greatest)
percentage_occurrence = int(greatest_occurrences / total * 100)

# Result presentation
topic = "numbers" if calculation_flag == "long" else "lines" if calculation_flag == "line" else "words"
top = "greatest number" if calculation_flag == "long" else "longest line" if calculation_flag == "line"\
    else "longest word"
is_line = "\n" if calculation_flag == "line" else ""
result_string = f"""Total {topic}: {total}.
The {top}: {is_line}{greatest}{is_line} ({greatest_occurrences} time(s), {percentage_occurrence}%)."""

print(result_string)
