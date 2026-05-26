## 1. Introduction

A composite is composed of two or more phases and thus is always designed to have comprehensive advantages of both substrates, and obviously the well-recognized effective physical property is the premise of its applications. In many industry fields, the thermal environment is very harsh and complex, such as the highspeed aircraft, the surface temperature reaches a value of 1600 C [1] and even higher with the increasing speed. To realize an applicable thermal management, the thermal characteristics of relevant composites need to be obtained firstly. The effective properties of composites can be calculated by an appropriate model based on the known properties of each phase. Such a model should contain adequate information of both macro and micro characteristics, like the macroscopic model size and the microscopic geometric structure, and thus needs considerable computational cost. Given that, a representative volume element (RVE) of much smaller size than the macro composite is always selected as the numerical model. The RVE model is always a repetitive unit or an element representative enough in the macroscopic structure. It contains enough microscopic structure information and the more notable appropriate boundary conditions (BCs) to get related to the macroscopic information that has been abandoned in the model establishment. Therefore, an RVE model should contain two essential elements, representative geometric structures and accurate BCs. Certainly, the thermal calculation needs corresponding thermal BCs.

Composite always consists of continuous phase of matrix (ceramic, resin, etc.) and discontinuous phase (reinforcing fiber, particle, porosities, etc.). According to the distribution patterns of discontinuous phase, the composite can be classified as disordered and ordered structures. The RVE model for these two types of composites are entirely different. The short fibrous layers in needled composites [2,3] and proton exchange membrane fuel cell [4,5], porous foam materials [6,7], granular composite [8] and fiber reinforced aerogel composites are typical composites with certain structural randomness. For such composites, the reproduce of the real random multiphase microstructure is the first challenge in RVE model establishment. Wang et al. [5,6,9–11] developed a very efficient ‘‘random generation-growth” method to reconstruct the microstructure based on statistical parameters of the real structures, and the method can take randomness of element size, locations and orientations into account. The reconstructed model is assumed to be representative enough if it has effective structure parameters, i.e. satisfy certain deviation standard, compared with the real composites. In addition, for such multiphase porous structures, lattice Boltzmann method is always a preferred numerical method due to its advantages in dealing with inter-particle interactions and complex BCs [9]. During calculations, isothermal BCs are always imposed on the two boundary surfaces in the calculation direction, and adiabatic or periodic BCs for other four surfaces. This type of boundary treatment is validated by considerable researches in the effective properties predictions, although it is an approximate rather than a precise boundary condition. Hence, for composites with disordered structures, the approximate RVE models and BCs are always adopted, and it is because of the absence of symmetries in these structures. On the other hand, for composites with ordered phase distributions, it is possible to formulate an accurate RVE model and derive precise BCs based on the structure symmetries and such model is expressed as unit cell.

In some composites such as continuous fiber reinforced composites, the discontinuous phase is distributed in a nearly ordered pattern and thus we can have a better control of its effective properties. Take unidirectional (UD) fiber reinforced composite as an instance, fibers always distributed by square or hexagonal pattern in matrix. Textile reinforced composite is another typical orderedstructure composite with extensive applications in aerospace industry [12]. It is fabricated by fiber preform solidifying with specific matrix, in which the preform is created by textile process and possesses certain structure symmetries. There are three types of symmetries in nature, i.e., translation along an axis, reflection about a plane and rotation about an axis. The structure symmetries provide us more convenience in selections of representative unit cell models. Each utilization of symmetries can formulate a new unit cell and certainly new boundaries, which means the size and BCs of unit cells are closely related to symmetries using.

If the structure of such composite is investigated, one can observe countless repetitive units which have translational symmetric relations for certain, and the unit is most likely to be selected as the first unit cell. Such model is called full unit cell (FUC) or can be expressed as UC1 which means the first formulated unit cell for the composite. A FUC is formulated based on translational symmetries, has the largest size compared with other unit cells, and should adopt the widely used so-called periodic BCs. Xia et al. [13] conducted a comprehensive study for unit cell formulations of translational symmetric structures in terms of mechanical study. FUC is also widely used in the thermal property studies for UD composite [14] and textile reinforced composites including two-dimensional woven [15–17], three-dimensional braided [18–21] composites. Sometimes specific composites with disordered structures such as the random porous foam materials [22–25] and particulate composites [8,26] are also assumed to have translational repetitive structures, and corresponding RVE (or FUC) models with idealized configurations are established. It is revealed that the translational symmetries enable us to create a limited size unit cell to represent the infinite structure. In fact, almost all the similar researches will first formulate a FUC regardless of whether it is stated in the papers.

Reflectional and 180 rotational symmetries are also commonly existing in composite structures and the further size-reducing of FUC can be realized based on them. Each utilization of reflectional or rotational symmetry will generate a new unit cell of half size and complicate BCs. However, corresponding studies are very limited. Li et al. [27,28] have made a complete use of structure symmetries in UD and plain woven composites to form unit cells of multi sizes to solve mechanical problems. In the authors’ previous papers [29,30], the effective thermal conductivities of plain woven and three-dimensional four-directional braided composites are calculated by multi-size unit cells formulated based on different symmetries. However, the general rules of unit cell formulations should be further summarized, the thermal-physical mechanism of relevant rules should be clarified, and thus an approach applicable to all composites with symmetric structures can be finally developed.

In this paper, the temperature distribution patterns in symmetric structures under macroscopic thermal stimuli of different directions are demonstrated, two disciplines that can be used in boundary condition derivations are defined and corresponding thermal-physical mechanisms are clarified. Unidirectional fiber reinforced and satin woven composites are studied to demonstrate and validate the developed approach. For UD composite, in the axial direction, a unit cell is formulated by translational symmetries and is used to account for the necessity of derived BCs; while in the transverse direction, all the structure symmetries in fiber distribution patterns are discussed and four relevant unit cells are formulated. For all the multi-harness (4HS, 5HS, 6HS, 7HS, 8HS) satin woven composites, two unit cells are formulated for each and corresponding BCs are derived in a unified form.

## 2. Unit cell formulation rules in thermal calculations

The formulation of unit cells and thermal BCs of several typical textile reinforced composites are studied in the author’s previous work [29,30], however, the general rules and concepts are not yet clarified. In this section, the authors would like to clarify why we need a unit cell, how to formulate a unit cell and how to obtain accurate thermal BCs.

According to Fourier heat conduction law, the constitutive equation of composites is:

$$q _ {x} ^ {o} = - \lambda _ {x x} ^ {o} T _ {x} ^ {o} - \lambda _ {x y} ^ {o} T _ {y} ^ {o} - \lambda _ {x z} ^ {o} T _ {z} ^ {o}\tag{ð1-1Þ}$$

$$q _ {y} ^ {o} = - \lambda _ {y x} ^ {o} T _ {x} ^ {o} - \lambda _ {y y} ^ {o} T _ {y} ^ {o} - \lambda _ {y z} ^ {o} T _ {z} ^ {o}\tag{ð1-2Þ}$$

