## 1. Introduction

In the modern high-performance aircraft design process, due to the growing concern on fuel efficiency, composite materials are increasingly deployed in aerospace structures. This is due to their performance advantages: directional stiffness and superior strength/stiffness-to-weight ratios compared with traditional metallic structures. In particular, the concept of aeroelastic tailoring using the directional stiffness properties of composite materials offers great potential for designers to improve aeroelastic performance.

Aeroelastic tailoring (Shirk et al., 1986) is a technology which can be used to control both static and dynamic aeroelastic phenomena. Aeroelastic tailoring using the anisotropic mechanical characteristics and multiple design variables, such as stacking sequence and ply angle of composite materials, is a beneficial way to enhance the aerodynamic and structural performance of aircraft. Aeroelastic tailoring has been applied to improve aeroelastic characteristics in the aircraft structural design process over the past few decades. Sherrer et al. (Sherrer et al., 1981) demonstrated that aeroelastic tailoring can be used to increase the divergence speed of a composite forward swept wing through low-speed wind tunnel tests. Guo (Guo, 2007) demonstrated aeroelastic tailoring to significantly reduce the weight of aircraft structures and, at the same time, to increase up to 30% the flutter speed. Alyanak et al. (Alyanak and Pendleton, 2017) applied aeroelastic tailoring simultaneously with active aeroelastic control to a lambda wing to reduce the aircraft weight. Marques et al. (Marques et al., 2017) presented an investigation on the aeroelastic tailoring of stiffened laminate composite panels in supersonic flow to maximize the flutter non-dimensional dynamic pressure. Yu et al. (Yu et al., 2017) applied the aeroelastic tailoring to a composite, high aspect ratio wing of a tailless aircraft for minimum gust response. Aeroelastic tailoring has also been successfully applied in wind turbine rotor blade (Deilmann, 2009; Kim et al., 2013; Scott et al., 2017) for improving the aeroelastic characteristics. One of the important aspects of aeroelastic tailoring is to assess aeroelastic characteristics such as divergence and flutter for composite wing in the subsonic, transonic and supersonic flight regimes. All these examples call for the development of an accurate and efficient approach to assess the aeroelastic characteristics (Cesnik et al., 1996).

High-performance modern aircraft often cruises at transonic flow regime to achieve high performance (Rizk, 1981). Therefore, it is particularly important to analyze and assess the transonic aeroelastic characteristics of aircraft. For accurate aeroelastic predictions, a high-fidelity fluid model is highly needed. In computational fluid analysis, linear potential flow theory provides a low-cost and high efficiency way for subsonic and supersonic aeroelastic stability analysis. Unfortunately, the linear aerodynamic theories formally fail due to the inherently nonlinear characteristics of the transonic flow. Fortunately, computational fluid dynamics (CFD) methods based on Euler or Reynolds-averaged Navier–Stokes (RANS) equations are available for transonic aeroelasticity. However, these full order models (FOMs), including finite element analysis (FEA) and CFD, require large computer memories and have high computational cost, making these methods impractical for routine use.

To circumvent the computational limitations encountered in transonic aeroelasticity, researchers proposed CFD-based unsteady aerodynamic reduced order models (ROMs). These ROMs extract key data of the fluid systems to generate a low dimensional system that retains similar accuracy of the full order model while reducing significantly the costs. System identification and proper orthogonal decomposition (POD) are the two most commonly used ROMs for nonlinear aeroelastic analysis. In the aeroelastic modeling field, ROMs have been used to simulate the nonlinear dynamics due to the fluid structure interaction. For example, Dowell (Dowell et al., 2004) and Zhang (Zhang et al., 2016) demonstrated the use of ROMs to investigate limit-cycle oscillation (LCO) in transonic flow. Zaide (Zaide and Raveh, 2006) presented the responses to discrete gusts of various shapes, amplitudes, and gradient lengths are computed via the ROMs throughout the subsonic and transonic regimes. Bekemeyer (Bekemeyer and Timme, 2017) discussed the ROMs of large civil aircraft under gust excitation in transonic flight for routine gust load analysis. For the POD method, which projects the flow snapshots into several dominant low-order vector bases, has been successfully applied to aeroelastic analysis in many fields of engineering, such as turbine blades (Cizmas and Palacios, 2003; Clark et al., 2012), helicopter rotor blade (Mariappan et al., 2014), wings (Demasi and Palacios, 2010; Stanford and Beran, 2013; Hesse and Palacios, 2014) and complete aircraft configurations (Lieu et al., 2006; Amsallem et al., 2007). Until now, CFD-based POD/ROM has been exercised for active aeroelastic control (Chen et al., 2014), LCO control in transonic flow (Chen et al., 2013), gust response analysis (Zhou et al., 2016a, 2017), and transonic flutter suppression with control delay (Zhou et al., 2016b). However, the majority of previous work is only adequate for a fixed flight condition and a given structural model, i.e. changes to flight conditions (Mach number, angle of attack, etc.) and structural parameters (mass, etc.) are excluded.

During the aeroelastic tailoring process, the composite structural model undergoes multiple changes until the desired requirements of aeroelastic performance are met. Unfortunately, traditional CFD-based ROMs are for fixed flight condition and a ‘‘frozen’’ model configuration. In order to accurately assess the aeroelastic characteristics of composite structure in aeroelastic tailoring process, both the structural model and the CFD-based POD/ROM have to be reconstructed. Rather than reconstructing a new POD/ROM, researchers have focused at improving the shortcoming of traditional ROMs. Lieu (Lieu and Lesoinne, 2004; Lieu and Farhat, 2006, 2007) demonstrated the use of ROMs to predict the transonic aeroelastic response and take into account variations of Mach number and angle of attack. Winter (Winter and Breitsamter, 2016b) presented a novel aerodynamic ROM approach for predicting generalized aerodynamic forces with variations of in Mach number using local linear neuro-fuzzy models. Winter (Winter and Breitsamter, 2016a) demonstrated an unsteady aerodynamic surrogate modeling approach for the prediction of surface pressure fluctuations and integral force and moment coefficients undergoing a pitching motion at high subsonic and transonic flow conditions, based on the POD method combined with a local linear neuro-fuzzy model.

However, few studies has considered the aeroelastic response for variations in the structural parameters within a ROM. When a composite structure modification is made by varying the ply thickness, ply material or stacking sequence, the structural model need to be updated and the new modeshapes and frequencies recalculated. In an aeroelastic analysis, the influence of changes in the structural modeshapes will also affect the solution of the fluid model. Methods which construct a new CFD-based ROM are denoted direct methods. For every change of the composite structural model, both structural modeshapes and associated frequencies and the ROM around the new equilibrium position should be regenerated, and each of these regeneration cycles takes a considerable time, which jeopardize the computational efficiency. To overcome the related computational expense, Fenwick (Fenwick et al., 2007) used a linear interpolation on a set of available ROMs to obtain a new ROM without regeneration for local mass redistribution (e.g. fuel load redistribution). Zhang (Zhang et al., 2015) demonstrated a method to obtain a new ROM using existing CFD-based auto regressive with eXogenous input (ARX) ROM based on radial basis function (RBF) interpolation functions for local changes of the root boundary condition. Winter (Winter et al., 2017) presented two novel CFD based reduced-order modeling methodologies robust to variations in the structural modeshapes due to the additional lumped mass.

