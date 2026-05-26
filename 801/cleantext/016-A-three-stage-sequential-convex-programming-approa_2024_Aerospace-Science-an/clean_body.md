## 1. Introduction

Both the flight vehicle’s overall design and the realization of advanced guidance technology greatly benefit from trajectory optimization [1,2]. On the one hand, flight performance evaluation based on trajectory optimization has significant implications for the preliminary design of a flight vehicle. On the other hand, with the development of computational guidance and control [3] technology, the distinction between trajectory optimization and guidance is gradually blurring. Taking online optimization results as guidance instructions [4,5] or constructing a “guidance model” based on offline trajectory optimization data [6] are the two main ways to realize advanced guidance. In short, the method must be more accurate and efficient to increase the applicability of trajectory optimization in these scenarios.

Trajectory optimization refers to obtaining the open-loop solution to an optimal control problem. Since the brachistochrone problem was solved in 1696, people have been researching methods [7,8] to solve the optimal control problem for more than three hundred years. In general, there are two types of methods for solving optimal control problems: indirect methods and direct methods. Indirect methods [9] have great advantages in solving simple problems, but they are difficult to implement when the control system is a little complicated. With the improvement of numerical optimization algorithms, it is possible to solve large-scale optimization problems quickly. In this context, direct methods, which transform the optimal control problem into a nonlinear programming (NLP) problem by discretization, have made great progress [7]. Compared with one class of direct methods called shooting methods, the other class called direct collocation methods usually constructs an NLP problem with stronger solvable properties and has more advantages in the expression of the objective function and constraint conditions [10]. However, it is typically difficult to solve an NLP problem, and the performance of the direct method is mostly governed by the nonlinear programming solver.

Over the last few years, many scholars proposed using sequence convex optimization (SCP) approaches to solve trajectory optimization problems [11,12]. The basic idea of SCP approaches is to obtain the solution of the original problem by solving a series of convex optimization subproblems rather than directly solving the NLP problem obtained after transcription. The lossless convexification technique [13] is the core of SCP approaches, which means relaxing the constraints of control to a second-order cone constraint [14]. This technique allows the original problem to be sufficiently simplified while preserving some nonlinearity. SCP approaches have been successfully applied to various flight vehicle trajectory optimization problems, such as rocket launch and landing [15–18], atmospheric reentry [1,19-21], and missile flight [22–24].

Although SCP approaches aim to avoid solving the complex NLP problem directly, they still fall under the category of direct collocation methods. Simple discretization schemes and low-order numerical integration and differentiation were used for problem transcription in the early SCP approaches, which undoubtedly resulted in poor accuracy of results. In fact, by 2010, direct collocation methods based on different transcription methods (including the trapezoidal method, the Hermite–Simpson method [10], the pseudospectral method [25], the hp pseudospectral method [26], and the hp-adaptive pseudospectral method [27]) have successively appeared. In recent years, some advanced transcription methods have been applied in SCP approaches [15,17,21,26,28,29]. In particular, the SCP approach based on hp-adaptive Radau pseudospectral discretization (RPD) was proposed [20] and successfully applied to a single-channel control reentry problem.

Initial value guessing is a significant aspect that affects the iterative stability of SCP, and to address the issue that the subproblem is intractable because of poor initial guessing, the strategy of adding a penalty function is utilized in most of the related research. Such a strategy has a great impact on the optimality of the solution and is not always effective when the discrete scale is large.

In this paper, we design a robust general three-stage SCP framework based on the hp-adaptive RPD [30] to solve general trajectory optimization problems for flight vehicles. To make the SCP method more stable and efficient and to have the ability to adaptively refine the mesh to meet the discretization accuracy requirement, we divided the iterative process into three stages, i.e., the “constraint relaxation & result approaching stage,” the “mesh refinement stage,” and the “fast convergence stage”. In the second stage, adaptive mesh refinement algorithm is used to improve the discretization accuracy. Before this, due to the small scale of discretization, the iteration will be easily carried out with the help of constraint relaxation, and the possibility of SCP iteration getting stuck due to the infeasibility of the subproblem is greatly reduced. After this, we enter the “fast convergence stage”, that is, introducing damping terms to suppress the iterative oscillation. The superior performance of the proposed approach is verified by two examples.

The remainder of this paper is organized as follows. In Section 2, the general multiple-phase trajectory optimization problem is formulated. Section 3 introduces the three-stage sequential convex programming approach in detail. Section 4 shows numerical simulations and a discussion of the results, and Section 5 summarizes the main work of this paper.

## 2. Problem formulation

Without loss of generality, consider a multiple-phase trajectory optimization problem $\mathscr {P} _ {0}$ defined by Eq.(1). The superscript (p) is used to indicate the phase to which variables belong, and the subscripts s and f represent the initial and terminal moments, respectively. The state of the dynamic system is described byx ∈ Rn, and the control is described by $\mathbf {u} \in \mathbb {R} ^ {m}$ . The Bolza type cost (objective) function J includes two parts: the terminal objective and the integral objective. The system dynamics constraints and the path constraints are established in each phase, and we call $\mathbf {f} ^ {( p )} : \mathbb {R} ^ {n + m + 1} {} \mathbb {R} ^ {n}$ and $\mathbf {c} ^ {( p )}$ dynamics functions and path functions, respectively. The boundary function b of the endpoint (means initial and terminal) states and time of all phases is used to describe the boundary constraints.

$$\begin{array} {r c l} {\displaystyle \mathcal {P} _ {p} : \mathrm{minimize} J} & {=} & {\displaystyle \varphi \Big [ {\pmb x} ^ {( P )} \left( t _ {f} ^ {( P )} \right) \Big ] + \sum _ {p = 1} ^ {P} \int _ {t _ {s} ^ {( P )}} ^ {t _ {f} ^ {( P )}} L ^ {( p )} \big ( \mathbf {x} ^ {( p )} , \mathbf {u} ^ {( p )} \big ) \mathrm{d} t} \\ {\mathrm{subject~to~} \dot {\mathbf {x}}} & {=} & {\mathbf {f} ^ {( p )} \big ( \mathbf {x} ^ {( p )} , \mathbf {u} ^ {( p )} \big ) , p = 1 , \cdots , P} \\ {\displaystyle \qquad \pmb {\mathbb {c}}} & {\leq} & {\mathbf {c} ^ {( p )} \left( x ^ {( p )} , u ^ {( p )} \right) \leq \overline {{\mathbf {c}}} , p = 1 , \cdots , P} \\ {\displaystyle \qquad \quad \mathbf {b}} & {\leq} & {\mathbf {b} \Big [ \mathbf {x} ^ {( 1 )} \left( t _ {s f} ^ {( 1 )} \right) , t _ {s f} ^ {( 1 )} , \cdots , \mathbf {x} ^ {( P )} \left( t _ {s f} ^ {( P )} \right) , t _ {s f} ^ {( P )} \Big ] \leq \overline {{\mathbf {b}}}} \end{array}\tag{1}$$

Dynamical constraints are crucial considerations in trajectory optimization, and the dynamical function $\mathbf {f} ^ {( p )}$ can generally be decomposed into three parts as shown in Eq.(2). The first term, $\mathbf {f} _ {0} ^ {( p )}$ , typically does not explicitly include the control u. The second term is a linear function about u which should be a reasonable choice to ensure linearity, and matrix $\mathbf {B} ^ {( p )}$ could be approximated as constant in each iteration. The third term $\mathbf {f} _ {\varepsilon} ^ {( p )}$ is an additional nonlinear function that has a relatively minor effect on the system compared to the first two terms and could also be approximated as constant. The purpose of decomposing the dynamic function is to simplify the convexification process of the original problem, ultimately facilitating the application of the SCP approach. Since the path and boundary constraints in problem $\mathcal {P} _ {0}$ are typically linear constraints of $\mathbf {x} ,$ they do not require convexification (even if some nonlinear constraints are present, they can be directly linearized).

$$\mathbf {f} ^ {( p )} \left( \mathbf {x} ^ {( p )} , \mathbf {u} ^ {( p )} \right) = \mathbf {f} _ {0} ^ {( p )} \left( \mathbf {x} ^ {( p )} \right) + \mathbf {B} ^ {( p )} \mathbf {u} ^ {( p )} + \mathbf {f} _ {\varepsilon} ^ {( p )}\tag{2}$$

