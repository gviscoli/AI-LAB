# Dot product 
import time 
import numpy 
import array

# 8 bytes size int 
a = array.array('q') 
for i in range(1000000): 
    a.append(i); 
  
b = array.array('q') 
for i in range(1000000, 2000000): 
    b.append(i) 

      
# dot product of vectors implementation  
# loop version
#
startTime = time.process_time() 
dot = 0; 

for i in range(len(a)):
      dot += a[i] * b[i] 
  
endTime = time.process_time() 

print("Start time:", startTime)
print("End time:", endTime)

print("dot_product = "+ str(dot)); 
print("Computation Start time = " + str(1000*(endTime - startTime)) + "ms") 
print("Computation End time = " + str((endTime - startTime))) 


print("\n")

n_tic = time.process_time() 
n_dot_product = numpy.dot(a, b) 
n_toc = time.process_time() 

print("n_tic:", n_tic)
print("n_toc:", n_toc)

print("\nn_dot_product = "+str(n_dot_product)) 
print("Computation Start time = "+str(1000*(n_toc - n_tic ))+"ms") 
print("Computation End time = "+str((n_toc - n_tic ))) 


print("\nTest difference: ",dot-n_dot_product)
