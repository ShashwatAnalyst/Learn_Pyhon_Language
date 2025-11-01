# read
with open("harry.txt","rt") as f:
    print(f.read())
    
# write
with open("john.txt","w") as f1:
    text = "john lives in Ohio. he is a bad motherfucker"
    f1.write(text)
    
# append 
with open("john.txt","a") as f2:
    text2 = "Fuck you john"
    f2.write(text2)