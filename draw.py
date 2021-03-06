from display import *
from matrix import *
from gmath import calculate_dot, calculate_normal
from math import cos, sin, pi
from random import randint

MAX_STEPS = 100

def add_polygon( points, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point( points, x0, y0, z0 )
    add_point( points, x1, y1, z1 )
    add_point( points, x2, y2, z2 )
    
def draw_polygons( points, screen, zb, color ):

    if len(points) < 3:
        print 'Need at least 3 points to draw a polygon!'
        return

    p = 0
    while p < len( points ) - 2:

        if calculate_dot( points, p ) < 0:
            ax = points[p + 1][0] - points[ p ][0]
            ay = points[p + 1][1] - points[ p ][1]
            az = points[p + 1][2] - points[ p ][2]
            
            bx = points[p + 2][0] - points[ p ][0]
            by = points[p + 2][1] - points[ p ][1]
            bz = points[p + 2][2] - points[ p ][2]
            normal = calculate_normal( ax, ay, az, bx, by, bz )
            draw_line( screen, zb, points[p][0], points[p][1], points[p][2],
                       points[p+1][0], points[p+1][1], points[p+1][2], color, normal)
            draw_line( screen, zb, points[p+1][0], points[p+1][1], points[p+1][2],
                       points[p+2][0], points[p+2][1], points[p+2][2], color, normal)
            draw_line( screen, zb, points[p+2][0], points[p+2][1], points[p+2][2],
                       points[p][0], points[p][1], points[p][2], color, normal)
            calcscanline(screen, zb, points[p][0], points[p][1], points[p][2], points[p+1][0], points[p+1][1], points[p+1][2], points[p+2][0], points[p+2][1], points[p+2][2] , [randint(0,255),randint(0,255),randint(0,255)],normal)
            calcscanline2(screen, zb, points[p][0], points[p][1], points[p][2], points[p+1][0], points[p+1][1], points[p+1][2], points[p+2][0], points[p+2][1], points[p+2][2] , [randint(0,255),randint(0,255),randint(0,255)],normal)
        p+= 3

def calcscanline(screen,zb,x0,y0,z0,x1,y1,z1,x2,y2,z2,color,normal):
    
    p=[[x0 ,y0, z0],[x1, y1, z1],[x2, y2, z2]]
    p.sort(key = lambda x: -x[1])
    '''
    p[2] is B
    p[1] is M
    p[0] is T
    '''

    ly = p[2][1]
    lx = p[2][0]
    lz = p[2][2]
    ry = p[2][1]
    rx = p[2][0]
    rz = p[2][2]
    

    #BM
    # dx/dy
    try:
        tau1 = (p[1][0] - p[2][0]) / float(p[1][1] - p[2][1])
    except:
        tau1 = 0
    # dz/dy
    try:
        tau2 = (p[1][2] - p[2][2])/ float(p[1][1]- p[2][1])
    except:
        tau2 = 0

    #MT
    # dx/dy
    try:
        tau3 = (p[0][0] - p[1][0])/float(p[0][1]-p[1][1])
    except:
        tau3 = 0
    # dz/dy
    try:
        tau4 = (p[0][2] - p[1][2])/float(p[0][1]-p[1][1])
    except:
        tau4 = 0

    #BT
    # dx/dy
    try:
        tau5 = (p[0][0] - p[2][0]) / float(p[0][1] - p[2][1])
    except:
        tau5 = 0
    # dz/dy
    try:
        tau6 = (p[0][2] - p[2][2])/ float(p[0][1]- p[2][1])
    except:
        tau6 = 0

    if abs(ry - p[1][1]) < 1:
        if rx < p[1][0]:
            rx = p[1][0]
            ry = p[1][1]
            rz = p[1][2]
        else:
            lx = p[1][0]
            ly = p[1][1]
            lz = p[1][2]
            tmp = tau5
            tau5 = tau3
            tau3 = tmp
            tmp = tau6
            tau6 = tau4
            tau4 = tmp
    
    #print "Set:"
    #print [tau1,tau2,tau3,tau4,tau5,tau6]
    #print [(p[0][0],p[0][1],p[0][2]),(p[1][0],p[1][1],p[1][2]),(p[2][0],p[2][1],p[2][2])]
    #print color
    #print [(lx,ly,lz),(rx,ry,rz)]
    if abs(p[2][1] - p[1][1]) > 1:
        draw_line(screen, zb, lx - tau5, ly - 1, lz - tau6, rx - tau1, ry - 1, rz - tau2, color,normal)
    else:
        draw_line(screen, zb, lx - tau5, ly - 1, lz - tau6, rx - tau3, ry - 1, rz - tau4, color,normal)
    while p[1][1] - ry >= 1:
        draw_line(screen, zb, lx, ly, lz, rx, ry, rz, color,normal)
        ry += 1
        ly += 1
        rx += tau1
        lx += tau5
        rz += tau2
        lz += tau6
    #print [(lx,ly,lz),(rx,ry,rz)]
    draw_line(screen, zb, lx, ly, lz, rx , ry , rz , color,normal)
    #if abs(p[2][1] - p[1][1]) > 1:
    #    rx = p[1][0]
    #    ry = p[1][1]
    #    rz = p[1][2]      
    while p[0][1] - ry >= 1:
        draw_line(screen, zb, lx, ly, lz, rx, ry, rz, color,normal)
        ry += 1
        ly += 1
        rx += tau3
        lx += tau5
        rz += tau4
        lz += tau6    
        

def calcscanline2(screen,zb,x0,y0,z0,x1,y1,z1,x2,y2,z2,color,normal):
    
    p=[[x0 ,y0, z0],[x1, y1, z1],[x2, y2, z2]]
    p.sort(key = lambda x: x[1])
    '''
    p[2] is T
    p[1] is M
    p[0] is B
    '''

    ly = p[2][1]
    lx = p[2][0]
    lz = p[2][2]
    ry = p[2][1]
    rx = p[2][0]
    rz = p[2][2]
    

    #TM
    # dx/dy
    try:
        tau1 = (p[1][0] - p[2][0]) / float(p[1][1] - p[2][1])
    except:
        tau1 = 0
    # dz/dy
    try:
        tau2 = (p[1][2] - p[2][2])/ float(p[1][1]- p[2][1])
    except:
        tau2 = 0

    #MB
    # dx/dy
    try:
        tau3 = (p[0][0] - p[1][0])/float(p[0][1]-p[1][1])
    except:
        tau3 = 0
    # dz/dy
    try:
        tau4 = (p[0][2] - p[1][2])/float(p[0][1]-p[1][1])
    except:
        tau4 = 0

    #TB
    # dx/dy
    try:
        tau5 = (p[0][0] - p[2][0]) / float(p[0][1] - p[2][1])
    except:
        tau5 = 0
    # dz/dy
    try:
        tau6 = (p[0][2] - p[2][2])/ float(p[0][1]- p[2][1])
    except:
        tau6 = 0

    if abs(ry - p[1][1]) < 1:
        if rx < p[1][0]:
            rx = p[1][0]
            ry = p[1][1]
            rz = p[1][2]
        else:
            lx = p[1][0]
            ly = p[1][1]
            lz = p[1][2]
            tmp = tau5
            tau5 = tau3
            tau3 = tmp
            tmp = tau6
            tau6 = tau4
            tau4 = tmp
    
    #print "Set:"
    #print [tau1,tau2,tau3,tau4,tau5,tau6]
    #print [(p[0][0],p[0][1],p[0][2]),(p[1][0],p[1][1],p[1][2]),(p[2][0],p[2][1],p[2][2])]
    #print color
    #print [(lx,ly,lz),(rx,ry,rz)]
    while ry - p[1][1] > 1:
        draw_line(screen, zb, lx, ly, lz, rx, ry, rz, color,normal)
        ry -= 1
        ly -= 1
        rx -= tau1
        lx -= tau5
        rz -= tau2
        lz -= tau6
    #print [(lx,ly,lz),(rx,ry,rz)]
    draw_line(screen, zb, lx, ly, lz, rx , ry , rz , color,normal)
    #if abs(p[2][1] - p[1][1]) > 1:
    #    lx = p[1][0]
    #    ly = p[1][1]
    #    lz = p[1][2]
    while ry - p[0][1] > 1:
        draw_line(screen, zb, lx, ly, lz, rx, ry, rz, color,normal)
        ry -= 1
        ly -= 1
        rx -= tau3
        lx -= tau5
        rz -= tau4
        lz -= tau6


             
def add_box( points, x, y, z, width, height, depth ):
    x1 = x + width
    y1 = y - height
    z1 = z - depth

    #front
    add_polygon( points, 
                 x, y, z, 
                 x, y1, z,
                 x1, y1, z)
    add_polygon( points, 
                 x1, y1, z, 
                 x1, y, z,
                 x, y, z)
    #back
    add_polygon( points, 
                 x1, y, z1, 
                 x1, y1, z1,
                 x, y1, z1)
    add_polygon( points, 
                 x, y1, z1, 
                 x, y, z1,
                 x1, y, z1)
    #top
    add_polygon( points, 
                 x, y, z1, 
                 x, y, z,
                 x1, y, z)
    add_polygon( points, 
                 x1, y, z, 
                 x1, y, z1,
                 x, y, z1)
    #bottom
    add_polygon( points, 
                 x1, y1, z1, 
                 x1, y1, z,
                 x, y1, z)
    add_polygon( points, 
                 x, y1, z, 
                 x, y1, z1,
	         x1, y1, z1)
    #right side
    add_polygon( points, 
                 x1, y, z, 
                 x1, y1, z,
                 x1, y1, z1)
    add_polygon( points, 
                 x1, y1, z1, 
                 x1, y, z1,
                 x1, y, z)
    #left side
    add_polygon( points, 
                 x, y, z1, 
                 x, y1, z1,
                 x, y1, z)
    add_polygon( points, 
                 x, y1, z, 
                 x, y, z,
                 x, y, z1) 


def add_sphere( points, cx, cy, cz, r, step ):
    
    num_steps = MAX_STEPS / step
    temp = []

    generate_sphere( temp, cx, cy, cz, r, step )
    num_points = len( temp )

    lat = 0
    lat_stop = num_steps
    longt = 0
    longt_stop = num_steps

    num_steps += 1

    while lat < lat_stop:
        longt = 0
        while longt < longt_stop:
            
            index = lat * num_steps + longt

            px0 = temp[ index ][0]
            py0 = temp[ index ][1]
            pz0 = temp[ index ][2]

            px1 = temp[ (index + num_steps) % num_points ][0]
            py1 = temp[ (index + num_steps) % num_points ][1]
            pz1 = temp[ (index + num_steps) % num_points ][2]
            
            if longt != longt_stop - 1:
                px2 = temp[ (index + num_steps + 1) % num_points ][0]
                py2 = temp[ (index + num_steps + 1) % num_points ][1]
                pz2 = temp[ (index + num_steps + 1) % num_points ][2]
            else:
                px2 = temp[ (index + 1) % num_points ][0]
                py2 = temp[ (index + 1) % num_points ][1]
                pz2 = temp[ (index + 1) % num_points ][2]
                
            px3 = temp[ index + 1 ][0]
            py3 = temp[ index + 1 ][1]
            pz3 = temp[ index + 1 ][2]
      
            if longt != 0:
                add_polygon( points, px0, py0, pz0, px1, py1, pz1, px2, py2, pz2 )

            if longt != longt_stop - 1:
                add_polygon( points, px2, py2, pz2, px3, py3, pz3, px0, py0, pz0 )
            
            longt+= 1
        lat+= 1

def generate_sphere( points, cx, cy, cz, r, step ):

    rotation = 0
    rot_stop = MAX_STEPS
    circle = 0
    circ_stop = MAX_STEPS

    while rotation < rot_stop:
        circle = 0
        rot = float(rotation) / MAX_STEPS
        while circle <= circ_stop:
            
            circ = float(circle) / MAX_STEPS
            x = r * cos( pi * circ ) + cx
            y = r * sin( pi * circ ) * cos( 2 * pi * rot ) + cy
            z = r * sin( pi * circ ) * sin( 2 * pi * rot ) + cz
            
            add_point( points, x, y, z )

            circle+= step
        rotation+= step

def add_torus( points, cx, cy, cz, r0, r1, step ):
    
    num_steps = MAX_STEPS / step
    temp = []

    generate_torus( temp, cx, cy, cz, r0, r1, step )
    num_points = len(temp)

    lat = 0
    lat_stop = num_steps
    longt_stop = num_steps
    
    while lat < lat_stop:
        longt = 0

        while longt < longt_stop:
            index = lat * num_steps + longt

            px0 = temp[ index ][0]
            py0 = temp[ index ][1]
            pz0 = temp[ index ][2]

            px1 = temp[ (index + num_steps) % num_points ][0]
            py1 = temp[ (index + num_steps) % num_points ][1]
            pz1 = temp[ (index + num_steps) % num_points ][2]

            if longt != num_steps - 1:            
                px2 = temp[ (index + num_steps + 1) % num_points ][0]
                py2 = temp[ (index + num_steps + 1) % num_points ][1]
                pz2 = temp[ (index + num_steps + 1) % num_points ][2]

                px3 = temp[ (index + 1) % num_points ][0]
                py3 = temp[ (index + 1) % num_points ][1]
                pz3 = temp[ (index + 1) % num_points ][2]
            else:
                px2 = temp[ ((lat + 1) * num_steps) % num_points ][0]
                py2 = temp[ ((lat + 1) * num_steps) % num_points ][1]
                pz2 = temp[ ((lat + 1) * num_steps) % num_points ][2]

                px3 = temp[ (lat * num_steps) % num_points ][0]
                py3 = temp[ (lat * num_steps) % num_points ][1]
                pz3 = temp[ (lat * num_steps) % num_points ][2]


            add_polygon( points, px0, py0, pz0, px1, py1, pz1, px2, py2, pz2 );
            add_polygon( points, px2, py2, pz2, px3, py3, pz3, px0, py0, pz0 );        
            
            longt+= 1
        lat+= 1


def generate_torus( points, cx, cy, cz, r0, r1, step ):

    rotation = 0
    rot_stop = MAX_STEPS
    circle = 0
    circ_stop = MAX_STEPS

    while rotation < rot_stop:
        circle = 0
        rot = float(rotation) / MAX_STEPS
        while circle < circ_stop:
            
            circ = float(circle) / MAX_STEPS
            x = (cos( 2 * pi * rot ) *
                 (r0 * cos( 2 * pi * circ) + r1 ) + cx)
            y = r0 * sin(2 * pi * circ) + cy
            z = (sin( 2 * pi * rot ) *
                 (r0 * cos(2 * pi * circ) + r1))
            
            add_point( points, x, y, z )

            circle+= step
        rotation+= step



def add_circle( points, cx, cy, cz, r, step ):
    x0 = r + cx
    y0 = cy

    t = step
    while t<= 1:
        
        x = r * cos( 2 * pi * t ) + cx
        y = r * sin( 2 * pi * t ) + cy

        add_edge( points, x0, y0, cz, x, y, cz )
        x0 = x
        y0 = y
        t+= step
    add_edge( points, x0, y0, cz, cx + r, cy, cz )

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    xcoefs = generate_curve_coefs( x0, x1, x2, x3, curve_type )
    ycoefs = generate_curve_coefs( y0, y1, y2, y3, curve_type )
        
    t =  step
    while t <= 1:
        
        x = xcoefs[0][0] * t * t * t + xcoefs[0][1] * t * t + xcoefs[0][2] * t + xcoefs[0][3]
        y = ycoefs[0][0] * t * t * t + ycoefs[0][1] * t * t + ycoefs[0][2] * t + ycoefs[0][3]

        add_edge( points, x0, y0, 0, x, y, 0 )
        x0 = x
        y0 = y
        t+= step

def draw_lines( matrix, screen, zb, color ):
    if len( matrix ) < 2:
        print "Need at least 2 points to draw a line"
        
    p = 0
    while p < len( matrix ) - 1:
        draw_line( screen,zb, matrix[p][0], matrix[p][1], matrix[p][2],
                   matrix[p+1][0], matrix[p+1][1], matrix[p+1][2], color,None)
        p+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )


