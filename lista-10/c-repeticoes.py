# C. Repetições


def greater_sequence(sequence: str) -> int:
    max_count = 1
    current_count = 1

    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            current_count += 1
            # get max between max and current
            max_count = max(max_count, current_count)
        else:
            # maintain one char sequence
            current_count = 1

    return max_count


print(greater_sequence(input()))
