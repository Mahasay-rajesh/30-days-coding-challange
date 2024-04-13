'''Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].'''

'''n = [2, 7, 11, 15]
sum = 0
for i in n:

    sum += i
print(sum)'''

'''nums = [2, 7, 11, 15]
sum = 0
i = 0
while i < len(nums):
    sum += nums[i]
    i += 1
print(sum)'''

'''n=int(input('Enter a num:'))
if n%4==0 or n%400==0 or n%100!=0:
    print('leap year')
else:
    print('not leap year')

def check_leap_year(n):
    if n % 4 == 0 and (n % 100 != 0 or n % 400 == 0):
        return 'Leap year'
    else:
        return 'Not leap year
        n = int(input('Enter a year: '))
print(check_leap_year(n))'''

'''nums = [-2, 1, -3, 4, -1, 2, 1, 1, -5, 4]
max_sum = float('-inf')
current_sum = 0
start = 0
end = 0
s = 0
for i in range(len(nums)):
    current_sum += nums[i]
    if current_sum > max_sum:
        max_sum = current_sum
        start = s
        end = i
    if current_sum < 0:
        current_sum = 0
        s = i + 1
print(nums[start:end+1])'''

input_string = "Ni@te_sh$"
output_list = [''] * len(input_string)

# Initialize pointers for start and end of the string
start, end = 0, len(input_string) - 1

while start <= end:
    # Check if the characters at start and end positions are alphabetic
    if input_string[start].isalpha() and input_string[end].isalpha():
        # Swap the characters at start and end positions
        output_list[start], output_list[end] = input_string[end], input_string[start]
        start += 1
        end -= 1
    elif not input_string[start].isalpha():
        output_list[start] = input_string[start]
        start += 1
    elif not input_string[end].isalpha():
        output_list[end] = input_string[end]
        end -= 1

output_string = ''.join(output_list)
print(output_string)