$$q _ {z} ^ {o} = - \lambda _ {z x} ^ {o} T _ {x} ^ {o} - \lambda _ {z y} ^ {o} T _ {y} ^ {o} - \lambda _ {z z} ^ {o} T _ {z} ^ {o}\tag{ð1-3Þ}$$

where $q _ {i} ^ {0}$ is the macroscopic heat flux, $\lambda _ {i} ^ {0}$ is the effective thermal conductivity, and $\nabla T _ {i} ^ {0}$ is macroscopic the temperature gradient. Compared with the scale of unit cell, the composite can be considered as macroscopic.

## 2.1. Unit cells and thermal boundary conditions

If the effective thermal conductivity in three directions of a composite is about to be experimentally measured, the measuring object should be a specimen with enough structure information. The experimental boundary conditions should be: a given heat flux in the measuring direction and four other adiabatic boundary planes, as shown in Eq. (2). When the experiment reaches a steady state, the macroscopic temperature gradient of the specimen can be measured and the effective thermal conductivities can then be obtained by Eq. (1). If the temperature gradient is given as BCs, then the heat flux is the item that should be measured.

$$q _ {x} ^ {0} = q , q _ {y} ^ {0} = 0 , q _ {z} ^ {0} = 0\tag{ð2-1Þ}$$

$$q _ {x} ^ {0} = 0 , q _ {y} ^ {0} = q , q _ {z} ^ {0} = 0\tag{ð2-2Þ}$$

$$q _ {x} ^ {0} = 0 , q _ {y} ^ {0} = 0 , q _ {z} ^ {0} = q\tag{ð2-3Þ}$$

On the other hand, for the prediction of thermal properties, a numerical model with the above configuration and BCs is definite accurate. The supposed model and BCs can be expressed as UC0 and BC0, respectively, for convenience. However, UC0 has macro size and micro structure information, and thus needs quite considerable computational cost. Hence a representative model with much smaller size and appropriate BCs are required, and the purpose of this paper is to develop an establishment approach of such model based on UC0 and BC0.

Symmetric structure means different parts have a certain symmetric relation: translation along an axis, reflection about a plane or rotation about an axis. As shown in Fig. 1, the structure in the top diagram is composed of countless repetitive units, and take the white unit as an example, when it is translational moved along x- or y-axis by a periodic length (unit length in x or y direction), it will encounter an identical element, hence, based on the translational symmetries along x- and y-axis, the repetitive unit can be selected as UC1 as shown in the middle diagram. For the structure of UC1, when the left part depicted by white dashed lines is 180 rotational transformed about z-axis, it will coincide with the original right part, and thus the left part can be furtherly selected as UC2 as shown in the bottom diagram. For UC2 structure, the left and the right parts are reflectional symmetric to each other about plane X, and thus the left part can be used to formulate UC3. It is clear, unit cells UC1, UC2 and UC3 can be used to represent the original structure UC0 provided that their thermal relations with UC0 are completely and precisely expressed in the boundaries. Therefore, the derivation of thermal BCs of unit cells is then becoming the key to obtain an accurate numerical model. The BCs of UC0, UC1, UC2 and UC3 are expressed as BC0, BC1, BC2 and BC3, respectively. The process of unit cell formulation and BCs derivation is summarized in Fig. 1.

UC0 and BC0 are ideal copies of experimental conditions as discussed above and are definite accurate. UC1 is formulated based on the translational symmetries in UC0 structures, and BC1 is derived based on BC0 and specific temperature distribution disciplines in translational symmetric structures. UC2 is formulated based on the rotational or reflectional symmetries in UC1 structures, and BC2 is derived based on BC1 and certain temperature disciplines in relevant symmetric structures. If further reflectional or rotational symmetries are existing in the structure of UC2, a smaller unit cell UC3 and BC3 can be further formulated and derived, and the process will go on until all the symmetries are identified and utilized. It is revealed in the process that the translational symmetry is used to reduce the computational domain from the infinite dimension to a finite size, while the reflectional and rotational symmetries are used to formulate a unit cell of half size. With the decreasing of the unit cell size, the BCs become more complicated, and the derivation process needs much mathematical and physical considerations. To be summarized, for a unit cell formulation, there are two key steps: the identification of structure symmetries and the derivation of boundary conditions, in which the first step is for the establishment of geometric model while the second one gives the model physical meaning to represent the original structure.

Before the derivation of BCs, temperature distribution disciplines in specific symmetric structures should be illustrated. In the heat conduction problems studied in this paper, the discipline is the temperature relations between corresponding symmetric nodes in symmetric structures. In the next sections, the disciplines under specific macroscopic heat flux (BC0) are defined and discussed for translational, reflectional and rotational symmetric structures, respectively, and the derivation process is further presented by example cases. During the discussions, the macroscopic heat flux is considered as thermal stimulus in a specific direction, for instance, the BCs described in Eq. (2-1) is considered as thermal stimulus in x direction.

## 2.2. Temperature disciplines in translational symmetric structures

Fig. 2 shows a typical translational symmetric structure. An arbitrary node M in structure will be transformed to M0 , M00, $M ^ {\prime \prime \prime}$ . . .after a translation along the x-axis by one, two, three. . . period lengths, respectively. The node O is a reference node, and O0 , O00, $O ^ {\prime \prime \prime}$ . . .are its symmetric nodes, respectively. According to the structure symmetries, the relative temperature relations between M and M0 can be described as:

$${\mathsf{STS}} : ~ T _ {M} - T _ {0} = T _ {M ^ {\prime}} - T _ {0 ^ {\prime}}\tag{ð3Þ}$$

STS is a definition that will be discussed in Section 2.3. Eq. (3) shows a periodic temperature gradients and is the temperature distribution discipline in translational symmetric structures under macroscopic thermal stimuli of any directions. The equation is confirmed by two calculation cases of x and y-thermal stimuli, respectively. The model geometry has 16 units as shown in Fig. 3 to simulate an infinite dimension, the thermal conductivity of the triangle region is 1 W/(m K) while the other region is 10 W/(m K). For the calculation under x-thermal stimulus, the heat flux on the two boundary edges in x-direction is 10 and $- 10 \mathsf{W} / \mathsf{m} ^ {2}$ , respectively, and adiabatic BCs are imposed on other two edges, as shown in Eq. (2-1). The case with y-thermal stimulus has opposite conditions, as shown in Eq. (2-2).

Fig. 3(a) and (b) shows the temperature fields calculated under x- and y-thermal stimuli, respectively. In Fig. 3(a), three units depicted by thick dashed lines are enlarged and presented with individual temperature legends. The identical temperature distribution pattern can be found in the three units and the relative temperature relation between symmetric nodes M and M0 satisfies Eq. (3). In Fig. 3(b), the temperature field has a periodic distribution pattern and Eq. (3) is certainly satisfied. Therefore, thermal stimuli of different directions will result in the same relative temperature relations for translational structures. In this regard, different situations will be introduced and discussed for reflectional and rotational structures later.

