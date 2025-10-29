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


# Result presentation
def sort_data(dat, sort):
    if sort == "natural" and data_type in ("long", "word"):
        sorted_data = sorted(dat)
        sorted_data = map(str, sorted_data)
        result = " ".join(sorted_data)
        return result
    elif sort == "natural" and data_type == "line":
        sorted_data = sorted(dat)
        result = "\n".join(sorted_data)
        return result
    else:
        occurrence_dict = {}
        sorted_data = []
        for item in dat:
            number_of_times = dat.count(item)
            percentage = int(number_of_times / total * 100)
            occurrence_dict[item] = [number_of_times, percentage]
            sorted_data = sorted(occurrence_dict.items(), key=lambda item: (item[1][0], item[0]))

        tmp_res = [f"{item[0]}: {item[1][0]} time(s), {item[1][1]}%" for item in sorted_data]
        result = "\n".join(tmp_res)
        return result


def generate_result():
    result_string = ""
    topic = "numbers" if data_type == "long" else "lines" if data_type == "line" else "words"
    is_line = "\n" if data_type == "line" else ""

    sorted_data = sort_data(data, sorting_type)

    if sorting_type == "natural":
        result_string = f"""Total {topic}: {total}
Sorted data: {is_line}{sorted_data}"""
    else:
        result_string = f"""Total {topic}: {total}.
{sorted_data}"""

    return result_string


print(generate_result())
