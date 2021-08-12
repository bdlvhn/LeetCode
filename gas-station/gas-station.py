class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            if gas[i] < cost[i]:
                continue

            amt = 0
            cur, cnt = i, 0
            while cnt < n:
                amt += (gas[cur] - cost[cur])
                if amt < 0:
                    break
                cur = (cur + 1) % n
                cnt += 1

            if amt >= 0:
                return i
        return -1