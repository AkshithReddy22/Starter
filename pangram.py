a=input("Enter a sentence")
count=0
alpha='a'
b={}
for i in range(0,26):
    b[alpha]=count
    alpha=chr(ord(alpha)+1)
a=a.lower()
for i in a:
    b[i]=b[i]+1
def function(b):
    for i in range(ord('a'),ord('z')+1):
        if(b[chr(i)]>=1):
            return True
        else:
            print("This is not pangram")
            break
function(b)
if(function==True):
    print("This is pangram")

        
  
  
  