It is worth noting that not all trajectory optimization problems are time-based; instead, they employ different independent variables to characterize the motion of the system, such as energy. Hence, in these cases, the symbol “t” should be considered a generalized argument of the dynamic system. In addition, whether the function in problem $\mathscr {P} _ {0}$ contains t explicitly or not, we omit t in the function to simplify writing.

## 3. Methodology

The basic idea of using a direct collocation method for trajectory optimization is to convert the original problem into a mathematical programming problem about the state, control, and other parameters through discretization, in which the conversion process is called “transcription.” In Section 3.1, we briefly describe the transcription process of this method and subsequently elaborate on the specific details of the three-stage SCP approach proposed in this paper.

## 3.1. Direct collocation method with hp RPD

The terminology “hp” mentioned earlier refers to the length of the segments and the interpolating polynomial order (corresponding to the number of knot points) used in the discretization scheme. Fig. 1 displays the Radau pseudospectral discretization process for a multiple-phase trajectory. Firstly, the initial and terminal moments for the pth phase $( \mathfrak {P} _ {p} )$ are denoted as $t _ {s} ^ {( p )}$ and $t _ {f} ^ {( p )}$ , respectively. Next, the time intervals of phase $\mathfrak {P} _ {p}$ are discretized into $S ^ {( p )}$ segments $( \mathfrak {S} _ {:} ^ {( p )} )$ using the proportion $k ^ {( s , p )} , ( s = 1 , \cdots , S ^ {( p )} )$ . Finally, $N _ {d} ^ {( s , p )} + 1$ Legendre-Gauss-Radau (LGR) knot points {τi} (composed by $N _ {d} ^ {( s , p )}$ collocated points and the right-end point) are laid out on each segment. The LGR collocated points are the zeros of $P _ {N - 1} ( \tau ) + P _ {N} ( \tau )$ , where $P _ {N}$ is the Nth degree Legendre polynomial. These points belong to the interval $[ - ~ 1 , 1 ]$ , and they have a affine transformation relationship with t as shown in Fig. 1.

Note that all other right-end points (also known as non-collocation points) participate in the construction of the Lagrange interpolation polynomial of the previous and next segments. Considering that the control variables will not change abruptly, the state will not show obvious turning points at these nodes. Denoting the state and control at all knot points as $\{\mathbf {X} _ {i} ^ {( s , p )} \}$ and $\{\mathbf {U} _ {i} ^ {( s , p )} \}$ , respectively, we proceed to transcribe the original problem ${\mathcal {P}} _ {0}$ Firstly, the terminal term of the objective and the boundary constraints can be represented as follows:

$$\varphi \left[ \mathbf {X} ^ {( P )} \left( t _ {f} ^ {( P )} \right) \right] \Rightarrow \varphi \left( \mathbf {X} _ {f} ^ {\left( S ^ {( P )} , P \right)} \right)\tag{3}$$

$$\mathbf {b} \leq \mathbf {b} \Big [ \mathbf {x} ^ {( 1 )} \Big ( t _ {s , f} ^ {( 1 )} \Big ) , t _ {s , f} ^ {( 1 )} , \cdots , \mathbf {x} ^ {( P )} \Big ( t _ {s , f} ^ {( P )} \Big ) , t _ {s , f} ^ {( P )} \Big ] \leq \overline {{\mathbf {b}}} \Rightarrow$$

$$\mathbf {{b}} \leq \mathbf {{b}} \Big ( \mathbf {X} _ {s , f} ^ {\big ( S ^ {( 1 )} , 1 \big )} , t _ {s , f} ^ {\big ( S ^ {( 1 )} , 1 \big )} , \cdots , \mathbf {X} _ {s , f} ^ {\big ( S ^ {( P )} , P \big )} , t _ {s , f} ^ {\big ( S ^ {( P )} , P \big )} \Big ) \leq \overline {{\mathbf {b}}}\tag{4}$$

Secondly, the continuous path constraints can be equivalently expressed as constraints on all knot points:

$$\begin{array} {l} {{\underline {{\mathsf{c}}} \leq \mathsf{c} ^ {( p )} \leq \bar {\mathbf {c}} \Rightarrow \underline {{\mathsf{c}}} \leq \mathsf{c} ^ {( s , p )} \Big ( \mathbf {X} _ {i} ^ {( s , p )} , \mathbf {U} _ {i} ^ {( s , p )} \Big ) \leq \bar {\mathbf {c}}}} \\ {{\Big ( i = 1 , \cdots , N _ {d} ^ {( s , p )} ; s = 1 , \cdots , S ^ {( p )} ; p = 1 , \cdots , P \Big )}} \end{array}\tag{5}$$

Next, for every term of the integral objective, the transcription is carried out using the Radau quadrature formula:

$$\begin{array} {l} {{\displaystyle \sum _ {p = 1} ^ {P} \int _ {t _ {s} ^ {( p )}} ^ {t _ {f} ^ {( p )}} L ^ {( p )} \left( \mathbf {x} ^ {( p )} , \mathbf {u} ^ {( p )} \right) \mathrm{d} t \Rightarrow}} \\ {{\displaystyle \sum _ {p = 1} ^ {P} \sum _ {s = 1} ^ {S ^ {( p )}} \left[ k ^ {( s , p )} \frac {t _ {f} ^ {( p )} - t _ {s} ^ {( p )}} {2} \sum _ {k = 0} ^ {N _ {d} ^ {( s , p )} - 1} \omega _ {k} L ^ {( s , p )} \left( \mathbf {X} _ {k} ^ {( s , p )} , \mathbf {U} _ {k} ^ {( s , p )} \right) \right]}} \end{array}\tag{6}$$

Finally, we require the system dynamics constraints to be satisfied at collocation points because the purely non-collocation points are the end points of each phase, where the dynamic function is not continuous. On each segment, the continuous state are approximated by a Lagrange interpolation polynomial as $\operatorname{Eq.} ( 7 ) ,$ , where $l _ {k} ^ {N}$ represents the kth basis function of an Nth order Lagrange interpolation.

$$\mathbf {x} ^ {( s , p )} ( \tau ) \approx \sum _ {k = 0} ^ {N _ {d} ^ {( s , p )}} l _ {k} ^ {N _ {d} ^ {( s , p )}} ( \tau ) \mathbf {X} _ {k} ^ {( s , p )}\tag{7}$$

