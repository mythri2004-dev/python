#built in fuctions 
#print(dir()) 
#print(dir("_builtins_"))
a="coddegnan"
print(a)
print(list(a))
print(tuple(a))
#print(dict(a)) error
#from keys()
b=dict.fromkeys(a)
print(b) 


c=dict.fromkeys(a,"pooja")
print(c) 


c["d"]="sam"
print(c) 

#eval()
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)''' 

'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)''' 

'''while True:
    a=(input("a value"))
    b=(input("b value"))
    print(a+b)'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''

#zip()->we can combine multiple collection into one collection
a=[10,20,30,40,50]
names=["teja","dinesh","vamsi","sanklap","surya"]
'''print(a+names)'''

'''b=zip(a,names)
print(b)'''# we can use data type

'''c=list(zip(a,names))
print(c)'''

'''c=tuple(zip(a,names))
print(c)'''

'''c=set(zip(a,names))
print(c)'''

'''c=dict(zip(a,names))
print(c)'''

#enumerate()#we can give counter to the collection
names=["mythri","darshini","sravani","srivarna","teja"]
'''for i in range(len(names)):
   print(i,names[i])'''

'''b=dict(enumerate(names))
print(b)'''

'''b=dict(enumerate(names,100))
print(b)'''

'''c=list(enumerate(names))
print(c)''' 

'''d=set(enumerate(names,1))
print(d)'''

'''e=tuple(enumerate(names,5))
print(e)'''  

#ASCII
#chr(),ord()
print(chr(65))
print(chr(90))
#print(chr("a"))#error

#ord()
print(ord("a"))

print(ord("z"))

#task
#print A to Z
for i in range(65,91):
    print(chr(i),end=" ")
    
#print a to z
for i in range(97,123):
    print(chr(i),end=" ")
#name in ascii
'''name=input("enter your name:")
for ch in name:
    print(ch,"=",ord(ch))'''

'''a=input("enter the name")
for i in a:
    print(i,"-",ord(i))''' 

#max(),min(),sum()

'''print(max(2,5,8,9,10,20,30))
print(min(2,4,6,8,10,12))
#print(sum(3,4,5,6,7,8,9)) #error
a=2,3,4,5,6,7,8
print(sum(a))'''

#task
#marks analysis report
marks=[90,70,40,97,56]
'''print("marks Anlysis Report")
print("Total students:",len(marks))
print("Highest marks:",max(marks))
print("Lowest marks:",min(marks))
print("Total arks:",sum(marks))
print("Average marks:",sum(marks) / len(marks))'''
    