## 2.3. Temperature disciplines in reflectional and 180 rotational symmetric structures

Reflectional and 180 rotational symmetries are also widely indicated in composite structures and can be used to further reduce the size of unit cells. However, for reflectional and 180 rotational symmetric structures, the relative temperature relations between symmetric nodes are dependent on the directions of macroscopic thermal stimuli, and thus the derivation of BCs of unit cells is very complex. First of all, a clear definition of thermal stimulus by their directions should be stated.

## 2.3.1. Two thermal stimuli definition

The macroscopic heat flux is defined as symmetric and antisymmetric thermal stimulus (STS and ATS) by its directions, in which STS is parallel to while ATS is perpendicular to the reflection plane or the 180 rotation axis. And the relative temperature relations between symmetric nodes under STS and ATS are described by Eqs. (3) and (4), respectively:

$${\mathsf{ATS}} : ~ T _ {M} - T _ {0} = T _ {0 ^ {\prime}} - T _ {M ^ {\prime}}\tag{ð4Þ}$$

It should be noted that Eqs. (3) and (4) have the opposite expressions. The two equations will be expressed as STS and ATS equations in the latter discussions, respectively.

The physical meaning of STS and ATS in heat transfer should be stated. Fig. 4(a) and (b) demonstrate the physical meanings of STS and ATS in reflectional and rotational symmetric structures, respectively. In the reflectional structure in $\mathrm{Fig.} 4 ( \mathsf{a} ) ,$ the white solid line indicates the reflection plane which is perpendicular to x-y plane. $M _ {x}$ and $M _ {x} ^ {\prime}$ are two symmetric nodes on the boundary planes in x direction, which means $M _ {x}$ becomes $M _ {x} ^ {\prime}$ after the reflectional transformation, and $M _ {y}$ and $M _ {y} '$ are symmetric nodes on y boundary planes. When the macroscopic thermal stimulus is in x

(a) in x direction 
(b) in y direction

(a) reflectional structures

(b) $180 ^{\circ}$ rotational structures 
(c) translational structures

$$\frac {q} {x} \geq \mathsf{sTS} \colon q _ {M x} = q _ {M x} ,$$

direction, the macroscopic heat flux $q ^ {0}$ is perpendicular to reflection plane, and the local heat flux of $M _ {x}$ and $M _ {x} ^ {\prime}$ have the same value while different sign (in and out), so the macroscopic heat flux is considered as ATS. On the other hand, when the macroscopic heat flux $q ^ {0}$ is in y direction and parallel to the reflection plane, the heat flux in $M _ {y}$ and $M _ {y} ^ {\prime}$ have the same value and sign (out and out), so the heat flux is considered as STS.

The similar situation can be found in the 180 rotational symmetric structure in Fig. 4(b). In the figure, a three-dimensional schematic is presented, and the white dashed line is the rotation axis which is parallel to z-axis, $M _ {x}$ and $M _ {x} ^ {\prime} , M _ {y}$ and $M _ {y} ^ {\prime} ,$ and $M _ {z}$ and Mz0 are symmetric nodes on x, y and z boundary planes, respectively. When the macroscopic heat flux $q ^ {0}$ is in x or y directions and perpendicular to the rotation axis, the heat flux in $M _ {x}$ and $M _ {x} ^ {\prime} , M _ {y}$ and $M _ {y} ^ {\prime}$ have the same value while different sign (in and out), so the macroscopic heat flux $q ^ {0}$ is considered as ATS. On the other hand, the macroscopic heat flux in z direction is considered as STS. The above descriptions are summarized in Tables 1 and 2.

Considering discussions in Section 2.2, it worth noting that in translational structures, thermal stimuli of different directions (parallel and perpendicular to the translation axis) will obtain the same temperature distribution patterns as described in Eq. (3). Although the direction of thermal stimuli has no specific influence, the thermal stimuli in both directions are considered as STS in this paper. As shown in Fig. 4(c), a translational symmetric structure (along x-axis) has infinite dimension in x-direction, so $M _ {x}$ and $M _ {x} ^ {\prime}$ are nodes in structure interior, $M _ {y}$ and $M _ {y} ^ {\prime}$ are nodes on y-boundary edge. When the macroscopic heat flux is parallel to the translation x-axis, the heat flux in $M _ {x}$ and $M _ {x} ^ {\prime}$ have the same sign, when the macroscopic heat flux is perpendicular to x-axis, the heat flux in $M _ {y}$ and $M _ {y} '$ also have the same sign (both out). Hence, for translational symmetric structures both thermal stimuli are defined as STS.

The definition of STS and ATS and corresponding temperature discipline equations are summarized in Table 3. When the arbitrary node M comes to a boundary plane, the STS and ATS equations can then be used to derive boundary conditions. Although the two equations are accurate, they should be confirmed for typical symmetric structures.

## 2.3.2. Temperature distribution disciplines in reflectional structures

In this section, two cases are calculated to confirm relative temperature relations between symmetric nodes described in Eqs. (3) and (4) for reflectional symmetric structures. Fig. 5 shows a typical reflectional symmetric structure, in which the red1 line indicates the reflection plane. A 2D model with similar structure is established, the thermal conductivity in the triangle region is 1 W/ (mK), while in other regions is $10 \mathrm {{W / ( m {\cdot K} )}}$ . For the calculation under x-thermal stimulus, the heat flux $q ^ {0}$ on the two boundary edges in x-direction is 10 and $- 10 \mathsf{W} / \mathsf{m} ^ {2}$ , respectively, and adiabatic BCs are imposed on other two edges. The case with y-thermal stimulus has opposite BCs expression.

Fig. 6(a) and (b) shows the temperature fields calculated under macroscopic x-heat flux and y-heat flux, respectively. In Fig. 6(a), the macroscopic $q ^ {0}$ is perpendicular to the reflection plane and thus can be considered as ATS, as shown in the temperature fields, the relative temperature of symmetric nodes M and M0 satisfy the relations described in Eq. (4). In Fig. 6(b), $q ^ {0}$ is parallel to the reflection plane, and thus can be considered as STS, and the temperature field is distributed as Eq. (3) shows. Thus, the STS and ATS equations are confirmed for reflectional symmetric structures.

## 2.3.3. Temperature distribution disciplines in 180 rotational structures

Fig. 7 shows a typical 180 rotational symmetric structure, in which the red point indicates the rotation axis, M and M0 , O and O0 are symmetric nodes on a specific cross section plane P. A 3D model with similar structure is established, the thermal conductivities are $1 \mathrm{W} / ( \mathrm{m} {\cdot} \mathrm{K} )$ and $10 \mathrm {{W / ( m {\cdot K} )}}$ in triangle regions and other regions, respectively. Two cases with the macroscopic heat flux $q ^ {0}$ in x and z directions are calculated, respectively. The heat flux for the two boundary planes in calculation directions are 10 and $10 \mathrm {{W / m ^ {2}}}$ , respectively, and other boundary planes are adiabatic.

