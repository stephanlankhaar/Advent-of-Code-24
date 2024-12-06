import re

results = 0
with open("input.txt") as file:
    processing = True
    for row in file:
        multiply = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\))", row)
        for item in multiply:
            if item == 'don\'t()':
                processing = False
            if item == 'do()':
                processing = True
            else:
                if processing and item.startswith('mul'):
                    if item != "do()":
                        to_multiply = item.replace('mul(', '').replace(')','')
                        to_multiply = to_multiply.split(",")
                        results += int(to_multiply[0]) * int(to_multiply[1])

print(results)
