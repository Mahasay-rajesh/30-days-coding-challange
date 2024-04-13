#a=[10,4.5,'str','true',5,89,3+7j]
'''res=0
i=0
while i<len(a):
    #if type(a[i])==int:
    if type (a[i])==str:
        print(a[i],end=' ')
    i+=1'''


'''a = [10, 4.5, 'str', 'true', 5, 89, 3 + 7j]
res = 0
i = 0
while i<len(a):
    if type(a[i])==int:
        res+=a[i]
    i+=1

print('sum of all digit:',res)'''

#a = [10, 4.5, 'str', 'true', 5, 7, 3 + 7j]
'''i=0
while i<len(a):
    if type(a[i])==int:
        if a[0]>a[i]:
            print(a[i])
        i+=1'''

#count no of element
l=[1,3,5,2,5,523,74567]
'''count=0
for x in l:
    count+=1
print('length of list:', count)'''

maxelement=l[0]
for x in l:
    if x >maxelement:
        maxelement=x
print(maxelement)



'''x=list(map(lambda x:x**2,range(5)))
print(x)'''

'''x=y=1
while x<4:
    x+=1
    while y<3:
        print(y,end='')
        y+=1'''
        
'''x = ['25', 'Today', '53', 'Sunday','15']
x.sort()

print(x)'''


'''x=[[0.0,1.0,2.0],[4.0,5.0,6.0]]
y=x[0][1]+x[1][0]
print(y)'''


'''def test(i,j):
    if(i==0):
        return j
    else:
        return test(i-1,i+j)
print(test(4,7))
'''
'''def gen():

   x=2
   while True:
       yield x
       x+=1
y=gen()
for i in y:
    if i>=5:
        break
    else:
        print(i,end='')'''
    



























         











        

    
