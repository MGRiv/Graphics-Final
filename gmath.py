import math
def calculate_normal( ax, ay, az, bx, by, bz ):
    normal = [0,0,0]
    normal[0] = ay * bz - az * by
    normal[1] = az * bx - ax * bz
    normal[2] = ax * by - ay * bx
    return normal

def calculate_dot( points, i ):
    #get as and bs to calculate the normal
    ax = points[i + 1][0] - points[ i ][0]
    ay = points[i + 1][1] - points[ i ][1]
    az = points[i + 1][2] - points[ i ][2]

    bx = points[i + 2][0] - points[ i ][0]
    by = points[i + 2][1] - points[ i ][1]
    bz = points[i + 2][2] - points[ i ][2]

    normal = calculate_normal( ax, ay, az, bx, by, bz )

    #set up the view vector values
    vx = 0
    vy = 0
    vz = -1
    
    #calculate the dot product

    
    return dot([vx, vy, vz], normal)

def dot(v1, v2):
    return sum([i * j for (i,j) in zip(v1, v2)])


def norm(v):
    return math.sqrt(sum([i**2 for i in v]))

def normalize(v):
    length = float(norm(v))
    return [i/length for i in v]

def scalar_multiply(vec, c):
    return [i * c for i in vec]

def sub(v1, v2):
    return [i - j for (i, j) in zip(v1, v2)]