However, most of the studies mentioned above only focused the attention on structural modifications at local level. Usually, the optimization of composite structure considers a large number of variables to describe the structural properties, and this results in a large problem requiring high computational resources. In view of these considerations, the bi-level approach has become one of the most popular techniques in recent years (Liu et al., 2000). The approach is commonly divided into global and local level. At the first step, it gives a global continuous description of the composite wing without the details for each region (Zhao et al., 2016). In this step, the stacking sequence of different orientations is fixed, and lamination parameters treated as continuous design variables. This step provides information to the local discrete level problem which give a detail description of the stacking sequences for each sub-region (Zhao et al., 2015). At the global level, wing modifications consist generally of changes to the mass and stiffness distribution to meet the design target loads. This calls for an efficient ROM formulation that presents the ability to investigate the impact of global structural modifications for the deployment to aeroelastic tailoring.

In this paper, we propose a new approximate aeroelastic characteristics evaluation method by introducing the structural dynamic reanalysis method with global level structural parameters modification in the aeroelastic tailoring process. This method has potential to be a powerful tool for aeroelastic tailoring to design new structures. The application is for a composite wing with planform given by the AGARD 445.6 model, and structural model parameters are changed at global level. Results show that the approximate aeroelastic characteristics evaluation method can produce the impulse responses and flutter boundary rapidly with enough accuracy. The paper is built as follows: Section 2 gives the brief introduction to the classic theory of composite laminates and the standard POD/ROM construction procedure for aeroelastic systems; Section 3 gives a description on the dynamic reanalysis based aeroelastic analysis method firstly, and then introduce the proposed incorporation procedure of the structural reanalysis algorithm with the POD/ROM construction method for aeroelastic characteristics evaluation with global structural parameter variation; In Section 4 the proposed approximate aeroelastic characteristics evaluation method was demonstrated and evaluated by an improved AGARD 445.6 aeroelastic wing model with global level structural parameters variation in transonic flow. Section 5 is the conclusion and discussion of the proposed method.

## 2. Overview of traditional direct evaluation method

To understand the fundamental principles underlying the aeroelastic tailoring of composite materials, and thus it is essential to understand both mechanics of composite materials and aeroelastic theory based on CFD-based POD/ROMs.

## 2.1. Mechanical model of composite laminates

The aeroelastic tailoring process must be done with attention to the mechanics of composite materials. The classical lamination theory (CLT) is a widely used theory used to analyze the composite structures. Classical lamination theory is an extension the standard plate bending and plane stress theories for layered plates with varying stiffness of each ply. In this theory, the constitutive equation of laminate plate is described as:

$$\begin{array} {r} {\left[ \begin{array} {l} {\mathbf {N}} \\ {\mathbf {M}} \end{array} \right] = \left[ \begin{array} {l l} {\mathbf {A}} & {\mathbf {B}} \\ {\mathbf {B}} & {\mathbf {D}} \end{array} \right] \left[ \begin{array} {l} {\pmb {\varepsilon}} \\ {\kappa} \end{array} \right]} \end{array}\tag{1}$$

where N and M are the distributed tractions and moments, respectively. Here, ε are midplane strains, and κ is the vector of curvatures. The sub-matrices A, B and D are the extensional stiffness matrix, the coupling stiffness matrix and the bending stiffness matrix, respectively, and by altering the stacking sequence and ply angle of a laminate, the sub-matrices A, B and D will change. So the stacking sequence and laminate ply angle of the composite structure are generally selected as design variables in the aeroelastic tailoring process. In particular, for symmetric plates, the coupling stiffness matrix B is zero. Each sub-matrix can be described as follow:

$${\pmb {\mathsf{A}}} _ {i j} = \sum _ {k = 1} ^ {n} {\overline {{\mathbf {Q}}}} _ {i j} ^ {( k )} {\left( {\bf z} _ {k} - {\bf z} _ {k - 1} \right)}$$

$${\bf B} _ {i j} = \frac {1} {2} \sum _ {k = 1} ^ {n} \overline {{{\bf Q}}} _ {i j} ^ {( k )} ( z _ {k} ^ {2} - z _ {k - 1} ^ {2} ) \qquad i , j = 1 , 2 , 6\tag{2}$$

$$\mathbf {D} _ {i j} = \frac {1} {3} \sum _ {k = 1} ^ {n} \overline {{\mathbf {Q}}} _ {i j} ^ {( k )} ( z _ {k} ^ {3} - z _ {k - 1} ^ {3} )$$

where $\mathbf {Z} _ {k}$ is the distance from laminate midplane to the bottom of the kth ply, $\overline {{\mathbf {Q}}} _ {i j} ^ {( k )}$ is the transformed stiffness matrix of the kth ply, it is related to elastic mechanical properties and fiber orientation of the individual plies, and n is the number of plies, as shown in Fig. 1. A complete discussion about the formulation of all the matrices presented above can be found in Jones and Bert (1975) and Reddy (2004). The mass matrix M and stiffness matrix K of composite materials can be obtained through the standard finite element generated and assembly process performed on the corresponding elemental matrices (Matthews et al., 2000).

## 2.2. CFD-based reduced order model for aeroelastic system

POD is a technique to reproduce the behavior of the overall system behavior with a small number of degrees of freedom. For simplicity, here we consider inviscid flows modeled by the Euler equations, POD used to construct a reduced-order model for Euler equations (Lucia et al., 2004). First, the unsteady Euler equations are linearized around a mean flow solution (equilibrium position). The linearized flow solver is then used to obtain the POD snapshots for the generation of the unsteady aerodynamic ROM. Denoting (∂w,∂u,∂u˙ ) small perturbation around the equilibrium $( \mathbf {w} _ {0} , \mathbf {u} _ {0} , \dot {\mathbf {u}} _ {0} )$ , where w is the vector of conservative flow variables, and u the structural displacement vector. One obtains the linearized flow equations:

$$\pmb {\mathrm{A}} _ {0} \dot {\pmb {w}} + \pmb {\mathrm{H}} \pmb {w} + ( \pmb {\mathrm{E}} + \pmb {\mathrm{C}} ) \dot {\pmb {\mathrm{u}}} + \pmb {\mathrm{G}} \pmb {\mathrm{u}} = \pmb {0}\tag{3}$$

where

$$\mathbf {H} = {\frac {\partial \mathbf {F}} {\partial \mathbf {w}}} ( \mathbf {w} _ {0} , \mathbf {u} _ {0} , {\dot {\mathbf {u}}} _ {0} ) \qquad \mathbf {G} = {\frac {\partial \mathbf {F}} {\partial \mathbf {u}}} ( \mathbf {w} _ {0} , \mathbf {u} _ {0} , {\dot {\mathbf {u}}} _ {0} )$$

$$\mathbf {E} = \frac {\partial \mathbf {A}} {\partial \mathbf {u}} \mathbf {w} _ {0} \qquad \mathbf {c} = \frac {\partial \mathbf {F}} {\partial \dot {\mathbf {u}}} ( \mathbf {w} _ {0} , \mathbf {u} _ {0} , \dot {\mathbf {u}} _ {0} )$$

