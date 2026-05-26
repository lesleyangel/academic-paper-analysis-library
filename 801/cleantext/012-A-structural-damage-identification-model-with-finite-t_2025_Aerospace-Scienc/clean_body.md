## 1. Introduction

The re-entry environment of the re-entry module is extremely harsh with severe aerodynamic heating and deceleration overload due to the high flight velocity and drastic spacecraft deceleration. Subjected to such extreme environmental loads, the thermal and force structures will experience damages [1], performance degradation and even failures [2]. If minor damage couldn’t be detected in time and adopt effective countermeasures, the likelihood of a catastrophic space incident is significantly high. The 2003 Columbia disaster, resulting from fuel tank structural damage, was potentially preventable with timely anomaly detection and return strategy adjustment, which proved the significance of structural damage identification (SDI).

Structural damage identification is an essential online structural health management technology based on sensor system and evaluation algorithm [3]. It employs embedded sensor systems to comprehensively monitor the structural condition and perform damage detection, localization, and assessment in real-time. By applying structural damage identification, the structural damage state of re-entry module can be monitored in real-time. Then evaluate the structural capacity based on the damage status. Finally, according to structural status, adjust the mission strategy and re-entry trajectory dynamically to ensure safety to the greatest extent possible. Such technology provides the possibility to significantly reduce the maintenance costs and improve the security for future reusable vehicles [4]. Therefore, it’s crucial for the future development of intelligent aircraft. By applying structural damage identification to manned spacecraft, the re-entry module can monitor the spacecraft’s structural state. Based on the real-time structural capacity, the aircraft could dynamically adjust its mission strategy, control strategy [5] or re-entry trajectory to ensure a safe return of the spacecraft and improve the safety of manned space missions [6].

The structural damage is defined as changes in geometry (such as cracks, permanent deformation, etc.) and material properties including stiffness and etc. [7], which lead to changes in structural response (stress, strain, etc.) [8], structural modal parameters (mode shapes, frequencies, etc.) and dynamic structural response [9]. By analyzing the changes in structural response before and after damage, the location and extent of the damage can be determined SDI is generally divided into two categories including dynamic response-based monitoring methods and static response-based monitoring methods. The dynamic-response based monitoring method is theoretically based on the structural dynamics [10] and assess the damage situation by analyzing the structural modal parameters [11], which can be obtained from sensor data based on signal processing techniques [12] such as wavelet decomposition [13] to determine the location and extent of damage based on MAC [14], COMAC [15], curvature methods [16] and newly optimization provenance of whiplash compensation [17]. Although this type of method can monitor the entire structural state, its application is limited due to the susceptibility of the structural natural frequency to environmental interference, difficulty to obtain the high-order natural frequency that is sensitive to damage, and poor effect of multi-damage identification. The static response monitoring method is based on the theory of elastic mechanics to predict the type, site, and degree of material damage according to the changes in static structural response [18]. Compared with the modal parameters, static response provides lower computational cost and more physical insight into the damage assessment process [19], which presents a huge advantage. Milanoski et al. measured material stress changes using FBG and monitored the debonding development of composite components using the method of parametric analysis [20]. Chandra and Prakash and others predicted the location of bolt removal by analyzing the strain distribution of composite components [21]. However, neither study established a universal and efficient structural damage state identification process, which made it difficult to apply those methods in complex structural systems. Moreover, these methods only focus on the microscopic damage and cannot effectively evaluate the overall structural performance.

In recent years, based on a vast amount of monitoring data of damaged structure, the use of machine learning (ML) methods to analyze and extract data features for constructing damage identification models has become a mainstream development direction [22]. ML is favored by most researchers because of its excellent data learning and feature extraction ability. Sofi and others discussed the application of machine learning technologies in SHM, including BPNN, CNN, and others, and they indicated the advantages of processing structural health monitoring signals and extracting damage features [23]. Mainini and Willcox established a surrogate model to map the measured quantities and system capabilities by combining the POD method with the self-organizing mapping network, and they completed the verification on a simple plate-shaped wing model [24]. Yumei constructed a surrogate model based on dynamic Bayesian networks to deduce the parameter uncertainty of the crack growth theory, predicted the crack growth of I-steel, and fully demonstrated the great potential of machine learning technology in SHM [25]. Arcaro and others, based on Principal Component Analysis (PCA) and K-Nearest Neighbor (KNN), constructed a machine learning classifier to achieve long-term monitoring of spent nuclear fuel assemblies [26]. However, these studies on damage identification were only verified in simple plate and shell models. Due to the model complexity, these methods do not have ideal application effects in complex structures under complex and variable loads.

As a significant branch of ML, deep learning is widely used in image recognition, data feature extraction, and other aspects and has demonstrated its excellent processing ability for complex data [27]. Sadegh recognized structural damage by processing real-time monitoring images of structures based on deep CNN [28]. Guan et al. used CNN and the orthogonal array method to process aircraft engine endoscope images to recognize structural damage and segment damaged structures [29]. Singh et al. adopt the curve fitting based vision technology to monitor the flexible structures [30]. Computer vision technology has achieved good results in visible damage identification, but it remains insufficient in understanding the internal microscopic damages and overall capacity of the structure. Therefore, deep learning technology has begun to be applied in real-time monitoring sensor data processing to extract damage features to identify damages. Tang et al. processed acceleration signals with CNN and autoregressive models to identify and locate damages [31]. Zhang et al. combined Lamb waves and 1D-CNN for damage assessment of honeycomb sandwich structures, achieving simultaneous identification of the damage location and degree [32]. Shang et al. built three Mask R-CNN networks to evaluate and locate the structural damage of an aeroengine blade [33]. Lannelli et al. adopted a data-driven deep neural network to process modal parameters and identify damages of large on-orbit flexible structural systems [34]. In recent years, thanks to the development of deep learning technology, LSTM (Long Short-Term Memory) [35], Transformer [36], PINN (Physics-Informed Neural Networks) have gradually been applied to structural damage identification. Inspired by computer vision technology and the development of grating fiber technology, the U-Net method has also achieved good identification results [37]. Timothy Sands proposed deterministic artificial intelligence [38], an advanced technology of artificial intelligence, which has been applied to control of underwater vehicle [39] and satellite [40]. Deterministic artificial intelligence has adaptive learning ability, which makes it have potential application in SDI. At same time, traditional artificial intelligence technology requires a large amount of data support to implement, and the acquisition of a large amount of damage data has always been a difficult issue. Currently, damage data can only be obtained through numerical simulation methods, which consume significant computational resources and time, making it challenging to obtain enough damage data in a short period. Insufficient training samples will lead to serious overfitting problems and result in poor generalization ability. Therefore, addressing the issue of damage data acquisition is key to the application of deep learning technology in damage identification.

In summary, this work presents a data-driven method to rapidly identify the damaged state of structure for the re-entry module. The digital model of the re-entry module was constructed based on the Orion spacecraft. The structural damage model was proposed based on the stiffness loss method. With the Kriging proxy model, the data expansion process was constructed, which provided a large amount of trusted damage data for model training to improve the identification and generalization ability of the model. The damage structure state identification model was established based on the neural network method, which could recognize and estimate the structure state by the force-heat sensors at a low cost. In addition, the entire process of structure diagnosis was built, by which the re-entry module can obtain the damage classification. Finally, this work used the digital model of the re-entry module as an example to verify the effectiveness of the method.

## 2. Re-entry module and structural damage model

In this section, taking the Orion spacecraft of the United States as a reference, the CAD model of the structure of the re-entry module is constructed, along with its return trajectory. Based on the stiffness loss method, the damage model of the re-entry module was put forward to offer basic model support for the construction of the database.

