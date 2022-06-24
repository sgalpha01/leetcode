from collections import deque, defaultdict


def findOrder(num_courses: int, prerequisites):
    preq = {i: set() for i in range(num_courses)}
    graph = defaultdict(set)
    for i, j in prerequisites:
        preq[i].add(j)
        graph[j].add(i)

    q = deque([])
    for key, val in preq.items():
        if len(val) == 0:
            q.append(key)

    taken = []
    while q:
        course = q.popleft()
        taken.append(course)
        if len(taken) == num_courses:
            return taken
        for cor in graph[course]:
            preq[cor].remove(course)
            if not preq[cor]:
                q.append(cor)
    return []
