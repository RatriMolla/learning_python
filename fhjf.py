# import problem

# print(problem.add(7,9))


# list=[1,2,3,2,1]
# print(list)
# list.reverse()

# if(list == list[::-1]):
#     print("true")
# else :   
#     print("f")

# 

# count =1
# while count <= 5 :
#     print(count)
#     count += 1
# print(count)

# i=5
# while i>=1:
#     print(i)
#     i-=1

# print(i)
#print number from 1 to 100

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

 