Fig. 1 shows the return trajectory of the re-entry module. The reentry module returns from the orbit at altitudes of 270 km. During the return phase, the flight velocity undergoes a rapid deceleration from 4000 m/s to approximately 200 m/s. During the return phase, the flight velocity undergoes a rapid deceleration from 4000 m/s to approximately 200 m/s. The aerodynamic heating effect is weak and the aerodynamic force is small due to the extremely thin atmosphere above 80 km. In the airspace below 20 km, the re-entry module flies at a slow velocity, which weakens the aerodynamic heating effect. Therefore, the phase when the re-entry module flies at an altitude of 80–20 km is the most severe stage during re-entry and return. During this phase, the atmospheric density undergoes a sharp increase at an extremely high velocity, leading to significant aerodynamic heating. In addition, the deceleration of the reentry module is much more severe at this stage, which causes serious deceleration overload. Consequently, this study focuses on the flight status of the re-entry module within the altitude range of 80–20 km (Fig. 2) as the primary research context.

Then, this work constructs the structure system of the re-entry module. As illustrated in Fig. 3, the structural system of the re-entry module comprises two primary components: a heat-proof shell and an internal cabin. The heat-proof shell determines the aerodynamic characteristics of the re-entry module during the re-entry process while blocking heat from entering the interior of the re-entry module. It is a body of revolution with a 72-degree generatrix, a height of 3.2 m, and a radius of 2.2–1.25 m. Components such as doors and portholes are ignored. The thickness of the shell is 40 mm, which is smaller than the overall scale. To ensure the convergence of calculation, the heat-proof shell is simplified into a shell in the modeling. The internal cabin is the main load-bearing component, which is composed of a pressure chamber, a lower rib plate, a stiffener, and an upper rib plate. To facilitate subsequent damage settings, this work divides the re-entry module into five compartments according to their structure and function for subsequent damage settings. As shown in Fig. 2(b), distinct colors were used for distinguishing between these zones, for more intuitive representation.

In order to obtain the structural response of the re-entry module in real time and provide measurement data for structural health monitoring and damage identification, thirty groups of force–temperature sensors are arranged in the internal cabin, as illustrated by the pentagon in Fig. 2. Regarding the sensor, this article did not consider the actual type of sensor and acquisition method of sensors, and with making the following assumptions (1)the strain and temperature at certain location are assumed to be simultaneously obtained, and the fiber optic sensors can be adopted to obtain the strain and temperature at the same time, or strain gage and thermal couples can be adopted to measure strain and temperature, respectively. (2) a parameter, i.e., random noise is used to indicate the measurement errors, data transmission errors, signal interference, etc. of sensors. For the placement, the sensors are mainly evenly arranged in the interior structure of the re-entry module, and according to the structural response, additional sensors are placed at the crucial part with stress concentration. Finally, the arrangement of sensors is as follows: Sensor 1 to Sensor 6 in Area 5, Sensor 7 to Sensor 14 in Area 4, Sensor 15 to Sensor 18 in Area 1, Sensor 19 to Sensor 22 in Area 2 and Sensor 23 to Sensor 30 in Area 3.

The stiffness loss method is a type of damage characterization method. As posited by the aforementioned method, a wide variety of structural damage can be characterized by a decline in material stiffness. This method is founded on the strain equivalence hypothesis [41] and has simple implementation and wide practicability. This hypothesis holds that the deformation caused by the stress on the damaged material is equivalent to the deformation on a virtual lossless material. In other words, the bearing area of the virtual lossless material is equal to the actual effective bearing area of the damaged material, which can be described by Eq. (1):

$$\varepsilon = \frac {\sigma} {\overline {{E}}} = \frac {\overline {{\sigma}}} {E}\tag{1}$$

where σ is the nominal stress on the cross section, σ is the stress on the effective bearing area of the virtual lossless material, E is the elastic modulus of material without damage, and E is the elastic modulus of the damaged material.

Damage variable λ is shown in Eq. (2):

$$\lambda = 1 - \frac {A} {A _ {0}}\tag{2}$$

where $A _ {0}$ is the initial bearing cross-sectional area of the material, and A is the effective bearing area of the damaged material. According to the definition of stress, Eq. (3) can be obtained:

$${\overline {{\sigma}}} = {\frac {\sigma} {1 - \lambda}}\tag{3}$$

Eq. (4) can be obtained by substituting Eq. (3) into Eq. (1):

$$\lambda = 1 - {\frac {\overline {{E}}} {E}}\tag{4}$$

As Eq. (4) shows, when the material is not damaged, the elastic modulus remains unchanged, i.e., λ=0. When the material is completely damaged, λ = 1. This method of characterizing material damage is the stiffness loss method. This work extends this method to the partitioned stiffness reduction method, where the structure is divided into multiple partitions, and the stiffness loss is set for each partition using the stiffness reduction method to simulate various types of material damage at different positions of the structure. Assuming that the re-entry module is divided into m blocks, elastic modulus vector E of the spacecraft can be obtained using Eq. (5):

$$\mathbf {E} = [ e _ {1} , . . . , e _ {m} ]\tag{5}$$

where $e _ {i}$ is the real-time elastic modulus of block i. ${\pmb E} _ {0}$ is the elastic modulus vector of the re-entry module without damage, and $e _ {i 0}$ is the elastic modulus of the ith block without damage.

The damage variable vector of the re-entry module is defined by Eq. (6):

$$\Lambda = [ \lambda _ {1} , . . . , \lambda _ {m} ]\tag{6}$$

where $\lambda _ {i}$ is the damage variable (the following are collectively referred to as damage values) of the ith area. There is $\lambda _ {i} \in [ 0 , l o s s _ {\operatorname* {m a x}} ]$ , where lossmax does not exceed 1 and is the maximum structural damage, while the flight capability can be maintained. The value can be set according to the actual situation of different areas.

In summary, the elastic modulus vector under damage to the re-entry module can be obtained using Eq. (7):

$$\mathbf {E} = \mathbf {E _ {0}} \cdot ( 1 - \Lambda ) ^ {T} = \left[ e _ {10} ( 1 - \lambda _ {1} ) , . . . , e _ {m 0} ( 1 - \lambda _ {m} ) \right]\tag{7}$$

Finally, block residual capability θiand structural residual capability vector L are defined in Eq. (8):

$$\mathbf {L} = \mathbf {1} - \boldsymbol {\Lambda} = [ 1 - \lambda _ {1} , . . . , 1 - \lambda _ {m} ]\tag{8}$$

Number of damage variable vectors Λ are randomly generated and substituted into Eq. (7) to obtain structural stiffness vector E. Then, E is substituted into the finite element model to complete the simulation for the damage situation of the re-entry module and construct the damage database. After establishing the damage model, it can be integrated into the finite element model for simulation, so as to obtain the structural response and damage database after damage under the aerodynamic action. Therefore, the following will focus on how to obtain aerodynamic load data and how to conduct damage simulation.

## 3. Damage database and its expansion method

In this section, the damage simulation is conducted to build the damage database based on the constructed model. The damage simulation is comprised of two primary processes: aerodynamic calculation and heat-force coupling analysis. Initially, aerodynamic calculations are performed to obtain the force–thermal load. Subsequently, the finite element model is constructed, and heat-force coupling analysis is performed for the stress field distribution. The final step in this process is the establishment of a preliminary damage database. However, the aerodynamic calculation and heat-force coupling analysis require substantial computing resources and time, which limits the feasibility of obtaining sufficient damage data within a limited timeframe. To address this challenge, this study proposes a data enhancement method using a surrogate model, facilitating the acquisition of substantial damage data in a relatively short timeframe.

## 3.1. Aerodynamic calculation model

The primary objective of the aerodynamic calculation is to ascertain the aerodynamic heat-force load of the module as boundary conditions of the finite element method (FEM). The present work adopts the engineering algorithm (including modified newton method and reference temperature method) to calculate the aerodynamic heat and force of the re-entry module.

The engineering algorithm uses triangular or quadrilateral surface elements to disperse the shape of the aircraft, solves the pressure coefficient and heat flux of each surface element, and obtains the aerodynamic force and heat distribution of the aircraft through superposition and combination. The pressure coefficient of the windward element can be calculated based on the modified newton method, i.e., Eq. (9):

$$C _ {p} = C _ {p} ^ {*} \mathrm{sin} ^ {2} \theta\tag{9}$$

where θ is the angle between the tangential aspect and incoming flow direction; $C _ {p} ^ {*}$ is the pressure coefficient behind the stagnation point of the shock wave, which can be calculated by shock wave theory as shown in Eq. (10):

