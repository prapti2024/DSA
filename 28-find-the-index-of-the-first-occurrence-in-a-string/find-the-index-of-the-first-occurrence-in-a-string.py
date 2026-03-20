class Solution(object):
    def strStr(self, haystack, needle):
        n = len(needle)

        for i in range( len(haystack) - len(needle) + 1):

            if haystack[i:i+n] == needle:
                x = 1
                return i 
    
        return -1

        