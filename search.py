def merge_sort(seq):
    # Reccurisive case
    if len(seq) > 1:
        # Middle index of sequence
        mid = len(seq) // 2

        # Creating lists of each half of seq
        first_seq = seq[:mid]
        second_seq = seq[mid:]

        # Sort both halves
        merge_sort(first_seq)
        merge_sort(second_seq)

        # Index values for future loops
        i = j = k = 0

        # Merging both sorted halves
        while i < len(first_seq) and j < len(second_seq):
            if first_seq[i] < second_seq[j]:
                seq[k] = first_seq[i]
                i += 1
            else:
                seq[k] = second_seq[j]
                j += 1
            k += 1

        # Add remaining elements from the list not emptied
        while i < len(first_seq):
            seq[k] = first_seq[i]
            i += 1
            k += 1

        while j < len(second_seq):
            seq[k] = second_seq[j]
            j += 1
            k += 1


def lin_search(seq, el):
    """Performs a linear search to find el

    Args:
        el (any): element to be found
        seq (sequence): sequence to find el in

    Returns:
        integer | None: index of el if exists, None if not
    """

    # Loop through seq until element found or end is reached
    for i in range(len(seq)):
        # Return index if element was found
        if seq[i] == el:
            return i

    # Element does not exist in sequence, returns None
    return None


def bin_search(seq, el):
    """Performs a binary search to find el.

    Args:
        seq (sequence[comparable]): SORTED sequence of elements
        el (comparable): element to be found

    Returns:
        integer | None: index of el if exists, None if not
    """

    beg = 0
    end = len(seq) - 1

    # Splitting sequence in half until el is found
    while (beg <= end):
        # Middle index of the sequence
        mid = (end + beg) // 2

        # Locating where el should be
        if seq[mid] == el:
            return mid
        elif seq[mid] > el:
            end = mid - 1
        else:
            beg = mid + 1

    # El does not exist in sequence
    return None