$$C _ {p} ^ {*} = \frac {2} {\gamma M a _ {\infty} ^ {2}} \left[ \left( \frac {\gamma + 1} {2} M a \right) ^ {\frac {\gamma} {\gamma - 1}} \frac {1} {\left( \frac {2 \lambda} {\gamma + 1} M a _ {\infty} ^ {2} - \frac {\gamma - 1} {\gamma + 1} \right) ^ {\frac {1} {\gamma - 1}}} - 1 \right]\tag{10}$$

The reference temperature method is used to calculate the heat flux. According to the reference temperature method, the aircraft surface temperature is determined by Eq. (11):

$$q _ {w} = \alpha ( T _ {r} - T _ {w} )\tag{11}$$

where $T _ {w}$ is the wall temperature; α is the heat exchange coefficient; $T _ {r}$ is the recovery temperature and can be calculated by Eq. (12):

$$T _ {r} = T _ {\infty} \left( 1 + \frac {\gamma - 1} {2} r M a ^ {2} \right)\tag{12}$$

where r is the temperature recovery coefficient, which is related to the boundary layer properties and Prandtl number (Pr). According to the correlation theory, $r = {\sqrt {P r}} \mathrm{for}$ the laminar flow, and $r = \sqrt [ 3 ] {P r}$ for the turbulent flow. The reference temperature can be calculated by an empirical formula:

$$T ^ {*} = T _ {e} + 0.5 ( T _ {w} - T _ {e} ) + 0.22 ( T _ {r} - T _ {e} )\tag{13}$$

where $T _ {e}$ is the airflow temperature at the outer edge of the boundary layer. Then The flow parameters in the boundary layer can be calculated based on the reference temperature. First, according to aerodynamics, the viscosity coefficient of the fluid can be calculated as shown in Eq. (14):

$$\mu ^ {*} = 1.46 \times 10 ^ {- 6} \frac {T ^ {* 1.5}} {T ^ {*} + 110}\tag{14}$$

Since the fluid pressure does not change along the boundary layer thickness, the density satisfies $\operatorname{Eq.}$ (15):

$$\rho ^ {*} = \rho _ {e} \frac {T _ {e}} {T ^ {*}}\tag{15}$$

Finally, the Reynolds number of the gas at the reference temperature is shown in Eq. (16):

$$R e ^ {*} = \frac {\rho ^ {*} \nu _ {e} x ^ {*}} {\mu ^ {*}}\tag{16}$$

where $x ^ {*}$ is the reference length, $x ^ {*} = x / 3$ for a laminar flow, and $x ^ {*} =$ $x / 2$ for a turbulent flow. The empirical formula of the transition Reynolds number can be calculated using Eq. (17):

$$R e _ {t r i} = 10 ^ {5.37 + 0.2326 M a - 0.004015 M a ^ {2}}\tag{17}$$

According to different Reynolds numbers, the heat exchange coefficient is calculated as shown in Eq. (18):

$$\begin{array} {l r} {\alpha = 0.332 R e ^ {* - 1.5} P r ^ {* - 1.5} \rho ^ {*} c _ {p} ^ {*} \nu _ {e}} & {\left( R e \leq R e _ {t r i} \right)} \\ {\alpha = 0.0296 R e ^ {* - 0.2} P r ^ {* - 1.5} \rho ^ {*} c _ {p} ^ {*} \nu _ {e}} & {\left( R e _ {t r i} < R e \leq 10 ^ {7} \right)} \\ {\alpha = 0.184 ( 1 g R e ^ {*} ) ^ {- 2.584} P r ^ {* - 1.5} \rho ^ {*} c _ {p} ^ {*} \nu _ {e}} & {\left( R e > 10 ^ {7} \right)} \end{array}\tag{18}$$

where Pr and $c _ {p} ^ {*}$ are related to the temperature, which can be obtained from a look-up table. Finally, the heat flux distribution can be obtained by substituting α, $T _ {r}$ and $T _ {w}$ into Eq. (11).

According to the established CAD model of the re-entry module, one can extract the heat-proof shell part and divide the surface grid. The surface element grid employs a 40-mm triangular mesh, and Fig. 4 illustrates the partitioning outcomes. The total number of mesh cells generated is 75,138.

As illustrated in Table 1, the final selection of calculation cases is presented. The calculation points have been judiciously selected based on the Mach number variation in the altitude range of 20 to 100 km. It is noteworthy that the majority of the calculated state points are concentrated within the interval of 40 to 20 km, a region characterized by a significant atmospheric density, substantial flight velocity, and substantial Mach number variation. At altitudes above 50 km, the atmosphere is considered thin, and the change in flight state is minimal. Consequently, the selection of calculation points is primarily based on changes in altitude and angle of attack.

The calculation results are illustrated by taking the flight conditions at altitudes of 27, 30, and 47 km as examples. Table 2 shows the flight status and environmental parameters, and Fig. 5 shows the calculation results.

When the air flow flows through the surface of the re-entry module at high speed, the air flow is strongly compressed and forms shock waves, which have the effect of aerodynamic heating. Simultaneously, the strong friction between air flow and object will produce a lot of heat. Consequently, the spacecraft’s kinetic energy is converted into heat. Notably, at the point of stasis, the relative velocity of the air flow is zero, leading to the most significant heating effect. At altitudes exceeding 30 km, the re-entry module operates at high speed. As altitude decreases, atmospheric density increases, intensifying aerodynamic heating and reaching a maximum near 30 km. Concurrently, the re-entry module’s flight velocity undergoes a proportional decrease, thereby allowing the aerodynamic heating phenomenon to subside.

The aerodynamic load obtained quickly by the surface element method can be approximated effectively to the flight environment conditions of the aircraft. The result will be loaded into the subsequent analysis model as the boundary condition of the heat-force load.

## 3.2. Structural heat-force coupling analysis model

After the aerodynamic load is obtained, the finite element analysis can be carried out using the aerodynamic load as the boundary condition. When the finite element method is used for mechanical and thermal coupling analysis, the sequential heat-force coupling analysis method is typically employed. First, the aerodynamic heat flux and pressure from the aerodynamic calculation is loaded into the finite element model through grid mapping to calculate the temperature field of the re-entry module, which is used as a predefined field in the structural finite element model. Then, the force and displacement boundary conditions are applied, and the calculation of the structural finite element model is completed. Finally, the stress field of the re-entry module under force-heat coupling is obtained.

## 3.2.1. Heat conduction analysis

The analysis of heat conduction is principally predicated on the differential equation of heat conduction, as illustrated in Eq. (19):

$$\frac {\partial} {\partial x} \left( k \frac {\partial T} {\partial x} \right) + \frac {\partial} {\partial y} \left( k \frac {\partial T} {\partial y} \right) + \frac {\partial} {\partial z} \left( k \frac {\partial T} {\partial z} \right) = 0\tag{19}$$

where k is the thermal conductivity.

Prior to the implementation of the finite element method (FEM) in the solution of the aforementioned heat-transfer equation, it is imperative to discretize the structural model using a grid and to construct the finite element model of heat conduction. The DS4 element was employed to subdivide the re-entry module structure, as illustrated in Fig. 6. The resulting mesh comprised 69,567 nodes and 70,781 grid cells.

The boundary conditions must be provided to solve the heat conduction problem. The aerodynamic heat flux is applied on the structural boundary (as shown in Eq. (20)):

$$- \kappa \bigg ( \frac {\partial T} {\partial n} \bigg ) _ {w a l l} = q ( x _ {w a l l} , y _ {w a l l} , z _ {w a l l} )\tag{20}$$

Given the disparity between the surface element mesh utilized in aerodynamic calculations and the finite element mesh employed for heat transfer calculation, it becomes imperative to employ a spatial interpolation algorithm to map the heat flux data from the surface element mesh to the finite element mesh of heat transfer. Furthermore, the thermal radiation effect of the high-temperature re-entry module must be considered in the calculation. The fundamental equation for thermal radiation calculation is the fourth power law, as delineated in Eq. (21):

$$q _ {r} = \varepsilon \sigma T ^ {4}\tag{21}$$

