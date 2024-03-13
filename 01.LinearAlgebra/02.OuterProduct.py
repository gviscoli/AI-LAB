# Outer product 
import time 
import numpy 
import array 
import os

# Configuration
#
max_range = 9000
start_number = 1000

a = array.array('i')
for i in range(max_range): 
    a.append(i); 
  
b = array.array('i') 
for i in range(start_number, start_number+max_range): 
    b.append(i) 

# Init two Array
#
outer_product1 = numpy.zeros((max_range, max_range)) 
outer_product2 = numpy.zeros((max_range, max_range))

# print(outer_product1)
# print("\n")
# print(outer_product2)

os.system('cls')

# classic outer product of vectors implementation  
#
startTime = time.process_time() 

  
for i in range(len(a)): 
   for j in range(len(b)): 
      outer_product1[i][j]= int(a[i]*b[j]) 
  
endTime = time.process_time() 

print("Results")
print("\n")

#print("outer_product1 = "+ str(outer_product1)); 
print("Computation time for standard loop = "+str(1000*(endTime - startTime ))+"ms") 
   
print("\n")

n_startTime = time.process_time() 
outer_product2 = numpy.outer(a, b) 
n_endTime = time.process_time() 
  
#print("outer_product2 = "+str(outer_product2)); 
print("\nComputation time for numpy.outer(a, b) = "+str(1000*(n_endTime - n_startTime ))+"ms") 

print("\n")

print("Check")
print(outer_product1[1][max_range-1])
print(outer_product2[1][max_range-1])