def draw_line( screen, zb, x0, y0, z0, x1, y1, z1, color, normal):
    dx = x1 - x0
    dy = y1 - y0
    dz = z1 - z0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        dz = 0 - dz
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
        tmp = z0
        z0 = z1
        z1 = tmp
    if dx == 0 and dy == 0:
        z_max = max(z0, z1)
        plot(screen, zb, color, x0, y0, z_max,normal)
    elif dx == 0:
        y = y0
        z = z0
        grad = dz / float(dy)
        while y <= y1:
            plot(screen, zb, color,  x0, y, z,normal)
            y = y + 1
            z = z + grad
    elif dy == 0:
        x = x0
        z = z0
        grad = dz / float(dx)
        while x <= x1:
            plot(screen, zb, color, x, y0, z,normal)
            x = x + 1
            z = z + grad
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        z = z0
        grad = dz / float(dy)
        while x <= x1:
            plot(screen, zb, color, x, y,z,normal)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
            z = z + grad
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        z = z0
        grad = dz / float(dy)
        while y <= y1:
            plot(screen, zb, color, x, y, z,normal)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
            z = z + grad
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        z = z0
        grad = dz / float(dy)
        while x <= x1:
            plot(screen, zb, color, x, y,z,normal)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
            z = z + grad
    else:
        d = 0
        x = x0
        y = y0
        z = z0
        grad = dz / float(dy)
        while y <= y1:
            plot(screen, zb, color, x, y,z,normal)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx
            z = z + grad

