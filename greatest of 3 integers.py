
a=int(input("Enter a integer : "))
b=int(input("Enter a integer : "))
c=int(input("Enter a integer : "))
print(a)
print(b)
print(c,"\n")

if (a>b):
    if(a>c):
        print(a,"is greatest ")
    else:
        print(c,"is greatest ")
else:
    if(b>c):
        print(b,"is greatest")
    else:
        print(c,"is greatest")
        
