class Solution(object):
    def canConstruct(self, ransomNote, magazine):
      
            mydict1 = {}
            flag = 0 
            
            for i in magazine:
                mydict1[i] = mydict1.get(i,0) + 1
    
            for i in ransomNote:
                mydict1[i] = mydict1.get(i,0) - 1

            for i in mydict1:
                if mydict1[i]<0:
                   flag = 1
                
            if flag > 0:
                return False
            else:
                return True