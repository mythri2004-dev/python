Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #arthematic
>>> a=2
>>> b=4
>>> print(a+b)
6
>>> print(a-b)
-2
>>> print(a*b)
8
>>> print(a//b)
0
>>> print(a/b)
0.5
>>> print(a**b)
16
>>> print(a%b)
2
>>> #assingement
>>> a=3
>>> b=5
>>> print(a+=b)
SyntaxError: invalid syntax
>>> a+b
8
>>> a+=b
>>> a
8
>>> a-=2
>>> a
6
>>> a*=2
>>> a
12
>>> a//=2
>>> a
6
>>> a**4
1296
>>> a
6
>>> a%=3
>>> a
0
>>> a**=5
>>> a
0
a
0
a=5
b=10
a+=b
b
10
a-=b
b
10
b-=5
b
5
a=3
print(a)
3
c=70
print(a)
3
#comparision
a=4
b=8
a<b
True
a>b
False
b<a
False
a!=b
True
a==b
False
False
False
a<=b
True
a>=b
False
#logical
a=5
b=7
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a>=b or a<=b
True
a!=b or a==b
True
True
True
not True
False
not False
True
#identify
a=4
type(a) is int
True
type(a) is not a int
SyntaxError: invalid syntax
type(a) is not int
False
b=23.4
type(b) is float
True
type(b) is not float
False
c="python"
type(c) is string
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    type(c) is string
NameError: name 'string' is not defined. Did you forget to import 'string'?
type(c) is "string"
False
False
False
type(c) is not a "string"
SyntaxError: invalid syntax
type(c) is not "string"
True
d=True
type(d) is bool
True
type(d) is not bool
False
e=False
type(e) is bool
True
type(e) is not bool
False
False
False
f="python"
type(f) is str
True
type(f) is not str
False
#membership
a=3,4,5,6,7,8,9,10
6 in a
True
40 in a
False
36 not in a
True
a=2
b=4
a&b
0
a=5
b=7
a&b
5
bin(2)
'0b10'
bin(4)
'0b100'
bin(5)
'0b101'
bin(7)
'0b111'
a=3
b=5
a|b
7
a=4
b=8
a|b
12
#not
a=2
-(a+1)
-3
a=5
~a
-6
a=9
~9
-10
b=-11
~b
10
c=-18
~c
17
#XOR
a=6
b=9
a^b
15
a=5
b=7
a^b
2
#left shift
a=3
a<<2
12
bin(3)
'0b11'
a=5
a<<3
40
#right shift
a=4
a>>2
1
bin(4)
'0b100'
a-9
-5
a>>3
0
a>>3
0
a=9
a>>3
1
