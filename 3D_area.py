import trimesh
import sys
import os

a = sys.argv[1]

mfiles = os.listdir(a)

for data in mfiles:
    # Load the mesh from the PLY file
    mesh = trimesh.load('{}/{}'.format(a, data))

    # Calculate the surface area
    surface_area = mesh.area

    print(data,'\t', f"Surface Area: {surface_area} square units")