$$\begin{array} {r l} {\frac {t _ {j} ^ {( p )} - t _ {s} ^ {( p )}} {2} \mathbf {f} ^ {( p )} ( \mathbf {x} ^ {( p )} , \mathbf {u} ^ {( p )} ) =} & {\frac {t _ {j} ^ {( p )} - t _ {s} ^ {( p )}} {2} [ \mathbf {f} _ {0} ^ {( p )} ( \mathbf {x} ^ {( p )} ) + \mathbf {B} ^ {( p )} \mathbf {u} ^ {( p )} + \mathbf {f} _ {\varepsilon} ^ {( p )} ]} \\ {\approx} & {\frac {\tilde {t} _ {j} ^ {( p )} - \tilde {T} _ {s} ^ {( p )}} {2} [ \frac {\partial \tilde {t} _ {0} ^ {( p )}} {\partial \mathbf {x}} | \mathbf {x} ^ {( p )} \mathbf {x} ^ {( p )} + \mathbf {B} ^ {( p )} \mathbf {u} ^ {( p )} ] ] +} \\ & {\frac {\mathbf {f} _ {j} ^ {( p )} ( \tilde {\mathbf {x}} ^ {( p )} , \tilde {\mathbf {u}} ^ {( p )} )} {2} ( t _ {j} ^ {( p )} - t _ {s} ^ {( p )} ) - \frac {\tilde {t} _ {j} ^ {( p )} - \tilde {T} _ {s} ^ {( p )}} {2} [ \frac {\partial \mathbf {f} _ {0} ^ {( p )}} {\partial \mathbf {x}} | \mathbf {\Sigma} _ {\kappa ^ {( p )}} \mathbf {\tilde {x}} ^ {( p )} + \mathbf {B} ^ {( p )} \tilde {\mathbf {u}} ^ {( p )} ]} \\ & = \frac {\tilde {t} _ {j} ^ {( p )} - \tilde {T} _ {s} ^ {( p )}} {2} [ \mathbf {A} ^ {( p )} \mathbf {x} ^ {( p )} + \mathbf {B} ^ {( p )} \mathbf {u} ^ {( p )} ] + \mathbf {C} ^ {( p )} [ t _ j \end{array}$$

Then, the system dynamics constraints on each segment can be expressed as follows:

$$\begin{array} {l} {{\displaystyle \sum _ {k = 0} ^ {N _ {d} ^ {( s , p )}} \left( {\bf X} _ {k} ^ {( s , p )} \frac {\mathrm{d} l _ {k} ^ {N _ {d} ^ {( s , p )}} ( \tau )} {\mathrm{d} \tau} \Bigg \vert _ {\tau _ {j} ^ {( s , p )}} \right) \approx \frac {t _ {f} ^ {( s , p )} - t _ {s} ^ {( s , p )}} {2} \dot {\bf x} ^ {( s , p )} \left( t _ {j} ^ {( s , p )} \right)} \ ~} \\ {{\displaystyle = k ^ {( s , p )} \frac {t _ {f} ^ {( p )} - t _ {s} ^ {( p )}} {2} {\bf f} ^ {( s , p )} \left( {\bf X} _ {j} ^ {( s , p )} , {\bf U} _ {j} ^ {( s , p )} \right) , \left( j = 0 , \cdots , N _ {d} ^ {( s , p )} - 1 \right)}} \end{array}\tag{8}$$

Write the above formula in matrix form as follows (to simplify

writing, N is used to represent $N _ {d} ^ {( s , p )} )$

$$\mathbf {D} ^ {( s , p )} \mathbf {X} ^ {( s , p )} = \mathbf {F} ^ {( s , p )}\tag{9}$$

where

$$\mathbf {X} ^ {( s , p )} = \left[ \mathbf {X} _ {0} ^ {( s , p )} , \cdots , \mathbf {X} _ {N} ^ {( s , p )} \right] ^ {T}$$

$$\mathbf {F} ^ {( s , p )} = k ^ {( s , p )} \frac {t _ {f} ^ {( p )} - t _ {s} ^ {( p )}} {2} \left[ \begin{array} {c} {\mathbf {f} ^ {( s , p )} \left( \mathbf {X} _ {0} ^ {( s , p )} , \mathbf {U} _ {0} ^ {( s , p )} \right) ^ {T}} \\ {\vdots} \\ {\mathbf {f} ^ {( s , p )} \left( \mathbf {X} _ {N - 1} ^ {( s , p )} , \mathbf {U} _ {N - 1} ^ {( s , p )} \right) ^ {T}} \end{array} \right]$$

$$\mathbf {D} ^ {( s , p )} \in \mathbb {R} ^ {N \times ( N + 1 )} , D _ {i j} ^ {( s , p )} = \frac {\mathrm{d} l _ {j} ^ {N} ( \tau )} {\mathrm{d} \tau} \Bigg \vert _ {\tau _ {i} ^ {( s , p )}}$$

Thus, we transcribe the original problem into the following mathematical programming problem $\mathcal {P} _ {\mathrm{NLP}} \mathrm{:}$

$$\begin{array} {r l} {\mathcal {P} _ {\mathrm{NLP}} : ~ \mathrm{minimize}} & {J = \mathrm{Eq.} ( 3 ) + \mathrm{Eq.} ( 6 )} \\ {\mathrm{subjectto}} & {\mathrm{Eq.} ( 4 ) , \mathrm{Eq.} ( 5 ) ~ \mathrm{and}} \\ & {\mathrm{Eq.} ( 9 ) , \mathrm{forall} \left( s , p \right)} \end{array}\tag{10}$$

## 3.2. Fundamental of conventional SCP approach

The fundamental principle of the SCP approach is to convexify problem $\mathcal {P} _ {\mathrm{NLP}}$ at a reference solution, solve the convex optimization subproblems, and update the reference solution until the convergence requirement is met. The main non-convexity is reflected in $\operatorname{Eq.} ( 9 )$ , which requires linearization of the system function at the reference solution of endpoint time, state and control (denoted as $\widetilde {t} _ {s , f} ^ {( p )} , \widetilde {\mathbf {x}} ^ {( p )}$ , and $\widetilde {\mathbf {u}} ^ {\left( p \right)}$ , respectively) as follows:

(11)

Notably, the first K dimensions of control (which commonly indicate the direction cosines and amplitude of the control force vector) must be limited as follows:

$$\| \mathbf {u} _ {1 : K - 1} ^ {( p )} \| _ {2} = \mathbf {u} _ {K} ^ {( p )}\tag{12}$$

In most cases, converting this constraint into the following secondorder cone constraint is a lossless convexification process (and the detailed proof can be found in references [12,13]):

$$\| \mathbf {u} _ {1 : K - 1} ^ {( p )} \| _ {2} \leq \mathbf {u} _ {K} ^ {( p )}\tag{13}$$

Substituting Eq.(11) into Eq.(9) yields:

$$\begin{array} {r l} {\mathbf {D} ^ {( s , p )} \mathbf {X} ^ {( s , p )} =} & {k ^ {( s , p )} \frac {\widetilde {t} _ {f} ^ {( p )} - \widetilde {t} _ {s} ^ {( p )}} {2} \left\{\left[ \mathbf {A} _ {0} ^ {( s , p )} \mathbf {X} _ {0} ^ {( s , p )} , \cdots , \mathbf {A} _ {N - 1} ^ {( s , p )} \mathbf {X} _ {N - 1} ^ {( s , p )} \right] ^ {T} + \left[ \mathbf {B} _ {0} ^ {( s , p )} \mathbf {U} _ {0} ^ {( s , p )} , \cdots , \mathbf {B} _ {N - 1} ^ {( s , p )} \mathbf {U} _ {N - 1} ^ {( s , p )} \right] ^ {T} \right\} +} \\ & {k ^ {( s , p )} \left[ \mathbf {C} _ {0} ^ {( s , p )} \left[ t _ {f} ^ {( p )} \right] , \cdots , \mathbf {C} _ {N - 1} ^ {( s , p )} \left[ t _ {f} ^ {( p )} \right] \right] ^ {T} + k ^ {( s , p )} \left[ \zeta _ {0} ^ {( s , p )} , \cdots , \zeta _ {N - 1} ^ {( s , p )} \right] ^ {T}} \end{array}$$

Because Eq.(14) is in the form of matrices and is given in segments, we have to flatten and consolidate all variables and constraints for programming. Firstly, flatten the state and control matrices by rows as:

$$\begin{array} {r l} & {\overline {{\mathbf {X}}} ^ {\left( s , p \right)} : = \overline {{\mathbf {X} ^ {\left( s , p \right)}}} = \left[ \left( \mathbf {X} _ {0} ^ {\left( s , p \right)} \right) ^ {T} , \cdots , \left( \mathbf {X} _ {N} ^ {\left( s , p \right)} \right) ^ {T} \right] ^ {T}} \\ & {\overline {{\mathbf {U}}} ^ {\left( s , p \right)} : = \overline {{\mathbf {U} ^ {\left( s , p \right)}}} = \left[ \left( \mathbf {U} _ {0} ^ {\left( s , p \right)} \right) ^ {T} , \cdots , \left( \mathbf {U} _ {N} ^ {\left( s , p \right)} \right) ^ {T} \right] ^ {T}} \end{array}\tag{15}$$

then, the left-hand side of $\operatorname{Eq.} ( 14 )$ is processed as follows:

(14)

$$\overrightarrow {\mathbf {D} ^ {( s , p )} \mathbf {X} ^ {( s , p )}} = \overline {{\mathbf {D}}} ^ {( s , p )} \overline {{\mathbf {X}}} ^ {( s , p )}\tag{16}$$

where (⊗ represents the Kronecker product and ${\mathbf I} _ {n}$ represents the n ×n identity matrix)

$$\overline {{\mathbf {D}}} ^ {( s , p )} = \mathbf {D} ^ {( s , p )} \otimes \mathbf {I} _ {n}$$

and the right-hand side of Eq.(14) equation is processed as:

$$\overrightarrow {\mathbf {F} ^ {( s , p )}} = \overline {{\mathbf {A}}} ^ {( s , p )} \overline {{\mathbf {X}}} ^ {( s , p )} + \overline {{\mathbf {B}}} ^ {( s , p )} \overline {{\mathbf {U}}} ^ {( s , p )} + \overline {{\mathbf {C}}} ^ {( s , p )} \left[ t _ {f} ^ {( p )} \right] + \overline {{\xi}} ^ {( s , p )}\tag{17}$$

where

$$\overline {{\mathbf {A}}} ^ {( s , p )} = k ^ {( s , p )} \frac {\widetilde {t} _ {f} ^ {( p )} - \widetilde {t} _ {s} ^ {( p )}} {2} \left[ \begin{array} {l l l l} {\mathbf {A} _ {0} ^ {( s , p )}} & & & {\mathbf {0}} \\ & {\ddots} & & {\vdots} \\ & & {\mathbf {A} _ {N - 1} ^ {( s , p )}} & {\mathbf {0}} \end{array} \right]$$

$$\overline {{\mathbf {B}}} ^ {( s , p )} = k ^ {( s , p )} \frac {\widetilde {t} _ {f} ^ {( p )} - \widetilde {t} _ {s} ^ {( p )}} {2} \left[ \begin{array} {l l l l} {\mathbf {B} _ {0} ^ {( s , p )}} & & & {\mathbf {0}} \\ & {\ddots} & & {\vdots} \\ & & {\ddots} & & \\ & & {\mathbf {B} _ {N - 1} ^ {( s , p )}} & {\mathbf {0}} \end{array} \right]$$

$$\begin{array} {r} {\overline {{\mathbf {C}}} ^ {( s , p )} = k ^ {( s , p )} \left[ \begin{array} {c} {\mathbf {C} _ {0} ^ {( p )}} \\ {\vdots} \\ {\mathbf {C} _ {N - 1} ^ {( p )}} \end{array} \right] , \overline {{\zeta}} ^ {( s , p )} = k ^ {( s , p )} \left[ \begin{array} {c} {\xi _ {0} ^ {( s , p )}} \\ {\vdots} \\ {\xi _ {N - 1} ^ {( s , p )}} \end{array} \right]} \end{array}$$

Next, we merge the system dynamics constraints within phase $\mathfrak {P} _ {p}$ The state and control of each phase are represented as follows (as adjacent segments share the endpoint, the total number of knot points is $N _ {p + 1} ) \colon$

$$\overline {{\mathbf {X}}} ^ {( p )} = \left[ \begin{array} {l} {\overline {{\mathbf {X}}} ^ {( 1 , p )}} \\ {\vdots} \\ {\overline {{\mathbf {X}}} ^ {\left( {S} ^ {( p )} , p \right)}} \end{array} \right] , \overline {{\mathbf {U}}} ^ {( p )} = \left[ \begin{array} {l} {\overline {{\mathbf {U}}} ^ {( 1 , p )}} \\ {\vdots} \\ {\overline {{\mathbf {U}}} ^ {\left( {S} ^ {( p )} , p \right)}} \end{array} \right] , N _ {p} = \sum _ {s = 1} ^ {S ^ {( p )}} N _ {d} ^ {( s , p )}\tag{18}$$

And let $Z ^ {( p )}$ denote all the variables within phase $\mathfrak {P} _ {p} ;$ :

$${\bf Z} ^ {( p )} = \left[ \begin{array} {c c c c c c c} {\overline {{\bf X}} ^ {( p )}} \\ {\overline {{\bf U}} ^ {( p )}} \\ {t _ {f} ^ {( p )}} \\ {t _ {s} ^ {( p )}} \end{array} \right] \in \mathbb {R} ^ {N _ {Z} ^ {( p )}} , N _ {Z} ^ {( p )} = ( n + m ) \big ( N _ {p} + 1 \big ) + 2\tag{19}$$

Then, the system dynamics constraints within phase $\mathfrak {P} _ {p}$ can be expressed as follows:

$$\mathbf {M} _ {d i f} ^ {( p )} \mathbf {Z} ^ {( p )} = \mathbf {M} _ {d i f} ^ {( p )} \mathbf {Z} ^ {( p )} + \mathbf {G} _ {s y s} ^ {( p )}\tag{20}$$

where (It should be noted that when merging A, B, and $\overline {{\mathbf {D}}} ,$ they do not strictly follow the diagonal distribution, but instead, there may be n or m overlapping columns. So, the size of M(p) and $\mathbf {M} _ {d i f} ^ {\left( p \right)}$ $\mathbf {M} _ {d i f} ^ {\left( p \right)}$ are both $n {\cdot} N _ {p} \times N _ {Z} ^ {( p )} . )$

$$\begin{array} {r l} {{\mathbb M} _ {d \ell} ^ {( j )} =} & {\left[ \begin{array} {l l} {{\mathbb D} ^ {( 1 , p )}} & {0} \\ {\ddots} & {\vdots} \\ {{\mathbb D} ^ {( S ^ {j} , p )}} & {0} \end{array} \right]} \\ {{\mathbb M} _ {s s} ^ {( j )} =} & {\left[ \begin{array} {l l l} {{\mathbb {\overline {{A}}}} ^ {( 1 , p )}} & {\mathbf {\overline {{B}}} ^ {( 1 , p )}} & {{\mathbb {\overline {{C}}}} ^ {( 1 , p )}} \\ {\ddots} & {\ddots} & {\vdots} \\ {{\mathbb {\overline {{A}}}} ^ {( S ^ {j} , p )}} & {\mathbf {\nabla} {\mathbb {B}} ^ {( S ^ {j} , p )}} & {{\mathbb {\overline {{C}}}} ^ {( S ^ {j} , p )}} \end{array} \right]} \\ {{\mathbb G} _ {s s} ^ {( j )} =} & {\left[ \begin{array} {l} {{\mathbb {\overline {{\xi}}}} ^ {( 1 , p )}} \\ {\vdots} \\ {{\mathbb {\overline {{\xi}}}} ^ {( S ^ {j} , p )}} \end{array} \right]} \end{array}$$

Finally, we merge all variables and system dynamics constraints from every phase as follows:

$$\big ( \mathbf {M} _ {d i f} - \mathbf {M} _ {s y s} \big ) \mathbf {Z} = \mathbf {G} _ {s y s}\tag{21}$$

where

$$\begin{array} {r l} {\mathbf {Z} =} & {{} \left[ \begin{array} {l} {\mathbf {Z} ^ {( 1 )}} \\ {\vdots} \\ {\mathbf {Z} ^ {( P )}} \end{array} \right] , \qquad \mathbf {M} _ {d i f} =} & {{} \left[ \begin{array} {l l l l l l} {\mathbf {M} _ {d i f} ^ {( 1 )}} & {} & {} & {} & {} \\ {} & {\ddots} & {} & {} & {} \\ {} & {} & {\mathbf {M} _ {d i f} ^ {( P )}} \end{array} \right]} \end{array}$$

$$\begin{array}{c} \begin{array} {c c l} {\displaystyle \mathbf {M} _ {s y s} =} & {\displaystyle [ \mathbf {M} _ {s y s} ^ {( 1 )}} & \\ & & {\ddots} \\ & & & {\displaystyle \mathbf {M} _ {s y s} ^ {( P )} ]} \\ {\displaystyle N _ {c} =} & {\displaystyle n \sum _ {p = 1} ^ {P} N _ {p} ,} \end{array} ] , ~ \mathbf {G} _ {s y s} = & {[ \begin{array} {l} {\displaystyle \mathbf {G} _ {s y s} ^ {( 1 )}} \\ {\vdots} \\ {\displaystyle \mathbf {G} _ {s y s} ^ {( P )}} \end{array} ]} \\ {\displaystyle N _ {Z} =} & {\displaystyle \sum _ {p = 1} ^ {P} N _ {Z} ^ {( p )}} \end{array}$$

