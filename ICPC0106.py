class Solution:
    def __init__(self):
        self.base = {
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E', 
            15: 'F'
        }
    def solve(self, base, np):
        num = 0
        t = 0
        while np:
            num += np%10 * 2**t
            np //= 10
            t += 1
        res = str()
        while num:
            bas = num % base
            if bas >= 10:
                bas = self.base[bas]
            res += str(bas)
            num //= base
        return res[::-1]

Fishsauce = Solution()
for case in range(int(input())):
    ans = Fishsauce.solve(int(input()), int(input()))
    print(ans)