Here, A is the diagonal matrix of cell volumes, F is the nonlinear numerical flux. The matrices H, E, G and C are the firstorder terms of a Taylor expansion of the non-dimensional numerical flux function around the equilibrium $( \mathbf {w} _ {0} , \mathbf {u} _ {0} , \dot {\mathbf {u}} _ {0} )$ . The matrix H is the gradient of the numerical flux function with respect to the vector of fluid variables. Matrices G and C are the gradients of the flux function with respect to the generalized coordinates and their velocities, respectively. Finally, the matrix E indicates the gradient of the cell volumes with respect to the generalized coordinates. Note that the matrices G, E and C need to be recomputed if the structural parameters are changed.

The linearization of the structural dynamic equation around an equilibrium state can be written as follows:

$$\overline {{\mathbf {M}}} \ddot {\mathbf {u}} + \overline {{\mathbf {D}}} _ {0} \dot {\mathbf {u}} + \overline {{\mathbf {K}}} _ {s} \mathbf {u} = \mathbf {P} _ {0} \mathbf {w}\tag{4}$$

where

$$\overline {{\mathbf {K}}} _ {0} = \frac {\partial \mathbf {f} ^ {i n t}} {\partial \mathbf {u}} ( \mathbf {u} _ {0} , \dot {\mathbf {u}} _ {0} ) \qquad \overline {{\mathbf {K}}} _ {s} = \overline {{\mathbf {K}}} _ {0} - \frac {\partial \mathbf {f} ^ {e x t}} {\partial \mathbf {u}} ( \mathbf {w} _ {0} , \mathbf {u} _ {0} )$$

$$\overline {{{\bf D}}} _ {0} = \frac {\partial {\bf f} ^ {i n t}} {\partial \dot {\bf u}} ( {\bf u} _ {0} , \dot {\bf u} _ {0} ) \qquad {\bf P} _ {0} = \frac {\partial {\bf f} ^ {e x t}} {\partial {\bf w}} ( {\bf w} _ {0} , {\bf u} _ {0} )$$

For the analysis of the system stability, the terms $\frac {\partial \mathbf {f} ^ {e x t}} {\partial \mathbf {u}}$ and $\overline {{\mathbf {D}}} _ {0}$ can be neglected, which leads to the structural dynamic equation such as:

$$\overline {{\mathbf {M}}} \ddot {\mathbf {u}} + \overline {{\mathbf {K}}} _ {0} \mathbf {u} = \mathbf {P} _ {0} \mathbf {w}\tag{5}$$

The linearized CFD-based aeroelastic equations of Eqs. (3) and (5) are too large for aeroelastic system for aircraft. Therefore, the full order models (FOMs) have to be reduced. For illustration purpose, the proper orthogonal decomposition (POD)

approach is used to reduce the aeroelastic system. Denote $\mathbf {x} ^ {k} , k = 1 , 2 , 3 \ldots m ,$ a set of data, with $\mathbf {x} ^ {k}$ is the n-dimensional space, and m is the number of snapshots. The POD method searches an m-dimensional proper orthogonal subspace, $\pmb {\psi} \in$ $\mathbf {R} ^ {n \times m}$ , to minimize the mapping errors from $\pmb {\psi}$

$$\mathbf {G} = \operatorname* {m i n} _ {\phi} \sum _ {k = 1} ^ {m} \left\| {\mathbf {x}} ^ {k} - \varOmega \varOmega ^ {T} {\mathbf {x}} ^ {k} \right\| = \sum _ {k = 1} ^ {m} \left\| {\mathbf {x}} ^ {k} - \varPsi \varPsi ^ {T} {\mathbf {x}} ^ {k} \right\| , \quad \varOmega ^ {H} \varOmega = \mathbf {I}\tag{6}$$

The minimization problem is equivalent to

$$\mathbf {H} = \operatorname* {m a x} _ {\boldsymbol {\Phi}} \sum _ {k = 1} ^ {m} \frac {\left. \left( \mathbf {x} ^ {k} , \boldsymbol {\Omega} \right) ^ {2} \right.} {\left. \boldsymbol {\Omega} \right. ^ {2}} = \sum _ {k = 1} ^ {m} \frac {\left. \left( \mathbf {x} ^ {k} , \boldsymbol {\Psi} \right) ^ {2} \right.} {\left. \boldsymbol {\Psi} \right. ^ {2}} , \quad \boldsymbol {\Omega} ^ {H} \boldsymbol {\Omega} = \mathbf {I}\tag{7}$$

The constraint optimization problem in $\operatorname{Eq.} \left( 7 \right)$ is transformed into the following Lagrange equation

$$J \left( \Omega \right) = \sum _ {k = 1} ^ {m} \left( {\bf x} ^ {k} , \Omega \right) ^ {2} - \lambda \left( \left. \Omega \right. ^ {2} - 1 \right)\tag{8}$$

Solving the partial derivative of the objective function $J ( \varOmega )$ with respect to $\pmb {\it {\Omega}}$ gives

$$\frac {d} {d \Omega} J \left( \Omega \right) = 2 \mathbf {X} \mathbf {X} ^ {H} \Omega - 2 \lambda \Omega\tag{9}$$

where ${\bf X} = {\bf x} _ {1} , {\bf x} _ {2} , . . . {\bf x} _ {m} \in \mathbb {R} ^ {n \times m}$ is a matrix containing m snapshots as columns. By setting Eq. (9) to zero; thus, the following equation is obtained:

$$\left( \mathbf {X} \mathbf {X} ^ {T} - \xi \mathbf {I} \right) \varPsi = 0\tag{10}$$

The problem is transformed into solving the eigenvalue problem of the POD kernel, $\mathbf {X X} ^ {H}$ . The eigenvalue problem has very large size, as $\mathbf {X} \mathbf {X} ^ {H} \in \mathbf {R} ^ {n \times n}$ . Because $\mathbf {X X} ^ {H}$ and $\mathbf {X} \bar {\mathbf {X} ^ {H}}$ have the same eigenvalues, so we can obtain Ψ as following equation:

