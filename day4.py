with open('input.txt') as file_:
    input = file_.read().splitlines()

cards = {}
for number in range(len(input)):
    cards[number] = 1

points = 0
for idx, line in enumerate(input):
    line = line.split(': ', 1)[1].strip()
    winning, numbers = line.split(' | ')
    winning = set(winning.split(' '))
    winning.discard('')
    numbers = set(numbers.split(' '))
    numbers.discard('')
    if matches := winning.intersection(numbers):
        points += pow(2, len(winning.intersection(numbers))-1)
        for card in range(idx+1, idx+1+len(matches)):
            cards[card] += 1 * cards[idx]
print(points)
print(sum(cards.values()))