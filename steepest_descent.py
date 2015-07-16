__author__ = 'Josh Fass'


''' Implementation of projected gradient descent as described in Appendix A
of "Linear Dimensionality Reduction: Survey, Insights, and Generalizations"
(Cunningham and Ghahramani, 2015, JMLR 16)

'''


def proj_grad_descent(init_point,manifold,obj_func,
                    convergence_threshold=0.1,max_iter=100):
    ''' perform projected gradient descent on the provided manifold until
    convergence or timeout'''

    obj_grad = grad(obj_func)
    
    # initialize M in the set of orthonormal matrices of desired dimension
    # M ∈ O^{d×r}
    M = init_point

    # while obj_func(M) has not converged...
    converged = False
    timed_out=False
    n_iter = 0
    while (not converged) and (not timed_out):
        old_M = M

        # calculate free gradient of the objective
        free_grad = obj_grad(M)

        # calculate search direction (eq. 34)

        # while the objective_func(retraction(projection(step))) is not < f(M) - \eps

            # adjust step size using linesearch / retraction (eq. 35)

        # update M


        n_iter += 1
        if n_iter >= max_iter:
        if np.mean((new_M - old_M)**2) < thresh:
            converged = True


    # return M
