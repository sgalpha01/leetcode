class Solution:
    def word_gt(self, word1, word2, order):
        m, n = len(word1), len(word2)
        word1 += "#" * (n - m)
        word2 += "#" * (m - n)
        for i in range(len(word1)):
            if order.index(word1[i]) > order.index(word2[i]):
                return True
            if order.index(word1[i]) < order.index(word2[i]):
                return False

        return False

    def isAlienSorted(self, words, order: str) -> bool:
        order = "#" + order
        for i in range(1, len(words)):
            if self.word_gt(words[i - 1], words[i], order):
                return False
        return True


alien_dict = Solution()

words = ["word", "world", "row"]
order = "worldabcefghijkmnpqstuvxyz"
print(alien_dict.isAlienSorted(words, order))
