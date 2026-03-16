class Solution(object):
    def intToRoman(self, num):
        symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        ans = []

        for i in range(13):
            while num >= values[i]:
                ans.append(symbols[i])
                num = num - values[i]
        
        return(''.join(ans))
        


        