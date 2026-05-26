## 1. Introduction

MAVs (miniature fixed-wing unmanned aerial vehicles) have emerged in recent years for a variety of applications [1–4]. Miniature fixed-wing unmanned aerial vehicles (MAVs) require stable and effective path-following control to accomplish the aforementioned tasks. However, navigating the MAVs along a predetermined threedimensional (3D) path in the presence of uncertainty in the underlying modeling parameters and external disturbances poses a significant challenge for the control strategy [5–7]. Due to their size, however, MAVs are more susceptible to environmental disturbances than typical UAVs, despite the fact that both the precise dynamic model of MAVs and the disturbance parameters are difficult to establish [8]. In addition, the available literature addressing the path-following problem focuses primarily on path-tracking performance rather than the characteristics of the involved path, which may not apply to real-world tasks. Therefore, we must research to promote the MAV path following control.

The 3D path following control problem, which is the issue of ensuring that a flying vehicle will track a predetermined route in 3D, was extensively studied by the academic community in the past. The vector-field following-based strategy is a notable type of strategy that can be found alongside other types of strategies. In general, methods in the current vector-field methodology serve as sources of motivation for researchers wishing to improve this strategy, as they have been utilized in the past for a variety of autonomous vehicle types [9–16]. Currently, there are several extensions in some related outstanding works, which are primarily of two types: one focuses on control mechanism and is designed to manage both the effects of disturbances and the system’s inaccurate model, while the other focuses on guidance technique and is designed to adaptively track different types of reference paths in accordance with missions in a more efficient manner.

In control-related fields, researchers attempt to mitigate the effects of both model imprecision and environmental disturbances. Han [17] presented a controller for the active rejection of disturbances (ADRC) based on the extended state observer, which was proved to be applicable to various engineering problems. Thus, ADRC served as motivation for researchers wishing to improve this strategy. Mokhtari [18], Shao [19], and Ma [20] improved Han’s observer-based controller by substituting the extended state observer with a redesigned linear observer. This new observer was then confirmed to work highly successfully in coaxial-rotor UAVs, quadrotor helicopters, and hypersonic reentry vehicles, but not for MAVs. A proportional–integral observer has been utilized in Son [21] and Kim [22] due to its ability to eliminate steady-state errors. According to their findings, a practical control structure using dual firstorder observers was proposed and implemented for robust speed control problems or power electronic applications. Other heuristic algorithms were applied to the tracking control of unmanned vehicles in the research published by Zhu [23]and Edison [24] to account for inherent and environmental disturbances. In [23], a biological neurons-based sliding mode controller was proposed for path-following control of the autonomous underwater vehicle. In [24], the proposed distributed genetic algorithm was implemented in a UAV-involved scenario, but the take-off and landing processes were eliminated. In [25], a method known as the sliding-mode-observer-based equivalent-input-disturbance technique was proposed to enable the quadrotor to fly from an arbitrary starting location to the desired position in a predetermined direction despite the presence of unknown wind disturbances. Concerning the dynamic modeling of quadrotors, Wu et al. [26] intended to develop a precise model and design a robust control law for the quadrotor based on sliding mode control. Adaptive fuzzy logic controllers or sliding mode controllers have been introduced in recent works to combat disturbances due to these intriguing findings. Xu [27] focused on the problems of fixed-time time-varying formation-containment control for multiple underactuated quadrotors, and a controller based on fuzzy logic was presented to combat unknown disturbances. Xiang [28] collaborated with a fuzzy logic controller to develop a line-of-sight guiding system for an unmanned underwater vessel, and a fuzzy adaptive method based on the guidance command and feedback linearization PID controller was designed during the dynamics phase to account for nonlinear dynamics and system uncertainties. Nonetheless, pathfollowing control with disturbances and the system’s inaccurate model methods, particularly when combined with fuzzy logic or sliding mode control to account for disturbances, while relatively effective for quadrotor, vessel, or regular sized $\mathrm{UAV} ,$ have not yet been demonstrated to be effective or practical for small-sized MAVs, which is one of the primary goals of this research.

In guidance-related fields, we can begin by learning from P.B. Sujit’s [29] extraordinary efforts, whose research and investigation demonstrate the advantages of vector-field-based (VF-based) path-following techniques in tracking speed and engineering accessibility, then emphasizing the significance of expanding it to 3D scenarios. Several recent works provide us with a significant opportunity to examine how we handle and employ it in 3D situations involving automobiles. Goncalves [9] proposed a method for calculating artificial VF that enables vehicles to converge to generic curvatures described in n-dimensions. As a result, these VFs can be easily applied to various robot paths following problems. Based on 3D VF and SMC theories, Zhu [10] proposed a spatial route-tracking strategy based on VF-based guidance and a sliding mode controller. However, the path of the stratospheric airship was constrained in the 2D plane. Rezende [15] developed a VF-based method for controlling a fixed-wing UAV to converge on a closed curve in a 3D environment. However, this study did not consider external disturbances and only considered the uncertainty of the dynamic model. Fari [14] proposed an enhanced adaptive VF-based control rule that can account for the absence of wind disturbance information and unmodeled vehicle dynamics. For a robot to traverse a general smooth Riemannian manifold, Yao [16] suggested using a variant of a VF-based guided pathfollowing algorithm. In [17], a composite VF-based guiding technique with smooth bump functions was developed to ensure that a robot follows any suitably smooth 2D path while avoiding obstacles. However, when it comes to VF-based literature, most studies focus on 2D settings, while attempting to manage 3D scenarios with wind disturbances and improve the tracking efficiency of VF-based algorithms, the literature rarely considers the adaptability of the path-following method to the path itself, which limits the algorithm to a single scenario. Consequently, displaying the path’s fundamental cause–effect relationship with the tracking method is an additional solution. The Dubins path is a well-known method for designing routes for mobile robots or aerial vehicles, which was utilized in the work of T. McLain [30] to link this relationship. A modified vector-field method was proposed to drive the Dubins airplane model to follow straight-line and helical paths in a 3D scenario. Still, the wind disturbances were ignored in his work, and the whole flight process, especially the take-off and landing process, known to be the most unstable flight process, was not yet considered.

