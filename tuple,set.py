Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple()
a=(4,5.6,"pooja",8+9j,True,False)
print(a)
(4, 5.6, 'pooja', (8+9j), True, False)
type(a)
<class 'tuple'>
len(a)
6
a.index(8+9j)
3
a.count(True)
1
#sets{}
a={3,6.7,"python",8+9j,"True","False"}
print(a)
{'False', 3, (8+9j), 'True', 6.7, 'python'}
type(a)
<class 'set'>
b={6,9,3,5,6,10,9,20,5}
print(b)
{3, 20, 5, 6, 9, 10}
a={2,3,4,5,6,7,8,9}
b={6,7,8,9}
a.issubset(a)
True
a.issubset(b)
False
#super set
a={4,5,6,7,8,9}
b={6,7,8,9}
a.issuperset(b)
True
#union()
a={1,2,3,4,5,6}
b={5,6,7,8,9,10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#intersection
a={3,4,5,6,7,8,9}
b={7,8,9,10,11,12}
a.intersection(b)
{8, 9, 7}
#difference
a={10,11,12,13,14,15,16}
b={6,7,8,12,13,14,15,16,17}
a.difference(b)
{10, 11}
b.difference(a)
{8, 17, 6, 7}
#symmetric_difference
a{2,3,4,5,6,7,8,9}
SyntaxError: invalid syntax
a={2,3,4,5,6,,7,8,9}
SyntaxError: invalid syntax
a={1,2,3,4,5,6,7,8,9}
b={5,6,7,8,9,10,11,1}
a.symmetric_difference(b)
{2, 3, 4, 10, 11}
b.symmetric_difference(a)
{2, 3, 4, 10, 11}
#update
a={1,2,3,4,5}
b={4,5,6,7,8}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8}
a
{1, 2, 3, 4, 5, 6, 7, 8}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8}
b
{1, 2, 3, 4, 5, 6, 7, 8}
#intersection_update
a={1,3,5,7,8,9,10}
b={2,4,6,7,10,11,12}
a
{1, 3, 5, 7, 8, 9, 10}
a.intersection_update(b)
a
{10, 7}
a
{10, 7}
b
{2, 4, 6, 7, 10, 11, 12}
b.intersection_update(a)
b
{10, 7}
b
{10, 7}
#difference update
a={2,3,4,5,6,7,8}
b={1,5,6,7,8,9,10}
a.difference_update(b)
a
{2, 3, 4}
a
{2, 3, 4}
b.difference_update(a)
b
{1, 5, 6, 7, 8, 9, 10}
b
{1, 5, 6, 7, 8, 9, 10}
#symmetric_difference update
a={2,3,4,5,6,7,8,9}
b={5,6,7,8,9,10,11}
a.symmetric_difference_update(b)
a
{2, 3, 4, 10, 11}
b.symmetric_difference_update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9}
b
{2, 3, 4, 5, 6, 7, 8, 9}
#add
a={3,4,5,6,7,8}
a.add(10)
a
{3, 4, 5, 6, 7, 8, 10}
a.copy()
{3, 4, 5, 6, 7, 8, 10}
b=a.copy
b
<built-in method copy of set object at 0x0000021707755EE0>
b=a.copy()
b
{3, 4, 5, 6, 7, 8, 10}
a.clear
<built-in method clear of set object at 0x0000021707755EE0>
a
{3, 4, 5, 6, 7, 8, 10}
a.clear
<built-in method clear of set object at 0x0000021707755EE0>
a.clear()
a
set()
c=set()
c.add(30)
c
{30}
a={5,6,7,8}
a.pop()
8
a.pop(7)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a.pop(7)
TypeError: set.pop() takes no arguments (1 given)
a.remove(7)
a
{5, 6}
a
{5, 6}
>>> a.pop(1)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    a.pop(1)
TypeError: set.pop() takes no arguments (1 given)
>>> a.add(4,5,6)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a.add(4,5,6)
TypeError: set.add() takes exactly one argument (3 given)
>>> a.add(10)
>>> a
{5, 6, 10}
>>> a.add(20)
>>> a
{20, 5, 6, 10}
>>> a={2,3,4,5,6}
>>> a.discard(4)
>>> a
{2, 3, 5, 6}
>>> b={4,5,6,7}
>>> c={8,9,10,11}
>>> b.isdisjoint(a)
False
>>> b.isdisjoint(c)
True
>>> a={4,5,6,7,8}
>>> len(a)
5
>>> a.count(7)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    a.count(7)
AttributeError: 'set' object has no attribute 'count'
>>> a.index(7)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    a.index(7)
AttributeError: 'set' object has no attribute 'index'