$N _ {c}$ and $N _ {z}$ represent the number of differential constraints and variables, respectively.

If there are nonlinear (non-convex) terms in the objective function, boundary constraints, and path constraints of the original problem, they can be converted into linear functions (constraints) at the reference solution, resulting in the simplified form:

$$J = \mathbf {m} _ {o b j} ^ {T} \mathbf {Z}\tag{22}$$

$${\underline {{\mathbf {G}}}} _ {e n d} \leq \mathbf {M} _ {e n d} \mathbf {Z} \leq {\overline {{\mathbf {G}}}} _ {e n d}\tag{23}$$

$$\underline {{\mathbf {G}}} _ {p a t h} \le \mathbf {M} _ {p a t h} \mathbf {Z} \le \overline {{\mathbf {G}}} _ {p a t h}\tag{24}$$

A trust region with a radius of $\mathbf {\Delta} \Delta _ {\mathrm{x}} , \mathbf {\Delta} \Delta _ {\mathrm{u}} ,$ , etc. for state, control, and other parameters should be set to prevent iteration divergence. These trust region radii are integrated into Δ according to the order of variables in Z to set the following constraint (where $\mathbf {Z} _ {r e f}$ is the vector of reference solution):

$${\bf Z} _ {r e f} - \Delta \le {\bf Z} \le {\bf Z} _ {r e f} + \Delta\tag{25}$$

