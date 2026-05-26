## 1. Introduction

Trajectory optimization plays a key role with regard to improved guidance and control for the reusable vehicle, especially in the reentry phase [1]. In recent decades, many methods have been proposed to address trajectory optimization problems [2,3]. Considering the high flight safety requirements and unpredictable flight states, improving the performance of trajectory optimization, including stability, computational efficiency, and result accuracy, is very important [4–6].

With the development of computer technology, the optimal control theory is gradually applied to trajectory design [7]. The main trajectory optimization methods can be classified as direct methods and indirect methods based on the algorithm framework. In comparison to the indirect method, it is much more efficient to apply the direct method to handle the trajectory design problem [3,8–10]. Nevertheless, obtaining the solution to a complicated trajectory optimization problem is no longer the primary aim today, and improving the abovementioned algorithm performance is the main trend of trajectory optimization research at present. The rapid generation of an accurate reference trajectory plays a crucial role in guidance effects and flight safety [11–13]. On the one hand, the boundary between onboard optimal guidance and trajectory optimization has become more and more blurred [14]. On the other hand, using a high-performance trajectory optimization algorithm to generate reference trajectory is also very beneficial to the implementation of some control algorithms like Deterministic Artificial Intelligence controller [15].

In recent years, it has been proposed to use sequential convex programming (or cone programming more precisely, and both abbreviated as SCP) methods to solve trajectory optimization problems in aerospace community [16]. The SCP methods have been applied to many engineering problems, including path planning of UAVs [17], optimal control of spacecraft [18,19], trajectory optimization of launch [20,21] and reentry [22–24]. In SCP methods, the normalization constraints of the control variables can be relaxed into cone constraints either directly or by adding regularization terms to the objective function, which is called lossless convexification [22,25–27]. The lossless convexification allows the original problem to be sufficiently simplified while preserving some nonlinearity.

The accuracy of the optimal trajectory obtained by the SCP methods is determined by both the linearization error and the discretization error. The linearization error decreases with the sequence optimization, whereas the discretization error is determined by the destination and differential approximation methods. However, in the general SCP methods, only the very simple destination and differential approximation methods are considered. For example, in references [17], [22], and [28], the authors chose the uniform discretization and set the number of discretized points unaccountably, and adopted the central difference method for the differential approximation. For problems with relatively flat state variation, this method can obtain a high-precision solution, but once the fluctuation is violent, there will be a large discretization error because the uniformly distributed discretized points are difficult to capture the local regulation of some states. In order to improve the integral accuracy of a discretized solution, Wang [29] and Sagliano [30] adopted hp schemes in which the segment division is carried out first, and then pseudospectral discretization and Lagrange polynomial fitting are implemented in each segment; Ma [31] used Chebyshev polynomials for state fitting and differential approximation. These methods use polynomials of a certain order to fit the state curves, which improves the accuracy of the results. However, since discretized points are all given before the iteration, these improved SCP methods can’t control the discretization error automatically. The position of discretized points and the order of the polynomial need to be set artificially, but there is not enough basis to do this before the problem is solved. When the problem is complicated, some attempts are needed to determine the discretization for higher precision, and once more discretized points are required, the computational efficiency will decrease. Therefore, the discretization method and iteration process need to be optimized to reduce the integral error with as few discretized points as possible.

In this paper, the idea of the hp-adaptive pseudospectral method [32–34] is used for reference, and an improved SCP algorithm is proposed. Considering the advantages and disadvantages of the three typical pseudospectral discretization [10], we finally decided to adopt the Radau pseudospectral discretization (RPD) in this paper. The iteration process of the improved SCP is divided into three stages depending on the characteristics of subproblems. At the first stage, a constraint relaxation strategy is adopted, so that the iteration can be carried out under a very simple initial value, whereas in the reference [22], the initial value needs some design. And then, the iteration enters the second stage, during which segment division and node encryption are carried out according to both the current differential error defined at the midpoint to evaluate the discretization error and the curvature of the state with the largest differential error. During the last stage, a regularization term is introduced to accelerate convergence. A typical example shows that the CPU time for the proposed algorithm reduced by 40%-70% when compared to other SCP methods, and is only twentieth of that of GPOPS-II. In addition, Monte Carlo simulation for initial values verifies the insensitivity to initial values of the proposed method.

The remainder of this paper is organized as follows. In Section 2, the original reentry trajectory optimization problem is given. Section 3 introduces hp Radau pseudospectral discretization and the convexification of the original problem. Then, the details of the iterative algorithm are given in Section 4. Numerical simulations and the result discussion are shown in Section 5, and Section 6 summarizes the main work of this paper.

## 2. Problem formulation

In this section, the formulation of the original reentry trajectory optimization problem is presented, including particle motion equations, constraints and optimization objective. The choice of control variables and the additional normalization constraints added to the control variables are also explained.

## 2.1. Motion equations

For no-power reentry, the motion equations with energy as the independent variable are generally used because the velocity state equation can be omitted. The three-degree-of-freedom motion equations with respect to the negative energy E in an inertial coordinate system (as shown in Fig. 1) are

