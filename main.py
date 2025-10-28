import argparse

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-dataType", choices=["long", "line", "word"], default="word")
parser.add_argument("-sortIntegers", action="store_true")
args = parser.parse_args()
data_type = args.dataType
sort_int = args.sortIntegers
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


if sort_int:
    data_type = "long"


if data_type == "long":
    get_input("long")
elif data_type == "word":
    get_input("word")
else:
    get_input("line")

# Calculations
total = len(data)
greatest = max(data) if data_type == "long" else max(data, key=len)
greatest_occurrences = data.count(greatest)
percentage_occurrence = int(greatest_occurrences / total * 100)


# Result presentation
def generate_result():
    result_string = ""
    if not sort_int:
        topic = "numbers" if data_type == "long" else "lines" if data_type == "line" else "words"
        top = "greatest number" if data_type == "long" else "longest line" if data_type == "line" \
            else "longest word"
        is_line = "\n" if data_type == "line" else ""

        result_string = f"""Total {topic}: {total}.
The {top}: {is_line}{greatest}{is_line} ({greatest_occurrences} time(s), {percentage_occurrence}%)."""
    else:
        sorted_data = sorted(data.copy())
        sorted_data = map(str, sorted_data)
        join = " ".join(sorted_data)
        result_string = f"""Total numbers: {total}.
Sorted data: {join}"""

    return result_string


print(generate_result())
