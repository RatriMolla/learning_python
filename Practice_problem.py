c=5.78
a=int(c)
print(a)
#1write  a program to input 2 number and print sum

a=int (input("a:") )

b= int (input("b:") )
sum=a+b
print("sum:",sum)

#2wap to side of square and print it's area

side=int(input("side="))

area=side*side
print("area=",area)


#3wap to input 2 floating point number & print their average

a=float (input("a:") )



b=float (input("b:") )

average=(a+b)/2
print("averag=", average)


#4wap to inpurt 2 int number a,b print true if a is greater than or equal to b .if not print false
a=int (input("a:") )

b= int (input("b:") )
print(a>=b)

#find the length of string

str1=str(input("firstname:"))
print(len(str1))

# count $
print(str1.count("$"))


#abc="fytguyh huyui uuy"

abc=str(input("string:"))
print(abc.count("u"))
3
#grade student based on marks
marks=int(input("marks:"))

if("marks>=90"):
    grade="A"
elif("marks<90" and "marks >=80"):
    grade="A-"
elif("marks<40"):
    grade="pass "
else:
   grade="fail"   
#wap to check if a number odd or even
num=int(input("number:"))
#d=num%2
if(num%2==0) :
    print("it's even number") 
else:
    print("it's odd number")
    #find greatest of 3 numbers entered by the number
num1=int(input("num1:")) 
num2=int(input("num1:")) 
num3=int(input("num1:"))    
if(num1 > num2 and num1 >num3):
    print(num1,"num1 is greatest number")
elif( num2> num1 and  num2 > num3):
    print(num2,"num2 is greatest  number")
else:
    print(num3,"num3 is greatest")  

#if a number is a multiple of 7 or not

number =int(input("number:"))

if(number%7==0):
    print(number,"number is multiple of 7")
else:
    print(number,"number is not multiple of 7" )  
    #list 
marks =[89.4, 88, 89, 81, 90]  
print(marks)
          

#ask to user input 3 value of a list
list=[]
mov1=input("enter 1st movie:")
mov2=input("enter 2st movie:")
mov3=input("enter 3st movie:")

list.append(mov1)
list.append(mov2)
list.append(mov3)
print(list)          
 
#check if a list contains a palindrome of elements

list=[1,2,3,2,1]


if(list == list[::-1]):
    print("it is palindrom")
else :   
    print("it isn't palindrom")

#another method


list=[1,2,3,2,1]
copylist=list.copy()

copylist.reverse()

if(list == copylist ):
    print("it is palindrom")
else :   
    print("it isn't palindrom")

    

#check if a sting contains a palindrome of elements          

st= str(input("string:"))
if(st == st[::-1]):
    print("it is palindrom")
else :   
    print("it is not palindrom")

#Store following world meaning in a python dictionary
table={
"a piece of furniture":"list of facts & figures",
"cat":"a small animal"

}    

print(table)

#print number from 1 to 100

i=1
while i <=100:
    print(i)
    i+=1
# print 100 to 1    
i=100
while i >=1:
    print(i)
    i-=1
#print the multipication table of number n    

n=int(input("n="))  
a=1
while a<=10:
    print(n*a)
    a+=1

n=int(input("n="))  
a=1
while a<=50:
    print(a)
    a+=5
#   print the element of the following list using loop
list =[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

idx=0
while idx<len(list):
    # print(idx)
    print(list[idx])
    idx+=1

# search for a number x in  tuple using loop
tpl=(1,4,9,16,25,36 , 49, 64, 81,100 )
pl=0
nm=int(input("number"))
while pl<len(tpl):
    if tpl[pl]==nm:
        print("found", tpl[pl] ,"in index",pl)
        break
    else:
        print(" not found", tpl[pl] )    
    pl+=1

number = 0
i=0
while  i<= 5:
    if(i==3):
        i+=1
        continue
    print(i)
       
#codeforce problem solving 71A

n= int(input())
for _ in range(n):
    word =str(input())
    if len(word)>10:
        abb=word[0]+str(len(word)-2)+[word-1]
        print(abb)
    else :
        print (word)   
        
#WRP for factorial

n=int(input("number:"))
fact=1
for i in range(1,n+1):
     fact *= i
print(n,"factorial is ",fact)

#convert used to  inr
def convert(usd_val):
     inr= usd_val*123
     print(usd_val,"USD=",inr,"INR")
convert (80) 


    