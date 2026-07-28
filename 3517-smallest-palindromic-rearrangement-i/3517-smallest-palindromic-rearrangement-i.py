from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        freq = Counter(s)
        left = ""
        middle = ""
# Get all the alphabets in ascending order
        for i in range(26):
            ch = chr(ord('a')+i)
# check if that ch is present in freq
            if ch in freq:
                left += ch * (freq[ch]//2)

                if freq[ch]%2 == 1:
                    middle = ch

        return left + middle + left[::-1]



        