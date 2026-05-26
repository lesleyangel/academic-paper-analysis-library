## 1. Introduction

High-speed flight vehicles experience harsh aerodynamic heating process, and the long-duration high-speed flight brings about severe heat accumulation [1,2]. Traditional thermal protection system (TPS) is mainly based on the thermal-proof coatings with high radiation emissivity [3] and thermal-insulation structures with low conduction ability [4], leading to very limited heat capacity and thermal protection efficiency. In recent years, integrating thermoelectric generator (TEG) into TPS has emerged as an efficient and promising technique for flight vehicles [5–8]. The TEG utilizes the semiconductor TE materials to directly or indirectly convert the heat into electricity from the temperature difference of the ambient energy source [9–11], and can be adopted to capture the aerodynamic heat of flight vehicles. Unlike most published TEGs operated under small temperature differences [12–19], the highspeed flight vehicle inherently creates huge temperature gradients between the fuselage interior and exterior. Thus, a highly stable TEG performance over a relatively large temperature range is essential for high-speed flight vehicles.

The TEG mainly consists of several couples of TE legs (N- and P-type) which are connected in series by electrodes, however, the imperfect contact at the multiple interfaces between TE legs and electrodes lead to a shrinkage effect of the heat and electrical flows. Such contact effects manifest as thermal contact resistance (TCR) and electrical contact resistance (ECR), and significantly influence the TE transfer and conversion process [20,21]. Liu et al. [22] studied the TCR between bearing inner ring and shaft journal, and found that the interference fit reduces the TCR because the interference fit reduces the interfacial contact area. Wan et al. [23] studied both ECR and TCR in Al to zinc-coated steel in resistance spot welding process, and explored the strong influence of resistance values by mechanical contact pressure and temperature at the interface. Ren et al. [24] found that the elastic modulus of a thermal pad acts like a clearance medium in the heat transfer between two solids, affecting the real contact area of the rough contact interface, which further affects the TCR, and also showed that the TCR is affected by the material properties. It can be seen that the interface temperature, pressure, clearance medium and material property are common factors affecting TCR, which are considered in this paper. However, most published reports on contact effects focused on conventional metallic materials (e.g., Fe, Al, Cu, $\operatorname{Zn} ,$ and Mn) and their alloys, with fewer studies on the TCR and ECR of TE materials.

The TCR and ECR prediction consists of three main steps: rough surface characterization, contact deformation, and TE transfer and conversion analysis. Accurate characterization of the rough surface is a necessary prerequisite for the precise assessment of the contact effect. Various methods can be employed to reconstruct rough surfaces, including W-M fractal models [25], GW statistical models [26], Euclidean geometrical statistical models [27], semi-deterministic-based approaches [28], and direct measurement of real surface topography [29]. In the authors’ previous works [30,31], an optical profiler is used to measure the real surface topography and construct TCR and ECR models for one or two TE couples, however, in this work, the TEG consists of twenty-seven TE couples (one TE couple includes one N- and P-type TE leg), totally 108 surfaces of TE legs and 108 surfaces of electrodes need to be measured, leading to unaffordable cost. Thus, the fractal W-M function with certain experimental confirmation is adopted to characterize the surface topography. The W-M fractal method can effectively capture the geometric self-similarity and self-affinity of rough surfaces, allowing similar surface topography to be observed at different magnifications, regardless of spatial scale, which are commonly employed for rough surface reconstructions [22,32–35]. Wang et al. [36] found that the study of TCR requires the use of elastoplastic deformation model. Contact deformation affects the real contact area at the micro-scale, and how to accurately calculate the real contact area is a hot topic in current research. For the TE transfer and conversion, current research focused on exploring the maximum supply voltage, output power and conversion efficiency.

In terms of TCR and ECR experimental measurements, the steadystate method stands as a well-established technique for assessing bulk materials [37–40]. Misra et al. [41] measured ECR and TCR in brassbrass contacts under vacuum conditions, different pressures and average interfacial temperatures. Karthick et al. [42] empirically demonstrated that the TCR can be effectively reduced by enhancing surface smoothness, applying pressure between contacting surfaces, and using thermal interface materials (TIMs). Li et al. [43] found that when the TEG system was used at high heat source temperatures, large pressure loads, and with thermally conductive grease as the interfacing material, it provided better performance at relatively low TCR and ECR. In the authors’ previous work [44], a platform is developed to indirectly measure the interfacial contact effects of individual TE couple. However, the experimental measurement of the TE transfer and conversion performance of the TEG is still limited.

In this paper, novel TEG is designed to collect aerodynamic heat from a high-speed flight vehicle and its performance is evaluated under typical aerodynamic conditions of the vehicle. During the design process, the load-bear function of the TEG is also taken into account, keeping the internal structure. The TEG consists of a force-bearing frame, twenty-seven couples of cylindrical TE legs, fifty-four couples of electrodes, two substrates, an insulation layer and two types of heterogeneous interfaces. The surface topography of TE legs and electrodes are reconstructed based on the contact-type measurement and W-M methodology. Numerical models of TCRs and ECRs are established and validated by in-direct experimental measurements, and the influences of pressure, temperature and clearance medium are clarified. Based on the influence of micro-scale TCR, the TE transfer and conversion process of the TEG is also simulated. The TE and mechanical performances under the vehicle’s typical aerodynamic conditions are numerically and experimentally evaluated.

## 2. The TEG design and preparation

## 2.1. The TEG with multi-interfaces