The trust region and other simple path constraints can be merged into constraints on the variable Z as follows:

$$\underline {{\mathbf {Z}}} \le \mathbf {Z} \le \overline {{\mathbf {Z}}}\tag{26}$$

In conclusion, based on the reference solution, we have constructed a second-order cone programming problem for Z as follows (where ${\bf q} _ {i} ^ {T} {\bf Z}$ represents the extraction of the ith group control that needs to satisfy the second-order cone constraint and $\mathcal {Q} _ {i}$ denotes a second-order cone space):

$$\begin{array} {r l} {\mathcal {P} _ {1} : \mathrm{~minimize~}} & {J = \mathbf {m} _ {o b j} ^ {T} \mathbf {Z}} \\ {\mathrm{subjectto~}} & {\left( \mathbf {M} _ {d i f} - \mathbf {M} _ {s y s} \right) \mathbf {Z} = \mathbf {G} _ {s y s}} \\ & {\underline {{\mathbf {G}}} _ {e n d} \leq \mathbf {M} _ {e n d} \mathbf {Z} \leq \overline {{\mathbf {G}}} _ {e n d}} \\ & {\underline {{\mathbf {G}}} _ {p a t h} \leq \mathbf {M} _ {p a t h} \mathbf {Z} \leq \overline {{\mathbf {G}}} _ {p a t h}} \\ & {\mathbf {q} _ {i} ^ {T} \mathbf {Z} \in \mathcal {Q} _ {i} , ( i = 1 , \cdots , N _ {c} )} \\ & {\mathbf {Z} < \mathbf {Z} < \overline {{\mathbf {Z}}}} \end{array}\tag{27}$$

Assuming the solution of problem $\mathcal {P} _ {1}$ is $\mathbf {Z} _ {o p t :}$ , if $\epsilon _ {\mathrm{iter}} \leq | \mathbf {Z} _ {o p t} -$ $\left. {\mathbf {Z}} _ {r e f} \right| \le \epsilon ,$ the iteration is terminated; otherwise, update ${\bf Z} _ {r e f} = {\bf Z} _ {r e f} +$ $\kappa ( \mathbf {Z} _ {o p t} - \mathbf {Z} _ {r e f} )$ , where κ is the iteration step size. The iteration error tolerance $( \epsilon _ {{\bf x}} , \epsilon _ {{\bf u}} ,$ , etc.) is generally set according to the physical significance of each state, control, and other parameters and then integrated into ϵ like Δ.

## 3.3. Improved hp-Adaptive mesh refinement algorithm

An hp RPD scheme can be determined by the three mesh parameters $S ^ {( : )} , N _ {d} ^ {( : , : )}$ , and $k ^ {( : , : )}$ . The traditional SCP is a process to eliminate the errors brought by linearization, while the discretization error is entirely determined by the mesh parameters. In general, the larger the mesh scale, the smaller the discretization error, but the more difficult it is to solve the subproblem. For this reason, we propose the following adaptive mesh refinement algorithm:

We denoted all variables in the segment $( s , p )$ of the sub-optimization result as $\mathbf {X} _ {o p t} ^ {( s , p )} , \mathbf {U} _ {o p t} ^ {( s , p )} , t _ {s , o p t} ^ {( p )}$ and $t _ {f , o p t} ^ {( p )} ,$ and the corresponding reference values as $\mathbf {X} _ {r e f} ^ {( s . p )} , \ \mathbf {U} _ {r e f} ^ {( s . p )} , \ t _ {s , r e f} ^ {( p )}$ and $t _ {f , r e f} ^ {( p )}$ . These variables satisfy Eq.(14), which can be rewritten as follows (where $\mathbf {F} _ {L} ^ {( s , p )}$ is the right-hand side of the equation) by taking advantage of a property of the Lagrange differential matrix $\mathbf {D} ^ {( s , p )}$ (see Appendix A):

$$\mathbf {X} _ {o p t} ^ {( s , p )} \left( \tau _ {1 : N _ {d} ^ {( s , p )}} \right) = \mathbf {1} \mathbf {X} _ {o p t} ^ {( s , p )} ( \tau _ {0} ) + \left( \mathbf {D} _ {1 : N _ {d} ^ {( s , p )} + 1} ^ {( s , p )} \right) ^ {- 1} \mathbf {F} _ {L} ^ {( s , p )}\tag{28}$$

The discretization error $\varepsilon ^ {( s , p )}$ is represented by the degree to which the variables at $N _ {d} ^ {( s , p )} + 2$ new LGR points violate the equation and is defined as follows:

$$\varepsilon ^ {( s , p )}$$

$$\begin{array} {r l} & {= \operatorname* {m a x} \Bigg \{\Bigg [ \widehat {\mathbf {X}} _ {o p t} ^ {( s , p )} ( \tau _ {0} ) + \Bigg ( \widehat {\mathbf {D}} _ {1 : N _ {d} ^ {( s , p )} + 1} ^ {( s , p )} \Bigg ) ^ {- 1} \widehat {\mathbf {F}} _ {L} ^ {( s , p )} - \widehat {\mathbf {X}} _ {o p t} ^ {( s , p )} \Big ( \tau _ {1 : N _ {d} ^ {( s , p )} + 1} \Big ) \Bigg ]} \\ & {\qquad \mathcal {O} \left[ \left[ \widehat {\mathbf {X}} _ {o p t} ^ {( s , p )} \right] \right] \Bigg \}} \end{array}\tag{29}$$

where the marker above variables indicates the value of the variable or function at the new knot points, ⟦ ⟧ represents to calculate the range of each dimension state, and ⊘ indicates that the matrix and vector are divided by columns. If the maximum discretization error occurs in the ̃nth dimension of the state, then we define the curvature ratio (which represents the ratio of maximum curvature to average curvature) of the state as follows:

$$\rho ^ {( s , p )} : = \frac {2 \operatorname* {m a x} \mathcal {H} ^ {( s , p )}} {\int _ {- 1} ^ {1} \mathcal {H} ^ {( s , p )} \mathrm{d} \tau} , \ \mathcal {H} ^ {( s , p )} = \frac {\left| \ddot {\mathbf {X}} _ {\tilde {n}} ^ {( s , p )} ( \tau ) \right|} {\left[ 1 + \dot {\mathbf {X}} _ {\tilde {n}} ^ {( s , p )} ( \tau ) ^ {2} \right] ^ {2 / 3}}\tag{30}$$

For a given threshold of curvature ratio $\rho _ {\mathrm{max}} , {\mathrm{if}} \ \rho ^ {( s , p )} {\leqslant} \rho _ {\mathrm{may}}$ which

## Algorithm 1

hp-adaptive mesh refinement algorithm.

