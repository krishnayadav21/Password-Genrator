import string
import random

size=int(input("Enter Password Length = "))
if size < 8:
    print("Password Must be 8 Characters Long")
else:
    upperletter=int(input("Enter Numbers of Upper Cases used = "))
    lowerletter=int(input("Enter Numbers of Lower Cases used = "))
    digits=int(input("Enter Numbers of Digits used = "))
    special=int(input("Enter Numbers of Special Characters used = "))
    a=''.join([random.choice(string.ascii_uppercase) for i in range(upperletter)])
    b=''.join([random.choice(string.ascii_lowercase) for i in range(lowerletter)])
    c=''.join([random.choice(string.digits) for i in range(digits)])
    d=''.join([random.choice(string.punctuation) for i in range(special)])
    z=a+b+c+d
    if len(z)>size:
        print("You Have Enter Wrong Data")
    else:
        list1=[]
        for i in z:
            list1.append(i)
        random.shuffle(list1)
        p="".join(list1)
        print("Your Password =",p)
