'''a=[1,2,'hbvhbg','ygs',5,6,'df']
i=0
sum=0
while i<len(a):
    if type(a[i]) == int:
        sum=sum+a[i]
        print(a[i],end='')
    i+=1
print('\nsum of all element:',sum)'''


'''a = [1, 2, 'hbvhbg', 'ygs', 5, 6, 'df']
i = 0
total_sum = 0

while i < len(a):
    if type(a[i]) == int:
        total_sum += a[i]
        print(a[i], end=' ')
    i += 1

print('\nSum of all integers:', total_sum)'''


'''a=[1,2,'hbvhbg','ygs',5,6,'df']
i=0
mul=1
while i<len(a):
    if type(a[i])==int:
        mul=mul*a[i]
        print(a[i],end='')
    i+=1
print('\n mul of all element:',mul)'''



'''a=[1,2,'hbvhbg','ygs',5,6,'df']
i=0
sum=0
while i<len(a):
    if type(a[i])==int:
        if a[i]%2==0:
            sum=sum+a[i]
            print(a[i],end=' ')
    i+=1
print('\nsum of all element:',sum)'''


'''a=[1,2,'hbvhbg','ygs',5,6,'df']
i=0
res=''
while i<len(a):
    if type(a[i])==str:
        res=res+a[i]
        #print(a[i],end='')
    i+=1
print('\nstring:',res)'''



s = 'learning1 python2 is3 very4 easy5'
l = s.split()
l1 = []
i = 0
while i < len(l):
    element = l[i]
    num = ''.join(char for char in element if char.isdigit())
    if num:
        l1.append(int(num))
        print(num, end='')
    i += 1
print('\nList of extracted integers:', l1)





    





































