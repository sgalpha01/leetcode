from collections import deque


def simplify_path(path):
    path = path.split("/")
    stack = deque()
    for directory in path:
        if directory == "..":
            if stack:
                stack.pop()
        elif directory == "." or not directory:
            continue
        else:
            stack.append(directory)

    return "/" + "/".join(stack)


path = "/home/"
print(simplify_path(path))
