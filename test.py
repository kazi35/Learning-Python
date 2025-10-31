# def isPalindrome(x: int) -> bool:
    
#     if x < 0:
#         return False
    
#     s = str(x)
#     if(s == s[::-1]):
#         return True
#     else:
#         return False
    
    
    
# print(isPalindrome(1))


# nums =[1,1,-2,3,4,4,5,5,6]
# print("Firstly l: ",nums)
# List_into_tupple = tuple(nums)
# print("Tupple",List_into_tupple)
# tupple_to_dictionary = dict(List_into_tupple)
# print("Dictionart: ",tupple_to_dictionary)

    
    
def find_duplicates_set(nums):
   
    seen = set()
    duplicates = set()  
    
    for num in nums:
        print("Now num is:",num)
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
            
    return list(duplicates)


print(f"Example 1 (Set): {find_duplicates_set([0, 1, 1, 0])}")