Fig. 1 illustrates the schematic diagram of the TEG designed for a high-speed flight vehicle. The research object of the aircraft has three levels of compression surfaces. The compression surfaces are in direct contact with the high-speed airflow, generating the airflow compression and therefore encountering harsh aerodynamic heat and force effects. In this work, the TEG is applied to the compression surfaces to harvest such large amount of aerodynamic heat. As depicted in the left part of Fig. 1, the TEG consists of a force-bearing frame, twenty-seven couples of cylindrical TE legs, fifty-four couples of electrodes, two substrates, an insulation layer and two types of heterogeneous interfaces. The forcebearing frame is used to contain the structure and bear external loads to prevent damage to the TEG. Between the upper and lower substrates, twenty-seven couples of cylindrical TE legs and fifty-four couples of electrodes (including upper and lower electrodes) are designed. The insulation layer is used to block the lateral conduction of the heat flow and to maintain one-dimensional heat transfer between the hot and cold sides of the TE legs. The structure is connected in series in the form of “N TE leg − electrode − P TE leg − electrode − N TE leg − ” to form a closed electrical circuitry. The main reason we design cylindrical TE legs instead of common square ones is that round cross-section can effectively avoid stress concentration and prevent excessive local stress from damaging the TE legs, while common square shaped TE legs generally have the problem of excessive local stress at the same loading pressure [45,46]. Moreover, cylindrical TE legs are easier to manufacture than common square shaped TE legs. As depicted in the right part of Fig. 1, the two types of heterogeneous interfaces refer to the contact between N-type TE legs and electrodes, and the contact between P-type TE legs and electrodes. The temperature difference and voltage are naturally generated when the aerodynamic heat is transferred through the TE legs, and if an external resistance is connected, an electrical flow with consistent direction can be generated. However, the clearances of interfaces influence the TE transfer and conversion processes, which are in essence due to the shrinkage effect of electrical and heat flow. When the clearance medium is vacuum or air, the heat is transferred by solid conduction in the real contact area and thermal radiation across the clearance, while the electrical flow is only conducted through the solid real contact area. However, when a high-thermal conductivity medium such as the silver-epoxy adhesive is used, the shrinkage effect and the resistances of electrical and heat flow in the clearance will be significantly reduced.

Fig. 2 illustrates the schematic diagram of the TEG and its components. The left and right parts of Fig. 2 depict the explosive and assembly views of the TEG, respectively. The TEG components include a forcebearing frame, twenty-seven couples of cylindrical TE legs, a polyether-ether-ketone (PEEK) insulation layer, a cover plate, the upper and lower integrated electrode substrates, and the upper and lower equivalent interfacial layers. To accurately study the contact effects between TE legs and electrodes and to prevent the influence of contact effects between other interfaces, the electrodes are fixed directly to the substrate. It means that the upper electrode and upper substrate are fabricated as a single unit, the lower electrode and lower substrate are fabricated as a single unit. The equivalent interfacial layers are hypothetical interfaces, as described later in Section 3.3. The envelope dimensions of the TEG and TE legs are about 86 × 60 × 16 mm and ϕ 5 × 10 mm, respectively. The thickness of the integrated electrode substrates is 1 mm. Several threaded holes around the perimeter of the forcebearing frame are used for secure fastening. In addition, two rectangular $5 \times 3$ mm holes are drilled in the force-bearing frame for the connection of measurement system. The materials of the force-bearing frame, N- and P-type TE legs, electrodes, substrates, insulation layer and cover plate are titanium alloy TC4, Pb0.55Te0.45 and PbTe, copper, alumina ceramics, poly-ether-ether-ketone (PEEK) and titanium alloy TC4, respectively. The $\mathrm{Pb} _ {0.55} \mathrm{Te} _ {0.45} ,$ PbTe, copper, alumina ceramics, and PEEK are purchased, and Table 1 list the vendor of related materials. The $\mathrm{Pb} _ {0.55} \mathrm{Te} _ {0.45}$ and PbTe are both bismuth telluride-based TE materials, which modulate the number of majority carriers through the ratios of the components to form N- and P-type TE materials. The bismuth telluride-based TE materials work in the temperature range of about 300 to 800 K. The copper has excellent thermal and electrical conductivity, and work below the melting point of 1358 K. The purchased alumina ceramics are 96 % pure and have excellent high-temperature stability and can withstand extremely high temperatures (below about 1270 K) without structural damage or deformation. The PEEK has excellent impact, flame and heat resistance. The titanium alloy TC4 has excellent comprehensive performance, stable metallographic organization, excellent plasticity and high temperature deformation resistance, and the it works at temperatures not exceeding about 700 K. Since the forcebearing frame is in contact with the heat source, the temperature of the TEG is below about 700 K. Table 2 lists the thermal and mechanical properties of these materials, while Table 3 lists the Seebeck coefficient, thermal conductivity, and electrical conductivity of the TE materials (measurement details can be found in the authors’ previous work [27]).

## 2.2. Fabrication and assembly of TEGs

Fig. 3 illustrates the fabrication and assembly process of the TEG, and six steps are involved: step 1, the fabrication of force-bearing frame and the lower integrated electrode substrate; step 2, the PEEK insulation layer is located on the lower integrated electrode substrate and fixed to the force-bearing frame with screws, with a gap between the upper integrated electrode; step 3, the N- and P-type TE legs are inserted into the PEEK holes in couples and contact with the electrodes on the lower substrate with coated silver-epoxy adhesive; step 4, the silver-epoxy adhesive is coated at the other end of the TE legs; step 5, the upper integrated electrode substrate is placed on the TE leg, and it is crucial to ensure that the TE legs are aligned with the electrodes in such step; step $^ {6 ,}$ the cover plate is placed on the upper integrated electrode substrate and fixed to the force-bearing frame by screws. During the above processes, the silver-epoxy adhesive should be heated and cured at about 423 K for 30 min to obtain certain viscous properties, thus the assembly process of the TEG is carried out on the heated platform, which needs to be heated during steps 3 and 5.

