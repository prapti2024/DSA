import random
class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.hashmap = {}
        self.seed = 1

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hashmap:
            return False 
        self.nums.append(val)
        self.hashmap[val] = len(self.nums) -1 
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hashmap:
            self.nums.remove(val)
            del self.hashmap[val]
            return True 
        return False
        

    def getRandom(self):
       return random.choice(self.nums)