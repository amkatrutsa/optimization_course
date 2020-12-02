# Optimization Methods

This repository contains seminars resources for the course "Optimization methods" for the 3-rd year students of Department of Control and Applied Mathematics, [MIPT](https://mipt.ru/english/).
Every seminar presents brief review of necessary part of theory covered in lectures and examples of standard tasks for considered topic. 

The main tool in development of efficient optimization methods is numerical linear algebra. 
To refresh your knowledge, you can use the crash course ([ru](./preliminaries/la_crash_course.ipynb), [en](./preliminaries/la_crash_course_en.ipynb)). 

Almost all numerical tests in this repository are performed with [liboptpy](https://github.com/amkatrutsa/liboptpy) library, where you can find easy to use implementations of different optimization methods. Also we use [CVXPY 1.0](https://www.cvxpy.org/index.html) for comparison purpose. 

## Fall term

- Preliminary 
	- Crash course on the numerical linear algebra ([ru](./preliminaries/la_crash_course.ipynb), [en](./preliminaries/la_crash_course_en.ipynb))

- [2016-2019](./Fall2016-2019/README.md) 
- [2020](./Fall2020/README.md)

### Questions

The minimum list of questions ([ru](/MinimumFall.pdf)) on the topics in Fall term.

## Spring term 

- Preliminary
	- Disciplined convex programming and autograd with PyTorch ([ru](preliminaries/dcp_autodiff/dcp_autodiff.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/preliminaries/dcp_autodiff/dcp_autodiff.ipynb), en)
	- Demo of convex optimization power ([ru](preliminaries/demos/demos.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amkatrutsa/MIPT-Opt/blob/master/preliminaries/demos/demos.ipynb), en)
	
- [2017-2019](./Spring2017-2019/README.md)
- [2020](./Spring2020/README.md)


### Questions

The minimum list of questions ([ru](/MinimumSpring.pdf)) on topics of Spring term.

## Advanced and additional topics

1. Nesterov's method and ODE ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/ODE4NesterovAcc/ODE4NesterovAcc.ipynb), en)
2. Sequential quadratic programming 
3. Theory of optimal methods and lower complexity bounds	
4. Mirror descent
5. Optimization methods on Riemanien manifolds	
6. Structured optimization with sparsity conditions
7. Submodular optimization

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