## 2.3. Rough surfaces measurement and reconstruction

The contacting interfaces between TE legs and electrodes will influence the TE transfer and conversion process. The accurate description of rough surfaces is essential to the evaluation of such contact effects. In this work, the TEG consists of twenty-seven TE couples, and totally 108 surfaces of TE legs and 108 surfaces of electrodes need to be measured with unaffordable cost. Thus, the fractal W-M function with certain experimental confirmation is adopted to characterize the surface topography. The W-M fractal method can effectively capture the geometric self-similarity and self-affinity of rough surfaces, allowing similar surface topography to be observed at different magnifications, regardless of spatial scale, and are commonly employed for rough surface reconstructions.

A three-dimensional fractal surface topography can be generated using the W-M fractal function [47,48]:

$$\begin{array} {c} {{\displaystyle z ( x , y ) = L _ {0} ( \frac {G} {L _ {0}} ) ^ {D _ {f} - 2} \cdot ( \frac {\ln \gamma _ {0}} {M} ) ^ {1 / 2} \cdot \sum _ {m = 1} ^ {M} \sum _ {n = 0} ^ {n _ {\mathrm{max}}} \gamma ^ {( D _ {f} - 3 ) n}}} \\ {{\displaystyle \times \left\{\cos \varphi _ {m , n} - \cos \left\{\frac {2 \pi \gamma _ {0} ^ {n} ( x ^ {2} + y ^ {2} ) ^ {1 / 2} )} {L _ {0}} \cdot \cos [ \tan ^ {- 1} ( \frac {y} {x} ) - \frac {\pi m} {M} ] + \varphi _ {m , n} \right\} \right\}}} \end{array}\tag{1}$$

where $D _ {f} ( 2 < D _ {f} < 3 )$ is the fractal dimension of the profile, and determines the contribution of high and low frequency components; $\vartheta ( \vartheta =$ 1.5) is a scaling parameter; $\varphi _ {m , n} ( 0 < \varphi _ {m , n} < 2 \pi )$ is a random phase. The fractal dimension is a key parameter for characterizing the topography of rough surfaces.

Fig. 4 illustrates the measurement and reconstruction of rough surfaces. As shown in the left part of Fig. 4, the surface characteristics of both the TE legs and electrodes are measured using a surface profilometer (TR 200 with resolution of 0.01 μm). The roughness mean absolute deviation (Ra) of the electrodes and TE legs is 3.215 and 1.799 μm, respectively. It is difficult to construct all 108 surfaces due to the large number of surfaces, and the N- and P-type TE legs are fabricated in the same batch using the same machining methods, so TE legs are constructed with approximately constant roughness. The electrode surface point set $( D _ {f} = 2.16 , L _ {0} = 90 \mu \mathrm{m} )$ and the TE leg surface point set $( D _ {f} = 2.2 , L _ {0} = 90 ~ \mu \mathrm{m} )$ are generated by W-M function with consideration of the measured statistics. Then, 7854 sampling points with spacing of 50 µm are collected from the point set for TE leg and electrode according to their real configurations (circular areas of 5 mm in diameter). Finally, the coordinates of sampling points are imported into CATIA to reconstruct the rough surfaces. As shown in the right part of Fig. 4, the roughness of the surfaces leads to the clearance presence between the contacting interfaces and lead to heterogeneous interfacial contact effects.

(a) Contacting pairs

(b) TEG and its components

## 3. Two-scale TEG evaluation model

The evaluation of TEG performance consists of two processes: microscale contact effects calculation and macro-scale performance analysis. The evaluation of contact effects consists of three processes: contact deformation, heat transfer and electrical conduction.

## 3.1. Governing equations

The contact deformation is simulated using an elasto-plastic deformation model. In terms of the elastic contact deformation stage, the equilibrium, geometric and constitutive equations are Eqs. (2), (3) and (4), respectively. In terms of the contact deformation plastic stage, the equilibrium, geometric and constitutive equations are Eqs. (2), (3) and (5), respectively. The correlation between stress and body force satisfies the equilibrium equation as Eq. (2):

(a) Meshed model of the fuselage

(b) Temperature distribution of the fuselage

(c) Pressure distribution of compression surfaces

(d) Temperature distribution of compression surfaces

$$\cfrac {\partial \sigma _ {x}} {\partial x} + \cfrac {\partial \tau _ {y x}} {\partial y} + \cfrac {\partial \tau _ {z x}} {\partial z} + f _ {x} = 0$$

$$\frac {\partial \tau _ {x y}} {\partial x} + \frac {\partial \sigma _ {y}} {\partial y} + \frac {\partial \tau _ {z y}} {\partial z} + f _ {y} = 0\tag{2}$$

$$\frac {\partial \tau _ {x z}} {\partial x} + \frac {\partial \tau _ {y z}} {\partial y} + \frac {\partial \sigma _ {z}} {\partial z} + f _ {z} = 0\tag{3}$$

where $\sigma _ {i} ( i = x , y , z )$ is the normal stress; $\tau _ {i j}$ is the shear stress. The correlation between strain and displacement satisfies the geometric equation as Eq. (3):

