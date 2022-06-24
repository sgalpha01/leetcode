def generateParenthesis(n):
    def helper(curr, l, r, arr=[]):
        if r >= l >= 0:
            if r == 0:
                arr.append(curr)
            helper(curr + "(", l - 1, r)
            helper(curr + ")", l, r - 1)

        return arr

    return helper("", n, n)


print(generateParenthesis(3))
