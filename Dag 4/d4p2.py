def open_file(input_file):
    with open(input_file) as file:
        data = [[x for x in line.strip()] for line in file]
        return data


def xmas(data, index_line, index_item):
    if (
        index_line <= 0 or index_item <= 0 or  # Top-left boundary
        index_line >= len(data) - 1 or index_item >= len(data[index_line]) - 1  # Bottom-right boundary
    ):
        return False

    if data[index_line][index_item] == "A":
        if data[index_line - 1][index_item - 1] == "M":
            if data[index_line + 1][index_item + 1] == "S":
                if data[index_line - 1][index_item + 1] == "M":
                    if data[index_line + 1][index_item - 1] == "S":
                        return True
        elif data[index_line - 1][index_item - 1] == "S":
            if data[index_line + 1][index_item + 1] == "M":
                if data[index_line - 1][index_item + 1] == "M":
                    if data[index_line + 1][index_item - 1] == "S":
                        return True
        elif data[index_line - 1][index_item - 1] == "M":
            if data[index_line + 1][index_item + 1] == "S":
                if data[index_line - 1][index_item + 1] == "S":
                    if data[index_line + 1][index_item - 1] == "M":
                        return True
        elif data[index_line - 1][index_item - 1] == "S":
            if data[index_line + 1][index_item + 1] == "M":
                if data[index_line - 1][index_item + 1] == "S":
                    if data[index_line + 1][index_item - 1] == "M":
                        return True
    return False


def main():
    input_data = open_file('input.txt')
    score = 0
    for line in range(len(input_data)):
        for item in range(len(input_data[line])):
            if line > 0 and line < len(input_data):
                if item > 0 and item < len(input_data[line]):
                    if xmas(input_data, line, item):
                        score += 1
    print(score)


if __name__ == '__main__':
    main()
