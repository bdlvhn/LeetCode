class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        arr_len = len(tickets) + 1

        def dfs(route: List[str], tickets: List[List[str]]) -> List[str]:
            if not tickets:
                return route
            for i, d in enumerate(tickets):
                fr, to = d
                if fr == route[-1]:
                    temp = dfs(route + [to], tickets[:i] + tickets[i+1:])
                    if temp and len(temp) == arr_len:
                        return temp

        return dfs(["JFK"], tickets)