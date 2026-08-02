#file handling
#write()
'''a=open("pooja.txt","w")
a.write("codegnan it solutions")
a.close()'''

'''a=open("pooja.txt","w")
a.write("python")
a.close()'''

#append()
a=open("pooja.txt","a")
a.write("\tpooja")
a.close()

#run time input
'''a=open("pooja.txt","w")
a.write(input("data"))
a.close()''' 

'''a=open("pooja.txt","w")
b=input("data")
a.write(a)
a.close()'''


#read()
'''a=open("pooja.txt")
print(a.read())#it will display entire content
print(a.readline())#it will display first line
print(a.readlines())#it will display with \n
print(a.read(20))'''

#writelines()->it makes every object side by side
'''names=["varshitha","vasavika","tejaswi","roopa","brundha"]
a=open("sweety.txt","w")
a.writelines("\n".join(names))
a.close()'''


'''a=open("conditions.py")
print(a.read())'''

'''a=open("C:\\Users\\mythr\\Desktop\\codegnan\\data.py")
print(a.read())'''

