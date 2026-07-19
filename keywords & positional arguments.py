
#keywords and positional aruguments
'''def details(id,name,mailid):
    id=10
    name="pooja"
    mailid="pooja@gmail.com"
    print(id,name,mailid)
details (id="id",name="name",mailid="mailid")''' 
    

'''def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid") 
details(id=20,name="bhanu",mailid="b@gmaili.com")     
details(id=30,name="nayana",mailid="n@gmaili.com")
details(40,"chethana","c@gmail.com") 
details("h@gmail.com",50,"harika")
details(mailid="k@gmail.com",id=60,name="kavya")''' 

#default aruguments
'''def Grocery(item,price):
    print("item is %s" % item)
    print("price is %.2f" %price)
Grocery("rice",1500)'''

'''def Grocery(item,price=2000):
    print("item is %s" % item)
    print("price is %.2f" %price)
Grocery("dhal")''' 


'''def Grocery(item="ghee",price):
     #non def arg follows def arg
    print("item is %s" % item)
    print("price is %.2f" %price)
Grocery(500)'''

#cake_name,price,quantity
#* arguments(* is used to unpack the elements)
'''a=[10,20,30,40,50]
print(a)
print(*a)'''

'''b=(5,6,7,8,9,10)
print(b)
print(*b)'''

'''c={6,7,8,9,10}
print(c)
print(*c)'''

'''d={"name":"pooja","year":2026,"month":7}
print(d)
print(*d)'''

'''a="codegnan"
print(a)
print(*a)'''

'''a,b,c=2,3,4,5,6,7,8,9,10,11
print(a)
print(b)
print(c)'''#error

'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''a,*b,c=2,3,4,5,6,7,8,9,10,11
print(a)
print(*b)
print(c)'''



