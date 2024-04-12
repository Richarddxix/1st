def incageres():
    age= int(input('what is your age'))
    if age >18:
            print("welcome")
    while age <18:
        
        print('ayooo')
        age +=1
incageres()

print("divider")

def desageres():
    age= int(input("what is your age"))
    if age >18:
            print("welcome")
    while age <18:
        
        print('ayooo')
        age -=1
    elif age ==0:
        exit("infant")
desageres()
desageres()