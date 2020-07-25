import string
import random
str=string.ascii_letters + string.digits
def an_ranpass(ch,v):
    if ch.lower()=='r':
        sp=['@','&','.','_','$']
        pas={random.choice(sp)}
    elif ch.lower() not in str:
        pas={ch}
    elif ch.lower()=='n':
        pas={random.choice(str)}    
    while len(pas)!=v:
        pas.add(random.choice(str))
    password=''.join(pas)
    print(password) 
def n_ranpass(ch,v):
    digits=string.digits
    if ch.lower()=='r':
        sp=['@','&','.','_','$']
        pas={random.choice(sp)}
    elif ch.lower() not in str:
        pas={ch}
    elif ch.lower()=='n':
        pas={random.choice(digits)}     
    while len(pas)!=v:
        pas.add(random.choice(digits))
    password=''.join(pas)
    print(password)
def an_keypass(ch,v):
    key=input("Enter the key to use:")
    if ch.lower()=='r':
        sp=['@','&','.','_','$']
        pas={key,random.choice(sp)}
    elif ch.lower() not in str:
        if len(ch)==1:
            pas={key,ch}    
    elif ch.lower()=='n':
        pas={key}
    v=(v+1)-len(key)     
    while len(pas)!=v:
        pas.add(random.choice(str))
    password=''.join(pas)
    print(password)    