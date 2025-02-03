class Solution:
    def solve(self, code):
        result = []
        i = 0
        n = len(code)

        while i < n:
            char = code[i]
            i += 1
            freq = 0
            while i < n and code[i].isdigit():
                freq = freq * 10 + int(code[i])
                i += 1
            result.append(char * freq)
        
        return ''.join(result)

Fishsauce = Solution()
t = int(input())
for _ in range(t):
    code = input().strip()
    print(Fishsauce.solve(code))