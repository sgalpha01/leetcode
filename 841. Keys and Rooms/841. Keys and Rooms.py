from collections import deque
from typing import List


def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    n = len(rooms)
    visited = [False] * n
    visited[0] = True
    stack = deque(rooms[0])
    while stack:
        for _ in range(len(stack)):
            room = stack.popleft()
            visited[room] = True
            for key in rooms[room]:
                if not visited[key]:
                    stack.append(key)
    return all(visited)


print(canVisitAllRooms([[1], [2], [3], []]))
