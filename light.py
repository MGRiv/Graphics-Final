from sys import maxint
from gmath import dot, normalize, norm, scalar_multiply, sub
import math

def ambient(c_a, k_a):
    return c_a * k_a

def diffuse(c_p, k_d, L, N):
    # c_a = ambient light color (list triple)
    # k_a = constant of ambient reflection
    L_hat = normalize(L)
    N_hat = normalize(N)
    return -1 * c_p * k_d * dot(L_hat, N_hat)
    #return 0

def specular(c_p, k_s, L, N, V):
    L_hat = normalize(L)
    N_hat = normalize(N)
    return -1 * dot(sub(scalar_multiply(N_hat, 2 * dot(L_hat, N_hat)), L_hat), normalize(V)) * k_s * c_p
    #return 0

def light(k, c, L, N, V):
    # k = [k_a, k_d, k_s]
    # c = [c_a, c_p]
    if sum(k) - 1 != 0:
        print "Error, k values must add up to 1"
    r = (ambient(c[0], k[0]) + diffuse(c[1], k[1], L, N) + specular(c[1], k[2], L, N, V))
    #m = 2 * maxint + 1
    #q = (r + maxint) * 255 / m
    #return int(q)
    return int(r)
'''
args = [K, C, L, N, V]
'''
def color_light(args):
    K = args[0]
    C = args[1]
    L = args[2]
    N = args[3]
    V = args[4]
    # K = [k_r, k_g, k_b]
    # K stores k values for red green and blue
    # k_r = [k_a, k_d, k_s]
    # C = [c_r, c_g, c_b]
    # c_r = [c_a, c_p]
    # C stores c values for red green and blue
    r = light(K[0], C[0], L, N, V)
    g = light(K[1], C[1], L, N, V)
    b = light(K[2], C[2], L, N, V)
    #print [r,g,b]
    return [r, g, b]
'''
args = [k, c, L, N, V]
'''
def monochrome_light():
    args[0] = k
    args[1] = c
    args[2] = L
    args[3] = N
    args[4] = V
    return [light(k, c, L, N, V) for i in range(2)]

