def reverse_words(s):
    word_ls = s.split()
    word_ls.reverse()
    return " ".join(word_ls)