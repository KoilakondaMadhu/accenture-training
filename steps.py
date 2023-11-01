# alice clibs a staircasr takes N steps to reach the Top .in each turn ,Alice can climb 1 or M stairs. Find the minmum number of climb to reach the top i.e nth stair
# input Format:
# the first line contains two space separated integers N and M
# OUtput Format
# Print the numbers the minimum number of clims required to reach the top 
# Constraints:
# 1<= N <= 10^g
# 1 <= M <= 10^9
# Example
# input
# 5 1
# output
# 5
# Explanation
# Alice can reach the top by 0 -> 1 -> 2 ->3 -> 4-> 5

# input 
# 6 4
#  Output 
# 3

# ask for accenture----------------------==========================---------------


n,m = map(int,input().split())
print(n//m+n%m)
