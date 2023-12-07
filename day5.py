with open('input.txt') as file_:
    input = file_.read().splitlines()

# Part 1
seeds = [int(x) for x in input[0].split(' ')[1:]]
remapped_indices = []
for line in input[2:]:
    if line == '':
        # remaining seeds keep their number
        continue
    if ':' in line:
        # new map
        remapped_indices = []
        continue
    dest, src, length = [int(x) for x in line.split()]
    for idx, seed in enumerate(seeds):
        if idx in remapped_indices:
            # Already handled
            continue
        if src <= seed <= src + length:
            # Seed is included in this remapping
            seeds[idx] = seed - src + dest
            remapped_indices.append(idx)
print(min(seeds))

# Print 2
numbers = [int(x) for x in input[0].split(' ')[1:]]
ranges = []
for idx in range(len(numbers)//2):
    ranges.append(range(numbers[2*idx], numbers[2*idx] + numbers[2*idx+1]))

new_ranges = []  # Ranges that were changed by current mapping
pending_ranges = []  # Leftover ranges when parts of a range is re-mapped
for line in input[2:]:
    if line == '':
        continue
    if ':' in line:
        # New mapping. Add the new ranges from the last mapping to the old ones.
        ranges.extend(new_ranges)
        new_ranges = []
        continue
    dest, src, length = [int(x) for x in line.split()]
    for idx, range_ in enumerate(ranges.copy()):
        if overlap := range(max(src, range_.start), min(src + length, range_.stop)):
            if pre_overlap := range(range_.start, src):
                pending_ranges.append(pre_overlap)
            if post_overlap := range(src + length, range_.stop):
                pending_ranges.append(post_overlap)
            new_ranges.append(range(overlap.start - (src-dest), overlap.stop - (src-dest)))
            ranges.remove(range_)
    ranges.extend(pending_ranges)  # Add all new ranges for the numbers not re-mapped.
    pending_ranges = []
ranges.extend(new_ranges)
print(min([x.start for x in ranges]))