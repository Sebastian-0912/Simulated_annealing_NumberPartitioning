import NumberPartition as num
import numpy as np
import matplotlib.pyplot as plt

set1=np.zeros((100,20),dtype=int)
set2=np.zeros((100,20),dtype=int)
minset=np.zeros(100,dtype=int)
index=0
numbers = [443, 552, 217, 319, 3, 708, 756, 342, 669, 133, 984, 405, 718, 105, 553, 66, 877, 705, 924, 654]
for temperature in range(1000,101000,1000):
    set1[index], set2[index] ,minset[index]= num.number_partitioning(numbers, initial_temperature=temperature, max_iterations=100000000)
    print(f"when T={temperature}:")
    print("array=",numbers)
    print("Set 1:", set1[index])
    print("Set 2:", set2[index])
    print("Cost:", minset[index],"\n")
    index+=1
