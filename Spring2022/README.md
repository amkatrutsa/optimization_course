# Spring term 2022

0. Overview of the term topics and some applications of convex optimization ([ru](./demos/demos.ipynb))

1. Intro to numerical optimization methods. Gradient descent ([ru](./intro_gd.ipynb))

2. How to accelerate gradient descent

   - conjugate gradient method ([ru](./cg.ipynb))
   - heavy-ball method and fast gradient method ([ru](./hb_acc_grad.ipynb))

3. Second order methods: Newton method. Quasi-Newton methods as trade-off between convergence speed and cost of one iterations  ([ru](./newton_quasi.ipynb))

4. Non-smooth optimization problems: subgradient methods and intro to proximal methods

5. Smoothing: smooth minimization of non-smooth functions ([original paper](https://link.springer.com/article/10.1007/s10107-004-0552-5))

6. Simple constrained optimization problems: projected gradient method and Frank-Wolfe method

7. General purpose solvers

    - interior point methods
    - SQP as generalization of interior point methods to non-convex problems

8. How to parallelize optimization methods: penalty method, augmented Lagrangian method and ADMM

9. Stochastic gradient methods: non-convex non-smooth but structured objectives. Training neural networks as a basic example ([ru](./stoch_grad_methods.ipynb))
