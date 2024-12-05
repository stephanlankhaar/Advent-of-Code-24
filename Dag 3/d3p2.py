import re

results = 0
with open("input.txt") as file:
    for row in file:
        multiply = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)', row)
        to_multiply=[]
        processing = True
        for item in multiply:
            if item == 'do()':
                processing = True
            if item == 'don\'t()':
                processing = False
            if processing:
                if item != "do()":
                    number_1 = re.search(r"(?<=mul\()\d{1,3}",
                                         item).group()
                    number_2 = re.search(r",(?<=,)\d{1,3}(?=\))",
                                         item).group()
                    number_2 = number_2.replace(",", "")

                    result = int(number_1) * int(number_2)
                    results += result


print(results)