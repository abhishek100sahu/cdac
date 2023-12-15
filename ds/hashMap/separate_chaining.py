from icecream import ic


class hashNode:
    def __init__(self):
        self.MAX_NODES = 10
        self.array = [[] for i in range(self.MAX_NODES)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX_NODES

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.array[h]):
            if len(element) == 2 and element[0] == key:
                self.array[h][idx] = (key, value)
                found = True
                ic("yay")
                ic(idx, element)
        if not found:
            self.array[h].append((key, value))

    def __print_array__(self):
        ic(self.array)

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.array[h]):
            if element[0] == key:
                del self.array[h][idx]

    def __getitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.array[h]):
            if element[0] == key:
                return self.array[h][idx][1]


obj = hashNode()

obj["march 1"] = 230
obj["march 2"] = 561
obj["march 3"] = 482
obj["march 4"] = 777
obj["march 5"] = 230
obj["march 6"] = 561
obj["march 7"] = 482
obj["march 8"] = 777
obj["march 9"] = 230
obj["march 10"] = 561
obj["march 11"] = 482
obj["march 12"] = 777
obj["march 13"] = 230
obj["march 14"] = 561
obj["march 15"] = 482
obj["march 16"] = 777
obj["march 1"] = 230
obj["march 18"] = 561
obj["march 19"] = 482
obj["march 20"] = 777
obj["march 1"] = 482
obj["march 22"] = 777
obj["march 23"] = 230
obj["march 24"] = 561
obj["march 25"] = 482
obj["march 26"] = 777
obj["march 27"] = 230
obj["march 28"] = 561
obj["march 29"] = 482
obj["march 30"] = 777

obj.__print_array__()

del obj["march 10"]
obj.__delitem__("march 26")

obj.__print_array__()
ic(obj.__getitem__("march 5"))
