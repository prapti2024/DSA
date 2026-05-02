class Solution(object):
    def twoSum(self, numbers, target):
        hashmap = {}

        for i,val in enumerate((numbers)):
            diff = target - numbers[i]
            if diff in hashmap:
               return (hashmap[diff]+1,i+1)
            else:
                hashmap[val] = i
        