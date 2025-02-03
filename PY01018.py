class Solution:
    def __init__(self):
        self.strP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
    def solve(self, k, xauS):
        n = len(xauS)
        lstS = []
        
        for i in range(n):
            idx = self.strP.find(xauS[i])
            lstS.append(self.strP[(idx+k)%28])
        lstS.reverse()
        return lstS
    
Fishsauce = Solution()
while True:
    inputs = [x for x in input().split(' ')]
    if inputs[0] == '0':
        break
    k = int(inputs[0])
    xauS = inputs[1]
    print(Fishsauce.solve(k, xauS))