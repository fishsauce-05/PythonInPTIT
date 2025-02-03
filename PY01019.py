class Solution:
    def solve(self, s1):
        s2 = s1[::-1]
        n = len(s1)
        for i in range(1, n):
            if abs(ord(s1[i]) - ord(s1[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1])):
                return "NO"
        return "YES"

Fishsauce = Solution()
t = int(input())
for cases in range(t):
    strS1 = input()
    print(Fishsauce.solve(strS1))