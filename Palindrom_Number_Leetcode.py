def palindrom(x : int) -> bool:
    max = 2**31 - 1  
    min = -2**31    
    sign = 1
    if x == 0:
        sign = 1
    if x < 0:
        sign = -1
        
    x_as_positive = abs(x)
    x_as_string = str(x_as_positive)
    x_as_reversed_string = x_as_string[len(x_as_string)-1 : : -1]
    x_as_int_again = int(x_as_reversed_string)
    final_look_of_x = x_as_int_again * sign
    if(x == final_look_of_x) :
        if final_look_of_x < min:
            return True
        if final_look_of_x> max:
            return True
        else:
            return False
    else:
        return False
    
    

print(palindrom(121))
    