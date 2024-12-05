import re

results = 0
with open("input.txt") as file:
    for row in file:
        multiply = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', row)
        for index in range(len(multiply)):
            number_1 = re.search(r"(?<=mul\()\d{1,3}", multiply[index]).group()
            number_2 = re.search(r",(?<=,)\d{1,3}(?=\))", multiply[index]).group()
            number_2 = number_2.replace(",","")

            result = int(number_1) * int(number_2)
            results += result

print(results)