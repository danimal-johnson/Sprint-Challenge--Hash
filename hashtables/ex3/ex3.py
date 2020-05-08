def intersection(arrays):
    """
    Takes an arbitritrary number of lists of arbitrary
    length and returns a list of all integers that are present
    in ALL of them (the intersection).

    Note: this function assumes there are no duplicates within
    each array.
    """
    num_arrays = len(arrays)
    ht = {}
    result = []

    # Only a mischeivous person would try this:
    if num_arrays == 0:
        return None

    # Only one array passed. All values intersect.
    if num_arrays == 1:
        return arrays[0]

    # Increment each number's value in the hash table.
    # Don't do the last one yet.
    for i in range(num_arrays - 1):  # 0 to num_arrays-2
        arr = arrays[i]
        for j in range(len(arr)):
            num = arr[j]
            if num not in ht:
                ht[num] = 1
            else:
                ht[num] += 1

    # Put passing values in result while parsing the last array.
    for num in arrays[num_arrays - 1]:
        if num in ht:
            # If every array has incremented this value so far.
            if ht[num] == num_arrays - 1:
                result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
