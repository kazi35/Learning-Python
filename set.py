collec ={1,2,3,4,5}
print(collec)
print(type(collec))
#set always unique value

#empty set
col ={}
print(type(col))
col = set()
print(type(col))


#method of set
collec.add(6)
print(collec)
collec.remove(6)
print(collec)

collec.pop() #random values
print(collec)
print(len(collec))
collec.clear()
print(len(collec))


#.union & .intersection
set1={1,2,3}
set2={3,4,5}

print(set1.union(set2))
print(set1)
print(set2)
print(set1.intersection(set2))