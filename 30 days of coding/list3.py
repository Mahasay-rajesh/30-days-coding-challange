s = 'Learning Python is very easy'
i=0
count=0
while i<len(s):
    if s[i]>='a' >= s[i]<='z':
        print(s[i])

        continue
    else:
        count+=1

    i+=1
    print(count ,end='')
