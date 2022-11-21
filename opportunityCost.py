import math 

class telefono:

    def _init_(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
telefonos = []       
n = 0
casos = [0,0,0,0,0,0,0]

n = int(input())

for i in range(n):
    x,y,z = input().split()
    telefonos.append(telefono(int(x),int(z),int(y)))
   
for i in range(n):
    casos[0] = max(casos[0], telefonos[i].x)
    casos[1] = max(casos[1], telefonos[i].y)
    casos[2] = max(casos[2], telefonos[i].z)
    casos[3] = max(casos[3], telefonos[i].x + telefonos[i].y)
    casos[4] = max(casos[4], telefonos[i].x + telefonos[i].z)
    casos[5] = max(casos[5], telefonos[i].y + telefonos[i].z)
    casos[6] = max(casos[6], telefonos[i].x + telefonos[i].y + telefonos[i].z)
        
    costo = math.inf
    ub = 0
    
for i in range(n):
        temporal = 0
        temporal = max(temporal, casos[0] - telefonos[i].x)
        temporal = max(temporal, casos[1] - telefonos[i].y)
        temporal = max(temporal, casos[2] - telefonos[i].z)
        temporal = max(temporal, casos[3] - telefonos[i].x - telefonos[i].y)
        temporal = max(temporal, casos[4] - telefonos[i].x - telefonos[i].z)
        temporal = max(temporal, casos[5] - telefonos[i].y - telefonos[i].z)
        temporal = max(temporal, casos[6] - telefonos[i].x - telefonos[i].y - telefonos[i].z)
        if (costo > temporal) :
            costo = temporal
            ub = i+1
            
print(costo, ub, end= '\n')