with open('input.txt') as file_:
    input = file_.read().splitlines()

part_1 = False

# Part 1
if part_1:
    times = [int(x) for x in input[0].split()[1:]]
    min_distance = [int(x) for x in input[1].split()[1:]]
# Part 2
else:
    times = [int(''.join(input[0].split()[1:]))]
    min_distance = [int(''.join(input[1].split()[1:]))]

prod = 1
for race in range(len(times)):
    lower_bound = (times[race] / 2) - pow(pow(times[race]/2, 2) - min_distance[race], 0.5)
    if lower_bound == int(lower_bound):
        lower_bound = int(lower_bound + 1)
    else:
        lower_bound = int(-(-lower_bound//1))  # ceil
    upper_bound = (times[race] / 2) + pow(pow(times[race]/2, 2) - min_distance[race], 0.5)
    if upper_bound == int(upper_bound):
        upper_bound = int(upper_bound - 1)
    else:
        upper_bound = int(upper_bound)
    print(f'{race}: {lower_bound} - {upper_bound}, solutions: {upper_bound+1 - lower_bound}')
    prod *= upper_bound+1 - lower_bound
print(prod)