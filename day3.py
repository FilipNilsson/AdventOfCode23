# First half
with open('input.txt') as file_:
    input = file_.read().splitlines()
for idx, line in enumerate(input):
    input[idx] = '.' + line + '.'
input.insert(0, '.' * len(input[0]))
input.append('.' * len(input[0]))

sum = 0
for row, line in enumerate(input):
    number = ""
    for col, char in enumerate(line):
        if char.isdigit():
            number += char
        if not char.isdigit():
            if number:
                area = input[row-1][col-len(number)-1:col+1] + \
                       input[row][col-len(number)-1:col+1] + \
                       input[row+1][col-len(number)-1:col+1]
                area = ''.join([x for x in area if not x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']])
                if area:
                    sum += int(number)
            number = ""
print(sum)

# Second half
numbers = []
for row, line in enumerate(input):  # Create bounding boxes around every number and store the number value in it
    number = {'number': '', 'bound': [[999999999999,0], [0,0]]}  # bound is ((x_min, y_min), (x_max, y_max))
    for col, char in enumerate(line):
        if char.isdigit():
            number['number'] += char
            number['bound'][0][0] = min(number['bound'][0][0], col-1)  # x min
            number['bound'][1][0] = col+1  # x max
            number['bound'][0][1] = row-1  # y min
            number['bound'][1][1] = row+1  # y max
        if not char.isdigit() and number['number']:
            number['number'] = int(number['number'])
            numbers.append(number)
            number = {'number': '', 'bound': [[999999999999,0], [0,0]]}

sum = 0
for row, line in enumerate(input):  # Process every gear in input
    for col, char in enumerate(line):
        if char == '*':
            numbers_touched = []
            for rectangle in numbers:
                if rectangle['bound'][0][0] <= col <= rectangle['bound'][1][0] and rectangle['bound'][0][1] <= row <= rectangle['bound'][1][1]:
                    # Gear is in range of this number
                    numbers_touched.append(rectangle['number'])
            if len(numbers_touched) == 2:
                sum += numbers_touched[0] * numbers_touched[1]
print(sum)