$$\begin{array} {c} {\displaystyle \varepsilon _ {x} = \frac {\partial u} {\partial x} ; \varepsilon _ {y} = \frac {\partial \nu} {\partial y} ; \varepsilon _ {z} = \frac {\partial w} {\partial z}} \\ {\displaystyle \gamma _ {y z} = \frac {\partial \nu} {\partial z} + \frac {\partial w} {\partial y} ; \gamma _ {x z} = \frac {\partial u} {\partial z} + \frac {\partial w} {\partial x} ; \gamma _ {x y} = \frac {\partial u} {\partial y} + \frac {\partial \nu} {\partial x}} \end{array}$$

where $\varepsilon _ {i} ( i = x , y , z )$ is the strain; $\gamma _ {i j}$ is the shear strain. The elastic and plastic stress–strain relation satisfies the constitutive equation as Eqs. (3) and (4), respectively.

$$d \sigma _ {i j} = D _ {i j k l} ^ {e} {\cdot} d \varepsilon _ {k l} ^ {e}\tag{4}$$

$$d \sigma _ {i j} = D _ {i j k l} ^ {e p} \cdot d \varepsilon _ {k l} = ( D _ {i j k l} ^ {e} - D _ {i j k l} ^ {p} ) d \varepsilon _ {k l}\tag{5}$$

where $\varepsilon _ {k l} ^ {e}$ is the elastic strain; $D _ {i j k l} ^ {e}$ is the elasticity matrix; where $D _ {i j k l} ^ {e}$ is the elasticity matrix; $D _ {i j k l} ^ {p}$ is the plasticity matrix.

Seebeck effect as shown in $\operatorname{Eq.} \ ( 7 )$ , and the thermoelectric coupling analysis is realized by these terms.

The energy and electrical potential equations are shown in Eqs. (6) and (7), respectively. The source term of the energy equation for TE materials are the Joule heating and Peltie effect as shown in Eq. (6), while that of the electric potential equation for TE materials is the

$$\frac {\partial ( \rho T )} {\partial t} = d i \nu ( \frac {\lambda} {c _ {p}} g r a d T ) + ( j \psi + j ^ {2} / k )\tag{6}$$

$$\frac {\partial ( \rho U )} {\partial t} = d i \nu ( \frac {k} {\varepsilon} g r a d U ) + k S \Delta T\tag{7}$$

where t is the time; ψ is the Peltier coefficient, equaling to Seebeck coefficient multiplied by the absolute temperature.

## 3.2. Calculation method of TCR and ECR

The TCR can be calculated by Eq. (8):

$$\mathrm{TCR} = \frac {\Delta T} {q _ {c} + q _ {r}} = \sum _ {i = 1} ^ {n} \frac {1} {h _ {i}}\tag{8}$$

where $\Delta T$ is the average temperature difference of two contact interfaces; $q _ {c}$ is the heat flux of solid conduction; $q _ {r}$ is the heat flux of thermal radiation; where $h _ {i}$ is the thermal contact conductance (TCC) of each contact element defined by Eq. (9):

