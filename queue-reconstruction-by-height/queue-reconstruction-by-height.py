class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        people = collections.deque(people)
        queue = []
        while people:
            now = people.popleft()
            if not queue:
                queue.append(now)
            else:
                if queue[-1][0] == now[0]:
                    queue.append(now)
                else:
                    if now[1] == 0:
                        queue = [now] + queue
                    else:
                        queue.insert(now[1],now)
        return queue