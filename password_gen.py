import other_meth as om
name=input("Welcome to the Password Generator\n*********************************\nEnter your name:")
val=int(input("No. of digits of password required mr./miss "+name+":"))
ch1=input("For Random password enter R\nFor using any string in password enter S\n")
try:
    if ch1.lower()=='r': 
        ch2=input("For Alphanumeric password enter AN\nFor Numeric password enter N\n")
        if ch2.lower()=='an':
            ch3=input("For using random special character in password enter R\nFor using specific special character input special character\nFor not using special character enter N\n")
            om.an_ranpass(ch3,val)
        elif ch2.lower()=='n':
            ch3=input("For using random special character in password enter R\nFor using specific special character input special character\nFor not using special character enter N\n")
            om.n_ranpass(ch3,val) 
    elif ch1.lower()=='s':
        ch3=input("For using random special character in password enter R\nFor using specific special character input special character\nFor not using special character enter N\n")
        om.an_keypass(ch3,val)
except:
    print("Invalid Choice") 