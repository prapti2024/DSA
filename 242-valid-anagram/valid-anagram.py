class Solution(object):
    def isAnagram(self, s, t):
        
        sum = 0 
        count1 = {}
        count2 = {}
        
        
        for i in s:
            count1[i] = count1.get(i,0)+1
            
            
        for j in t:
            count2[j] = count2.get(j,0)+1
            
         
        if count1 == count2:
            return True
        else:
            return False       