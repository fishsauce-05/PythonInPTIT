from collections import defaultdict as df
class Solution:
	def solve(self):
		
Fishsauce = Solution()
for case in range(int(input())):
	v, e = map(int, input().split())
	adj = df(list)
	for i in range(e):
		x, y = map(int, input().split())
		adj[x].append(y)
		adj[y].append(x)
	
	print(Fishsauce.solve())