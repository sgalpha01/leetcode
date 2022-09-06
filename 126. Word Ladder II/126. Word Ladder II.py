def find_ladders(begin, end, word_list):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: List[List[str]]
    """
    word_list = set(word_list)
    if end not in word_list:
        return []
    if begin == end:
        return [[begin]]
    word_list.add(begin)
    word_list.add(end)
    word_list = list(word_list)
    word_list.sort()
    word_list_len = len(word_list)
    word_list_index = {word: i for i, word in enumerate(word_list)}
    graph = [[] for _ in range(word_list_len)]
    for i in range(word_list_len):
        for j in range(i + 1, word_list_len):
            if one_diff(word_list[i], word_list[j]):
                graph[i].append(j)
                graph[j].append(i)
    queue = [(0, begin, [begin])]
    visited = set()
    while queue:
        level, word, path = queue.pop(0)
        if word == end:
            return [path]
        if word in visited:
            continue
        visited.add(word)
        for i in graph[word_list_index[word]]:
            queue.append((level + 1, word_list[i], path + [word_list[i]]))
    return []