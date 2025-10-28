def longestCommonPrefix(strs: list[str]) :
   
    if not strs:
        return ""
    strs.sort()
    
    first_str = strs[0]
    last_str = strs[-1]
    
    common_prefix = []
    for i in range(len(first_str)):
        if i >= len(last_str) or first_str[i] != last_str[i]:
            break
        common_prefix.append(first_str[i])
        
    return "".join(common_prefix)



strs1 = ["flower", "flow", "flight"]
print(f"Input: {strs1}")
print(f"Output: '{longestCommonPrefix(strs1)}'") 


