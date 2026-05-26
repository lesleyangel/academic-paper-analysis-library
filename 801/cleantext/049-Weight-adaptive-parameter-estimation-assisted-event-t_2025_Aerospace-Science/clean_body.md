## 1. Introduction

With the retirement of the space shuttle in 2011, winged spacecraft, once highly favored in manned spacefl ight, seemed to have been declared obsolete [1]. However, people believe that as technology continues to advance, winged vehicles will eventually regain their relevance in space transportation [2]. Among the key technologies, reentry guidance is crucial for enhancing reliability, safety, and reducing maintenance costs [3].

Most conventional reentry guidance uses a “trajectory design and tracking guidance” strategy [4]. Glide reentry does not have the same flexible fl ight control capability as a powered cruise vehicle, which makes it necessary to leave enough performance redundancy in the reference trajectory design. In addition, since the reentry dynamics system is an underactuated system, only one to three state variables can be selected for tracking (e.g., drag acceleration, altitude, latitude, and longitude) when performing tracking guidance [5,6]. This results in a wide range of state dispersion during and at the end of the reentry fl ight, which is not conducive to safe landing and reuse of the vehicle.

With the rapid development of embedded computing capabilities, computational guidance and control (CG&C) technology based on complex online computing is gradually replacing traditional guidance methods [7]. Model-based [8,9] and data-based [10-- 13] are two paradigms for achieving computational guidance, and this study will focus on the former. Since various pseudospectral methods [14] have begun to demonstrate excellent performance in solving trajectory optimization problems (TOP), many researchers have been trying to apply them to actual fl ight control [15-- 17] rather than simply using them as an offline fl ight performance evaluation tool. For a long time, the main goal of related research has been to improve the efficiency of trajectory optimization (TO), such as the sequential convex optimization (SCP) method and its many improved versions [17-- 19]. The core idea of the model predictive static programming (MPSP) method proposed by Dwivedi et al. [20] is like that of SCP, and these methods usually use equal distance discretization and the trapezoidal method to approximate the dynamic equation constraints [21-- 23].

To simplify the concept, we will refer to the method of generating guidance commands using online TO solutions as nonlinear model predictive guidance (NMPG), where “nonlinear” means that the TO under consideration is a non-linear programming problem. We cannot expect the NMPG to provide guidance commands in real-time like traditional algorithms, and current research has primarily employed two strategies for generating guidance commands through TO: the uninterrupted NMPG (UI-NMPG) strategy [24], which immediately carries out TO after completing the previous one; and the fi xed cycle NMPG (FC-NPMGP) strategy [25,26], which establishes a longer interval to ensure optimal guidance law generation within that period. However, both strategies have limitations: the former requires substantial computing resources and demands constant high sensitivity from the entire navigation, guidance, and control system, while the latter is constrained by confl icting relationships between guidance cycle duration, TO efficiency, and guidance accuracy.

Given that NMPG is very similar to the concept of model predictive control (MPC) [27] or that NMPG can be regarded as a special application of MPC, we can introduce some advanced concepts from the MPC field into NMPG. Event-triggered model predictive control (ET-MPC) [28] has become a very popular control strategy in recent years, which, unlike the traditional time-triggered, periodic control strategy, executes update commands only when an event occurs, thus avoiding unnecessary complex computations and achieving a good balance between system performance and resource utilization [29,30]. ET-MPC has been applied in fi elds such as autonomous driving [31], orbital control [32] and other fi elds. Zhang et al. [33] proposed an event-triggered model predictive guidance (ET-NMPG) method to achieve optimal ascent guidance of the launch vehicle, which shows better guidance performance and stronger potential for practical application than the traditional iterative guidance and other NMPG strategies.

For reentry guidance problems considering process constraints (such as heat fl ux, dynamic pressure, and overload), the application of NMPGtype approaches is prone to repeated guidance failures. This is due to the inability to update the guidance law in a timely manner, as path and terminal constraints cannot be satisfi ed, even when constraint buff ers are accounted for. These problems can be attributed to the fact that the fl ight state during the unpowered gliding process is not fully controllable; that is, the system is underactuated. In actuality, dealing with process constraints on state variables has always been a significant challenge in the fi eld of guidance and control. One potential solution is to adopt robust model predictive control, which incorporates system uncertainties when formulating the online trajectory optimization problem. However, these robust model predictive control methods are primarily designed for linear time-invariant systems, making them difficult to apply to spacecraft reentry guidance problems. Meanwhile, a winged spaceplane needs to have fl exible windows and reusable features so that the external environment and its inherent characteristics may differ slightly from one mission to another. Hence, to improve the accuracy of the guidance, online model identifi cation is very important. However, most model identifi cation is carried out offline for modeling purposes and cannot be directly used for real-time guidance [34]. Sun et al. [35] proposed a new recursive sequence identifi cation method for aerodynamic model identifi cation of the NASA F-16; Chowdhary et al. [36] compared the performance of three recursive parameter estimation algorithms for aerodynamic parameter estimation of two aircraft from real flight data; Silva et al. [37] proposed to improve spacecraft orbit control effectiveness by introducing online estimation of asteroid parameters. It is indisputable that any model represents a simplifi ed approximation of reality, and our utilization of online model parameter estimation aims to minimize the overall bias inherent in the pre-existing model to the greatest extent possible.

There is no denying that online model identifi cation for hypersonic reentry vehicles is challenging. One of the main difficulties is that realtime fl ight data is limited and noisy, and the aerodynamic model of the reentry vehicle exhibits strong nonlinearity. Direct least-squares estimation often does not reduce the parameter deviation but may yield very unreasonable estimation results. For this reason, we propose a weightadaptive parameter estimation (WAPE) method and embed it into the ET-NMPG framework. Specifically, at the beginning of reentry, openloop guidance is performed based on the pre-obtained optimal guidance command law (hereafter referred to as guidance law). An event trigger is defi ned as the difference between the current guidance law’s reference state and the actual fl ight state. At a certain moment, the NMPG is called upon to update the guidance law and the reference trajectory when an event arises because of dynamic disturbances and model deviations. Additionally, the WAPE is called to estimate the primary parameters of the atmospheric model and aerodynamic model online when an event occurs, there is adequate fl ight historical data, and other required conditions are satisfi ed. The updated model is then used for subsequent NMPGs. Furthermore, we have designed a change point detection step for the case of parameter deviation during the fl ight process (in-fl ight faults), thereby preventing unnecessary parameter estimation and data mixing. The details of the above algorithms will be elaborated upon in the main text.

This paper is organized as follows. The standard reentry motion model, the motion model considering deviations and disturbances, and the reentry guidance problem are provided in Section 2. Section 3 presents the implementation of the ET-NMPG, and details of the WAPE method are given in Section 4. In Section $^ {5 ,}$ the guidance framework proposed in this paper is presented, and a brief introduction and comparison of other related guidance methods (strategies) are also given. Simulation results and analysis are given in Section $^ {6 ,}$ and fi nally, a summary of the work is given in Section 7.

## 2. Problem formulation

We will begin this section by presenting the standard reentry motion equations. The “real” motion equations for guiding simulation, which include dynamic disturbances and modeling deviations, will next be defi ned. Finally, we will outline the reentry guidance problem that is considered in this work, along with some necessary assumptions.

## 2.1. Standard motion equations

