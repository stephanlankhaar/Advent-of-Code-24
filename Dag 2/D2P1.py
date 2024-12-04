def main():
    safe_counter = 0
    with open("input.txt") as file:
        for row in file:
            report_list = list(map(int, row.split()))

            if sorted(report_list) == report_list or sorted(report_list, reverse=True) == report_list:
                if all(abs(report_list[i] - report_list[i+1]) in range(1, 4) for i in range(len(report_list) - 1)):
                    print(report_list)
                    safe_counter += 1

        print(safe_counter)

if __name__ == "__main__":
    main()