This study describes an adaptive path-following control approach that compels the MAV to follow a 3D Dubins reference route during a conventional successive reconnaissance and attack mission with wind disturbances. The guidance layer uses a modified VF path-following method to construct a guidance rule that directs the Dubins airplane model to follow SL trajectories, CS trajectories, and helical trajectories, respectively. At the control layer, an adaptive SMC is designed to convert the guidance order into control quantities and provide robustness against inaccurate model parameters and wind disturbances. In addition, the applicability and superiority of the presented method are thoroughly demonstrated by presenting both simulation scenarios and a real-world flying experiment.

This study provides the following contributions:

(1) Path-following control for MAVs with system-modeling inaccuracies and wind interferences are thoroughly evaluated and exploited; solutions of what we refer to as the “multi-layered framework”, in which VF-based guiding and adaptive SMC manage disturbances in the exterior and interior environments, respectively.

(2) Examining the effect of the MAV’s route on the effectiveness of the route following in view of the route planner. Utilizing the 3D Dubins path as the instructional path makes the technique more applicable to engineering.

Following is a summary of the paper’s outline: Section 2 describes the MAV model and problem description. Section 3 illustrates both the modified VF-based route following the algorithm and an adaptive SMC. In Section $^ {4 ,}$ the outcomes of the simulated scenarios and the actual flight experiment are presented, and in Section 5, the conclusions are discussed.

## 2. System model and problem description

## 2.1. System model

Multiple coordinate systems can be used to model aircraft motion, and the correct coordinate system can more accurately depict the aircraft’s motion and simplify the expression form of its motion equation. As can be seen in Table 1, this paper employs a variety of coordinate systems.

As the initial step in resolving the problem of path-following control, this section introduces the kinematic and dynamic models of the MAV as integral system components.

Fig. 1 illustrates a fixed-wing MAV flying with velocity $V _ {u} ,$ angle of heading $\psi ,$ and angle of flight-path $\gamma$ Defining the inertial location of MAV as $[ x ( k ) , y ( k ) , z ( k ) ] ^ {T}$ , the bank angle as $\phi ,$ and the kinematics can be calculated as:

