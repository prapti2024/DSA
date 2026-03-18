class Solution(object):
    def reverseWords(self, s):
        words = ""
        wlist = []

        for i in range(len(s)):
            if s[i] == " ":
                wlist.append(words)
                words = ""
            else:
                words+=s[i]
   
        wlist.append(words)

        i = 0 
        j = len(wlist)

        while i < j:
            temp = wlist[i] 
            wlist[i] = wlist[j-1]
            wlist[j-1] = temp
            i = i + 1
            j = j - 1
    
        final = ""

        new_arr = []

        for i in range(len(wlist)):
             if wlist[i] != '':
                 new_arr.append(wlist[i])
       
        return(' '.join(new_arr))
        