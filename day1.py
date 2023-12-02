with open('input.txt') as file_:
    input = file_.readlines()

first = None
second = None
idx = 0
sum = 0
for line in input.copy():
    line = line.strip()
    while idx < len(line):
        if first is None:
            if line[idx].isdigit():
                first = line[idx]
            elif line[idx:].startswith("one"):
                first = "1"
            elif line[idx:].startswith("two"):
                first = "2"
            elif line[idx:].startswith("three"):
                first = "3"
            elif line[idx:].startswith("four"):
                first = "4"
            elif line[idx:].startswith("five"):
                first = "5"
            elif line[idx:].startswith("six"):
                first = "6"
            elif line[idx:].startswith("seven"):
                first = "7"
            elif line[idx:].startswith("eight"):
                first = "8"
            elif line[idx:].startswith("nine"):
                first = "9"
        if second is None:
            if line[-idx-1].isdigit():
                second = line[-idx-1]
            elif line[:len(line)-idx].endswith("one"):
                second = "1"
            elif line[:len(line)-idx].endswith("two"):
                second = "2"
            elif line[:len(line)-idx].endswith("three"):
                second = "3"
            elif line[:len(line)-idx].endswith("four"):
                second = "4"
            elif line[:len(line)-idx].endswith("five"):
                second = "5"
            elif line[:len(line)-idx].endswith("six"):
                second = "6"
            elif line[:len(line)-idx].endswith("seven"):
                second = "7"
            elif line[:len(line)-idx].endswith("eight"):
                second = "8"
            elif line[:len(line)-idx].endswith("nine"):
                second = "9"
        idx += 1
        if first is not None and second is not None:
            sum += int(first + second)
            idx = 0
            first = None
            second = None
            break
print(sum)