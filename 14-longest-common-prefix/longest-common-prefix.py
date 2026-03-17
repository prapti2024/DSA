class Solution(object):
    def longestCommonPrefix(self, strs):

        prefix = ""

        for x in range(len(min(strs,key = len))):
            char = strs[0][x]
    
            if all(s[x] == char for s in strs):
                prefix += char
            else:
                 break
        return(prefix)