class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        lastSeen = -1

        for i in range(len(nums)):
            if nums[i] == 1:
                if lastSeen != -1:
                    if (i - lastSeen) <= k:
                        return False
                lastSeen = i
        return True
