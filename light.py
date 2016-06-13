from gmath import dot, normalize, norm, scalar_multiply, sub
import math

def ambient(c_a, k_a):
    return c_a * k_a

def diffuse(c_p, k_d, L, N):
    # c_a = ambient light color (list triple)
    # k_a = constant of ambient reflection
    return c_p * k_d * dot(L, N)/(norm(L) * norm(N))

def specular(c_p, k_s, L, N, V):
    L_hat = normalize(L)
    N_hat = normalize(N)
    return math.pow(dot(sub(scalar_multiply(N, 2 * dot(L_hat, N_hat)), L_hat), V), 2) * k_s * c_p


def light(k, c, L, N, V):
    # k = [k_a, k_d, k_s]
    # c = [c_a, c_p]
    if sum(k) - 1 != 0:
        print "Error, k values must add up to 1"
    return ambient(c[0], k[0]) + diffuse(c[1], k[1], L, N) + specular(c[1], k[2], L, N, V)

def color_light(K, C, L, N, V):
# K = [k_r, k_g, k_b]
# K stores k values for red green and blue
# C = [c_r, c_g, c_b]
# c_r = [c_a, c_p]
# C stores c values for red green and blue
    return [light(K[0], C[0], L, N, V), light(K[1], C[1], L, N, V), light(K[2], C[2], L, N, V)]

def monochrome_light(k, c, L, N, V):
    return [light(k, c, L, N, V) for i in range(2)]
