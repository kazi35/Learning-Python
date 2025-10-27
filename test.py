def isPalindrome(x: int) -> bool:
    
    if x < 0:
        return False
    
    s = str(x)
    if(s == s[::-1]):
        return True
    else:
        return False
    
    
    
print(isPalindrome(120))

