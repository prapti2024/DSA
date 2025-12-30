class Solution(object):
    def hIndex(self, citations):
        count = 0 
        f = len(citations) + 1
        lst = [0] * f
        for i in range(len(citations)):
            if citations[i] <= len(citations):
                lst[citations[i]] += 1
            else:
                lst[f-1] += 1
        n = len(citations)
        while n >= 0:
            count += lst[n]
            if count >= n:
                return n 
            n = n - 1

                