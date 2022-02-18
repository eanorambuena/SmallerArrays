class IntArray():

    def __init__(self, iterable = None, items_size = 1, auto_resize = True):
        self.array = 0
        self.empty = True
        self.items_size = items_size
        self.items = 0
        self.auto_resize = auto_resize

        for element in iterable:
            self.append(element)

    def __getitem__(self, index):
        return self.list[index]

    def __len__(self):
        return self.items

    def __str__(self):
        return str(self.list)

    def auto_grow(self, item):

        if self.auto_resize:
            item_len = len(str(item))

            if item_len > self.items_size:
                self.items_size = item_len

    def append(self, element):
        self.empty = False
        self.auto_grow(element)
        self.array = self.array * (10 ** self.items_size) + element
        self.items += 1

    @property
    def list(self):
        string = str(self.array)
        factor = self.items_size - (len(string) % self.items_size)
        result = "0" * (factor % self.items_size) + string

        if result == "0" * self.items_size and self.empty:
            return []

        list_result = []

        for i in range(len(result) // self.items_size):
            lower = i * self.items_size
            upper = (i + 1) * self.items_size

            sub = result[lower : upper]

            list_result.append(int(sub))

        return list_result
        
    def pop(self):
        if len(str(self)) <= self.items_size:
            self.empty = True
        self.array = self.array // (10 ** self.items_size)
        self.items -= 1

    @property
    def size(self):
        import sys
        return sys.getsizeof(self)
