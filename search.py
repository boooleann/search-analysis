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
