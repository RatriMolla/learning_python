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
student={
"name":"ratri",
"roll":"016",
"batch":"25",
"dept":"cse",
 "course":{
     "HTML":"completed",
     "JAVASCRIPT":"completed",
     "PYTHON":"RUNNING"
      }

}

print(student["course"])
print(list(student.keys()))
print(student.keys())
print(len(list(student.keys())))
print(student.items())
pairs=list(student.items())

print(pairs[0])

print(student.get("name"))
print(student["name"])

location={
    "devision":"dhaka",
    "distric":"shariatpur",
    "union":"gharishar"
   }
student.update(location)

print(student)