$$\left\{\begin{array} {l l} {\dot {x} = V _ {u} c o s \gamma c o s \psi} \\ {\dot {y} = V _ {u} c o s \gamma s i n \psi} \\ {\dot {z} = - V _ {u} s i n \gamma} \end{array} \right.\tag{1}$$

where $V _ {u}$ is the magnitude of $V _ {u}$

Similar to the coordinated turn requirement stated in [30], the connection between ψ and ϕ may be signified as $\dot {\psi} = g t a n \phi / V _ {u}$

With the assumption of the engaged MAV’s dynamics being sufficiently fast, γ and ϕ are respectively restricted to the command angle $\gamma ^ {c}$ and $\phi ^ {c}$ by a low-level autopilot embedded in the control layer.

Therefore, the MAV’s kinematic model is as follows:

$$\left\{\begin{array} {l l} {\dot {x} = V _ {u} c o s \gamma ^ {c} c o s \psi} \\ {\dot {y} = V _ {u} c o s \gamma ^ {c} s i n \psi} \\ {\dot {z} = - V _ {u} s i n \gamma ^ {c}} \\ {\dot {\psi} = g t a n \phi ^ {c} / V _ {u}} \end{array} \right.\tag{2}$$

However, the attainable bank and flight-path angles should be limited within thresholds $\overline {{\phi}}$ and $\bar {\gamma}$ due to the physical abilities of the MAV. So, the constraints on bank and flight-path angles are $\vert \phi ^ {c} \vert \le \overline {{{\phi}}}$ $| \gamma ^ {c} | \leq \overline {{\gamma}}$ Coincidentally, the kinematic model (Eq. (2)) subjected to the physical ability constraints can be referred to as the Dubins model, proposed initially by Chitsaz [13].

## 2.2. Problem description

This paper examines the problem for scenarios in which a fixed-wing MAV executes sequential operations, including reconnaissance, strike, and verification operations on a known target area. In this scenario, only one vehicle specialty is presented: the combat MAV can perform all three types of missions. In addition to the three sequential operations, the entire flight range should include the take-off and landing processes to reveal the actual scenario.

Fig. 2 depicts the complete flight range of a combat MAV in the given scenario, which includes take-off, operations execution, and landing. During take-off and landing, the MAV is only required to maintain a steady attitude along the corresponding flight path. Different characteristics of the required trajectories for three types of tasks may challenge the robustness of the path-following control mechanism during the operations execution process. Consequently, a comprehensive analysis of the operational execution process’s trajectories will follow.

Fig. 3 illustrates the geometric representation of the involved trajectories generated by a 3D Dubins-based path planner.

Two combat MAVs are tasked with executing on three separate targets, as depicted in Fig. 3. The missions include R, S for the green target, S for the yellow target, and a double attack for the blue target. The trajectory of the combat MAV 2 from position O to point F′ is depicted by a blue line beginning at point O and ending at point F′ . Red and green lines depict the combat MAV 1’s trajectory from point A to point F. The green line represents the path of MAV which conduct a reconnaissance mission on a green-colored target, while the path component DEF represents the path of MAV that conduct a strike mission on a blue-colored target. While it is reasonable for the MAV’s altitude to vary based on the task at hand, it should also lower its altitude when dropping ammunition in the target area to increase its detecting range.

Thus, the ultimate goal of this path-following problem, which is significantly distinct from other works in the literature, is to regulate the path of a MAV so that it converges to a given 3D Dubins path from takeoff to landing.

Fig. 4 depicts a sketch map of the path to be followed. The tracking error is represented as ε $= \left\{x _ {g} , y _ {g} , z _ {g} \right\} ^ {T} , ( x _ {g} , y _ {g} , z _ {g}$ signify the directional, lateral, and altitudinal-track error, respectively). The instructive 3D Dubins trajectory is represented as $P$ (considered to be characterized by a virtual reference point).

The issue of the MAV path following control based on the kinematic model (Eq. (1)) is therefore described as follows: For an instructional 3D

Dubins path P, a guiding principle is expected to guide MAV to track the instructive path in such a way that MAV’s center of mass arithmetically reaches p and its vector of velocity corresponds with P’s tangent vector, then it finally approaches on P(t).

## 3. Methodology

In this section, a multi-layered framework (as depicted in Fig. 5) is developed based on the problem statement and the involved guidance and control problem with disturbances.

The given framework has a guidance layer and a control layer, and there appears to be a close relationship between them. The guidance layer depends on the MAV’s flying condition, and the controller’s capacity can significantly impact the guidance’s performance. Therefore, a robust controller responsible for both disturbances and the subsequent efficiency should be developed for the control layer. A guiding method improves the precision of the tracking pattern at the guidance layer.

Consequently, the next step for this work is to explain the multilayers underlying mechanism. As shown in Fig. $^ {6 ,}$ at the guidance layer, the objective is to transform the instructional route given as $[ x _ {p} , y _ {p} ,$ $z _ {p} ]$ into operational guiding signals as $[ \chi , h _ {d} , \nu _ {a} ]$ , which is achieved by the VF-based guidance algorithm described in the following section. The fundamental requirement of the dynamics layer is to provide a controller to ensure a stable approach of the MAV in the presence of disturbances; as a result, we integrate an adaptive SMC to stem the correct forces and torques on the MAV.

## 3.1. VF-based path following

Typically, the air velocity during a MAV flight is 20% to 30% of its flying speed. This is a significant difference from a conventional airplane. Therefore, a path-following strategy must be developed to combat the wind. In this section, a 3D vector guiding method for addressing the given problem will be presented.

Straight-line following, circle following, and helix following are all examples of 3D Dubins route planner’s instructional trajectory; thus, the path-following algorithm suggested in this section applies the framework described in this section to all three types.

## 3.1.1. Straight-line following

Two vectors can be utilized to represent a straight line:

$$P _ {s} ( \pmb {a} , \pmb {w} ) = \{s = \pmb {a} + \varsigma \pmb {w} \}\tag{3}$$

where a signifies a starting point of $P _ {s} ( \pmb {a} , \pmb {w} )$ , and w signifies the direction of $P _ {s} ( \pmb {a} , \pmb {w} )$

The goal of the VF-based guiding strategy for Eq. (3) is to minimize the lateral error of the path by providing angle heading instruction.

Table 2 illustrates the descriptions of VF-based Straight-line following. The VF-based straight-line route following approach considers two scenarios: $( 1 ) \left| e _ {w y} \right|$ is moderately large; MAV follows the given flight route at angle $\chi ^ {\infty} \in \left( 0 , \pi / 2 \right] ; \left( 2 \right) \left| e _ {w y} \right|$ is in close proximity to $0 ; \chi ^ {\infty}$ is set to be around 0.

## 3.1.2. Arc paths following

In general, an arc route is stated as

$$\mathbf {\psi} _ {P _ {c}} = ( \mathbf {c} , \rho , \lambda ) = \left. r = c + \lambda \rho ( c o s \varphi , s i n \varphi , 0 ) ^ {T} , \varphi \in \left[ 0 , \frac {\pi} {2} \right) \right.\tag{4}$$

where $\pmb {c} = \left( c _ {n} , c _ {e} , c _ {d} \right) ^ {T}$ represent the center of $P _ {c ; \rho}$ is the magnitude of radius, and $\lambda \in \{- 1 , 1 \}$ signifies the direction of rotation of $P _ {c}$

When following $P _ {c} ,$ , it is assumed that the MAV maintains a constant height. Hence the altitude command is set as $h ^ {c} = - ~ c _ {d}$ Table 3 illustrates the descriptions of the VF-based circle path following.

As indicated by Table $^ {3 ,}$ the basic idea behind following $P _ {c}$ is to position d(t) and $\chi ( t )$ so that they are nea $\cdot \rho$ and $\chi ^ {0}$ at the proper times t.

## 3.1.3. Helical paths following

The helical path depicted in Fig. 7 is described by Eq. (5):

$$\left\{\begin{array} {l l} {x ^ {h} ( t ) = \rho _ {h} c o s \gamma _ {h} + x _ {c h}} \\ {y ^ {h} ( t ) = \rho _ {h} s i n \gamma _ {h} + y _ {c h}} \\ {z ^ {h} ( t ) = \mu \gamma _ {h} + z _ {c h}} \end{array} \right.\tag{5}$$

where $\rho _ {h}$ represents the radius of the helical path; $\mu$ signifies the climb rate of the helical path; $[ x _ {c h} , y _ {c h} , z _ {c h} ]$ is the center of the helical path; $[ x ^ {h} ( t ) , y ^ {h} ( t ) , z ^ {h} ( t ) ]$ is the position of a point on the helical path at time t, and $\gamma _ {h}$ is the corresponding flight-path angle.

The helical path depicted in Fig. 7 is given in the NED coordinate system. $S _ {M} = \left[ x _ {m} , y _ {m} , z _ {m} \right]$ represents the current position of the MAV, and $S _ {1} , S _ {2} , S _ {3}$ are three individual points on the helical path; the black circle O is the horizontal projection of helical path, and $S _ {0} , S _ {M 0}$ are the projective points of $S _ {1}$ and $s _ {M}$ on the X-Y plane, respectively. $d _ {\phi}$ is the distance from $S _ {M 0}$ to S0; $d _ {\theta}$ is the shortest vertical distance from MAV to the helical path, and $\xi _ {\phi _ {c}}$ represents the desired yaw angle to convergence to the helical path, $\xi _ {\phi _ {0}}$ is current yaw angle of the MAV.

In the space depicted in Fig. $^ {7 ,}$ vector-fields-based guidance can be described in general terms by a horizontal track heading ϕ and a vertical flight path angle θ. The general guidance equation for helical path can be

Table 2 Descriptions of VF-based straight-line following.

Descriptions of VF-based circle path following.

written as follows:

$$\left\{\begin{array} {l l} {\displaystyle \xi _ {\theta} = \xi _ {\theta} \infty \frac {2} {\pi} a r c t a n 2 ( d _ {\theta} , k _ {h} )} \\ {\displaystyle \xi _ {\phi} = \xi _ {\phi} \infty \frac {2} {\pi} a r c t a n 2 \big ( d _ {\phi} , k _ {h} \big )} \end{array} \right.\tag{6}$$

where $\xi _ {\theta} , \xi _ {\phi}$ are the desired command angles; $\xi ^ {\infty}$ is the predefined angle at infinity, $\xi ^ {\infty} \in \{\pi / 3 , \pi / 2 \} ; d _ {\theta} , d _ {\phi}$ are the distance between the MAV and the desired path in the vertical and horizontal directions, respectively; $k _ {h} ,$ which is similar to $k _ {p a t h}$ and $k _ {c i r c l e} ,$ is a positive constant.

In the scenario depicted in Fig. 7, the helical path is predefined.

Therefore, the MAV must be steered to follow the predefined helical path; thus, the guiding equation for the helical path is reformulated as follows:

$$\left\{\begin{array} {l l} {\theta _ {d} = \xi _ {\theta} \displaystyle {\cfrac {\alpha} {\pi}} \frac {2} {\pi} a r c t a n 2 ( d _ {\theta} , k _ {h} ) + a r c t a n 2 ( \varpi \mu , \rho _ {h} )} \\ {\displaystyle {\phi _ {d} = \xi _ {\phi} \displaystyle {\cfrac {\alpha} {\pi}} \frac {2} {\pi} a r c t a n 2 \big ( d _ {\phi} , k _ {h} \big ) + a r c t a n 2 \big ( y _ {m} - y _ {c h} , x _ {m} - x _ {c h} \big ) - \varpi \pi \gamma / 2}} \end{array} \right.\tag{7}$$

where ϖ denotes the direction of the helical path; when the helix path springs upward $\varpi = 1$ , otherwise, $\varpi = - 1$

## 3.2. Adaptive sliding mode control

In this section, two uncertain conditions—unknown wind field disturbance and UAV model uncertainty—are considered. An adaptive sliding mode control law is proposed for MAV 3D path following uncertain conditions. In the first step, the path following the sliding mode control law is designed with wind disturbance in mind. Considering the model uncertainty, when the nominal value of the MAV autopilot’s parameters deviates from the actual value, the adaptive algorithm is used to estimate the dynamic model parameters in real-time, and the adaptive sliding mode control law is designed for the MAV 3D path following. It is demonstrated that the control law can make the tracking system asymptotically stable globally.

Due to the influence of internal and external disturbances and the physical properties of MAV, the MAV model (autopilot parameters) will be subject to uncertainty, and its nominal value may deviate from its actual value. Using imprecise autopilot parameters in the design of a path-following control law will reduce the tracking precision. Uncertainty conditions encompass the unknown disturbance of the wind field and the model’s uncertainty. Define $\boldsymbol {r} = ( x , y , h ) ^ {T} , \boldsymbol {r} _ {r} = ( x _ {r} , y _ {r} , h _ {r} ) ^ {T}$ as MAV’s current location and the location of a point on the given path, respectively. Consequently, the objective of the controller is to design the control law to converge the MAV tracking error when the MAV has unknown wind field disturbance, and the nominal value of autopilot parameters deviates from the actual value, i.e.:

$$\operatorname* {l i m} _ {t \infty} \Big \| r ( t ) - r _ {r} ( t ) \Big \| = 0\tag{8}$$

## 3.2.1. SMC of path following under wind disturbance

The adaptive control mechanism and SMC are developed to derive the MAV autopilot command. According to Eq. (2), the actual flight velocity of a MAV in the presence of wind disturbance can be calculated as follows:

$$\left\{\begin{array} {l} {{\nu _ {x} = V _ {u} c o s \gamma c o s \psi + \omega _ {x}}} \\ {{\nu _ {y} = V _ {u} c o s \gamma s i n \psi + \omega _ {y}}} \\ {{\nu _ {h} = V _ {u} s i n \gamma + \omega _ {h}}} \end{array} \right.\tag{9}$$

where $\pmb {\nu} = V _ {u} = ( \nu _ {x} , \nu _ {y} , \nu _ {h} ) ^ {T}$ is the velocity of MAV, $\begin{array} {r} {\nu = V _ {u} = \| V _ {u} \| ; \pmb {\omega} =} \end{array}$

$( \omega _ {x} , \omega _ {y} , \omega _ {h} ) ^ {T}$ represents the velocity of wind disturbance. Subsequently, Eqs. (2)–(3) can be reformulated as:

$$\left\{\begin{array} {l l} {\dot {x} = \nu _ {x}} \\ {\dot {y} = \nu _ {y}} \\ {\dot {h} = - \dot {z} = \nu _ {h}} \\ {\dot {v} = \dot {V} _ {u} = ( v ^ {c} - \nu ) \Big / \tau _ {\nu}} \\ {\dot {\gamma} = ( \gamma ^ {c} - \gamma ) / \tau _ {\nu}} \\ {\dot {\psi} = ( \psi ^ {c} - \psi ) / \tau _ {\psi}} \end{array} \right.\tag{10}$$

where $\left( \dot {\nu} , \dot {\gamma} , \dot {\psi} \right) ^ {T}$ represents the variations of $( \nu , \gamma , \psi ) ^ {T} ; \pmb \theta = ( \tau _ {\nu} , \tau _ {\gamma} , \tau _ {\psi} ) ^ {T}$ denotes the actual value of autopilot parameters, and the matched nominal value is represented by $\pmb {\theta} _ {0}$

Le $\boldsymbol {\xi} = \boldsymbol {r} - \boldsymbol {r} _ {r} , \eta = \boldsymbol {\nu} - \dot {\boldsymbol {r}} _ {r} , \mu = \left( \boldsymbol {\nu} , \gamma , \psi \right) ^ {T} , \mu ^ {c} = \left( \boldsymbol {\nu} ^ {c} , \gamma ^ {c} , \psi ^ {c} \right) ^ {T} ( \nu ^ {c} , \gamma ^ {c}$ and ψ c respectively represent the command of speed, angle of flight-path, and angle of bank), then

$$\left\{\begin{array} {l l} {\dot {\pmb {\xi}} = \pmb {\eta}} \\ {\dot {\pmb \eta} = \pmb {T} \pmb {A} ^ {- 1} ( {\pmb \mu} ^ {c} - {\pmb \mu} ) + \dot {\pmb \omega} - \ddot {\pmb r} _ {r}} \end{array} \right.\tag{11}$$

where $A = d i a g ( \tau _ {\nu} , \tau _ {\gamma} , \tau _ {\chi} ) ( ( \tau _ {\nu} , \tau _ {\gamma} , \tau _ {\psi} )$ are the autopilot parameters);

$$\pmb {T} = \left[ \begin{array} {c c c} {c o s \gamma c o s \psi} & {- \nu s i n \gamma c o s \psi} & {- \nu c o s \gamma s i n \psi} \\ {c o s \gamma s i n \psi} & {- \nu s i n \gamma s i n \psi} & {\nu c o s \gamma c o s \psi} \\ {s i n \gamma} & {\nu c o s \gamma} & {0} \end{array} \right]$$

The sliding mode function is defined as:

$${\pmb s} = \dot {\pmb \xi} + {\pmb A} {\pmb \xi}\tag{12}$$

where Λ = diag(λ1, λ2, λ3), λi > 0(i = 1, 2, 3); then

$$\dot {\pmb {s}} = \ddot {\pmb {\xi}} + {\pmb {\Lambda}} \dot {\pmb {\xi}} = \dot {\pmb {\eta}} + {\pmb {\Lambda}} \pmb {\eta}\tag{13}$$

The sliding mode controller is given as:

$$\pmb {\mu} ^ {c} = \pmb {\mu} + \pmb {A} \pmb {T} ^ {- 1} ( \ddot {\pmb {r}} _ {r} - \pmb {A} \pmb {\eta} - \pmb {K} \pmb {s} - D \mathrm{sgn} ( \pmb {s} ) )\tag{14}$$

where $K = d i a g ( k _ {1} , k _ {2} , k _ {3} ) , k _ {i} > 0 ( i = 1 , 2 , 3 )$ is a positive definite diagonal matrix; D is the upper bound of $\| \dot {\omega} \| _ {\infty} ,$ that $\mathbf {i s} , \| \dot {\boldsymbol {\omega}} \| _ {\infty} \leq D$

Theorem 1. The closed-loop system composed of path rr, MAV’s dynamics Eq. (10), and controller Eq. (14) are asymptotically stable.

Proof. For the system with s as the state variable, the Lyapunov candidate function is given as:

$$L _ {1} = \frac {1} {2} \boldsymbol {s} ^ {T} \boldsymbol {s}\tag{15}$$

then

$$\dot {L} _ {1} = s ^ {T} \dot {s} = s ^ {T} ( \dot {\pmb {\eta}} + {\pmb {\cal A}} \pmb {\eta} )\tag{16}$$

According to Eqs. (11) and (14), then

$$\dot {\pmb {\eta}} = \dot {\pmb {\omega}} - \pmb {A} \pmb {\eta} - \pmb {K} \pmb {s} - D \operatorname{sgn} ( \pmb {s} )\tag{17}$$

Eq. (17) is substituted into Eq. (16):

$$\begin{array} {r l} & {\dot {L} _ {1} = s ^ {T} [ \dot {\pmb {\omega}} - \pmb {K} s - D \mathrm{sgn} ( s ) ]} \\ & {\quad = - s ^ {T} \pmb {K} s + s ^ {T} \dot {\pmb {\omega}} - D s ^ {T} \mathrm{sgn} ( s )} \\ & {\quad \le - s ^ {T} \pmb {K} s + \| \pmb {s} \| _ {1} \| \dot {\pmb {\omega}} \| _ {\infty} - D \| s \| _ {1}} \\ & {\quad \le - s ^ {T} \pmb {K} s} \end{array}\tag{18}$$

Holder inequality is utilized in Eq. (18), as $\forall \pmb {a} \in \mathbb {R} ^ {n} \forall \pmb {b} \in \mathbb {R} ^ {n}$ $1 \leq p \leq \infty , 1 / p + 1 / q = 1$ , then a $^ T {\pmb {b}} \leq \| {\pmb {a}} \| _ {p} \| {\pmb {b}} \| _ {q}$

Evidently, L1 is a positive definite function and $\dot {L} _ {1}$ is a negative definite function; Thus, according to Lyapunov stability theorem, the closed-loop system is asymptotically stable. Therefore, when $t \to \infty ,$ then s→○; Based on the sliding mode function given by Eq. (12), then $\dot {\pmb {\xi}} = -$ $\pmb {\varDelta} \xi ,$ thus $\pmb {\xi} = e x p ( - \pmb {\Lambda} t )$ t), and $t \to \infty , \xi \to \infty ,$ , finally, Eq. (8) is obtained.

Theorem 1 describes the path-following control sliding mode control law under wind disturbance conditions. In the following section, we will continue to enhance the MAV path following control law under model uncertainty.

## 3.2.2. SMC of path following under model uncertainty

On the basis of the controller depicted in Section 3.2.1, an adaptive mechanism is designed to derive the adaptive SMC law for the MAV 3D path following under model uncertainty.

When the nominal value $\pmb {\theta} _ {0}$ deviates from the actual value $\theta ,$ it is evident from Eq. (14) that the given sliding mode controller cannot be implemented or can only rely on the nominal value, but the nominal value’s inaccuracy will affect the tracking performance. Consequently, it is essential to estimate the actual value of the autopilot parameter, denoted by $\widehat {\pmb {\theta}} ^ {\prime} = ( \widehat {\tau} _ {\nu} , \widehat {\tau} _ {\gamma} , \widehat {\tau} _ {\psi} ) ^ {T}$

Then, Let

$$\pmb {\Omega} = \pmb {T} ^ {- 1} ( \ddot {r} _ {r} - \pmb {A} \pmb {\eta} - \pmb {K} \pmb {s} - D \operatorname{sgn} ( \pmb {s} ) )\tag{19}$$

Thus, Eq. (14) can be reformulated as:

$$\pmb {\mu} ^ {c} = \pmb {\mu} + \pmb {\Lambda} \pmb {\Omega}\tag{20}$$

Since θ is unknown, the controller can only be given by $\widehat {\pmb {\theta}}$ as follows:

$${\pmb {\mu}} ^ {c} = {\pmb {\mu}} + \widehat {A} \pmb {\Omega}\tag{21}$$

where ${\widehat {\pmb {A}}} \ = d i a g ( {\widehat {\pmb {\theta}}} \ ) ;$

Therefore, the adaptive mechanism is given as follows:

$$\dot {\widehat {\pmb {\theta}}} ^ {\dot {\prime}} = - {\pmb {P}} d i a g ( {\pmb {\Omega}} ) {\pmb {T}} ^ {T} s\tag{22}$$

where $P = d i a g ( p _ {1} , p _ {2} , p _ {3} ) , p _ {i} > 0 ( i = 1 , 2 , 3 )$

Theorem 2. The closed-loop system consisting of the path $r _ {r} ,$ the dynamics of the MAV (Eq. (10)), the controller (Eq. (21)), and the adaptive mechanism (Eq. (22)) is asymptotically stable.

Proof. The Lyapunov candidate function is given as:

$$L _ {2} = L _ {1} + \frac {1} {2} \widetilde {\pmb {\theta}} ^ {T} A ^ {- 1} {\pmb {P}} ^ {- 1} \widetilde {\pmb {\theta}}\tag{23}$$

where $\widetilde {{\pmb \theta}} = {\pmb \theta} - \widehat {\pmb \theta}$

Based on Eqs. (11), (13) and (21),

$$\dot {L} _ {2} = s ^ {T} \Big ( T {\sl A} ^ {- 1} \widehat {\cal A} ~ \pmb {\mathscr {Q}} + \dot {\pmb {\omega}} - \ddot {r} _ {r} + {\cal A} \eta \Big ) + \widetilde {\pmb {\theta}} ^ {T} {\cal A} ^ {- 1} P ^ {- 1} \dot {\widetilde {\pmb {\theta}}}\tag{24}$$

According to Eq. (19),

$$\dot {L} _ {2} = s ^ {T} ( - K s + \dot {\omega} - D s \mathrm{gn} ( s ) ) + \widetilde {\pmb {\theta}} ^ {T} {\cal A} ^ {- 1} {\cal P} ^ {- 1} \dot {\widetilde {\pmb {\theta}}} + s ^ {T} T \Big ( {\cal A} ^ {- 1} \widehat {\pmb {A}} - I \Big ) \Omega$$

Thus,

$$\begin{array} {r l} {\dot {L} _ {2} \leq - s ^ {T} K s + \widetilde {\theta} ^ {T} A ^ {- 1} P ^ {- 1} \dot {\widetilde {\theta}} + s ^ {T} T \Big ( A ^ {- 1} \widehat {A} - I \Big ) \mathcal {Q}} & {\leq - s ^ {T} K s + \widetilde {\theta} ^ {T} A ^ {- 1} P ^ {- 1} \dot {\widetilde {\theta}} + s ^ {T} T d i a g ( \varOmega ) A ^ {- 1} \widetilde {\theta}} \end{array}\tag{25}$$

It is evident from the equation $\widetilde {{\pmb \theta}} = {\pmb \theta} - \widehat {{\pmb \theta}}$ that $\dot {\tilde {\theta}} = - \stackrel {\cdot} {\theta}$ , consequently, $\dot {L} _ {2} \leq - s ^ {T} K s$ . Evidently, $L _ {2}$ is a positive definite function and $\dot {L} _ {2}$ is negative definite function. Therefore, according to Lyapunov stability theorem, the closed-loop system is asymptotically stable. As $\dot {L} _ {2} \leq 0 ,$ then $V _ {2} ( t )$ is bounded, thus, $\begin{array} {r} {\int _ {0} ^ {\infty} \dot {L} _ {2} ( t ) d t = L _ {2} ( 0 ) - L _ {2} ( \infty ) < \infty ;} \end{array}$ consequently, $\begin{array} {r} {\infty \mathrm{~>~-~} \int _ {0} ^ {\infty} \dot {L} _ {2} ( t ) d t = \int _ {0} ^ {\infty} s ^ {T} K s d t \mathrm{\ge~} \lambda _ {k} \int _ {0} ^ {\infty} s ^ {T} s d t} \end{array}$ , where $\lambda _ {k}$ is the minimum eigenvalue of K.

Finally, $\begin{array} {r} {\int _ {0} ^ {\infty} \| s \| _ {2} ^ {2} d t < \infty ,} \end{array}$ , then s ˙ is bounded; from Barbarat lemma, then $l i m _ {t \infty} s = \circ ,$ and Eq. (8) is obtained.

With the controller design procedure outlined in Sections 3.2.1 and 3.2.2, the adaptive sliding mode control law with the guidance data derived from Section 3.1 is obtained under model uncertainty and wind disturbance conditions.

## 4. Performance evaluations and discussions

In this section, two distinct types of test cases are presented. The purpose of these examples is to validate the suggested models and methods in the simulated setting and flight test scenario, respectively. First, a 3D Dubins path with SL segments, AL segments, and helical segments is regarded as the instructive path to trace. Wind disturbance is regarded as the primary factor affecting the adaptability and efficacy of the presented method. In the flight test a flight test is administered to evaluate the method’s applicability in a real-world setting.

## 4.1. Simulation case

The MAV must complete a predetermined mission from take-off to landing in this test. Hence, the instructive path generated by the path planner consists of an ascent path, a cruise path, and a descent path, which correspond to the assembly, reconnaissance, and attack tasks, respectively.

The simulation case parameters are specified in Tables 4 and 5.

The airflow disturbance (AD) is presented as a Dryden [31] model, and the corresponding parameters are presented in Table 5.

The corresponding outcomes are depicted in Figs. 8–12.

In terms of the path planner, the instructive path is depicted in Fig. 8. The multiple 3D Dubins paths consist of a helical ascending path, three cruising paths with varying altitudes, and a descent path to strike the target. Four task switching points are provided to separate these path segments, and the spatial location relationship between the adjacent switching points determines the shape of the path segments.

The actual path with wind disturbance and the instructional path are shown in Figs. 9–12.

From Figs. 9 to 12, it is evident that case 1’s maximum tracking error is $^ {27}$ m, which is less than case 2’s comparable result, which eventually reaches 35 m, demonstrating that the difference is due to varying wind speeds. In addition, velocity and altitude errors are within allowable limits, indicating that the proposed method applies to this test.

(26)

Nonetheless, the following error is directly related to the parameter setting $k _ {o r b i t}$ . Table 6 displays the findings regarding the effects of $k _ {o r b i t}$ on the following error.

Table 6 indicates that as $k _ {o r b i t}$ increases, the tracking error of tests 1 and 2 decreases steadily. However, it is essential to note that $k _ {o r b i t}$ should be constrained to a threshold level.

Despite this, a head-to-head comparison of the efficacy of various commonly available algorithms is conducted. The other prominent algorithms analyzed and compared in this work are the Carrot algorithm, ${\mathrm{NLGL}} ,$ , PLOS-based, and LQR-based algorithms. The ultimate goal is to reasonably validate the feasibility and efficiency of the suggested method. Integral tracking error (Te) is the total tracking error; Tc represents the total control consumption. Finally, Eqs. (27)–(28) presents the performance score for each method involved.

cruising path segment at altitute 400m and attack path segment

$$T c = \sum _ {t = 0} ^ {t = T} u ^ {2} ( t )$$

$$T e = \sum _ {t = 0} ^ {t = T} | d ( t ) |\tag{27}$$

$$\xi = T \overline {{T}} c + ( 1 - T ) \overline {{T}} e\tag{28}$$

where Γ signifies the weight coefficient; ξ represents the performance score; Tc represents the average of Tc; Te signifies the average of Te.

In addition to the method’s performance, the test platform also influences the total score in Eq. (28). As a result, we employ P.C./104 (Fig. 13) as the platform for the tested methods and Real-Time Linux as the operating system.

The results of Monte Carlo simulations are compared to the performance metrics in Eqs. (27) and (28). Wind velocity and direction differ between simulations. The wind blows in a random pattern that can be described as “North Northeast East Southeast South” every thirty seconds. Five hundred simulations with the same settings are executed when evaluating path-following control algorithms. The scores of methods with varying weights Γ are shown in Fig. 14.

As shown in Fig. 14, using an ASMC controller in conjunction with the VF is incredibly advantageous for any weight coefficient. It is quite comparable to ASMC in terms of performance when Γ ranges are between 0.7 and 1, and Carrot, PLOS, and LQR all perform similarly; however, these methods perform very similarly to one another. The performance is ranked as follows when Γ ranges are between 0 and 0.7: VF with ASMC, NLGL, LQR, PLOS, and Carrot; consequently, VF with ASMC is more effective considering both accuracy and efficiency.

## 4.2. Real flight experiment

The purpose of this experiment is to validate the performance and applicability of the proposed adaptive 3D path following the control algorithm in a real-world scenario, and to compare the behavior of the PID-based path following controller, the LQR-based controller, applied to the involved MAV, against the ASMC-based controller, as described in Section 3.2.

To retrieve the experimental data, the experiment is conducted in an outdoor environment with a setup suitable for two MAVs. The test platform is depicted in Fig. 15, and the moment of the test is shown in Fig. 16.

The path planner on the external computer plans the instructive Dubins paths for two MAVs, as shown in Fig. 17.

The hardware we use to measure the distance is GPS, IMU, magnetometer and barometer. The use of several kinds of hardware is selected according to their own characteristics and the adaptability of the flight process. The federated Kalman filtering algorithm is utilized in order to process the measurement data more accurately.

The architecture of the measurement system is shown in Fig. 18:

Table 7 details the three path-following control algorithms’ absolute value of maximum track error in each flight phase under the given environmental conditions.

According to the results shown in Table 7 and Fig. 19, our proposed method only marginally improves the takeoff and landing processes compared to the conventional PID controller. This is because the cruising path consists primarily of straight-line paths with an almost constant altitude, making the flight quite stable and safe. In reality, straight-line characteristics lead to minor errors in the specified cases for all methods.

In the take-off and landing process, the influences induced by the MAV’s unstable and dramatic state change activate the ASMC-based VF and apparently cause the ASMC-based VF to outperform the LQR-based and PID-based path, followed by attaining severe advances. For control accuracy part, remarkably, even the PID-based VF achieves 20 m and 25 m smaller following errors than the LQR-based controller for MAV1 and MAV2, respectively, representing an improvement of approximately 59%. In spite of this, the proposed adaptive SMC-based VF reduces the error to below 7 m by compensating for wind disturbances, unmodeled dynamics, and an unsafe flight period consisting of both an orbit path and a helical path, which are reduced by 68% and 87%, respectively, when compared to PID controller-based VF and LQR-based path following. For control efficiency part, we choose the average transition time of the three controllers in the whole flight process as the factor to evaluate their control efficiency; according the results presented in Table 7, for MAV1 involved case, the average transition time of ASMC controller, LQR controller and PID classic controller is 3.32 s, 10.2 s and 5.71 s respectively, and for MAV2 involved case, the corresponding average transition time is 3.9 s, 9.47 s and 5.31 s, respectively. That is to say, compared with the other two controllers, the ASMC controller has faster response efficiency for path tracking and can adjust the MAV to the scheduled path in a shorter time. Consequently, for a fixed-wing MAV with limited capabilities, the validation of the ASMC-based VF algorithm’s superiority in tracking a 3D Dubins route from take-off to landing process makes it a more viable option.

## 5. Conclusions

This study investigated the path-following control issue for a MAV constrained to a 3D Dubins route with wind disturbance and model uncertainty. This was accomplished by introducing an adaptive sliding model control technique based on a vector-field. The technique was characterized by the incorporation of a multilayered structure to handle the guidance and control levels. In comparison to the previous vectorfield-based guiding legislation, the incorporation of the 3D Dubins route makes it more applicable to real-world situations. Furthermore, both wind disturbances and system uncertainties were explicitly analyzed and managed through the implementation of an adaptive sliding model controller. Simulation results demonstrated that the proposed controller provides effective tracking control. The efficacy and usefulness of this strategy have been demonstrated by a real-world flight test.

It should be noted that the suggested control strategy was developed without considering unknown observer factors. Thus, uncertain observer parameters should be addressed a future work. Future efforts should incorporate collision avoidance in order to meet the prerequisites for complex tasks involving multiple MAVs.

## Omitted Tables

- [Table 1 omitted; saved to tables/table_001.md]
- [Table 2 omitted; saved to tables/table_002.md]
- [Table 3 omitted; saved to tables/table_003.md]
- [Table 4 omitted; saved to tables/table_004.md]
- [Table 5 omitted; saved to tables/table_005.md]
- [Table 6 omitted; saved to tables/table_006.md]
