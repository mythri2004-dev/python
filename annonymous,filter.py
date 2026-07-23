#marks analysis report
'''students= int(input("Enter number of students: "))

marks = []

for i in range(1,students+1):
    mark = int(input(f"Enter marks  student {i} marks"))
    marks.append(mark)
for i in marks:
    print(i)
print(".........Marks Analysis Report............")
print("Total Students :", students)
print("Highest Marks  :", max(marks))
print("Lowest Marks   :", min(marks))
print("Total Marks    :", sum(marks))
print("Average Marks  :", sum(marks) /students)'''

#annonymous functions (nameless functions)
#write a function to calculate 2*x+5 where x=5
'''def f(x):
    print(2*x+5)
f(5)'''

'''def f():
    x=int(input())
    print(2*x+5)
f()'''

#syntax
#a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input())
b=lambda x:2*x+5
print(b(a))'''

#task
'''multiply=lambda a,b:a*b
print(multiply(5,4))'''

'''a=int(input())
b=int(input())
c=lambda a,b:a*b
print(c(a,b))'''

#task
'''a="codegnan"
upper=lambda x:x.upper()'''

'''print(upper(a)) 
b=lambda a:a.upper()
print(b(a))'''
 
'''b="python course"
title=lambda x:x.title()
print(upper(a))
print(title(b))'''
#firstname+lastname=fullname 
'''first=input("enter fname:")
last=input("enter  lname:")
fullname=lambda fname,lname:(fname +" "+lname).title()
print(fullname(fname,lname))'''

'''fname,lname=[x for x in input("enter the names")
             .split(" ,")]
fullname=lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''


#filter()
a=[10,20,23,25,67,45,80,90,97,85,100]
#print all even numbers
'''if a%2==0:
    print(a)'''

'''for i in a:
    if i%2==0:
        print(i)'''

'''b=list(filter(lambda x:x%2==0,a))
print(b)'''

'''b=list(filter(lambda x:x%2!=0,a))
print(b)'''

#[],(),{}
'''a=[]
print(type(a))

b=()
print(type(b))

c={}
print(type(c))

d=set()
print(type(d))'''

'''a=[[],set(),{}," ",None,3,5.6,"pooja",4+9j,True,False]
b=list(filter(None,a))
print(b)'''








    
  
