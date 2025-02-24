'''
Fishsauce
'''

def min_cost_to_reach_any_point(T, games):
    from math import gcd
    from collections import defaultdict
    import sys
    
    results = []
    
    for game in games:
        n, a, c = game
        gcd_cost_map = {0: 0}  # Dictionary to store minimum cost for each GCD
        
        for i in range(n):
            ai = a[i]
            ci = c[i]
            new_gcd_cost_map = defaultdict(lambda: sys.maxsize)
            for g, cost in gcd_cost_map.items():
                new_g = gcd(g, ai)
                new_cost = cost + ci
                if new_cost < new_gcd_cost_map[new_g]:
                    new_gcd_cost_map[new_g] = new_cost
            for g in new_gcd_cost_map:
                if g in gcd_cost_map:
                    gcd_cost_map[g] = min(gcd_cost_map[g], new_gcd_cost_map[g])
                else:
                    gcd_cost_map[g] = new_gcd_cost_map[g]
        
        if 1 in gcd_cost_map:
            results.append(gcd_cost_map[1])
        else:
            results.append(-1)
    
    return results

games = []
for _ in range(int(input())):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    c = list(map(int, input().strip().split()))
    games.append((n, a, c))

ans = min_cost_to_reach_any_point(T, games)
for ac in ans:
    print(ac)