Fig. 8(a) and (b) shows the temperature fields of plane P under x and z-direction macroscopic thermal stimuli, respectively. In Fig. 8 (a), the macroscopic heat flux $q ^ {0}$ is in x direction and perpendicular to the rotation axis and thus can be considered as ATS, while in Fig. 8(b), $q ^ {0}$ is in z direction and parallel to the reflection plane, and thus can be considered as STS. Accordingly, the relative temperature of symmetric nodes M and M0 in Fig. 8(a) and (b) satisfy the relations described in Eqs. (4) and (3), respectively. It is clear that the STS and ATS equations for 180 rotational symmetric structures are confirmed by these two cases.

In this section, for three typical symmetric structures, symmetric and antisymmetric thermal stimuli are defined and corresponding temperature distribution disciplines, i.e., the relative temperature relations between symmetric nodes are described by STS and ATS equations. The disciplines demonstrated above imply that if a new unit cell is formulated based on the original structure, when the arbitrary node M comes to boundaries, the STS and ATS equations can be used to derive additional constraint BCs of the unit cell under specific macroscopic heat flux, which in fact is the BCs of the original structure.

In summary, for an infinite dimension structure UC0, a unit cell is first formulated based on translational symmetries and called UC1, its boundary condition BC1 is derived from BC0, which is the measurement conditions of experiment, then reflectional and rotational symmetries present in UC1 can be identified and used to formulate unit cells, UC2, UC3 . . . UCn, with smaller sizes. UC1 is the basic cell, and BC1 is the basic boundary conditions. BC1 is called periodic BCs, in thermal studies, the attention paid on it is not enough since inappropriate BCs sometimes can lead to approximate accurate results. In the next Section 3, the derivation, the meaning and the necessity of periodic BCs will be clearly stated by a simple case of unidirectional fiber reinforced composite, and the error cause of inappropriate BCs is revealed in the physical mechanism point of view.

## 3. Axial calculations of UD composites

## 3.1. Unit cell and boundary conditions

Fig. 9(a) shows the typical structure of the axial cross section of a unidirectional (UD) fiber reinforced composite, the red region is fiber and the blue one is the matrix. If the axial (x-direction) effective thermal conductivity is about to be calculated, the BC0 of the macroscopic structure is Eq. (2-1).

In order to realize a feasible numerical study, a unit cell UC1 indicated by the white rectangle region should be formulated based on translational symmetries along x and y directions as shown in Fig. 9(a). In the figure, a and b are the length and the width of the unit cell, respectively. c is the width of the fiber region. It should be noted that the unit cell length a can be an arbitrary value since no certain periodic length existing in x-direction, which means the length-width ratio, a/b of the unit cell can be an arbitrary value, and this may influence the simulation results to some extent. In this section, the influence of length-width ratio on the numerical results is studied under two types of boundary conditions: simpler BC0 and the derived BC1.

UC1 has four boundary edges, $x = 0 , x = a , y = 0$ and $y = b$ needing BCs. The boundary edges in x direction (x = 0 and x = a) and y direction (y = 0 and $y = b )$ are formulated by translational symmetry along x and y directions, respectively, so these two groups of edges should be derived separately. For edges in x direction, an arbitrary node $M = \left( x _ {1} , y _ {1} \right)$ is assumed to be in the structure, its symmetric node M0 corresponding to translation along x direction will have a coordinate of $( x _ {1 +} a , y _ {1} )$ , and reference nodes O and O0 can be specified as $( 0 , 0 )$ and $( a , 0 ) ,$ , respectively. If the macroscopic temperature gradient of the original structure is $\nabla T _ {x} ^ {0} ,$ then the temperature difference between reference nodes O and $O ^ {\prime}$ is $\Delta T = a \nabla T _ {x} ^ {0}$ . When M comes to the UC1 boundary edge $x = 0 ,$ , we can have $M = ( 0 , y _ {1} )$ and $M ^ {\prime} = \left( a , y _ {1} \right)$ , then the STS equation (Eq. (3)) becomes:

$$T _ {( 0 , y _ {1} )} - T _ {( a , y _ {1} )} = \Delta T = a \nabla T _ {x} ^ {0}\tag{ð5Þ}$$

Eq. (5) is the boundary condition of edges $x = 0$ and $x = a$

For edges in y direction, the arbitrary node M and its symmetric node M0 corresponding to translation along y direction have coordinates of $( x _ {1} , y _ {1} )$ and $( x _ {1} , y _ {1} + \mathsf{b} )$ , and reference node O and O0 can be specified as $( 0 , 0 )$ and $( 0 , b )$ , respectively. Considering Eq. (4), the temperature difference between O and O0 is 0. When M comes to the boundary edge $y = 0 ,$ we can have $M = ( x _ {1} , 0 )$ and $M ^ {\prime} = ( x _ {1} , \mathbf {b} ) ,$ then the STS equation (Eq. (2)) becomes:

$$T _ {( x _ {1} , 0 )} - T _ {( x _ {1} , b )} = 0\tag{ð6Þ}$$

Eqs. (5) and (6) are the derived boundary conditions BC1 and are the so-called periodic BCs. The periodic BCs have accurate descriptions for certain and have wide utilization, however, for some complex structure, another type boundary condition as shown in Eq. (7) seems to be much simpler and easier to apply.

$$q _ {x} | _ {x = 0} = - q _ {x} | _ {x = a} = q , q _ {y} | _ {y = 0} = q _ {y} | _ {y = b} = 0\tag{ð7Þ}$$

In fact, Eq. (7) is the expression of BC0 (Eq. (2-1)) and will lead to some calculation errors for certain. Compared with BC0, BC1 describes a constraint of nodal temperatures on symmetric locations. If we define the dimensionless temperature difference (DTD) between symmetric nodes on boundary planes $x = 0$ and $x = a$ as: $( T _ {( 0 , y _ {1} )} - T _ {( a , y _ {1} )} ) _ {y} / \mathrm{mean} ( T _ {x _ {= 0}} - T _ {x = a} )$ , BC1 means the DTD value equals to 1 at different locations (y-coordinate), while for BC0 it varies with y values. Fig. 9(b) shows the schematic of BC1,

BC0 and another type possible BCs described by $\operatorname{Eq.} \left( 9 \right)$ in later discussions. From the figure, one can notice that BC1 demonstrates temperature constraints between symmetric nodes on corresponding boundaries and is stricter comparing with BC0.

## 3.2. Axial effective thermal conductivities

In this section, BC0 and BC1 are imposed on calculations, respectively, to demonstrate their difference in the physical mechanism point of view.

In the model, $b = 5$ and $c = 3$ which means the fiber volume fraction is 0.6. If the thermal conductivity of the matrix is assumed to be 1 W/(mK) and the axial thermal conductivity of the fiber is 10 W/(m K), according to the classic Rule of Mixture which is derived based on the parallel-series network method as shown in Eq. (8), the effective axial thermal conductivity of the UD composite is $6.4 {\mathrm{W}} / ( {\mathrm{m}} {\cdot} {\mathrm{K}} )$ In Eq. $( 8 ) , \lambda ^ {0} , \lambda _ {f} , V _ {f}$ and $\lambda _ {m}$ are the axial effective thermal conductivity of composites, axial thermal conductivity of fibers, volume fraction of fibers and thermal conductivity of matrix, respectively.

