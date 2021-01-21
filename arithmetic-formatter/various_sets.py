import re

test_input = ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
solution = False

data = []

for item in test_input:
    datum = [re.findall('[0-9]+', item), re.findall('[+-]', item)]
    if datum[1][0] == '+':
        datum.append(str(int(datum[0][0])+int(datum[0][1])))
    else:
        datum.append(str(int(datum[0][0])-int(datum[0][1])))
    datum.append(max(len(datum[0][0]), len(datum[0][1])) + 2)
    data.append(datum)

#x = [print(datum) for datum in data]

to_print = ''
line_one = ''
line_two = ''
line_three = ''
line_four = ''

for datum in data:
    line_one += (' '*(datum[3] - len(datum[0][0]))) + datum[0][0] + '    '
    line_two += datum[1][0] + (' '*(datum[3] - len(datum[0][1]) - 1)) + datum[0][1] + '    '
    line_three += '-'*datum[3] + '    '
    if solution:
        line_four += (' '*(datum[3] - len(datum[2]))) + datum[2] + '    '

if solution:
    to_print = line_one + '\n' + line_two + '\n' + line_three + '\n' + line_four
else:
    to_print = line_one + '\n' + line_two + '\n' + line_three

print(to_print)