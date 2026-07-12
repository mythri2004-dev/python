Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
print(a+" "+b)
python course
fname="pooja"
lname="ch"
print(fname+lname)
poojach
print(fname+" "+lname)
pooja ch
print(fname.title()+" "+lname.title())
Pooja Ch
print(fname+" "+lname).title())
SyntaxError: unmatched ')'
print((fname+" "+lname).title())

Pooja Ch
#formatting
a=2
b=4
print(a+b)
6
print("the sum is",a+b)
the sum is 6
city="vija"
print("the city is",city)
the city is vija
#formate method(

#formate method()
a="motu"
b="pathulu"
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
