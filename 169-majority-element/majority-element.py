class Solution(object):
    def majorityElement(self, nums):
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1
        return(max(hashmap,key = hashmap.get))
        