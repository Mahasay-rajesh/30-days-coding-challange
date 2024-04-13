# # class Employee:
# #     def __init__(self,eno,ename,esal,eaddr):
# #         self.eno=eno;
# #         self.ename=ename;
# #         self.esal=esal;
# #         self.eaddr=eaddr;
# #     def display(self):
# #         print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)
# # with open("emp.dat","wb") as f:
# #     e=Employee(100,"Durga",1000,"Hyd")
# #     pickle.dump(e,f)
# #     print("Pickling of Employee Object completed...")

# # with open("emp.dat","rb") as f:
# #     obj=pickle.load(f)
# #     print("Printing Employee Information after unpickling")
# # obj.display()

# # import pickle
# # d={'sname':'Rajesh',
# #    'Gender':'Male',
# #    'Degree':'B.E'}
# # out=pickle.dumps(d)
# # print(out)
# # t=pickle.dumps((1,2,3))
# # s=pickle.dumps({1,2,3})
# # c=pickle.dumps(3+4j)
# # '''unpickling'''
# # print(pickle.loads(out))
# # print(pickle.loads(t))
# # print(pickle.loads(s))
# # print(pickle.loads(c))

# import pickle
# d={'sname':'Rajesh',
#    'Gender':'Male',
#    'Degree':'B.E'}
# f=open(r"C:\Users\rajes\OneDrive\Desktop\kam.txt","wb")
# pickle.dump(d,f)
# pickle.dump((1,2,3),f)
# pickle.dump({1,2,3},f)
# pickle.dump(3+4j,f)
# f.close()
# #unpickling data with file
# f1=open(r"C:\Users\rajes\OneDrive\Desktop\kam.txt","rb")
# print(pickle.load(f1))
# print(pickle.load(f1))
# print(pickle.load(f1))
# print(pickle.load(f1))
# f1.close()

from collections import Counter

def identify_champion(strings):
    counts = Counter(strings)
    max_count = max(counts.values())
    for string, count in counts.items():
        if count == max_count:
            return string

# Example usage:
input_str = "apple banana orange grape kiwi"
strings = input_str.split()
print(identify_champion(strings))