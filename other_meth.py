import string
import random
str=string.ascii_letters + string.digits
def an_ranpass(ch,v):
    length = v
    if ch.lower()=='r':
        sp=['@','&','.','_','$']
        pas={random.choice(sp)}
    elif ch.lower() not in str:
        pas={ch}
    elif ch.lower()=='n':
        pas={random.choice(str)} 
    v=v-len(pas)    
    while len(pas)!=length:
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
    v=v-len(pas)    
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
        pas={key,ch}
    elif ch.lower()=='n':
        pas={key} 
    v=v-len(pas)    
    while len(pas)!=v:
        pas.add(random.choice(str))
    password=''.join(pas)
    print(password)    