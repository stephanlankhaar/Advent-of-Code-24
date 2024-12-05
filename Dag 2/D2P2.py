def safe_report(input_list):
    if sorted(input_list) == input_list or sorted(input_list,
                                                    reverse=True) == input_list:
        if all(abs(input_list[i] - input_list[i + 1]) in range(1, 4) for i in
               range(len(input_list) - 1)):
            return True
    else:
        return False

def main():
    safe_counter = 0
    with open("input.txt") as file:
        for row in file:
            report_list = list(map(int, row.split()))
            for index in range(len(report_list)):
                tmp_item_list = report_list[index]
                report_list.pop(index)
                if safe_report(report_list):
                    safe_counter +=1
                    break
                report_list.insert(index, tmp_item_list)

        print(safe_counter)

if __name__ == "__main__":
    main()
