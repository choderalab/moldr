__author__ = 'Josh Fass'

'''
This is a partial clone of the excellent MATLAB package for constrained
optimization on manifolds, Manopt (www.manopt.org, Nicolas Boumal).

Defines a manifold base class and a Stiefel manifold subclass.

To-dos:
- Implement Grassmann manifold class
- Write tests

'''

import numpy as np
import numpy.random as npr
from utils import sign

class Manifold():
    ''' skeleton class for subclassing '''
    def __init__(self):
        self.dim = None

    def proj(self,X):
        ''' project X '''
        raise NotImplementedError

    def random_vec(self):
        ''' return a random point on this manifold '''
        return self.proj(npr.randn(self.dim))

    def point_on_manifold(self,X):
        raise NotImplementedError

class StiefelManifold(Manifold):
    ''' The Stiefel manifold is the set of orthonormal n-by-p matrices,
    a Riemannian submanifold of R^(np).
    '''

    def __init__(self,n,p):
        self.n = n
        self.p = p
        self.dim = n*p - 0.5*(p*(p+1))
        self.typical_distance = np.sqrt(p)

    def __str__(self):
        return '{0}x{1} Stiefel manifold'.format(self.n,self.p)

    def inner(self,d1,d2):
        return np.dot(d1,d2)

    def norm(self,d):
        return np.norm(d)

    def proj(self,X,U):
        ''' X is a point on the stiefel manifold,
        U is the object we want to project'''
        skew_XTU = 0.5 * (np.dot(X.T,U) - np.dot(U.T,X))
        XXT = np.dot(X,X.T)
        I = np.eye(len(XXT))
        return np.dot(X,skew_XTU) + np.dot(I - XXT,U)

    def tangent(self,X,U):
        return self.proj(X,U)

    def egrad2rgrad(self,X,U):
        return self.proj(X,U)

    def retraction(self,X,U,t=1.0):
        Y = X + t*U
        Q,R = np.linalg.qr(Y)
        return Q * np.diag(sign(sign(np.diag(R))+0.5))

    def point_on_manifold(self,X):
        ''' check that X is the correct shape and has orthonormal columns'''
        if X.shape == (self.n,self.p) and np.allclose(X.T.dot(X),np.eye(p)):
            return True
        return False

class GrassmannManifold(Manifold):
    ''' this is the manifold of all rank-p subspaces of R^n'''
    def __init__(self):
        self.implemented_ = False
