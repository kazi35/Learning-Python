a_int = 100

print("First look of our interger:  ",a_int)
sign=1
if(a_int < 0):
    sign = -1
    
print("Sign is :",sign)
a_positive = abs(a_int)
print("after applying Absuluate function: ",a_positive)
a_str = str(a_positive)
print("After make the iteger as a String: ",a_str)
a_reverse = a_str[len(a_str)-1 : : -1]
print("After make the string reverse: ",a_reverse)
a_again_int = int(a_reverse)
print("After make the string into integer : ",a_again_int)
a_final_look = a_again_int * sign
print("final look of a: ",a_final_look)