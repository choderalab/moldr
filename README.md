# moldr
**Manifold optimization for linear dimensionality reduction**

Reproducing and extending: "Linear dimensionality reduction- Survey, Insights, and Generalizations" ([Cunningham and Ghahramani, 2015, JMLR](http://stat.columbia.edu/~cunningham/pdf/CunninghamJMLR2015.pdf)). The main point of the paper is to cast these algorithms as numerical optimization problems over matrices rather than as eigenvalue / generalized eigenvalue problems. When the constraint set is the set of orthonormal matrices, for example, this allows the use of standard techniques from manifold optimization (e.g. projected gradient descent). Surprisingly, they show the suboptimality of eigenvector solutions for several of these problems.

This might provide a useful framework for implementing variants of tICA. Most relevant to the tICA problem is the discussion of Maximum Autocorrelation Factors (section 3.1.5). There they note how the approach can be generalized to seek linear projections that best capture a pre-specified type of dynamical structure (e.g. a linear dynamical system). This could be a useful way to approach "end-to-end" optimization of projections for MSM construction.

They use a MATLAB package for manifold optimization ([manopt](http://www.manopt.org/)). There doesn't appear to be a comparable package in Python, so I started implementing the relevant subset of features from that package in Python (representing Stiefel manifolds and Grassmann manifolds, and a generic first-order projected gradient solver described in appendix A of the paper).
