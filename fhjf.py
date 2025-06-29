# import problem

# print(problem.add(7,9))


# list=[1,2,3,2,1]
# print(list)
# list.reverse()

# if(list == list[::-1]):
#     print("true")
# else :   
#     print("f")

list=[1,2,3,2,1]
copylist=list.copy()

copylist.reverse()

if(list == copylist ):
    print("it is palindrom")
else :   
    print("it isn't palindrom")

st= str(input("string:"))
if(st == st[::-1]):
    print("true")
else :   
    print("f")