from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        def f(i: int, j: int, acc: int) -> int:
            if j >= len(nums):
                return acc

            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                return f(i + 1, j + 1, acc + 1)

            return f(i, j + 1, acc)

        return f(0, 1, 1)

class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        i, j = 0, 0

        while j <= len(nums) - 1:
            ch = nums[j]
            j += 1

            while j < len(nums) and nums[j] == ch:
                j += 1

            nums[i] = ch
            i += 1

        return i