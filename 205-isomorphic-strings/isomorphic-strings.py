class Solution(object):
    def isIsomorphic(self, s, t):
        
        hs1 = {}
        hs2 = {}

        for i,j in zip(s,t):

            if i in hs1 and hs1[i] != j:
                return False
            
            if j in hs2 and hs2[j] != i:
                return False 

            hs1[i] = j
            hs2[j] = i

        return True

        