import numpy as np
# 矩阵创建
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
# 矩阵加法
c = a + b
# 矩阵乘法
d = np.dot(a, b)
print("矩阵加法结果：\n", c)
print("矩阵乘法结果：\n", d)