age= int(input("Please enter your age and we will tell you are eligable or not  to use perticular website :"))

if(age >= 18):
    print("Congrats!you are eligalble to use the site!")

if(age < 18 and age>0):
    print("You have to try after",18-age,"years")

if(age == 0 or age <0):
    print(" You are a BOT!")

else:
    print("GOOD BYEE!")