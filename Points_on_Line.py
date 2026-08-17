import sys

input = sys.stdin.read().split()

if input:
    n = int(input[0])
    d = int(input[1])
    x = [int(val) for val in input[2:]]

    total_triplets = 0
    left = 0

    for right in range(n):
        while x[right] - x[left] > d:
            left += 1

        count = right - left
        if count >= 2:
            total_triplets += count * (count - 1) // 2

    print(total_triplets)
    