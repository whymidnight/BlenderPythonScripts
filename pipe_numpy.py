import numpy

sx, sy, sz = 10, 10, 10
plane = numpy.arange(sx * sy).reshape(sy, -1)

spec_a, spec_b = 2, 2
x_length = numpy.median(range(sx))
y_length = numpy.median(range(sy))


# need to spit plane into 4 quadrants
quadrants = numpy.array([
    plane[:sy // 2, :sy // 2],
    plane[:sy // 2, sx // 2:],
    plane[sx // 2:, :sy // 2],
    plane[sx // 2:, sx // 2:],
])

indices = []
h_sx = sx//2
h_sy = sy//2
for i, quadrant in enumerate(quadrants):
    rot_quadrant = numpy.rot90(quadrant, i)
    if i > 1:
        rot_quadrant = numpy.rot90(quadrant, -i+1)
    zero = rot_quadrant[h_sx-3:h_sx, h_sy-3:h_sy]
    indices.append(zero)
    print()
    print(rot_quadrant, zero, sep="\n")
    print()

print(numpy.array(indices).flatten())


"""
for x in range(sx):
    if x == int(elb_float) or x == int(elb_float) + spec_a:
        middle_float = numpy.median(plane[x])
        middle_int = int(middle_float)
        
        for y in range(sy):
            indice = plane[x][y]
            if indice >= middle_int or indice <= middle_int:
                if (middle_float - middle_int) != 0:
                    if indice == middle_int or indice == middle_int + spec_b:
                        print(indice)
"""
