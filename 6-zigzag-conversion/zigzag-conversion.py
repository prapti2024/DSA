class Solution(object):
    def convert(self, s, numRows):

        arrs = [""] * numRows

        i = 0
        r = 0

        while i < len(s):
            
            while r < numRows and i < len(s):
                arrs[r] += s[i]
                r = r + 1
                i = i + 1
                
            r = r - 2 
            
            while r > 0 and i < len(s):
                arrs[r] += s[i]
                i = i + 1
                r = r - 1
                
        return("".join(arrs))