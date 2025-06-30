#output
print("hello world")
print("it is my first code in python.","i will try my best")
print(23)
print(23+5)
name="ratri"#string
age=22
gpa=4.94
print(name)#variable print
print ("my name is :",name)
print("my age is :", age)
age2=age


print("my age is :", age2)

#print data type of variable
print(type(name))
print(type(gpa))


a=23
old=False
b=None
print(type(old))
print(type(b))


#operator
a=10
b=5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)# a to the power 2


print(a==b)
print(a!=b)

print(a>=b)
print(a>b)

print(a<=b)
print(a<b)

num=10
# num+= 10 #num=num+10
# num+= 5 #num=num+5
# num*= 5 #num=num*5
num%= 5 #num=num%5



print("NUM:",num)


"""
multiline
comment """
# (ctrl + /) for comment selected line
#operator

print(not True)
print(not False)

p=30
q=50

print(not(a>b))
val1=True
val2= True
print("And operator:",val1 and val2)
print("or operator:", val1 or val2)
print((p==q) or (p>q))
#type conversion
w=5
x=4.9
print(x+w)  #autometiclly print float type
#type casting

w=int(x)
y=3

print(w+y)


#user input

#input("enter your name:")
name=input("enter your name:") # input converting any typer of valu in string type
#print("welcome",name)
print(type(name),name)

age=int(input("enter your age:"))
print(type(age),age)

#string
str1 ="this is a string .\n two are creating it in "
print(str1)


str2="ratri"
str3="molla"
name= str2+ " " +str3
print(name)
#string length len(str)
print(len(name))
#indexing str[index]
ch=name[4]
print(ch)
print(name[3])
#slicing: accessing parts of a string str[starting_idx : end_idx]
print(name[0:5])
print(name[4:11])
print(name[0:len(name)])

print(name[:12])
print(name[0:])
print(name[-4:-1])
print(name[-7:-1])
print(name[::-1])# reverse: one step backward
#string function 


str4="i am studing python"

print(str4.endswith("on"))

print(name.capitalize())# capitalized first letter

print(name.replace("studing","learning"))
print(name.find("a"))
print(name.count("a"))
print(name.find("a"))

#conditional statement
age3 =int(input("age:"))
color=str(input("color"))
# if(age3 >= 21):
#     print("can vote ") #4 space
#colour=green

# if(True):
#     print("go")

if(color == "green"):
     print("go")
elif(color=="red"):
    print ("stop")
elif(color=="yellow"):
    print ("look") 
else:
    print("no light")    

    #nesting
age=34   
if("age>=18"):
    if("age>=35"):
        print("can't apply for this job")
    else:    
        print("can apply for this job")  
else:
    print("can't apply for this job")

#LIST

marks =[89.4, 88, 89, 81, 90]  #in list we can stores different types of data and we can change value
print(marks)
print (marks[4])
print(len(marks))
student =["ratri", "cse",25]
print(student)
student[0]="mafruja" 
print(student)
#list slicing  list[start:stop]

print(marks[1:5])
print(marks[-5:-1])

#list[start:stop:step]

print(marks[::2])# TAKE EVERY second element 

print(marks[::-1])# reverse: one step backward

#method of list
list=[2,1,4]
list.append(5)# add element in the last

list.sort()#sort ascending order
print(list)

list.sort(reverse=True)#decending order
print(list)

list2=list.copy()
print(list2)

list1=["rose","lily","nightqueen","lotus","sunflower"]
list1.sort()
print(list1)

list1.reverse()# write the list from the end:reverse
print(list1)

list1.insert(3,"jesmin")#inser element in particuler element .insert(index,element)
print(list1)

list1.remove("jesmin")#remove first occurrence of  element
print(list1)

list1.pop(3)#remove element according to index number
print(list1)

#Tuples
   
    #Tuples

tup=(1,)#single element tuple,without comma it's just a integer number
print(tup)
print(type(tup))

tpl=(3,5,6,8,3,6,)
print(tpl[1:3])

tpl.index(5)
print(tpl.index(5))#.index(element), it find index of value

print(tpl.count(6))# count how may time element has in tuple


#dictionary in python "key":value
info={
      "name":"ratri",
      "age":23,
      "university":"ZHSUST",
      "Learning": "coding",
      "course_name":["python","css","javascript"]

}

print (info)
        

         












 




