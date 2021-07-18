class MyHashMap:
    
    def __init__(self):
        self.table = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.table)):
            if key == self.table[i][0]:
                self.table[i][1] = value
                return
        self.table.append([key, value])

    def get(self, key: int) -> int:
        for i in range(len(self.table)):
            if key == self.table[i][0]:
                return self.table[i][1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.table)):
            if key == self.table[i][0]:
                self.table.remove(self.table[i])
                return