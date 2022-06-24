✅ [Python] Simple Solution w/ Explanation | DP

Given an array of `words`, we need to find the length of the ***longest possible word chain***. I will use some terms whose definitions are given in the problem statement without explaining them here.

How should we approach this problem? 🤔
The first thing which comes into mind is **DP**. There are a few reasons for this thought.

- It asks for **longest** possible word chain, so it is an optimization problem.
- The chain is built by adding a word which only one letter added anywhere to it. So, it can be broken down into subproblems.

___
✅ **Solution I: Bottom-Up DP [Accepted]**

Generally, we need to think of a recursive relation in a DP problem and then optimize it. But here, it wasn't required. Can we start with the shortest word and try to build a chain starting with it? Let's think in this direction. We then need to find the next shortest word and so on. It could be expensive, so *sorting* the entire array based on length will help.

Let `prev` be the predecessor of a word. Building a successor from `prev` will be more expensive than building a predecessor from that word. The following example will make it clear:

```text
prev = "chain"
To build all possible successors, we need to add a letter anywhere in the word.
_ c _ h _ a _ I _ n _
We have 6 possible spaces and 26 possible letters, so a total of 6 * 26 possibilities.

Now, getting a predecessor from a word is a lot easier. Just remove a letter.
word = "chains"
pred = {"hains", "cains", "chins", "chans", "chais", "chain"}
```

So, for each word, we'll look for a predecessor. Wouldn't it be great if can have a *data structure* with the following two properties: 

- Can tell which of these predecessors are present in the array.
- Size of the chain ending with that predecessor.

Turns out that we already have one. It is `unordered_map` is `C++` and `dictionary` in python.

Now with these ideas in mind, we are ready to code!

```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        res = 1
        for word in sorted(words, key=len):
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1 :]
                if prev in dp:
                    dp[word] = dp[prev] + 1
                    res = max(res, dp[word])

        return res
```

- **Time Complexity:** `O(nlog(n) + nll)`
  - `O(nlog(n))` for sorting
  - `O(n*l*l)`: `n` for each loop, `l` for inner loop and `l` for string concatenation.
- **Space Complexity:** `O(ns)`
  - `O(n)` for sorting and storing in dictionary.
  - `O(ns)`: `s` for creating space for `word`, `n` times. 

___
___
If you like the solution, please **upvote**! 🔼
For any questions, or discussions, comment below. 👇️
