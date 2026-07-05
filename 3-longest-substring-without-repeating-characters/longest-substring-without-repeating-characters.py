class Solution(object):
    def lengthOfLongestSubstring(self, s):
        setitems = set()
        l = 0 
        res = 0 

        for r in range(len(s)):
            while s[r] in setitems:
                setitems.remove(s[l])
                l += 1    
            setitems.add(s[r])
            res = max(res,r-l+1)
        
        return res
    
        

        