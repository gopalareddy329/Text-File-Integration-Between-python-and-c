def check(username,password,rollno,email) :
    
    rollno=rollno+'\n'
    file_name=open("C://Users/LENOVO/Desktop/text file integration/main/stdb.txt","r")

    i=0
    linenumber=0
    content = file_name.readlines()
    test=[i.split('\t', 4)[2] for i in content]
    for i in range (0,len(test)):
        if email == test[i]:
            linenumber=i
    line=content[linenumber]
    data=line.split('\t')
    i=0
    if username==data[0]:
        i+=1
    if password==data[1]:
        i+=1
    if email==data[2]:
        i+=1
    if rollno==data[3]:
        i+=1
    return i

username=input("Enter Username : ")
password=input("Enter Password : ")
email=input("Enter email : ")
rollno=input("Enter rollnumber : ")
verify=check(username,password,rollno,email)
if verify==4:
    print("Correct")
else :
    print("Wrong")