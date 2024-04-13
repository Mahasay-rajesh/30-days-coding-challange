#1-----------------------------------------------------------------
'''n = 'google.com'
i = {}

for char in n:
    if char in i:
        i[char] += 1
    else:
        i[char] = 1

# Display the result
print(f"Sample String: {n}")
print("Character Frequency:", i)'''
#2-----------------------------------------------------------------
'''n = 'Rajesh Kumar'
i = 0
while i < len(n):
    print(n[i],end='')
    i += 1'''
#3-----------------------------------------------------------------
'''n = 'Rajesh Kumar'
for i in n:
    print(i, end='')'''
#4-----------------------------------------------------------------
'''n = 'Rajesh Kumar'
i=0
while i<len(n):
    if i%2==0:
        print(n[i],end='')
    i+=1'''
#5-----------------------------------------------------------------
'''n = 'Rajesh Kumar'
for i in range(len(n)):
    if i % 2 == 0:
        print(n[i], end='')'''
#6-----------------------------------------------------------------
'''n = 'Rajesh Kumar'
output = ''
for i in range(2, len(n)):
    output += n[i]

print(output)'''
#7-----------------------------------------------------------------
'''n = 'Rajesh Kumar'
output = ''
for char in n:
    if char.lower() != 'r':
        output += char
print(output)'''
#8-----------------------------------------------------------------
'''n = 'Rajesh Kumar'

res=''
for i in n:
    if i.lower()!='a':
        res+=i
print(res)'''
#9-----------------------------------------------------------------
'''n = 'Rajesh Kumar'

Using a for loop to exclude characters after a space without built-in functions
output = ''
skip_next = False

for i in range(len(n)):
    char = n[i]
    if char == ' ':
        skip_next = True
    elif not skip_next:
        output += char

print(output+' Raj')'''
#10-----------------------------------------------------------------
'''n = 'Rajesh Kumar'

# Using a for loop to exclude characters after the first space and include "Raj" with space
output = ''
skip_next = False

for i in range(len(n)):
    char = n[i]

    if char == ' ' :
        skip_next = True
    elif not skip_next:
        output += char

print(output + ' Raj')'''
#11-----------------------------------------------------------------
'''n = 'Rajeshkumar.ece20*****19@dscet.ac.in'

# Using a for loop to remove asterisks from the string
output = ''

for char in n:
    if char != '*':
        output += char

print(output)'''
#12-----------------------------------------------------------------
'''n = 'fjn8ddjf*&djn23'

# Using a for loop to print only alphabetic characters without inbuilt function
output = ''

for char in n:
    # Check if the character is a letter (uppercase or lowercase)
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        output += char

print(output)'''
#13-----------------------------------------------------------------
n = 'fjn8ddjf*&djn23'
res = ''

for i in n:
    if ('a' <= i <= 'z' or 'A' <= i <= 'Z') or ('0' <= i <= '9'):
        res += i

print(res)
#14-----------------------------------------------------------------
'''n = 'fjn8ddjf*&djn23'
chars = ''
digits = ''

for i in n:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        chars += i
    elif '0' <= i <= '9':
        digits += i

# Print all characters
print("Alphabetic Characters:", chars)

# Print all digits
print("Digits:", digits)'''
#15-----------------------------------------------------------------
'''n = 'fjn8ddjf*&djn23'
chars = ''
digits = ''

for i in n:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        chars += i
    elif '0' <= i <= '9':
        digits += i

# Print both characters and digits in a single line
print("Alphabetic Characters:", chars,digits)'''
#16-----------------------------------------------------------------
'''n = 'fjn8ddjf*&djn23'
digits=''
for i in n:
    if '0'<=i<='9': 
        if int(i)%2==0:
            digits+=i
print(digits)'''
#17-----------------------------------------------------------------
'''n = 'fjn8ddjf*&djn23'
digits_char=''
for i in n:
    if '0'<=i<='n' or 'a'<=i<='z':
        digits_char+=i
print(digits_char)'''
#18-----------------------------------------------------------------
'''n = 'fjn8ddjf*&djn23'
digits=''
char=''
for i in n:
    if '0'<=i<='9':
        digits+=i
    if 'a'<=i<='z':
        char+=i
print(digits,char)'''
#19-----------------------------------------------------------------
'''n = 'fjn8ddjf*&djn23'
digits=''
for i in n:
    if '0'<=i<='9': 
        digits+=i
    
print(digits)'''
#20-----------------------------------------------------------------
'''n = 'fjn8ddjf*&djn23'
digit_sum = 0

for i in n:
    if '0' <= i <= '9':
        digit_sum += int(i)

print("Sum of Digits:", digit_sum)'''
#21-----------------------------------------------------------------
'''n='                 '
count=0
for i in n:
    if i==' ':
        count+=1
    
print(count)'''
#22-------------------------------------------------------------------    
'''n = '                 '
count = 0

for i in n:
    if i == ' ':
        count += 1

print(count)'''
#23-----------------------------------------------------------------
'''n='fjernf efehbfe erfbrf'
count=0
for i in n:
    if i==' ':
        count+=1
print(count)'''
#24-----------------------------------------------------------------
'''n = ['sdsdff', '56345(dfdf)', { 'dfkjv' }]
strings = []

for i in n:
    if type(i) == str:
        strings.append(i)

print(strings)'''
#25-----------------------------------------------------------------
'''n = ['sdsdff', '56345(dfdf)', { 'dfkjv' }]
string=[]
for i in range(len(n)):
    if i%2==0:
        string.append(n[i])
print(string)'''
#26-----------------------------------------------------------------
n = ['sdsdff', '56345(dfdf)', { 'dfkjv' }]
string = []

for i in range(len(n)):
    if i % 2 == 0:
        string.append(n[i])

print(string)
#27-----------------------------------------------------------------
'''l = ['a', 'b', 'c']

for i in range(len(l)):
    print(l[i])'''
#28-----------------------------------------------------------------
'''n='rajesh kumar'
i=0
for i in range(len(n)):
    if i%2==0:
        print(n[i])'''
#29-----------------------------------------------------------------    
'''n = 'rajesh kumar'
words = n.split()

# Check if there are at least two words, then print the second word
if len(words) >= 2:
    print(words[1])
else:
    print('Word not found')'''
#30-----------------------------------------------------------------
'''n='Rajesh kumar'
i=-1
while i< -len(n):
    print(n[i],end='')
    i-=1'''
#31-----------------------------------------------------------------    
'''n = 'Rajesh kumar'
i = -1

while i >= -len(n):
    print(n[i], end='')
    i -= 1'''
#32-----------------------------------------------------------------
'''n = 'Rajesh kumar'
m = n.split()
i = -1

while i >= -len(m):
    print(m[i], end=' ')
    i -= 1'''
#33---------------------------------------------------------------

'''n = 'fjn8ddjf*&djn23'
spcl = ''
digits = ''

for char in n:
    
    if not ('a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9'):
        spcl += char
    
    elif '0' <= char <= '9':
        digits += char

print("Special Characters and Digits:", spcl+digits)'''

































































        
 

















        






















































































   
