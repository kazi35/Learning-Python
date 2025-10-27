def lengthOfLastWord(s: str) -> int:
    
    length = 0

    for i in range(len(s) - 1, -1, -1):
        char = s[i]
        
        if char != ' ':
            length += 1
        else:
            if length > 0:
                return length
           
            
   
    return length

print(lengthOfLastWord("Nasir is a good Guy"))