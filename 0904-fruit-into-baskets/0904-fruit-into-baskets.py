
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:

        left = 0
        max_length = 0
        basket = {}

        for right in range(len(fruits)):

            # Add current fruit
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            # Shrink if more than 2 types
            while len(basket) > 2:

                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]

                left += 1

            # Update maximum window
            max_length = max(max_length, right - left + 1)

        return max_length