Input: discretization error $\varepsilon ^ {( : , p )}$ and curvature ratio $\rho ^ {( : p )}$ of phase p; $S ^ {( p )} , N _ {d} ^ {( : , p )} , k ^ {( : , p )} \ {\bf o f}$ 
current mesh; algorithm parameter $( \mathrm{i} . \mathrm{e} . , \rho _ {\mathrm{max}} , \varepsilon _ {\mathrm{max}} , N _ {d \mathrm{min}} ) ;$ 
Output: $\widehat {\boldsymbol {S}} ^ {( p )} , \widehat {N} _ {d} ^ {( : , p )} , \widehat {\boldsymbol {k}} ^ {( : , p )}$ of new mesh; 
1: initialize $\widehat s = 0 ;$ 
2: for s = 1toS(p) do 
3: $\mathbf {i f} \rho ^ {( s , p )} \leq \rho _ {\mathrm{max}}$ then 
4: $\widehat {s} = \widehat {s} + 1 ;$ 
5: $\widehat {\cal N} _ {d} ^ {( \widehat {s} , p )} = {\cal N} _ {d} ^ {( s , p )} + {\cal N} _ {K} ^ {( s , p )} , \widehat {k} ^ {( \widehat {s} , p )} = k ^ {( s , p )} ;$ 
6: else 
7: calculate ν; 
8: for $i = 1 \tplus N _ {K} ^ {( s , p )}$ do 
9: $\widehat {s} = \widehat {s} + 1 ;$ 
10: $\widehat {N} _ {d} ^ {( \widehat {s} , p )} = N _ {d \operatorname* {m i n}} , \widehat {k} ^ {( \widehat {s} , p )} = k ^ {( s , p )} \nu _ {i} ;$ 
11: end for 
12: end if 
13: end for 
14: $\widehat {\boldsymbol {s}} ^ {( p )} = \widehat {\boldsymbol {s}} ;$

indicates that the state ${\bf x} _ {\tilde {n}}$ in this segment changes slightly, in order to improve the accuracy, we just increase the number of LGR knot points $\mathsf{by} N _ {K} ^ {( s , p )}$ . Otherwise, we need to divide this segment into $N _ {K} ^ {( s , p )}$ subsegments. The integer. $N _ {K} ^ {( s , p )}$ . is calculated as follows (where $\varepsilon _ {\mathrm{max}}$ is the allowable discretization error and ⌈⌉ means round up):

$$N _ {K} ^ {( s , p )} = \left\lceil \log _ {10} \frac {\varepsilon ^ {( s , p )}} {\varepsilon _ {\mathrm{max}}} \right\rceil\tag{31}$$

The sequence of $N _ {K} ^ {\left( s , p \right)} - 1$ partition positions is determined according to the following formula, which makes all sub-segments have similar curvature distributions.

$$\frac {\int _ {- 1} ^ {\Gamma _ {i}} {\left( \mathcal {K} ^ {\left( s , p \right)} \right) ^ {\frac {1} {3}} \mathrm{d} \tau}} {\int _ {- 1} ^ {1} {\left( \mathcal {K} ^ {\left( s , p \right)} \right) ^ {\frac {1} {3}} \mathrm{d} \tau}} = \frac {i} {N _ {K} ^ {\left( s , p \right)}} , \left( i = 1 , \cdots , N _ {K} ^ {\left( s , p \right)} - 1 \right)\tag{32}$$

The fraction vector ν between all sub-segments and the original segment is defined as:

$$\pmb {\nu} : = \frac {\mathbf {\Gamma} \Gamma _ {f} - \mathbf {\Gamma} \Gamma _ {s}} {2}\tag{33}$$

where

$$\begin{array} {l l l} {\Gamma _ {f} = \Big [ \Gamma _ {1}} & {\cdots} & {\Gamma _ {N _ {K} ^ {\left( s , p \right)} - 1} \quad 1 \Big ] ^ {T} {} _ {s}} \\ {\Gamma _ {s} = \Big [ - 1} & {\Gamma _ {1}} & {\cdots} & {\Gamma _ {N _ {K} ^ {\left( s , p \right)} - 1} \Big ] ^ {T}} \end{array}$$

Finally, we apply the mesh refinement algorithm of one segment (as shown in Algorithm 1) to all segments to complete the entire mesh

refinement.

## 3.4. The three-stage scp approach

To make sequence optimization more stable and efficient, the iteration process should be carefully designed. Next, we will introduce the proposed three-stage SCP in detail, the flowchart of which is shown in Fig. 2.

The first stage (constraint relaxation & result approaching): In the initial stage of iteration, due to the large deviation between the reference and the real trajectory, the problem is difficult to solve unless the differential constraint that needs to be strictly satisfied is relaxed. Since the use of a penalty function can lead to slow convergence, difficulty in selecting penalty function weights, and a lack of optimality, we use constraint relaxation to address this issue. Specifically, the differential constraint of the subproblem is appropriately relaxed to $\mathcal {P} _ {2}$ as defined by $\operatorname{Eq.} ( 34 )$ , where δ is called the relaxation factor. If problem P 2 still cannot be solved after the first relaxation, then the relaxation factor needs to be doubled and problem $\mathcal {P} _ {2}$ updated until a solution is obtained. It should be noted that many solvers can determine whether a convex optimization problem is feasible immediately [31,32], which is one of the key factors in the growing popularity of SCP. We name the first stage (where the iteration step size is small to avoid divergence) so because its primary objective is to guide the reference trajectory towards the actual trajectory.

$$\begin{array} {r l} {\mathcal {P} _ {2} : \operatorname{minimize}} & {J = \mathbf {m} _ {o b} ^ {T} \mathbf {Z}} \\ {\mathrm{subjectto}} & {| \big ( \mathbf {M} _ {d i f} - \mathbf {M} _ {s s s} \big ) \mathbf {Z} - \mathbf {G} _ {s y s} | \leq \delta | \mathbf {G} _ {s y s} |} \\ & {\underline {{\mathbf {G} _ {e n d}}} \leq \mathbf {M} _ {e n d} \mathbf {Z} \leq \overline {{\mathbf {G}}} _ {e n d}} \\ & {\underline {{\mathbf {G} _ {p a t h}}} \leq \mathbf {M} _ {p a t h} \mathbf {Z} \leq \overline {{\mathbf {G}}} _ {p a t h}} \\ & {\mathbf {q} _ {i} ^ {T} \mathbf {Z} \in \mathcal {Q} _ {i} , ( i = 1 , \cdots , N _ {c} )} \\ & {\underline {{\mathbf {Z}}} < \mathbf {Z} < \overline {{\mathbf {Z}}}} \end{array}\tag{34}$$

The second stage (mesh refinement): When problem $\mathcal {P} _ {1}$ can be solved directly, the iteration enters the second stage (“mesh refinement stage”). In this stage, not only the reference solution is constantly updated, but also the mesh is adaptively updated according to the mesh refinement algorithm described in Section 3.3. Since the construction of sub-problems at this stage has better reference, we can choose a larger iteration step size.

The third stage (fast convergence): As the mesh is updated, the discretization error decreases to a given threshold, and the iteration enters the third stage (“fast convergence stage”). If the previous iteration is still followed, the solution of the subproblem often oscillates due to the use of a fixed step size without line search, which greatly slows down the convergence speed. Therefore, we add a damping term to the optimization objective of the problem in this stage and form the optimization problem $\mathcal {P} _ {3}$ as shown in Eq.(35).

$$\begin{array} {r l} {\mathcal {P} _ {3} : \mathrm{minimize}} & {J = \mathbf {m} _ {o b j} ^ {T} \mathbf {Z} + \eta \| \mathbf {Z} - \mathbf {Z} _ {r e f} \| _ {2}} \\ {\mathrm{subjectto}} & {\left( \mathbf {M} _ {d i f} - \mathbf {M} _ {s y s} \right) \mathbf {Z} = \mathbf {G} _ {s y s}} \\ & {\mathbf {\underline {{G}}} _ {e n d} \leq \mathbf {M} _ {e n d} \mathbf {Z} \leq \overline {{\mathbf {G}}} _ {e n d}} \\ & {\mathbf {\underline {{G}}} _ {p a t h} \leq \mathbf {M} _ {p a t h} \mathbf {Z} \leq \overline {{\mathbf {G}}} _ {p a t h}} \\ & {\mathbf {q} _ {i} ^ {T} \mathbf {Z} \in \mathcal {Q} _ {i} , \left( i = 1 , \cdots , N _ {c} \right)} \\ & {\mathbf {Z} \leq \mathbf {Z} \leq \overline {{\mathbf {Z}}}} \end{array}\tag{35}$$

