class Solution(object):
    def jump(self, nums):
        if len(nums) == 1:
           return 0
       
        jump = 0 
        current_end = 0 
        farthest_end = 0 
       
        for i in range(len(nums)-1):
           farthest_end = max(farthest_end,nums[i]+i)
           if i == current_end:
               jump += 1
               current_end = farthest_end
        return  jump