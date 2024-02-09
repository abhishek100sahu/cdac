from icecream import ic

class HashTable:
    def __init__(self) -> None:
        self.MAX = 10
        self.array = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def get_prob(self, index):
        return [*range(index, len(self.array))] + [*range(0, index)]
    
    def  find_slot(self, key, index):
        prob_range = self.get_prob(index)
        # prob_range is [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]
        for prob_index in prob_range:
            if self.array[prob_index] is None:
                return prob_index
            if self.array[prob_index][0] == key:
                return prob_index
        raise Exception("HashMap FULL!")
    
    def __setitem__(self, key, value):
        h = self.get_hash(key=key)
        
        if self.array[h] is None:
            self.array[h] = (key, value)
        else:
            new_h = self.find_slot(key=key, index=h)
            self.array[new_h] = (key, value)
        ic(self.array)

    def __delitem__(self, key):
        h = self.get_hash(key=key)
        
        prob_range = self.get_prob(index=h)
        
        for prob_index in prob_range:
            if self.array[prob_index] is None:
                return
            if self.array[prob_index][0] == key:
                self.array[prob_index] = None

if __name__ == '__main__':
    h1 = HashTable()
    h1["qwe"]=324
    h1["gh"]=34
    h1["dfgh"]=32
    h1["mjh"]=4
    
    h1["gh"]=98766