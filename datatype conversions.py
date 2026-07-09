Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatype conversions
>>> #int()
>>> int(9)
9
>>> int(8.9)
8
>>> int("pooja")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("pooja")
ValueError: invalid literal for int() with base 10: 'pooja'
>>> int(6+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(6+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
>>> 
>>> #float
>>> float(6)
6.0
>>> float(3.4)
3.4
>>> float("python")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float("python")
ValueError: could not convert string to float: 'python'
>>> float(7+9j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(7+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
TypeError: float() argument must be a string or a real number, not 'complex'float(7+9j)
SyntaxError: invalid syntax


float(True)
1.0
float(False)
0.0
#str()
str(6)
'6'
str(5.6)
'5.6'
str("hi")
'hi'
str(6+9j)
'(6+9j)'
str(True)
'True'
str(False)
'False'
#complex
complex(7)
(7+0j)
complex(7.8)
(7.8+0j)

(7.8+0j)
(7.8+0j)
complex("hello")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    complex("hello")

ValueError: complex() arg is a malformed string
complex(5+9j)
(5+9j)
complex(True)
(1+0j)
complex(False)
0j
#bool
bool(5)
True
bool(8.9)
True
bool("java")
True
bool(5+9j)
True
bool(True)
True
bool(False)
False