where $q _ {r}$ is the radiated heat flux; ε is the emissivity; σ is the Stefan–Boltzmann constant, and $\sigma = 5.67 \times 10 ^ {- 8} W / \big ( m ^ {2} {\cdot} K ^ {4} \big )$

Furthermore, a substantial ablative phenomenon transpires within the thermal shield of the re-entry module, thereby dissipating a considerable amount of heat and ensuring that the cabin structure maintains an ambient temperature. The ablation effect of thermal protection materials is typically determined through experimental measurements; however, direct and accurate calculation remains challenging [42] . In the absence of relevant experimental data, an approximation using convective heat transfer effects is employed to replace the ablation process based on calculations from several literature sources. The calculation formula for convective heat transfer is as shown in Eq. (22): [43]. The ablation effect of thermal protection materials is typically determined through experimental measurements; however, direct and accurate calculation remains challenging. In the absence of relevant experimental data, an approximation using convective heat transfer effects is employed to replace the ablation process based on calculations from several literature sources. The calculation formula of convective heat transfer is as shown in Eq. (22):

$$q _ {a} = h ( T _ {w} - T _ {e} )\tag{22}$$

where $q _ {a}$ is the heat flux of convective heat transfer which indicates the ablative one; h is the equivalent convective heat transfer coefficient; $T _ {e}$ is ambient temperature. Therefore, the ablative effect can be simulated by calculating the equivalent convective heat transfer coefficient of ablative effect. When the re-entry module is in thermal equilibrium, the relationship shown in formula (23) holds:

$$q = q _ {r} + q _ {a} + q _ {i n}\tag{23}$$

where $q _ {i n}$ is heat flux transmitted through thermal conduction into module structure. Through Eq. (19) and Eq. (21), the $q _ {a}$ and $q _ {i n}$ can be obtained. Then h can be calculated by Eq. (22). In this work, silicone rubber [43] is used as thermal protection coating and thermodynamic properties are shown in the Table 3.

According to the experimental results in reference, $T _ {w}$ and $T _ {O}$ are about $1200~^{\circ}\mathrm{C}$ and $70~^{\circ}\mathrm{C}$ under heat flux of 600 $\mathrm {k W / m ^ {2}}$ and an ambient temperature $T _ {e}$ of ${20 \ ^{\circ} \mathrm{C}}$ . Therefore, the equivalent convective heat transfer coefficient is assumed to be 400 W/K in this work to simulate the ablative effect of the thermal protection coating.

Finally, the material thermodynamic properties of each component must be provided. Table 4 shows their materials and thermodynamic properties.

## 3.2.2. Static analysis

The calculation of elastic stress was based on the fundamental equations of elastic mechanics, encompassing equilibrium differential equations, geometric equations, and physical equations, as demonstrated in Eqs. (24), (25), and (26), respectively.

$$\left. \begin{array} {l} {\displaystyle \frac {\partial \sigma _ {x x}} {\partial x} + \frac {\partial \sigma _ {y x}} {\partial y} + \frac {\partial \sigma _ {z x}} {\partial z} + f _ {x} = 0} \\ {\displaystyle \frac {\partial \sigma _ {x y}} {\partial x} + \frac {\partial \sigma _ {y y}} {\partial y} + \frac {\partial \sigma _ {z y}} {\partial z} + f _ {y} = 0} \\ {\displaystyle \frac {\partial \sigma _ {x z}} {\partial x} + \frac {\partial \sigma _ {y z}} {\partial y} + \frac {\partial \sigma _ {z z}} {\partial z} + f _ {z} = 0} \end{array} \right\}\tag{24}$$

(a) Pressure distribution of a 27-km altitude

(b) Heat flux distribution of a 27-km altitude

(c) Pressure distribution of a 30-km altitude

(d) Heat flux distribution of a 30-km altitude

(e) Pressure distribution of a 47-km altitude

(f) Heat flux distribution of a 47-km altitude

$$\left. \begin{array} {c} {\displaystyle \varepsilon _ {x} = \frac {\partial u} {\partial x} , \varepsilon _ {y} = \frac {\partial v} {\partial y} , \varepsilon _ {z} = \frac {\partial w} {\partial z}} \\ {\displaystyle \gamma _ {x y} = \frac {\partial v} {\partial x} + \frac {\partial u} {\partial y}} \\ {\displaystyle \gamma _ {x z} = \frac {\partial w} {\partial x} + \frac {\partial u} {\partial z}} \\ {\displaystyle \gamma _ {y z} = \frac {\partial v} {\partial z} + \frac {\partial w} {\partial y}} \end{array} \right\}\tag{25}$$

$$\begin{array} {c} {\varepsilon _ {x} = \displaystyle \frac {1} {E} \left[ \sigma _ {x x} - \mu \big ( \sigma _ {y y} + \sigma _ {z z} \big ) \right]} \\ {\varepsilon _ {y} = \displaystyle \frac {1} {E} \left[ \sigma _ {y y} - \mu \big ( \sigma _ {x x} + \sigma _ {z z} \big ) \right]} \\ {\varepsilon _ {z} = \displaystyle \frac {1} {E} \left[ \sigma _ {z z} - \mu \big ( \sigma _ {y y} + \sigma _ {x x} \big ) \right]} \\ {\gamma _ {y z} = \displaystyle \frac {2 ( 1 + \mu )} {E} \sigma _ {y z} \gamma _ {x z} = \frac {2 ( 1 + \mu )} {E} \sigma _ {x z} \gamma _ {x y} = \frac {2 ( 1 + \mu )} {E} \sigma _ {x y} \Bigg )} \end{array}\tag{26}$$

where σ is the stress $; f$ is the force; ε is the strain; γ is shear strain; u, v, w are the displacement components; E and $\mu$ are the Elastic modulus and Poisson’s ratio of material, respectively.

The thermal stress is coupled in the mechanical analysis as Eq. (27) shown:

$$\sigma = \sigma _ {f} + E \alpha \Delta T\tag{27}$$

where α is the thermal expansion coefficient, $\sigma _ {f}$ is the stress caused by aerodynamic pressure, and $\varDelta T$ is the temperature change.

In this work, the S4R mesh is adopted to discretize the structure of the re-entry module. To perform the heat-force coupling analysis, the grid division method of the structural finite element model is identical to that of the heat conduction finite element model, as shown in Fig. 5. Since the re-entry module flies in the atmosphere without fixed displacement boundary conditions, an inertial release technology is necessary. The inertial release is based on D’Alembert’s principle, which eliminates the rigid body motion by placing virtual supports on the structure and applying inertial forces to balance external forces. The aerodynamic pressure is applied on the surface of the re-entry module as boundary condition.

Meanwhile, it is assumed that the heat-proof shell of the re-entry module mainly plays the role of heat insulation and force transmission while ignoring its mechanical properties. The internal structure uses aluminum alloy material. Table 5 shows the physical properties of materials.

Based on the above parameters and data, the finite element calculation model can be constructed, and the structural response of the reentry capsule after structural damage is obtained through finite element analysis. Then the damage response database of the re-entry capsule can be constructed by using the sensor sites described in Section 1 to extract the relevant response.

## 3.3. Data expansion method

The heat-force coupling analysis based on FEM has been revealed to have several limitations. These include high computing resource consumption, slow simulation speed, and low efficiency. Consequently, it is unable to obtain a significant amount of damage data in a timely manner. Due to data-driven nature of neural network algorithm, serious overfitting will occur when the amount of data is insufficient, which results in insufficient generalization ability of the damage identification model. To address this limitation, it is imperative to expand the existing database to ensure the generalization capability of the damage identification model. The present study proposes a data expansion process based on the Kriging surrogate model, as illustrated in Fig. 7.

The Kriging method is a surrogate model technique that constructs a data mapping model to replace the complicated and time-consuming numerical simulation process and accelerate the acquisition of simulation data. This method has been shown to establish an unbiased fitting model with a high degree of efficiency for nonlinear functions with limited samples. The present study proposes the development of a damage simulation surrogate model based on the Kriging method. The primary objectives of this endeavor is to rapidly acquire damage data and then expand the database, thereby to ensure the generalization ability of the damage identification model. The simulation database is established firstly according to the simulation method in Section 2 firstly. Then the database is used to train Kriging model which can map the damage value to the sensor data. Finally, random sampling method including Latin hypercube sampling will be used for generating the data value and the relevant sensor value will be calculated by the Kriging model. Through the above process, the database can be expanded quickly without complex and time-consuming simulation.

