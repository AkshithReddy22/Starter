a=input("Enter a sentence")
count=0
alpha='a'
b={}
for i in range(0,26):
    b[alpha]=count
    alpha=chr(ord(alpha)+1)
a=a.lower()
for i in a:
    if(i!=' '):
        b[str(i)]=b[str(i)]+1
    else:
        continue
def func(b):
    for i in range(ord('a'),ord('z')+1):
        if(b[chr(i)]<1):
            return "This is not pangram"
            break
        else:
            continue
if(func(b)==None):
    print("This is pangram")
else:
    print(func(b))

        
  
  
  