$$\lambda ^ {0} = \lambda _ {f} V _ {f} + \lambda _ {m} ( 1 - V _ {f} )\tag{ð8Þ}$$

It worthy discussed here is that for some composites with ordered distribution of dispersed phase like the UD composite, the structure seems to be simple, for this type of composite, the parallel-series network method is efficient and easier to be realized. However, most composites have relative complex structures and the parallel-series network method has some difficulties in simulating these systems. For example, in most analytic studies of the textile reinforced composite, the consideration of undulation of fiber yarns will make the model very complicated.

Numerical calculations with different length-width ratio (a/ $b = 0.1 \sim 200 )$ are conducted in this section and the calculated effective axial thermal conductivities are shown in Fig. 10. In the figure, the black dashed line is 6.4 W/(m K) which is the accurate results calculated by the classic mixture rule, the blue solid line with circles shows the results obtained by derived BC1, while the red solid line with rectangles is that of BC0. As shown in the figure, BC1 can obtain the accurate results in the whole range of lengthwidth ratio (0.1 200). However, BC0 has some deviations from the accurate result especially when the length-width ratio is small, effective results can only be obtained when the length-width ratio reaches to 100. This reveals that BC0 is not an appropriate boundary condition, and if the temperature distributions of boundary planes are investigated, the differences between BC0 and BC1 can be clarified.

Fig. 11 shows the dimensionless temperature difference (DTD) between symmetric nodes on boundary planes $x = 0$ and $x = a ,$ i.e., nodes $( 0 , y _ {1} )$ and $( a , y _ {1} ) ,$ , calculated by BC0. The horizontal axis is the value of y1. Different solid lines are results obtained by different length-width ratios. The red dashed line indicates value 1 which is the DTD distribution of boundary nodes constrained by BC1. As shown in the figure, DTD is smaller in the fiber region $( y _ {1} = ( 1 , 4 ) )$ which has larger thermal conductivity, while larger in the matrix region which has smaller thermal conductivity. With the increasing length-width ratio reaches 100, DTD approaches to 1, which means the temperature distribution on boundary planes induced by BC0 is equivalent to that constrained by BC1. This indicates a conclusion: it is not the length-width ratio but the BCs that influence the calculation accuracy.

(a) $q ^ {0}$ in x direction (ATS)

(b) $q ^ {0}$ in y direction (STS)

On the other hand, if a heat flux distribution as shown in Eq. (9), is imposed on the model, the calculated effective thermal conductivity also equals to 6.4 W/(mK) under different length-width ratios. This indicates that BC0 in Eq. (7) prescribes an inaccurate distribution of heat flux in boundary edges. However, for most complex situations, the distribution as shown in Eq. (9) is unavailable at the pre-processing stage, so the strictly derived boundary conditions as BC1 is essential for an accurate calculation.

$$\begin{array} {r l} & {q _ {x} | _ {x = 0} = - q _ {x} | _ {x = a} = q _ {1} , ( b - c ) / 2 \leqslant y \leqslant ( b + c ) / 2} \\ & {q _ {x} | _ {x = 0} = - q _ {x} | _ {x = a} = q _ {2} , 0 < y < ( b - c ) / 2 \mathrm{~or~} ( b + c ) / 2 < y < b} \\ & {q _ {y} | _ {y = 0} = q _ {y} | _ {y = b} = 0 ,} \\ & {q _ {1} / q _ {2} = 10 : 1} \end{array}\tag{ð9Þ}$$

## 4. Study of typical composites with symmetric structures

In this section, unit cell formulations of several typical composites are presented. The transverse cross section of a unidirectional (UD) composite is investigated, the translational, reflectional and 180 rotational symmetries indicated in the structure are observed and relevant unit cells for thermal calculations are formulated. According to the simple case, the basic calculation process of composite effective thermal conductivities using unit cells is clarified. Then for all types of satin woven composites, the symmetric structure is analyzed, unit cells of different sizes are formulated, BCs are derived in a unified form and corresponding calculations are conducted.

(a) $q ^ {0}$ in x direction (ATS)

## 4.1. Transverse thermal properties of UD composite

## 4.1.1. Unit cells and boundary conditions

Fig. 12 shows the typical hexagonal fiber-matrix distribution pattern on transverse cross-section of a UD composite, and several types of unit cells formulated based on translational, reflectional and 180 rotational structure symmetries. In the figure, the red circles indicate fibers, the matrix is not shown, the two black lines with arrow are the translation axes, the blue and green lines are the reflection planes $P _ {x}$ and $P _ {y} ,$ respectively, while the pink dot presents the rotation axis $L _ {z}$ The left diagram of Fig. 12 shows part structure of macroscopic cross section of UD composite (UC0), and it possesses translational symmetries in x and y directions. As shown in Fig. 12, UC1 is then formulated based on translational symmetries, and then a reflectional symmetric structure can be observed in UC1. Two reflection planes in horizontal $\left( P _ {x} \right)$ and vertical $\left( P _ {y} \right)$ directions are indicated by blue and green lines, respectively, UC2 of $1 / 2$ size and UC3 of $1 / 4$ size will be formulated based on them, respectively. The structure of UC3 has a $180 ^{\circ}$ rotational symmetry about rotation axis $\left( {{L} _ {z}} \right)$ indicated by the pink dot, and UC4 of $1 / 8$ size will be finally formulated. In this section, appropriate thermal BCs for UC1, UC2, UC3 and UC4 are derived as shown in Eqs. (11)–(14), respectively, and corresponding thermal calculations are conducted. The derivation process of BCs is summarized in Table 4, from the table one can notice that STS or

ATS equations are used by each derivation step for each boundary plane and are the definite basis of BC derivation of a unit cell. The details are similar to the discussion in Section 3.1 and are omitted here.

Under different directions of the macroscopic heat flux $q ^ {0} ,$ the BCs should be derived separately considering different STS and ATS equations, while for BC1 in which the STS equation is applicable in all conditions, a unified form is obtained. For each unit cell, there are four boundary edges requiring $\mathsf{BCS} ,$ , and considering that all the unit cells have a rectangle configuration, the boundary edges can be demonstrated by $L _ {1} , \ L _ {2} , \ L _ {3}$ and $L _ {4} ,$ respectively, although they have different coordinates for different unit cells as shown in Fig. 13. In addition, as discussed in [21,29] for such case the BCs of four vertices should be described by separate constraint equations to avoid the possible redundant constraints that may stop the analysis running, and the additional equations can be derived from Eqs. (10)–(13) and are omitted here for simplicity.

