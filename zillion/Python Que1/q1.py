'''
1) For a input of two strings X and Y, find the minimum number of steps required to convert X to Y. (each operation is counted as 1 step.)
You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example:
Input 1:
X = "abad"
Y = "abac"

Output 1:
1

Explanation 1:
Operation 1: Replace d with c.

Input 2:
X = "Insa"
Y = "India"

Output 2:
2

Explanation 2:
=> Operation 1: Replace s with d.
=> Operation 2: Insert i.
'''

def levenshtein_algorithm(x, y):
    row = len(x)
    col = len(y)
    dp = [[0] * (col + 1) for _ in range(row + 1)]
    dp = [[0 for _ in range(col+1)] for _ in range(row+1)]
    # print(dp)

    for i in range(row + 1):
        dp[i][0] = i
    for j in range(col + 1):
        dp[0][j] = j

    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],  # Delete
                                   dp[i][j - 1],  # Insert
                                   dp[i - 1][j - 1])  # replace
 
    return dp[row][col]

str1 = "abad"
str2 = "abac"

print(levenshtein_algorithm(str1, str2)) 

str1= "Insa"
str2 = "India"

print(levenshtein_algorithm(str1, str2))  

