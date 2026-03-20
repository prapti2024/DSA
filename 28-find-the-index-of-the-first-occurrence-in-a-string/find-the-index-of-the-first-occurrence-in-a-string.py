class Solution(object):
    def strStr(self, haystack, needle):
        n = len(needle)
        x = -1 
        i = 0 

        while i < len(haystack):

            word = haystack[i:i+n]

            if word == needle:
                x = 1
                return i 
                break

            i = i + 1
        return x 

        