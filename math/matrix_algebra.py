# Matrix Algebra

import numpy as np

a = np.array([[1,2,3],
              [2,7,4]])

b = np.array([[1,-1],
              [0,1]])

c = np.array([[5,-1],
              [9,1],
              [6,0]])

d = np.array([[3,-2,-1],
              [1,2,3]])

u = np.array([6,2,-3,5])

v = np.array([3,5,-1,4])

w = np.array([[1],
             [8],
             [0],
             [5]])

alpha = 6

for matrix in [a,b,c,u,v,w]:
    print matrix.shape
    
print u + v
print u - v
print alpha * u
print np.dot(u,v)
print np.linalg.norm(u)

try:
    print a + c
except ValueError:
    print "a+c is not defined"
print a-c.transpose()
print c.transpose() + 3*d    
print np.dot(b,a)
try:
    print np.dot(b,a.transpose())
except ValueError as err:
    print "dot product of b and a^t is not defined"
