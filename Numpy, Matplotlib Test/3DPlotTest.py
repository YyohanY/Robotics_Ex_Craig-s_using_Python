import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

x_axis = np.arange(1, 11)
y_axis = np.arange(1, 11)
z_axis = np.arange(1, 11)

test_graph1 = plt.figure(1)

test_graph2 = test_graph1.add_subplot(111, projection = '3d')

test_graph2.plot(x_axis, y_axis, z_axis, 'r')

test_graph2.set_xlabel('axis_x')
test_graph2.set_ylabel('axis_y')
test_graph2.set_zlabel('axis_z')

plt.title('3D Plot Test')
plt.show()

