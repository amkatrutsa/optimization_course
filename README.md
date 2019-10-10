# Optimization Methods

This repository contains seminars resources for the course "Optimization methods" for the 3-rd year students of Department of Control and Applied Mathematics, [MIPT](https://mipt.ru/english/).
Every seminar presents brief review of necessary part of theory covered in lectures and examples of standard tasks for considered topic. 
Also after every seminar students have home assignment which has to be submitted in LaTeX or Jupyter Notebook format before deadline.

The main tool in development of efficient optimization methods is numerical linear algebra. 
To refresh your knowledge, you can use the crash course ([ru](la_crash_course.ipynb), [en](la_crash_course_en.ipynb)). 

Almost all numerical tests in this repository are performed with [liboptpy](https://github.com/amkatrutsa/liboptpy) library, where you can find easy to use implementations of different optimization methods. Also we use [CVXPY 1.0](https://www.cvxpy.org/index.html) for comparison purpose. 

## Fall term

1. Introduction ([ru](/01-Intro/Seminar1.pdf), [en](./01-Intro/Seminar1en.pdf)). Demo of convex optimization power ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/01-Intro/demos.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/01-Intro/demos.ipynb), en)

2. Convex sets ([ru](https://github.com/amkatrutsa/MIPT-Opt/blob/master/02-Convex/Seminar2.pdf), [en](https://github.com/amkatrutsa/MIPT-Opt/blob/master/02-Convex/Seminar2en.pdf))

3. Projection onto set, separation, support hyperplane ([ru](/03-Separation/Seminar3.pdf), [en](./03-Separation/Seminar3en.pdf))

4. Conjugate sets. Farkas' lemma ([ru](/04-Conjugacy/Seminar4.pdf), [en](./04-Conjugacy/Seminar4en.pdf))

5. Introduction to matrix calculus ([ru](/05-MatrixCalculus/Seminar5.pdf), [en](./05-MatrixCalculus/Seminar5en.pdf))

6. Convex functions ([ru](/06-ConvexFunctions/Seminar6.pdf), [en](./06-ConvexFunctions/Seminar6en.pdf))

7. Subdifferential ([ru](/07-Subdifferential/Seminar7.pdf), [en](./07-Subdifferential/Seminar7en.pdf))

8. Feasible direction cone, tangent cone, sharp extremum ([ru](/08-Cones/Seminar8.pdf), [en](/08-Cones/Seminar8en.pdf))

9. Conjugate functions ([ru](/09-ConjugateFunctions/Seminar9.pdf), [en](/09-ConjugateFunctions/Seminar9en.pdf)) + [smoothing demo](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/09-ConjugateFunctions/smooth_demo.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/09-ConjugateFunctions/smooth_demo.ipynb) 

10. Optimality conditions ([ru](/10-OptimalityConditions/Seminar10.pdf), [en](/10-OptimalityConditions/Seminar10en.pdf))

11. Introduction to duality theory ([ru](/11-Duality/Seminar11.pdf), [en](/11-Duality/Seminar11en.pdf))

### Questions

The list of questions ([ru](/MinimumFall.pdf)) about topics in Fall term part of the course that students have to answer to pass the exam.

## Spring term

1. Numerical optimization methods: introduction, convergence speed, classes of methods, black box model, one-dimensional optimization ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/12-NumMethods/Seminar12.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/12-NumMethods/Seminar12.ipynb), [en](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/tree/master/12-NumMethods/Seminar12en.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/12-NumMethods/Seminar12en.ipynb))
	* Applications of convex optimization and CVXPy ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/01-Intro/demos.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/01-Intro/demos.ipynb), en)
	* Disciplined convex programming and autograd with PyTorch ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/dcp_autodiff/dcp_autodiff.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/dcp_autodiff/dcp_autodiff.ipynb), en)
2. Unconstrained optimization problems
	* Gradient descent ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/13-GradDescent/Seminar13.ipynb), [en](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/13-GradDescent/Seminar13en.ipynb))
	* Heavy-ball method and accelerated Nesterov method ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/AccGrad/AccGrad.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/AccGrad/AccGrad.ipynb), en)
	* Newton method ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/14-Newton/Seminar14.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/14-Newton/Seminar14.ipynb), [en](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/14-Newton/Seminar14en.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/14-Newton/Seminar14en.ipynb))
	* Quasi-Newton methods ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/QuasiNewton/quasi_newton.ipynb), [en](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/QuasiNewton/quasi_newton_en.ipynb))
	* Conjugate gradient method ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/15-ConjGrad/Seminar15.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/15-ConjGrad/Seminar15.ipynb), [en](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/15-ConjGrad/Seminar15en.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/15-ConjGrad/Seminar15en.ipynb))
	* Subgradient method and intro to proximal methods (ru, [en](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/Non-smoothProx/seminar.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/Non-smoothProx/seminar.ipynb))

3. Linear programming
	* Simplex method ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/17-LinProgSimplex/Seminar17.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/17-LinProgSimplex/Seminar17.ipynb), [en](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/17-LinProgSimplex/Seminar17en.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/17-LinProgSimplex/Seminar17en.ipynb))
	* Primal interior point method ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/18-LinProgPrimalInterior/Seminar18.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/18-LinProgPrimalInterior/Seminar18.ipynb), [en](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/18-LinProgPrimalInterior/Seminar18en.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/18-LinProgPrimalInterior/Seminar18en.ipynb))

