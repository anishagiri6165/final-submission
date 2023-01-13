import re
import random
try:
    file = open("Stu.txt",'r')
    file2 = open("googlemail.txt","a+")
    p = []
    a = file.readlines()
    for lines in a:
        mail = ""
        id = lines[:9]
        nm = lines[9:]
        p = nm.split(",")
        for i in p[1]:
            if i.isupper():
                mail += i + "."
        email = (mail + p[0] + str(random.randint(1000,4000)) + "@poppleton.ac.uk").lower()
        std = re.sub("[-' ]","", email)
        file2.write(id+" "+std+"\n")
    file.close()
    file2.close()

except FileNotFoundError as fe:
    print(fe)


    

