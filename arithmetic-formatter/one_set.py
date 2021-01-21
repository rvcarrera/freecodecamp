import re

test_input = "9999 + 9999"

numbers = re.findall('[0-9]+', test_input)

operation = re.findall('[+-]', test_input)

solution = 0

if operation[0] == '+':
    solution = int(numbers[0]) + int(numbers[1])
else:
    solution = int(numbers[0]) - int(numbers[1])

solution_s  = str(solution)

print(numbers, operation, solution_s)

lenght = max(len(numbers[0]), len(numbers[1])) + 2

print(lenght)

print((' '*(lenght - len(numbers[0]))) + numbers[0])
print(operation[0] + (' '*(lenght - len(numbers[1]) - 1)) + numbers[1])
print('-'*lenght)
print((' '*(lenght - len(solution_s))) + solution_s)