Fig. 1 shows the coordinate system used to describe reentry motion, as well as the definitions of the corresponding state variables. The equations of motion for the center of mass of an unpowered vehicle of constant mass are as follows:

$$\begin{array} {r} {\left\{\begin{array} {l l} {\mathrm{d} \Gamma} & {= \nu \sin \eta ,} \\ {\mathrm{d} \Gamma} & {= \nu \cos \eta \sin \psi ,} \\ {\mathrm{d} \eta} & {= \nu \cos \eta \sin \psi} \\ {\mathrm{d} \eta} & {= \nu \cos \eta \sin \psi} \\ {\mathrm{d} \eta} & {= \nu \cos \eta \cos \psi} \\ {\mathrm{d} \eta} & {= - \frac {\eta} {N} ,} \end{array} \right.} \end{array}\tag{1}$$

where ?? is the distance from the center of the Earth, ?? is the longitude, $\phi$ is the latitude, ?? is the relative velocity, $\gamma$ is the fl ight-path angle, $\psi$ is the heading angle, and ?? is the bank angle. $\omega , \mu , R _ {e} ,$ and $M$ are constants, representing the Earth self-rotation rate, the equatorial radius, the geocentric gravitational constant, and the mass of the vehicle, respectively.

The aerodynamic lift and drag, ?? and ?? are given by

$$\left\{\begin{array} {l l} {L = q S _ {r e f} C _ {L}} \\ {D = q S _ {r e f} C _ {D}} \end{array} \right.\tag{2}$$

where $q = \rho v ^ {2} / 2$ is the dynamic pressure, $S _ {r e f}$ is the reference area, and $C _ {L}$ and $C _ {D}$ are the lift coefficient and the drag coefficient, respectively, which are modeled as functions of angle of attack ?? and ?? as follows [38]:

$$\left\{\begin{array} {l} {{C _ {L} = C _ {L 0} + C _ {L 1} \alpha + C _ {L 2} e ^ {C _ {L 3} v}}} \\ {{C _ {D} = C _ {D 0} + C _ {D 1} \alpha ^ {2} + C _ {D 2} e ^ {C _ {D 3} v}}} \end{array} \right.\tag{3}$$

The atmospheric density is modeled as the exponential function $\rho =$ $\rho _ {0} \exp ( H / \beta )$ , where $\rho _ {0}$ is the atmospheric density at sea level, $\beta$ is the scale height, and $H = r - R _ {e}$ is the altitude.

## 2.2. Deviations and disturbances

Simplify Eq. (1) as follows:

$$\dot {{\pmb x}} = f \left( {\pmb x} , {\pmb u} , P _ {b} \right)\tag{4}$$

where $\mathbf {\boldsymbol {x}} = \left[ r , \theta , \phi , v , \gamma , \psi \right] ^ {\top}$ is the fl ight state, $\pmb {u} = [ \alpha , \sigma ] ^ {\top}$ is the control input (i.e., the guidance command), and $P _ {b} = \left[ \rho _ {0} , \beta , C _ {L 0 : 3} , C _ {D 0 : 3} , m \right] ^ {\top}$ represents the main modeling parameter vector (the subscript $\cdot _ {b} ,$ denotes standard values).

In contrast to Eq. (4), real-world motion often includes various dynamic disturbances and deviations of model parameters, i.e.,

$$\dot {\pmb {x}} = f \left( \pmb {x} , \pmb {u} , P _ {t} \right) + \left[ \pmb {0} \atop \pmb {\psi} \right]\tag{5}$$

where $P _ {t}$ represents the true parameters (which only means, of course, better fi tting to the real situation) and $\pmb {\mathcal {Y}} = \left[ \varPsi _ {v} , \varPsi _ {\gamma} , \varPsi _ {\psi} \right] ^ {\intercal}$ represents disturbances corresponding to the three dynamic equations (defi ned by a random process). Due to the inherent modeling inaccuracies and the presence of various uncertain disturbances that are challenging to estimate, for the sake of generalization, we simulate these random processes using the sum of 20 sine waves with different frequencies and phases with a given amplitude $A ,$ that is:

$$\varPsi _ {\vdots} \left( t \right) = \frac {\varxi _ {\vdots} \left( t \right)} {\operatorname* {m a x} \left( \left| \xi _ {:} \left( t \right) \right| \right)} \frac {q \left( t \right)} {\bar {q}} A\tag{6}$$

where

$$\xi _ {:} \left( t \right) = \sum _ {i = 1} ^ {20} \sin \left( 2 \pi f _ {i} t + \varphi _ {i} \right)\tag{7}$$

It should be emphasized that $q \left( t \right) / \bar {q}$ (where ??̄ represents a reference dynamic pressure) is included in Eq. (6) to better fi t the real situation, as disturbances in the reentry process are mostly produced by the aerodynamic force.

## 2.3. Reentry guidance problem

The primary objective of reentry guidance is to guide the spacecraft from the initial state $\mathbf {\boldsymbol {x}} _ {0}$ to the target state $\boldsymbol {x} _ {f}$ by issuing guidance commands and making certain that the path constraints (shown in Eq. (8), where $k _ {Q}$ is a constant.), such as constraints on overload $n ,$ heating rate ??, and dynamic pressure ??, are satisfi ed as much as possible.

$$\left\{\begin{array} {l l} {q = 0.5 \rho v ^ {2} \leqslant q _ {\mathrm{max}}} \\ {Q = k _ {Q} \rho ^ {0.5} v ^ {3.15} \leqslant Q _ {\mathrm{max}}} \\ {n = \displaystyle \frac {\sqrt {L ^ {2} + D ^ {2}}} {m} \leqslant n _ {\mathrm{max}}} \end{array} \right.\tag{8}$$

In traditional reentry guidance, the primary focus is usually on whether the terminal position state $( \mathrm{i.e.,} [ r , \theta , \phi ] )$ reaches the specifi ed value. This is mainly because it is challenging to track velocity states during unpowered reentry. However, more stringent terminal state constraints are crucial for the safety and stability of the entire fl ight mission.

Despite the commonly held perception of GNC as an integrated system, research on guidance techniques often overlooks the other two components. In order to prevent any potential confusion regarding the subsequent research content in this paper, we are operating under the following assumptions:

1. The navigation system is considered accurate enough to ignore the flight state error in its output. In fact, the advanced integrated navigation technology performs very well in hypersonic reentry fl ight [39,40], and its error is far lower than the state deviation threshold considered in this paper.

2. Atmospheric environmental parameters (referring to atmospheric density) are directly measured by airborne equipment [41].

3. The control system can track the guidance commands well and ignore the infl uence of the attitude control process [42].

## 3. The ET-NMPG method

As outlined in the introduction, the core of an NMPG method lies in solving a TOP and utilizing the optimal control solution as the openloop guidance law for subsequent periods. In this section, we fi rst defi ne the reentry TOP under consideration and then provide some tips to enhance the performance of the trajectory optimization solution. Finally, we provide a summary of the complete ET-NMPG process.

## 3.1. Definition of TOP

In this paper, we take minimum trajectory fl uctuation, which is rep-[ ] resented by the integral of $\dot {\gamma} ^ {2}$ over the fl ight time interval $\left[ t _ {0} , t _ {f} \right]$ , as the performance index of the TOP constructed in NMPG. The complete trajectory optimization problem is represented as follows:

$$\begin{array} {r l} & {\mathscr {P} _ {1} : \mathrm{~minimize~} J = \displaystyle \int _ {\imath _ {0}} ^ {\imath _ {f}} \dot {\gamma} ^ {2} \mathrm{d} t} \\ & {\qquad \mathrm{subject~to~} \dot {x} = f \left( x , u , P _ {b} \right)} \\ & {\qquad x \left( t _ {0} \right) = x _ {0} , x \left( t _ {f} \right) = x _ {f}} \\ & {\qquad t _ {0} = 0 , t _ {f} \mathrm{~is~free~}} \\ & {\qquad \mathrm{~Eq.~} ( 8 )} \end{array}\tag{9}$$

Path constraints are always activated at some moments or during specifi c time intervals (otherwise, these constraints would be meaningless). Even if the reference trajectory satisfi es all constraints, the fl ight state may still exceed the boundaries due to disturbances and deviations. An unavoidable problem is that, at a certain moment, when we intend to call NMPG, we may fi nd that the initial state is already outside the path constraint boundaries, which implies that the problem $\mathcal {P} _ {1}$ is infeasible. In general, the inequality constraints in Eq. (8) make it difficult for NMPG to proceed smoothly. To address this, we introduce a buff ered hard constraint to enhance the feasibility of NMPG. Specifically, we introduce a variable $\eta _ {r}$ to limit the upper bound of the ratio between the three path functions and their corresponding maximum values. Additionally, we include a term in the optimization objective with a large penalty factor $K _ {p}$ to minimize the impact of constraint relaxation on the original problem’s solution under normal conditions. Additionally, the velocity plays a crucial role in determining the residual energy of the reentry process. However, it can often be challenging to strictly satisfy the end constraint in direction of velocity due to deviations, so we also relax the terminal heading angle constraints. The modifi ed optimization problem is denoted as $\mathcal {P} _ {2}$ in Eq. (10), where $\pmb {x} _ {e \psi}$ represents the amount of state except $\psi$ . It is important to note that the path constraint in the formula serves as a concise mathematical representation, and it can be readily reformulated for computational resolution of the TOP if necessary.

$$\begin{array} {r l} & {\mathcal {P} _ {2} : \mathrm{~minimize~} J = \displaystyle \int _ {t _ {0}} ^ {t} {\gamma ^ {2} \mathrm{d} t} + K _ {p} \Biggl [ \eta _ {r} + \Biggl ( \frac {\psi \left( {t _ {f}} \right)} {\psi _ {f}} - 1 \Biggr ) ^ {2} \Biggr ]} \\ & {\mathrm{~subject~to~} \dot {x} = f \left( x , u , P _ {b} \right)} \\ & {\qquad x \left( {t _ {0}} \right) = x _ {0} , x _ {e \psi} \left( {t _ {f}} \right) = x _ {e \psi , f}} \\ & {\qquad t _ {0} = 0 , t _ {f} \mathrm{~is~free~}} \\ & {\qquad \eta _ {r} - \operatorname* {m a x} \left\{\frac {Q} {q _ {\operatorname* {m a x}}} , \frac {Q} {Q _ {\operatorname* {m a x}}} , \frac {n} {\eta _ {\operatorname* {m a x}}} \right\} \geqslant 0} \\ & {\qquad q _ {r} \in [ 1 , 1 , 2 ]} \end{array}\tag{10}$$

Remark 1. Even after implementing the deformation of TOP, in numerous scenarios where, for example, the true lift force significantly deviates from that corresponding to the utilized model, the real fl ight trajectory may remain below the optimized trajectory. Consequently, it becomes challenging to identify a trajectory that satisfi es path constraints such as dynamic pressure and heating rate, even when assigning the maximum value for $\eta _ {r}$ . This aspect also underscores the significance of integrating parameter estimation (PE) into ET-NMPG in our research.

## 3.2. Process of ET-NMPG

Denote the solution of problem $\mathcal {P} _ {2}$ as ${\pmb x} ^ {*} \left( t \right)$ and ??∗ (??). In this paper, $\pmb {u} ^ {*} \left( t \right)$ refers to the open-loop guidance law, and ${\pmb x} ^ {*} \left( t \right)$ is the reference trajectory that will be used in ET-NMPG $( \boldsymbol {x} ^ {*} \left( t \right)$ is also denoted as ${\pmb x} _ {r e f} \left( t \right)$ for ease of understanding). Defi ne the state error as follows:

$$\pmb {\varepsilon} _ {x} \left( t \right) : = \left| \pmb {x} \left( t \right) - \pmb {x} _ {r e f} \left( t \right) \right|\tag{11}$$

Then, defi ne the event function ???? as:

$$E T : = \operatorname* {m i n} \left( \sigma - \varepsilon _ {x} \left( t \right) \right)\tag{12}$$

where, the error threshold ?? is a vector of the same size as $x$ . In the ET-NMPG process, $E T \leqslant 0$ serves as the event trigger fl ag. Specifically, when $E T \leqslant 0$ , NMPG is promptly called to update the open-loop guidance law and the reference trajectory. Otherwise, the current guidance law is utilized for open-loop guidance.

## 3.3. Tricks for TO online

## 3.3.1. Mesh refi nement or not

Discrete and transcribed methods play a decisive role in the accuracy of TO results. TO, based on hp Radau pseudospectral discretization, is a relatively advanced method at present. It adopts the idea of piecewise polynomial approximation, which uses the concatenation of several low-order polynomials to approximate the continuous state and control curve to complete the transcription of the original problem. In this discretization scheme, the interval is partitioned into multiple segments (the proportion of each segment is denoted as $k ^ {( i )} ) ,$ , and $\hat {N} _ {d} ^ {( i )}$ Lagrange Gauss-Radau (LGR) points are distributed on each segment. Therefore,{ } a mesh scheme can be represented by the segment scale vector $\left\{k ^ {\left( i \right)} \right\}$ and the discrete points vector $\left\{N _ {d} ^ {( i )} \right\}$

In offline applications, we can start with a rough mesh scheme and continuously improve the mesh quality through the hp-adaptive mesh refi nement algorithm. We call the complete hp-adaptive mesh refi nement trajectory optimization $^ {\mathrm{*}} \mathrm {M R T O ^ {\mathrm{*}}}$ and the simple fi xed-mesh singlestep (meaning no mesh updates) trajectory optimization “FSTO”. To improve the comprehensive performance of NMPG, MRTO is invoked only when the actual initial state differs from the o˙l ine-obtained reference trajectory or the main model parameters change, and FSTO is used in other cases.

## 3.3.2. Mesh scheme and initial value

For both FSTO and MRTO, we can construct a relatively friendly mesh scheme for the current TOP by using mesh truncation and mesh reduction methods based on the previous TO mesh scheme. Specifically, when FSTO needs to be called, by analyzing the relative position of the current fl ight state in the reference trajectory, the excess part in front of the corresponding mesh is deleted, and the segment and the remaining segment are normalized to obtain a new mesh. When it is necessary to call MRTO, the above mesh truncation operation is performed fi rst (it is not necessary if it is the start time of reentry), and then fragment merging and node deletion operations are performed on the constructed mesh to avoid excessive mesh size caused by subsequent mesh refi nement. The concrete implementation of mesh truncation and mesh reduction methods can be referred to in [26] and [33].

Generating an initial guess through interpolation or direct assignment (if only mesh truncation has been performed, most of the relative positions of mesh nodes remain unchanged) is a simple yet highly useful technique for solving TOP. The specifi c implementation method will not be further elaborated on in this paper.

## 3.3.3. State prediction before NMPG

When implementing NMPG, one important consideration is the potential delay in outputting guidance commands due to the time required for solving the TOP. Assuming that the current time is $t _ {s}$ and the NMPG resolution delay is $t _ {d} ,$ the actual fl ight state ${\pmb x} _ {a c t}$ at the time of updating guidance commands $( t _ {s} + t _ {d} )$ is as follows:

$${\pmb x} _ {a c t} \left( t _ {s} + t _ {d} \right) = {\pmb x} \left( t _ {s} \right) + \int _ {t _ {s}} ^ {t _ {s} + t _ {d}} {\left\{{\pmb f} \left( {\pmb x} , {\pmb u} _ {o l d} ^ {*} \left( t \right) , P _ {t} \right) + \left[ \frac {{\bf 0}} {\psi} \right] \right\}} \mathrm{d} t\tag{13}$$

where ${\pmb u} _ {o l d} ^ {*} \left( t \right)$ refers to the previous open-loop guidance law. Note that the state of the optimal trajectory with $\pmb {x} \left( t _ {s} \right)$ as its initial state at time $t _ {s} + t _ {d}$ is:

$${\pmb x} _ {o p t} \left( t _ {s} + t _ {d} \right) = {\pmb x} \left( t _ {s} \right) + \intop _ {t _ {s}} ^ {t _ {s} + t _ {d}} {\pmb f} \left( {\pmb x} , {\pmb u} _ {n e w} ^ {*} \left( t \right) , {\pmb P} _ {b} \right) \mathrm{d} t\tag{14}$$

where $\boldsymbol {u} _ {n e w} ^ {*} ( t )$ refers to the new open-loop guidance law. Upon comparing the two equations, it is evident that, apart from being infl uenced by deviation and perturbation, the disparity in the open-loop guidance law utilized will also lead to a substantial distinction between ${\pmb x} _ {a c t}$ and $\mathbf {\boldsymbol {x}} _ {o p t}$

Consequently, as the new guidance law begins to take effect, $\pmb {\varepsilon} _ {x} \left( t _ {s} + {t _ {d}} \right)$ will have already attained a considerable value, thereby diminishing the alignment between the optimal guidance command and the fl ight state.

For this reason, before NMPG, we make a prediction of the fl ight state by the following calculation, and in the next problem $\mathcal {P} _ {2} , \pmb {x} _ {p r e}$ is taken as the initial state, that is, ${\pmb x} _ {0} = {\pmb x} _ {p r e}$

$${\pmb x} _ {p r e} = {\pmb x} \left( t _ {s} \right) + \int _ {t _ {s}} {{\pmb f} \left( {\pmb x} , {\pmb u} _ {o l d} ^ {*} \left( t \right) , {\pmb P} _ {b} \right)} {\mathrm{d} t}\tag{15}$$

where $t _ {p}$ is the predicted duration, which can be roughly given by the maximum CPU times of the last two historical solutions.

## 4. WAPE and change point detection

Various onboard sensors of the vehicle can measure different types of motion state information and external environmental information. Based on these data, we can estimate the primary modeling parameters mentioned in Section 2 to reduce model deviations. In this paper, we assume that atmospheric density, (angular) acceleration (ignoring the conversion process), and fl ight state data can be obtained at a constant sampling frequency.

## 4.1. PE for atmosphere

We simulate atmospheric density measurement data by adding a 5% random perturbation to an accurate atmospheric density model. The logarithmic form of the atmospheric model, as shown in Eq. (16), can easily make least-squares estimates of the parameters $\rho _ {0}$ and $\beta$

$$\ln \rho = \ln \rho _ {0} - \frac {1} {H _ {s}} H\tag{16}$$

Suppose the ?? sets of altitude and atmospheric density data measured( ) ( ) be $H \left( t _ {1 : m} \right)$ and $\rho \left( t _ {1 : m} \right)$ , then

$$\left[ \begin{array} {l} {- 1 / H _ {s}} \\ {\ln \rho _ {0}} \end{array} \right] = \left( H _ {e} ^ {\top} H _ {e} \right) ^ {- 1} H _ {e} ^ {\top} \rho\tag{17}$$

where

$$\begin{array} {r l} & {H _ {e} = \left[ \begin{array} {c c c c} {H \left( t _ {1} \right)} & {H \left( t _ {2} \right)} & {\cdots} & {H \left( t _ {m} \right)} \\ {1} & {1} & {\cdots} & {1} \end{array} \right] ^ {\intercal} ,} \\ & {\rho = \left[ \rho \left( t _ {1} \right)} & {\rho \left( t _ {2} \right)} & {\cdots} & {\rho \left( t _ {m} \right) \right] ^ {\intercal}} \end{array}$$

Thus the estimates of the parameters $\rho _ {0}$ and $\beta$ can be obtained directly by Eq. (17).

## 4.2. PE for aerodynamics

Denote the part of the main modeling parameters that removes the parameters Rho0 and Beta as:

$$P _ {a e r o} = \left[ C _ {L 0} , C _ {L 1} , C _ {L 2} , C _ {L 3} , C _ {D 0} , C _ {D 1} , C _ {D 2} , C _ {D 3} , m \right] ^ {\top} = \left[ P _ {C _ {L}} , P _ {C _ {D}} , m \right] ^ {\top}\tag{18}$$

The observed (and processed) (angular) acceleration is denoted as $\pmb {f} _ {d} \left( \pmb {x} , \pmb {u} ,\pmb {P} \right) = \left[ f _ {d 1} , f _ {d 2} , f _ {d 3} \right] ^ {\top}$ , and the dynamics portion of motion equations (1) as $\mathbf {} a \left( t \right) = \left[ a _ {1} \left( t \right) , a _ {2} \left( t \right) , a _ {3} \left( t \right) \right] ^ {\intercal}$ . Defi ne the following leastsquares objective function containing ?? sets of measurements:

$$f _ {l s q} \left( P \right) = \sum _ {j = 1} ^ {m} \sum _ {i = 1} ^ {3} \left[ \frac {f _ {d i} \left( \boldsymbol {x} \left( t _ {j} \right) , \boldsymbol {u} \left( t _ {j} \right) , P \right)} {a _ {i} \left( t _ {j} \right)} - 1 \right] ^ {2}\tag{19}$$

Proposition 1. In the reentry problem, the aerodynamic model parameters and the mass cannot be estimated simultaneously, $i . e . ,$ the parameter vector $P _ {a e r o}$ that minimizes the objective function $f _ {l s q}$ is not unique.

Proof 1. Let

$$\begin{array} {r l} & {P _ {a e r o} ^ {*} = \left[ C _ {L 0} ^ {*} , C _ {L 1} ^ {*} , C _ {L 2} ^ {*} , C _ {L 3} ^ {*} , C _ {D 0} ^ {*} , C _ {D 1} ^ {*} , C _ {D 2} ^ {*} , C _ {D 3} ^ {*} , M ^ {*} \right] ^ {\top}} \\ & {\qquad = \left[ P _ {C _ {L}} ^ {*} , P _ {C _ {D}} ^ {*} , M ^ {*} \right] ^ {\top}} \end{array}\tag{20}$$

be a set of optimal solutions, corresponding to an objective function value of $f _ {l s q} ^ {*}$ . For a constant $\kappa > 0 _ {:}$ , let the other set of parameters be

$$\begin{array} {r l} & {\boldsymbol {P} ^ {\prime} = \left[ \kappa C _ {L 0} ^ {*} , \kappa C _ {L 1} ^ {*} , \kappa C _ {L 2} ^ {*} , C _ {L 3} ^ {*} , \kappa C _ {D 0} ^ {*} , \kappa C _ {D 1} ^ {*} , \kappa C _ {D 2} ^ {*} , C _ {D 3} ^ {*} , \kappa M ^ {*} \right] ^ {\intercal}} \\ & {\quad = \left[ P _ {C _ {L}} ^ {\prime} , P _ {C _ {D}} ^ {\prime} , M ^ {\prime} \right] ^ {\intercal}} \end{array}\tag{21}$$

and then the corresponding objective function value is calculated according to Eq. (22), where $a _ {c}$ denotes the portion of the right end term of the kinetic equation that removes the aerodynamic forces.

$$\begin{array} {c l} {\check {E} _ {1} ^ {\prime \prime} ( x ) - \displaystyle \sum _ {j = 1} ^ {3} \frac {\sum _ {k = 1} ^ {5} \Big [ \big ( \epsilon - \Delta \epsilon \big ( \epsilon \big ( \epsilon \cdot \epsilon _ {j} \big ) , \Delta \epsilon ( \epsilon ) , \epsilon _ {j} \big ) , \epsilon _ {j} \big ) \Big ] ^ {2}} {\alpha ( \epsilon , \epsilon _ {j} )} - 1 \Bigg ] ^ {2}} \\ & {= \displaystyle \sum _ {k = 1} ^ {5} \Bigg [ \big ( - \Delta \epsilon \big ( \epsilon - \Delta \epsilon \big ( \epsilon \cdot \epsilon _ {j} \big ) , \big ) \big ) \big ( x ^ {\prime} \big < x ^ {\prime} ( x ) - 1 \Big ) ^ {2} \Bigg ] ^ {2}} \\ & {\displaystyle \sum _ {k = 1} ^ {5} \Bigg [ \big ( x - \big ( \epsilon \cdot \epsilon _ {j} \big ) , \big ) \big / \epsilon \big ( x ^ {\prime} \big < x ^ {\prime} ( x ) - 1 \big ) \int _ {x} ^ {x} \big < \xi ( x ) - 1 \Bigg > ^ {2}} \\ & {\displaystyle \sum _ {k = 1} ^ {5} \Bigg [ \big ( \mathrm{i} x - \big ( \epsilon \cdot \epsilon _ {j} \big ) , \big ) / \Delta \epsilon \big < x ^ {\prime} ( x ) - 1 \Bigg ) ^ {2} \Bigg ] ^ {2}} \\ & {= \displaystyle \sum _ {k = 1} ^ {5} \Bigg [ \big ( - \Delta \epsilon \big ( \epsilon \big ( \epsilon \cdot \epsilon _ {j} \big ) , \big / \Delta \epsilon \big < x ^ {\prime} ( x ) - 1 \big ) \int _ {x} ^ {x} \big < \xi ( x ) - 1 \Big > ^ {2} \Bigg ] ^ {2}} \\ & {\displaystyle - \sum _ {k = 1} ^ {5} \Bigg [ \big ( \mathrm{i} x - \big ( \Delta \epsilon \big ( \epsilon \cdot \epsilon _ {j} \big ) , \big / \Delta \epsilon \big < x ^ {\prime} ( x ) - 1 \big ) \int _ {x} ^ {x} \big < \xi ( x ) - 1 \Big > ^ {2}} \\ & \displaystyle + \sum _ k = \end{array}\tag{22}$$

Remark 2. In fact, since we only have information on acceleration, which is determined by both force and mass, we cannot make an estimate of both the aerodynamic coefficient and the mass of the vehicle.

Proposition 2. The use of a combination of relative aerodynamic parameter ??̂ and $M = 1$ (as defi ned in Eq. (23)) is consistent with a dynamical system represented by a combination of the true aerodynamic parameter ?? and the true mass ?? .

$$\hat {P} = \left[ \frac {C _ {L 0}} {M _ {b}} , \frac {C _ {L 1}} {M _ {b}} , \frac {C _ {L 2}} {M _ {b}} , C _ {L 3} , \frac {C _ {D 0}} {M _ {b}} , \frac {C _ {D 1}} {M _ {b}} , \frac {C _ {D 2}} {M _ {b}} , C _ {D 3} , 1 \right] = \left[ \hat {P} _ {C _ {L}} , \hat {P} _ {C _ {D}} , 1 \right]\tag{23}$$

Proof 2. Based on the definitions of these variables, we can easily get this proposition. (See Eq. (24).)

$$\begin{array} {r l} & {f _ {d} \left( x , u , P \right) = \left[ \begin{array} {c} {\displaystyle {{\frac {D \left( {{P} _ {C}} _ {D} \right)} {M}} + a _ {c 1}}} \\ {\displaystyle {{\cal L} \left( {{P} _ {C}} _ {D} \right)}} \\ {\displaystyle {{\cal L} \left( {{P} _ {C}} _ {L} \right)}} \\ {\displaystyle {{\cal M} \left( {{P} _ {C}} _ {L} \right)}} \end{array} \right]} \\ & {\quad \quad \quad = \left[ \begin{array} {c} {\displaystyle {- D \left( {{P} _ {C}} _ {D} \right) + a _ {c 1}}} \\ {\displaystyle {{\cal L} \left( {{P} _ {C}} _ {L} \right)} \cos \sigma + a _ {c 2}} \\ {\displaystyle {{\cal L} \left( {{P} _ {C}} _ {L} \right) \sin \sigma + a _ {c 3}}} \end{array} \right]} \\ & {\quad \quad \quad = \left[ \begin{array} {c} {\displaystyle {{\cal L} \left( {{P} _ {C}} _ {L} \right)} \cos \sigma + a _ {c 2}} \\ {\displaystyle {{\cal L} \left( {{P} _ {C}} _ {L} \right) \cos \sigma + a _ {c 3}}} \\ {\displaystyle {{\cal L} \left( {{P} _ {C}} _ {L} \right) \sin \sigma + a _ {c 3}}} \end{array} \right] = f _ {d} \left( x , u , \hat {P} \right)} \end{array}\tag{24}$$

Remark 3. This set of relative aerodynamic coefficients can be considered a kind of “aerodynamic acceleration coefficient.” The mass of the vehicle will not be used as a parameter to be estimated but will always be used as a reference value for the motion modeling. In what follows, we will still denote the aerodynamic coefficients as ?? .

When the recorded data is limited, noise significantly impacts aerodynamic coefficient estimation, often leading to substantial deviations between the estimated and true values. Fig. 2 illustrates the $v - \alpha$ relationship for a typical reentry trajectory on a $C _ {D}$ contour map (the $C _ {L}$ case is similar). It can be observed that inadequate sampled data may result in parameter estimation data being nearly parallel to the ?? or ?? axis, thereby posing challenges for relatively accurate coefficient estimation. To address this, we propose the following augmented least squares objective function:

$$\begin{array} {c} {{\displaystyle \hat {f} _ {I s q} \left( P \right) = \sum _ {j = 1} ^ {m} \left\{\displaystyle \sum _ {i = 1} ^ {n} \left[ \displaystyle \frac {f _ {d i} \left( \boldsymbol {x} \left( t _ {j} \right) , \boldsymbol {u} \left( t _ {j} \right) , P \right)} {a _ {i} \left( t _ {j} \right)} - 1 \right] ^ {2} \right.}} \\ {{\displaystyle \left. + \sum _ {k = 1} ^ {8} \left[ \sqrt {\rho _ {I s q}} W _ {P k} \left( \displaystyle \frac {P _ {k}} {\bar {P} _ {k}} - 1 \right) \right] ^ {2} \right\}}} \\ {{\displaystyle = f _ {I s q} \left( P \right) + \frac {m} {2} \rho _ {I s q} \left\| W \left( \displaystyle \frac {P} {\bar {P}} - 1 \right) \right\| _ {2} ^ {2}}} \end{array}\tag{25}$$

The weights corresponding to the amount of data are defi ned as:

$$\begin{array} {l} {\rho _ {l s q} = 10 ^ {- W _ {d a t a}}} \\ {W _ {d a t a} = 0.01 + \frac {1} {0.2 + \exp \left[ - 10 \times \left( \cfrac {m \Delta t} {T _ {r e f}} - 0.5 \right) \right]}} \end{array}\tag{26}$$

where Δ?? is the sampling period and $T _ {r e f}$ is the reference fl ight time. The weight $\rho _ {l s q}$ is used to characterize the extent to which the parameter estimates are allowed to deviate from the baseline values, i.e., the larger the amount of data, the smaller the weight $\rho _ {l s q}$ . The curves of $\rho _ {l s q}$ and $W _ {d a t a}$ versus the amount of data $m \Delta t / T _ {r e f}$ are shown in Fig. 3. The rationale for selecting this weight, featuring a gradual transition at both ends and a rapid shift in the middle, is as follows: when dealing with limited data volume, we aim to avoid a sharp decrease in the penalty for the degree to which the estimate deviates from the reference value, as significant model adjustments may have irreversible implications on subsequent motion; conversely, with ample data collection, we seek to promptly update the model to fully harness the potential of WAPE.

The weight matrix associated with each parameter is defi ned as:

$$\begin{array} {l} {{W = \mathrm{diag} \left( W _ {0} , W _ {\alpha} , W _ {v} , W _ {v} \right)}} \\ {{W _ {0} = \displaystyle \frac {\mu _ {c} \rho _ {l s q}} {S _ {W}} , W _ {\alpha} = \displaystyle \frac {\mu _ {\alpha} \rho _ {l s q}} {S _ {W}} , W _ {v} = \displaystyle \frac {\mu _ {v} \rho _ {l s q}} {S _ {W}}}} \\ {{S _ {W} = \sum \left[ \mu _ {c} , \mu _ {\alpha} , \mu _ {v} \right]}} \\ {{\mu _ {\alpha} = \displaystyle \frac {20} {\operatorname* {m i n} \left( L _ {\alpha} , 20 \right)} , \mu _ {v} = \displaystyle \frac {6000} {\operatorname* {m i n} \left( L _ {v} , 6000 \right)}}} \end{array}\tag{27}$$

where $L _ {\alpha}$ and $L _ {v}$ denote the coverage of angle of attack and velocity in the sampled data (in deg and ${\mathfrak {m}} / {\mathfrak {s}} ,$ respectively). The larger the value, the smaller the corresponding aerodynamic coefficient weights $( W _ {\alpha}$ and $W _ {v} ) _ {:}$ , i.e., the more inclined to believe the least squares estimation results.

Remark 4. Since the models for the lift and drag coefficients are completely independent, the parameter estimation model described above can also be split into two parts for calculation.

## 4.3. Change point detection

In the event of an abrupt alteration in aerodynamic coefficients resulting from a in-fl ight malfunction, continued utilization of all historical data for parameter estimation will invariably yield inaccurate results. Consequently, we have devised a change-point detection procedure to eliminate superfl uous data. Specifically, for ?? sets of sampled data, defi ne the model similarity at each sampling moment as follows:

$$Y _ {P} \left( t _ {j} \right) = \sum _ {i = 1} ^ {3} \left| \frac {f _ {d i} \left( \boldsymbol {x} \left( t _ {j} \right) , \boldsymbol {u} \left( t _ {j} \right) , P \right) - g _ {r e f}} {a _ {i} \left( t _ {j} \right) - g _ {r e f}} - 1 \right| , j = 1 , \cdots , m\tag{28}$$

where ${{g} _ {r e f}}$ represents the gravitational part of the pure inertial dynamics equations, which is calculated based on navigation information.{ }

If the range of the similarity sequence $\left\{\boldsymbol {Y} _ {P} \right\}$ exceeds a predefi ned threshold $S _ {Y}$ , i.e.,

$$\left( Y _ {P} \left( t _ {:} \right) \right) \geqslant S _ {Y}\tag{29}$$

a changepoint is identifi ed within the sampled data, indicating a significant deviation in the vehicle’s primary modeling parameters during this interval.

Subsequently, a changepoint detection algorithm is utilized to pinpoint the location of parameter mutations. The goal of changepoint detection is to ascertain an index ?? that minimizes the following residual function, with the aim of achieving uniform root mean square levels on both sides of the changepoint:

$$\begin{array} {l} {\displaystyle {J = ( k - 1 ) \ln \left( \frac {1} {k - 1} \sum _ {i = 1} ^ {k - 1} Y _ {P} \left( t _ {i} \right) ^ {2} \right)}} \\ {\displaystyle {~ + ( m - k + 1 ) \ln \left( \frac {1} {m - k + 1} \sum _ {i = k} ^ {m} Y _ {P} \left( t _ {i} \right) ^ {2} \right)}} \end{array}\tag{30}$$

The pre-mutation sampling data is discarded, and only the postmutation data is retained, from which least squares parameter estimation is performed.

## 5. The guidance framework

In this section, we provide a comprehensive overview and comparative analysis of the three NMPG strategies: UI-NMPG, FC-NMPG, and ET-NMPG. Subsequently, we delineate the fundamental process of the WAPE-assisted ET-NMPG methodology proposed in this paper. Finally, we enumerate the parameters integral to the guidance algorithm presented herein, accompanied by some relevant considerations.

Fig. 4 illustrates the general fl ow (as shown by the black path in the figure) of reentry guidance using NMPGs, which are centered on continuously updating the open-loop guidance law through online trajectory optimization. The guidance commands at each moment are obtained through interpolation. The distinguishing factor among the different NMPG strategies lies in the mechanism by which NMPG is invoked. For UI-NMPG, the NMPG is invoked uninterruptedly, making the guidance system appear chaotic and extremely taxing on computational resources. Notably, a single guidance simulation using UI-NMPG takes longer than the actual duration of the fl ight, which is highly impractical for algorithm validation. Therefore, we do not simulate this strategy in this paper. For FC-NMPG, the guidance period is artifi cially predetermined, leading to slightly weaker suppression of fl ight state deviations, and the terminal state accuracy is usually insufficient.

We assume in this paper that for all NMPGs, failing to solve the TO and update the guidance law three times in a row is seen as a guidance failure. From then on, simulations are based on the last successful output of the guidance law for the radical calculation.

Remark 5. At the fi rst event trigger, WAPE is not performed if the sampled data are insufficient, meaning the amount of useful data is less than the minimum estimated amount of data $m _ {m i n ^ {\prime}}$

Remark 6. When the amount of data collected during two event triggers is insufficient, performing WAPE will not significantly enhance the accuracy of the estimation results. Moreover, rapid parameter updates can result in insufficiently smooth changes in commands. Therefore, we establish a minimum time interval $t _ {m i n}$ for WAPE.

Table 1 lists all the algorithm parameters used in this paper for WAPE-assisted ET-NMPG simulation.

## 6. Simulation results and discussion

In this section, we compare conventional feedback linearized trajectory tracking guidance (FLG), FC-NMPG, ET-NMPG, and WAPE-assisted ET-NMPG through a typical reentry guidance problem, where the guidance periods of FLG and FC-NMPG are taken to be 0.5 s and 30 s, respectively.

The upper limits of path constraint $q _ {\operatorname* {m a x}} , Q _ {\operatorname* {m a x}}$ , and $n _ {\mathrm{max}}$ are set as 38 kPa, $2500 \mathrm{kW} / \mathrm{m} ^ {2} ;$ , and 3.5, respectively. The initial conditions and terminal state requirements are shown in Table 2, and the deviation ranges of the initial states are also given in the table. The vehicle related parameters and their deviation ranges are given in Table 3. It should be noted that since the focus of this paper is on the guidance algorithm itself, we consider all the above deviations to be uniformly distributed within the set interval. In the later Monte Carlo simulations, we use the Latin hypercube sampling method to obtain different simulation conditions. All the following numerical simulations are implemented in a MATLAB environment on a personal desktop with an AMD Ryzen 7 2.90 GHz processor.

## 6.1. Comparison of different methods

Firstly, we compare FLG and three types of NMPG through two examples: one without considering any deviations or disturbances, and the other with an initial state deviation set to −2007.7 m, 1.8969◦, 1.1312◦, $30.0 \mathrm{m/s} , 0.1827 ^{\circ}$ , and −4.6318◦. Figs. 5 and 6 show the $v - H$ curves and ground tracks of the simulation results. It can be observed that when all conditions and parameters are accurate, both FLG and ET-NMPG can guide the vehicle to the desired terminal state. However, when there is a large initial state deviation, FLG fails to complete the guidance successfully, whereas the three types of NMPG achieve the desired terminal state following very similar fl ight trajectories. In summary, for reference trajectories obtained through trajectory optimization, FLG generally fails to track accurately due to insufficient performance redundancy.

Secondly, we compare the guidance performance of FC-NMPG and ET-NMPG under dynamic disturbances using an example. As depicted in Fig. $^ {7 ,}$ due to the fi xed nature of FC-NMPG’s guidance cycle, a failure to update the guidance commands promptly when the fl ight state is approaching the path constraints may lead to subsequent violations of these constraints, resulting in guidance failure. In contrast, ET-NMPG exhibits superior capability in preventing the fl ight state from exceeding the path constraints.

Finally, we compared ET-NMPG and WAPE-assisted ET-NMPG using an example with an initial state deviation of $[ \ 521.08 \ \mathrm{m} , \ - 2.4474 ^{\circ} ;$ $1.0166 ^{\circ} , ~ 24.85 \mathrm{m/s} , ~ - 0.1932 ^{\circ} , ~ 1.1347 ^{\circ} ~ ] ^ {\intercal}$ , a parameter deviation of [ -0.0059, -0.0485, 0.0008, 4.399 × 10−6, 0.0002, -0.0591, -0.0131, $0.0001 , \ - 74.2935 \mathrm{m} , \ - 0.0008 \ \mathrm{kg} / \mathrm{m} ^ {3} , \ - 30 \mathrm{kg} \ \mathrm{l} ^ {\mathsf{T}}$ , and considering disturbances. The results are shown in Figs. 8 to 10. It can be seen that although ET-NMPG dynamically updates the guidance law based on state deviations, when parameter deviations are significant, the fl ight altitude may consistently remain below the optimized result, ultimately leading to multiple failures in solving the TOP. In the mid-fl ight phase, due to extremely adverse fl ight conditions, solving the TOP becomes challenging, resulting in noticeable abrupt changes in the corresponding guidance command history. With the assistance of WAPE, the fl ight state slightly exceeds the original strict boundaries but remains within the relaxed boundaries. In Figs. 10, we also drawn corresponding lines on the guidance instruction curve chart to represent the 10 time for parameter estimation, from which it can be seen that the event trigger interval is relatively long after the parameters are updated.

Fig. 11 presents the corresponding WAPE output estimates, where the two parameters of the atmospheric density model are very close to the true values after the fi rst estimation, mainly because the corresponding parameter estimation problem is relatively simple. For the aerodynamic coefficient model parameters, $C _ {L 0 , 1}$ and $C _ {D 0 , 1}$ , being the primary infl uencing factors, converge well to the true values after several estimations, while $C _ {L 2 , 3}$ and $C _ {D 2 , 3}$ require more data to be estimated accurately. Fortunately, the impact of $C _ {L 2 , 3}$ and $C _ {D 2 , 3}$ on the model is much lower than that of $C _ {L 0 , 1}$ and $C _ {D 0 , 1} \mathrm {{;}}$ , so even with some deviations in their estimations, the subsequent guidance command solutions are likely to succeed. It should be noted that because the dynamic disturbances do not exhibit zero-mean characteristics, the estimation errors for certain parameters do not strictly decrease as the amount of data increases.

## 6.2. Monte Carlo simulation

We obtained 300 test samples using the Latin Hypercube Sampling, considering initial state deviations, modeling parameter deviations, and disturbances. Fig. 12 compares the terminal position errors of the vehicle in all successful simulations between ET-NMPG and WAPE-assisted ET-NMPG. ET-NMPG succeeded in 134 out of 300 simulations, whereas WAPE-assisted ET-NMPG succeeded in 213 instances. Among these results, WAPE-assisted ET-NMPG shows a more concentrated terminal position distribution.

Table 4 presents the performance statistics of the three NMPGs. ET-NMPG shows a large difference between the maximum and minimum number of guidance cycles $( N _ {g} ) ,$ primarily due to varying degrees of modeling deviations across all samples. In contrast, the $N _ {g}$ for FC-NMPG is almost constant. The introduction of WAPE significantly reduces the guidance frequency for ET-NMPG. The single guidance computation time $( t _ {c} )$ for ET-NMPG is slightly lower than that of FC-NMPG, mainly because the consecutive TOP solutions in ET-NMPG are not significantly different, enhancing the effectiveness of the initial guess and mesh generation mentioned in Section 3. In NMPGs, when model parameter updates are not considered, the successive TOPs only differ in initial states and generally converge more rapidly. However, upon introducing the model update step, each TOP requires a longer time to solve. In fact, the entire parameter estimation process takes only about 5ms, and the increase of $t _ {c}$ shown in Table 4 is primarily due to the deceleration of TO. Although WAPE-assisted ET-NMPG requires more time to update the guidance law, its total simulation time per guidance cycle $( t _ {s} )$ is shorter. Regarding guidance success number $( N _ {s} ) _ {:}$ , FC-NMPG performs the worst, while WAPE-assisted ET-NMPG achieves 69 more successful instances than ET-NMPG.

\* The numbers in parentheses indicate the standard deviation of the corresponding parameters. This will not be repeated later.

\* The data separated by ${{^ \circ}} _ {\gamma}$ in the table represent the maximum value, average absolute value, and minimum value. This will not be repeated later.

Table 5 presents the terminal state error statistics using different methods. WAPE-assisted ET-NMPG performs the best overall, especially in terms of terminal speed deviation, which almost strictly meets the initial constraints except the heading angle. Due to the relaxation of terminal heading angle constraints introduced in the optimization problem, the terminal heading angle errors of the three methods are comparable. Of course, this is to improve the stability of NMPG solution calculation, and it is acceptable. In contrast, FC-NMPG and ET-NMPG exhibit larger errors in terminal speed.

The following provides a statistical analysis of the parameter estimation for the test cases of successful guidance described above. Figs. 13a and 13b illustrate the distribution of relative estimation errors for the four parameters related to the lift coefficient and drag coefficient in different estimation iterations. Among all the simulation results, a maximum of 13 parameter estimations were carried out, but due to a small sample size, the corresponding error distributions are not presented in the fi gures. It can be noted that during the fi rst estimation, the errors for all parameters are usually large. For the parameters $C _ {L 0 , 1}$ and $C _ {D 0 , 1}$ , the relative errors are generally within 20% after two estimations. In combination with the analysis of the specifi c case parameter estimation results above, for $C _ {L 2 , 3}$ and $C _ {D 2 , 3}$ , accurate estimation can only be achieved in the later stages of the fl ight (when data related to lower speeds become available).

Figs. 14a and 14b depict the distribution of the parameter estimation errors and the corresponding estimation times in a time-error coordinate system. It can be observed that the estimation errors for $C _ {L 0 , 1}$ and $C _ {D 0 , 1}$ demonstrate a rapid convergence tendency, while the errors for $C _ {L 2 , 3}$ and $C _ {D 2 , 3}$ remain almost completely random for a considerable period. Considering the substantial enhancement in the guidance success rate after introducing the WAPE, it can be inferred that, even if accurate estimation of $C _ {L 2 , 3}$ and $C _ {D 2 , 3}$ cannot be accomplished during the early or mid-phase of the fl ight, if the other model parameters are corrected within a reasonable range, the guidance commands output by the NMPG can still precisely adjust the fl ight state. This ensures that the path constraints are satisfi ed in most cases, and the problem of insufficient deceleration before reaching the terminal state is unlikely to arise. In conclusion, parameter estimation and updating are effective for reentry guidance. It should be noted that even if accurate estimates of $C _ {L 2 , 3}$ and $C _ {D 2 , 3}$ cannot be obtained, these parameters should not be fi xed to baseline values during parameter estimation, as their values can infl uence the accuracy of the estimation for other parameters.

(a) $\mathrm{For} ~ C _ {L}$

(b) $\mathrm{For} C _ {D}$

(a) For CL

(b) Fr $C _ {D}$

## 6.3. Results with in-fl ight faults

In this section, we examine the performance of WAPE assisted ET-NMPG in mid-course failure scenarios through multiple simulation cases and verify the efficacy of the change point detection method introduced in Section 4.3.

To highlight the key points of this section without affecting the overall trends in the test results, we do not consider deviations in the atmospheric density model parameters and initial state here. Using the Latin Hypercube Sampling method, we obtained eight sets of different parameter deviations and set 4 different mutation time $( t _ {m u t a t i o n} )$ for these deviations (50 s, 500 s, 1000 s, 2000 s), resulting in 32 test samples. Figs. 15 and 16 show the speed-altitude curves and guidance command curves for four sets of guidance simulation results (samples numbered 1, 9, 17, and 25 with the same deviation magnitude, i.e., Group 1). It can be observed that WAPE-assisted ET-NMPG demonstrates excellent guidance performance, with fl ight altitude largely remaining within constraint boundaries and accurately reaching the fi nal position. Overall, the earlier the fault occurs, the smoother the fl ight trajectory and guidance command curves. This is because faults occurring in the early flight phase allow for quicker model updates through WAPE, making it easier for subsequent trajectories to meet constraint conditions, and thus performance indicators representing fl ight smoothness are also better.

Fig. 16 also compares the distribution of parameter estimation moments. It can be observed that the fi rst parameter estimation in each test case occurs after the corresponding $t _ {m u t a t i o n} ,$ , indicating the effectiveness of the mutation detection. In fact, across all 32 simulation test sets, the mutation detection method proposed in this chapter successfully identifies the moment of mutation, with an error of no more than 3 seconds.

Fig. 17 shows the parameter estimation results corresponding to these four sets of simulations. It can be seen that the estimates for $C _ {L 0 , 1}$ and $C _ {D 0 , 1}$ quickly converge to the true values after the abrupt change, while $C _ {L 2 , 3}$ and $C _ {D 2 , 3}$ remain challenging to estimate accurately, similar to the results from the previous section. The 32 sets of simulation test situations mentioned above are statistically analyzed as shown in Table 6. In most cases, the main aerodynamic coefficients are corrected to be close to the real values within 100 seconds after the occurrence of the fault. From the perspective of guidance accuracy, different $t _ {m u t a t i o n}$ hardly affect the average level of terminal state deviation. In addition, for the cases where the parameter mutation occurs earlier, the more event triggers occur in the early stage. However, with the update of parameters, the subsequent guidance solutions will be more efficient. For the cases where the parameter mutation occurs later, although there are fewer guidance solutions in the early stage, due to the relatively larger parameter estimation error in the later stage, event triggers occur more frequently. Therefore, on the whole, there is little difference in the number of guidance solutions and simulation time.

## 7. Conclusions

This paper proposes a WAPE-assisted ET-NMPG method for reentry guidance. Unlike most guidance methods based on online optimization (i.e., NMPG) that use time-triggered strategies, the ET-NMPG with an event-triggered mechanism achieves a better balance between guidance accuracy and computational resource consumption. Building on this, we incorporated a parameter estimation step into the ET-NMPG process to improve model prediction accuracy, thereby further reducing the number of guidance cycles, enhancing guidance precision, and ensuring flight safety. Simulation results demonstrate that WAPE-assisted ET-NMPG offers greater application potential compared to existing methods such as UI-NMPG, FC-NMPG, and ET-NMPG. Further research is warranted to address various sources of deviation in actual fl ight processes and to enhance online parameter estimation using more comprehensive sensor data. In addition, it is important to comprehensively consider the sources and magnitudes of uncertainties based on the actual situation. On this basis, the method for selecting the event-triggered threshold and the potential need for introducing robust NMPG should be explored in more detail.

## CRediT authorship contribution statement

Tengfei Zhang: Writing -- review & editing, Writing -- original draft, Software, Methodology, Data curation, Conceptualization. Licong Zhang: Writing -- review & editing, Software, Methodology. Chunlin Gong: Writing -- review & editing, Methodology, Conceptualization. Songyu Liu: Writing -- review & editing, Methodology. Hua Su: Writing – review & editing, Software, Data curation, Conceptualization.

## Omitted Tables

- [Table 1 omitted; saved to tables/table_001.md]
- [Table 2 omitted; saved to tables/table_002.md]
- [Table 3 omitted; saved to tables/table_003.md]
- [Table 4 omitted; saved to tables/table_004.md]
- [Table 5 omitted; saved to tables/table_005.md]
- [Table 6 omitted; saved to tables/table_006.md]
