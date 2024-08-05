def max_min_distance(stalls, cows):
    stalls.sort()
    low = 1
    high = stalls[-1] - stalls[0]
    res = -1

    while low <= high:
        mid = (low + high) // 2
        if can_place_cows(stalls, cows, mid):
            res = mid
            low = mid + 1
        else:
            high = mid - 1

    return res

def can_place_cows(stalls, cows, min_distance):
    count = 1
    prev_stall = stalls[0]

    for stall in stalls[1:]:
        if stall - prev_stall >= min_distance:
            count += 1
            prev_stall = stall
        if count == cows:
            return True

    return False

N, C = map(int, input().split())
stalls = [int(input()) for _ in range(N)]

print(max_min_distance(stalls, C))