Kriging method holds that all unknown functions can be approximated as the combination of global trend and static random process and assumes that all model errors come from a random process [44], as shown in Eq. (28):

$$\begin{array} {r} {\pmb {y} ( \pmb {x} ) = \pmb {f} ( \pmb {x} ) ^ {T} \beta + \pmb {z} ( \pmb {x} )} \end{array}\tag{28}$$

where $\beta$ is the basis function weight function; $f ( x )$ is the basic function, including the constant basic function and linear basic function. The constant basic function can be represented as $f _ {1} \left( x \right) {=} 1 ;$ the linear basic function is $f _ {1} ( x ) {=} 1 , f _ {2} ( x ) {=} x _ {1} , . . . , f _ {2} ( x ) {=} x _ {n} ,$ z (x), which represents a static random process, and it satisfies Eq. (29):

$$E ( z ( x ) z ( w ) ) = \sigma ^ {2} R ( \theta , w , x ) = \sigma ^ {2} \prod _ {j = 1} ^ {n} R _ {j} \bigl ( \theta , w _ {j} - x _ {j} \bigr )\tag{29}$$

where $R ( \theta , {\bf w} , x )$ is the correlation function, including the Gaussian correlation function, exponential correlation function, and linear correlation function. This work adopts the Gaussian correlation function, as expressed by Eq. (30):

$$R _ {j} \big ( \theta , d _ {j} \big ) = \exp \Bigl ( - \theta _ {j} d _ {j} ^ {2} \Bigr )\tag{30}$$

The prediction function form of the Kriging method is Eq. (31):

$${\widehat {\boldsymbol {y}}} ( {\boldsymbol {x}} ) = {\boldsymbol {c}} ^ {T} {\boldsymbol {Y}}\tag{31}$$

where $Y = [ y _ {1} , . . . , y _ {n} ]$ is the response to input data $X = [ x _ {1} , . . . , x _ {n} ]$ in the data set, and $c ( x )$ is the vector of reference functions with respect to x (to express convenience, the following text is written as c). The purpose of the fit is to select the appropriate basis function vector c, so that the fitting mean square error is minimized, which can be expressed as

$$\begin{array} {r l} & {\quad M S E = E \big ( ( \widehat {\boldsymbol {y}} ( \pmb {x} ) - \pmb {y} ( \pmb {x} ) ) ^ {2} \big )} \\ & {= E \Big ( \big [ c ^ {T} Y - \big ( f ( \pmb {x} ) ^ {T} \beta + z ( \pmb {x} ) \big ) \big ] ^ {2} \Big )} \end{array}\tag{32}$$

The basis function can be solved by the Lagrange multiplier method. To construct the Lagrange multiplier, we must represent ${\widehat {y}} ( x ) - y ( x )$ as

$$\widehat {\pmb {y}} ( \pmb {x} ) - \pmb {y} ( \pmb {x} ) = \pmb {c} ^ {T} \pmb {Y} - \big ( \pmb {f} ( \pmb {x} ) ^ {T} \pmb {\beta} + \pmb {z} ( \pmb {x} ) \big )\tag{33}$$

Substituting Eq. (29) into Eq. (34), Eq. (35) can be obtained:

$$\begin{array} {c} {{{\widehat {y}} ( x ) - y ( x ) = c ^ {T} ( F \beta + Z ) - {\left( {f ( x )} ^ {T} \beta + z ( x ) \right)}}} \\ {{{}}} \\ {{= c ^ {T} Z - z ( x ) + {\left( F ^ {T} c - f ( x ) \right)} ^ {T} \beta}} \end{array}\tag{34}$$

where $Z$ and F are the deviation and basis function of the known points, respectively; z(x) and $f ( x )$ are the deviation and basis function of the predicted points, respectively. Since $f ( x ) ^ {T} \beta$ is an unbiased estimate of the global trend, one obtains Eq. (35):

$${\cal F} ^ {T} {\cal C} = f ( x )\tag{35}$$

Thus, ${\widehat {\boldsymbol {y}}} ( {\boldsymbol {x}} ) - {\boldsymbol {y}} ( {\boldsymbol {x}} )$ can be expressed by Eq. (36):

$$\widehat {\pmb {y}} ( \pmb {x} ) - \pmb {y} ( \pmb {x} ) = \pmb {c} ^ {T} \pmb {Z} - \pmb {z} ( \pmb {x} )\tag{36}$$

Substituting Eq. (36) into Eq. (32) yields the following formula:

$$\begin{array} {c} {{M S E = E \bigl ( \bigl ( \widehat {y} ( x ) - y ( x ) \bigr ) ^ {2} \bigr ) = E \Bigl ( \bigl ( c ^ {T} Z - z ( x ) \bigr ) ^ {2} \Bigr )}} \\ {{= E \bigl ( z ^ {2} ( x ) + c ^ {T} Z Z ^ {T} c - 2 c ^ {T} Z z ( x ) \bigr )}} \\ {{= \sigma ^ {2} \bigl ( 1 + c ^ {T} R c - 2 c ^ {T} r \bigr )}} \end{array}\tag{37}$$

Then, the Lagrange multipliers can be constructed as shown in Eq. (38):

$$\begin{array} {l} {{L ( c , \lambda ) = \sigma ^ {2} \big ( 1 + c ^ {T} R c - 2 c ^ {T} r \big ) - \lambda ^ {T} \big ( F ^ {T} c - f \big )}} \\ {{\qquad}} \\ {{\displaystyle {\frac {\partial L} {\partial c}} = 2 \sigma ^ {2} ( R c - r ) - F \lambda}} \end{array}\tag{38}$$

which satisfies Eq. (39):

$$\begin{array} {l} {{F ^ {T} c = f ( x )}} \\ {{{}}} \\ {{{\displaystyle {\frac {\partial L} {\partial c}} = 2 \sigma ^ {2} ( R c - r ) - F \lambda}}} \end{array}\tag{39}$$

By solving Eq. (37), the following equation is obtained:

$$\left. \begin{array} {c} {\lambda = - 2 \sigma ^ {2} \big ( F ^ {T} R ^ {- 1} F \big ) ^ {- 1} \big ( F ^ {T} R ^ {- 1} r - f ( x ) \big )} \\ {c = R ^ {- 1} \big ( r + 2 \sigma ^ {2} F \lambda \big )} \end{array} \right.\tag{40}$$

The Kriging prediction fitting model can be obtained by substituting c of Eq. (40) into ̂y(x) − y(x).

This work established a damage database via simulation. In the database, X is defined as the randomly acquired damage state and written by Eq. (41):

$$\pmb {X} = [ \Lambda _ {1} , . . . . , \Lambda _ {n} ] ^ {T} = \left[ \begin{array} {c} {\lambda _ {1 , 1} . . . \lambda _ {1 , n a}} \\ {\vdots \ddots \vdots} \\ {\lambda _ {m , 1} . . . \lambda _ {m , n a}} \end{array} \right]\tag{41}$$

Eq. (41) expresses the damage value of each area in damage condition with number m; na is the number of areas. Response Q of sensors is defined as shown in Eq. (42):

$$\mathbf {Q} = [ S _ {1} , . . . . , S _ {n} ] ^ {T} = \left[ \begin{array} {c} {s _ {1 , 1} \cdots s _ {1 , n s}} \\ {\vdots \ddots \vdots} \\ {s _ {m , 1} \cdots s _ {m , n s}} \end{array} \right]\tag{42}$$

where $Q$ is the response of ns stress sensors in the damage condition with number m. This work uses the Kriging model to construct the surrogate model with number ns to realize the mapping in Eq. (43):

$$T _ {i} : X {} Q _ {i}\tag{43}$$

