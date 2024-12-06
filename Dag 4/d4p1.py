def open_file(input_file):
    with open(input_file) as file:
        data = [[x for x in line.strip()] for line in file]
        return data


def xmas_up(data, index_row, index_item):
    if data[index_row][index_item] == 'X':
        if data[index_row - 1][index_item] == 'M':
            if data[index_row - 2][index_item] == 'A':
                if data[index_row - 3][index_item] == 'S':
                    return True
    return False


def xmas_down(data, index_row, index_item):
    if data[index_row][index_item] == 'X':
        if data[index_row + 1][index_item] == 'M':
            if data[index_row + 2][index_item] == 'A':
                if data[index_row + 3][index_item] == 'S':
                    return True
    return False

def xmas_left(data, index_row, index_item):
    if data[index_row][index_item] == 'X':
        if data[index_row][index_item-1] == 'M':
            if data[index_row][index_item-2] == 'A':
                if data[index_row][index_item-3] == 'S':
                    return True
    return False

def xmas_right(data, index_row, index_item):
    if data[index_row][index_item] == 'X':
        if data[index_row][index_item+1] == 'M':
            if data[index_row][index_item+2] == 'A':
                if data[index_row][index_item+3] == 'S':
                    return True
    return False

def xmax_dig_left_up(data, index_row, index_item):
    if data[index_row][index_item] == 'X':
        if data[index_row - 1][index_item-1] == 'M':
            if data[index_row - 2][index_item-2] == 'A':
                if data[index_row - 3][index_item-3] == 'S':
                    return True
    return False

def xmax_dig_right_up(data, index_row, index_item):
    if data[index_row][index_item] == 'X':
        if data[index_row - 1][index_item+1] == 'M':
            if data[index_row - 2][index_item+2] == 'A':
                if data[index_row - 3][index_item+3] == 'S':
                    return True
    return False

def xmax_dig_left_down(data, index_row, index_item):
    if data[index_row][index_item] == 'X':
        if data[index_row + 1][index_item-1] == 'M':
            if data[index_row + 2][index_item-2] == 'A':
                if data[index_row + 3][index_item-3] == 'S':
                    return True
    return False

def xmax_dig_right_down(data, index_row, index_item):
    if data[index_row][index_item] == 'X':
        if data[index_row + 1][index_item+1] == 'M':
            if data[index_row + 2][index_item+2] == 'A':
                if data[index_row + 3][index_item+3] == 'S':
                    return True
    return False
def main():
    input_data = open_file('input.txt')
    score = 0
    for index_row in range(len(input_data)):
        for index_item in range(len(input_data[index_row])):
            if index_row > 2:
                if xmas_up(input_data, index_row, index_item):
                  score += 1
            if index_row < len(input_data)-2:
                if xmas_down(input_data, index_row, index_item):
                    score += 1
            if index_item > 2:
                if xmas_left(input_data, index_row, index_item):
                    score += 1
            if index_item < len(input_data[0])-3:
                if xmas_right(input_data, index_row, index_item):
                    score += 1
            if index_row > 2 and index_item > 2:
                if xmax_dig_left_up(input_data, index_row, index_item):
                    score += 1
            if index_row > 2 and index_item < len(input_data)-3:
                if xmax_dig_right_up(input_data, index_row, index_item):
                    score += 1
            if index_row < len(input_data)-3 and index_item > 2:
                if xmax_dig_left_down(input_data, index_row, index_item):
                    score += 1
            if index_row < len(input_data)-3 and index_item < len(input_data)-3:
                if xmax_dig_right_down(input_data, index_row, index_item):
                    score += 1

    print(score)


if __name__ == '__main__':
    main()
