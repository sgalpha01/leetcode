def reverse_words(s):
    return " ".join(i[::-1] for i in s.split())


s = "Let's take LeetCode contest"
print(reverse_words(s))