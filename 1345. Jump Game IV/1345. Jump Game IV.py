from collections import deque, defaultdict


def min_jumps(arr):
    stack = deque([0])
    graph = defaultdict(list)
    for idx, num in enumerate(arr):
        graph[num].append(idx)

    steps = 0
    while stack:
        steps += 1
        for _ in range(len(stack)):
            idx = stack.popleft()
            if idx - 1 >= 0 and arr[idx - 1] in graph:
                stack.append(idx - 1)

            if idx + 1 == len(arr) - 1:
                return steps

            if idx + 1 < len(arr) and arr[idx + 1] in graph:
                stack.append(idx + 1)

            for jump_idx in graph.pop(arr[idx], []):
                if jump_idx == len(arr) - 1:
                    return steps
                if jump_idx != idx:
                    stack.append(jump_idx)

    return steps


arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
print(min_jumps(arr))
