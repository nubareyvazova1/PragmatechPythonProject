a=int(input('ilk eded:'))
b=int(input('ikinci eded:'))
c=int(input('ucuncu eded:'))
def my_function():
    d=max(a,b,c)
    print(d)
my_function()    
#1-ci alqoritim

my_list=[8,2,3,0,7]

def sum_function(): 
    cem=0
    for x in my_list:
        cem=cem+x
    print(cem)
sum_function()

#2-ci alqoritim
my_list=[8,2,3,-1,7]

def multiply_function(): 
    hasil=1
    for y in my_list:
        hasil=hasil*y
    print(hasil)
multiply_function()
#3-ci alqoritim
z='1234abcd'[::-1]
print(z)
#4-ci alqoritim
a=int(input('emsal daxil edin:'))
b=int(input('emsal daxil edin:'))
c=int(input('emsal daxil edin:'))
d=b**2-4*a*c
def kvadrat_kok():
    if d>0:
        x1=(-b-d**(1/2))/2*a
        x2=(-b+d**(1/2))/2*a
        print(x1,x2)
    elif d==0:
        x=-b/2*a 
        print(x)
    else:
        print("tenliyin koku yoxdur")      
        
kvadrat_kok()
#5-ci alqoritim