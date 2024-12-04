def main():
    list1 = []
    list2 = []
    with open("input.txt") as file:
        for row in file:
            complete_list = row.split()
            list1.append(complete_list[0])
            list2.append(complete_list[1])
    list1.sort()
    list2.sort()

    total_distance = 0
    index = 0
    for element in list1:
        element = int(element)
        list2[index] = int(list2[index])
        distance = abs(element - list2[index])
        index += 1
        total_distance += distance

    print(total_distance)

if __name__ is main():
    main()