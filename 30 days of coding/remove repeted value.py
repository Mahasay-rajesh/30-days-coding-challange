'''a=[2,4,2,5,2,6,78,5,3,6]
b=list(set(a))
print(b)'''

'''a='a,fd,e,e,a,,,,a,wr,.er.t,eas.'
b=str(set(a))
print(b)'''

a = [2, 4, 2, 5, 2, 6, 78, 5, 3, 6]
'''res = []
i = 0

while i < len(a):
    if a[i] not in res:
        res.append(a[i])
    i += 1

print("repeated values removed:", res)'''

res=[]
i=0
while i<len(a):
    if a[i] not in res:
        res.append (a[i])
    i+=1
print('remove repeted value:',res)

