import argparse

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-dataType", choices=["long", "line", "word"], default="word", nargs='?')
parser.add_argument("-sortingType", choices=["natural", "byCount"], default="natural", nargs='?')
parser.add_argument("-inputFile", default="not_provided", nargs="?")
parser.add_argument("-outputFile", default="not_provided", nargs="?")
args, unknown_args = parser.parse_known_args()
data = []


class ArgException(Exception):
    def __init__(self, arg):
        if arg == "data" or arg == "sorting":
            arg = arg + " type"
        self.message = f"No {arg} defined!"
        super().__init__(self.message)


def validate_args():
    global data_type, sorting_type, input_file, output_file
    # Params
    try:
        data_type = args.dataType
        sorting_type = args.sortingType
        input_file = args.inputFile
        output_file = args.outputFile
        if not data_type:
            raise ArgException("data")
        if not sorting_type:
            raise ArgException("sorting")
        if not input_file or not output_file:
            raise ArgException("filename")

        if unknown_args:
            for arg in unknown_args:
                print(f'"{arg}" is not a valid parameter. It will be skipped.')

        return 1

    except ArgException as e:
        print(e)

    return 0


def get_input(input_type, input_file):
    long_wrong = []

    if input_file not in (None, "not_provided"):
        file = open(input_file, "rt")
        for line in file:
            if input_type == "long":
                for num in line.split():
                    try:
                        data.append(int(num))
                    except ValueError:
                        long_wrong.append(num)
            elif input_type == "word":
                for word in line.split():
                    data.append(word)
            else:
                for ln in line.splitlines():
                    data.append(ln)
        file.close()
    else:
        while True:
            try:
                if input_type == "long":
                    for num in input().split():
                        try:
                            data.append(int(num))
                        except ValueError:
                            long_wrong.append(num)
                elif input_type == "word":
                    for word in input().split():
                        data.append(word)
                else:
                    for line in input().splitlines():
                        data.append(line)

            except EOFError:
                break

    if long_wrong:
        for item in long_wrong:
            print(f'"{item}" is not a long. It will be skipped.')


# Result presentation
def sort_data(dat, sort, total):
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


def generate_result(output_file):
    result_string = ""
    total = len(data)
    topic = "numbers" if data_type == "long" else "lines" if data_type == "line" else "words"
    is_line = "\n" if data_type == "line" else ""

    sorted_data = sort_data(data, sorting_type, total)

    if sorting_type == "natural":
        result_string = f"""Total {topic}: {total}
Sorted data: {is_line}{sorted_data}"""
    else:
        result_string = f"""Total {topic}: {total}.
{sorted_data}"""

    if output_file not in (None, "not_provided"):
        file = open(output_file, 'w')
        file.write(result_string)
        file.close()
    else:
        return result_string


def main():
    if validate_args():
        get_input(data_type, input_file)
        res = generate_result(output_file)
        if res:
            print(res)


if __name__ == "__main__":
    main()
