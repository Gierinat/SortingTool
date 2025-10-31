import argparse

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-dataType", choices=["long", "line", "word"], default="word", nargs='?')
parser.add_argument("-sortingType", choices=["natural", "byCount"], default="natural", nargs='?')
args, unknown_args = parser.parse_known_args()
data = []
arg

class ArgException(Exception):
    def __init__(self, arg):
        self.message = f"No {arg} type defined!"
        super().__init__(self.message)


# Params
try:
    data_type = args.dataType
    sorting_type = args.sortingType
    if not data_type:
        raise ArgException("data")
    if not sorting_type:
        raise ArgException("sorting")

    if unknown_args:
        for arg in unknown_args:
            print(f'"{arg}" is not a valid parameter. It will be skipped.')

except ArgException as e:
    print(e)


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
    total = len(data)
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


def main():
    if data_type == "long":
        get_input("long")
    elif data_type == "word":
        get_input("word")
    else:
        get_input("line")

    print(generate_result())


if __name__ == "__main__":
    main()
