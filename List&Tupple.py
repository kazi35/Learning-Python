#Now time to learn About LIST in Python
#List it miutable or we can say modifieable not like as String

student= ["Nashir", 24,"DSC"]
print(student[-3:])
print(student[0:])
student[0]="MR_KZ" #We can modifed or reassign any value
print(student[-3:-1])

#Now it's time to learn some Function/ Method about LIST

#Append [Add one element at the end of the of the list]
student.append("Home Town: Rajbari")
print(student)

# Sort [Sorting the list]
age=[10,5,18,19,20,21,22,9,7]
age.sort()
age.sort(reverse=True) #Desending Order
print(age)

#Reverse Method
age.reverse()
print(age)

#Insert
age.insert(len(age)-len(age),"Inserted") #['Inserted', 5, 7, 9, 10, 18, 19, 20, 21, 22]
print(age)

#Remove [It remove the first occures of elements]
age.remove("Inserted")

#pop [remove element at index]
print(age)
age.pop(2)
print(age)
