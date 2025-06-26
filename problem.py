# number =int(input("number:"))

# if(number%7==0):
#     print(number,"number is multiple of 7")
# else:
#     print(number, "number is not multiple of 7" )   
# 
  
        

# def add(a,b):
#     return a+b

marks =[89.4, 88, 89, 81, 90]  #in list we can stores different types of data and we can change value
print(marks)
print (marks[4])
print(len(marks))
student =["ratri", "cse",25]
print(student)
student[0]="mafruja" 
print(student)
print(marks[1:5])
print(marks[-5:-1])

#method of list
list=[2,1,4]
list.append(5)# add element in the last

list.sort()#sort ascending order
print(list)
list.sort(reverse=True)#decending order
print(list)
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

