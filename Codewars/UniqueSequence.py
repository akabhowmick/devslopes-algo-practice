def unique_in_order(sequence):
    if not sequence:  # Check if the sequence is empty
        return []

    result = [sequence[0]]  # Start with the first element in the sequence

    for element in sequence[1:]:
        if element != result[-1]:  # Compare with the last element in the result list
            result.append(element)

    return result
