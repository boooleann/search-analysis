import random
from time import time

# Code modified from https://www.scaler.com/topics/merge-sort-in-python/


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


# Seed
random.seed(12345)


def generate_list_target(list_source, k):
    """Generate list of elements to be searched. First half will be in list_source, second half not

    Args:
        list_source (list): List of elements
        k (integer): Length of list target
    """

    # List of elements to search for. First half are in list_source, second half are not
    list_target = random.sample(list_source, round(
        k / 2)) + random.sample(range(len(list_source), len(list_source) * 2), round(k / 2))

    return list_target


# Experimenting with multiple "n" values
for n in [100, 1000, 10_000]:
    # Source of numbers to be searched
    list_source = random.sample(range(0, 1_000_000), n)

    # Displaying amount of elements in source
    print("n = ", n)

    # Amount of elements to be searching for
    k = 1

    # Testing linear and binary search algorithms with different numbers of search elements.
    while k < n:
        # Elements to search for
        list_target = generate_list_target(list_source, k)

        # Linear searching
        st = time()
        for el in list_target:
            lin_search(list_source, el)
        et = time()
        lin_time = et - st

        # Binary searching
        # List copy so original list does not get sorted
        sorted_list = list_source[:]

        st = time()
        # Sorting list
        merge_sort(sorted_list)

        # binary searching for each element in list_target
        for el in list_target:
            bin_search(sorted_list, el)
        et = time()
        bin_time = et - st

        # Displaying results of current amount of search terms
        print("k = %d, lin: %.4fs, bin: %.4fs" % (k, lin_time, bin_time))

        # Incrementing amount of elements
        if lin_time < bin_time:
            k += 5
        else:
            k += n // 10

    print()
