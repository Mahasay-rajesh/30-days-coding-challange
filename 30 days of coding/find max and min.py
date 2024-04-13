l=[1,3,5,2,5,523,74567]
'''maxelement=l[0]
for x in l:
    if x >maxelement:
        maxelement=x
print(maxelement)'''

'''min=l[0]
for x in l:
    if x<min:
        min=x
print(min)'''


l = [10, 4.5, 'str', 'true', 5, 89, 3 + 7j]

maxelement = None

for x in l:
    if type(x) == int and (maxelement is None or x > maxelement):
        maxelement = x

print("Maximum int:", maxelement)

maxelement = None

for x in l:
    if type(x) == int and (maxelement is None or x < maxelement):
        maxelement = x

print("Minimum int:", maxelement)
