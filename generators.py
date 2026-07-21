#generators
#list comphrahension
#a=[expr for var in collection/range]
'''a=[i for i in range(21)]
print(a)
print(type(a))'''
#generator
#a=(expr for var in collection/range)
'''a=(i for i in range(21))
print(a)
print(*a)
print(type(a))'''

#print(list(a))
#print(tuple(a))
#print(set(a))

'''a=a,b=(int(x) for x in input("enter the values")
       .split(","))
def check(a,b):
    while a<b:
        #yield a
        a=a+1
        yield a
print(*check(a,b))''' 

'''a,b=(int(x) for x in input("enter the values")
       .split(","))
def check(a,b):
    while a<b:
         a=a+1
         return a
print(check(a,b))''' 


#yield v/s return
'''def mygen():
  #return "vija"
  #return "hyd"
  #return "DSA"
  return "vija","hyd","vzg" 
print(*mygen())'''

'''def mygen():
    yield "python"
    yield "java"
    yield "DSA"
print(*mygen())'''

#next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))
#print(next(d))stop iteration 



#right angle triangle
'''n=int(input("enter number of rows:"))
for i in range(n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()'''
#reverse right angle triangle
'''row = int(input("Enter the number of rows:"))

for i in range(row, 0,-1):
    for j in range(i):
        print("*", end="")
    print()'''


# solid square pattern

'''
N rows(outer loop), N cols(inner loop)

row col 1 2 3 4 5
    1   * * * * *
    2   * * * * *
    3   * * * * * 
    4   * * * * *
    5   * * * * *
'''


'''N = int(input('N= '))

for row_num in range(1, N+1):
    for col_num in range(1,N+1):
        print("*",end=" ")
    # new row, new line
    print()'''

'''rows = int(input("Enter number of rows: "))

    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(i):
            print("* ", end="")
        print()'''


#pramaid [ run time ]


'''a=int(input("enter the rows"))
for i in range(1,a+1):
    print(" "*(a-i),end="")
    print("* "*i)'''


