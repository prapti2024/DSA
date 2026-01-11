class Solution(object):
    def trap(self, height):
        arr = height[:]       
        newarr = height[:]    

        s1 = sum(height)

  
        i = 0
        while i < len(arr) - 1:
            if arr[i] > arr[i+1]:
                diff = arr[i] - arr[i+1]
                arr[i+1] += diff
            i += 1

       
        j = len(newarr) - 1
        g = newarr[j]
        while j > 1:
            if newarr[j-1] > g:
                g = newarr[j-1]
            newarr[j-1] += g - newarr[j-1]
            j -= 1

        
        compare = []
        for i in range(len(arr)):
            compare.append(min(arr[i], newarr[i]))

        s2 = sum(compare)

        return s2 - s1



s = Solution()
print(s.trap([4, 2, 0, 3, 2, 5]))  
