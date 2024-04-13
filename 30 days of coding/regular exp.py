# import re
# inp='aaaaabbbbccccdeeggggjjjhhhhiiijjjkkk***8123'
# print(re.findall('a',inp))
# print(re.findall('b',inp))
# print(re.findall('aa',inp))
# print(re.findall('bb',inp))
# print(re.findall('c',inp))
# print(re.findall('d',inp))


# import re

# inp = 'aaaaabbbbccccdeeggggjjjhhhhiiijjjkkk***8123'

# print(re.search('aaa', inp))
# print(re.search('bb', inp))
# print(re.search('abb', inp))
# print(re.search('bb', inp))
# print(re.search('abb', inp).start())
# out1 = re.search('abb', inp)
# print(out1.span())
# out2 = re.search('abb', inp)
# print(out2.string)

# import re
# inp = 'abcdabcdefghi'
# print(re.sub('abcd','ABCD', inp))
# print(re.sub('abcd','ABC', inp))
# print(re.sub('abcd','A', inp))
# print(re.sub('abcd','', inp))
# print(re.sub('abcd','A', inp,1))
# print(re.sub('abcd','A', inp,0))
# print(re.sub('g','A', inp,1))

#Check the valid phone number
'''import re

a = input('Enter a phone number: ')
out = re.findall(r'([6-9][0-9]{9})', a)

if out and len(a) == 10:
    print(a, 'is a valid phone number')
else:
    print(a, 'is not a valid number')'''

#wap to check the valid vechile number
# import re
# a=input('Enter the vechile number:')
# out=re.findall('[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}')
# if out and len(a)==10:
#     print(a,'valid vechile number')
# else:
#     print(a,'not valid number')


