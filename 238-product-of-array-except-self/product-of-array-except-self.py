
class Solution(object):
    
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = 1
        suffix = 1
        prods = [1]*len(nums)

        for i in range(len(nums)):
            prods[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            prods[i] *= suffix
            suffix *= nums[i]
        
        return (prods)
        