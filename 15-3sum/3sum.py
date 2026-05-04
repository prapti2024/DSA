class Solution(object):
    def threeSum(self, nums):
        sortedarr = sorted(nums) #timsort
        result = []
        for i in range(len(sortedarr)-2):
            if i > 0 and sortedarr[i] == sortedarr[i - 1]:
                continue
            
            l = i + 1
            r = len(sortedarr) - 1
            while l < r:

                total = sortedarr[i] + sortedarr[l] + sortedarr[r]
                
                if total == 0:
                    result.append([ sortedarr[i] , sortedarr[l] , sortedarr[r] ])
                    
                    while l < r and sortedarr[l] == sortedarr[l+1]:
                        l = l + 1
                    
                    while l < r and sortedarr[r] == sortedarr[r-1]:
                        r = r - 1
                        
                    l += 1
                    r -= 1
                elif total < 0:
                    l = l + 1
                else:
                    r = r - 1
            
        return(result)