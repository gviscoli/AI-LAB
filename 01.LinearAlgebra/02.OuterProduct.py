# Outer product 
import time 
import numpy 
import array 
  
a = array.array('i')
for i in range(2000): 
    a.append(i); 
  
b = array.array('i') 
for i in range(2000, 4000): 
    b.append(i) 

print(a)
print(b)

# classic outer product of vectors implementation  
#
startTime = time.process_time() 
outer_product = numpy.zeros((200, 200)) 
  
for i in range(len(a)): 
   for j in range(len(b)): 
      outer_product[i][j]= a[i]*b[j] 
  
endTime = time.process_time() 
  
print("outer_product = "+ str(outer_product)); 
print("Computation time = "+str(1000*(endTime - startTime ))+"ms") 
   
n_startTime = time.process_time() 
outer_product = numpy.outer(a, b) 
n_endTime = time.process_time() 
  
print("outer_product = "+str(outer_product)); 
print("\nComputation time = "+str(1000*(n_endTime - n_startTime ))+"ms") 