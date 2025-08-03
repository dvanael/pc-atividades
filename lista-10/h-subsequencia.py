# H. Subsequência

len_seq_a, len_seq_b = map(int, input().split())

seq_a = list(map(int, input().split()))
seq_b = list(map(int, input().split()))


def subsequence(seq_a: list[int], seq_b: list[int]) -> str:
    count = 0
    for i in seq_a:
        if count < len(seq_b) and i == seq_b[count]:
            count += 1

    if count == len(seq_b):
        return "S"
    return "N"


print(subsequence(seq_a, seq_b))
