with open('input.txt') as file_:
    input = file_.read().splitlines()

# part 1
result = {'five': [], 'four': [], 'full_house': [],
          'three': [], 'two_pair': [], 'one_pair': [],
          'high': []}
for line in input:
    line = line.replace('T', 'a').replace('J', 'b').replace('Q', 'c'). \
        replace('K', 'd').replace('A', 'e')
    hand = line.split()[0]
    hand_set = set(hand)
    if len(hand_set) == 1:
        result['five'].append(line)
    elif len(hand_set) == 2:
        if hand.count(hand[0]) in (1, 4):
            result['four'].append(line)
        else:
            result['full_house'].append(line)
    elif len(hand_set) == 3:
        for char in hand:
            if hand.count(char) == 3:
                result['three'].append(line)
                break
            elif hand.count(char) == 2:
                result['two_pair'].append(line)
                break
    elif len(hand_set) == 4:
        result['one_pair'].append(line)
    else:
        result['high'].append(line)
multiplier = len(input)
total_sum = 0
for type_ in result.keys():
    result[type_].sort(reverse=True)
    for hand in result[type_]:
        total_sum += multiplier * int(hand.split()[1])
        multiplier -= 1
print(total_sum)

# part 2
result = {'five': [], 'four': [], 'full_house': [],
          'three': [], 'two_pair': [], 'one_pair': [],
          'high': []}
for line in input:
    line = line.replace('T', 'a').replace('J', '1').replace('Q', 'c'). \
        replace('K', 'd').replace('A', 'e')
    hand = line.split()[0]
    hand_set = set(hand)
    joker_exists = '1' in hand_set
    if len(hand_set) == 1:
        result['five'].append(line)
    elif len(hand_set) == 2:
        if hand.count(hand[0]) in (1, 4):
            if joker_exists:
                result['five'].append(line)
            else:
                result['four'].append(line)
        else:
            if joker_exists:  # Converting either a single or quad to the other becomes a five
                result['five'].append(line)                    
            else:
                result['full_house'].append(line)
    elif len(hand_set) == 3:
        for char in hand:
            if hand.count(char) == 3:
                if char == '1':  # A triple jokers become a four
                    result['four'].append(line)
                elif joker_exists:  # A triple plus a joker becomes a four
                    result['four'].append(line)
                else:
                    result['three'].append(line)
                break
            elif hand.count(char) == 2:
                if char == '1':  # A double joker gets converted into the other pairs card
                    result['four'].append(line)
                elif joker_exists:  # A double plus either double joker or single joker
                    if hand.count('1') == 1: # A double plus single joker becomes full house
                        result['full_house'].append(line)
                    else:  # A double plus double joker becomes a four
                        result['four'].append(line)
                else:
                    result['two_pair'].append(line)
                break
    elif len(hand_set) == 4:
        if joker_exists:  # Either a joker pair or a single joker becomes a triple hand
            result['three'].append(line)
        else:
            result['one_pair'].append(line)
    else:
        if joker_exists:
            result['one_pair'].append(line)
        else:
            result['high'].append(line)
multiplier = len(input)
total_sum = 0
for type_ in result.keys():
    result[type_].sort(reverse=True)
    for hand in result[type_]:
        total_sum += multiplier * int(hand.split()[1])
        multiplier -= 1
print(total_sum)