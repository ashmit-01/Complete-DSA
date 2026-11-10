class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        letters.sort()
        for st in letters:
            if st > target:
                return st
        return letters[0]    

        