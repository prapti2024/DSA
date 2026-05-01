class Solution(object):
    def isSubsequence(self, s, t):
        i = 0 
        j = 0 
        snew = []

        while i < len(s) and j < len(t):
            p1 = s[i]
            while j < len(t):
                p2 = t[j]
                if p1 == p2:
                    snew.append(p1)
                    i = i + 1
                    j  = j + 1
                    break
                j = j + 1

           
        if (''.join(snew)==s):
            return True
        else:
            return False
            