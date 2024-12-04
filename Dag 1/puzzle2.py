def main():
    list1 = []
    list2 = []
    with open("input.txt") as file:
        for row in file:
            complete_list = row.split()
            list1.append(complete_list[0])
            list2.append(complete_list[1])

        similarity_score_total = 0
        index = 0
        for element in list1:
            similarity_score = int(element) * list2.count(element)
            similarity_score_total += similarity_score
            index += 1

        print(similarity_score_total)

if __name__ is main():
    main()