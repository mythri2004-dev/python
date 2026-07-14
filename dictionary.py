Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=[9,1,5,2,8,4,6,7,3,0]
>>> a1=a[0:5]
>>> a1
[9, 1, 5, 2, 8]
>>> a2=a[5:10]
>>> a2
[4, 6, 7, 3, 0]
>>> a1.sort()
>>> a1
[1, 2, 5, 8, 9]
>>> a2.sort()
>>> a2
[0, 3, 4, 6, 7]
>>> a1.reverse()
>>> a1
[9, 8, 5, 2, 1]
>>> a2.reverse()
>>> a2
[7, 6, 4, 3, 0]
>>> c=a1+a2
>>> c
[9, 8, 5, 2, 1, 7, 6, 4, 3, 0]
>>> c=a2+a1
>>> c
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> #dict()
>>> a={"name":"pooja","year":2026,"month":6}
>>> print(a)
{'name': 'pooja', 'year': 2026, 'month': 6}
>>> type(a)
<class 'dict'>
>>> b={"name","pooja"}
>>> type(b)
<class 'set'>
>>> c={2027:7}
>>> type(c)
<class 'dict'>
a={"year":2026,"month":"july","date":4}
a.update({"time":7})
a
{'year': 2026, 'month': 'july', 'date': 4, 'time': 7}
a.update({"name":"pooja"},{"city":"vija"})
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.update({"name":"pooja"},{"city":"vija"})
TypeError: update expected at most 1 argument, got 2
a.update({"name":"pooja","city":"vija"})
a
{'year': 2026, 'month': 'july', 'date': 4, 'time': 7, 'name': 'pooja', 'city': 'vija'}
#set default()
a={"course":"python"}
a.setdefault("duration",4)
4
a
{'course': 'python', 'duration': 4}
a={"colour":"black","food":"biriyani","icecream":"nuts"}
a["colour"]
'black'
a
{'colour': 'black', 'food': 'biriyani', 'icecream': 'nuts'}
a["black"]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a["black"]
KeyError: 'black'
a.get("food")
'biriyani'
a
{'colour': 'black', 'food': 'biriyani', 'icecream': 'nuts'}
a={"months":7,"day":"sat","time":7}
a.keys()
dict_keys(['months', 'day', 'time'])
a.values()
dict_values([7, 'sat', 7])
a.items()
dict_items([('months', 7), ('day', 'sat'), ('time', 7)])
a={"city":"vija","country":"india","state":"ap"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("city")
'vija'
a
{'country': 'india', 'state': 'ap'}
a.popitem()
('state', 'ap')
a
{'country': 'india'}
a={"name":"pooja","mail":"p@codegnan.com"}
len(a)
2
a.copy()
{'name': 'pooja', 'mail': 'p@codegnan.com'}
a
{'name': 'pooja', 'mail': 'p@codegnan.com'}
a.clear()
a
{}
a={"name":"pooja","year":2026,"name":"pooja"}
print(a)
{'name': 'pooja', 'year': 2026}
b={"name":"pooja","year":2026,"name":"pooja"}
b
{'name': 'pooja', 'year': 2026}
b={"name":"pooja","year":2026,"name":"priya"}
b
{'name': 'priya', 'year': 2026}
a={"name1":"pooja","year":2026,"name2":"pooja"}
a
{'name1': 'pooja', 'year': 2026, 'name2': 'pooja'}
a={"idnos":[10,20,30],"names":["sweety","cuty","hearty"]"marks":[60,70,80]}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a={"idnos":[10,20,30],"names":["sweety","cuty","hearty"]"marks":[60,70,80]}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a={"idnos":[10,20,30],"names":["sweety","cuty","hearty"],"marks":[60,70,80]}
print(a)
{'idnos': [10, 20, 30], 'names': ['sweety', 'cuty', 'hearty'], 'marks': [60, 70, 80]}
a.keys()
dict_keys(['idnos', 'names', 'marks'])
a.values()
dict_values([[10, 20, 30], ['sweety', 'cuty', 'hearty'], [60, 70, 80]])
a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['sweety', 'cuty', 'hearty']), ('marks', [60, 70, 80])])
a={"year":2026,"month":7}
a.count("year")
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a.count("year")
AttributeError: 'dict' object has no attribute 'count'
a.index("month")
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.index("month")
AttributeError: 'dict' object has no attribute 'index'
#task
a=["codegnan","python","course"]
a.upper()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.upper()
AttributeError: 'list' object has no attribute 'upper'
b=str(a)
b.upper()
"['CODEGNAN', 'PYTHON', 'COURSE']"
c=[]
c.append(a.upper())
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    c.append(a.upper())
AttributeError: 'list' object has no attribute 'upper'
