class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = dict()
        left = 0
        right = 0
        result = 0

        while right < len(s):
            if s[right] in hashmap:
                left = max(hashmap[s[right]]+1,left)
            hashmap[s[right]] = right
            result = max(result,(right-left)+1)
            right += 1
        return result        