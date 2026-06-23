#for i in range(0,11,2):
#    print(i,end=';')
#for i in range(10,):
#    print(i,end=';')
#for i in range (10,0,-1):
#    print(i, end=';')
#n=int(input('n='))
#s=0
#for i in range (1,n+1):
# if i%2==1:
#    s+=i
#print('s=',s)
#n=int(input('n='))
#f=1
#for i in range(1,n+1):
#    f*=i
#print(n,'!','=',f)
#n=int(input())
#kvadrat=0
#for i in range(1,n+1):
#  kvadrat+=i**2
#print(n,'=',kvadrat)

#k=int(input('k'))
#n=int(input('n'))
#if n>0:
# for i in range(1,n+1):
#    print(k,'\n')
a=int(input())
b=int(input())
s=0
if a<b:
    for i in range(a,b+1):
        s=s+i
print('S=\'',s)
