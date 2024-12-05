import re

results = 0
with open("input.txt") as file:
    for row in file:
        multiply = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)', row)
        for index in range(len(multiply)-1):
            index_do = 0
            index_dont = 0
            if multiply[index] == 'do()':
                if multiply[index+1] == 'do()':
                    multiply.pop(index+1)
                if multiply[index+1] != 'don\'t()':
                    print(multiply[index+1])
                    number_1 = re.search(r"(?<=mul\()\d{1,3}", multiply[index+1]).group()
                    number_2 = re.search(r",(?<=,)\d{1,3}(?=\))", multiply[index+1]).group()
                    number_2 = number_2.replace(",","")

                    result = int(number_1) * int(number_2)
                    results += result

print(results)