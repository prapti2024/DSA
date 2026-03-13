class Solution(object):
    def romanToInt(self, s):
        hash_table = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        arr = []
        i = 0
        while i < len(s):
            if i<len(s)-1 and hash_table.get(s[i]) < hash_table.get(s[i+1]):
                d = hash_table.get(s[i+1]) - hash_table.get(s[i])
                arr.append(d)
                i += 2
            else:
                    arr.append(hash_table.get(s[i]))
                    i = i + 1
        return sum(arr)