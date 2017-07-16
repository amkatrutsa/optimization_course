from __future__ import print_function
import numpy as np
import time

class ProjGD():
    '''
    Class represents projected gradient descent method 
    '''
    def __init__(self, maxiter=None, tol=1e-6):
        self.f = None
        self.grad = None
        self.proj = None
        self.maxiter = maxiter
        self.tol = tol
        self.x0 = None
        self.callback = None
        
    def backtracking(self, x, descent_dir, p, c=0.9, rho=0.8):
        alpha = 1
        x_next = self.proj(x + alpha * descent_dir)
        while self.f(x_next, p) >= self.f(x, p) - c * alpha * descent_dir.dot(x_next - x):
            alpha *= rho
            if alpha < 1e-16:
                break
            x_next = self.proj(x + alpha * descent_dir)
        return alpha
    
    def solve(self, f, grad_f, proj, x0, p):
        self.f = f
        self.grad = grad_f
        self.proj = proj
        self.x0 = x0.copy()
        if "callback" in p:
            self.callback = p["callback"]
        x = self.x0.copy() 
        x = self.proj(x)
        x_prev = x.copy()
        if self.callback is not None:
            self.callback(x)
        if "disp" not in p:
            p["disp"] = 1
        i = 1
        start = time.time()
        while True:
            prev_f = self.f(x_prev, p)
            if p["disp"] > 0 and ((i < 10) or (i % 10 == 0 and i >= 10)):
                print("Iteration = {0}: f = {1}".format(i, prev_f))
            current_gradient = self.grad(x, p)
            alpha = self.backtracking(x, -current_gradient, p)
            y = x - alpha * current_gradient
            x = self.proj(y)
            current_f = self.f(x, p)
            f_diff = prev_f - current_f
            x_diff = x - x_prev
            if self.callback is not None:
                self.callback(x)
            if i % 10 == 0 and p["disp"] > 1:
                print("Diff function =", f_diff)
                print("Norm diff x =", np.linalg.norm(x_diff))
            if f_diff <= self.tol: # and np.linalg.norm(x_diff) <= self.tol:
                if p["disp"] > -1:
                    print("Tolerance reached on iteration", i + 1)
                    print("Diff function =", f_diff)
                    print("Norm diff x =", np.linalg.norm(x_diff))
                    print("f* =", current_f)
                break
            if self.maxiter is not None and i == self.maxiter:
                if p["disp"] > -1:
                    print("Max iterations = {0} exceeds".format(self.maxiter))
                    print("Diff function on last iteration =", f_diff)
                    print("Norm diff x on last iteration =", np.linalg.norm(x_diff))
                    print("f* =", current_f)
                break
            x_prev = x.copy()
            i += 1
        fin = time.time()
        return {"x": x, "time": fin - start, "num_iter": i}
    
class CondGD():
    '''
    Class represents conditional gradient descent method aka Frank Wolfe algorithm
    '''
    def __init__(self, maxiter=None, tol=1e-6):
        self.f = None
        self.grad = None
        self.linprogsolver = None
        self.maxiter = maxiter
        self.tol = tol
        self.x0 = None
        self.callback = None
        
    def backtracking(self, x, cond_grad, grad, p, c=0.8, rho=0.5):
        alpha = 1
        while self.f(x + alpha * cond_grad, p) >= self.f(x, p) + c * alpha * grad.dot(cond_grad):
            alpha *= rho
            if alpha < 1e-16:
                break
        return alpha
    
    def solve(self, f, grad_f, linprogsolver, x0, p):
        self.f = f
        self.grad = grad_f
        self.linprogsolver = linprogsolver
        self.x0 = x0.copy()
        if "callback" in p:
            self.callback = p["callback"]
        x = self.x0.copy() 
        x_prev = x.copy()
        if self.callback is not None:
            self.callback(x)
        if "disp" not in p:
            p["disp"] = 1
        i = 1
        start = time.time()
        while True:
            prev_f = self.f(x_prev, p)
            if p["disp"] > 0 and ((i < 10) or (i % 10 == 0 and i >= 10)):
                print("Iteration = {0}: f = {1}".format(i, prev_f))
            current_gradient = self.grad(x, p)
            s = self.linprogsolver(current_gradient)
            cond_grad = s - x
            alpha = self.backtracking(x, cond_grad, current_gradient, p, rho=0.5)
            x = x + alpha * cond_grad
            current_f = self.f(x, p)
            f_diff = prev_f - current_f
            x_diff = x - x_prev
            if self.callback is not None:
                self.callback(x)
            if i % 10 == 0 and p["disp"] > 1:
                print("Diff function =", f_diff)
                print("Norm diff x =", np.linalg.norm(x_diff))
            if f_diff <= self.tol: # and np.linalg.norm(x_diff) <= self.tol:
                if p["disp"] > -1:
                    print("Tolerance reached on iteration", i)
                    print("Diff function =", f_diff)
                    print("Norm diff x =", np.linalg.norm(x_diff))
                    print("f* =", current_f)
                break
            if self.maxiter is not None and i == self.maxiter:
                if p["disp"] > -1:
                    print("Max iterations = {0} exceeds".format(self.maxiter))
                    print("Diff function on last iteration =", f_diff)
                    print("Norm diff x on last iteration =", np.linalg.norm(x_diff))
                    print("f* =", current_f)
                break
            x_prev = x.copy()
            i += 1
        fin = time.time()
        return {"x": x, "time": fin - start, "num_iter": i}