$$\left\{\begin{array} {l l} {\mathbf {X} \mathbf {X} ^ {T} \mathbf {V} = \mathbf {V} A} \\ {\pmb {\varPsi} = \mathbf {X} \mathbf {V} A ^ {- 1 / 2}} \end{array} \right.\tag{11}$$

where $\varPsi = [ \psi _ {1} , \psi _ {2} , \ldots , \psi _ {m} ] , \varLambda = d i a g ( \xi _ {1} , \xi _ {2} , \ldots , \xi _ {m} ) , \xi _ {1} \geq \xi _ {2} \geq . . . , \geq \xi _ {m}$ The value of $\xi _ {i}$ represents the contribution of the ith snapshot to the original system. To build an aeroelastic ROM, it is typically possible to retain the first r-order POD modes $\pmb {\varPsi} _ {r} = [ \pmb {\psi} _ {1} , \pmb {\psi} _ {2} , \dots , \pmb {\psi} _ {r} ]$ while retaining most of the energy of the original system. By projecting the full-order series $\mathbf {x} ^ {n \times 1}$ on the r-order POD modes $\pmb {\varPsi} _ {r} = [ \pmb {\psi} _ {1} , \pmb {\psi} _ {2} , \dots , \pmb {\psi} _ {r} ]$ , we can reduced the full order system to a reduced r-order system

$$\left\{\begin{array} {l l} {\dot {\mathbf {x}} _ {r} = \boldsymbol {\varPsi} _ {r} ^ {T} \mathbf {A} \boldsymbol {\varPsi} _ {r} \mathbf {x} _ {r} + \boldsymbol {\varPsi} _ {r} ^ {T} \mathbf {B} \mathbf {y}} \\ {\mathbf {f} ^ {e x t} = \mathbf {C} \boldsymbol {\varPsi} _ {r} \mathbf {x} _ {r}} \end{array} \right.\tag{12}$$

where $\begin{array} {r} {\pmb {\mathrm{A}} = - \pmb {\mathrm{A}} _ {0} ^ {- 1} \pmb {\mathrm{H}} , \pmb {\mathrm{B}} = - \pmb {\mathrm{A}} _ {0} ^ {- 1} \left[ \pmb {\mathrm{E}} + \pmb {\mathrm{C}} \pmb {\mathrm{G}} \right] , \pmb {\mathrm{y}} = \left[ \pmb {\dot {\mathrm{u}}} \pmb {\mathrm{u}} \right] ^ {T} , \pmb {\mathrm{C}} = \pmb {\mathrm{P}} .} \end{array}$

By taking the advantage of anisotropic mechanical characteristics and multiple design variables of composite structure in aeroelastic tailoring, the stiffness properties of structure are characterized by its ply angles and the fraction of each ply angles in the stacking sequence. And so, when the ply angle and its fraction changed, the model shapes and frequencies may also be changed. Hayes et al. (Hayes et al., 2014) have shown that the change of modeshapes and frequencies must be taken into account for aeroelastic design. Hence, in the aeroelastic tailoring process, for modified structure model using a constant set of normal model shapes to assess the aeroelastic characteristics of composite structure will produce an inaccurate aeroelastic results. In order to accurately assess the aeroelastic properties of composite structure, both structure model and CFD-based POD/ROM have to be recalculated, which is called direct evaluation method. Furthermore, these reconstructions have to be repeated every time whenever a parameter is modified in the composite structure, which destroys the computational efficiency of the CFD-based POD/ROM and could not be applied directly in the transonic aeroelastic tailoring.

## 3. Approximate aeroelastic characteristics evaluation method

## 3.1. Structural dynamic reanalysis method

In structural optimization, it is very important to recompute the eigenvalues and eigenvectors of the structures when the parameters of the structures are changed. In many cases, one of main obstacles is the high computational cost involved in the solution of a large-scale eigenvalue problem. To this goal, a number of methods (Kirsch, 2008) have been proposed to ease the eigenvalue reanalysis for the modified structure, instead of performing full structural modal analysis. Generally, these reanalysis methods are classified into two categories (Song et al., 2014). First, direct methods are commonly based on the Sherman–Morrison–Woodbury (SMW) formula (Akgün et al., 2001) that is applicable for large but local (or lowrank) modifications. The drawback of direct methods is that they are limited by the scale of the problem or the rank of the modification, and are not suitable for global modifications of the structural parameters. Direct methods also suffer from high computational costs. As an alternative to direct methods, approximate methods (Beliveau et al., 1996; Chen and Yang, 2000; Kirsch et al., 2007) aim at obtaining the frequencies and modeshapes for the modified structures, in which the modeshapes of modified structure are approximated as a linear combination of basic modeshapes. The advantages of approximate method is a significant reduction of the computational costs, and the applicability is extended for global (or high-rank) modifications of the structure. The extended Kirsch combined method (Chen and Yang, 2000; Chen et al., 2000) is an efficient approach for the case of large modifications of the structural parameters. More details relevant to this work are given next.

The extended Kirsch combined method is an efficient approach for the case of modifications of the structural parameters. Consider an initial composite material with stiffness matrix $\mathbf {K} _ {0}$ and mass matrix $\mathbf {M} _ {0}$ The corresponding model shapes ${\boldsymbol {\phi}} _ {0} ^ {i}$ and modal frequencies $\lambda _ {0} ^ {i}$ are calculated by solving the set of initial analysis equations:

$${\bf K} _ {0} \boldsymbol {\phi} _ {0} ^ {i} = \lambda _ {0} ^ {i} {\bf M} _ {0} \boldsymbol {\phi} _ {0} ^ {i}\tag{13}$$

that is referred to as the original problem (indicated by the subscript 0). When the structural parameters are modified, and $\mathbf {M} _ {0}$ are perturbed into the form $\mathbf {K} _ {0} + \varDelta \mathbf {K} \left( \mathbf {K} {=} \mathbf {K} _ {0} + \varDelta \mathbf {K} \right)$ and $\mathbf {M} _ {0} + \varDelta \mathbf {M} ( \mathbf {M} {=} \mathbf {M} _ {0} + \varDelta \mathbf {M} )$ , respectively, in which ∆K and ∆Mare the perturbations to the original stiffness and mass matrices. The eigenvalue problem for modified structural parameters becomes:

$$\mathbf {K} \pmb {\phi} ^ {i} = \lambda ^ {i} \mathbf {M} _ {0} \pmb {\phi} ^ {i}\tag{14}$$

where $\lambda ^ {i}$ is ith eigenvalue of the modified structure, $\phi ^ {i}$ is ith eigenvector of the modified structure.

Extended Kirsch combined method use the second-order eigenvector terms (Chen et al., 1994) as the basis vectors in the following modal shape reduced basis:

$${\pmb {\phi}} ^ {i} = \phi _ {B} ^ {i} {\pmb z} ^ {i} , \qquad {\pmb z} ^ {i} = ( {\sf z} _ {0} ^ {i} , {\sf z} _ {1} ^ {i} , {\sf z} _ {2} ^ {i} ) ^ {T} \in {\bf R} ^ {3 \times 1}\tag{15}$$

where

$$\pmb {\phi} _ {B} ^ {i} = \left[ \pmb {\phi} _ {0} ^ {i} , \pmb {\phi} _ {1} ^ {i} , \pmb {\phi} _ {2} ^ {i} \right]\tag{16}$$

$$\phi _ {1} ^ {i} = \sum _ {s = 1 , s \neq i} ^ {n} \frac {1} {\lambda _ {0} ^ {i} - \lambda _ {0} ^ {s}} [ ( \phi _ {0} ^ {s} ) ^ {T} ( \varDelta \mathbf {K} - \lambda _ {0} ^ {i} \varDelta \mathbf {M} ) \phi _ {0} ^ {i} ] \phi _ {0} ^ {s} - \frac {1} {2} [ ( \phi _ {0} ^ {i} ) ^ {T} \varDelta \mathbf {M} \phi _ {0} ^ {i} ] \phi _ {0} ^ {i} = \phi _ {0} \varDelta ^ {i}\tag{17}$$

$$\begin{array} {l} {\displaystyle \phi _ {2} ^ {i} = \sum _ {s = 1 , s \neq i} ^ {n} \frac {1} {\lambda _ {0} ^ {i} - \lambda _ {0} ^ {s}} [ ( \phi _ {0} ^ {s} ) ^ {T} ( \varDelta \mathbf {K} - \lambda _ {0} ^ {i} \varDelta \mathbf {M} ) \phi _ {1} ^ {i} - \lambda _ {1} ^ {i} ( \phi _ {0} ^ {s} ) ^ {T} ( \mathbf {M} _ {0} \phi _ {1} ^ {i} + \varDelta \mathbf {M} \phi _ {0} ^ {i} ) ] \phi _ {0} ^ {s}} \\ {\displaystyle - \frac {1} {2} [ ( \phi _ {0} ^ {i} ) ^ {T} \varDelta \mathbf {M} \phi _ {1} ^ {i} + ( \phi _ {1} ^ {i} ) ^ {T} ( \mathbf {M} _ {0} \phi _ {1} ^ {i} + \varDelta \mathbf {M} \phi _ {0} ^ {i} ) ] \phi _ {0} ^ {i} = \phi _ {0} Z _ {2} ^ {i}} \end{array}\tag{18}$$

For aeroelastic tailoring, the mass of the structure is generally considered to be constant, then $\varDelta {\mathbf {M}} = {\mathbf {0}} , {\phi _ {1} ^ {i}}$ and $\pmb {\phi} _ {2} ^ {i}$ can be expressed as:

$$\phi _ {1} ^ {i} = \sum _ {s = 1 , s \neq i} ^ {n} \frac {1} {\lambda _ {0} ^ {i} - \lambda _ {0} ^ {s}} ( \phi _ {0} ^ {s} ) ^ {T} \varDelta \mathbf {K} \phi _ {0} ^ {i} \phi _ {0} ^ {s} = \phi _ {0} \mathbf {Z} _ {1} ^ {i}\tag{19}$$

$$\phi _ {2} ^ {i} = \sum _ {s = 1 , s \neq i} ^ {n} \frac {1} {\lambda _ {0} ^ {i} - \lambda _ {0} ^ {s}} [ ( \phi _ {0} ^ {s} ) ^ {T} ( \varDelta \mathbf {K} ) \phi _ {1} ^ {i} - \lambda _ {1} ^ {i} ( \phi _ {0} ^ {s} ) ^ {T} \mathbf {M} _ {0} \phi _ {1} ^ {i} ] \phi _ {0} ^ {s} - \frac {1} {2} [ ( \phi _ {1} ^ {i} ) ^ {T} \mathbf {M} _ {0} \phi _ {1} ^ {i} ] \phi _ {0} ^ {i} = \phi _ {0} \varDelta _ {2} ^ {i}\tag{20}$$

where ${\boldsymbol {\phi}} _ {1} ^ {i}$ and $\pmb {\phi} _ {2} ^ {i}$ are the ith first-order and second-order eigenvector of the modified structure, respectively. The coefficient vector, $\mathbf {z} ^ {i} ,$ contains three unknowns (for a second-order perturbation). Substituting Eqs. (19) and (20) into Eq. (15), Φ can be written as

$$\small \boldsymbol {\phi} = \left[ \begin{array} {c c c c} {\phi _ {0} ^ {1} . . . \phi _ {0} ^ {i}} & {\mathbf {0}} & {\mathbf {0}} \\ {\mathbf {0}} & {\phi _ {0} ^ {1} . . . \phi _ {0} ^ {i}} & {\mathbf {0}} \\ {\mathbf {0}} & {\mathbf {0}} & {\phi _ {0} ^ {1} . . . \phi _ {0} ^ {i}} \end{array} \right] \left[ \begin{array} {c c c c} {\mathbf {I} _ {0} ^ {1} \cdot . . . \mathbf {I} _ {0} ^ {i}} & {\mathbf {0}} & {\mathbf {0}} \\ {\mathbf {0}} & {\mathbf {Z} _ {1} ^ {1} . . . \mathbf {Z} _ {1} ^ {i}} & {\mathbf {0}} \\ {\mathbf {0}} & {\mathbf {0}} & {\mathbf {Z} _ {2} ^ {1} . . . \mathbf {Z} _ {2} ^ {i}} \end{array} \right] ^ {T} \left[ \begin{array} {c c c} {\mathbf {z} ^ {1}} & {\mathbf {0}} & {\mathbf {0}} \\ {\mathbf {0}} & {\mathbf {z} ^ {2}} & {\mathbf {0}} \\ {\mathbf {0}} & {\mathbf {0}} & {\mathbf {z} ^ {3}} \end{array} \right] = \bar {\boldsymbol {F}} _ {0} \mathbf {Z}\tag{21}$$

where

$$\mathbf {Z} = \left[ \begin{array} {c c c} {\mathbf {I} _ {0} ^ {1} . . . \mathbf {I} _ {0} ^ {i}} & {\mathbf {0}} & {\mathbf {0}} \\ {\mathbf {0}} & {\mathbf {Z} _ {1} ^ {1} . . . . \mathbf {Z} _ {1} ^ {i}} & {\mathbf {0}} \\ {\mathbf {0}} & {\mathbf {0}} & {\mathbf {Z} _ {2} ^ {1} . . . . \mathbf {Z} _ {2} ^ {i}} \end{array} \right] ^ {T} \left[ \begin{array} {c c c} {\mathbf {z} ^ {1}} & {\mathbf {0}} & {\mathbf {0}} \\ {\mathbf {0}} & {\mathbf {z} ^ {2}} & {\mathbf {0}} \\ {\mathbf {0}} & {\mathbf {0}} & {\mathbf {z} ^ {3}} \end{array} \right]\tag{22}$$

Substituting Eq. (15) into the modified analysis equations Eq. (14), and premultiplying by $( \phi _ {B} ^ {i} ) ^ {T}$ , one obtains:

$$( \phi _ {B} ^ {i} ) ^ {T} ( {\bf K} _ {0} + \Delta {\bf K} ) \phi _ {B} ^ {i} {\bf z} ^ {i} = \lambda ^ {i} ( \phi _ {B} ^ {i} ) ^ {T} {\bf M} _ {0} \phi _ {B} ^ {i} {\bf z} ^ {i}\tag{23}$$

Introducing the notation

$$\mathbf {K} _ {R} ^ {i} = ( \pmb {\phi} _ {B} ^ {i} ) ^ {T} ( \mathbf {K} _ {0} + \varDelta \mathbf {K} ) \pmb {\phi} _ {B} ^ {i}\tag{24}$$

$$\mathbf {M} _ {R} ^ {i} = ( \pmb {\phi} _ {B} ^ {i} ) ^ {T} \mathbf {M} _ {0} \pmb {\phi} _ {B} ^ {i}\tag{25}$$

and substituting Eqs. (20) and (21) into Eq. (15), we can obtain a set of $( 3 \times 3 )$ matrix equation

$$\mathbf {K} _ {R} ^ {i} \mathbf {z} ^ {i} = \lambda ^ {i} \mathbf {M} _ {R} ^ {i} \mathbf {z} ^ {i}\tag{26}$$

Thus, the coefficient vector $\pmb {z} ^ {i}$ is evaluated from Eq. (26). The ith eigenvector of the modified structure is obtained by substituting $\pmb {z} ^ {i}$ into Eq. (15) and Z is obtained by substituting zi into Eq. (22).

Finally, the ith eigenvalue of the modified structure, $\lambda _ {K} ^ {i}$ , is computed using Rayleigh quotient:

$$\lambda _ {K} ^ {i} = \frac {( \pmb {\phi} ^ {i} ) ^ {T} ( \mathbf {K} _ {0} + \varDelta \mathbf {K} ) \pmb {\phi} ^ {i}} {( \pmb {\phi} ^ {i} ) ^ {T} \mathbf {M} _ {0} \pmb {\phi} ^ {i}}\tag{27}$$

## 3.2. Aeroelastic characteristics evaluation method for modified structure

The modeshapes $\pmb {\varPhi} _ {0}$ of the original structure is taken as the basic modeshapes for basic POD/ROM construction. For modified structure, the physical displacement Θ of the wing can be written as

$$\Theta = \varPhi \mathbf {{u}}\tag{28}$$

Substituting Eq. (21) into Eq. (28), the physical displacement of the wing can also be written as

$$\boldsymbol {\Theta} = \boldsymbol {\varPhi} _ {0} ( \mathbf {Z} \mathbf {u} )\tag{29}$$

and ${\mathbf {u}} _ {b} = {\mathbf {Z}} {\mathbf {u}} , {\mathbf {u}} _ {b}$ is artificially defined as basic generalized displacements.

A change of the structural parameters affects the matrices G, E and C of the linearized flow solver, Eq. (3). Substituting the relation $\mathbf {u} _ {b} = \mathbf {Z} \mathbf {u}$ , the matrices may be rewritten in terms of the vector of basic generalized displacements:

$$\mathbf {G} = {\frac {\partial \mathbf {F}} {\partial \mathbf {u}}} ( \mathbf {w} _ {0} , \mathbf {u} _ {0} , {\dot {\mathbf {u}}} _ {0} ) = {\frac {\partial \mathbf {F}} {{\pmb {Z}} ^ {- 1} \partial \mathbf {u} _ {b}}} ( \mathbf {w} _ {0} , \mathbf {u} _ {0} , {\dot {\mathbf {u}}} _ {0} ) = \mathbf {Z} \mathbf {G} _ {b}$$

$$\mathbf {E} = {\frac {\partial \mathbf {A}} {\partial \mathbf {u}}} \mathbf {w} _ {0} = {\frac {\partial \mathbf {A}} {\mathbf {Z} ^ {- 1} \partial \mathbf {u} _ {b}}} \mathbf {w} _ {0} = \mathbf {Z} \mathbf {E} _ {b}\tag{30}$$

$$\mathbf {C} = {\frac {\partial \mathbf {F}} {\partial {\dot {\mathbf {u}}}}} ( \mathbf {w} _ {0} , \mathbf {u} _ {0} , {\dot {\mathbf {u}}} _ {0} ) = {\frac {\partial \mathbf {F}} {{\mathbf {Z}} ^ {- 1} \partial {\dot {\mathbf {u}}} _ {b}}} ( \mathbf {w} _ {0} , \mathbf {u} _ {0} , {\dot {\mathbf {u}}} _ {0} ) = \mathbf {Z} \mathbf {C} _ {b}$$

where $\mathbf {G} _ {b} , \mathbf {E} _ {b} , \mathbf {C} _ {b}$ are the first order terms in a Taylor series expansion of the basis reduced r-order system aeroelastic. Now, the reduced fluid model of modified structure is written as

$$\left\{\begin{array} {l l} {\dot {\mathbf {x}} _ {r} = \pmb {\varPsi} _ {r} ^ {T} \mathbf {A} \pmb {\varPsi} _ {r} \mathbf {x} _ {r} + \pmb {\varPsi} _ {r} ^ {T} \mathbf {Z} \mathbf {B} _ {b} \mathbf {y}} \\ {\mathbf {f} ^ {e x t} = \mathbf {Z} \mathbf {C} _ {b} \pmb {\varPsi} _ {r} \mathbf {x} _ {r}} \end{array} \right.\tag{31}$$

$$\begin{array} {r} {\mathrm{where} \ : \mathbf {A} = - \mathbf {A} _ {0} ^ {- 1} \mathbf {H} , \mathbf {B} _ {b} = - \mathbf {A} _ {0} ^ {- 1} \left[ \mathbf {E} _ {b} + \mathbf {C} _ {b} \mathbf {G} _ {b} \right] , \mathbf {y} = \left[ \dot {\mathbf {u}} \mathbf {u} \right] ^ {T} , \mathbf {C} _ {b} = \mathbf {P} _ {b} .} \end{array}$$

The structural dynamic equations of modified structure are:

$$\overline {{\mathbf {M}}} \ddot {\mathbf {u}} + \overline {{\mathbf {K}}} \mathbf {u} = \mathbf {f} ^ {e x t}\tag{32}$$

here, $\overline {{\mathbf {M}}} = \mathbf {Z} ^ {T} \mathbf {\Phi} \mathbf {\Phi} \mathbf {\Phi} _ {0} ^ {T} \mathbf {M} _ {0} \mathbf {\Phi} \mathbf {\Phi} \mathbf {\Phi} \Phi _ {0} \mathbf {Z} , \overline {{\mathbf {K}}} = \mathbf {Z} ^ {T} \mathbf {\Phi} \mathbf {\Phi} \mathbf {\Phi} \mathbf {\Phi} ^ {T} ( \mathbf {K} _ {0} + \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Delta} \mathbf {\Phi} ) \mathbf {\Phi} \Phi _ {0} \mathbf {Z}$ . In addition, when $\varDelta \mathbf {K} = \mathbf {0} , \mathbf {Z}$ is the unit matrix, Eqs. (31) and (32) are equivalent to Eqs. (12) and (5), respectively.

The generalized aerodynamic loads $\mathbf {f} ^ {e x t}$ corresponding to the new modeshapes $\pmb {\mathcal {P}}$ of the global modification structural model can be rapidly calculated without the expensive time-consuming reconstruction procedure of the new POD basis.

The proposed appropriate structural dynamic reanalysis based proposed approximate aeroelastic characteristics evaluation method is illustrated in Fig. 2.

To summarize, the proposed approximate aeroelastic characteristics evaluation method consists of the following steps:

(1) Establish CFD-based POD/ROMs based on the basis modeshapes;

(2) Use extended Kirsch combined method to get Z;

(3) Per Eq. (25), transform generalized displacements u to the basis generalized displacements ub;

(4) Input the basis generalized displacements ${\bf u} _ {\mathrm{b}}$ into POD/ROMs based on the basis modeshapes to obtain the generalized aerodynamic force coefficients $\mathbf {f} ^ {e x t}$

(5) Finally, combining reduced fluid model Eq. (31) and the structural dynamic model Eq. (32) to compute the generalized aerodynamic force coefficients corresponding to the modeshapes Φ.

When the composite structure are modified at global level, the generalized aerodynamic force (GAF) corresponding to the modeshapes can be computed quickly by repeating steps 1–5, rather than constructing a new set of POD/ROMs basis. The proposed approximate aeroelastic characteristics evaluation method can significantly reduce the computational cost which would be convenient for the transonic aeroelastic tailoring with global structural modification.

## 4. Numerical results and discussion

## 4.1. POD/ROM solver validation

Before demonstrating the efficiency and accuracy of the proposed approximate aeroelastic characteristics evaluation method for transonic aeroelastic tailoring with global structural parameter variations, the POD/ROM solver is validated firstly using the AGARD 445.6 aeroelastic wing model (Yates, 1987). The AGARD 445.6 aeroelastic model is with a 45 deg quarter-chord sweep angle, a panel aspect ratio of 1.6525, and a taper ratio of 0.6576 with a symmetrical NACA65A004 airfoil section, as shown in Fig. 5. The wing material properties were with the density of 381.98 Kg/m3. The elastic modulus in the span-wise direction and the chord-wise direction is 3.151 and 0.416 GPa, respectively. The shear modulus is 0.4392 GPa, the Poisson’s ratio is 0.31 (Zhong and Xu, 2016). The structural model, shown in Fig. 3(a), consists of 231 nodes and 200 elements. The thickness distribution of the wing was governed by airfoil shape.

A multi-block structured mesh was employed for the flow solver, consisting of 61 computational nodes around each airfoil section and 20 nodes along the wing semispan, as shown in Fig. 3(b). The spatial convergence of the CFD mesh was analyzed in Zhou (Zhou et al., 2016b), which reported a good agreement of the results from both the medium and fine grids. The total number of grid points on the medium grid, herein used, is 223,146 $( 99 \times 49 \times 46 )$ . Fig. 4 shows the flutter speed predictions computed by the present coupled CFD/CSD solver and the POD/ROM solver. For comparison, experimental data from Yates (1987) are also included. The agreement between the ROM and the large computational aeroelastic solver is good for all Mach numbers considered (0.499 to 1.141), including the well-known transonic dip of the flutter speed. The accuracy of both methods have been evaluated over the years in a number of aeroelastic studies (Chen et al., 2012; Zhou et al., 2014, 2016b).

(b)

## 4.2. Accuracy evaluation of the structural dynamic reanalysis model

In this paper, an improved AGARD 445.6 aeroelastic wing model, its structural properties is replaced by composite materials, was employed to demonstrate and evaluate the accuracy and efficiency of the proposed approximate aeroelastic characteristics evaluation method. The quarter-chord line of the wing is defined as the local laminate’s 0 deg ply direction, other ply directions are defined relative to the local laminate’s 0 deg ply direction, as shown in Fig. 5, this figure also show the planform and dimensions of AGARD 445.6.

The ply angles cannot be chosen arbitrarily. In order to comply with certification requirements and meet practical aircraft applications of composite materials, ply angles are restricted to 0, 45, −45, and 90 deg. In this paper, the case study makes several simplifying assumptions that make it tractable. The composites structure are limited to a symmetric construction with respect to the midplane of the wing, and stacking sequence of composite layers is fixed as 0◦, 45◦, −45◦ and 90◦. For initial model, the fraction of each ply angles in the stacking sequence is 25%. The tailoring is achieved by varying the fraction of each ply angles in the stacking sequence. Because the ply angle does not affect the mass of structure, so wing mass is constant. According to the general principles of composite laminate design, which is commonly applied in the industry, the fraction of each ply angles not be less than 10%. In order to test the proposed approximate aeroelastic characteristics evaluation method, some assumptions have been made to allow variation of fraction of each ply angles in the wing, the three case studies has been chosen as shown in Table 1.

To assess the accuracy of the extended Kirsch combined method in analyzing the modal characteristics of the modified structural model, two criteria are introduced. The first represents the error of the modal frequencies:

$$E r r o r = \frac {f _ {A} ^ {i} - f _ {E} ^ {i}} {f _ {E} ^ {i}}$$

where $f _ {E} ^ {i}$ denotes the exact modal frequencies, which are computed through a direct full modal analysis, and $f _ {A} ^ {i}$ denotes the approximate modal frequencies obtain by the extended Kirsch combined method. The second criterion is the Modal Assurance Criterion (MAC), defined as:

$$\mathsf{MAC} ( \boldsymbol {\varPhi} _ {A} , \boldsymbol {\varPhi} _ {E} ) = \frac {\left| \boldsymbol {\varPhi} _ {E} ^ {T} \boldsymbol {\varPhi} _ {A} \right| ^ {2}} {( \boldsymbol {\varPhi} _ {A} ^ {T} \boldsymbol {\varPhi} _ {A} ) ( \boldsymbol {\varPhi} _ {E} ^ {T} \boldsymbol {\varPhi} _ {E} )}$$

where $\pmb {\varPhi} _ {E}$ represents the exact modeshapes (direct full modal analysis), and ΦA $\pmb {\varPhi} _ {A}$ represents the approximate modeshapes (extended Kirsch combined method). For a perfect match between the exact and approximate modeshape, the value of MAC is 1. The error of the frequencies of these three models and the MAC of modal modes are shown in Table 2. For the sake of brevity, Fig. 6 only shows the exact and approximate modal characteristics of the initial model and model B, respectively. As can be seen from Table 2, the maximum frequency error does not exceed 4%, and value of MAC is very close to 1. This shows that the extended Kirsch combined method can obtain the structural modal data with high precision in the aeroelastic tailoring process.

## 4.3. Accuracy evaluation of the aeroelastic characteristics evaluation method

After evaluating the accuracy of the POD/ROM solver and the structural dynamic reanalysis model using the improved AGARD 445.6 wing, which are both the key procedures of the proposed approximate aeroelastic characteristics evaluation method, the whole approximate evaluation method will be evaluated in this section. According to Eq. (31), the approximate method transform the generalized aerodynamic force (GAF) based on the original modeshapes (as shown in Fig. 6(a)) to the aerodynamic responses corresponding to modified modeshapes.

(b)

The time histories of the GAF predicted by the direct and the proposed approximate aeroelastic characteristics evaluation method are shown in Fig. 7. For simplifying the description, only the aeroelastic responses with Model B at the Mach number of 0.960 and the zero angle of attack (AOA) are shown in Fig. 6. As it can be seen, the aeroelastic responses predicted by both methods agree fairly well. The other cases with the different structural parameter variations have the similar conclusions. The well agreements initially indicate that the proposed approximate aeroelastic characteristics evaluation method can accurately capture the generalized unsteady aerodynamic responses corresponding to the global structural parameter variations.

For further demonstrating the accuracy of the approximate aeroelastic characteristics evaluation method, two typical aeroelastic structural time responses (decaying and diverging) for the three different structural parameter variation cases under different free stream dynamic pressures are compared as shown in Figs. 8–10. The aeroelastic responses are both obtained by the direct and approximate aeroelastic characteristics evaluation method, respectively. It can be seen that in all the three different structural modification cases, both the divergent and convergent aeroelastic time responses are well consistent. It indicates again that the approximate aeroelastic characteristics evaluation method has good accuracy for aeroelastic response prediction of the improved AGARD 445.6 wing in a very large range of composite structural parameter variation, without reconstructing a new set of POD/ROMs basis corresponding to the new structural model.

The flutter speeds for different case studies predicted by the two methods are illustrated in Table 3. The results show that the flutter speed predicted by the different methods are well consistent with each other. Although there are some deviations in the flutter speed obtained by these two methods, the max difference is still less than 2%. It should be note that the flutter speed of Model A and C are very close. The reason is that although the fraction of each ply angles in the stacking sequence of Model A and C are different, their frequencies and model shapes are basically the same, as shown in Table 2, and for the MAC values between Model A and C of first four modes is 0.9972, 0.9977, 0.9993, 0.9994. All of the above comparison results indicate that the proposed approximate aeroelastic characteristics evaluation method can capture the generalized displacement responses and predict the flutter boundary speed with good accuracy corresponding to the great global structural parameter variation, even for large changes in parameters.

(a) GAF, first bending mode

(b) GAF, first torsional mode

(c) GAF, second bending mode

(d) GAF, second torsional mode

## 4.4. Efficiency evaluation of the aeroelastic characteristics evaluation method

Our objective is to propose a new approximate aeroelastic characteristics evaluation method which is suitable for transonic aeroelastic tailoring, so the computational efficiency is one of the most important criteria of the proposed method for assess the aeroelastic stability in aeroelastic tailoring process. All of these simulations are performed on a Windows 7 system PC with Intel⃝R Core(TM) i7-2600 CPU (3.40 GHz, 8 cores, but only one core used) and 16 GB RAM. The computational cost of the direct and proposed approximate aeroelastic characteristics evaluation method for the three case studies is listed in Table 4.

Suppose the application of the direct and the proposed approximate aeroelastic characteristics evaluation method to aeroelastic tailoring process where the structure parameters would change 1000 times, and 20 free stream dynamic pressure values were input for searching the flutter point and the aeroelastic responses at each fixed structural model. The computational cost for the direct evaluation method would be $16 \mathrm{~h~} \times 1000 + 1.78 \mathrm{~s~} \times 20 \times 1000 = 16009.72$ h which is about 667 days. However the computational cost of the proposed approximate aeroelastic characteristics evaluation method is only $16 \mathrm{~h~} \times 1 + 0.74 \mathrm{~s~} \times 1000 + 1.82 \mathrm{~s~} \times 20 \times 1000 = 26.31$ h about which is only little more than one day.

(a) Generalized displacements, first bending mode (left: $V _ {_ {\infty}} = 190 \mathrm{m/s} ,$ right $V _ {_ {\infty}} = 230 \mathrm{m/s} )$

(b) Generalized displacements, first torsional mode (left: $V _ {\infty} = 190$ m/s, right: $V _ {_ {\infty}} = 230 \mathrm{m} / \mathrm{s} )$

(c) Generalized displacements, secod bending mode (left: $V _ {\infty} = 190$ m/s, right $V _ {\infty} = 230$ m/s)

(d) Generalized displacements, second torsional mode $( \mathrm{left} ; V _ {\mathrm {{o o}}} = 190$ m/s, right: $V _ {_ {\mathrm{cs}}} = 230 \mathrm{m} / \mathrm{s} )$

For the three case studies, the direct evaluation method has to reconstruct the new POD/ROM for three times. However, without the most expensive time-consuming reconstruction procedure, the computational cost of the proposed method is reduced obviously, especially after the POD/ROM for original structure was constructed. The demonstration case indicated that the proposed approximate aeroelastic characteristics evaluation method is very computational efficiency, which is very suitable for transonic aeroelastic tailoring with large global structure variation.

(a) Generalized displacements, first bending mode (left $V _ {_ {\infty}} = 230 \mathrm{m/s} ,$ right $V _ {_ {\infty}} = 270 \mathrm{m/s} )$

(b) Generalized displacements, first torsional mode (left $V _ {_ {\infty}} = 230 \mathrm{m} / \mathrm{s} \mathrm{,right} \mathrm{;} V _ {_ {\infty}} = 270 \mathrm{m} / \mathrm{s} \mathrm{)}$

(c) Generalized displacements, second bending mode $( \mathrm{left} ; V _ {\infty} = 230 \mathrm{m} / \mathrm{s} , \mathrm{right} ; V _ {\infty} = 270 \mathrm{m} / \mathrm{s} )$

(d) Generalized displacements, second torsional mode (left $V _ {_ {\infty}} = 230 \mathrm{m} / \mathrm{s} ,$ right: $V _ {_ {\infty}} = 270 \mathrm{m/s} )$

(a) Generalized displacements, first bending mode (left: $V _ {\infty} = 180$ m/s, right: $V _ {_ {\infty}} = 220 \mathrm{m} / \mathrm{s} )$

(b) Generalized displacements, torsional mode (left: $V _ {\mathrm {{s}}} = 180 \mathrm {{m}} / \mathrm {{s}} ,$ right $V _ {_ {\infty}} = 220 \mathrm{m} / \mathrm{s} )$

(c) Generalized displacements, second bending mode (left $V _ {_ {\infty}} = 180 \mathrm{m} / \mathrm{s} ,$ right: $V _ {_ {\infty}} = 220 \mathrm{m} / \mathrm{s} )$

(d) Generalized displacements, second torsional mode (left: $V _ {_ {\infty}} = 180 \mathrm{m/s} ,$ right: $V _ {_ {\infty}} = 220 \mathrm{m} / \mathrm{s} )$

## 5. Conclusions

In aeroelastic tailoring of composite structure, the parameters of composite structure model undergo multiple changes to achieve design goals, and because the standard aeroelastic ROMs including POD/ROMs cannot account for any changes in the aeroelastic system, they are not suitable for aeroelastic tailoring. Extending the existing constructed CFD-based POD/ROM to rapidly evaluate the aeroelastic characteristics of composite structure with global structural parameter variation in aeroelastic tailoring is needed. In this paper a new approximate aeroelastic characteristics evaluation method was proposed to rapidly evaluate the aeroelastic responses corresponding to the global composite structural parameter variation by incorporating the approximate structural dynamic reanalysis algorithm into the standard CFD-based POD/ROM construction procedure.

The feasibility and accuracy of the approximate aeroelastic characteristics evaluation method was demonstrated and evaluated by an improved AGARD 445.6 aeroelastic wing model. Firstly, the accuracy of the POD/ROM solver is validated by using the AGARD 445.6 standard aeroelastic wing model. The accuracy of the extended Kirsch combined structural reanalysis method was also evaluated by using an improved AGARD 445.6 aeroelastic wing model when the composite structures were modified at global level. Then, the accuracy of the proposed method is evaluated by comparing the responses obtained from the direct and approximate aeroelastic characteristics evaluation method in three different cases, including the generalized aerodynamic forces and the generalized displacements in different free steam velocities. The good agreements of the numerical results show that the proposed approximate aeroelastic characteristics evaluation method can capture the aeroelastic characteristics in transonic aeroelastic tailoring when composite structure modifications are made at global level, even for large changes.

One advantage of the proposed approximate aeroelastic characteristics evaluation method is not only to evaluate the aeroelastic characteristics in aeroelastic tailoring with high accuracy, but also to keep down the computational cost. The proposed method provides a potential powerful tool for evaluating aeroelastic characteristics in aeroelastic tailoring in the presence of large changes of the structure.

## Omitted Tables

- [Table 1 omitted; saved to tables/table_001.md]
- [Table 2 omitted; saved to tables/table_002.md]
- [Table 3 omitted; saved to tables/table_003.md]
- [Table 4 omitted; saved to tables/table_004.md]
