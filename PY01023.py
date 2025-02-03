class Solution:
    def solve(self, num):
        factors = ['1']
        original_num = num
        for i in range(2, int(num**0.5) + 1):
            pow = 0
            while num % i == 0:
                pow += 1
                num //= i
            if pow != 0:
                factors.append(f"{i}^{pow}")
        if num > 1:
            factors.append(f"{num}^1")
        if not factors:
            factors.append(f"{original_num}^1")
        return ' * '.join(factors)

t = int(input())
for cases in range(t):
    num = int(input())
    Fishsauce = Solution()
    print(Fishsauce.solve(num))