where $Q _ {i}$ is the data of the ith sensor. In total, this work established ns surrogate models. One can obtain damage data X through the random number method or other methods. Then, the predicted response values $\pmb {T} ( X _ {r} ) = [ T _ {1} ( X _ {r} ) , . . . , T _ {n s} ( X _ {r} ) ]$ ] of the sensors under various damage conditions are calculated using the Kriging surrogate model. Thus, a large amount of damage data can be obtained in a short period of time to expand the database. Therefore, based on the small amount of data obtained by simulation a large database can be built, so as to avoid the problems of training overfitting and poor model generalization ability caused by insufficient data in the following model training.

## 4. Damage identification model based on BPNN

An artificial neural network is a mathematical model based on the principle of neural networks in biology. It possesses robust data processing capabilities and self-learning capabilities. The backpropagation neural network (BPNN) is a prominent example of an artificial neural network, renowned for its ability to self-learn capabilities through the use of the error backpropagation algorithm for weight parameter updates. The present study employs BPNN to construct a mapping model between sensor data and area damage value, with the objective of accurately predicting the damage value of the re-entry module.

(a) Temperature distribution of the heat-proof shell (27 km)

(b) Temperature distribution of the internal cabin (27 km)

(c) Stress distribution of the internal cabin (27 km)

(d) Temperature distribution of the heat-proof shell (30 km)

(e) Temperature distribution of the internal cabin (30 km)

(f) Stress distribution of the internal cabin (30 km)

(g) Temperature distribution of the heat-proof shell (47 km)

(h) Temperature distribution of the internal cabin (47 km)

(i) Stress distribution of the internal cabin (47 km)

The neural layers in BPNN are divided into three types: the input layer, the hidden layer, and the output layer. To enhance the network’s capacity to accommodate nonlinearities, each neuron incorporates an activation function.

In this work, the Relu function and Sigmoid function are adopted as activation functions of the neural network, and their function forms are

(a) Raw data for area 5

(b) Expanded data of area 5

(c) Raw data for area 3

(d) Expanded data of area 3

(e) Raw data for area 1

(f) Expanded data of area 1

(g) Raw data for area 4

(h) Expanded data of area 4

(a) The identification error without database expansion

(b) The identification error with database expansion

shown in Eqs.. (44) and (45):

Sigmoid $\mathbf {\partial} : F ( {\boldsymbol {x}} ) = {\frac {1} {1 + e ^ {- x}}}$

(44)

Relu : $F ( x ) = \operatorname* {m a x} ( x , 0 )$

(45)

The data transmission process of BPNN is comprised of two distinct components: forward propagation and back propagation. In the forward propagation process, the input data are extracted by the hidden layer and output by the output layer. The process for each neuron is delineated as follows: the output signal of neurons in the upper layer is transmitted to the current neuron through the corresponding connection weight. This signal is then summed, biased, and activated to obtain the output signal, as depicted in Eq. (46).

$$y = F {\Big (} \sum w _ {i} x _ {i} + b {\Big )}\tag{46}$$

(a) Variation of $r _ {a \nu g \_ o \nu}$ in training

where $x _ {i}$ refers to the output signal of the ith neuron in the previous layer, wi represents the connection weight between the ith neuron in the previous layer and the current neuron, b is bias, y refers to the output signal of the current neuron. The output signal is also transmitted to the next layer of neurons in the same process until the output layer outputs the final data.

The backpropagation process represents the training and parameter updating process of BP neural network. When the training set data is input into the neural network and the final output is obtained through the forward propagation process, the loss function is used to measure the fitting effect of the neural network. The calculated training loss is transmitted reversely step by step by the chain rule, and the weight parameters of the network are updated using the gradient descent method. This process is repeated until the minimum fitting loss of the neural network is achieved, thereby facilitating the training of the network.

The MSE is the most commonly used loss function in neural networks and is expressed by $\operatorname{Eq.}$ (47):

(b) Variation of the training loss in training

$$L o s s = \frac {1} {n} {\sum} \left( y _ {i} - \widehat {y} _ {i} \right) ^ {2}\tag{47}$$

BPNN updates the parameters based on the gradient descent method. It uses the chain rule to find the gradient of the loss function to the network weight parameter and makes the weight change to the negative gradient direction by a certain step. The updated weight parameter is then determined, as illustrated in Eq. (48).

$$w _ {i} ^ {( 1 )} = w _ {i} ^ {( 0 )} - \eta \frac {\partial L o s s} {\partial w _ {i} ^ {( 0 )}}\tag{48}$$

where $w _ {i} ^ {( 0 )}$ is the network weight before the update, $w _ {i} ^ {( 1 )}$ is the updated weight, and η is called the learning rate. Based on data in the training set, repeat the above process and constantly update the network weight and bias parameters, that is 1 epoch of training. After the completion of a epoch of training, the data in the test set are used for a validation to verify whether the model is overfitting. This process is repeated until the network converges (As shown in the upper right sub diagram of Fig. 8).

The selection of the learning rate exerts a substantial influence on the outcomes of training. An elevated learning rate can facilitate accelerated convergence and assist in circumventing local optimization. However, if the learning rate is excessively high, the model may fail to converge. Conversely, a lower learning rate, facilitates the attainment of the optimal solution, while resulting in a slower convergence rate and possible locally optimal solution. This work dynamically adjusts the training learning rate to optimize performance, commencing with a substantial learning rate to expedite convergence and progressively reducing it as the training loss stabilizes at a minimal value.

The damage identification model under consideration in this work utilizes stress, temperature, and flight state data as inputs. Given the difference in unit size and scale of the input data, it is imperative to standardize the input data to ensure the integrity of the model’s data features and the viability of model training. The standardized formula is expressed in Eq. (49).

$$x _ {b} = {\frac {x - \mu} {\sigma}}\tag{49}$$

where $\mu ( x )$ is the mean value of the sensor data, and σ(x) is the variance. The output data represent the residual capacity of the corresponding reentry module areas after damage, whose dimension is equal to the number of re-entry module areas. Finally, Table 6 shows the structure of the constructed damage identification neural network in this work.

The first layer of the network is the data input layer, and the input layer has the same dimension as the input data dimension. The input data in this paper includes stress and temperature data measured by the sensor as well as flight status (i.e. data altitude, angle of attack and speed). Then the normalization layer completes the data standardization to eliminate the impact of differences in input data units and sizes on damage identification to the greatest extent. Four hidden layers apply the fully connected network and Relu activation function to extract data features and acquire the output data. Finally, according to the statement in Section 1, the output data should be in the 0–1 range. Therefore the sigmoid layer was added to ensure the output data can be kept in the correct range.

## 5. Structural strength factor and definition of damage grade

Based on the model established in Section 3, the residual strength capacity of the structural block of the re-entry capsule can be realized by using the sensor data. According to the established damage identification model, the structural residual capacity of each area of the re-entry module can be obtained. According to the structural residual capacity of different areas, the overall structural performance of the re-entry module can be diagnosed. According to the function and importance of structure partition, the structural strength factor ωi is defined by Eq. (50):

$$\sum _ {i = 1} ^ {m} \omega _ {i} = 1\tag{50}$$

The overall structural capability of the final defined structure can be defined by Eq. (52):

$$C s = \sum _ {i = 1} ^ {m} \omega _ {i} \theta _ {i}\tag{51}$$

Finally, the structural capability can be classified according to the overall structural capability and regional structural performance. Table 7 shows the classification. A higher damage level corresponds to more serious damage.

## 6. Results and discussions

The proposed database expansion and damage identification methods in this work were validated based on the established re-entry module, as an example. Section 5.1 presents the outcomes of establishing the primary damage database. Section 5.2 is concerned with the expansion of the data set, which is based on the preliminary database, as well as the accuracy verification and visual analysis of the expansion effect. Section 5.3 is devoted to the verification of the identification effect of the neural network damage identification. Finally, section 5.4 analyzes the anti-noise interference ability of the model, as well as the application and the limitation of the proposed method.

## 6.1. Primary construction of the damage database

The damage database was constructed based on the proposed structural heat-force coupling model and damage mode. This section utilizes the 27, 30, and 47 km altitudes as case studies to elucidate the stress–temperature field calculation outcomes. As illustrated in Fig. 9, the distributions of the temperature field and stress field are presented.

