import numpy

sx, sy, sz = 10, 10, 0
plane = numpy.arange(sx * sy).reshape(sy, -1)

for x in range(sx):
    middle_float = numpy.median(plane[x])
    isAlongVertices = False
    middle_int = int(middle_float)


print(plane)
