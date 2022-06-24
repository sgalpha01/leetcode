from collections import deque


def can_reach(arr, start):
    q = deque([start])
    while q:
        curr = q.popleft()

        if arr[curr] == 0:
            return True

        if arr[curr] < 0:
            continue

        if curr + arr[curr] < len(arr):
            q.append(curr + arr[curr])

        if curr - arr[curr] >= 0:
            q.append(curr - arr[curr])

        arr[curr] *= -1

    return False


print(can_reach([0, 1], 1))