In the context of an external heat flow, the temperature of the spacecraft’s exterior can reach thousands of degrees Celsius. The implementation of an external heat-proof shell is instrumental in maintaining the internal structure temperature of the re-entry module within the optimal range of $170~^{\circ}\mathrm{C}$ . This ensures the operational stability of the internal structure and associated devices, thereby safeguarding their functionality within the permissible temperature range. And, it is crucial to note that significant thermal stresses are generated due to the substantial temperature fluctuations and uneven temperature distribution. Concurrently, the aerodynamic pressure exerts significant local stresses on the main bearing components of the structure, particularly in high-temperature areas, which decides the critical monitoring area of the sensor.

## 6.2. Expansion of damage database

In this section, the damage database established by simulation under the flight condition of the re-entry module at the 30 km altitude, Ma10 velocity, and –20◦ angle of attack was taken as an example to verify the effects of data augmentation. To ensure that the model can fully extract the features of each sensor data, the data were normalized before data expansion. Following this, the database data were segmented into a training set and a test set, with a ratio of 8:2. The model’s performance was then evaluated based on the test set, and the results indicated that the average error of each sensor prediction value was <3 %, with a maximum error of ${<} 9$ %. These findings suggest that the surrogate model can effectively establish a reliable mapping from the area damage value to the sensor data. Table 8 presents the test set fitting error of the Kriging surrogate model for select sensors.

After the Kriging surrogate model of the sensors had been completed, a large amount of random area damage data, which were generated using the random number method or Latin hypercube sampling method, were substituted into the model to expand the database. To visually analyze the expansion effect, the data of two sensors were randomly selected as horizontal and vertical coordinates, and the residual capacity

Maximum Error: 1.83 
Maximum Error: 0.52 
The real damage situation

Residual Capacity Between 80%-60%

Residual Capacity Between 40%-20%

Identified damage data

(a) Damage Sample 1 of 47 km altitude

(b) Damage Sample 2 of 47 km altitude

The real damage situation

(c) Damage Sample 3 of 47 km altitude

of a structure area was used as color indicators to draw a scatter cloud map to measure the data trend and test the data expansion effect, as shown in Fig. 10.

As demonstrated in Fig. 10, the Kriging surrogate model effectively expanded the substantial amount of data. A comparison of the expanded data with the original simulation database reveals a similar trend, as depicted in the figure. This observation substantiates the efficacy of the data expansion method employed. The ensuing analysis will employ the expanded data in conjunction with the original data set to train the damage identification model.

## 6.3. Training of the damage identification model

In this section, the BPNN was trained based on the database. In this work, the error distribution and damage identification accuracy were used to evaluate the identification performance of the model. The identification error was defined as the absolute difference between the predicted and true residual capacities of the structure after damage. For a single damage sample, the overall error is defined as the average identification error of the five areas’ residual capability value. The $r _ {a \nu g o \nu}$ was defined as the mean overall error of all samples in the dataset, while $r _ {\mathrm{max}}$ and $r _ {\mathrm{min}}$ were defined as the mean value of the maximum and minimum area’s identification error of all the samples in the dataset, respectively. To obtain the identification accuracy, this work first defined the error threshold to represent the identification accuracy of the damage value. And the value of the error threshold represents the tolerance for identification error and the metric for accuracy was based on the error thresholds. For an area, when the absolute value of the identification error is within the threshold, the identification of the area is considered correct, which means the identification error is within tolerance range. When the damage values of all the areas are correctly predicted, the identification of this sample is correct.

In order to assess the efficacy of the training process and to ascertain the presence of the overfitting phenomenon in the model, it is imperative to randomly allocate the training data into training sets and test sets. In this study, 20 % of the out-of-order data set was designated as the test set. Before formal model training, this paper adopted a small subset of simulation data to verify the effect of data expansion method. In the comparison experiment, 200 simulation damage data were used in both groups and the second group expanded the data to 2000 using the method described above. The change of identification error is shown in Fig. 11.

From Fig. 11, we can find that the training without database expansion occurred serious overfitting. Although the model performs well on the training set, the model did not have recognition capability in the test set. In contrast, in the other group, the phenomenon was much relieved and the recognition error of the model in the test set is 40 % of the original. The performance of the model in the training set and the test set is not much different, which proves the good generalization performance of the model.

In order to circumvent local optimization and to optimize the identification accuracy of the neural network, it is necessary to adjust the learning rate of the neural network during training. Therefore, in formal training to ensure the network model’s full convergence, the training was repeated 2400 epochs. The selection of training parameters is outlined in Table 9.

Fig. 12(a) and (b) show the identification error and training loss in the training process, respectively. Table 10 shows Loss, $r _ {a \nu g . o \nu} , r _ {\mathrm{max}} ,$ and rmin of the final training. According to them, with the progress of training, both the identification error, i.e., $r _ {a \nu g o \nu}$ and training loss are reduced to a very small value, which proves the effectiveness and convergence of training. At the same time, the $r _ {a \nu g o \nu}$ and loss in the identification of the training set and the test set data are close, which indicates that the model does not appear overfitting phenomenon and verifies the generalization ability of the model.

After the training has been completed, all data of the database are input into the model for identification, and Fig. 13 shows the histogram of the error distribution.

As illustrated in Fig. 13, the model’s identification of a single area revealed that 80 % of the damage identification errors occurred within the range of 0–0.01, with errors greater than 0.04 accounting for <1 %. This indicates the model’s capacity for accurate damage identification of a single block. The overall identification error demonstrates a normal distribution with an average value of 0.0045, and the proportion of the overall identification error greater than 0.04 is <0.1 %, indicating the reliability and stability of the overall damage identification.

The error thresholds were set as 0.02, 0.03, and 0.04, and the proportion of correct identification (overall accuracy) and identification accuracy of each area under the three error thresholds, as well as their modified variance (As Eq. (52) shown) were calculated (as shown in Table 11).

The Modified Variance in Table 11 can be defined $\mathsf{as} S _ {n} ^ {* 2}$ , which can be calculated by eq. (52):

$$S _ {n} ^ {* 2} = {\frac {1} {n - 1}} ( x _ {i} - {\overline {{x}}} ) ^ {2}\tag{52}$$

where $x _ {i} , {\bar {x}}$ and n represent sample, mean of sample and size of sample respectively. The analysis of the above results shows that the neural network model can effectively converge after training and achieve high identification accuracy. For the identification of a single area, when the error threshold is 0.02, 0.03, or 0.04, high identification accuracy can be achieved. The low variance also indicates the stability and robustness of the model. Table 12 shows the damage identification effect under different flight conditions.

Under different flight conditions, the model can effectively predict the damage of each area with low identification error and high damage identification accuracy, which verifies the feasibility and reliability of the established structure health monitoring method in this work.

In addition, the determination of the confidence interval of the identified value is also an important problem, which can provide a basis for the subsequent task decision margin design and avoid the adverse effects of model errors to a greater extent. According to the above results, the confidence level and confidence interval of the recognition results can also be obtained. In this paper F-test is applied to determine the confidence level and confidence interval of result. Assumed that the recognition error ri follows a normal distribution, then $\mathrm{eq.}$ (53) can be obtained:

$$\frac {r _ {i} - \mu} {\sigma} \sim N ( 0 , 1 )\tag{53}$$

where μand σ refer to the mean and variance of model’s identification error respectively. N(0, 1) represents the standard normal distribution. The error mean and variance of the model can be estimated using the sample error mean and modified variance and there is:

$$\frac {( n - 1 ) S _ {n} ^ {* 2}} {\sigma ^ {2}} \sim \chi ^ {2} ( n - 1 )\tag{54}$$

where $\chi ^ {2} ( n - 1 )$ refers to Chi-square distribution with the freedom degree of n-1. Then eq. (55) can be obtained:

$${\frac {\left( {\frac {r _ {i} - \mu} {\sigma ^ {2}}} \right) ^ {2}} {\left. {\frac {( n - 1 ) S _ {n} ^ {* 2}} {\sigma ^ {2}}} \right/ ( n - 1 )}} \sim F ( 1 , n - 1 )\tag{55}$$

