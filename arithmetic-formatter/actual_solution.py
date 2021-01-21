import re

problems = ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]
solution = False
arranged_problems = ''

if len(problems) > 5:
    arranged_problems = 'Error: Too many problems.'

data = []

for problem in problems:
    datum = [re.findall('[0-9]+', problem), re.findall('[+-]', problem)]
    if not datum[1]:
        arranged_problems = 'Error: Operator must be \'+\' or \'-\'.'
    if len(datum[0]) != 2:
        arranged_problems = 'Error: Numbers must only contain digits.'
    if max(len(datum[0][0]), len(datum[0][1])) > 4:
        arranged_problems = 'Error: Numbers cannot be more than four digits.'
    if datum[1][0] == '+':
        datum.append(str(int(datum[0][0])+int(datum[0][1])))
    else:
        datum.append(str(int(datum[0][0])-int(datum[0][1])))
    datum.append(max(len(datum[0][0]), len(datum[0][1])) + 2)
    data.append(datum)

line_one = (' '*(data[0][3] - len(data[0][0][0]))) + data[0][0][0]
line_two = data[0][1][0] + (' '*(data[0][3] - len(data[0][0][1]) - 1)) + data[0][0][1]
line_three = '-'*data[0][3]
line_four = (' '*(data[0][3] - len(data[0][2]))) + data[0][2]

for i in range(1, len(data)):
    line_one += '    ' + (' '*(data[i][3] - len(data[i][0][0]))) + data[i][0][0]
    line_two += '    ' + data[i][1][0] + (' '*(data[i][3] - len(data[i][0][1]) - 1)) + data[i][0][1]
    line_three += '    ' + '-'*data[i][3]
    line_four += '    ' + (' '*(data[i][3] - len(data[i][2]))) + data[i][2]

if solution:
    arranged_problems = line_one + '\n' + line_two + '\n' + line_three + '\n' + line_four
else:
    arranged_problems = line_one + '\n' + line_two + '\n' + line_three

print(arranged_problems)