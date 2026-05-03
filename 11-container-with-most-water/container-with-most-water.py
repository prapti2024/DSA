class Solution(object):
    def maxArea(self, height):
        water = 0 
        left = 0 
        right = len(height) - 1

        while (left < right):
            water = max(water,min(height[left]*(right-left),height[right]*(right-left)))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1 
                
        return water
                