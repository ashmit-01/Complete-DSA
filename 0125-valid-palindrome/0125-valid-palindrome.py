
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # Left side par non-alphanumeric characters skip karo
            if not s[left].isalnum():
                left += 1

            # Right side par non-alphanumeric characters skip karo
            elif not s[right].isalnum():
                right -= 1

            # Characters ko case-insensitive compare karo
            elif s[left].lower() != s[right].lower():
                return False

            # Match hone par dono pointers move karo
            else:
                left += 1
                right -= 1

        return True
