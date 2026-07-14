Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #concatenation
... a="code"
... b="gnan"
... print(a+b)
... codegnan
... a="python"
... b="course"
... print(a+" "+b)
... python course
... fname="pooja"
... lname="ch"
... print(fname+lname)
... poojach
... print(fname+" "+lname)
... pooja ch
... print(fname.title()+" "+lname.title())
... Pooja Ch
... print(fname+" "+lname).title())
... SyntaxError: unmatched ')'
... print((fname+" "+lname).title())
... 
... Pooja Ch
... #formatting
... a=2
... b=4
... print(a+b)
... 6
... print("the sum is",a+b)
... the sum is 6
... city="vija"
... print("the city is",city)
... the city is vija
... #formate method(
... 
... #formate method()
... a="motu"
... b="pathulu"
print("hello {}{}".format(a,b))
hello motupathulu
print("hello {} {}".format(a,b))
hello motu pathulu
print("hello {} hello{}".format(a,b))
hello motu hellopathulu
hello motu hellopathulu
SyntaxError: invalid syntax
>>> 
>>> a="sita"
>>> b="ram"
>>> print(f"hello {a}{b}")
hello sitaram
>>> print(f"hello {a}  {b}")
... 
hello sita  ram
>>> print(f"hello {a} hello {b}")
... 
hello sita hello ram
>>> 
>>> a=4
>>> b=5
>>> print(a*b)
20
>>> c=a*b
>>> print("the product is {}".formate (c))
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print("the product is {}".formate (c))
AttributeError: 'str' object has no attribute 'formate'. Did you mean: 'format'?
>>> print("the product is {}".format (c))
the product is 20
>>> print("the product is {c}")
the product is {c}
>>> print(f" the product is {c}")
 the product is 20
>>> print("the product is {}".format (a*b))
the product is 20
>>> print(f" the product is {a*b}")
 the product is 20
>>> KeyboardInterrupt
>>> print("the product is {}{}".format (a*b))
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print("the product is {}{}".format (a*b))
IndexError: Replacement index 1 out of range for positional args tuple
#list[]
SyntaxError: multiple statements found while compiling a single statement
a=[3,5.6,"python",9+7j,True,False]
print(a)
[3, 5.6, 'python', (9+7j), True, False]
type(a)
<class 'list'>
b=9
type(b)
<class 'int'>
c=[9]
type(c)
<class 'list'>
a=["python","java","c"]
a.append("c++")
a
['python', 'java', 'c', 'c++']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
a
['python', 'java', 'c', 'c++', ['ml', 'ai']]
#extend()
a=["java","html","css"]
a.extend(["js","bs"])
a
['java', 'html', 'css', 'js', 'bs']
#insert()
b=["apple","banana","grapes"]
b.insert(1,"mango")
b
['apple', 'mango', 'banana', 'grapes']
#sort()
a=["kiwi","mango","apple","dragon","berry"]
a.sort()
a
['apple', 'berry', 'dragon', 'kiwi', 'mango']
b=[9,6,3,0,2,4,20]
b.sort()
b
[0, 2, 3, 4, 6, 9, 20]
#reverse()
a=["c","java","html","css"]
a.reverse()
a
['css', 'html', 'java', 'c']
b=[9,10,12,14,15]
b.reverse()
b
[15, 14, 12, 10, 9]
#pop()
a=["black","white","red","blue","pink"]
a.pop()
'pink'
a.pop(2)
'red'
a
['black', 'white', 'blue']
a.pop("whie")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.pop("whie")
TypeError: 'str' object cannot be interpreted as an integer
#remove()
a.remove("white")
a
['black', 'blue']
#copy()
a=["pooja","priya","sweety","cuty"]
a.copy()
['pooja', 'priya', 'sweety', 'cuty']
b=a.copy()
b
['pooja', 'priya', 'sweety', 'cuty']
a.clear()
a
[]
b=[]
b.append("hi")
b
['hi']
a=["hi","hello","how"]
len(a)
3
b="hello"
len(b)
5
c=["hello"]
len(c)
1
a.count("hello")
1
a=["ppoja"]
a.index("pooja"]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
a.index("pooja")
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a.index("pooja")
ValueError: list.index(x): x not in list
a=["pooja"]
a.index("pooja")
0
