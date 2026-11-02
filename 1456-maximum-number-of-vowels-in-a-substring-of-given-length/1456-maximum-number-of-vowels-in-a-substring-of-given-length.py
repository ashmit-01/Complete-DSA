class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        holder = [c in {'a','e','i','o','u'} for c in s]
        count = MaxCount = sum(holder[:k])
        for i in range(len(s)-k):
            count += holder[i+k] - holder[i]

            if count > MaxCount:
                MaxCount = count
        return MaxCount        
        