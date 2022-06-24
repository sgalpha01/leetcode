from collections import deque


def ladder_len(begin_word, end_word, word_list):
    word_list = set(word_list)
    stack = deque([[begin_word, 1]])
    steps = 0
    alpha = [chr(i) for i in range(ord("a"), ord("z") + 1)]
    while stack:
        word, steps = stack.popleft()
        if word == end_word:
            return steps
        for i in range(len(word)):
            for c in alpha:
                next_word = word[:i] + c + word[i + 1 :]
                if next_word in word_list:
                    word_list.remove(next_word)
                    stack.append([next_word, steps + 1])

    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(ladder_len(beginWord, endWord, wordList))
