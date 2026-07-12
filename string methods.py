Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count()
a="twinkle twinkle little star"
count("twinkle")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count("twinkle")
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count(k)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.count(k)
NameError: name 'k' is not defined
a.count("k")
2
a.count("t")
5
a.count(" ")
3
b="twinkletwinkle"
b.count("twinkle")
2
b.count("twinkletwinkle")
1
c=("twinkle.twinkle")
c.count("twinkle.twinkle")
1
c.count("twinkle")
2
#find a string
a="python"
a[2]
't'
a.find("t")
2
a.findd("n")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.findd("n")
AttributeError: 'str' object has no attribute 'findd'. Did you mean: 'find'?
a.find("n")
5
b="hello"
b.find("l")
2
b[2:4]
'll'
a.find("m")
-1
#escape sequences
#\n->new line
#\t->tab space
a="name\nmobileno\tmailid\ncollege\tbranch"
print(a)
name
mobileno	mailid
college	branch
b="name:pooja\nmobileno:789065432\tmailid:pooja@gmail.com\ncollege:nit\tbranch:ai"
print(b)
name:pooja
mobileno:789065432	mailid:pooja@gmail.com
college:nit	branch:ai
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="i love java"
b.replace("java","python")
'i love python'
a
'wait until you succeed'
a="cheeetha"
a.count(e)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.count(e)
NameError: name 'e' is not defined
a.count("e")
3
a.find(3)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.find(3)
TypeError: find() argument 1 must be str, not int
#upper
a="hello"
a.upper()
'HELLO'
#lower()
b="HI"
b.lower()
'hi'
c="python"
c.upper("p")
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    c.upper("p")
TypeError: str.upper() takes no arguments (1 given)
c[0].upper()
'P'
c.capitalize()
'Python'
d="python course"
d.title()
'Python Course'
e="i am in class"
e.capitalize()
'I am in class'
e.title()
'I Am In Class'
a="python"
a.isupper()
False
a.islower()
True
a.isalpha()
True
b="python course"
b.isaipha()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    b.isaipha()
AttributeError: 'str' object has no attribute 'isaipha'. Did you mean: 'isalpha'?
c="pythoncourse"
c.isalpha()
True
d=1234
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d="1234"
d.isdigit()
True
e="pooja"
e.isalnum()
True
f="pooja1234"
f.isalnum()
True
g="pooja@1234"
g.isalnum()
False
x="pooja_1234"
x.isalnum()
False
a="java"
a.startswith("j")
True
a.endswith("a)
           
SyntaxError: unterminated string literal (detected at line 1)
a.endswith("a")
           
True
#strip()
           
#lstrip(),rstrip()
           
a="         pooja          "
           
a.strip()
           
'pooja'
a.lstrip()
           
'pooja          '
>>> a.rstrip()
...            
'         pooja'
>>> #split()
...            
>>> a="python java c c++"
...            
>>> a.split()
...            
['python', 'java', 'c', 'c++']
>>> b="i am in class room"
...            
>>> b.split()
...            
['i', 'am', 'in', 'class', 'room']
>>> #join()
...            
>>> b="vija","hyd","vzg"
...            
>>> "".join(b)
...            
'vijahydvzg'
>>> " " .join(b)
...            
'vija hyd vzg'
>>> "k".join(b)
...            
'vijakhydkvzg'
>>> c="python"
...            
>>> "k".join(c)
...            
'pkyktkhkokn'
>>> join(b)
...            
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    join(b)
NameError: name 'join' is not defined
