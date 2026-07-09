Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #variables
>>> print(3+8)
11
>>> a=10
>>> print(a)
10
>>> b=20
>>> print(b)
20
>>> x=40
>>> print(X)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
>>> print(x)
40
>>> z=50
>>> print(z)
50
>>> 3=80
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> a3=80
>>> print(a3)
80
>>> 6a=90
SyntaxError: invalid decimal literal
>>> b123456789=300
>>> print(b123456789)
300
>>> @=60
SyntaxError: invalid syntax
>>> print(2)
2
>>> print(@)
SyntaxError: invalid syntax
>>> _ =50
print(_)
50
  =90
  
SyntaxError: unexpected indent
if=20
SyntaxError: invalid syntax
a=4,b=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=4;b=9
print(a+b)
13
a,b=3,4
print(a,b)
3 4
a,b,c=(2,3,4)
print(a,b,c)
2 3 4
a,b,c = 2,3,4,5,6,7,8,9,0
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a,b,c = 2,3,4,5,6,7,8,9,0
ValueError: too many values to unpack (expected 3, got 9)
fname="pooja"
lname="ch"
print(fname+lname)
poojach
print(fname +" " +lname)
pooja ch
print(fname,lname)
pooja ch
name="pooja"
print(name)
pooja
NAME="pooja"
print(NAME)
pooja
Name="Pooja"
print(Name)
Pooja
