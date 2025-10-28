import argparse

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-dataType", choices=["long", "line", "word"], default="word")
parser.add_argument("-sortingType", choices=["natural", "byCount"], default="natural")
args = parser.parse_args()

# Params
data_type = args.dataType
sorting_type = args.sortingType


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
def sort_data(dat, sort):

    # sorted_data = sorted(data.copy())
    # sorted_data = map(str, sorted_data)
    # join = " ".join(sorted_data)
    pass


def generate_result():
    result_string = ""
    topic = "numbers" if data_type == "long" else "lines" if data_type == "line" else "words"
    is_line = "\n" if data_type == "line" else ""

    sort_data(data, sorting_type)

    result_string = f"""Total {topic}: {total}.
Sorted data: """

    return result_string


print(generate_result())
