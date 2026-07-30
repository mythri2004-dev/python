#exception handling
'''while True:
    try:
        a=int(input("a value"))
        b=int(input("b value"))
        c=a//b
        print(c)
    except:
        print("exception is rasied")
    else:
        print("no exceptions")
    finally:
        print("program ends")'''


#regular expressions(regex)
'''a="codegnan is in vja"
print(a)''' 

'''a="codegnana\nis\tin\nvja"
print(a)'''

#rstring
'''a=r"codegnan\nis\tin\nvja"
print(a)''' 


#compile(),search(),findall(),split(),sub()

#sequence characters
'''\w->it matches alphanumeric
\W->it matches non-alphanumeric
\d->it matches any digit
\D->it matches non-digit
\s->it represents white spaces(blanck)
\S->it represents non-white spaces'''

#compile()
import re
'''a="mat map cap cup money cash cat dog mug donkey maths"
b=re.compile(r"m\w\w\w\w")
print(b)'''

#search
'''c=b.search(a)
print(c)'''

'''c=re.search(r"m\w+",a)
print(c)'''

#find all
'''d=re.findall(r"m\w+",a)
print(d)'''

#split()
'''e=re.split(r"m",a)
print(e)

f=re.split(r"\s",a)
print(f)'''

#sub()
'''g=re.sub(r"m","a",a)
print(g) '''

#task
'''import re
a="123 456 abc 789"
b=re.findall(r"\d+",a)
print(b)'''

'''c="year 2026 month 7 date 30"
d=re.findall(r"\D+",c)
print(d)'''
        

'''c="year 2026 month 7 date 30"
d=re.findall(r"\d+",c)
print(d)'''
        


