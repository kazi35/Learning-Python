nameList=["Nashir","Alvi","Rimon","Subir","Rabbi","Anon","Shakib","Rafi","Saddam"];
print(nameList);
print(len(nameList));

numList=[11,22,33,44,55,66,77,88,99,111,122,133,144];
print(len(numList));

multiList=[11,"Name",'A',True,2.55,]    #Multi Type List#
print("\n     \n\n\n\n")
print(multiList);
print("\n")

thisList= list((1,"Nashir",'A',3.75));  #List constructor#
print(thisList)

#Acces List
print("\n");
print(thisList[1]);
print("\n");
print(nameList[3:4]);
print("\n");
print(nameList[3:]);
print("\n");
print(nameList[-9:-2]);
print("\n");
NameList=["Nashir","Alvi","Rimon","Subir","Rabbi","Anon","Shakib","Rafi","Saddam"];
if "Ball" in NameList:
  print("Yes,\"Ball is in the list\"");
else :
 print("No, Ball is not exist in the List");
 

 #Change Item Value
 print("\n\n\n");
 kList=["ab",22,22.5];
 kList[0]="Abu Bakar";
 print(kList);
 
 #Change a Range of Item Values
 print("\n");
 kList[1:]=["bb","cc"];
 print(kList)
 
 
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Insert Items

print("\n");
thatlist = ["apple", "banana", "cherry"]

thatlist.insert(1, "watermelon");#it increase list size#
print("\n");
print(thatlist);
print(len(thatlist))

#Add List Items
thatlist = ["apple", "banana", "cherry"]
thatlist.append("Bambbo");   #append add the element in the end of the list
print("\n");
print(thatlist);

#Extend List
tropical = ["mango", "pineapple", "papaya"];
thatlist = ["apple", "banana", "cherry"];
thatlist.extend(tropical);
print("\t");
print(thatlist)


#Remove List Items
thatlist = ["apple", "banana", "cherry"];
thatlist.remove("apple");
print("\n\n")
print(thatlist)
thatlist= ["mango", "pineapple", "papaya"];
thatlist.pop()   #pop remove last item
print("\n\n")
print(thatlist)
thatlist.pop(1)  #In this line pop remove the Esfesefic element 
print(thatlist)

thatlist = ["apple", "banana", "cherry"];
del thatlist[0:1] #del also remove specific element from the list
print("\n\n\n")
print(thatlist)


#Clear the List
thatlist = ["apple", "banana", "cherry"]; 
print("\n\n\n\n\n")
thatlist.clear()
if (len(thatlist)==0) :
    print("The list is empty");
    

#Loop Through a List
thatlist =["apple", "banana", "cherry"]; 

for x in thatlist:
 print(x);
 

#Loop Through the Index Numbers
thatlist =["apple", "banana", "cherry"]; 
print("\n\n\n\n")
for x in range(len(thatlist)):
    print(thatlist[x]);
    

#A short hand for loop that will print all items in a list:
thatlist =["apple", "banana", "cherry"]; 
print("----------------------------------------------------------------------------")
[print(x) for x in thatlist]


#List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if 'a' in x:
      newlist.append(x)
print("--------------------------------------------------------------------------")   
print(newlist)   

#in minimal way
newlist.clear()
newlist=[x for x in fruits if 'a' in x]
print("---------------------------------------------------------------------------------")
print(newlist)


newlist = [x.upper() for x in fruits]
print("--------------------------------------------------------------------------------------")
print(newlist)
print("--------------------------------------------------------------------------------------")
newlist=["FRUITS" for x in fruits] #what ever we gave it work with it
print(newlist)


#List sort
flistt=["orange", "mango", "kiwi", "pineapple", "banana"]
flistt.sort()  #by default it assending order
print("-------------------------------------------------------------")
print(flistt);
flistt.sort(reverse=True);
print("---------------------------------------------------------------------------")
print(flistt);