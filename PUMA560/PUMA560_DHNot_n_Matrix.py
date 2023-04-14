# PUMA560's D-H Notation and Matrix

import sympy as sp

conv2Rad = lambda x : x*sp.pi/180  # Degree to Radian

theta1 = sp.symbols('theta1')  # Set symbols
theta2 = sp.symbols('theta2')
theta3 = sp.symbols('theta3')
theta4 = sp.symbols('theta4')
theta5 = sp.symbols('theta5')
theta6 = sp.symbols('theta6')

# a2, a3 : Link Length (between two joint axes)
a2, a3 = sp.symbols('a2 a3')  

# d3, d4 : Link Offset (distance from the origins of Frame in direction of z-axis)
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

# Trans_0to1 = RotZ(theta1)
# Trans_1to2 = RotX(conv2Rad(-90))*RotZ(theta2)
# Trans_2to3 = D_q(a2,0,0)*D_q(0,0,d3)*RotZ(theta3)
# Trans_3to4 = RotX(conv2Rad(-90))*D_q(a3,0,0)*D_q(0,0,d4)*RotZ(theta4)
# Trans_4to5 = RotX(conv2Rad(90))*RotZ(theta5)
# Trans_5to6 = RotX(conv2Rad(-90))*RotZ(theta6)

# Trans_0to2 = sp.simplify(Trans_0to1*Trans_1to2)
# Trans_0to3 = sp.simplify(Trans_0to2*Trans_2to3)
# Trans_0to4 = sp.simplify(Trans_0to3*Trans_3to4)
# Trans_0to5 = sp.simplify(Trans_0to4*Trans_4to5)
# Trans_0to6 = sp.simplify(Trans_0to5*Trans_5to6)