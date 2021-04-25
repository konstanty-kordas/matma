import math
for i in range(1,5):
    for j in range(1,5):
        x = complex(i,j)
        print(math.sqrt((x*x).real**2+(x*x).imag**2))
        print (x*x)
