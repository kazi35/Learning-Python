dik ={
    "name": "Nashir",
    "cgpa": 3.62,
    "course":["se411","se11","SE433"]
}
print(dik["name"])
print(dik["cgpa"])
print(dik["course"])
print(dik)
dik["name"]="MD NASHIR"
print(dik["name"])

null_dik={} #NULL dictonary
print(null_dik)

#Nested Dictonary

student = {
    "name":"MD NASHIR KAZI",
    "courses": {
        "SE411": "A",
        "SE412": "A-",
        "SE413": "B+"
        
    }
}

print(student)
print(student["courses"])
print(student["courses"]["SE413"]) #Accesing the nested Dictionary


#Methods of Dictionary

print(list(student.keys())) # key
print(len(student))
print(len(list(student.keys())))

print(student.values())

print(student.items())
print(type(list(student.items())))

#.get
print(student.get("name"))

#.update
print("Before")
print(student)
student.update({"city":"DSC"})
print("After")
print(student)

