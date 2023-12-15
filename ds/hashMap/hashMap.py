from icecream import ic


class hashNode:
    def __init__(self):
        self.MAX_NODES = 100
        self.array = [None for _ in range(self.MAX_NODES)]
        ic(self.array)

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX_NODES

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.array[h] = value

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.array[h] = None

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.array[h]


object_1 = hashNode()

object_1.__setitem__("Name", "Abhishek Sahu")
object_1.__setitem__("dob", "2 april")

ic(object_1.__getitem__("Name"))
ic(object_1.__delitem__("Name"))
ic(object_1.__getitem__("Name"))
del object_1["dob"]
ic(object_1["dob"])
