#global and local variables & scope of the variable 
#first case of global variable
'''a=3
def check1():
    print("inside value is ",a)
check1()
print("outside value is",a)'''


#second case of global variables
'''a=4
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("outside value is",a)'''

#third case of both global and local variable
'''a=2
b=9
def check3():
    a=7
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=4#local variable
    b=b+a
    print("value of b is",b)
check3()
print("a value is",a)
print("b value is",b)''' 

#usage of global keyword     
'''a=5
def final ():
    global a,b
    print("inside value is",a)
    a=10
    print("upddated value is",a)
    #global b
    b=15
    b=b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)'''

#task-1
students=int(input("enter number of students:"))
present=0
absent=0
for i in range(1,students +1):
    status=input(f"enter attendance of student {i} (p/a):").upper()
    if status == "p":
        prsent += 1
    elif status == "A":
        absent += 1
    else:
        print("invalid input!enter only p or  A")

print("\nattendance tracking report")
print("total students:",students)
print("total prsents:",present)
print("total bsent:",absent)
 