$$\left\{\begin{array} {l l} {r ^ {\prime} = \sin \gamma / D} \\ {\theta ^ {\prime} = \cos \gamma \sin \psi / r D \cos \phi} \\ {\phi ^ {\prime} = \cos \gamma \cos \psi / r D} \\ {\gamma ^ {\prime} = [ L \cos \sigma / m + ( \upsilon ^ {2} - \mu / r ) \cos \gamma / r + 2 \omega \upsilon \cos \phi \sin \psi} \\ {\quad \quad + r \omega ^ {2} ( \cos \gamma \cos \phi + s i n \gamma \sin \phi \cos \psi ) \cos \phi ] / \upsilon ^ {2} D} \\ {\psi ^ {\prime} = [ L \sin \sigma / m \cos \gamma + \upsilon ^ {2} \cos \gamma \sin \psi / \tan \phi / r} \\ {\quad \quad - 2 \omega \upsilon ( \tan \gamma \cos \psi \cos \phi - \sin \phi ) + r \omega ^ {2} \sin \psi \sin \phi \cos \phi / \cos \gamma ] / \upsilon ^ {2} D} \end{array} \right.\tag{1}$$

where the r is the radial distance from the center of the Earth to the mass center of the vehicle, θ is the longitude, φ is the latitude, υ is the relative velocity, γ is the flight-path angle, ψ is the heading angle, and σ is the bank angle. ω, $\mu ,$ and m are constants, representing the Earth self-rotation rate, the geocentric gravitational constant, and the mass of the vehicle, respectively.

To make the system dimensionless, the radius of the Earth $R _ {e} ,$ the geocentric gravitational constant $\mu ,$ and the mass of the vehicle m are chosen as the three fundamental quantities to scale all the physical quantities in Eq. (1). For example, υ is scaled by $\sqrt {\mu / R _ {e}}$ . The aerodynamic lift and drag, L and D are expressed as

$$\left\{\begin{array} {l l} {L = \rho \upsilon ^ {2} C _ {L} S _ {r e f} / 2} \\ {D = \rho \upsilon ^ {2} C _ {D} S _ {r e f} / 2} \end{array} \right.\tag{2}$$

where $\rho$ the atmospheric density, $S _ {r e f}$ is the reference area, $C _ {L}$ and $C _ {D}$ are the drag coefficient and the lift coefficient, respectively. The atmospheric and aerodynamic coefficient models adopted in this paper are

$$\begin{array} {l} {\rho = \rho _ {0} e ^ {( r - R _ {e} ) / \beta}} \\ {\left\{\begin{array} {l l} {C _ {L} = C _ {L 0} + C _ {L 1} \alpha + C _ {L 2} e ^ {C _ {L 3} \upsilon}} \\ {C _ {D} = C _ {D 0} + C _ {D 1} \alpha ^ {2} + C _ {D 2} e ^ {C _ {D 3} \upsilon}} \end{array} \right.} \end{array}\tag{3}$$

(4)

where $\rho _ {0} = 1.2258$ kg/m3, $\beta = - 1.3785 \times 10 ^ {- 4}$ , C Li , and $C _ {D i} \ ( i = 0 , 1 , 2 , 3 )$ are all constants, α is the angle of attack. The energy E is defined as:

$$E = m ( \mu / r - \upsilon ^ {2} / 2 )\tag{5}$$

So, the relative velocity υ can be computed at a given E and r as follows:

$$\upsilon = \sqrt {2 ( \mu / r - E / m )}\tag{6}$$

Like most related studies [22], the α profile is assumed to be specified and the main control variable is σ . During most of the reentry flight, the optimum lift-to-drag ratio α is chosen, whereas in the initial stage of reentry, a high angle of attack must be adopted in order to reduce the heating rate. In this paper, the α profile is defined by

$$\alpha ( E ) = \alpha _ {n} ( E ) + k _ {1} e ^ {k _ {2} ( E _ {0} - E )}\tag{7}$$

where $E _ {0}$ is the initial energy, k1 and $k _ {2}$ are the two designed coefficients.

## 2.2. Choice of control variable

Although the α profile is specified, the Eq. (1) is still very nonlinear with respect to the control variable σ . If we choose

$$u _ {1} = \cos \sigma , \quad u _ {2} = \sin \sigma\tag{8}$$

as the new control variables, the Eq. (1) can be rewritten in the dimensionless form as follows:

$$\left\{\begin{array} {l l} {\tilde {r} ^ {\prime} = \sin \gamma / \tilde {D}} \\ {\theta ^ {\prime} = \cos \gamma \sin \psi / \tilde {r} \tilde {D} \cos \phi} \\ {\phi ^ {\prime} = \cos \gamma \cos \psi / \tilde {r} \tilde {D}} \\ {\gamma ^ {\prime} = ( 1-1 / \tilde {r} \tilde {\upsilon} ^ {2} ) \cos \gamma / \tilde {r} \tilde {D} + \lambda u _ {1} / \tilde {\upsilon} ^ {2} + \varOmega _ {1}} \\ {\psi ^ {\prime} = \cos \gamma \sin \psi \tan \phi / \tilde {r} \tilde {D} + \lambda u _ {2} / \tilde {\upsilon} ^ {2} \cos \gamma + \varOmega _ {2}} \end{array} \right.\tag{9}$$

where the superscript ∼ means dimensionless, $\lambda = L / D$ is the lift-to-drag ratio, and $\varOmega _ {1} , \varOmega _ {2}$ are the terms associated with ω in Eq. (1). Then, Eq. (9) can be further expressed in a vector form as follows:

$${\pmb x} ^ {\prime} = {\pmb f} ( {\pmb x} , e ) + B ( {\pmb x} , e ) {\pmb u} + {\pmb g} ( {\pmb x} , e )\tag{10}$$

where $\pmb {x} = [ \widetilde {r} , \theta , \phi , \gamma , \psi ] , \pmb {u} = [ u _ {1} , u _ {2} ] ^ {T}$ , and e is the dimensionless form of E.

## 2.3. Optimal control problem

Considering the definitions of $u _ {1}$ and $u _ {2}$ the control vector u must meet the normalization constraint:

$$\| \pmb {u} \| _ {2} ^ {2} = 1\tag{11}$$

and the constraints, including $0 \leqslant u _ {1} \leqslant 1 , - 1 \leqslant u _ {2} \leqslant 1$ also need to be satisfied.

The typical path constraints, including dynamic pressure, heating rate, and overload, are expressed as

$$\begin{array} {r l r} & {{\tilde {q} = \frac {1} {2} \tilde {\rho} \tilde {\upsilon} ^ {2} \leqslant \tilde {q} _ {\mathrm{max}}}} \\ & {\tilde {Q} = k _ {Q} \tilde {\rho} ^ {0.5} \tilde {\upsilon} ^ {3.15} \leqslant \tilde {Q} _ {\mathrm{max}}} \\ & {\tilde {n} = \sqrt {\tilde {L} ^ {2} + \tilde {D} ^ {2}} \leqslant \tilde {n} _ {\mathrm{max}}} \end{array}\tag{12}$$

(13)

(14)

$k _ {Q}$ in Eq. (13) is a coefficient related to the shape of the vehicle. So, all the three constraints above can be expressed as inequalities of $r ,$ and unity the three constraints into the constraint

$$r \geqslant r _ {\operatorname* {m i n}} ( e ) = \operatorname* {m a x} ( r _ {\operatorname* {m i n}} ^ {q} , r _ {\operatorname* {m i n}} ^ {Q} , r _ {\operatorname* {m i n}} ^ {n} )\tag{15}$$

where $r _ {\operatorname* {m i n}} ^ {q} , r _ {\operatorname* {m i n}} ^ {Q}$ and $r _ {\mathrm{min}} ^ {n}$ are the lower bounds of $r ,$ respectively.

The values of x at the initial energy and the termination energy are wholly or partially given. These conditions can be expressed as

$${\pmb h} ( {\pmb x} ( e _ {0} ) , {\pmb x} ( e _ {f} ) ) = 0\tag{16}$$

Since the processing of complex optimization objectives is not the focus of this paper, please refer to reference [22] for more details about optimization objectives. In this paper, maximizing the terminal longitude is chosen as the optimization objective. So far, the original reentry trajectory optimization problem can be expressed as

$$\begin{array} {r l} {\mathcal {P} \mathrm{0:~}} & {\mathrm{minimize~} J = - \theta ( e _ {f} )} \\ & {\mathrm{subject~to~Eqs.~} ( 10 ) , ( 12 ) , ( 16 ) , ( 17 )} \end{array}\tag{17}$$

## 3. Convexification and discretization

In this section, we use the convexification method and the discretization method to transform the problem $\mathcal {P} _ {0}$ into a convex optimization subproblem.

## 3.1. Convexification

There are two non-convex constraints in the problem ${\mathcal {P}} _ {0}$ . One is the normalization constraint and the other is the motion equations. The motion equations are approximated by linearization at a reference obtained from the preceding solution, and the linearization error will decrease with the sequence optimization. The specific iteration process will be introduced later, but for now, suppose that the state reference and the control reference for the current iteration are ${\pmb x} _ {r e f}$ and ${\pmb u} _ {r e f}$ , respectively. According to the Taylor Formula, it is intuitive to approximate Eq. (10) as follows:

$$\begin{array} {l} {{\displaystyle {\pmb x} ^ {\prime} = {\pmb f} ( {\pmb x} , e ) + B ( {\pmb x} , e ) {\pmb u} + {\pmb g} ( {\pmb x} , e )}} \\ {\displaystyle \approx {\pmb f} ( {\pmb x} _ {r e f} , e ) + B ( {\pmb x} _ {r e f} , e ) {\pmb u} _ {r e f} + {\pmb g} ( {\pmb x} _ {r e f} , e ) + \frac {\partial {\pmb f}} {\partial {\pmb x}} | _ {{\pmb x} _ {r e f}} ( {\pmb x} - {\pmb x} _ {r e f} )} \\ {+ \frac {\partial B {\pmb u}} {\partial {\pmb x}} | _ {{\pmb x} _ {r e f}} ( {\pmb x} - {\pmb x} _ {r e f} ) + \frac {\partial {\pmb g}} {\partial {\pmb x}} | _ {{\pmb x} _ {r e f}} ( {\pmb x} - {\pmb x} _ {r e f} ) + \frac {\partial B {\pmb u}} {\partial {\pmb u}} \bigg | _ {{\pmb x} _ {r e f}} ( {\pmb u} - {\pmb u} _ {r e f} )} \end{array}\tag{18}$$

Ignoring the small quantity in Eq. (18), we have:

$$\pmb {x} ^ {\prime} \approx A \pmb {x} + B \pmb {u} + c\tag{19}$$

which is a standard linear time-varying system, and where A and c are

$$A = \frac {\partial {\mathbf {f}}} {\partial \mathbf {x}} \bigg \vert _ {x _ {r e f}} , ~ c = f ( {\pmb x} _ {r e f} , e ) - \frac {\partial {\mathbf {f}}} {\partial \mathbf {x}} \bigg \vert _ {{\pmb x} _ {r e f}} {\pmb x} _ {r e f} + {\pmb g} ( {\pmb x} _ {r e f} , e )\tag{20}$$

For the normalization constraint, according to the optimality condition, it can be relaxed directly as the inequality constraint

$$\| \mathbf {u} \| _ {2} ^ {2} \leqslant 1\tag{21}$$

which is a convex constraint. ${\mathsf{So}} ,$ the problem $\mathcal {P} _ {0}$ is transformed to

$$\begin{array} {r l} {\mathcal {P} _ {1} :} & {\mathrm{minimize} ~ J = - \theta ( e _ {f} )} \\ & {\mathrm{subject~to~Eqs.} ( 20 ) , ( 22 ) , ( 16 ) , ( 17 )} \end{array}\tag{22}$$

A brief proof of the lossless convexification of the normalization constraint is shown below. Please refer to references [25–27] for more detailed proof in other cases.

Proof. Proving the convexification is lossless is equivalent to proving the optimal solution of $\mathcal {P} _ {1}$ makes $\| \pmb {u} \| _ {2} ^ {2} = 1$ hold everywhere. The Hamiltonian for $\mathcal {P} _ {1}$ is as follows:

$$H ( \pmb {x} , \pmb {u} , \lambda , \mu , e ) = \pmb {\lambda} ^ {T} ( \pmb {A} \pmb {x} + \pmb {B} \pmb {u} + c ) + \pmb {\mu} ^ {T} \left[ \begin{array} {l} {\pmb {u} _ {1} ^ {2} + \pmb {u} _ {2} ^ {2} - 1} \\ {\pmb {r} _ {\operatorname* {m i n}} - \pmb {r}} \end{array} \right]\tag{23}$$

where $\lambda = [ \lambda _ {1} , \lambda _ {2} , \lambda _ {3} , \lambda _ {4} , \lambda _ {5} ] ^ {T}$ is costate vector, ${\pmb {\mu}} = [ \mu _ {1} , \mu _ {2} ] ^ {T}$ is Lagrange multipliers vector. According to the maximum principle, the optimal control variable $u _ {1} ^ {*}$ and $u _ {2} ^ {*}$ have to satisfy the following equation:

$$\left. {\frac {\partial H} {\partial \pmb {u}}} \right| _ {{\pmb {u}} = {\pmb {u}} ^ {*}} = \left[ b _ {41} \lambda _ {4} - 2 \mu _ {1} u _ {1} \right] = 0\tag{24}$$

where $b _ {i j}$ is the element in the ith row and the jth column of the matrix B. Assuming that $\| \pmb {u} \| _ {2} ^ {2} = 1$ doesn’t hold in an interval $[ e _ {1} , e _ {2} ] \subseteq [ e _ {0} , e _ {f} ]$ , according to the complementary slack conditions, we have $\mu _ {1} = 0 , \forall e \in [ e _ {1} , e _ {2} ]$ . Substituting this into Eq. (24), we get $\lambda _ {4} = \lambda _ {5} = 0 , \forall e \in [ e _ {1} , e _ {2} ]$

The costate equations can be expressed as:

$$\left\{\begin{array} {l l} {\lambda _ {1} ^ {\prime} = \frac {\partial H} {\partial r} = - a _ {11} \lambda _ {1} - a _ {21} \lambda _ {2} - a _ {31} \lambda _ {3} - a _ {41} \lambda _ {4} - a _ {51} \lambda _ {5} - \mu _ {2}} \\ {\lambda _ {2} ^ {\prime} = \frac {\partial H} {\partial \theta} = 0} \\ {\lambda _ {3} ^ {\prime} = \frac {\partial H} {\partial \phi} = - a _ {23} \lambda _ {2} - a _ {53} \lambda _ {5}} \\ {\lambda _ {4} ^ {\prime} = \frac {\partial H} {\partial \gamma} = - a _ {14} \lambda _ {1} - a _ {24} \lambda _ {2} - a _ {34} \lambda _ {3} - a _ {44} \lambda _ {4} - a _ {54} \lambda _ {5}} \\ {\lambda _ {5} ^ {\prime} = \frac {\partial H} {\partial \psi} = - a _ {25} \lambda _ {2} - a _ {35} \lambda _ {3} - a _ {55} \lambda _ {5}} \end{array} \right.\tag{25}$$

where $a _ {i j}$ is the element in the ith row and the jth column of the matrix A. Since $\lambda _ {4} = \lambda _ {5} = 0 ,$ , we have $\lambda _ {2} ( a _ {23} - ( a _ {25} / a _ {35} ) ^ {\prime} ) = 0 ,$ $\forall e \in [ e _ {1} , \overline {{e _ {2}}} ]$ from Eq. (25).

According to the transversality condition

$$\lambda _ {2} ( e _ {f} ) = \frac {\partial ( - \theta ( e _ {f} ) )} {\partial \theta} \Bigg | _ {e _ {f}} = - 1\tag{26}$$

and ${\partial \lambda _ {2}} / {\partial e} = 0$ , we have $\lambda _ {2} = - 1 , \forall e \in [ e _ {1} , e _ {2} ]$ . So, $a _ {23} - ( a _ {25} / a _ {35} ) ^ {\prime} = 0$ , e $\in [ e _ {1} , e _ {2} ]$ which is impossible. Therefore, there exists no interval $[ e _ {1} , e _ {2} ] \subseteq [ e _ {0} , e _ {f} ]$ in which $\| \mathbf {u} \| _ {2} ^ {2} \leqslant 1$ .

## 3.2. Discretization and approximation

Now, we discretize the state and control variables in the problem $\mathcal {P} _ {1}$ , so as to transform the continuous optimal control problem into a mathematical programming problem.

In this paper, the hp-adaptive Radau pseudospectral discretization is adopted. The terminology $" h p "$ is used because the segment widths (denoted h) and the polynomial degree (denoted $p )$ in each segment are determined simultaneously [32]. The update method of the discretization is covered in the next section, and we just focus on one iteration here.

Assuming that in the current iteration, the energy interval is divided into N segments (denoted by $\mathcal {H} _ {i} , i = 1 , \ldots , N$ , respectively), and the number of discretized points in segment $\mathcal {H} _ {i}$ is $p ^ {( i )} + 1$ . The division of segments and the distribution of discretized points are shown in Fig. 2.

The initial energy and the termination energy of $\mathcal {H} _ {i}$ are $e _ {0} ^ {( i )}$ and $e _ {f} ^ {( i )}$ separately, and there are $N - 1$ common endpoints. For $\mathcal {H} _ {i}$ , we get the $\boldsymbol {p} ^ {( i )}$ LGR points by solving the following equation

$$P _ {p ^ {( i )} - 1} ( \tau ) + P _ {p ^ {( i )}} ( \tau ) = 0\tag{27}$$

where $P _ {k}$ is the kth degree Legendre polynomial defined on $[ - 1 , 1 ]$ , and $\tau _ {1} ^ {( i )} = - 1$ . Combining the $\boldsymbol {p} ^ {( i )}$ LGR points and the non-collocated point ‘1’, we can obtain $p ^ {( i )} + 1$ discretized points on $\mathcal {H} _ {i}$ according to

$$e _ {k} ^ {( i )} = \frac {e _ {f} ^ {( i )} - e _ {0} ^ {( i )}} {2} \tau _ {k} ^ {( i )} + \frac {e _ {f} ^ {( i )} - e _ {0} ^ {( i )}} {2} , ~ k = 1 , \dots , p ^ {( i )} + 1\tag{28}$$

Then, the state variables on segment $\mathcal {H} _ {i}$ can be approximated by a Lagrange interpolation polynomial of degree at most $p ^ {( i )} + 1$ as

$$\pmb {x} ^ {( i )} ( \tau ) \approx X ^ {( i )} ( \tau ) = \sum _ {k = 1} ^ {p ^ {( i )} + 1} X _ {k} ^ {( i )} l _ {k} ( \tau )\tag{29}$$

where $l _ {k} ( \tau )$ is a basis of Lagrange interpolation polynomial, $X _ {k} ^ {( i )}$ is the state variables at $e _ {k} ^ {( i )}$ . On the basis of Eq. (29), the state derivative at each coordination point can be expressed as:

$$\left( \pmb {x} _ {j} ^ {( i )} \right) ^ {\prime} \approx \left( \boldsymbol {X} _ {j} ^ {( i )} \right) ^ {\prime} = \sum _ {k = 1} ^ {p ^ {( i )} + 1} \boldsymbol {X} _ {k} ^ {( i )} \big [ \boldsymbol {l} _ {k} ( \tau _ {j} ) \big ] ^ {\prime} , \quad j = 1 , \dots , p ^ {( i )}\tag{30}$$

which shows that $( X _ {j} ^ {( i )} ) ^ {\prime}$ is a linear combination of $X _ {k} ^ {( i )}$

## 3.3. Convex optimization subproblem

The discrete form of the state constraint Eq. (19) in ith segment can be expressed as (note that the state derivative constraints on terminal are not considered):

$$\frac {2} {e _ {j} ^ {( i )} - e _ {0} ^ {( i )}} \big ( {\pmb x} _ {j} ^ {( i )} \big ) ^ {\prime} = A ( e _ {j} ) {\pmb x} _ {j} ^ {( i )} + B ( e _ {j} ) {\pmb u} _ {j} ^ {( i )} + c ( e _ {j} ) , \quad j = 1 , \dots , p ^ {( i )}\tag{31}$$

Put the 5 states and 2 control variables at all discretized points into two columns and denote them by X and U , respectively. The composition of X and U are

$$\begin{array} {r l} & {X = [ \widetilde {r} _ {1} , \theta _ {1} , \phi _ {1} , \gamma _ {1} , \psi _ {1} , \hdots , \widetilde {r} _ {\overline {{N}}} , \theta _ {\overline {{N}}} , \phi _ {\overline {{N}}} , \gamma _ {\overline {{N}}} , \psi _ {\overline {{N}}} ] ^ {T}} \\ & {U = [ u _ {1 , 1} , u _ {2 , 1} , \hdots , u _ {1 , \overline {{N}}} , u _ {2 , \overline {{N}}} ] ^ {T}} \\ & {\overline {{N}} = \sum _ {k = 1} ^ {N} p ^ {( k )} + 1} \end{array}\tag{32}$$

where $\overline {{N}}$ is the total number of discretized points, $\boldsymbol {X} \in \mathbb {R} ^ {5 \overline {{{N}}}}$ , and $U \in \mathbb {R} ^ {2 \overline {{N}}}$ . Then, the state constraint at all discretized points is given by

$$\boldsymbol {F} \boldsymbol {X} = \boldsymbol {M} [ \boldsymbol {X} ^ {T} , \boldsymbol {U} ^ {T} ] ^ {T} + \boldsymbol {O}\tag{33}$$

where, F is the $5 \overline {{N}} \times ( 5 \overline {{N}} + 5 )$ differentiation matrix constituted by all $[ l _ {k} ( \tau ) ] ^ {\prime}$ , M is the $5 \overline {{N}} \times ( 7 \overline {{N}} + 7 )$ system matrix, and O is the $\overline {{N}} \times 1$ additional vector.

M and O are obtained as:

$$M = \left[ \begin{array} {c c c c c c c c} {A ( e _ {1} )} & {\mathbf {0}} & {\cdots} & {\mathbf {0}} & {B ( e _ {1} )} & {\mathbf {0}} & {\cdots} & {\mathbf {0}} \\ {\mathbf {0}} & {A ( e _ {2} )} & & {\vdots} & {\mathbf {0}} & {B ( e _ {2} )} & & {\vdots} \\ {\vdots} & & & {\ddots} & {\mathbf {0}} & {\vdots} & & {\ddots} & {\mathbf {0}} \\ {\mathbf {0}} & {\cdots} & {\mathbf {0}} & {A ( e _ {N} )} & {\mathbf {0}} & {\cdots} & {\mathbf {0}} & {B ( e _ {N} )} \end{array} \right] , \quad O = \left[ \begin{array} {c} {c ( e _ {1} )} \\ {c ( e _ {2} )} \\ {\vdots} \\ {c ( e _ {N} )} \end{array} \right]\tag{34}$$

The sparsity pattern of F has the form shown in Fig. 3. It can be seen that F is a partitioned matrix with N submatrices, each of which contains the differentiation coefficients of the corresponding segment. Therefore, the fewer discretized points in each segment, the lower the order of the submatrix, and the sparser the differentiation matrix. The overlapping columns of two adjacent submatrices (as shown in the dashed box in Fig. 3) indicate that the values at the junction are used for state fitting in both the two segments. Since both F and M are sparse matrices, the linear equality constraint represented by Eq. (33) is tractable for the optimization algorithm.

To avoid iteration divergence, it is necessary to consider the following trust region constraints:

$$| X - X _ {r e f} | \leqslant \underbrace {[ \varDelta ^ {T} \cdot \cdot \cdot \varDelta ^ {T} ]} _ {\mathrm{Repeated} \overline {{N}} \mathrm{times}} ^ {T}\tag{35}$$

where Δ is the trust region radius. Considering that the discrete forms of Eq. (15), Eq. (16), and Eq. (35) are all direct restrictions on X , they may all be represented as

$$\underline {{{X}}} \leqslant X \leqslant \overline {{{X}}}\tag{36}$$

where $\underline {{\boldsymbol {X}}} , ~ \overline {{\boldsymbol {X}}}$ are the lower and upper bounds of X. In the reentry trajectory optimization problem, all terminal state variables except longitude are supplied.

In general, at the beginning of the iteration, a relaxation variable $\xi \geqslant 0$ is introduced to prevent the optimization problem from becoming infeasible, and then the associated upper and lower bounds change to

$$\begin{array} {r} {\underline {{X}} _ {f} = [ \tilde {r} _ {f} - \xi , \phi _ {f} - \xi , \gamma _ {f} - \xi , \psi _ {f} - \xi ] ^ {T}} \\ {\overline {{X}} _ {f} = [ \tilde {r} _ {f} + \xi , \phi _ {f} + \xi , \gamma _ {f} + \xi , \psi _ {f} + \xi ] ^ {T}} \end{array}\tag{37}$$

where the subscript f represents the index of the terminal state variables except longitude.

So far, we can approximate $\mathcal {P} _ {1}$ as the following convex optimization subproblem:

$$\begin{array} {r l} {\mathcal {P} _ {2} ^ {( k )} :} & {\mathrm{minimize~} J = P _ {\theta} \theta _ {f} + P _ {\xi} \xi} \\ & {\mathrm{subject~to~} F X = M ( [ X ^ {T} , U ^ {T} ] ^ {T} ) + O} \\ & {\qquad \quad \underline {{X}} \leqslant X \leqslant \overline {{X}}} \\ & {\quad \quad \quad U _ {i} ^ {2} + U _ {i + 1} ^ {2} \leqslant 1 , \quad i = 1 , 3 , \cdots , 2 \overline {{N}} - 1} \\ & {\quad \quad \quad \quad Z = [ X ^ {T} , U ^ {T} , \xi ] ^ {T}} \end{array}\tag{38}$$

where the superscript (k) represents this subproblem is formed during the kth iteration, $P _ {\theta} < 0 , P _ {\xi} \gg 0$ are the weight coefficients of the terminal longitude and the relaxation variable respectively, and $Z \in \mathbb {R} ^ {7 \times \overline {{N}} + 1}$ is the optimization variable of this subproblem.

## 4. Iterative algorithm

## 4.1. Differential error and state curvature

There are two features used to judge the solution of problem $\mathcal {P} _ {2} ^ {( k )}$ and serve as a basis for the hp-adaptive RPD update process. One is the differential error, and the other is the curvature of the worst state variable.

We assume that the optimal state and control of ith segment obtained in the current iteration are $X ^ {( i )}$ and $U ^ {( i )}$ , corresponding to $\boldsymbol {p} ^ {( i )}$ discretized $\hat {e} ^ {( i )}$ , and the midpoints are defined as:

$$\hat {e} _ {j} ^ {( i )} = \frac {e _ {j} ^ {( i )} + e _ {j + 1} ^ {( i )}} {2} , \quad j = 1 , \ldots , p ^ {( i )}$$

The differential error matrix is defined as:

(39)

$$\begin{array} {r l} & {R ^ {( i )} = \left[ R _ {1} ^ {( i )} \cdots R _ {p ^ {( i )}} ^ {( i )} \right] ^ {T}} \\ & {R _ {j} ^ {( i )} = \left| \left( X ^ {( i ) \prime} - \pmb {x} ^ {( i ) \prime} \right) \oslash \pmb {x} ^ {( i ) \prime} \right| _ {e = \hat {e} _ {j} ^ {( i )}}} \end{array}\tag{40}$$

where $X ^ {( i ) \prime}$ and $\pmb {x} ^ {( i ) \prime}$ are state differential calculated by Eq. (30) and Eq. (31), 
 represents the division of the corresponding elements. Then, the differential error is calculated as:

$$\mathcal {R} ^ {( i )} = \operatorname* {m a x} R ^ {( i )}\tag{41}$$

The state variable with the largest differential error is chosen as the worst one. The curvature of this state is calculated as (take the flight-path angle as an example)

$$\mathcal {K} _ {j} ^ {( i )} = \left. \frac {\gamma ^ {( i )} \prime \prime} {[ 1 + ( \gamma ^ {( i )} \prime ) ^ {2} ] ^ {3 / 2}} \right. _ {e = \hat {e} _ {j} ^ {( i )}} , \quad j = 1 , \hdots , p ^ {( i )}\tag{42}$$

It should be noted that the derivative (both first order and second order) of states at the midpoints can be expediently calculated using the Lagrange interpolation polynomial.

## 4.2. hp-Adaptive RPD

In hp-adaptive RPD update process, determining locations of new segments or increasing the number of collocation points of segment $\mathcal {H} _ {i}$ is determined by the two features: $\mathcal {R} ^ {( i )}$ and $\mathcal {K} _ {j} ^ {( i )}$ . We evaluate the uniformity of the curvature ${\kappa} _ {j} ^ {( i )}$ distribution in this segment by:

$$\mathcal {V} ^ {( i )} = \frac {\operatorname* {m a x} \mathcal {K} ^ {( i )}} {\overline {{\mathcal {K}}} ^ {( i )}}\tag{43}$$

where $\overline {{\mathcal {K}}} ^ {( i )}$ is the mean of the vector $\mathcal {K} ^ {( i )}$ . If $\mathcal {V} ^ {( i )}$ is less than a given parameter ζ , the only operation is to increase the number of matching points in the segment to the following value

$$p _ {\mathrm{new}} ^ {( i )} = p ^ {( i )} + \operatorname* {m a x} \biggl ( \biggl | \log _ {10} \biggl ( \frac {\mathcal {R} ^ {( i )}} {\varepsilon} \biggr ) \biggr rceil , 0 \biggr )\tag{44}$$

where ε is the reference error. Otherwise, we divide the current segment into $n _ {\mathrm{new}} ^ {( i )}$ (calculated as Eq. (45)) subsegments. The endpoints of each subsegment $\tilde {e} _ {i} ^ {( i )}$ satisfy Eq. (46), where the integrand reflects the probability of the error distribution [35]. Then, $p _ {\mathrm{min}}$ points are arranged on each subsegment, where pmin is a given parameter.

$$n _ {\mathrm{new}} ^ {( i )} = \operatorname* {m a x} \biggl ( \biggl | \log _ {10} \biggl ( \frac {\mathcal {R} ^ {( i )}} {\varepsilon} \biggr ) \biggr | , 2 \biggr )\tag{45}$$

$$\begin{array} {l} {{\displaystyle {\widetilde {e} _ {j} ^ {( i )}}} ( \mathcal {K} ^ {( i )} ( e ) ) ^ {1 / 3} \mathrm{d} e = \frac {j} {n _ {\mathrm{new}} ^ {( i )}} , \quad j = 1 , \dots , n _ {\mathrm{new}} ^ {( i )} - 1} \\ {{\displaystyle e _ {0} ^ {( i )}}} \end{array}\tag{46}$$

$$\widehat {\mathcal {K}} ^ {( i )} : = \int _ {e _ {0} ^ {( i )}} ^ {e _ {j} ^ {( i )}} \bigl ( \mathcal {K} ^ {( i )} ( e ) \bigr ) ^ {1 / 3} \mathrm{d} e$$

## 4.3. Iteration process

The iteration process starting from a rough discretization and a simple initial value. For example, the energy interval $[ e _ {0} , e _ {f} ]$ is divided into 10 segments, and 4 LGR points are arranged on each segment. The initial and terminal states and controls are given directly or are easy to guess at a reasonable value, and the states and controls at other points are linearly interpolated based on the corresponding initial and terminal values.

The state and control reference required for the $k + 1$ iteration is calculated based on the reference value of the current iteration and the optimal value obtained by solving $\mathcal {\bar {P}} _ {2} ^ {( k )}$ , i.e.

$$\begin{array} {r l} & {X _ {r e f} ^ {k + 1} = X _ {r e f} ^ {k} + \kappa ( X _ {o p t} ^ {k} - X _ {r e f} ^ {k} )} \\ & {U _ {r e f} ^ {k + 1} = U _ {r e f} ^ {k} + \kappa ( U _ {o p t} ^ {k} - U _ {r e f} ^ {k} )} \end{array}\tag{47}$$

where $X _ {o p t} ^ {k}$ is the solution of ${\mathcal {P}} _ {2} ^ {( k )}$ , and $\kappa \in ( 0 , 1 ]$ called search efficiency determining the line search step.

Algorithm 1 hp-adaptive RPD update process. 
Input: eˆ(:) , R(:) , K(:) , and $\mathcal {V} ^ {( : )}$ 
Output: New discretized points $e _ {\mathrm{new}} ^ {( : )}$ 
1: initialize $e _ {\mathrm{new}} ^ {( \cdot )} = \mathrm{NULL} , ~ N _ {\mathrm{new}} = 0 ;$ 
2: for i = 1 to N do 
3: if V (i) - ζ then 
4: $e _ {\mathrm{new}} ^ {( i + N _ {\mathrm{new}} )} : = p _ {\mathrm{new}} ^ {( i )}$ LGR points in $[ e _ {0} ^ {( i )} , e _ {f} ^ {( i )} ] ;$ 
5: $N _ {\mathrm{new}} = N _ {\mathrm{new}} + 1 ;$ 
6: else 
7: Calculate $n _ {\mathrm{new}} ^ {( i )} - 1$ breakpoints $e _ {j} ^ {( i )}$ 
8: for $j = 1$ to $n _ {\mathrm{new}} ^ {( i )}$ do 
9: $e _ {\mathrm{new}} ^ {( i + N _ {\mathrm{new}} )} : = p _ {\mathrm{min}}$ LGR points in $[ e _ {j - 1} ^ {( i )} , e _ {j} ^ {( i )}$ ]; 
10: $N _ {\mathrm{new}} = N _ {\mathrm{new}} + 1 ;$ 
11: end for 
12: end if 
13: end for

In this paper, the iteration process is divided into three stages, called “approach stage”, “hp update stage” and “convergence stage”, respectively. In the approach stage, the problem $\mathcal {P} _ {2} ^ {( k )}$ has a small scale and is solved quickly. However, because the initial value of the iteration is far from the real trajectory, the state constraint equation will be very difficult to satisfy. In a sense, the state differentiation constraint at the beginning of the iteration is very rough and it is not necessary to meet it strictly. The goal of the approach stage is achieved as long as the results of subproblems approximate the real trajectory. So, we relax Eq. (33) by parameter $\delta _ {r}$ as follows:

$$\vert F X - M ( [ X ^ {T} , U ^ {T} ] ^ {T} ) \vert \leqslant {\cal {O}} ( 1 + \delta _ {r} )\tag{48}$$

As the iteration goes on, the unrelaxed constraints can be satisfied, and then the iteration enters the hp update stage. In this stage, the scale of the problem $\mathcal {P} _ {2} ^ {( k )}$ gradually increases, but the differential error gradually decreases.

When the differential error of all segments is less than the threshold value, the iteration enters the convergence stage. Due to the small difference between the two adjacent optimal solutions, the difference between two adjacent suboptimization problems will be very minute. It is easy to cause solutions of subproblems to fluctuate in a certain range, and the convergence is slow. To overcome this shortcoming, a regularization term is added to the optimization objective J as follows (note that the relaxation of terminal constraints can be removed in this stage):

$$J = P _ {\theta} \theta _ {f} + P _ {e} \| X - X _ {r e f} \| _ {2}\tag{49}$$

where $P _ {e}$ is the coefficient of the regularization term. It can be considered that this regularization term plays a role in damping the convergence process, thus preventing excessive fluctuations in some states.

```latex
Algorithm 2 SCP iteration process.
Input: e, Xguess , U guess , Δ, q˜max, Q˜ max, nmax, P θ , P ξ , P e
Output: eresult , Xresult , U result
1: initialize $X _ {r e f} ^ {( : )} , U _ {r e f} ^ {( : )} , T _ {s t a g e} = 1 ^ {s t} ;$
2: for k 1 to $N _ {\mathrm{max}}$ do
3: Calculate X, X, F , M, O and form the optimization subproblem ${\mathcal {P}} _ {2} ^ {( k )} ;$
4: Solve $\mathcal {P} _ {2} ^ {( k )}$ to obtain $X _ {o p t} ^ {k}$ and $U _ {o p t} ^ {k}$ (nrel times relaxation is carried out until solved);
5: Calculate $\epsilon _ {\mathrm {{i t e r}}} ;$
6: if -iter - - then
7: $X _ {r e s u l t} = X _ {o p t} ^ {k} , U _ {r e s u l t} = U _ {o p t} ^ {k}$ and eresult = enew ;
8: break;
9: else
10: Select parameter κ based on $T _ {\mathrm{stage}} ,$ and calculate the new reference $X _ {r e f} ^ {k + 1} , \ : U _ {r e f} ^ {k + 1}$
11: Calculate eˆ(:) , R(:) , K(:) and $\mathcal {V} ^ {( : )} ;$
12: if $\mathcal {R} ^ {( : )} > \varepsilon \& n _ {r e l} = 1$ then
13: Obtain $e _ {\mathrm{new}} ^ {( : )}$ by hp-adaptive RPD, $X _ {r e f} ^ {k + 1} , U _ {r e f} ^ {k + 1}$ by interpolate;
14: $T _ {\mathrm{stage}} = 2 ^ {\mathrm{nd.}}$
15: else if $\mathrm {{\Delta} n} _ {r e l} > 1 \mathrm {{\Delta}}$
16: $T _ {\mathrm{stage}} = 1 ^ {\mathrm{nd.}}$
17: else
18: $T _ {\mathrm{stage}} = 3 ^ {\mathrm{nd.}} ;$
19: end if
20: end if
21: end for
```

When the following conditions are met, the iteration ends.

$$\epsilon _ {\mathrm{iter}} = \operatorname* {m a x} ( | X _ {o p t} - X _ {r e f} | ) \leq \epsilon\tag{50}$$

where max refers to the maximum residual of each state, and - is the given allowable error vector corresponding to each state. The appropriate parameter κ should be selected according to the stage type.

## 5. Numerical simulations and discussion

In this section, a typical reentry trajectory optimization problem for hypersonic vehicle dubbed CAV-H [36] will be used to demonstrate the proposed algorithm. For CAV-H, the coefficients in Eq. (4) are $C _ {L 0} = - 0.236 , C _ {L 1} = 2.945 , C _ {L 2} = 0.295 , C _ {L 3} = - 3.394 \times 10 ^ {- 4} , C _ {D 0} =$ 0.023, $C _ {D 1} = 2.379 , C _ {D 2} = 0.398 , C _ {D 3} = - 1.079 \times 10 ^ {- 3}$ . The trust region radius and the allowable iteration error vector are chosen as follows.

$$\begin{array} {l} {\displaystyle \varDelta = \left[ \frac {20 \mathrm{km}} {R _ {e}} , \frac {20 \pi} {180} , \frac {20 \pi} {180} , \frac {20 \pi} {180} , \frac {20 \pi} {180} \right] ^ {T}} \\ {\displaystyle \epsilon = \left[ \frac {1 \mathrm{m}} {R _ {e}} , \frac {d _ {\varepsilon} \pi} {180} , \frac {d _ {\varepsilon} \pi} {180} , \frac {d _ {\varepsilon} \pi} {180} , \frac {d _ {\varepsilon} \pi} {180} \right] ^ {T} , \quad {d _ {\varepsilon} = 10} ^ {- 4}} \end{array}\tag{51}$$

(52)

The initial and terminal conditions, the upper bounds of path constraints, and the model parameters are listed in Table 1. All of the following numerical simulations were implemented in a MATLAB environment on a personal desktop with an Intel Core i5 3.0GHz processor, and the convex optimization subproblems were solved by MOSEK [37] in version 9.3.6.

## 5.1. Solve by the proposed algorithm

In this instance, other parameters of the proposed algorithm are set as follows: $P _ {\theta} = 1 , \ P _ {\xi} = 10 ^ {4} , \ P _ {e} = 10 ^ {- 2} , \ \varepsilon = 10 ^ {- 2} , \ \delta _ {r} = 10 ^ {- 3}$ $N _ {\mathrm{max}} = 50 , p _ {\mathrm{min}} = 4$ , and in each of the three stages, κ is set to 0.35, 0.75, and 0.9, respectively. The initialization with rough discretization and simple initial values is described in Sec. 4.3.

Since the trajectory accuracy is not directly calculated in the iteration process, it is necessary to evaluate the accuracy of the optimization results by the integral results $X _ {i n t}$ . The explicit Runge-Kutta (4,5) formula is used to obtain the integral results in this paper, and the definitions of the maximum error $\mathcal {E} _ {\mathrm{max}}$ , the average error $\mathcal {E} _ {\mathrm{mean}}$ and the terminal error $\mathcal {E} _ {\mathrm{end}}$ of the ith state $X ^ {i}$ are shown in Eq. (53).

$$\begin{array} {r l} & {\mathcal {E} _ {\operatorname* {m a x}} = \underset {e \in [ e _ {0} , e _ {f} ]} {\operatorname* {m a x}} \mathcal {E} ( e ) , \quad \mathcal {E} _ {\operatorname* {m e a n}} = \frac {\int _ {e _ {0}} ^ {e _ {f}} \mathcal {E} ( e ) \mathrm{d} e} {e _ {f} - e _ {0}} , \quad \mathcal {E} _ {\mathrm{end}} = \mathcal {E} ( e _ {f} )} \\ & {\mathcal {E} ( e ) = | X _ {r e s u l t} ^ {i} ( e ) - X _ {i n t} ^ {i} ( e ) |} \end{array}\tag{53}$$

The relative values of these errors will also be given later, which is calculated by referring to the range of the corresponding state along the trajectory.

The comparison between the optimal trajectory in altitude-velocity space obtained by the proposed algorithm and the integral one is shown in Fig. 4. As can be observed from the figure, the two curves overlap almost perfectly, which shows that the proposed algorithm is feasible.

The errors of each state are shown in Table 2. The maximum error of altitude does not exceed 24 m, and the maximum errors of longitude and latitude do not exceed $0.02 ^{\circ}$ and 0.002◦, respectively. From the perspective of relative value, these errors are not more than one thousandth except the flight-path angle. However, due to the small range of the flight-path angle, the maximum error of around $4 \text{‰}$ is also negligible. The altitude reaches the constraint boundary at some points or intervals, which can be seen from the two regional enlarged drawings in Fig. 4. Specifically, within the speed range [5800 m/s, 6700 m/s], the altitude decreases gradually with fluctuation and reaches the lower boundary at the four troughs of the fluctuation. Within the speed range [2900 m/s, 3400 m/s], the altitude is very close to the lower boundary and descends along the boundary for some time.

As shown in Fig. 5, the ground tracks of two results are also highly consistent. It can be seen from both Fig. 4 and Fig. 5 that the density of the distribution of discretized points changes along the trajectory, which is caused by adaptive mesh updating. On the whole, the distribution of discretized point is denser in the region where the trajectory changes sharply, and the distribution of discretized points is sparser in the part where the trajectory changes gently.

The history of bank angle with time and the corresponding error of control defined by $1 - ( u _ {1} ^ {2} + u _ {2} ^ {2} )$ is shown in Fig. 6. It should be noted that, both σ and t can be obtained by simple operations on the basis of the obtained results. It can be seen that, in order to maximize the terminal longitude, the bank angle becomes large only at the start and end of the trajectory, and fluctuates around a small value the rest of the time. The error of control is less than $10 ^ {- 7}$ most of the time, which confirms the proof of lossless relaxation in Sec. 3.1.

## 5.2. Convergence analysis of the proposed algorithm

The solving process of the above problem has carried out 19 iterations in total, and the CPU time for the proposed algorithm is 2.377 s. The following content is about the convergence analysis of the iteration.

Fig. 7 shows how the longitude-altitude curve is updated with the iteration process. It can be seen that the initial guess is a very simple straight line. After 7 iterations in the stage 1 (approach stage), the curve gradually changes to the shape (the thick azure line) of the beginning of stage 2 (hp update stage), which looks more realistic. Due to the small number of discretized points, the curve at this stage is more like a broken line, and the linearization error is still very large. In the hp update stage, the number and position of discretized points are updated by the hp-adaptive RPD update method in each iteration, and the curve gradually becomes smooth. After 5 iterations, the differential error reaches the threshold value, and the longitude-altitude curve at this time (the thick pink line) is very close to the final optimization result (the thick carmine line). In the following stage 3 (convergence stage), during 7 iterations, the state residual decreases rapidly (which means the reduction of linearization error), and finally meets the convergence requirement. As shown in the regional enlarged drawing in Fig. 7, the difference in terminal longitude has been less than $0.01 ^{\circ}$ in the last 4 iterations.

It has been explained in Sec. 4.3 that differential constraint relaxation is required in the approach stage to make the convex optimization subproblem feasible. In this case, $n _ {r e l}$ in the approach stage is all 2, which means that only one differential constraint relaxation with parameter δr is required to make the subproblem feasible. When the 5 iterations of this stage are completed, this relaxation is no longer required. Fig. 8 shows the variation trend of the mean of the maximum state residual $\boldsymbol {\epsilon} _ {\mathrm{iter}}$ and the maximum differential error $\mathcal {R} ^ {( : )}$ with the number of iterations. The residuals of the approach stage, hp update stage, and convergence stage are shown in black, azure, and pink, respectively.

As can be seen from the graph, the maximum differential error does not decrease during the first stage. This is because there are few discretized points, and the differential error is evaluated at the central point. The change of trajectory shape has little effect on the maximum differential error. Generally speaking, the main purpose of the first stage is to approach the real trajectory from the initial guess gradually. In the second stage, the maximum differential error gradually decreases to below ε, which is due to the adaptive mesh updating. The main purpose of this stage is to increase the number of discretized points and adjust their distribution position reasonably. In the first two stages, the mean of the maximum state residual $\boldsymbol {\epsilon} _ {\mathrm{iter}}$ decreases very slowly. This is because both constraint relaxation and mesh update make the optimization results of two adjacent iterations differ greatly. In the final stage, the mesh is no longer updated, and the state residual decrease rapidly until the accuracy requirements are met. Similarly, since the number of discretized points does not increase, the differential error remains basically stable.

The number of discretized points and CPU time for each iteration versus cumulative number of iteration steps are shown in Fig. 9. It can be seen that the CPU time is positively correlated with the number of discretized points. Nevertheless, due to the uncertainty of the optimization algorithm, the CPU time fluctuates slightly. In the approach stage, the number of discretized points is 41 (containing 40 LGR points and the endpoint), and the corresponding CPU time is less than 50 milliseconds. During the hp update stage, the number of discretized points gradually increases to 403, and the calculation time increases to about 250 milliseconds. Interestingly, the CPU time does not increase significantly though the regularization term is added to the optimization objective in the convergence stage.

In order to verify the insensitivity to initial values of the proposed algorithm, the Monte Carlo simulations performed with different initial values have been carried out. The initial values used for simulation $( X _ {g u e s s} ^ {m} )$ are generated according to Eq. (54), where $X _ {g u e s s} ^ {l}$ is the linear initial guess based on the two endpoints, and $\varDelta _ {x}$ is the range of states. Given that the terminal longitude is not fixed, the $X _ {g u e s s} ^ {m}$ is determined by both $k _ {m}$ and $\theta _ {f , g u e s s}$

$$\begin{array} {c} {{X _ {g u e s s} ^ {m} = X _ {g u e s s} ^ {l} + k _ {m} \Delta _ {x} \sin \displaystyle \left( \pi \frac {e - e _ {0}} {e _ {f} - e _ {0}} \right)}} \\ {{k _ {m} \sim U ( 10 ^ {- 2} , 10 ^ {- 1} )}} \\ {{\theta _ {f , g u e s s} \sim U ( 80 ^{\circ} , 120 ^{\circ} )}} \end{array}\tag{54}$$

Both $k _ {m}$ and $\theta _ {f , g u e s s}$ follow uniform distribution, and the distribution parameters are shown in Eq. (54). 1000 samples are randomly selected for Monte Carlo simulations, and the statistical parameters are shown in Table 3. As can be seen from the table, the iteration is between 16 and 22, the number of discretized points is between 402 and 485, and the CPU time is between 1.68 s and 3.461 s. The optimization results are very close, and the parameters of the benchmark simulation above are close to the mean values in the table, which indicates that the benchmark one can represent the general performance of the algorithm. The standard deviation of each parameter is very small, which indicates that the proposed algorithm has strong insensitivity to initial values.

## 5.3. Comparison with other algorithms

In this subsection, SCP with uniform discretization (UD), SCP with hp Radau pseudospectral discretization (hp RPD), and GPOPS-II [32] are used to solve the same entry trajectory optimization problem. When SCP with UD is applied to solve the problem, the initial guess must be designed, especially for altitude, if there is no differential constraint relaxation. As for SCP with hp RPD, as the differential constraints are more complex and there are many discretized points at the beginning of the iteration, constraint relaxation needs to be considered in the first several iterations, just like the algorithm proposed. The search efficiency for SCP with UD and SCP with hp RPD is 0.75.

The discretization parameters and solution performance of different algorithms are given in Table 4. In SCP with hp-adaptive RPD (the proposed algorithm), the number of segments and number of discretized points are 81 and 403, both of which are lower than the value of GPOPS-II. For both SCP with UD and SCP with hp RPD, we chose two discretization schemes, one sparse and the other dense (abbreviated as UD (420), UD (800), RPD (105), and RPD (150), respectively). It should be noted that there is no concept of segment in uniform discretization, so we consider the number of stages equal to the number of discretized points minus 1. In SCP with hp RPD, the number of LGR points in all segments is set to 4.

Due to the small scale of subproblems, the CPU time for UD (420) and RPD (105) using a sparse discretization scheme is less than 4 seconds. The CPU time for RPD (105) is slightly longer because its differential constraint conditions are more complex and the subproblems are more difficult to solve. The average CPU time of each iteration of RPD (105) is 0.164 s, 19.7% longer than that of UD (420). However, from the perspective of the maximum error, the performance of the two sparse discretization schemes is poor. In particular, the maximum error of flight-path angle is more than 0.1◦ (and the relative error is more than 20 ), which is very unfavorable for accurately describing the trajectory.

A denser discretization scheme should be adopted in order to improve the accuracy of the results. In UD (800) and RPD (150), the maximum altitude error is reduced to about 20 m. The maximum latitude error is reduced by one order of magnitude, and other maximum errors are reduced by more than half. However, using more discretized points means longer CPU time. The CPU time for UD (800) is 8.071 s, and the CPU time for RPD (150) is 6.277 s. As can be seen from Table 4, the accuracy of the proposed method and GPOPS-II is similar to that of the two dense discretization schemes. The number of iterations of the proposed algorithm is 19, whereas that of UD is 28 and RPD is 24. As for GPOPS-II, 6 mesh updates are carried out in its solving process, and the number of iterations of nonlinear programming reached 76 in total. The CPU time for the proposed algorithm is 70.5% shorter than UD (800), and 62.1% shorter than RPD (150), and even only 1/20 of GPOPS-II. Even compared with UD (420) and RPD (105), both the total CPU time and the average CPU time for the proposed algorithm are still shorter thanks to the hp-adaptive RPD updating and regularization.

Compared with other methods, the maximum longitude obtained by the proposed algorithm has a certain loss, but the maximum difference is only 0.05%. Fig. 10 shows the optimal longitude-altitude curves obtained by different algorithms. It can be seen that the six curves are relatively close on the whole, but they show different fluctuation rules in the glide stage.

The maximum residual history in different algorithms is shown in Fig. 11. It is worth noting that the convergence curves of the same class of SCP methods are very similar. The convergence rate of SCP with UD remains unchanged basically, whereas the convergence rate of SCP with hp RPD (including the proposed algorithm) is slow at first and then fast. This is because the first several iterations belong to the process of slowly approaching, and constraint relaxation is needed to solve each convex optimization subproblem, and the inheritance relationship between the two adjacent optimization results is weak.

Due to the more accurate approximation of state derivative in SCP with hp RPD, the solution of the convex optimization subproblem can be closer to the real trajectory. It can be seen that in the following iterations, the convergence rate of RPD method is significantly faster than that of UD method. Considering that each iteration adopts a fixed search rate and does not carry out the optimal line search calculation, the solution of the suboptimization problem is easy to oscillate at the end of the iteration. The addition of the regularization term at the last stage of iteration suppresses the oscillations effectively. From the figure, it is obvious that the convergence rate of the proposed algorithm is faster than that of RPD method and UD method.

## 6. Conclusions

Trajectory optimization based on SCP is widely used in the aerospace community. The core of SCP is the convexification technology, especially the lossless convexification technology about non-convex control constraints. However, since SCP belongs to the direct method category, essentially, discretization is also a crucial factor affecting the accuracy of the solution and the efficiency. The main contribution of this paper is to improve the existing SCP method in terms of discretization and iteration, and the SCP with hp-adaptive RPD is proposed. The application of hp-adaptive RPD makes the scale of the subproblem in the iteration process gradually increase, thus improving the solving efficiency on the whole. More importantly, the optimal trajectory with as high precision as possible can be obtained with fewer discretized points through reasonable mesh updating. In addition, constraint relaxation and regularization techniques are used at the beginning and end of iteration, respectively, to make the proposed algorithm insensitive to initial values and achieve fast convergence at the end. Compared with other methods, the algorithm proposed in this paper has strong competitiveness.

Although the regularization term is added to the optimization objective in this paper to improve the convergence rate of the iteration process, its linear convergence property is not changed. In future work, we want to utilize the Hessian matrix of nonlinear functions as the weight of the regularization item, which may boost the algorithm’s performance even more.

## Omitted Tables

- [Table 1 omitted; saved to tables/table_001.md]
- [Table 2 omitted; saved to tables/table_002.md]
- [Table 3 omitted; saved to tables/table_003.md]
- [Table 4 omitted; saved to tables/table_004.md]
- [Table 5 omitted; saved to tables/table_005.md]
