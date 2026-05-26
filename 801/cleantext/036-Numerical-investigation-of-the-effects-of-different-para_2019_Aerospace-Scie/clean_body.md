## 1. Introduction

With the rapid development of aviation technologies and related disciplines, the modern aircraft design is pursuing long distance flight, high maneuverability and low energy performances [1]. In nature, flying and swimming have been a source of inspiration for new vehicle. Fishes, birds and insects employing flapping wing are much more excellent than existing artificial flight and underwater vehicles. For example, the turning radius of anglerfish is only 6% of its body length [2], while the underwater vehicle has to reduce more than 50% of its speed to decrease the turning radius. The creatures’ amazing ability of flying or swimming inspires a few investigations about flapping wing thrust performance [3–5]. In particularly, the flapping wing benefits from using simple translational motions compared to existing conventional propulsion systems, which not only exhibits superior performance in unsteady flow but also is easier to manufacture. Therefore, a lot of new concepts about bio-inspired vehicle have been investigated [6–8], which will help us to create high performance aircraft in the military and civil engineering fields.

The actual circumstances of birds, insects and fishes employing flapping motion are very complicated, so that experimental observation, theoretical analysis and numerical simulation are all used together to reveal the mechanism of the bionic movement. In the early of 1930s, like-flapping fish swimming has been experimentally observed systematically [9], and later, Lighthill has proposed the large-amplitude slender theory for fishes movement in the theoretical analysis [10]. Theoretical analysis can give quantitative hydrodynamic results by means of simplified approximation and explains the inherent fluid mechanism of like-flapping fish swimming. But the theoretical analysis can only solve the bionic movement with very simple structures and simple movement parameters. Experimental investigation can obtain force and some flow field information to further reveals the nature of the bionic movements and provide basis test data for numerical method. Lin et al. designed a flapping mechanism to simulate the motion of a bird, the thrust and lift were measured employing wind tunnel tests [11]. The experimental visualization of the three-dimensional wake structure of flapping wing was achieved using PIV combined with traditional force measurements [12]. However, experiment research for bionic movement has also some disadvantages, such as poor repeatability, lack of enough detail of the flow field and also very expensive. It still is a great challenge to develop more high-resolution and cheaper experimental techniques. Therefore, how to accurately simulate three-dimensional flapping motion using numerical method becomes one of the key issues to biological and biomimetic flow simulation. Numerical simulations can obtain many flow detail information compared to experimental methods. In recent years, numerical simulations are becoming more and more attractive to investigate the parameter effects on the flow filed structure and thrust performance of pitching and heaving flapping wings. The vortex structure and hydrodynamic performance of a pitching and heaving ellipsoidal flapping was investigated by an Navier–Stokes solver [13]. The aerodynamic characteristics of a flapping wing with different pitching elasticity were calculated by solving unsteady Reynolds-averaged Navier–Stokes equations [14]. An immersed-boundary-method-based incompressible Navier–Stokes equation solver was also used to examine the variations in the wake structures and propulsive performance of a pitching-rolling motion plates over a range of major parameters such as Strouhal numbers, Reynolds numbers, and plate aspect ratios [15]. Three-dimensional instabilities in the wake of a plunging and pitching wing of infinite aspect ratio at low Reynolds number were considered by varying the mean pitch angle and the phase shift by two-dimensional and three-dimensional DNS simulation [16]. The effect of wing mass in the free flight of a two-dimensional flapping wing was numerical investigated by an immersed boundary-lattice Boltzmann method [17]. Dash et al. pointed out flapping wing experiences thrust deterioration when the flapping frequency exceeds a certain critical value basing on N–S method [18], which need choose new angle of attack profiles.

As it can be seen as the above, different parameters have great effects on the thrust performance and the flow structures of rigid flapping wings, such as the flow parameters [15,16], kinematic parameters [19] and geometry parameters [13]. It is well known that changes in geometric parameters under threedimensional effects have a huge impact on the flapping wing. However, it is necessary to overcome the problem of mesh volume and moving boundary using traditional CFD method to solve three-dimensional problems. In the study of many geometric parameters, three-dimensional phenomena are often ignored. In the past research, two-dimensional flapping wings draws much more attentions [20–24]. Many numerical studies are carried out in which the spanwise variability of the geometry and flow field were ignored [25–27], and large aspect-ratio wings were used for focusing on the two-dimensional effect [28,29]. These twodimensional cases given many coarse explanations on the fluid mechanism and hydrodynamics force of flapping wings. For example, a two-dimensional flapping foil will produce reverse Karman vortex street under the appropriate combination of parameters. For the thrust flapping foils, the reverse Karman vortex street in the trailing area will appear when the Strouhal number is between 0.25 and 0.35. The influence of control parameters, such as the angle of attack and the asymmetric pair also have great effects on propulsion performance [30–32]. A large number of experiments and calculations show that three-dimensional vortex structures are far more complex than those of the two-dimensional foils. The vortex topology induced by three-dimensional flapping wings was obviously different from the reverse Karman vortex streets generated from two-dimensional flapping wings [33–35]. By considering the computational time cost, most of the 2D simulations are based on several millions of meshes. In fact, in the two-dimensional approximation, only the cross-flow component of the vorticity is considered. Therefore, the propulsion efficiency is overestimated due to underestimation of wake energy loss. However, for the parameters analysis of the hydrodynamic mechanism for three-dimensional flapping wings, it is very important and useful to capture much more details of the evolution procedure of the unsteady vortex structures in much larger scale simulations. In solving the three-dimensional flapping instability characteristics, the traditional numerical simulation method is used to overcome body-fitted mesh low efficiency and viscous dissipation, and it is urgent to develop on the basis of a large number of grid parallel solving methods.

