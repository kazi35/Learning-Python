class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        seen = set()
        duplicate = set()
        
        for num in nums:
            
            if num in seen:
                duplicate.add(num)
            else:
                seen.add(num)
        
        return list(duplicate)
    
 
 
 
if __name__ == "__main__":
    
    my_nums = [1, 1, 3, 3, 5, 6]
    solve= Solution()
    print("final output: ",solve.getSneakyNumbers(my_nums))
        