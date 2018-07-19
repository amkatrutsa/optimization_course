# Optimization Methods

This repository contains seminars resources for the course "Optimization methods" for the 3-rd year students of Department of Control and Applied Mathematics, [MIPT](https://mipt.ru/english/).
Every seminar presents brief review of necessary part of theory covered in lectures and examples of standard tasks for considered topic. 
Also after every seminar students have home assignment which has to be submitted in LaTeX or Jupyter Notebook format before deadline.

The main tool in development of efficient optimization methods is numerical linear algebra. 
To refresh your knowledge, you can use the crash course ([ru](la_crash_course.ipynb), [en](la_crash_course_en.ipynb)). 

Almost all numerical tests in this repository are performed with [liboptpy](https://github.com/amkatrutsa/liboptpy) library, where you can find easy to use implementations of different optimization methods.

## Fall term

1. Introduction ([ru](/01-Intro/Seminar1.pdf), [en](./01-Intro/Seminar1en.pdf))

2. Convex sets ([ru](), [en]())

3. Projection onto set, separation, support hyperplane ([ru](/03-Separation/Seminar3.pdf), [en](./03-Separation/Seminar3en.pdf))

4. Conjugate sets. Farkas' lemma ([ru](/04-Conjugacy/Seminar4.pdf), [en](./04-Conjugacy/Seminar4en.pdf))

5. Introduction to matrix calculus ([ru](/05-MatrixCalculus/Seminar5.pdf), [en](./05-MatrixCalculus/Seminar5en.pdf))

6. Convex functions ([ru](/06-ConvexFunctions/Seminar6.pdf), [en](./06-ConvexFunctions/Seminar6en.pdf))

7. Subdifferential ([ru](/07-Subdifferential/Seminar7.pdf), [en](./07-Subdifferential/Seminar7en.pdf))

8. Feasible direction cone, tangent cone, sharp extremum ([ru](/08-Cones/Seminar8.pdf), [en](/08-Cones/Seminar8en.pdf))

9. Conjugate functions ([ru](/09-ConjugateFunctions/Seminar9.pdf), [en](/09-ConjugateFunctions/Seminar9en.pdf))

10. Optimality conditions ([ru](/10-OptimalityConditions/Seminar10.pdf), [en](/10-OptimalityConditions/Seminar10en.pdf))

11. Introduction to duality theory ([ru](/11-Duality/Seminar11.pdf), [en](/11-Duality/Seminar11en.pdf))

### Questions

The list of questions ([ru](/MinimumFall.pdf)) about topics in Fall term part of the course that students have to answer to pass the exam.

## Spring term

1. Numerical optimization methods: introduction, convergence speed, classes of methods, black box model, one-dimensional optimization ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/12-NumMethods/Seminar12.ipynb), [en](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/tree/master/12-NumMethods/Seminar12en.ipynb))

2. Unconstrained optimization problems
	* Gradient descent ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/13-GradDescent/Seminar13.ipynb), [en](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/13-GradDescent/Seminar13en.ipynb))
	* Newton method. Quasi-Newton methods ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/14-Newton/Seminar14.ipynb), en)
	* Conjugate gradients methods ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/15-ConjGrad/Seminar15.ipynb), [en](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/15-ConjGrad/Seminar15en.ipynb))

3. Linear programming
	* Simplex method ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/17-LinProgSimplex/Seminar17.ipynb), en)
	* Primal interior point method ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/18-LinProgPrimalInterior/Seminar18.ipynb), en)

4. Constrained optimization problems
	* Projected gradient method and Frank-Wolfe method ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/19-SimpleStructureSet/Seminar19.ipynb), en)
	* Interior point methods ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/20-InteriorPoint/Seminar20.ipynb), en)
	* Penalty methods and augmented Lagrangian methods ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/21-Penalty/Seminar21.ipynb), [en](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/21-Penalty/Seminar21en.ipynb))


### Questions

The list of questions ([ru](/MinimumSpring.pdf)) about topics in Spring term part of the course that students have to answer to pass the exam.

## Advanced and additional topics

1. Least squares problem ([ru](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/16-LSQ/Seminar16.ipynb), [en](https://nbviewer.jupyter.org/github/amkatrutsa/MIPT-Opt/blob/master/16-LSQ/Seminar16en.ipynb))
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

1. [Stephen Boyd, Lieven Vandenberghe. Convex Optimization](https://www.dropbox.com/s/zukr0b3f1eqfrw9/bv_cvxbook.pdf?dl=0)

2. [Convex optimization course by S. Boyd at Stanford](http://stanford.edu/class/ee364a/)

3. [Convex analysis and optimization course at MIT](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-253-convex-analysis-and-optimization-spring-2012/)

4. [Optimization methods course by L. Vandenberghe at UCLA](http://www.seas.ucla.edu/~vandenbe/ee236b/ee236b.html) 

5. [Y.E. Nesterov. Introductory lectures on convex optimization: A basic course](https://www.amazon.com/Introductory-Lectures-Convex-Optimization-Applied/dp/1461346916/ref=oosr)

6. [B.T. Polyak. Introduction to optimization](https://www.amazon.com/Introduction-Optimization-Translations-Mathematics-Engineering/dp/0911575146)

7. [Lectures by A. Juditsky at Grenoble UJF](http://ljk.imag.fr/membres/Anatoli.Iouditski/)

8. [Matrix Cookbook](https://www.dropbox.com/s/ymsjldwl8qxqlp8/matrixcookbook.pdf?dl=0)

9. [Video lectures by S. Boyd on course Convex Optimization at Stanford](https://www.youtube.com/watch?v=McLq1hEq3UY&list=PL3940DD956CDF0622)

10. [Minicourse on convex optimization by S. Boyd'a](http://stanford.edu/~boyd/papers/cvx_short_course.html)

11. [Nonlinear Optimization by A. Ruszczy](https://www.dropbox.com/s/w6ax8vzzjdxniaq/Andrzej_Ruszczy_Nonlinear_Optimization.pdf?dl=0)

12. [Convex Optimization: Algorithms and Complexity by S. Bubeck](https://www.dropbox.com/s/kkubqkmd9ni475i/Bubeck15.pdf?dl=0)

13. [Blog by S. Bubeck](https://blogs.princeton.edu/imabandit/)

14. [Numerical Optimization by J. Nocedal & S. J. Wright](https://www.dropbox.com/s/f27b15vnvrzf7ef/Numerical_Optimization.pdf?dl=0)

15. [Lectures on Modern Convex Optimization by A. Nemirovski](https://www.dropbox.com/s/gr6addvyxqfqjn0/Lect_ModConvOpt.pdf?dl=0)

16. [Review of Stochactic Optimization Algorithms](https://www.cs.ubc.ca/~schmidtm/Documents/2012_Notes_BigN.pdf)

17. [Semidefinite Optimization by M. Laurent & F. Vallentin](https://www.dropbox.com/s/shbad9vtvgbdv01/SDP_book.pdf?dl=0)

## Contributing

If you want to send pull-request, please read the following [instruction](./contribution.md)
