class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            fuel = 0
            for j in range(n+1):
                loc = (i + j) % n
                fuel += gas[loc]
                if fuel - cost[loc] < 0:
                    fuel -= cost[loc]
                    break
                else:
                    fuel -= cost[loc]
            if fuel >= 0:
                return i
        return -1