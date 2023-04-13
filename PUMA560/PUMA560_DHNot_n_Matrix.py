# PUMA560's D-H Notation and Matrix

import sympy as sp

conv2Rad = lambda x : x*sp.pi/180  # Degree to Radian

theta1 = sp.Symbol('theta1')  # Set symbols
theta2 = sp.Symbol('theta2')
theta3 = sp.Symbol('theta3')
theta4 = sp.Symbol('theta4')
theta5 = sp.Symbol('theta5')
theta6 = sp.Symbol('theta6')

a2, a3 = sp.Symbol('a2 a3')
d3, d4 = sp.symbols('d3 d4')

# Rotation Matrix : z-axis
def RotZ(a) :
    return sp.Matrix( [ [sp.cos(a), -sp.sin(a), 0, 0],
                       [sp.sin(a), sp.cos(a), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])

# Rotation Matrix : x-axis
def RotX(a) :
    return sp.Matrix( [ [1, 0, 0, 0],
                       [0, sp.cos(a), -sp.sin(a), 0],
                       [0, sp.sin(a), sp.cos(a), 0],
                       [0, 0, 0, 1] ] )

# Translation Matrix
def D_q(a1, a2, a3) :
    return sp.Matrix( [ [1, 0, 0, a1],
                       [0, 1, 0, a2],
                       [0, 0, 1, a3],
                       [0, 0, 0, 1] ] )