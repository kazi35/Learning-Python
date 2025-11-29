class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        total = sum(nums)
        result= (total % k)
        return result