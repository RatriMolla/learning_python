# # import problem

# # print(problem.add(7,9))


#funciton def function_name(parameters1, parameters2):
def cal_sum(a,b):
     sum=a+b
     print(sum)
     return sum
     #return a+b
cal_sum(4,5)
cal_sum(10.8,34)

def print_hello():#empty function
     print("hello")
print_hello()     

city=["dhaka","rajshahi","cumilla","cattogram"]
dist=["shariatpur", "Fridpur"," Madaripur"]

def print_len(list):
     print (len(list))
print_len(city)  
print_len(dist)   

#print(),len(),type(),range()

def print_list(list):
     for item in list:
          print(item ,end=" ")


print_list(dist)          

