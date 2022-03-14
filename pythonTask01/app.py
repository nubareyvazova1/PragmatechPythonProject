a=int(input('kvadiratin ilk terefi:'))
b=int(input('kvadiratin ikinci terefi:'))
c=int(input('kvadiratin ucuncu terefi:'))
d=int(input('kvadiratin dorduncu terefi:'))
if a==b and b==c and c==d:
    s=a*b
    print(s)
else: 
  print(a+b+c+d) 
 
#1-ci tapsiriq
a=int(input('ilk eded:'))
b=int(input('ikinci eded:'))
c=int(input('ucuncu eded:'))
d=int(input('dorduncu eded:')) 
max=list[0]
list1=[a,b,c,d]
i=0
max=a
for y in list1:
    if max<y:
        max=y
        i=i+1
print(max)     
      
#2-ci tapsiriq     
      
      
fruits={
    "alma":"1azn",
    "armud":"2azn", 
    "alca":"4azn", 
    "banan":"3azn"
}
print(fruits)
a=input("meyvelerden birinin adini daxil edin:")
if a in fruits:
    print(fruits[a])
else:
    print("error")
    
#3-cu tapsiriq


            
            
 
newlist=(1,2,3,4,5,12,14)
sum=0  
for x in newlist:
    sum=sum+x
print(sum)
    
#5-cu tapsiriq bitdi   
    
list2=(1,2,34,4,5,12,14)
max=list2[0] 
i=0
for x in list2:
    if x>max:
        max=x
        
        i=i+1      
print(max)

#6-cu tapsiriq bitdi

list3=(1,2,34,4,5,12,14)
min=list3[0] 
i=0
for x in list3:
    if x<min:
        min=x
        
        i=i+1      
print(min)

#7-cu tapsiriq bitdi

samplelist=['abc', 'xyz', 'aba', '1221']
for x in samplelist:
    if len(x)>=2:
        if x[0]==x[-1]:
            print(x)
            
#8-cu tapsiriq bitdi            
list4=[] 
if not list4:
       print("empty list")
#9-cu tapsiriq bitdi" 
my_text = "Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings."
my_list=my_text.split()
my_list.sort()
for z in my_list:
        print(z)
#10-cu tapsiriq bitdi

numbers=[10,23,34,21,13,45,66,64,98,88]
for i in numbers:
    if i%2!=0:
        print(i)
        
#ad=input("adinizi daxil edin:")
#if len(ad)<11 and len(ad)>3:
#    soyad=input("soyadinizi daxil edin:")
#    if len(soyad)<15 and len(soyad)>5:
#        il=input("doguldugunuz ili daxil edin:")
#        if len(il)==4:
#            yas=2022-int(il)
#            yas=str(yas)
#            email=input("emailinizi daxil edin:")
#            if len(email)>10 and len(email)<32:
#                if email[-11:-1]=="@gmail.com":
#                    parol=input("parol daxil edin:")
#                    if len(parol)>5 and len(parol)<13:
#                        testiqle=input("parol testiq edin:")
#                        if parol==testiqle:
#                            print("qeydiyat tamamlandi")
#                            answer=input("qeydiyyatin detallarina baxmaq istəyirsinizmi?")
#                            if answer=="he":
#                                print("Ad: "+ad, "Soyad: "+soyad,"Yas: "+yas,"Email: "+email,"Parol: "+parol)
#                            else:
#                                print(ad+soyad+"ugurlar")    
#                        else:
#                            print("eyni parol deyil")
#                    else:
#                        print("daha guclu parol daxil edin")
#                        
#                else:
#                    print("emeilinizi deyisin")
#            else:
#                print("emeilinizi deyisin")            
#        else:
#            print("doguldugunuz ili duzgun daxil edin")        
#    else:
#        print("soyadinizi duzgun daxil edin")
#else:
#    print("adinizi duzgun daxil edin")
#4-cu tapsiriq bitdi
#dict1={
#    "name": "Plato" ,
#    "country": "Ancient Greece",
#    "born": -427 ,
#    "teacher": "Socrates",
#    "student": "Aristotle"
#}
sual1=input("sualinizi daxil edin: ")
if "born" and "when" in sual1:
    answer=input("Maybe did you mean 'When was Plato born?'")
    if answer=="yes":
        print(dict["born"])
    else:
        print("none")
else:
    print("not found")      