class IntArray():

    def __init__(self, size):
        self.array = 0
        self.empty = True
        self.size = size
        self.items = 0

    def append(self, element):
        self.empty = False
        self.array = self.array * (10 ** self.size) + element
        self.items += 1

    @property
    def list(self):
        string = str(self.array)
        factor = self.size - (len(string) % self.size)
        result = "0" * (factor % self.size) + string
        if result == "0" * self.size and self.empty:
            return []
        list_result = []
        for i in range(len(result) // self.size):
            lower = i * self.size
            upper = (i + 1) * self.size
            sub = result[lower : upper]
            list_result.append(int(sub))
        return list_result
        
    def __str__(self):
        return str(self.list)
        
    def pop(self):
        if len(str(self)) <= self.size:
            self.empty = True
        self.array = self.array // (10 ** self.size)
        self.items -= 1
        
    def __getitem__(self, index):
        return self.list[index]
