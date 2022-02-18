class IntArray():

    def __init__(
        self,
        iterable = None,
        items_size = 1,
        auto_resize = True,
        force_no_use_builtin_list = True
    ):
        self.array = 0
        self.empty = True
        self.items_size = items_size
        self.items = 0
        self.auto_resize = auto_resize
        self.dont_use_builtin_list = force_no_use_builtin_list

        for element in iterable:
            self.append(element)

    def __getitem__(self, index):

        if self.dont_use_builtin_list:
            lower = self.items_size * index
            upper = self.items_size * (index + 1)

            return self.__format_array__()[lower : upper]

        return self.list[index]

    def __setitem__(self, index, value):
        pass

    def __len__(self):
        return self.items

    def __str__(self):
        if self.dont_use_builtin_list:
            return self.str_without_builtin_lists
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

    def clear(self):
        self.array = 0
        self.items = 0
        self.empty = True

    def __format_array__(self):
        string = str(self.array)
        factor = self.items_size - (len(string) % self.items_size)
        result = "0" * (factor % self.items_size) + string

        if result == "0" * self.items_size and self.empty:
            return ""

        return result

    @property
    def str_without_builtin_lists(self):
        result = self.__format_array__()

        if result == "":
            return "[]"

        str_result = "["

        last_iteration = len(result) // self.items_size - 1

        for i in range(last_iteration + 1):
            lower = i * self.items_size
            upper = (i + 1) * self.items_size

            sub = result[lower : upper]

            str_result += sub

            if i != last_iteration:
                str_result += ", "

            else:
                str_result += "]"

        return str_result

    @property
    def list(self):
        result = self.__format_array__()

        if result == "":
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

class FloatArray(IntArray):

    def __init__(
        self,
        iterable = None,
        items_size = 1,
        tail_size = 1,
        auto_resize = True,
        auto_tail_resize = True
    ):
        self.tail_size = tail_size
        self.auto_tail_resize = auto_tail_resize
        super().__init__(iterable, items_size, auto_resize)
        
    def auto_grow_tail(self, item):

        if self.auto_tail_resize:
            str_item = str(item)
            item_tail = str_item.split(".")[1]

            tail_len = len(item_tail)

            if tail_len > self.tail_size:
                self.tail_size = tail_len
    
    def append(self, element):
        self.auto_grow_tail(element)
        amplificator = 10 ** self.tail_size

        super().append(element * amplificator)
