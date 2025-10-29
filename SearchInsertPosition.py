
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        return self._binarySearch(nums, target, 0, len(nums) - 1)

    def _binarySearch(self, nums: list[int], target: int, left: int, right: int) -> int:
        if left > right:
            return left

        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        if target > nums[mid]:
            return self._binarySearch(nums, target, mid + 1, right)
        else:
            return self._binarySearch(nums, target, left, mid - 1)
        
        
        
if __name__ == "__main__":
   
    s = Solution()
    
    my_nums = [1, 3, 5, 6]
    
    target1 = 5
    index1 = s.searchInsert(my_nums, target1)
    print(f"List: {my_nums}, Target: {target1} -> Output Index: {index1}")  # Expected: 2