where $F ( 1 , n - 1 )$ refers to F distribution with the freedom degree of 1 and n-1. Then based on the quantile of F distribution $F _ {1 - \alpha} ( 1 , n - 1 )$ , the confidence interval of error can be calculated with confidence level of 95 $^ {\% ,}$ as eqs. (56) and (57) shown:

$$\frac {\left( \frac {r _ {i} - \mu} {\sigma ^ {2}} \right) ^ {2} \bigg / 1} {\frac {( n - 1 ) S _ {n} ^ {* 2}} {\sigma ^ {2}} \bigg / ( n - 1 )} < F _ {0.05} ( 1 , n - 1 )\tag{56}$$

$$0 = \mu - \sqrt {F _ {0.05} ( 1 , n - 1 ) S _ {n} ^ {* 2}} < r _ {i} < \mu + \sqrt {F _ {0.05} ( 1 , n - 1 ) S _ {n} ^ {* 2}} = u _ {i} ^ {p}\tag{57}$$

Where $u _ {i} ^ {p}$ is the error confidence interval of identified result with confidence level $p$ and $p$ is 0.95. Since the error in the calculation is absolute error, the confidence lower bound is 0. According to the above description, confidence intervals with 95 % confidence of error can be calculated, and the results are shown in the table:

According to the upper bound of confidence interval $u _ {i} ^ {p} ,$ the confidence interval of identified result with confidence level $p$ can be calculated:

$$y \in \left[ y - u _ {i} ^ {p} , y + u _ {i} ^ {p} \right]\tag{58}$$

The partial damage state of the re-entry module at the altitude of 47 km was used as an example to illustrate the damage identification effect. Fig. 14 represents the real damage value, sensor data and predicted damage value respectively under three kinds of damage conditions. Under different damage conditions, the sensor data distribution will change slightly and show different damage characteristics. The neural network can obtain the final predicted damage value by processing the sensor data and extracting its features. The maximum error of the predicted results of the three damage cases is about 0.015, indicating its excellent identification ability.

Similarly, confidence intervals with 95 % confidence level for the predictions of the three samples can be obtained as table shown.

Tables 13–16

According to the above tables, it can be found that all the real values fall into the confidence interval, which reveals the confidence of the identified value. Finally, the damage grade of the above three conditions can be obtained. Defining the structural strength factors for each area and calculating the damage level as described in Section 4, then yielding the results in Table 17. And the damage grade can be used for task adaptive adjustment.

## 6.4. Analysis of the anti-interference ability of the model

In the actual situation, the actual sensor value will deviate from the real value due to sensor error, signal transmission, and other factors. This deviation in the sensor number will result in a deviation in structural damage identification. Consequently, the model must demonstrate stability and be capable of maintaining functionality in the event of sensor data errors. In this study, the sensor data were corrupted by random noise with percentages of 0.3 %, 0.5 %, and 1 %, respectively.

By incorporating random errors into the database data, the model’s identification performance under interference can be assessed. The results of this verification are presented in Tables 18–20.

Due to the introduction of random noise error, both identification accuracy and identification error were affected. Under the action of noise below 1 %, the error change was relatively limited, and the change of error was maintained within 0.002. When the error threshold was 0.02, the overall identification accuracy was greatly affected. However, for the identification of a single area, the model maintained the basic identification ability under the action of random noise. When the error threshold was 0.03 and 0.04, the model was basically stable, which fully proves the stability and anti-interference ability of the model.

The damage identification method established in this paper can accurately determine whether damage has occurred in the structural blocks of the re-entry module based on sensor data, as well as the realtime stiffness conditions of the structure post-damage. Utilizing the stiffness conditions of different blocks to assess the overall damage status of the spacecraft can serve as a decision basis for whether launch and return missions can be executed normally. Furthermore, based on the residual stiffness of each block, the safe overload range of the structure can be determined, thereby planning a safe and feasible flight trajectory to ensure flight safety. Ground-based utilization of this technology can also be used for structural assessment of the re-entry module, serving as a basis for maintenance decisions and enhancing the reusability of the re-entry module.

However, this method has some limitations. In the assumption of damage in this paper, all the damage within a certain area are equivalently converted into the stiffness reduction of the entire area. Therefore, this method can only evaluate the overall stiffness capacity of the damaged area which can be used for determination of the module’s remaining capacity, and unable to achieve the precise positioning analysis of minor damages. At the same time, due to the simplification of damage modeling, the proposed method could not be used in accurate analysis of damage types (including cracks, corrosion, etc.).

For further validation with real-world data, the re-entry module involved in this work has relatively large scale, so the corresponding experimental validation is difficult to carry on. Therefore, most relevant studies were carried based on the numerical simulation and theoretical analysis. Of course, in future studies, the verification can be carried out step by step from four levels: (1) By using the typical structural components of the spacecraft, carry out the experiments in typical environmental states; (2) Based on the typical structural components of the spacecraft, carry out the experiments under the real environmental states of the full flight envelop; (3) Based on the real module, carry out the experiments under the real environmental states of the full flight envelop; (4) Based on the real module, carry out the flight tests. In fact, the present method can be validated by the first step to some extent, and its performance verification can be conducted along with following costly experiments.

Besides, there remain several problems that merit further investigation: (1) In this paper, the determination of sensor locations is subjective, and future research can be conducted to optimize sensor placement with the goal of improving prediction accuracy. (2) Research could be directed towards model updating techniques, employing actual flight measurement data to maintain and update the predictive models and databases. Meanwhile construct a digital twin of the re-entry capsule, thereby enhancing the accuracy of the predictions.

## 7. Conclusions

In this study, a damage identification model was developed for a reentry module. This model incorporated numerical simulations, sensor measurements, and machine learning algorithms. The primary damage database is established by thermomechanical numerical simulations and the strain-equivalent-based stiffness reduction method. A database expansion method based on the Kriging agent model is proposed to expand the damage database, and a damage identification model with BPNN is developed. The following conclusions were obtained:

(1) It is demonstrated that the zonal stiffness loss model can be utilized to construct the damage model of the re-entry module. Through the implementation of numerical simulations, a damage database has been constructed within the altitude range of 20 km to 80 km, effectively characterizing the extreme conditions that the re-entry module experiences during its return.

(2) The proposed database expansion method has been shown to significantly reduce the thermomechanical numerical simulation cost. The database is expanded by a factor of ten, and the expanded data can effectively simulate the distribution trend of the original simulation data with a maximum deviation of 7 %, thereby demonstrating the reliability and accuracy of the expanded data. Meanwhile, the contrast experiment of BPNN model training with and without database expansion demonstrated that based on the same simulation damage data, the identification error of the model with data expansion in the test set is 40 % of the original. And the overfitting was avoided to the greatest extent with low identification error, which further reveals the effectiveness and superiority of the database expansion method.

(3) The damage identification model’s training loss is reduced to 0.0000926, accompanied by a substantial decrease in the identification error to 0.0062, which sufficiently substantiates the convergence of the model. The model’s superior identification performance in both the training and test sets further substantiates its exemplary generalization capability. The model demonstrates a remarkable accuracy of 92.6 %, with an error threshold of 0.03, and exhibits notable anti-interference capabilities, with an error rate of <1 % in the presence of random sensor noise.

## CRediT authorship contribution statement

Xiao-Bing Ma: Writing – original draft, Visualization, Validation, Methodology, Data curation, Conceptualization. Rui Guo: Writing – original draft, Visualization, Validation, Methodology. Hua Su: Supervision, Methodology. Chun-Lin Gong: Writing – review & editing, Supervision. Jian-Jun Gou: Writing – review & editing, Supervision, Funding acquisition.

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
- [Table 15 omitted; saved to tables/table_015.md]
- [Table 16 omitted; saved to tables/table_016.md]
- [Table 17 omitted; saved to tables/table_017.md]
- [Table 18 omitted; saved to tables/table_018.md]
- [Table 19 omitted; saved to tables/table_019.md]
- [Table 20 omitted; saved to tables/table_020.md]
- [Table 21 omitted; saved to tables/table_021.md]
