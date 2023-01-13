import random 
list1 = ["apple","banana","orange","pine","watermelon","papaya"]
list2 = ["patato","onion","lemon","garlic","bringal","tomato"]
list3 = ["tiger","lion","dog","cat","elephant","monkey"]
print("password Generator")
print("===================\n")
a = int(input("enter the number of password:"))
if 1<=a<=24:
    for i in range(a):
        password = random.choice(list1)+random.choice(list2)+random.choice(list3)
    print(password)
else:
    print("please enter a suitable number")
