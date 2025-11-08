class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        from bisect import bisect_left
        for num1_idx, num1 in enumerate(numbers):
            num2 = target - num1
            num2_idx = bisect_left(numbers[num1_idx+1:], num2) + (num1_idx+1)
            if numbers[num2_idx] == num2:
                return [num1_idx+1, num2_idx+1]