It is worth noting that the first stage is not always necessary. That is, due to the high linearity of the motion equation (implying that the linearization is not heavily dependent on the selection of reference), the initially formed subproblem can be solved directly even if the initial guess and the final solution are very different. As such, the iteration proceeds directly to the second stage.

## 4. Simulations and discussion

All the following numerical simulations are implemented in a MATLAB environment on a personal desktop with an AMD Ryzen 7 2.90 GHz processor, and the convex optimization subproblems are solved by MOSEK [32] in version 10.0.21. In each example, the initial mesh consists of several segments with the same proportion and the numbers of collocation points are all $N _ {d \operatorname* {m i n}}$ . The initial guess is obtained by linear interpolation of the endpoints. We evaluate the accuracy of the optimization result by comparing it with the solution which is obtained by “ode45” of MATLAB with the control sequence of the optimization result as input on 10,000 equidistant nodes. It should be noted that all variables are dimensionless when solving the problem.

## 4.1. Reentry trajectory optimization with dual-channel control

We first consider a reentry trajectory optimization problem with the objective of determining the optimal control inputs, including the angle of attack and bank angle, to minimize the reentry time or maximize the range. To simplify the problem, many studies [19,20] have specified the profile of the angle of attack and utilized only the bank angle as the control input. In this paper, reentry trajectory optimization with dual-channel control is considered, and the non-time-dependent $\mathrm{dy}$ namic equations are defined by Eq.(36) where $e = m \mu / r - m \nu ^ {2} / 2$ is the negative mechanical energy, r is the radial distance from the center of the Earth to the mass center of the vehicle, θis the longitude, $\phi$ is the latitude, v is the relative velocity, γ is the flight-path angle, $\psi$ is the heading angle, and σ is the bank angle. ω and m are constants, representing the angular velocity of the Earth and the mass of the vehicle, respectively.

$${\begin{array} {r l} {{\frac {\mathrm{d} r} {\mathrm{d} r}}} & {= {\frac {\mathrm{sin} \gamma} {D r}}} \\ {{\frac {\mathrm{d} \rho} {\mathrm{d} \rho}} =} & {{\frac {\mathrm{coving}} {D r}}} \\ {{\frac {\mathrm{d} \phi} {\mathrm{d} r}}} & {= {\frac {\mathrm{coving}} {D r}}} \\ {{\frac {\mathrm{d} \phi} {\mathrm{d} r}}} & {= {\frac {\mathrm{coving}} {D r}}} \\ {{\frac {\mathrm{d} \phi} {\mathrm{d} \rho}} =} & {{\frac {L \times \mathrm{ave}} {D ^ {2} D r}} + \left( {\frac {1} {r D}} - {\frac {\mu} {r ^ {2} + {\frac {3} {2}}}} \right) \mathrm{cov} +} \\ & {\quad 2 \rho \mathrm{covosion} \mu r \quad {\mathrm{ro}} ^ {\mathrm{cosc/ecosc/ecosc/}} + \mathrm{sin} \mathrm{sin} \mathrm{eacosc} {\psi}} \\ & {\quad {\frac {\mathrm{d} \rho} {\mathrm{d} \rho}} -} & {{\frac {L \times \mathrm{in} \sigma} {D ^ {2} D r}} + {\frac {\mathrm{cossing} \mathrm{sing} \mathrm{sing} \mathrm{cosc} {\psi}} {r D}} + {\frac {\mathrm{rosc/ecosc/}} {{\mathrm{sin} \sqrt {2}} \mathrm{roscosc} {\psi}}}} \\ {{\frac {\mathrm{d} \rho} {\mathrm{d} \rho}}} & {=} & {{\frac {\mathrm{7cing}} {D ^ {2} D r}} + {\frac {\mathrm{cossing} \mathrm{cosc/ecosc}} {r D}} + {\frac {\mathrm{rosc/ecosc/ect}} {{\mathrm{sin} \sqrt {2}} \mathrm{roscosc} {\psi}}}} \end{array}}\tag{36}$$

The atmospheric model is the same as in the previous example, and the lift and drag coefficients are defined as follows:

