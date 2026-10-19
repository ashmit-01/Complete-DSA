class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return (self.is_Pal(s, left+1, right)
                or self.is_Pal(s, left, right-1))
            left += 1
            right -= 1
        return True    


    def is_Pal(self ,s: str, left: int, right: int):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True        
                     
        