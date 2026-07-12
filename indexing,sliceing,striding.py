Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="vijayawada"
a[0]
'v'
a[1]
'i'
a[5]
'a'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
a="i am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[2]+a[3]
'am'
a[5]+a[6]
'in'
a="simple is better than complex"
a="simple is better than complex"
a[10]+a[11]=a[12]+a[13]+a[14]+a[15]
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
a[10]+a[11]+a[12]+a[13]+a[14]+a[15]
'better'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'simple'
a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]
'complex'
b="codegnan it solutions"
b[12]+b[13}+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
b[12]+b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]
'solution'
b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+b[7]
'codegnan'
#Negative indexing
a="i am learning python"
a[-6]+a[-5]+a[-4]+[-3]+[-2]+[-1]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a[-6]+a[-5]+a[-4]+[-3]+[-2]+[-1]
TypeError: can only concatenate str (not "list") to str
a="i am learning python"
a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
a[-15]+a[-14]+a[-13]+a[-12]+a[-11]
'learn'
a[-18]+a[-17]
'am'
a=python fullstack
SyntaxError: invalid syntax
a="python fullstack"
a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'stack'
a[-9]+a[-8]+a[-7]+a[-6]
'full'
a[-16]+a[-15]+a[-14]+a[-13]+a[-12]+a[-11]
'python'
'python'
'python'
#slicing
a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a="time is very precious"
a[13:21]
'precious'
a[0:4]
'time'
a[8:12]
'very'
b="work until you succeed"
b[15:23]
'succeed'
'succeed'
'succeed'
b[0:4]
'work'
b[5:10]
'until'
'until'
'until'
'until'
'until'
b[13:15]
'u '
b[12:15]
'ou '
'ou '
'ou '
b[13:15]
'u '
#negative sliceing
>>> a="vizag is city of destiny"
>>> a[-15:-11]
'city'
>>> a[-7:]
'destiny'
>>> a[-24:-19]
'vizag'
>>> b="hi hello how are you"
>>> b[-17:-12]
'hello'
>>> 'hello'
'hello'
>>> b[-7:-4]
'are'
>>> b[-3:]
'you'
>>> b[-11:-8]
'how'
>>> 'how'
'how'
>>> #striding
>>> start:stop:increment
SyntaxError: invalid syntax
>>> KeyboardInterrupt
>>> #sliding
>>> a="data science"
>>> [::]
SyntaxError: invalid syntax
>>> a[::]
'data science'
>>> a[::1]
'data science'
>>> a[::2]
'dt cec'
>>> #negative sliding
>>> a[:-5]
'data sc'
>>> a[-8:-2]
' scien'
