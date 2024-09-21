def sum_pairs(ints, s):
    seen = {}

    for num in ints:
        target = s - num
        if target in seen:
            return [target, num]
        seen[num] = seen.get(num, 0) + 1

    return None
