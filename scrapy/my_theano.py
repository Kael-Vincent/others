import numpy as  np
import theano.tensor as T
from theano import function
arr = np.random.normal(1.75, 0.1, (4, 5))
print(arr)

stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 求每一行的平均值(0表示列)
print("每一列的平均值:")
result = np.mean(stus_score, axis=0)
print(result)

# 求每一行的平均值(1表示行)
print("每一行的平均值:")
result = np.mean(stus_score, axis=1)
print(result)

print(2**38)

x = T.dscalar('x')
y = T.dscalar('y')
z = x + y
f = function([x,y],z)

f(2,3)