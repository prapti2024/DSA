class Solution(object):
    def lengthOfLastWord(self, s):
        arr = s.split()
        nth_word = arr[-1]
        return len(nth_word)
        