$$h _ {i} = \left\{\begin{array} {c} {{h _ {c c} ( d _ {i} = 0 )}} \\ {{h _ {m c} + h _ {r} ( d _ {i} \neq 0 )}} \end{array} \right.\tag{9}$$

where $d _ {i}$ is the distance of the corresponding real contact elements; where $h _ {c c}$ is the TCC for the real contact elements; $h _ {m c}$ is the TCC of clearance medium for the non-contact elements; and $h _ {r}$ is the TCC of equivalent thermal conductance for thermal radiation. In this study, the TCC for the real contact elements is assumed to be perfect and given as 1 $\times ~ 10 ^ {10} ~ \mathrm {W / ( m ^ {2} {\cdot} K )}$ . For the non-contact elements, $h _ {m c}$ equals to 0 when the clearance medium is vacuum and equal to the thermal conductivity divided by the clearance distance when the medium is air or silver-epoxy adhesive. The equivalent thermal conductance of thermal radiation in different temperature can be calculated by Eq. (10):

(a) Contacting pairs

$$h _ {r} ^ {T} = \frac {q _ {r} ^ {T}} {\left( T + \Delta T \right) - \left( T - \Delta T \right)} = q _ {r} ^ {T}\tag{10}$$

Eq. (10) shows that the equivalent thermal conductance for the thermal radiation from A (source surface) to B (target surface) at T, equals to the heat flux of the thermal radiation.

The ECR can be calculated by Eq. (11):

$$\mathrm{ECR} = {\frac {\Delta U} {j}}\tag{11}$$

where $\Delta U$ is the average electric potential difference of two contact interface.

## 3.3. Equivalent interfacial layers in TEG

As shown in Fig. 2, red markers indicate the upper and lower equivalent interfacial layers in the TEG. The equivalent interfacial layer can be used to simulate the contact effects of heterogeneous interfaces as a substitute of the micro-scale rough surface model with great computational complexity. These equivalent interfacial layers are assumed to be between the electrodes and TE legs, and have the same cross-sectional shape as the electrode with a thickness of 0.5 mm. The equivalent thermal and electrical conductivities can be calculated by Eqs. (12) and (13), respectively.

$$\lambda _ {e q} = \frac {d _ {e q}} {\mathrm{TCR}}\tag{12}$$

$$k _ {e q} = \frac {d _ {e q}} {\mathrm{ECR}}\tag{13}$$

where $d _ {e q}$ is the thickness of equivalent interfacial layer.

Table 4 lists the equivalent thermal and electrical conductivities of contacting pairs at 0.1 MPa which corresponding to TCR and ECR at 0.14 MPa, and the pressure ratio keeps consistent with the crosssectional area ratio of TE legs and TEG. The equivalent thermal conductivity changes from 0.6719 to 14.68 W/(m⋅K) under air clearance, from 14.10 to 16.46 W/(m⋅K) under the silver-epoxy adhesive clearance. The equivalent electrical conductivity varies from 2.760 to 4.945 S/mm under air clearance, from 269.9 to 625.5 S/mm under the silver-epoxy adhesive clearance. It can be seen that the silver-epoxy adhesive clearance can substantially increase the equivalent thermal and electrical conductivities.

## 3.4. Meshed models

Fig. 5(a) and (b) are the meshed models of contacting pairs and TEG, respectively. In this work, hexahedral elements are maximized while using an economic strategy that combines hexahedral elements with tetrahedral elements. As shown in Fig. 5(a), the rough regions of contacting pairs are meshed with tetrahedral elements, while the others are meshed with hexahedral elements to save computational cost. The contacting pairs model consists of 448,613 elements (378,693 tetrahedral elements and 69,920 hexahedral elements) and 160,153 nodes. As shown in Fig. 5(b), the TEG model consists of 232,036 hexahedral elements and 339,599 nodes: the force-bearing frame, PEEK, cover plate, upper integrated electrode substrate, lower integrated electrode substrate, upper equivalent interfacial layer, lower equivalent interfacial layer, and TE leg consist of 31,400 elements and 46,103 nodes, 37,256 elements and 48,141 nodes, 35,950 elements and 54,795 nodes, 22,772 elements and 38,648 nodes, 22,814 elements and 38,716 nodes, 4844 elements and 11,528 nodes, 4988 elements and 11,812 nodes, and 72,012 elements and 89,856 nodes, respectively. In the analyses of contact mechanics, heat transfer, and electrical conduction of contacting pairs, the tetrahedral and hexahedral element types are C3D4 and C3D8R for “3D Stress”, DC3D4 and DC3D8 for “Heat transfer”, and DC3D4E and DC3D8E for “Thermoelectric”, respectively. In the thermomechanical coupling analysis of TEG, the element type is C3D8T for “Thermo-mechanical coupling”. The rough topological surface mesh model constructed based on the contact-type measurement and W-M function, also shown as Fig. 5(a), is referred to as a micro-scale interface model. Correspondingly, Fig. 5(b) employs the equivalent model in which there are no rough surface features and the rough surfaces are replaced by the equivalent interfacial layers in TEG. The micro-scale interface model simulates the topography of rough surfaces, which is necessary when calculating TCR and ECR accurately. But when calculating TEG performance, the micro-scale interface model wastes a huge amount of computational effort due to the large number of interfaces (one hundred and eight interfaces in the TEG in this paper).

## 3.5. Boundary conditions

In this work, the real aerodynamic conditions are considered to evaluate the TE performance. The commercial software Fluent is adopted to calculate the temperature and pressure. Fig. 6(a), (b), (c) and (d) show the meshed model of the fuselage, the temperature distribution of the fuselage, the pressure distribution of compression surfaces, and the temperature distribution of compression surfaces respectively. Three typical cruising conditions (speeds of 3 Ma at 15 km, 4 Ma at 20 km, and 5 Ma at 22 km) are selected for the TEG design and performance analyses. As shown in Fig. 6(a), the fuselage consists of about 1.35 million structured grids, and the first boundary layer lies within the logarithmic rate layer $( 30 < \mathbf {y} + < 300 )$ . The computational conditions and assumptions in the analysis are as follows: aerodynamic and surface temperature distribution are calculated under density-based and steady-state conditions; the governing equations are the Reynolds-averaged Navier-Stokes equation; the airflow is treated as an ideal gas; the molecular viscosity is calculated by the density-based formulations; the turbulent flow is modeled using SST k-ω model; the second-order upwind scheme is adopted; the surfaces are set to be adiabatic and non-slip. As shown in

Fig. 6(b),(c) and (d), when the vehicle cruises at 15 km altitude with speed of 3 Ma, 20 km altitude with speed of 4 Ma, and 22 km altitude with speed of 5 Ma, the fuselage temperature mainly ranges from about 550 to 570 K, 860 to 880 K, and 1260 to 1300 K, respectively; the pressure on the compression surfaces mainly ranges from about 15,000 to 40,000 Pa, 12,000 to 40,000 Pa, and 10,000 to 30,000 Pa, respectively; the temperature on the compression surfaces mainly ranges from about 560 to 580 K, 880 to 900 K, and 1300 to 1350 K, respectively. The upper temperature limit of the TEG is about 700 K as discussed in Section 2.1, so in this work, a thermal insulation layer (Saffil alumina fiber material) with a thickness of 0.84 mm is added between the TEG and the compression surface skin.

Fig. 7 illustrates the boundary conditions of contacting pairs and TEG. As shown in Fig. 7(a), RP denotes a reference point located on surface P1, and an “MPC beam” constraint is established between RP and surface P1. The side surfaces of the contacting pair are defined as surface P3. In the contact mechanics simulation, specified displacement w is applied on surface P1. In addition, the specified displacements u and v of P1 & P3, as well as $u ,$ v and w of P2, are constrained to be 0. In the heat transfer simulation, specified temperatures T1 and T2 are applied on surfaces P1 and P2, respectively, while surface P3 remains adiabatic. In the electrical conduction simulation, specified electrical potential U1 and U2 are applied on surfaces P1 and $P 2 ,$ respectively, while surface P3 remains insulative. Table 5 lists the specific values of the above boundary conditions. Due to the limited temperature range (<800 K) of TE legs as discussed in Section 2.1, the T1 ranges is assumed to be from 400 to 800 K. As shown in Fig. 7(b), specified temperatures $T _ {0} 1$ and $T _ {0} 2$ are applied on surfaces $P _ {0} 1$ and $P _ {0} 2$ & $P _ {0} 3 ,$ , respectively, while other surfaces are adiabatic. Specified loading pressure F is applied on surface $P _ {0} 1$ . Table 6 lists the specific values of the above boundary conditions of TEG. Due to the limited temperature range (<700 K) of force-bearing frame as discussed in Section 2.1, the $T _ {0} 1$ is assumed to be from 400 to 700 K. The $P _ {0} 1$ is assumed to be from 0.01 to 0.1 MPa to satisfy the pressure on the compression surfaces.

## 4. Experimental platform and models’ validation

## 4.1. TCR measurements under different pressure and temperature

Fig. 8 shows the experimental measurements of TCR. The measurement platform mainly consists of a microcomputer heater, a loading device, a heat flux meter based on stainless-steel block, a water-cooled heat exchanger and a data acquisition system. These components accordingly provide the heat source, loading pressure, heat flux measurement, heat sink, data acquisition. The heat flux can be calculated by one-dimensional steady heat transfer process of the stainless-steel block

(a) Vacuum clearance

(b) Air clearance 
(c) Silver-epoxy adhesive clearance.

as Eq. (14):

$$q = \lambda g r a d T\tag{14}$$

where gradT is the gradient of the stainless-steel block, respectively. The test sample consists of substrates, PEEK, electrodes and TE legs (N- and P-type TE legs). The electrode is drilled with a circular hole for collecting voltage and temperature signals. The data acquisition system includes a multi-channel temperature collector and a digital multimeter. A total of $^ {7}$ temperature channels and 2 voltage channels are used: channels 1 and 2 are used to measure the electrode temperature; channels 2 to 5 are used to monitor the temperature of the stainless-steel block. When collecting the voltage signal, the two probes of the digital multimeter are inserted into the round holes at the upper and lower electrodes. The TCR between the electrodes and TE legs can be calculated based on the measured temperature and voltage signals. Detailed measurement method and accuracy analysis can be found in the authors’ previous work [17].

## 4.2. Power supply measurement of TEG

Fig. 9 shows the experimental measurements of TEG power supply. The test sample is TEG manufactured in Section 2.2, including a forcebearing frame, twenty-seven couples of cylindrical TE legs, a PEEK insulation layer, a cover plate, the upper and lower integrated electrode substrates. A total of 8 temperature channels and 2 voltage channels are used: channel 1 is used to measure the cold side temperature of the TEG; the average value of channel 2 and 3 is used as the hot side temperature of the TEG; channels 4 to 8 are used to monitor the temperature of the stainless-steel block. For the voltage signal acquisition, the two probes of the digital multimeter are inserted into the rectangular holes, and are in contact with the electrodes. The voltage signal obtained in the experiment represents the real output voltage of the TEG. The output power and the conversion efficiency can be calculated based on the measured voltage.

## 5. Results and discussions

## 5.1. Contact effects

## 5.1.1. Contact mechanics

Fig. 10 shows the dimensionless real contact area varied with the loading pressure. The numbers in the diagram denote the absolute values of compression displacements. As shown in Fig. 10, the dimensionless real contact area exhibits a positive correlation trend with the absolute value of the loading pressure. In terms of surface of $\dot {} N ,$ when the wc ranges from − $\phantom - 8.0 \times 10 ^ {- 3} \mathrm{to} - 10.0 \times 10 ^ {- 3}$ mm, the loading pressure and dimensionless real contact area changes from 0.8179 to 2.947 MPa and from 0.1624 % to 0.5250 %, respectively; as for the surface of $P ,$ when the $w _ {c}$ varies from $- 9.0 \times 10 ^ {- 3} \mathrm{t} 0-11.0 \times 10 ^ {- 3}$ mm, the loading pressure and dimensionless real contact area changes from 1.201 to 3.041 MPa and from 0.2647 % to 0.6148 %, respectively. The number of grids for the contacting pairs is independent of the dimensionless real contact area. The deviation of the dimensionless real contact area is less than 3.7 % when the number of grids is increased or decreased by 10 %. Fig. 11 shows the Mises stress distribution of rough surfaces for contacting pairs. The area of Mises stress significantly increases with the rising loading pressure, while Mises stress in the real contact region exhibits a slightly increasing trend. The average Mises stress for the surface of $N ,$ the surface of P and the surface of electrode at the maximum loading pressure is about 42.82, 57.82, and 150.1 MPa, respectively. The Mises stress at the maximum loading pressure is still within the elastic modulus of the materials.

## 5.1.2. Thermal and electrical contact resistances

Fig. 12 shows the TCRs between electrodes and TE legs. Fig. 12(a), (b) and (c) depict TCRs under vacuum, air and silver-epoxy adhesive clearance, respectively. The TCRs between electrodes and TE legs decrease with increasing loading pressure. Table 7 lists the variation of TCRs under vacuum, air and silver-epoxy adhesive clearance. The TCRs vary from $12.63 \times 10 ^ {- 4} \mathrm{~to~} 2.920 \times 10 ^ {- 4} \mathrm {~ ( K {\cdot} m ^ {2} ) / W}$ under vacuum clearance, $\mathrm {f r o m ~ 6.571 ~ \times ~ 10 ^ {- 4} ~ t o ~ 2.106 ~ \times ~ 10 ^ {- 4} ~ ( K {\cdot} m ^ {2} ) / W}$ under air clearance, and from $3.377 \times 10 ^ {- 5} \mathrm{to} 2.485 \times 10 ^ {- 5} ( \mathrm{K} {\cdot} \mathrm{m} ^ {2} ) / \mathrm{W}$ under the silver-epoxy adhesive clearance. It can be seen that TCRs change the most in vacuum clearance and the least in silver-epoxy adhesive clearance.

Fig. 13 shows the ECRs between electrodes and TE legs. Under the epoxy-silver and the air/vacuum clearance, the ECRs also decrease with increasing loading pressure, and show better linearity under the silverepoxy adhesive clearance. Table 8 lists the variation of ECRs under multiple clearance mediums. The ECRs vary from $1.720 \times {{10} ^ {- 8}}$ to 3.615 $\times 10 ^ {- 8} \Omega {\cdot} \mathrm{m} ^ {2}$ under air/vacuum clearance, from $8.151 \times 10 ^ {- 10}$ to 6.919 $\times 10 ^ {- 10} \Omega {\cdot} \mathrm{m} ^ {2}$ under the silver-epoxy adhesive clearance.

## 5.1.3. The comparison with experimental results

The TCRs of the “E-N” and $\mathrm {^ {66} E} P ^ {\prime}$ are measured at two loading pressure and two temperature boundaries. Table 9 lists the measured and numerically calculated TCRs. As shown in Table 9, the maximum differences $\mathrm {_ {d f}} \cdots \mathrm{E} - N ^ {\prime}$ and $\mathrm {^ {66}}$ are − 13.4 % and − 4.56 %, respectively. The maximum deviation within 15 % (compared to similar literature data accuracy) and the trend is reasonable, which indicates the numerical model is highly reliable. The positive sign for the difference indicates that the measured value exceeds the numerically calculated value and vice versa. The $T _ {E 1}$ and $T _ {E 2}$ represent the measured temperatures for the hot and cold sides of the samples, respectively.

The evaluation of ECR involves contact deformation and electrical conduction, and its process similar to TCE. The experimental validation of ECR has been realized by the authors in previous work [5], and experimental platform has been described in Section 3.2 of literature [5]. To further verify the accuracy of the ECR in this paper, we supplemented the rough surfaces of the electrode, N- and P-type TE legs based on the contact-type measurement and W-M function, and those Ra are 3.22, 10.09, and 19.41 μm, respectively. These surfaces are basically the same as those in literature [5]: the rough surface Ra values of the electrode, N- and P-type TE legs are 3.55, 10.16 and 20.23 μm, respectively. Table 10 shows two comparisons of the ECR with the experimental and numerical results from the literature [5], respectively. It shows that the maximum deviations are 15.1 % for experimental (i.e., difference I) and 4.92 % for simulation (i.e., difference II), respectively. The deviation of numerical simulations is smaller than that of experiments.

## 5.2. TEG performance

## 5.2.1. Validation of the equivalent interfacial layers

Fig. 14 illustrates the comparison between equivalent model and micro-scale interfacial model. The temperature difference of the TE legs can prove the validity of the equivalent model. If the two series of curves (Curves for micro-scale interfacial model and curves for equivalent model) are basically overlapped, then it can be shown that the microscale rough contact model can be replaced by the equivalent model. As shown in Fig. 14, the maximum deviation of temperature for the Nand P-type TE legs is about 2.53 K (with a deviation of 0.404 %) and about 2.88 K (with a deviation of 0.444 %), respectively. The temperature difference shown in Fig. 14 are for air clearance conditions. Under the silver-epoxy adhesive clearance, the maximum deviation of temperature for the N- and P-type TE legs is about 2.37 K (with a deviation of 0.299 %) and about 2.76 K (with a deviation of 0.347 %), respectively. The above analysis demonstrates the significant effectiveness of the equivalent model.

## 5.2.2. Thermo-mechanical performance

The TEG works under external thermo-mechanical coupling, thus Figs. 15 and 16 show the temperature and Mises stress distribution under different clearances, respectively. Fig. 15(a) and (b) show the temperature distribution of the contacting pairs and TE couples, respectively. The temperature gradient at the contact interface decreases with increasing loading pressure at the same clearance medium. The temperature gradient under vacuum clearance is considerably lower than that under air clearance and slightly lower than that under the silver-epoxy adhesive clearance. The above indicates that TCRs decrease in the following order: vacuum, air, and silver-epoxy adhesive clearance. Furthermore, the TCR decreases as the loading pressure increases. The temperature gradient of the TE couples under air clearance is also smaller than that under the silver-epoxy adhesive clearance.

Fig. 16 shows the Mises stress distribution for TEG and its components. Fig. 16(a), (b) and (c) display the Mises stress distribution of the TE couples, the force-bearing frame and the TE legs, respectively. The Mises stress increases with increasing loading pressure under the same clearance medium. The Mises stress of the TE couples and legs under the silver-epoxy adhesive clearance is less than that under air clearance. Under the silver-epoxy adhesive clearance, the local maximum stresses of the TE couples, force-bearing frame and TE legs are about 4.68, 7.88 and 1.93 MPa, respectively; under air clearance, the local maximum stresses the TE couples, force-bearing frame, and TE legs are about 3.49, 7.68 and 1.32 MPa. The above values are lower than the yield stress of the materials and therefore fulfill the force-bearing prerequisites. Furthermore, a high stress on one side of the TE couples can be observed, which results of slight asymmetries in the integrated electrode substrate in fabrication, and this stress can be reduced by the silver-epoxy adhesive clearance.

(b) Twenty-seven TE couples

## 5.2.3. TEG performance

Fig. 17and Fig. 18 shows the TEG performances of the voltage and output power, respectively. The voltage is positively correlated with the temperature, while the voltage increases slightly as the loading pressure increases from 0.01 MPa to 0.1 MPa. The output power which is proportional to the square of the voltage, shows a similar trend: a gradual increase with increasing temperature and a slight increase with increasing loading pressure. Table 11 lists the quantitative analysis results of the TEG performances of the voltage and output power. The TEG performance of the voltage varies from 0.9487 to 4.941 V under air clearance, and from 1.460 to 6.978 V under the silver-epoxy adhesive. Simultaneously, the output power changes from 0.2654 to 5.849 W under air clearance and from 0.650 to 12.41 W under the silver-epoxy adhesive.

Fig. 19 illustrates the TEG performance of the conversion efficiency. As shown in Fig. 19, the efficiencies of N-type TE legs, P-type TE legs and TEG increases with the temperature, and the loading pressure also enhances the efficiency. The efficiency of TEG lower than the efficiency of TE legs is mainly because the heat dissipation and contact effect caused by additional structures in TEG. Table 12 lists the quantitative analysis results of the TEG performance of the conversion efficiency. As shown in Table 12, when the hot side temperature increases from 400 to 700 K and cold side temperature keeps 300 K, the efficiencies of N-type TE legs,

P-type TE legs and TEG vary from 1.178 % to 6.431 %, 0.6438 % to 3.278 %, and 0.303 % to 1.643 % under air clearance. The silver-epoxy adhesive clearance can improve the performance, the efficiencies of Ntype TE legs, P-type TE legs and TEG change from 1.896 % to 9.330 %, 0.9313 % to 4.043 $^ {\% ,}$ and 0.478 % to 2.334 % under the silver-epoxy adhesive clearance.

## 5.2.4. The comparison with experimental results

The voltage performance of the TEG (under the silver-epoxy adhesive clearance) is measured. Table 13 lists the measured and numerically calculated voltages of TEG. The maximum differences between the measured and numerically calculated voltage are about − 19.69 % (at 0.01 MPa) and − 15.06 % (at 0.04 MPa), respectively. The measured voltages are lower than the numerically calculated values, which results from the imperfect connection of the multiple TE couples in the handmade samples as well as cumulative deviations in the equivalent model. The $T _ {S 1}$ and $T _ {S 2}$ represent the measured temperatures for the hot and cold sides of the TEG, respectively.

## 6. Conclusion

In this work, an aerodynamic-heat-harvest TEG is innovatively developed and evaluated based on the full consideration of the multiinterface contact effect. The TEG including a force-bearing frame, twenty-seven couples of cylindrical TE legs, fifty-four couples of electrodes, two substrates, an insulation layer and two types of heterogeneous interfaces is designed and fabricated. The TEG possess the heatharvest and force-bear functions simultaneously. The surface topography of TE legs and electrodes are reconstructed based on the contacttype measurement and W-M function, numerical models of thermal and electrical contact resistances are established and experimentally validated, and the influences of pressure, temperature and clearance medium are clarified. The performance of TEG considering micro-scale contact resistances is numerically and experimentally evaluated under the vehicle’s typical aerodynamic conditions. Some conclusions are obtained:

(a) Twenty-seven TE couples

(b) Force-bearing frame

(c) TE 1egs

(a) TE 1egs

(b) TEG

1. The TCR and ECR decrease with the increase of loading pressure and average temperature of the interfaces, and they are reduced by the presence of clearance medium. When the loading pressure varies from 0.8179 to 3.041 MPa, the TCR decreases from $12.63 \times {{10} ^ {- 4}}$ to $2.920 \times 10 ^ {- 4} , 6.571 \times 10 ^ {- 4} {\mathrm{to}} 2.106 \times 10 ^ {- 4}$ and $3.377 \times 10 ^ {- 5}$ to $2.485 \times 10 ^ {- 5} ( \mathrm{K} {\cdot} \mathrm{m} ^ {2} ) / \mathrm{W}$ under vacuum, air and silver-epoxy adhesive clearance, respectively; the ECR varies from $17.20 \times 10 ^ {- 8}$ to $4.348 \times 10 ^ {- 8} , 8.151 \times 10 ^ {- 10} \mathrm {{t o}} 6.919 \times 10 ^ {- 10} \mathrm {{\Omega}} \Omega {\cdot} \mathrm {{m}} ^ {2}$ under air/ vacuum and silver-epoxy adhesive clearance, respectively.

2. The TCR model is validated by indirect experimental measurements with the maximum deviation of 13.4 %.

3. The fabricated TEG has the ability to capture aerodynamic heat to generate power with the maximum voltage, output power and conversion efficiency are 6.978 V, 12.41 W and 2.334 %, respectively (at 0.1 MPa and under the silver-epoxy adhesive clearance).

4. The equivalent interfacial model can be used to evaluate the performance of the TEG under consideration of interfacial contact effects with a maximum model deviation of 0.444 %. The thermoelectric and mechanical performance are influenced by the loading pressure and the clearance medium, and the force-bearing frame has the highest Mises stress of 7.88 MPa under the silverepoxy adhesive clearance and 7.68 MPa under air clearance.

5. Experimental measurements validated the TEG evaluation model with a maximum deviation in output voltage of − 19.69 %.

## CRediT authorship contribution statement

Shi-Yuan Chen: Conceptualization, Data curation, Methodology, Software, Writing – original draft, Writing – review & editing. Hai-Peng Chen: Data curation, Validation. Ge Gao: Software, Data curation. Chun-Lin Gong: Conceptualization, Project administration, Supervision. Yang Wu: Investigation, Validation. Jian-Jun Gou: Conceptualization, Funding acquisition, Project administration, Writing – review & editing.

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
- [Table 12 omitted; saved to tables/table_012.md]
- [Table 13 omitted; saved to tables/table_013.md]
- [Table 14 omitted; saved to tables/table_014.md]
