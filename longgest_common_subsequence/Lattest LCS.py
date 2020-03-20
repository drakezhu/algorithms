class Solution(object):
    
        def shortestCommonSupersequence(self, str1, str2):
            i = j = 0
                m = len(str1)
                n = len(str2)
                l = [[0 for i in range(n+1)] for j in range(m+1)] 
                
                def LCSLength(X,Y,m,n):
                    for i in range(1,m+1):
                        for j in range(1,n+1):
                            if X[i-1] == Y[j-1]:
                                l[i][j] = l[i-1][j-1]+1
                            else:
                                l[i][j] = max(l[i-1][j],l[i][j-1])
                
                def LCS(X, Y, m, n):
                    if m == 0 or n == 0:
                        return ""
                    if X[m-1] == Y[n-1]:
                        return LCS(X,Y,m-1,n-1) + X[m-1]
                    if l[m-1][n] > l[m][n-1]:
                        return LCS(X,Y,m-1,n)
                    else:
                        return LCS(X,Y,m,n-1)
                
                LCSLength(str1,str2,m,n)

                lcs = LCS(str1,str2,m,n)
                print x
                
                
                
'''
lee's method
'''
def lcs(A, B):
    n, m = len(A), len(B)
    dp = [["" for _ in xrange(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if A[i] == B[j]:
                dp[i + 1][j + 1] = dp[i][j] + A[i]
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
    return dp[-1][-1]