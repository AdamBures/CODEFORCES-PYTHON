number = int(input())
lst = []
for i in range(number):
    polyhedrons = str(input())
    lst.append(polyhedrons)

sumarize = 0
for i in lst:
    if i == "Tetrahedron":
        sumarize+=4
    if i == "Cube":
        sumarize+= 6
    if i == "Octahedron":
        sumarize+= 8
    if i == "Dodecahedron":
        sumarize+= 12
    if i == "Icosahedron":
        sumarize+= 20
        
print(sumarize)
