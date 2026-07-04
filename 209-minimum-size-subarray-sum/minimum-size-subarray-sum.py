class Solution(object):
    def minSubArrayLen(self, target, nums):
        low = 0 
        high = 0  
        current_sum = 0
        winsize = 10000000

        while (high<len(nums)):
            current_sum += nums[high]
            high += 1
            while (current_sum >= target):
                current_winsize = high-low
                winsize = min(winsize,current_winsize)
            
                current_sum = current_sum - nums[low]
                low += 1

        return (0 if winsize==10000000  else winsize)