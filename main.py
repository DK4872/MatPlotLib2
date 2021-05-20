import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# # ZAD1
# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# z = np.linspace(0, 2 * np.pi)
# x = np.sin(z)
# y = 2 * np.cos(z)
# ax.plot(x, y, z)
# ax.legend()
# plt.show()
# plt.savefig('zad1.png')

# # ZAD2
#
# np.random.seed(832145)
#
#
# def randrange(n, vmin, vmax):
#     return (vmax - vmin)*np.random.rand(n) + vmin
#
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# n = 20
#
# for c, m, zlow, zhigh in [('b', 'D', -25, 25), ('g', 'H', 0, 5), ('cyan', 'P', -10, 10),
#                           ('crimson', '*', 0, 25), ('coral', 's', -30, 30)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)
#
# ax.set_xlabel('oś X')
# ax.set_ylabel('oś Y')
# ax.set_zlabel('oś Z')
# plt.show()
# plt.savefig('zad2.png')

# # ZAD4
# fig = plt.figure(figsize=plt.figaspect(0.5))
# ax1 = fig.add_subplot(2, 3, 1, projection='3d')
# ax2 = fig.add_subplot(2, 3, 2, projection='3d')
# ax3 = fig.add_subplot(2, 3, 3, projection='3d')
# ax4 = fig.add_subplot(2, 3, 4, projection='3d')
# ax5 = fig.add_subplot(2, 3, 5, projection='3d')
# ax6 = fig.add_subplot(2, 3, 6, projection='3d')
# _x = np.arange(4)
# _y = np.arange(5)
# _xx, _yy = np.meshgrid(_x, _y)
# x, y = _xx.ravel(), _yy.ravel()
# top = x + y
# bottom = np.zeros_like(top)
# width = depth = 1
# ax1.bar3d(x, y, bottom, width, depth, top, color='coral', shade=True)
# ax2.bar3d(x, y, bottom, width, depth, top, color='gold', shade=True)
# ax3.bar3d(x, y, bottom, width, depth, top, color='lime', shade=True)
# ax4.bar3d(x, y, bottom, width, depth, top, color='gray', shade=True)
# ax5.bar3d(x, y, bottom, width, depth, top, color='dodgerblue', shade=True)
# ax6.bar3d(x, y, bottom, width, depth, top, color='darkslategray', shade=False)
# plt.show()
# plt.savefig('zad4.png')

# # ZAD5
# fig = plt.figure(figsize=plt.figaspect(0.5))
# ax = fig.add_subplot(1, 2, 1, projection='3d')
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# ax.set_zlim(-1.01, 1.01)
# fig.colorbar(surf, shrink=0.5, aspect=5)
# ax = fig.add_subplot(1, 2, 2, projection='3d')
# X = np.arange(-5, 5, 0.1)
# Y = np.arange(-5, 5, 0.1)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=True)
# ax.set_zlim(-1.01, 1.01)
# fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.show()
# plt.savefig('zad5.png')