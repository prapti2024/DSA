class Solution(object):
    def wordPattern(self, pattern, s):
        lst = s.split()
        hs1 = {}
        hs2 = {}
        
        if len(pattern) != len(lst):
           return False

        for i,j in zip(pattern,lst):
            if i in hs1 and hs1[i] != j:
                return False
            if j in hs2 and hs2[j] != i:
                return False

            hs1[i] = j 
            hs2[j] = i

        return True
        