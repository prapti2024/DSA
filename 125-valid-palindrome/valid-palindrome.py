class Solution(object):
    def isPalindrome(self, s):
        snew = []

        n = len(s) 

        for i in range(n):
            if s[i].isalnum():
                snew.append(s[i])

        final1 = ''.join(snew).lower()
            
        i = len(snew)-1

        news = []

        while i >= 0 :
            news.append(snew[i])
            i = i - 1
            
        final2 = ''.join(news).lower()
    
        if final1 == final2:
            return True
        else:
            return False


        