# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.


def comp(array_a, array_b):
    if array_a is None or array_b is None:
        return False

    # Square each element in array_a
    squared_a = [x**2 for x in array_a]

    # Sort both lists to compare
    return sorted(squared_a) == sorted(array_b)