$$\left\{\begin{array} {l} {{C _ {L} = C _ {L 0} + C _ {L 1} \alpha + C _ {L 2} e ^ {C _ {L 3} \nu}}} \\ {{C _ {D} = C _ {D 0} + C _ {D 1} \alpha ^ {2} + C _ {D 2} e ^ {C _ {D 3} \nu}}} \end{array} \right.\tag{37}$$

During reentry, the overload, dynamic pressure, and heat flux must meet the constraints in $\operatorname{Eq.} ( 38 )$ , wherek $\dot {\mathbf {\rho}} _ {Q} = 9.437 \times 10 ^ {- 5}$ . Finally, $C _ {L i} ,$ $C _ {D i}$ and other parameters used in this example are shown in Table 1.

$$\left\{\begin{array} {l l} {q = 0.5 \rho \nu ^ {2} \leq q _ {\operatorname* {m a x}}} \\ {Q = k _ {Q} \rho ^ {0.5} \nu ^ {3.15} \leq Q _ {\operatorname* {m a x}}} \\ {n = \sqrt {L ^ {2} + D ^ {2}} \Big / m \leq n _ {\operatorname* {m a x}}} \end{array} \right.\tag{38}$$

We solve the trajectory with the maximum longitudinal range given the initial and terminal states (exceptθ) in this example. Moreover, the iteration step sizes of the three stages are chosen as 0.35, 0.75, and $0.9 ,$ respectively, and the trust region radii and the iteration error tolerance are selected as follows: $\mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf \Delta \mathbf {} \Delta \mathbf {} \Delta \mathbf \Delta \Delta \mathbf {} \Delta \mathbf {} \Delta \mathbf \Delta \Delta \mathbf {} \Delta \Delta \mathbf \Delta \Delta \mathbf \Delta \Delta \Delta \mathbf {} \Delta \mathbf \Delta \Delta \Delta \mathbf \Delta \Delta \Delta \mathbf \Delta \Delta \Delta \mathbf \Delta \Delta \Delta \Delta \mathbf \Delta \Delta \Delta \Delta \mathbf \Delta \Delta \Delta \Delta \Delta \Delta \Delta \Delta$ m, and $\epsilon _ {\theta , \phi , \gamma , \psi} =$ 0.0001∘ . For other processing details, see Appendix B.

Next, we analyze and discuss the solution results in detail. It can be seen from Fig. 3 that, due to the strong nonlinear characteristics of the reentry motion equations, it takes several iterations of the first stage to make the optimization result of the subproblem close to the convergence value when solving it by the approach proposed in this paper (represented by “SCP with ARPD” later). Taking the evolution of the ψ at e = $4.4 \times 10 ^ {10} \mathrm{J}$ as an example, the significance of adding a damping term in the third stage is illustrated. Fig. 4 shows that, when no damping term is added, 38 iterations are performed in the third stage, accompanied by numerical oscillation. However, when the damping term is added, it only takes 9 iterations to converge, and no oscillation occurs.

For comparison, we use SCP approaches with simple discretization schemes (ED and RPD represent equidistant discretization and hp Radau pseudospectral discretization, respectively, and the selection of knot points is shown in Table 2) and the software GPOPS-II to solve the problem.

From the comparison of altitude and ground track in Fig. $^ {5 ,}$ the results are consistent, while the variation law of inclination angle and angle of attack with time in Fig. 6 has obvious differences. In the results of SCP with ED and RPD, there are mutations of $\sigma ,$ while the results of SCP with ARPD and GPOPS-II are smooth.

The convergence of the maximum $\epsilon _ {\mathrm{iter}}$ of the three SCP approaches is shown in Fig. 7, and it can be observed that the maximum $\epsilon _ {\mathrm{iter}}$ of SCP with ED continuously decreases from the beginning of the iteration, owing to its simple constraint that approximates the derivative by central difference. However, SCP with RPD and ARPD do not reduce the error in the first 7–8 iterations, and in the subsequent iterations, the former had a similar convergence speed to the equidistant scattered method, while SCP with ARPD has a significant increase in convergence speed due to the addition of the damping term. It can be seen from Table 2 that SCP with ARPD has significant advantages over GPOPS-II in terms of discretization scale and CPU time.

Due to the fluctuating trend of the variables in the reentry problem, the discretization accuracy in the mesh refinement stage of SCP depends on dividing the sub-segments rather than competing knot points. As a result, the average number of collocation points in all sub-segments remains around 4 as shown in Fig. $8 ~ ( N _ {d \operatorname* {m i n}} ~ = 4 )$

Table 3 shows the comparison of the solution accuracy for different methods in solving the reentry trajectory optimization problem. It is obvious that SCP with ED has the poorest accuracy, particularly in the maximum relative errors of altitude and ballistic angle, which exceeded 10‰. In comparison to ED, SCP with RPD significantly improves solution accuracy, but at the cost of reduced computational efficiency. The solutions of SCP with ARPD and GPOPS-II have similar accuracy, but the CPU time of the former is less than $^ {7 \ s ,}$ which is only one-tenth of the latter.

## 4.2. Ascent trajectory optimization of launch vehicle

Consider another typical problem, the objective of which is to maneuver the launch vehicle to the GTO orbit while maximizing the remaining fuel in the upper stage. The trajectory consists of two phases, with the first phase beginning with the separation of the booster and ending with the depletion of the core first stage fuel, and the second phase beginning with the termination of the first phase and ending with the rocket entering the orbit.

The equations of motion for a point mass are expressed in Cartesian earth-centered inertial coordinates as:

$$\left\{\begin{array} {l l} {\dot {\mathbf r} = \mathbf v} \\ {\dot {\mathbf v} = - \mu \mathbf r / \| \textbf {r} \| ^ {3} + T \mathbf u / m - \mathbf D / m} \end{array} \right.\tag{39}$$

where $\mathbf {r} = [ r _ {x} , r _ {y} , r _ {z} ] ^ {T}$ is the position, $\mathbf {v} = [ \nu _ {x} , \nu _ {y} , \nu _ {z} ] ^ {T} \mathrm{.}$ is the velocity, $\mu$ is the gravitational parameter, T is the thrust, $\mathbf {u} = {[ u _ {x} , u _ {y} , u _ {z} ]} ^ {T}$ is the thrust direction, and D is the drag force which is defined as:

## Table 4

† The data in parentheses represents the relative error (with the range of the corresponding state as reference) multiplied by 103 .

$$\mathbf {D} = 0.5 \rho \mathbf {v} _ {r e l} ^ {2} C _ {D} S _ {r e f}\tag{40}$$

where the Earth relative velocity $\mathbf {v} _ {r e l}$ with the angular velocity $w = 7.292115 \times 10 ^ {- 5} \mathrm{rad/s}$ is calculated as:

$$\mathbf {v} _ {r e l} = \mathbf {v} - \pmb {\omega} \times \mathbf {r} , \pmb {\omega} = \left[ 0 \quad 0 \quad w \right] ^ {T}$$

and the atmospheric density is modeled as the exponential function:

$$\rho = \rho _ {0} \mathrm{exp} [ \left( r - R _ {e} \right) / \beta ]\tag{41}$$

where $\rho _ {0} = 1.225 \mathrm{kg} / \mathrm{m} ^ {3}$ is the atmospheric density at sea level, $R _ {e} \ =$ 6371kmis the equatorial radius of the Earth, and $\beta = 7.2 \mathrm{km}$ is the density scale height. In this example, the thrust is constant in each phase, so the mass m can be determined according to time. The vehicle properties and trajectory conditions for this problem are taken from reference [33] and are shown in Table 4 (where RAAN refers to the right ascension of the ascending node and AP refers to the argument of periapsis).

† The data in parentheses represents the relative error (with the range of the corresponding state as reference) multiplied by $10 ^ {3}$

In addition, the selection of the iteration step sizes is the same as the previous example, and the trust region radii and the iteration error tolerance are selected as follows: Δrx,y,z = 10km, $\begin{array} {r} {\Delta _ {\nu _ {x , y , z}} = :} \end{array}$ 1km $/ {\bf s} , {\bf \Delta} {\bf a} _ {\bf u} =$ $0.6 , \epsilon _ {r _ {x , y , z}} = 10 ^ {- 3} \mathrm{m} , \epsilon _ {\nu _ {x , y , z}} = 10 ^ {- 6} \mathrm{m/s} ,$ and $\epsilon _ {\mathbf {u}} = 10 ^ {- 8}$ . For other processing details, see Appendix C. In the same way, we use SCP approaches with simple discretization schemes (sparse and dense mesh schemes are selected for both SCP with ED and RPD, and the selection of knot points is shown in Table 5) and the software GPOPS-II to solve this problem. Fig. 9 and Fig. 10 compare the results of different solutions and show that the results are completely consistent overall.

Fig. 11 shows the trend of the maximum $\epsilon _ {\mathrm{iter}}$ of the five SCP solutions, among which residual oscillation occurs in SCP with ED1 and RPD2, but they can still reach the specified tolerance. However, the maximum $\epsilon _ {\mathrm{iter}}$ of SCP with ED2 does not reach the tolerance. The reason for this phenomenon is that too many discrete points make it difficult to solve convex optimization subproblems. Even if the parameters of the subproblems change weakly, the solutions may fluctuate. In contrast, SCP with ARPD has a faster convergence speed and Fig. 12 shows the mesh-feature update after the three-stage SCP enters the second stage. It can be observed that only 3 iterations of mesh refinement are needed to reduce the discretization error below the acceptable tolerance, and only increasing the number of nodes is needed since all variables in the ascending problem are smooth. The average number of collocation points in all sub-segments increases from ${\beta} ( N _ {d \mathrm{min}} = 3 )$ at the beginning to around 7 at the end. The final mesh contains 52 nodes with an “average polynomial order” of 8.3 for all segments.

We summarize and compare the solutions of all simulations in Table 5, in which the flight time and true anomaly angle obtained based on SCP with ED1 have obvious differences compared with other methods. To improve the solution accuracy, many nodes need to be added in SCP with ED2. However, as shown earlier, the simple SCP approach cannot achieve convergence for all variables with 600 knot points. On the other hand, using RPD can achieve higher solution accuracy with fewer knot points, even though the computational efficiency is slightly lower than that of ED. The CPU time of SCP with ARPD is 0.338 s, which is much lower than GPOPS-II. Although other SCPs also have high solver efficiency, their results are generally less accurate. Table 6 provides a detailed comparison of the process accuracy and terminal accuracy of different methods. The errors of SCP with ED1 and

ED2 are very large, especially the semi-major axis error of SCP with ED1, which reaches a maximum of more than 40 km. The result of SCP with ARPD has similar accuracy to that of GPOPS-II and has one to two orders of magnitude improvement compared with SCP with RPD.

## 5. Conclusions

In this paper, a three-stage sequential convex programming approach is proposed for general trajectory optimization problems. Based on constraint relaxation, mesh refinement, and iterative damping, the problems of poor iteration stability, large discretization error, and slow convergence speed of conventional SCP approaches are effectively improved. Numerical simulation results show that compared with other SCP approaches, the accuracy of the proposed approach (almost equivalent to GPOPS-II) is improved by 2–4 orders of magnitude, and the CPU time is reduced to a certain extent. The work in this paper further enhances the potential for onboard real-time application of SCP approaches. Moreover, the proposed approach is based on the general form of trajectory optimization problems, therefore, has universality for application.

The proposed approach still has some limitations. On the one hand, to further accelerate the convergence speed, line search can be used to determine the step size between iterations. On the other hand, it may be more efficient to approximate nonlinear constraints using quadratic functions (which require the use of BFPS, etc., to approximate the Hessian matrix) than simple linearization.

## Omitted Tables

- [Table 1 omitted; saved to tables/table_001.md]
- [Table 2 omitted; saved to tables/table_002.md]
- [Table 3 omitted; saved to tables/table_003.md]
- [Table 4 omitted; saved to tables/table_004.md]
- [Table 5 omitted; saved to tables/table_005.md]
- [Table 6 omitted; saved to tables/table_006.md]
