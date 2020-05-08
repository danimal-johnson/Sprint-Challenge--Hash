def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    ht = {}  # Using a dictionary as a hash table.

    # Fill
    for i in range(length):
        ht[weights[i]] = i  # { curr_weight: index }

    for i in range(length):
        weight_complement = limit - weights[i]
        if weight_complement in ht:
            return_val = [i, ht[weight_complement]]
            return_val.sort(reverse=True)
            return return_val

    return None