Different from the traditional CFD method using body-fitted mesh to solve the problem of moving boundary, the immersed boundary method (IBM) which was firstly proposed by Peskin [36], modulates the boundary motion into force rather than the boundary condition. Without the time-consuming mesh update procedure at each time step, the immersed boundary method is especially suitable for solving the unsteady flows with large deformation wings. It has been widely used in the fields of animals swimming, biological valve movement, transportation of fluid particle and swing of filament [37], such as the propulsion performance of two-dimensional fin fish [38]. The deformation of the wing involving the moving boundary can improve the performance of the flapping wing MAV. As an alternative of traditional NS equation, the Lattice Boltzmann Method (LBM) is a mesoscopic simulation technique which takes the transport equation as its govern equation. The LBM solvers have the same numerical accuracy as the NS solver under the unremitting efforts of many scholars, which has become an important tool for simulating complex flow in a broad application prospect [39–42]. Since IBM and LBM both use Cartesian grids, it is interesting to combine the two approaches to simulate complex unsteady flow problems. The IB-LBM method was first introduced by Feng and Michaelides where the restoring force caused by the boundary deformation was obtained by punishment force method [43,44], which has good stability for the unsteady flow problems with large deformation boundary and complex shape geometric boundary. It is widely used in bionic motion simulations [45–47].

In this paper, using Chinese supercomputer TianHe-II presents a wide range of possibilities for the further development of parallel IB-LBM, employing tens of millions grids will help us to obtain more complete and accurate 3D flapping wing flow field information at different geometry parameters. The in evolution procedures of the 3D flapping wing leading edge vortex and wake flow vortex structures were analyzed in detail. Our study explained the 3D flapping wing thrust performance variation with different wing shapes, aspect ratios and pitch-bias angles of attack. This paper is organized as follow: Firstly, the IB-LBM numerical method and solver validation is briefly introduced in Sec. 2; and independence verification is obtained in Sec. 3. our problems description and different parameters on thrust performance was numerical investigated in Sec. 4; and Sec. 5 is conclusion.

## 2. Numerical method and validation

## 2.1. The lattice Boltzmann method

The lattice Boltzmann equation uses a square or cube mesh to discretize the fluid region into a series of grid points. The fluid is seen as a fluid micelle that can only move toward the surrounding grid point or stand still. The lattice Boltzmann equation describing the motion of fluid particles is as follows [48]:

$$\begin{array} {l} {f _ {i} ( \mathbf {x} + \mathbf {e} _ {i} \delta t , t + \delta t ) - f _ {i} ( \mathbf {x} , t )} \\ {\displaystyle = - \frac {1} {\tau} \big [ f _ {i} ( \mathbf {x} , t ) - f _ {i} ^ {e q} ( \mathbf {x} , t ) \big ] + \frac {3} {2} \omega _ {i} \mathbf {f} \cdot \mathbf {e} _ {i} \delta t} \end{array}\tag{1}$$

where $f _ {i}$ is the particle density distribution function, $f _ {i} ^ {e q}$ is the corresponding equilibrium state distribution function, τ is the dimensionless relaxation time, δt is the time step, f is the fluid density, $\mathbf {e} _ {i}$ is the particle velocity, $\omega _ {i}$ is the weight coefficient, ei and $\omega _ {i}$ are related to discrete density model. In this paper, D3Q19 model is chosen.

In D3Q19 model, the velocity is modeled as:

