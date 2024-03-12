# Dot product 
import time 
import numpy 
import array

# 8 bytes size int 
a = array.array('q') 
for i in range(100000): 
    a.append(i); 
  
b = array.array('q') 
for i in range(100000, 200000): 
    b.append(i) 

      
# dot product of vectors implementation  
# loop version
#
tic = time.process_time() 
dot = 0.0; 

for i in range(len(a)): 
      dot += a[i] * b[i] 
  
toc = time.process_time() 
  
print("dot_product = "+ str(dot)); 
print("Computation time = " + str(1000*(toc - tic )) + "ms") 
   
  
n_tic = time.process_time() 
n_dot_product = numpy.dot(a, b) 
n_toc = time.process_time() 
  
print("\nn_dot_product = "+str(n_dot_product)) 
print("Computation time = "+str(1000*(n_toc - n_tic ))+"ms") 