$$\begin{array} {r} {L _ {1} - L _ {2} : T _ {( 0 , y _ {1} )} - T _ {( a , y _ {1} )} = a \nabla T _ {x} ^ {0}} \\ {\mathrm{BC1:}} \\ {L _ {3} - L _ {4} : T _ {( x _ {1} , 0 )} - T _ {( x _ {1} , b )} = b \nabla T _ {y} ^ {0}} \end{array}\tag{ð10Þ}$$

$${\begin{array} {l} {L _ {1} - L _ {2} : T _ {( 0 , y _ {1} )} - T _ {( a , y _ {1} )} = a \nabla T _ {x} ^ {0}} \\ {{\mathrm{BC2~under~}} q {\boldsymbol {0}} x :} \\ {L _ {3} , L _ {4} : q _ {( x _ {1} , 0 )} = q _ {( x _ {1} , b / 2 )} = 0} \end{array}}\tag{ð11-1Þ}$$

(a) Axial section of UD composite and its unit cell 
(b) Two boundary conditions

$${\begin{array} {r l} & {L _ {1} - L _ {2} : T _ {( 0 , y _ {1} )} - T _ {( a , y _ {1} )} = 0} \\ {{\mathrm{BC2~under~}} q _ {y} ^ {0} :} & {L _ {3} : T _ {( x _ {1} , 0 )} - T _ {( 0 , 0 )} = 0} \\ & {L _ {4} : T _ {( x _ {1} , b / 2 )} - T _ {( 0 , 0 )} = - b \nabla T _ {y} ^ {0} / 2} \end{array}}\tag{ð11-2Þ}$$

$$L _ {1} : T _ {( 0 , y _ {1} )} - T _ {( 0 , 0 )} = 0$$

$$\begin{array} {r l} {\mathrm{BC3~under~} q _ {x} ^ {0} :} & {\mathbf {L} _ {2} : T _ {( a / 2 , y _ {1} )} - T _ {( 0 , 0 )} = - a \nabla T _ {x} ^ {0} / 2} \\ & {L _ {3} , L _ {4} : q _ {( x _ {1} , 0 )} = q _ {( x _ {1} , b / 2 )} = 0} \end{array}\tag{ð12-1Þ}$$

$$L _ {1} , L _ {2} : q _ {( 0 , y _ {1} )} = q _ {( a / 2 , y _ {1} )} = 0$$

$$\begin{array} {r l} {{}} & {{\mathrm{BC3~under~} q _ {y} ^ {0} : ~ {\bf {L}} _ {3} : T _ {( x _ {1} , 0 )} - T _ {( 0 , 0 )} = 0}} \\ {{}} & {{{\bf {L}} _ {4} : T _ {( x _ {1} , b / 2 )} - T _ {( 0 , 0 )} = - b \nabla T _ {y} ^ {0} / 2}} \end{array}\tag{ð12-2Þ}$$

$$\begin{array} {r l} & {L _ {1} : T _ {( 0 , y _ {1} )} - T _ {( 0 , 0 )} = 0} \\ & {L _ {2} : T _ {( a / 2 , y _ {1} )} - T _ {( 0 , 0 )} = - a \nabla T _ {x} ^ {0} / 2} \\ {\mathrm{BC4~under~} q _ {x} ^ {0} :} & {L _ {3} : q _ {( x _ {1} , 0 )} = 0} \\ & {L _ {4} : T _ {( x _ {1} , b / 4 )} + T _ {( a / 2 - x _ {1} , b / 4 )} - 2 T _ {( 0 , 0 )} = - a \nabla T _ {x} ^ {0} / 2} \end{array}\tag{ð13-1Þ}$$

$$\begin{array} {c} {{L _ {1} , L _ {2} : q _ {( 0 , y _ {1} )} = q _ {( a / 2 , y _ {1} )} = 0}} \\ {{\mathrm{BC4~under~} q _ {y} ^ {0} : \mathrm{~} L _ {3} : T _ {( x _ {1} , 0 )} - T _ {( 0 , 0 )} = 0}} \\ {{\mathrm{~}}} \\ {{L _ {4} : T _ {( x _ {1} , b / 4 )} + T _ {( a / 2 - x _ {1} , b / 4 )} - 2 T _ {( 0 , 0 )} = - b \nabla T _ {y} ^ {0} / 2}} \end{array}\tag{ð13-2Þ}$$

According to the above discussion, the basic process of the formulation of a unit cell can be summarized as: 1st the identification of structure symmetries; 2nd the establishment of geometric configuration of UCi; 3rd the determination of $\scriptstyle {q ^ {0}}$ direction, i.e., STS or ATS; 4th the derivation of boundary conditions.

## 4.1.2. Temperature fields and effective thermal conductivities

In the numerical model, the fiber volume fraction is 0.3, and the thermal conductivity of the fiber and matrix are 10 and 1 W/(mK), respectively. Fig. 14 shows the temperature fields calculated by four unit cells, the upper diagrams are the results obtained under macroscopic heat flux of x direction, while the lower ones are that under y direction. The identical temperature contours for four unit cells can be observed in the figure. In addition, the calculated effective thermal conductivities are listed in Table 5. Eq. (14) [31] is an analytic equation which can be used to compute transverse thermal conductivity of unidirectional (UD) fiber reinforced composite, and the results calculated by the equation is also listed in Table 5. It should be noted that Eq. (14) is also developed based on the parallel-series network method. In the table, it can be first found that thermal conductivities in x and y directions have the identical value which means the composite is transversely isotropic. And the same effective thermal conductivities are obtained by numerical models and analytic equation, in order to show the results deviation of less than 0.02%, five effective digits are presented in the table. The good agreement between numerical and analytic results confirms the accuracy of unit cells and BCs established in this paper.

$$\lambda ^ {0} = \lambda _ {m} + \frac {V _ {f}} {1 / ( \lambda _ {f} - \lambda _ {m} ) + ( 1 - V _ {f} ) / ( 2 \lambda _ {m} )}\tag{ð14Þ}$$

where $\lambda ^ {0} , \lambda _ {m}$ and $\lambda _ {f}$ are the thermal conductivity of the composite, matrix and fibers, respectively, $V _ {f}$ is the fiber volume fraction.

The UD composite is widely existing in various composites. For instance, the fiber bundles (yarn) in more complex textile reinforced composite can be considered as UD composites. Thus, the unit cells and results obtained in this section can be used as the input conditions in thermal study of other composites with complex structures.

## 4.2. Satin woven composites

## 4.2.1. Unit cells formulation

Textile reinforced composite is a typical composite with symmetric structures, in which satin woven composite is fabricated based on satin weave textiles and specific matrix (resin or ceramic). Among all the woven composites, the satin one has glossier surface and is more flexible due to its less interlacing points of weft and warp yarns, however, the specialized study of its unit cells is very limited. In this paper, the satin woven composite is selected to conduct the calculation for two reasons: 1st it has wide industry application potential while very limited present research; 2nd compared with plain woven and 3D braided composite that we studied in previous works [29,30], in the satin weave textile nonorthogonal translation symmetries can be used to formulate a unit cell which is much smaller than the orthogonal symmetries.