4. Constrained optimization problems
	* Projected gradient method and Frank-Wolfe method ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/19-SimpleStructureSet/Seminar19.ipynb), [en](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/19-SimpleStructureSet/Seminar19en.ipynb))
	* Interior point methods ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/20-InteriorPoint/Seminar20.ipynb), [en](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/20-InteriorPoint/Seminar20en.ipynb))
	* Penalty methods and augmented Lagrangian methods ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/21-Penalty/Seminar21.ipynb), [en](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/21-Penalty/Seminar21en.ipynb))


### Questions

The list of questions ([ru](/MinimumSpring.pdf)) about topics in Spring term part of the course that students have to answer to pass the exam.

## Advanced and additional topics

1. Least squares problem ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/16-LSQ/Seminar16.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/16-LSQ/Seminar16.ipynb), [en](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/16-LSQ/Seminar16en.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/16-LSQ/Seminar16en.ipynb))
2. Nesterov's method and ODE ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/ODE4NesterovAcc/ODE4NesterovAcc.ipynb), en)
3. Sequential quadratic programming 
4. Theory of optimal methods and lower complexity bounds	
5. Mirror descent
6. Gradient descent and beyond
7. Optimization methods on Riemanien manifolds	
8. Structured optimization with sparsity conditions
9. Proximal methods (ru, [en](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/ProxMethods/prox_methods_en.ipynb))
10. Submodular optimization
11. ...


## References

### Books, lecture notes and blogs

* [Stephen Boyd, Lieven Vandenberghe. Convex Optimization](https://www.dropbox.com/s/zukr0b3f1eqfrw9/bv_cvxbook.pdf?dl=0)

* [Y.E. Nesterov. Introductory lectures on convex optimization: A basic course](https://www.amazon.com/Introductory-Lectures-Convex-Optimization-Applied/dp/1461346916/ref=oosr)

* [B.T. Polyak. Introduction to optimization](https://www.amazon.com/Introduction-Optimization-Translations-Mathematics-Engineering/dp/0911575146)

* [Lectures by A. Juditsky at Grenoble UJF](http://ljk.imag.fr/membres/Anatoli.Iouditski/)

* [Matrix Cookbook](https://www.dropbox.com/s/ymsjldwl8qxqlp8/matrixcookbook.pdf?dl=0)

* [Nonlinear Optimization by A. Ruszczy](https://www.dropbox.com/s/w6ax8vzzjdxniaq/Andrzej_Ruszczy_Nonlinear_Optimization.pdf?dl=0)

* [Semidefinite Optimization by M. Laurent & F. Vallentin](https://www.dropbox.com/s/shbad9vtvgbdv01/SDP_book.pdf?dl=0)

* [Convex Optimization: Algorithms and Complexity by S. Bubeck](https://www.dropbox.com/s/kkubqkmd9ni475i/Bubeck15.pdf?dl=0)

* [Blog by S. Bubeck](https://blogs.princeton.edu/imabandit/)

* [Numerical Optimization by J. Nocedal & S. J. Wright](https://www.dropbox.com/s/f27b15vnvrzf7ef/Numerical_Optimization.pdf?dl=0)

* [Lecture notes on Modern Convex Optimization by A. Nemirovski](https://www.dropbox.com/s/gr6addvyxqfqjn0/Lect_ModConvOpt.pdf?dl=0)

* [Review of Stochastic Optimization Algorithms](https://www.cs.ubc.ca/~schmidtm/Documents/2012_Notes_BigN.pdf)

* [Introductory Lectures on Stochastic Optimization by J. Duchi](http://stanford.edu/~jduchi/PCMIConvex/Duchi16.pdf)

* [Practical optimization by P. E. Gill, W. Murray, M. H. Wright](https://www.amazon.com/Practical-Optimization-Philip-Gill/dp/0122839528)

### Related courses

* [Convex optimization by S. Boyd at Stanford](http://stanford.edu/class/ee364a/) ([YouTube video](https://www.youtube.com/watch?v=McLq1hEq3UY&list=PL3940DD956CDF0622))

* [Convex analysis and optimization by D. Bertsekas at MIT](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-253-convex-analysis-and-optimization-spring-2012/)

* [Optimization methods by L. Vandenberghe at UCLA](http://www.seas.ucla.edu/~vandenbe/ee236b/ee236b.html)

* [Minicourse on convex optimization by S. Boyd](http://stanford.edu/~boyd/papers/cvx_short_course.html)

* [Advanced Optimization and Randomized Methods by A. Smola and S. Sra at CMU](http://www.cs.cmu.edu/~suvrit/teach/aopt.html)

* [Convex optimization by S. Sra at UC Berkeley](http://suvrit.de/teach/ee227a/lectures.html)

* [Optimization for Machine Learning by M. Jaggi at EPFL](https://github.com/epfml/OptML_course)

* [Convex Optimization and Approximation by M. Hardt at UC Berkeley](https://ee227c.github.io/)

## Contributing

If you want to send pull-request, please read the following [instruction](./contribution.md)
