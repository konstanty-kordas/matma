import math



vertices = [complex(3,0)]
for i in range (3):
    vertices.append(vertices[-1]*complex(0,1))
print(vertices)

rotated = []
for vertice in vertices:
    rotated.append(vertice*complex(math.cos(math.pi/6),math.sin(math.pi/6)))



for i in rotated:
    print("Wierzchołek = ("+str(i.real)+', ' + str(i.imag)+")")
    print(i.real)
    print(i.imag)
print(rotated)

