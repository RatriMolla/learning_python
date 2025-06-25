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
          
 


          

 