All the complex textile structures definitely obey some specific symmetric rules and thus can be used to formulate unit cells.

According to the interlacing points layout, the satin weave textile can be defined as 4-, 5-, 6-, 7- and 8-harness (HS) textiles. Fig. 15 shows the textile structures (left) and unit cells (right) for each harness textile, and the matrix is not shown to display the yarn orientation clearly. The out-plane cross section is presented in the left lower part of the figures. For 4, 5, 6, 7 and 8HS satin textiles, there are 4, 5, 6, 7 and 8 warp yarns between two neighbouring floating weft yarns, respectively, as shown in Fig. 15.

The right parts of Fig. 15 are schematic diagrams of unit cells, in which only interlacing points are displayed by black rectangles. The square unit cell (SUC) has the configuration formulated in literature [32], while UC1 and UC2 are two unit cells established in this work. The SUC is formulated based on the orthogonal transla-

(a) 4HS stain weave textile

(b) 5HS stain weave textile

(c) 6HS stain weave textile

(d) 7HS stain weave textile

(e) 8HS stain weave textile

tional symmetries in x-, y- and z-axis (perpendicular to the paper) and has a square cross section. In this work, for each textile, parallelogram unit cells UC1 are formulated based on the translational symmetries in $x ^ {\prime} , y ^ {\prime} -$ and z-axis, and smaller parallelogram unit cells UC2 are formulated further based on the 180 rotational symmetry about the axis $Z _ {1}$ indicated by the white point. It is clear that UC1 and UC2 have much smaller size than SUC.

Fig. 16 shows a schematic of 4HS textile, from which one can see that the whole region can be covered by translations of the parallelogram unit cell UC1. Compared with yellow lines indicated SUC, UC1 has a 1/4 size as shown in Fig. 16, and thus UC2 has a 1/8 size. Similarly, for 5, 6, 7 and 8HS satin weave fabrics, UC1s are of 1/5, 1/6, 1/7 and 1/8 size, and UC2s are of 1/10, 1/12, 1/14 and 1/16 size, respectively.

If the structure of UC1 is carefully investigated, a 180 rotational symmetric structure can be found. Fig. 17 is the 180 rotational symmetric structure of UC1 of 4HS, in the figure ‘‘FB” means fiber bundle, the rotation axis (out plane direction) is indicated by a blue point, all the bundles can be classified as 5 groups, FB1 and FB10 , FB2 and FB20 , FB3 and FB30 , FB4 and FB40 , and FB5 and FB50 , according to their 180 rotational symmetric relations. After a 180 rotational transformation, the FB1 FB5 bundles will become FB10 FB50 , respectively. At this condition, one can establish a model contains only fiber bundles of FB1 FB5, i.e., UC2 instead of the whole structure UC1 as long as the accurate BCs are imposed on.

Fig. 18 is the UC1 model of 4HS satin woven composite, UC2 is depicted by white dashed lines, the cross section and side profile of fiber bundles are shown by two bundles (FB1 + FB10 , FB3 + FB30 ) from the front view, the matrix is not shown in the figure. In the figure, S is the distance between the two adjacent fiber bundles axes, W is the width, $h _ {f}$ is the height of fiber bundles, and h is the height of models (with matrix). In this work for all the satin woven composites, $S = 1.45$ mm, W = 1.25 mm, $h _ {f} = 0.19$ mm, h = 0.52 mm. The model has a fiber bundle volume fraction of 0.45, while a matrix volume fraction of 0.55.

Each fiber bundle has two types of segments: the undulant and straight segments. The axis of the undulant segment can be defined by Eq. (15):

$$z = \pm \frac {h} {2} \cos ( \pi x / S ) , z = \pm \frac {h} {2} \cos ( \pi y / S )\tag{ð15Þ}$$

The cross section of the fiber bundles can also be described by similar cosine equations.

## 4.2.2. Coordinate systems

In the calculation, the axial and transverse thermal conductivities of fiber bundles are input as material properties, and thus for each fiber bundle a principal axis should be specified which means a local coordinate system (CS) should be specified. However, the undulant segment means one local coordinate system is not enough to describe the whole fiber bundle. In this work, the elements in undulant segment are classified into some groups by their locations in the global CS. For elements in the same group, the same local CS is defined and thus have the same transverse and axial directions. A schematic of the CS involved in the calculation is shown in Fig. 19. There are three types of CSs, i.e., the global CS for the composite, the local CS for the matrix which is identical with the global CS, and the local CS for fiber bundles which is varies with the undulation the fiber bundles. In this work, for each undulant segment with a length of $S _ {x} ,$ 10 groups of elements which mean 10 local coordinate systems are defined. Also, the numerical results are independent of this number.

## 4.2.3. Boundary conditions

As shown in Fig. 20, UC1 (the parallelogram depicted by the yellow and blue solid lines) is the unit cell that formulated by translations along $x ^ {\prime} - , y ^ {\prime} -$ and z-axis. a and b are the width and length of the unit cell, respectively. a and b are the angles that x0 - and y0 -axis relative to x-axis, respectively. The geometry parameters of unit cells for different satin woven composites are listed in Table 6, where S is the distance between two adjacent fiber bundles as discussed above. It is clear that UC2 has a $b / 2$ length boundary $x ^ {\prime} = 0$ and the same other parameters with UC1.

Based on the unified parameter a, b, a and b, the BCs of multiharness satin woven composites are derived in unified equations, and for UC1 and UC2 are described by Eqs. (16) and (17), respectively. The general derivation process is listed in Table 7 and the details are omitted. As discussed above the BCs of eight vertices and twelve edges should be described by separate constraint equations and are omitted here for simplicity. In the equations, $P _ {1} , P _ {2} ,$ $P _ {3} , \ P _ {4} , \ P _ {5}$ and $P _ {6}$ indicate boundary planes as shown in the 3D model in Fig. 20.

$${\begin{array} {r l} & {P _ {1} - P _ {2} : T _ {x ^ {\prime} = 0} - T _ {x ^ {\prime} = a} = a \cos ( \alpha ) T _ {x} ^ {o} - a \sin ( \alpha ) T _ {y} ^ {o}} \\ {{\mathrm{UC1:~}} P _ {3} - P _ {4} : T _ {y ^ {\prime} = 0} - T _ {y ^ {\prime} = b} = b \cos ( \beta ) T _ {x} ^ {o} + b \sin ( \beta ) T _ {y} ^ {o}} \\ & {P _ {5} - P _ {6} : T _ {z = 0} - T _ {z = h} = h T _ {z} ^ {o}} \end{array}}\tag{ð16Þ}$$

## 4.2.4. Temperature fields and effective thermal conductivities

