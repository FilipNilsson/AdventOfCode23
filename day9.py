with open('input.txt') as file_:
    input_ = file_.read().splitlines()

import math
part1 = False
x_list = range(1, len(input_[0].split()) + 1)
if part1:
    unknown_x = len(input_[0].split()) + 1
else:
    unknown_x = 0
total_sum = 0
for line in input_:
    y_list = [int(y) for y in line.split()]
    nominator = math.factorial(len(input_[0].split()))
    sum = 0
    for idx, number in enumerate(y_list):
        täljare = 1
        for value in x_list:
            if value == idx+1:
                continue
            täljare *= idx+1 - value
            täljare = round(täljare)
        sum += round(number * (nominator / (unknown_x-idx-1)) / täljare)
    total_sum += sum
print(abs(total_sum))  # No idea why abs was needed for my final input on part 2