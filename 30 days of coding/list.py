'''n=[1,2,3,4,5,6]
#print(n)
for i in n:
    if n[i]%2==0:
        print(i)'''

n = [1, 2, 3, 4, 5, 6,7,8,9]
i = 0

while i < len(n):
    if n[i] % 2 == 0:
        if n[i] == 5:
            break
        if n[i] == 4:
            i += 1
            continue
        print(i)
    i += 1


#print(len(n))