In the numerical model, the fiber is carbon fiber with transverse and axial thermal conductivities of 0.84 and 8.4, respectively, the matrix is phenolic resin with a thermal conductivity of 0.42, and the fiber volume fraction is 0.38. Fig. 21 shows the temperature distributions obtained by UC1 and half size UC2, under ydirection and z-direction macroscopic heat fluxes ${( q _ {y} ^ {~ 0}}$ and $q _ {z} ^ {\bar {0}} ) ,$ respectively. The temperature legend is not shown since the absolute value of temperature is not concerned in this work. From the top to the bottom are the results of 4, 5, 6, 7 and 8HS satin woven composites, respectively. In all the results of UC1, the temperature fields are distributed in disciplines which are described by Eqs. (3) (STS) and (4) (ATS) equations. As shown in the figure, in the results under ${q _ {y}} ^ {0}$ (left diagrams), the relative temperature between symmetric parts satisfies the STS equation, while the distribution under ${q _ {z}} ^ {0}$ satisfies the ATS equation. In addition, UC1 and UC2 obtain the very similar temperature distributions.

Table 8 shows the calculated in-plane ${( \lambda _ {x x}} ^ {0} = {\lambda _ {y y}} ^ {0} )$ and out-plane $( {\lambda _ {z z}} ^ {0} )$ effective thermal conductivities. Identical results with the maximum deviation of 0.19% are obtained by the two multi-size unit cells. Considering the identical temperature fields and effective thermal conductivities, it can be concluded that the established unit cells and the derived BCs in this work are accurate. In addition, if the results of different composites are compared, one can notice that the in-plane thermal conductivity increases, while the out-plane one decreases very slightly with the increasing harness number of composites. This is because of the less interlacing points of weft and warp yarns, which means the shorter projection length of fiber yarns (higher heat conductive ability) in out-plane direction.

$$\begin{array} {r l} & {P _ {1} - P _ {2} : T _ {x - 0} - T _ {x - a} = a \cos ( x ) T _ {x} ^ {0} - a \sin ( x ) T _ {y} ^ {0}} \\ & {P _ {3} : T _ {y - 0 , x \leq a / 2} + T _ {y - 0 , x \leq a / 2} - 2 T _ {( 0 , 0 , 0 )} = - a \cos ( x ) T _ {x} ^ {0} + a \sin ( x ) T _ {y} ^ {0}} \\ {\mathrm{UC2~under~} q \mathrm{0} x \mathrm{~or~} q \mathrm{0} y : \} \\ & {P _ {4} : T _ {y - b / 2 , x \leq a / 2} + T _ {y - b / 2 , x \leq a / 2} - 2 T _ {( 0 , 0 , 0 )} = - ( a \cos ( x ) + b \cos ( \beta ) ) T _ {x} ^ {0} + ( a \sin ( \alpha ) - b \sin ( \beta ) ) T _ {y} ^ {0}} \\ & {P _ {5} - P _ {6} : T _ {z - 0} - T _ {z \mathrm{ab}} = h T _ {z} ^ {0}} \end{array}\tag{ð17-1Þ}$$

$${\begin{array} {r l} & {P _ {1} - P _ {2} : T _ {x - 0} - T _ {x - a} = a \cos ( \alpha ) T _ {x} ^ {0} - a \sin ( \alpha ) T _ {y} ^ {0}} \\ & {P _ {3} : T _ {y = 0 , x \leqslant a / 2} - T _ {y ^ {- 0} , x ^ {\prime} \geqslant a / 2} = a \cos ( \alpha ) T _ {x} ^ {0} - a \sin ( \alpha ) T _ {y} ^ {0}} \\ {{\mathrm{UC2~under~}} q _ {z} ^ {0} :} & {P _ {4} : T _ {y ^ {- b} / 2 , x ^ {\prime} \leqslant a / 2} - T _ {y ^ {- b} / 2 , x \geqslant a / 2} = b \cos ( \beta ) T _ {x} ^ {0} + b \sin ( \beta ) T _ {y} ^ {0} + a \cos ( \alpha ) T _ {x} ^ {0} - a \sin ( \alpha ) T _ {y} ^ {0}} \\ & {P _ {5} - P _ {6} : T _ {z = 0} - T _ {z - h} = h T _ {z} ^ {0}} \end{array}}\tag{ð17-2Þ}$$

4.2.5. Comparison with available experimental results

Although the identical numerical result obtained by multi-size unit cells implies that the boundary conditions derived in this work are accurate, in order to further make the validation more reliable, a case of C/phenolic 8HS satin woven composite are calculated and compared with the experimental results available in [16]. The C/ phenolic model established in this work has the same architecture and constituents $\left( V _ {f} = 0.46 \right)$ with that in [16], and the results are listed in Table 9. We can notice a relatively good agreement with a maximum deviation of 15.8% which might be regarded acceptable for the complexities in both measurement and simulation.

## 5. Conclusions

In this paper, a general rule of unit cell formulation for thermal calculation of composites with symmetric structures is developed. The rule is based on the macroscopic experimental specimen and measurement conditions. The macroscopic heat flux in experiment is defined as symmetric thermal stimuli (STS) and antisymmetric thermal stimuli (ATS) by its directions for translational, reflectional and 180 rotational symmetric structures, respectively. The temperature distribution disciplines in different symmetric structures are described by corresponding equations and confirmed by typical calculations, and can be used to derive boundary conditions of unit cells. A case of axial study of unidirectional fiber reinforced composite is conducted to show the necessity of derived boundary conditions, and a transverse study is presented to introduce the basic process of unit cell formulations and boundary conditions derivation, and then for more complex $4 - , 5 - , 6 - , 7 -$ and 8-harness satin woven composites, two unit cells of different sizes are formulated, the corresponding boundary conditions are derived in a unified form, and the numerical models are validated by the identical results and also the experimental results available in reference. The approach developed in this paper can be referenced by thermal calculations of any other composites with symmetric structures. It can be concluded that:

1. Effective thermal properties of composites with symmetric structures can be efficiently calculated by a unit cell model, which should be formulated based on the symmetries indicated in the structures, and the corresponding boundary conditions should be derived based on temperature distribution disciplines clarified in this work.

2. The basic process of the formulation of a unit cell has four steps: the identification of structure symmetries, the establishment of geometric configuration, the determination of $q ^ {0}$ direction and the derivation of boundary conditions.

3. Each utilization of symmetries can create a new unit cell with smaller size, and new boundary conditions should be derived strictly since inappropriate boundary conditions will affect the calculation accuracy.

4. For the studied satin woven composites, the in-plane thermal conductivity increases, while the out-plane one decreases very slightly with the increasing harness of composites.

## Omitted Tables

- [Table 1 omitted; saved to tables/table_001.md]
- [Table 2 omitted; saved to tables/table_002.md]
- [Table 3 omitted; saved to tables/table_003.md]
- [Table 4 omitted; saved to tables/table_004.md]
- [Table 5 omitted; saved to tables/table_005.md]
- [Table 6 omitted; saved to tables/table_006.md]
- [Table 7 omitted; saved to tables/table_007.md]
- [Table 8 omitted; saved to tables/table_008.md]
- [Table 9 omitted; saved to tables/table_009.md]
- [Table 10 omitted; saved to tables/table_010.md]
- [Table 11 omitted; saved to tables/table_011.md]
