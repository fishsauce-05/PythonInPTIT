class Solution:
    def solve(self, xau):
        code = []
        curX = 1 
        c_code = xau[0]
        for x in xau[1:]:
            if c_code == x:
                curX += 1 
            else:
                code.append(str(curX) + str(c_code))
                c_code = x
                curX = 1
        code.append(str(curX) + str(c_code))
        return ''.join(code)
        
t = int(input())
for cases in range(t):
    xau = input()
    Fishsauce = Solution()
    print(Fishsauce.solve(xau))