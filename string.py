#Here we go all about String in Python

st1= 'here we go'
st2= "here we go"
st3= '''here we go'''
# Here we see three diffrent type of cotation to creat String.

#Scape Sequence Character
st4= "Hello there.\nWe will learn About Python Scape Sequence Characters in this line"
#\n for newline
# \t for tab space
#print(st4)  

#Now concatanation 
st5="MD"
st7=" NASHIR"
st6=" KAZI"
#print(st5+st7+st6)
#print(len(st6)) #Findout the the Length of string

# Now time to learn Indexing in python

#print(st5[0]) # from left side started with zero "0"
#print(st7[-3]) # from right side started with zero "-1"

# Slicing in Python

'''
print(st1[0:4])
print(st1[5:10])
print(st1[:10]) # 0 to 10th characters
print(st6[-5:len(st6)])
'''
# String Function in Python
print(st5.endswith("D")) #st5="MD"
st8="i am a student"
st8= st8.capitalize() # Permanently capitalize firstletter of main string
print(st8.capitalize()) # The first letter will be capitalize for a while not in the original string

#Some string function 
st8.count()
st8.find()