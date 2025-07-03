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

#set in muteable but element of set is immuatble
collection ={3, 6, 8.78,"abc",}
# emptyset= set()
collection.add("ratri")
collection.add("ratri")#set ignore duplicate value
collection.remove("ratri")
print(collection)
# collection.add(["ratri"])#set don't support list


print(len(collection))

collection.pop()#remove random value
print(collection)

collection.clear()#remove all
print(collection)

set1={4, 6, 7,8}
set2={6, 3, 8,1}

print(set1.union(set2))
print(set1.intersection(set2))


table={
"a piece of furniture":"list of facts & figures",
"cat":"a small animal"

}    

print(table)

