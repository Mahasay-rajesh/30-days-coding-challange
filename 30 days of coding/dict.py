d={'name': 'Rahul', 'age': 25, 'greet': ['hello']}
#out=[ 'Rahul',25, ['hello']]
#output=list(d.values())
'''res=[]
for key in d:
    res.append(d[key])
print(res)'''

s={'name': 'Rahul', 'age': 25, 'greet': ['hello']}

#out=[ 'Rahul',25, hello]


output = []
res=s.values()
for value in res:
  if type(value) == list:
    output = output + value
  else:
    output.append(value)
print(output)
