import numpy as np

def GradientDescent(f, gradf, x0, epsilon, num_iter, line_search, 
                    disp=False, callback=None, **kwargs):
	x = x0.copy()
	iteration = 0
	opt_arg = {"f": f, "grad_f": gradf}
	for key in kwargs:
		opt_arg[key] = kwargs[key]
	while True:
		gradient = -gradf(x)
		alpha = line_search(x, gradient, **opt_arg)
		x = x + alpha * gradient
		if callback is not None:
			callback(x)
		iteration += 1
		if disp:
			print("Current function val =", f(x))
			print("Current gradient norm = ", np.linalg.norm(gradf(x)))
		if np.linalg.norm(gradf(x)) < epsilon:
			break
		if iteration >= num_iter:
			break
	res = {"x": x, "num_iter": iteration, "tol": np.linalg.norm(gradf(x))}
	return res

def backtracking(x, descent_dir, **kwargs):
    f = kwargs["f"]
    grad_f = kwargs["grad_f"] 
    if kwargs["method"] == "Armijo":
        beta1 = kwargs["beta1"]
        rho = kwargs["rho"]
        alpha = 1
        while f(x + alpha * descent_dir) >= f(x) + beta1 * alpha * grad_f(x).dot(descent_dir) or np.isnan(f(x + alpha * descent_dir)):
            alpha *= rho
    return alpha
