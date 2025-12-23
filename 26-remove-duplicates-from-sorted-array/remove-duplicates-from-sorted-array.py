class Solution(object):
    def removeDuplicates(self, nums):
        i = 0 
        k = 0
        j = i + 1
        while j <= len(nums)-1:
            if nums [i] != nums [j]:
                nums[k] = nums[i]
                k = k + 1   
            i = i +1
            j = j + 1
        nums[k] = nums[j-1]
        return k+1
        