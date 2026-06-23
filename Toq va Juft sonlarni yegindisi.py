N=int(input())
jufy=0
toq=0
for i in range(1,N+1):
    if i % 2==0:
        jufy+=i
    else:
        toq+=i
    print(jufy,toq)