$$\mathbf {e} _ {i} = \left\{\begin{array} {l l} {( 0 , 0 , 0 )} & {i = 0} \\ {( \pm 1 , 0 , 0 ) , ( 0 , \pm 1 , 0 ) , ( 0 , 0 , \pm 1 )} & {i = 1 , 2 , \cdots , 6} \\ {( \pm 1 , \pm 1 , 0 ) , ( 0 , \pm 1 , \pm 1 ) , ( \pm 1 , 0 , \pm 1 )} & {i = 7 , 8 , \cdots , 18} \end{array} \right.\tag{2}$$

The corresponding weighting coefficient is:

$$\omega _ {i} = \left\{\begin{array} {l l} {1 / 3} & {i = 0} \\ {1 / 18} & {i = 1 , 2 , \cdots , 6} \\ {1 / 36} & {i = 7 , 8 , \cdots , 18} \end{array} \right.\tag{3}$$

The equilibrium state distribution function of D3Q19 model is:

$$f _ {i} ^ {e q} = \rho \omega _ {i} \bigg [ 1 + 3 \mathbf {e} _ {i} \cdot \mathbf {u} + \frac {9} {2} ( \mathbf {e} _ {i} \cdot \mathbf {u} ) ^ {2} - \frac {3} {2} \mathbf {u} \cdot \mathbf {u} \bigg ]\tag{4}$$

The relationship between dimensionless relaxation time τ and fluid viscous coefficient υ is:

$$\upsilon = ( 2 \tau - 1 ) / 6\tag{5}$$

The velocity and mass of the fluid at the lattice point can be computed by:

$$\rho = \sum _ {i} f _ {i}\tag{6}$$

$$\mathbf {u} = \frac {\sum _ {i} \mathbf {e} _ {i} f _ {i} + 0.5 \mathbf {f} \delta t} {\rho}\tag{7}$$

The pressure of the fluid at the lattice point can be given as:

$$p = c _ {s} ^ {2} \rho\tag{8}$$

where $c _ {s}$ is the lattice sound velocity, $c _ {s}$ is equal to $1 / \sqrt {3}$ for the D3Q19 model.

## 2.2. The immersed boundary method

The idea of Immersed Boundary Method (IBM) and traditional Computational Fluid Dynamics (CFD) are different in dealing with moving boundary. IBM considered the boundary as internal force in fluid, and then took it into the Navier–Stokes equations or the Boltzmann equation with external force term. Compared to CFD methods using body-fitted meshes IBM does not need to regenerate new mesh at each time step when solving complex moving boundary problems, which greatly improves the computational efficiency. IBM has been applied in the fields of biomimetic motion and filament swing, and has become a research hotspot in computational fluid dynamics.

In order to clearly introduce the concept of IBM, assume that a flexible filament (denoted by Γ ) is immersed in a two-dimensional incompressible viscous fluid (denoted by Ω). The boundary of the flexible filament Γ is denoted by Lagrangian coordinate s, and the fluid area Ω is represented by Euler coordinates x. The coordinates on the flexible filament can be expressed as $\mathbf {x} = \mathbf {X} ( \mathbf {s} , t )$ . The entire systems of the immersed boundary method combined with the incompressible NS equations are listed below [43]:

$$\rho \left( \frac {\partial \mathbf {u}} {\partial t} + \mathbf {u} \cdot \boldsymbol {\nabla} \mathbf {u} \right) = - \boldsymbol {\nabla} p + \mu \boldsymbol {\nabla} ^ {2} \mathbf {u} + \mathbf {f}\tag{9}$$

$$\nabla \cdot \mathbf {u} = \mathbf {0}\tag{10}$$

$$\mathbf {f} ( \mathbf {x} , t ) = \intop _ {T} \mathbf {F} ( \mathbf {s} , t ) \delta {\big (} \mathbf {x} - \mathbf {X} ( \mathbf {s} , t ) {\big )} d \mathbf {s}\tag{11}$$

$$\frac {\partial \mathbf {X}} {\partial t} = \intop _ {\Omega} \mathbf {u} ( \mathbf {x} , t ) \delta \big ( \mathbf {x} - \mathbf {X} ( \mathbf {s} , t ) \big ) d \mathbf {x}\tag{12}$$

where $p$ is fluid pressure, $\rho$ is fluid density, u is fluid viscosity, $\mathbf {F} ( \mathbf {\pmb {s}} , t )$ is concentrated force density at immersed boundary. f(x, t) is fluid force density. δ(x X(s, t)) is the Dirac delta interpolation function.

The three-dimensional Dirac delta interpolation function in equation (12) is as follows [49]:

$$\delta ( r ) = \left\{\begin{array} {l l} {\frac {1} {4} ( 1 + \cos ( \frac {\pi | r |} {2 \Delta x} ) )} & {| r | \leq 2 \Delta x ;} \\ {0 ,} & {| r | \geq 2 \Delta x .} \end{array} \right.\tag{13}$$

## 2.3. The IB-LBM

The concentrated force can be constructed by different methods at a point in IBM, which can be divided into virtual boundary model [50], spring force model [51] and direct force model [52]. All three models can simulate the boundary conditions of the object, but they all have their own scope of application. The virtual boundary model is suitable for processing rigid objects and their active motion. The spring force model and the direct force model are suitable for handling fluid–structure coupled motion. The object of this paper is the numerical simulation of rigid active flapping wing, so the virtual boundary model is chosen. The concentrated force in the virtual boundary model is calculated by:

$$\mathbf {F} ( \mathbf {s} , t ) = \alpha \intop _ {0} ^ {t} [ \mathbf {u} {\big (} \mathbf {X} ( \mathbf {s} , t ) , t _ {1} {\big )} - \mathbf {u} {\big ]} d t _ {1} + \beta {\big [} \mathbf {u} ( \mathbf {X} ( \mathbf {s} , t ) , t {\big ]} - \mathbf {u} {\big ]}\tag{14}$$

where u is the surface velocity of the object. For a given moving object, its speed u(X(s, t), t) can be previously interpolated from the velocity information on the nearby Euler points. The feedback coefficients of α and $\beta$ correspond to speed time integral and speed feedback respectively. For a detailed introduction to the speed correction IB-LBM algorithm, refer to Suzuki’s work [53].

The basic scheme of 3D IB-LBM parallel solver for flapping wing can be linked to calculation process and mathematical formulation through the following Table 1.

## 2.4. Solver validation

To validate the accuracy and reliability of the IB-LBM solver, several cases are tested. The first case is the steady flow around a sphere and the second case is the unsteady flow past a flapping wing. These validation cases have been explained in our previous articles [54]. Moreover, the unsteady flow past of biomimetic wing with IB-LBM has been studied in our previous works [55]. Here, the unsteady flow past a three-dimensional ellipsoidal flapping wing [13] was used to shown and validate the performance of the solver for bionic wings simulation.

Pitching-and-heaving mode has been used widely in the simulation of fish and birds. The center of the wing heaves in the z-direction according to:

$${Z ( t ) = A _ {z} \sin ( 2 \pi f )}\tag{15}$$

At the same time, the wing pitches about its center according to:

$$\theta ( t ) = \alpha _ {0} + A _ {\theta} \sin ( 2 \pi f t + \varphi )\tag{16}$$

(a)

(b)

where $A _ {z}$ and $A _ {\theta}$ represent the heaving and pitching amplitudes respectively and f is the flapping frequency. ϕ is the phase shift between heaving and pitching. α0 is the pitch-bias angle.

The Strouhal number (St) and Reynolds number (Re) are defined as, respectively:

$$S t = 2 A _ {z} f / U _ {\infty} \qquad R e = U _ {\infty} L / \upsilon\tag{17}$$

where Stream speed $U _ {\infty}$ is set as 1, υ is fluid viscous coefficient. The thrust and lift coefficients are defined as, respectively:

$$C _ {T} = {\frac {T} {0.5 \rho U _ {\infty} ^ {2} A ^ {\prime}}} \qquad C _ {L} = {\frac {L} {0.5 \rho U _ {\infty} ^ {2} A ^ {\prime}}}\tag{18}$$

where T is the force in the wing span direction, and L is the force in the heaving direction. $A ^ {\prime}$ denotes twice the area of the ellipsoidal wing.

The calculation parameters of the verification example are shown in Table 2. All of the above parameters are dimensionless in the current study.

As shown in Fig. 1, the asterisk scatter chart shows the result of Dong; the solid line is the calculation result of this article, the numerical results of the thrust and lift coefficients were good agreement with Dong’s who used the finite volume NS equations with immersed boundary method [13]. Therefore, provides a powerful platform for solving the problem of flapping wing unsteady flow mechanism and is broadly applicable to a variety of parameter research.

## 3. Independence validation

To illustrate the independence of the selected mesh and time step, here we consider the pitching-heaving flapping motions of a three-dimensional NACA0012 wing at a constant inflow, the mesh and time step independence are verified in detail. Of course, each of the cases given in this paper is verified in their mesh and time step independence, but it’s not listed because of the paper length.

## 3.1. Mesh independence validation

The pitching-heaving flapping motions of a three-dimensional NACA0012 wing at a constant inflow $U _ {\infty}$ as shown in Fig. 2 (a). The direction of incoming fluid coincides with X axis and Y axis is spanwise direction of the wing. The length of the wing in y direction is 2 and the one in x direction is 1. The maximum thickness of the NACA0012 wing is 0.12. The specific movement mode can be described in equation (15) and (16). The focus of our study is to capture more flow field information using a large number of an overall-grid instead of local hybrid grid. The flow field calculation domain information is given in Fig. 2 (b), whose size is $18 \times 10 \times 10$ . This choice of domain size was based on our experience with running test simulations on a number of different domains. The total mesh of fluid domain is $540 \times 300 \times 300$ , which is 48.6 million. It was treated as nominal grid. The overall grid size for this refined gird is $630 \times 350 \times 350$ which amounts to about 77.1 million grid points. The overall gird size for this roughed gird is $450 \times 250 \times 250$ which amounts to about 28.1 million. The time step dt equals 0.001.

Fig. 3 shows a comparison of key dynamic quantities for the grid independence study carried out for the $S t = 0.6 , \ R e = 200 ,$ $\varphi = \pi / 2$ and $A _ {\theta} = \pi / 6 ~ {\mathsf{case}}$ . To give a clearer explanation of mesh independence, a quantitative analysis was introduced. As shown in

(a)

(b)

(a)

(b)

Table 3, the average thrust coefficient is compared to verify the mesh independence. Compared with nominal mesh, the relative errors between the refined and coarse meshes are about 0.86%, 1.3%, respectively. Meanwhile, it is shown that the lift and thrust force coefficients didn’t obvious change with the number of grid changed by comparing Fig. 3. Fig. 4 shows the comparison of flow field vorticity cloud diagrams under the three grid states. It is shown that nominal grid and finer grid are basically consistent on the vorticity, which indicated the solver has a good convergence in the grid selection. The selected computational domain and the computational grid are justified.

## 3.2. Time independence validation

The same calculation model and kinetic parameters as in the previous section is chosen. To verify the time independence, we use identical normal grid but different time steps is $d t = 0.0005$ $d t = 0.001$ and $d t = 0.0015 ,$ , named as compact time, normal time and loose time respectively. Fig. 5 shows the lift and thrust force coefficients under different time steps. From this figure, it can be seen that lift and thrust force coefficients are extremely similar with qualitative analysis. We also give the average thrust coefficient as a comparison to verify the time independence, as shown in Table 4. The relative error is given, and the independence of time step is further explained from the quantitative point of view. Fig. 6 shows the comparison of flow field vorticity cloud diagrams under the three time steps. We can find that the obtained flow field information is the same as the problem described by the kinetic curve, which is shown that the solver has a good convergence in the time selection.

## 4. Results and discussions

## 4.1. Problem statement

Our focus is on using the parallel solver that has been developed to explore the 3D flapping thrust performance and flow mechanism under different parameters. In this paper, the main parameters we consider include: the wing shape, the aspect ratio and pitch-bias angel of attack. The motion mode of the flapping wing adopts the above described conventional pitching and heaving. After the mesh and time step independence are verified, the same settings as in the previous section verification example are used. According to our experience, the calculation domain size still chooses $18 \times 10 \times 10$ The parameters that need to be changed are given in Table 5. In this paper, we don’t consider the influence of kinematic parameters for the time being, so the other parameters are consistent with Table 3 in the solver verification case.

(a)

(b)

(c)d

(a)

(b)

(b)

(c)

## 4.2. The influence of wing shape on thrust performance

The momentum theorem is usually used to analysis the bionic wing’s performance [48]. As shown in Fig. 7, there are symmetry jets about the x–y plane in the wake regions by giving the one cycle average velocity profile. It’s indicated that the average lift coefficient of is zero, which is also the characteristic that all symmetrical wing should exhibit. The average velocity in the wake zone present a jet shape, which is consistent with the other researchers [56,57] have also shown the jet-like velocity profile is a public characteristics related to the flapping wing movement. The above results further verify that our solver performs well in solving the 3D flapping wing. According to momentum theorem for incompressible flow, thrust can be obtained by the integration of the velocity square distribution along the control surface times density. The computing domain we choose is the same. Because of the velocity magnitudes at the outlet surface for the three cases are very similar, the thrusts are very alike too. The jet region average velocity strength in Fig. 8 (a), (b) and (c) are obviously different. The mean velocity strength distribution of the cuboid wing shown as in Fig. 7 (c) is significantly smaller than those of the other two airfoils. Although the thrust variation between the three is very similar according to the momentum theorem, the thrust of the cuboid wing thrust should be smaller from the velocity strength.

Therefore, we give quantitative analysis from the perspective of the rising resistance coefficient.

Fig. 8 (a) and (b) show the relationship between the lift and thrust coefficients of the above three flapping wings and the f t combination parameters. It can be seen from Fig. 8 (a) that the amplitude of the three case lift coefficients is different. However, they are all symmetric about the x-axis, which lead to the average lift is zero. It is consistent with the expected zero-lift force according to the symmetric average velocity profile shown in Fig. 7. However, the time-related thrust coefficient curve shown in Fig. 8 are asymmetric about the 0 axis, thus the periodic thrust is generated. The average thrust coefficients of the ellipsoidal wing, the NACA0012 wing and the cuboid wing are 0.4809, 0.4587 and 0.1125, respectively. The average thrust coefficient of the ellipsoidal wing is the biggest, followed by NACA0012 wing. The thrust coefficient of the cuboid wing is the smallest which should be related to the sharp leading edge and non-streamlined cross-sectional profile. It can be indicated from this that the obtuse wing has the best thrust performance compared with other sharp wing shapes. The values of the average thrust coefficients are consistent with the strength of the average velocity distribution in the wake regions in Fig. 7. The projection configuration of the NACA0012 wing and cuboid wing are the same rectangular. However, their average thrust coefficients are different and are smaller than that of the ellipsoidal wing. It indicates that the thrust coefficient of the flapping wing with ellipse projection shape is larger than those with rectangular projection shape. It is in fact that most of the plane projection shape of fish body and insect wings are similar to the oval, which shows that biological evolution obeyed some profound natural laws. The NACA0012 wing and the plate wing have the same projection shape, however their thrust coefficients are obvious different. This indicates that the streamlined flapping wings can improve their thrust performance as much as possible. This streamlined wing shape is easier to manufacture than the elliptical wing, under the premise of ensuring similar aerodynamic characteristics, the research on the influence of parameter changes on its thrust performance is more instructive for the design of new actual aircraft. From the above results, we can only obtain the aerodynamic characteristics of different wing shape, and why it is necessary to further analyze from the perspective of vorticity.

(a)

In this paper, the leading edge vortex of different shape flapping wings are compared to reveal the mechanism of force produce. Fig. 9 shows the flapping wing span symmetrical plane vorticity diagram of at entire computational domain. We selected transient clouds at the same position and the same time to compare the differences between the three cases. The flapping motion produces a vortex street with the same jet velocity, but the cuboid wing vortex strength is obviously smaller. In order to explain the influence

(b)

(c)

(a)

(b)

(a)

(b)

(c)

of different wing shapes on the flapping wing thrust performance from the perspective of flow mechanism, the role of the leading edge vortex is discussed. As shown in Fig. 10, the vorticity cloud map is partially enlarged to clearly observe the change of the leading edge vortex. It can be seen from Fig. 10 (a) that the leadingedge vortex V1 of the ellipsoidal wing is closer to the surface than the other wings. The ellipsoidal wing leading edge vortex is not elongated as quickly as the other two cases, and V1 is fuller and stronger. A leading edge vortex that is closer to the flapping wing surface and has stronger vortex strength results in greater thrust. From Fig. 10 (b) and (c), it can be seen that the leading-edge vortex V1 of NACA0012 wing is closer to the wing upper surface than the cuboid wing. The thrust coefficient of NACA0012 wing is also slightly larger than that of the cuboid wing. Therefore, thrust coefficient of the cuboid wing is smallest actually.

These results indicate that the leading edge vortex V1 is an important determinant mechanism of the thrust performance of bionic flapping wings. The blunt leading edge of the cuboid wing ultimately affects the formation of the leading edge vortex, which will determine the average velocity field behind the airfoil. However, the leading edge of cuboid wing and NACA0012 wing are blunt, causing similar vortex and velocity distribution. Their thrust coefficients are also close to each other. In summary, the leading edge shape is one of the factors affecting the thrust magnitude. It suggests that in bionic flapping wing design, the blunt leading edge wing should be avoided in order to obtain a higher propulsion performance. To further explore the flow mechanism of the flapping wing in a motion cycle, Fig. 11 shows the NACA0012 wing vorticity evolution in one cycle at five different moments. When the wing begins to do the pitching and heaving movement (Fig. 11 (a)), the leading edge vortex begins to move across the wing to the trailing edge and meets the vortex shedding in the previous cycle. When the wing is moved up to the intermediate position, the vortex begins to adhere to the lower surface as shown in Fig. 11(b). The strength of the vortex on the wing lower surface is significantly greater than that of wing upper surface vortex, which will help lift the wing. When the wing reaches the highest point as shown in Figure (c), the strength of the vortex on the wing lower surface is significantly reduced, although the vortex attached to the lower surface will affect its movement, it can be seen that the upper surface will produce a stronger vortex is shown in Figure (d). The strength of the vortices on the upper and lower surfaces produced is not the same when the wing is flapping, which will help to generate thrust. From Fig. 11 (d) to (e), the leading edge vortex is always attached to the upper surface during the wing down, resulting in a downward thrust that causes the wing to move downward. As the wing moves downward, the strength of the lower surface vortex becomes smaller, and the upper surface rapidly produces a stronger vortex. The lower surface vortex that hinders the downward movement gradually disappears, which is also the cause of the cyclical change in thrust.

(a)

(b)

(c)

(b) t=18.4s 
(d) t=19.2s

(c) t=18.8s 
(e) t=19.6s

(a) Ellipsoidal wing

(b) NACA0012 wing

(c) Cuboid wing

Furthermore, the wake flow structure can also indicate many flow mechanism of the 3D flapping wing. Fig. 12 shows the vortex structure identified by Q-criterion (Q 0.1) in the wake of the three different shape flapping wings. As can be seen from Fig. 12 (a), the vortex rings of the ellipsoid wing gradually decrease compared to the other wings. However, their shapes keep complete vortex wing when they are evolving downstream. They can induce stronger velocity so the thrust performance of the ellipsoidal wing rank top among the three flapping wings. Fig. 12 (c) shows the vortex rings intertwine and affect each other when they leave the cuboid flapping wing. Then the vortex rings fracture, resulting in a rapid reduction of velocity in the wake of cuboid flapping wing, which leads to the worst thrust performance among the four flapping wing. In order to see this phenomenon more clearly, we draw the same order of vortex structure with red lines in the figure. It can be seen from the figure that, the elliptical wing is similar to the NACA0012 wing vortex structure at the red line position, but the vortex structure of the cuboid wing will begin to rupture, and its induction speed will be weak at the same position. As a result, the horizontal velocity component becomes smaller, and the thrust is of course the smallest of the three. We can also see that the vortex structure of NACA0012 and the vortex structure of the elliptical wing are very similar, which inspires us to choose obtuse leading edge wing shape instead of a circle considering the process difficulty in the actual processing and manufacturing. This is also the reason why people are beginning to pay attention to the NACA0012 flapping wing.

(a) AR=1

(b) AR=2

(c) AR=3

(d) AR=5

(e) AR=7

(a)

(b)

## 4.3. The influence of aspect ratio on thrust performance

In this section, the vortex structures and hydrodynamic coefficients of flapping wings with different aspect ratio were investigated. The geometric model is rectangle wing with NACA0012 wing. The length of the flapping wing along x-axis is constant 1 and the lengths along y-axis are 1, 2, 3, 5 and 7, which means the aspect ratio AR is also 1, 2, 3, 5, 7, respectively. The other computational parameters were as same as those in Table 2. The one-cycle average velocity contour of the five flapping NACA0012 wings with different aspect ratios are shown in Fig. 13. With the variation of the aspect ratio, the average velocity contours also change obviously. With the increase of the aspect ratio, the velocity contours in Fig. 13 (a) and Fig. 13 (b) are similar with bifurcated jets, the bifurcated jets begin to blend as a main jet in Fig. 13 (c), and then the wake jets disappear as shown in Fig. 13 (d) and Fig. 13 (e). The reason for this phenomenon is that the three-dimensional effect is not obvious because of the increase in the aspect ratio. It can be inferred that the thrust in those cases is small. Although the jet structures are similar for the AR1 wing and AR2 wing, the velocity intensity of AR2 wing is stronger than that of AR1 wing. The thrust coefficient of the AR2 wing is expected to be bigger than that of AR1 wing. The thrust is judged by the average velocity. AR2 should generate the maximum thrust because the average velocity in the wake is higher than the other four cases. However, from the average velocity shape, the main jet of AR3 will also affect the magnitude of the thrust. The velocity intensity in both side of the main jet of the AR3 wing is higher than those near the center line. For the AR5 and AR7 wing, the wake flows still appear as a main jet, however the angle and the velocity intensity of the jets are less than that of AR3 flapping wing. However, further quantitative analysis is still necessary to identify the rank of the thrust coefficients.

Fig. 14 gives the hydrodynamic coefficients at different aspect ratios. The average lift coefficients of five wings with different aspect ratios are 0. The average thrust coefficients of five flapping wings with the aspect ratios of 1, 2, 3, 5 and 7 are 0.3426, 0.4587, 0.5098, 0.3852 and 0.1997 respectively. When the aspect ratio changes from 1 to 3, the average thrust coefficient increases. This is consistent with strongest average velocity contour when the aspect ratio is 3. As the aspect ratio changes from 3 to 7, the thrust coefficients decreases. The thrust coefficient quantitative analysis can be found that the average velocity field prediction results are basically consistent with the actual thrust distribution. By comparing the average velocity field distribution, we can find that smaller angle of the jet in wake flow will produce small velocity, which also induces the decreased thrust performance

(a) AR= 1

(b) AR=2

(c) AR=3

(d) AR=5

(e) AR=7

(d) AR=5

(d)AR=7

Furthermore, we analyze the vortex structure of several special circumstances to reveal the mechanism of force produced. Fig. 15 shows the vorticity contours on the wing span symmetry plane of different NACA0012 flapping wings. It is found that when the aspect ratio is 1, the leading-edge vortex is very small and far from the wing surface. As the aspect ratio increases, the shape of the leading edge vortex becomes more and more full and the strength is also enhanced. When the aspect ratio continues to 5 and 7, the strength of the leading edge vortex begins to become smaller, which is also the cause of the thrust change. As for the tailing-edge vortex, the tailing-edge vortex is relatively slender and far away from the AR1 wing. When the aspect ratio is 2, the tailing-edge vortex is approximately similar to the that of AR1 wing. When the aspect ratio continues to 5 and 7, the strength of the tailing-edge vortex produced on the upper surfaces are stronger. In summary, comparing the thrust coefficients, we can find that different aspect ratios will produce different leading edge vortices and trailing-edge vortices. The strength of the vortex is the main factor affecting the thrust generation. The reason why the thrust of the AR3 is the largest is not only because the leading edge vortex is closer to the wing surface wing and the vortex shape is full, but also because of the stronger leading edge vortex and the weaker trailing edge vortex.

Fig. 16 shows the vortex structure identified by Q-criterion when the NACA0012 flapping wings are at the lowest position in their flapping trajectory. It can be seen that the spanning distance of the vortex structure in wing surface is close to the length of the wing. This means that the spanwise length of the vortex structure on the wing surface become larger with the aspect ratio increases. However, the vortices induced by the flapping wings at different aspect ratios are basically the same in the direction of the airflow direction. During the evolution of the vortex ring to the downstream, the span distance is reduced. When the aspect ratio is 1 and 2, the main vortex induced by the wing surfaces is narrow and also the strength is relatively small. Influenced by the leadingedge vortex, the vortex structure becomes vortex wing along the downstream. When the aspect ratio is 3, 5 and 7, the main vortex become longer and longer. Under the same Q value, it can be seen from the fullness of the vortex that the strength of the leading edge vortex is weaker than the strength of the main vortex, which fails enclose of vortex structures. In the downstream wake flow, the vortex takes on intertwined vortex structures. The wingtip vortex will induce disturbed velocity along its normal direction, which makes vortex structure go away from each other. This phenomenon coincides with those in Fig. 19 where the angle of wake vortex decrease as the aspect ratio increases.

(a) α0 =0°

(b) $\alpha _ {0} = 10 ^{\circ}$

(c) $\alpha _ {0} = 20 ^{\circ}$

(c) $\alpha _ {0} = 30 ^{\circ}$

## 4.4. The influence of pitch-bias angle of attack on thrust performance

In the previous cases, the flapping wing pitch-bias angle of attack was assumed to be $0 ^{\circ}$ . In fact, the wing pitch-bias angle of attack was also crucial for the propulsion performance of the 3D flapping wings. In this section, the effects of the pitch-bias angles on hydrodynamic coefficients and vortex structure are investigated for NACA0012 flapping wing. Fig. 17 shows the one-cycle average velocity. It can be seen that with the increase of the pitchbias angle of attack, the average speed of the intensity gradually decreased. According to the momentum theorem, the thrust coefficient will decrease as the angle increase. At the same time, for the angle of attack of $0 ^{\circ}$ , the average velocity is symmetrical about the x–y plane. However, the average velocity contours become non-symmetrical bifurcated jets, which makes the wing produce a certain lift.

It can be seen from Fig. 18 (a) that the lift coefficient curves at four different pitch-bias angles of attack change greatly. The mean lift coefficients for 0◦, 10◦, 20◦, and $30 ^{\circ}$ are $0 , \ - 0.7007 , \ - 1.2762$ −1.6797, respectively. This is consistent with the average velocity distribution in the wake flow as shown in Fig. 17. Fig. 18 (b) shows the thrust coefficient time response. For the pitch-bias angle of $0 ^{\circ}$ and $10 ^{\circ}$ , the forward amplitude is significantly larger than the backward amplitude which lead to the positive thrust force. While for the pitch-bias angle of $20 ^{\circ}$ and $30 ^{\circ}$ , the negative amplitude is larger than their positive counterparts, so the drag force is generated. The average thrust coefficients for each pitch-bias angle can be obtained by averaging the thrust curves in various cases: 0.5098, $0.3714 , \ : - 0.0104 , \ : - 0.5055$ It can be seen that for these flapping wings, the thrust coefficient will decrease or even become to resistance phenomenon with the pitch-bias angle of attack increases.

In order to make the flow mechanism more clearly, the vorticity contours on the symmetry plane of the flapping wings in different pitch-bias angle were presented in Fig. 19. With the increase of the pitch-bias angle of attack, the strength of the leading edge vortex hardly changes much, but the strength of the trailing-edge vortex increases significantly, but the cover distance above the upper wing surface is gradually reduced as shown in Fig. 19 (a) and Fig. 19 (b). Furthermore, with the increase of the pitch-bias angle of attack, the tail vortex is no longer keeping the elongated shape, but gradually moves close to the wing surface. The strength of the trailing edge vortex increases, which leads to the smaller thrust force. The selection of the pitch-bias angle of attack is very important for the bionic flapping wing movement design which has significant effects on the lift and thrust performance.

## 5. Conclusions

The influence of geometrical and motion parameters on the flow mechanism and thrust performance of bionic flapping wing is one of the key issues in the design of wing shape and motion control law for bionic flapping aircraft and underwater vehicles. To capture the flow mechanism and fine vortex structures of three-dimensional complex flapping wings is a time-consuming challenge task, especially for the parameter influence investigations in large-scale calculation. In this paper, a three-dimensional parallel IB-LBM solver suitable for running on TianHe-II Supercomputer was developed and validated.

(a)

(b)

(a) α0 =0°

(c) $\alpha _ {0} = 20 ^{\circ}$

(b) α0 =10 
(d) $\alpha _ {0} = 30 ^{\circ}$

The wing shape, aspect ratio and pitch-bias angle of attack have great influences on the thrust performance of the flapping wings. The numerical results show the ellipsoidal wing has the best thrust performance in the three flapping wings, whose leading-edge vortex is full and close to the wing surface. The vortex structures of NACA0012 wing and ellipsoidal wing are very similar, which causes also the similar thrust performance. The vortex structure of the cuboid wing is small and far from the wing which leads to the worst thrust performance. With the increase of aspect ratio, the average thrust coefficient of NACA0012 flapping wings increases firstly and then decreases. The two-dimensional characteristics of the vorticity distribution is obviously exhibited with the increase of the aspect ratio. It means that for the small aspect ratio flapping wing, its three-dimensional effects in thrust performance must be taking into accounting for. With the pitch-bias angle of attack increases, the thrust coefficient of NACA0012 flapping wing decrease, or even shown resistance phenomenon at the large pitch-bias angel of attack. The evolution procedures of the leading edge vortex and wake flow vortex structures are the possible main reasons which could be used to explain the thrust performance changes with parameter variation of the flapping wing.

In future work, much more fluid parameters such as Reynolds numbers, Strouhal number, and more different motion patterns such as amplitude, frequency, would be further investigated. At the same time, we will further explore the influence of 3D thickness and leading edge curvature on thrust performance. The effect of the structural flexibility is also very important and obvious for true fish, insects and birds. Taking into account for the fluid-structural interaction effects based on IB-LBM method is also expected in next step, although it is a challenge task in large scale simulation.

## Conflict of interest statement

There is no conflict of interest.

## Omitted Tables

- [Table 1 omitted; saved to tables/table_001.md]
- [Table 2 omitted; saved to tables/table_002.md]
- [Table 3 omitted; saved to tables/table_003.md]
- [Table 4 omitted; saved to tables/table_004.md]
- [Table 5 omitted; saved to tables/table_005.md]
