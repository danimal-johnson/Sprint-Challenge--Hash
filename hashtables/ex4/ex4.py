def has_negatives(a):
    """
    Finds the positive integers in a list that have matching negative integers.
    Two-pass algorithm:
    1. Store the negative numbers in a hash table.
    2. Check each positive number. Add matches to result.
    """
    result = []
    ht = {}

    for number in a:
        if number < 0:
            # It doesn't actually matter what we store here.
            ht[number] = 'True'

    for number in a:
        if number > 0:
            inverse = 0 - number
            if inverse in ht:
                result.append(number)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
