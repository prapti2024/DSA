class Solution(object):
    def rob(self, nums):
        loot = nums

        if (len(nums) < 2):
            return nums[0]
            
        total_loot = [0] * len(loot)
        total_loot[0] = loot[0]
        total_loot[1] = max(loot[0],loot[1])

        for i in range(2,len(loot)):
            total_loot[i] = max((total_loot[i-2] + loot[i]),total_loot[i-1])
            
        return (total_loot[len(total_loot)-1])