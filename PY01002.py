class Solution:
	def solve(self, equation):
		pos = equation.find('=')
		expression = equation[:pos]
		result = list(equation.split())[-1]
		if eval(expression) == int(result):
			return "YES"
		return "NO"

equation = input()
fishsauce = Solution()
print(fishsauce.solve(equation))