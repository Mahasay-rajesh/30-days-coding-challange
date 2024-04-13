'''a='2[a]3[bc]'                       #"a6b4c2"
b=" "
i=0
while i<len(a):
    char=a[i]
    i+=1
    count=int(a[i])
    i+=1
    b +=char*count
print(b)'''


'''class car:
    def __init__(self,model,year,wheel):
        self.model=model
        self.year=year
        self.wheel=wheel
class motercycle:
    def __init__(self,model,year,wheel):
        self.model=model
        self.year=year
car(print(435,2001,4))
motercycle(print(43,2005,2))
car()
motercycle()'''

'''def add_digits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num
user_input = input("Enter a number: ")

if user_input.isdigit():
    input_num = int(user_input)
    output = add_digits(input_num)
    print(f"The final single-digit result is: {output}")
else:
    print("Invalid input. Please enter a valid number.")'''


#print("stmt-1")
#
def divide(a,b):
    return a/b
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
    
    



















        
