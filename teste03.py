def PalindromicSubstring(strParam):
    n = len(strParam)
    dp = [[False for _ in range(n)] for _ in range(n)]
    longest = ""

    for i in range(n):
        for j in range(i + 1):
            if strParam[j] == strParam[i] and (i - j <= 2 or dp[j + 1][i - 1]):
                dp[j][i] = True
                if i - j + 1 > len(longest):
                    longest = strParam[j: i + 1]
    return longest

strParam = input("Insira uma palavra: ")
print(PalindromicSubstring(strParam))