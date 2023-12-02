with open('input.txt') as file_:
    input = file_.readlines()

# First part
id_sum = 0
for idx, line in enumerate(input):
    failed = False
    line = line.strip().split(': ', 1)[1]
    handfuls = line.split(';')
    for collection in handfuls:
        number_and_colours = collection.strip().split(',')
        for number_colour in number_and_colours:
            number, colour = number_colour.split()
            number = int(number)
            if colour == 'red' and number > 12:
                failed = True
                break
            if colour == 'green' and number > 13:
                failed = True
                break
            if colour == 'blue' and number > 14:
                failed = True
                break
        if failed:
            break
    if not failed:
        id_sum += idx + 1    
print(id_sum)

# Second part
total_sum = 0
for line in input:
    red = blue = green = 1
    line = line.strip().split(': ', 1)[1]
    handfuls = line.split(';')
    for collection in handfuls:
        number_and_colours = collection.strip().split(',')
        for number_colour in number_and_colours:
            number, colour = number_colour.split()
            number = int(number)
            if colour == 'red':
                red = max(red, number)
            if colour == 'green':
                green = max(green, number)
            if colour == 'blue':
                blue = max(blue, number)
    total_sum += red * blue * green
print(total_sum)