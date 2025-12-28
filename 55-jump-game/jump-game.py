class Solution(object):
    def canJump(self, nums):
        finalpos = len(nums)-1
        i = len(nums)-2
        while i >= 0:
            if nums[i] + i >= finalpos:
                finalpos = i
            i = i - 1
        return finalpos == 0
        
        