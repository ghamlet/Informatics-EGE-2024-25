f = open("17_Integer_data_processing/6/1__1n2up.txt")

m = [int(i) for i in f]

local_min = [m[i+1] for i in range(len(m)-2) if m[i] > m[i+1] and m[i+2] > m[i+1]]
  
        
print(len(local_min), max(local_min))