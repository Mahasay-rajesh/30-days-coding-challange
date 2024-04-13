'''s='i am rajesh'
#out='rajesh am i'
i=0
while len(s)>i:
    print(s[i], end='')
    i+=1'''

'''s='i am rajesh'
i=-1
while i>=-len(s):
    print(s[i],end='')
    i=i-1'''

'''s='i am rajesh'
for i in range(len(s)-1,-1,-1):
    print(s[i],end='')'''
   

'''s='ABCD'
#OUT=CDEF
i=0
l=0
while i<len(s):
    if s not in i:
        s.remove(input('Enter a chr:'))'''

s="ABCD"
l=s.split()
l1=[]
i=len(l)-1
while i>=0:
    l1.append(l[i])
    i=i-1
    output=' '.join(l1)
print(output)



#s = "ABCD"
s='ABCDEF'
out = ""
for i in s:
    j = ord(i)
    j += 2
    char = chr(j)
    out += char
print(out)


