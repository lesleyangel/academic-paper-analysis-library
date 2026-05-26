## 1. Introduction

The high-speed vehicle encounters severe external aerodynamic [1–3] and internal electronic heating [4,5] effects and a heat transport (HT) system is always adopted to transport such heat from high-temperature regions to low-temperature regions and to maintain the structural and cabin temperature in available ranges. In multiple hypersonic flight missions like reusable launch vehicles, the accumulative effect of various damages in HT paths will lead to resistance augment, performance undermining, and even failures of these HT systems. Thus, a certain tolerance of damages is essential for a qualified HT system. Specifically, an HT system refers to a system that transports heat between components and equipment of different temperatures through passive schemes such as high thermal conductivity materials, heat pipes, etc. [6–8], as well as active schemes such as convective cooling [9–11].

Materials with high thermal conductivities are always adopted to enhance the heat conduction property at certain orientations to form an HT system. For instance, Li et al. [12] and Wang et al. [13] proposed HT systems based on C/C composite materials with high thermal conductivities (higher than 500 W/(m⋅K) in [12]). NASA used high thermal conductivity graphite fiber reinforced Metal Matrix Composites (higher than 400 W/(m⋅K) in 200–400 K with low density) as heat sinks for electronic devices in the 1990s [14]. Lu et al. [4] developed a temperature control film with a thermal conductivity of 1600 W/(m⋅K) based on the high thermal conductivity diamonds for a satellite phased array antenna, the ground and flight tests revealed a surface temperature difference of smaller than 3 K. To improve the thermal performance of materials under high temperatures, Ultra-High Temperature Ceramics (UHTC) and C/SiC composite based on $\mathrm{ZrB} _ {2}$ and $\mathrm{HfB} _ {2}$ are proposed. Squire et al. [15] designed a sharp leading edge of high-speed vehicles using diboride-based UHTC with high-temperature capability and high thermal conductivity, such HT structure allows the aerodynamic heat near the stagnation region to be quickly conducted away to cooler regions and radiated back to the environment. Cecere et al. [16] and Luo et al. [17] prepared sharp leading edge structures using $\mathbf {Z r B} _ {2} - \mathbf {S i C}$ based UHTC and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at high temperatures, and test results indicated that a ZrO skeleton was formed resulting in improvement of the ablation resistance. Mungiguerra et al. $[ 18 , 19 ]$ proposed a near-zero ablation HT system made of Ultra-High-Temperature Ceramic Matrix Composites (UHTCMC) based on $\mathrm {Z r B _ {2}}$ with a density of 4300 kg/m3 and a thermal conductivity of 49

W/(m⋅K). UHTC based on ZrB2 and HfB2 could achieve thermal conductivities of 55–60 W/(m⋅K) [20], while C/C composites based on ZrB2 could achieve in-plane thermal conductivities of 100–200 W/(m⋅K) [21]. However, research by Liu et al. [22] indicated that ZrO2 has a very low thermal conductivity, which will accelerate heat accumulation on the surface of the composites and result in a gradual temperature increase.

Heat pipes can maintain a nearly uniform temperature over the structure with a very high HT efficiency, so highly integrated heat pipes are proposed as effective solutions for high-speed vehicles [7]. For instance, Fusaro et al. [7] and Liu et al. [23,24] separately designed integrated heat pipe structures for sharp leading edges and analyzed the effects of geometric configuration and working fluid on heat pipe cooling using finite element methods. Xiao et al. [25] proposed a heat-pipe-cooled HT structure for wing leading edges and developed a three-dimensional numerical method considering the sonic limit of the heat pipe. Tokuda et al. [26] developed an oscillating heat pipe with sodium as the working fluid, their studies proved that the maximum HT rate of 477 W was obtained at temperatures of 1093 K for the heating section and 882 K for the cooling section.

HT technology of convective cooling in high-speed vehicles mainly focuses on the specific local HT path and the global HT network. For local HT paths, the configurations of structures and properties of materials are studied to improve thermal performance [10,27,28]; for global HT networks, propellant distribution and power allocation should be considered [9,29]. Qiao et al. [10] proposed an active HT system with multiple parallel channels of the leading edge and analysis results showed that the “diamond” channel with coolant of kerosene RP-3 could improve the cooling performance. Gopinath et al. [27] designed an HT system based on the metal sandwich panel with a corrugated core for the scramjet engine and proposed a semi-coupled analysis method to study the flow-thermal-structural response. Zhao et al. [28] established a simulation method to investigate the effect of pressure on the thermal cracking of RP-3 kerosene under supercritical conditions and found that heat transfer is enhanced as pressure increases when the fuel temperature is below 830 K. Gou et al. [9] proposed an HT system for a high-speed vehicle considering the full process of the heat dissipation, transport, and reuse based on the thermal protection system (TPS), regenerative cooling network, and thermoelectric conversion component, respectively. Ferretto et al. [29] proposed an HT system with integrated onboard power generation capabilities for a Mach 8 high-speed aircraft powered by liquid hydrogen, and the implementation of a system schematic was presented within the EcosimPro platform.

For these HT systems, the accumulation of various damages which has high probabilities in reusable launch vehicles will influence the performance and even lead to functional failures as discussed above. For instance, oxidation and ablation could cause reductions in the HT performance of materials with high thermal conductivities [8,30–32]; fatigue and corrosion in convective cooling systems could cause blockage and cracks in the HT network [33–35].

For materials with high thermal conductivities, Huang et al. [8] prepared a three-dimensional ZrC-SiC-modified C/C composite with a thermal conductivity of 206.5 W/(m⋅K) in X(Y) direction and designed the mesophase-pitch-based carbon fibers/pyrocarbon skeleton as HT channels to improve the ablation resistance. Li et al. [30] and Liu et al. [31] studied the ablation behavior of C/SiC-HfC composites and their tests indicated that the introduction of HfC could increase the thermal conductivity and improve the ablation resistance. Hassan et al. [32] found that ZrB2 composites reinforced with fine SiC (about 5 μm) have better oxidation resistance than coarse SiC (about 30 μm). For convective cooling systems, Murad et al. [33] found that most failure modes of HT pipelines in the industrial field like fatigue, creep, corrosion, and hydrogen attack are caused by the aggressive service environment or manufacturing imperfections. Zhou et al. [34] proposed a failure probabilistic analysis method based on simulations of the generation and growth processes of pits by non-homogeneous Poisson and stationary gamma processes, respectively. Pelliccione et al. [35] analyzed a titanium plate HT system for freshwater cooling by seawater and found that the load fluctuations and subsequent mechanical fatigues caused the failure of the plates. Song et al. [36,37] proposed an intensity distribution inverse design method based on a finite element numerical model and a shaped high-power laser heat source to study thermal fatigue behavior on pistons. Yin et al. [38] developed a physical model for vapor leakage based on the experimental research of vapor leakage through pipeline cracks.

According to the generation and growth processes, the above damages can be classified into two types: the non-thermal damage caused by various non-thermal loads like mechanical vibration, impact, etc., and randomness is often involved in the volume fraction and size; the thermal damage which is closely related with the temperature, like the ablation, oxidation, etc. In this work, two mathematical models are developed to describe these types of damages. A dendritic HT system is established using topologic optimization with the objective of the lowest geometric average temperature, and the non-thermal and thermal damages are reconstructed in such system. The effects of damages on the HT performance are numerically clarified, and two damage tolerance indicating models are proposed by polynomial fittings and validated by extended numerical data.

## 2. The high-speed vehicle and its HT system

Fig. 1(a), (b) and (c) show the high-speed vehicle and heating effects, the heat transfer processes and HT paths, respectively. As shown in Fig. 1 (a), the heating effect of high-speed vehicles includes aerodynamic and electronic ones. As shown in Fig. 1(b), aerodynamic and electronic heat will be partly dissipated into the environment and cabin, respectively, and the rest heat will be transported to low-temperature region by HT systems. The HT paths could be designed in different forms when used in different parts of a high-speed vehicle. The mostly adopted HT paths are shown in Fig. 1(c), $\mathrm{i.e.,}$ the parallel path with less HT resistance and the dendritic path with higher HT efficiency in theory. Gao et al. [39] designed the parallel HT paths used on the flat region for a leading edge. The overall dimensions $( L \times W \times H )$ are 100 mm $\times 100 \mathrm{mm} \times 16$ mm, and the sizes of parallel paths $( t \times w \times h )$ are 2.2 mm × 84.4 mm × 2.2 mm. The external coolant, deionized water, goes through the parallel paths and transports the heat from the leading edge. The 304 stainless steel and TC4 titanium alloy are employed as the parent material of the wall plate.

Although the HT system shows attractive potential for high-speed vehicles, damages may occur in the HT paths due to the severe thermo-mechanical conditions. After a long period of operation, the accumulation of various damages can lead to a decrease in the efficiency of the HT systems, and result in failures of structures and equipment in vehicles. Thus, the characterization of tolerance for various damages is essential for the design of HT paths. In this work, the influences of damages on thermal performance of a dendritic HT path are studied and two damage tolerance indicating models are obtained.

## 3. The physical model and HT path design

Generally, HT systems with various configurations and heat sinks for different components of the vehicle can be characterized by different physical models. Therefore, a typical problem should be studied in order to obtain some universal conclusions. The Volume-to-Point (VP) problem [40–42] is a fundamental heat conduction problem in the cooling of electronics (components and packages). The usual configuration of a two-dimensional VP problem contains a rectangular area with a distributed heat source, and one or more heat sinks with limited size and constant temperature on the borders of the area [41]. Topology optimization could offer the greatest potential for exploring ideal and optimum heat transfer paths [43,44]. Different from shape optimization and size optimization, the topology method can obtain any shape within the design region without a predefined configuration [45]. Wu et al. [45] developed the optimization models for the heat transfer and flow channels with porous structures. For a reaction domain with the radius of 0.5 m and the heat source of 500 $\mathrm {{W / m} ^ {2}}$ a coral-like fin structure was obtained. Li et al. [43] proposed a new method for computing the orientations and locations of heat transfer paths from a standard finite element analysis, which gives a quantitative measure of the contribution of any point in the structure to heat conduction performance. A case in square plate (100 mm × 100 mm) with heat sources of 10 W was provided, and the heat conduction path with better heat performance was obtained. Therefore, a two-dimensional VP problem is studied as benchmark as shown in Fig. 2(a), of which the length is 100 mm and the heat source is 5 W. The cold source at the bottom boundary has a length of 2 mm and a constant temperature of 293 K. The rest of boundary is adiabatic.

In this paper, the HT paths are designed by the density-based topology optimization method. The material density of the whole design domain is assumed to change between 0 and $1 , \rho = 1$ represents the domain with material of high thermal conductivity. To achieve the purpose of optimization, the solid isotropic material with penalization (SIMP) model is used to penalize intermediate densities $0 < \rho \leq 1$ . The minimum geometric average temperature, $T _ {\mathrm{geoav}}$ is used as the objective. The optimization model can be given as:

Find : $\rho ( x ) , x \in \Omega$

$$\begin{array} {l l} {\displaystyle \mathrm{Min} :} & {T _ {\mathrm{geouv}} = \left( \displaystyle \frac {1} {| \Omega |} {\displaystyle \int _ {\Omega}} ( T _ {i} ( x ) ) ^ {m} d \Omega \right) ^ {\frac {1} {m}} , x \in \Omega} \\ {\mathrm{s.t.}} & {\displaystyle \int _ {\Omega} k _ {i} \nabla T _ {i} d \Omega = \int _ {\Omega} q _ {i} d \Omega} \\ & {\displaystyle \int _ {\Omega} \rho d \Omega \leq V _ {c}} \end{array}\tag{1}$$

where, $\rho$ is the normalized material density; Ω denotes the area of the design domain; $k _ {i}$ $T _ {i ,}$ and $q _ {i}$ represent the thermal conductivity, temperature and thermal load, respectively; $V _ {c}$ is the volume constraint. The

(a) Vehicle and heating effects 
(b) Heat transport processes 
(c) HT paths

(a) Schematic diagram of the design domain (b) Mesh model

geometric average temperature is controlled by factor m. Theoretically, the objective tends to the average and maximum temperature when m tends to 1 and infinity, i.e.:

$$\begin{array} {r l} & {T _ {\mathrm{geoavg}} \overset {m \longrightarrow 1} {\longrightarrow} \mathrm{avg} ( T _ {i} ( x ) ) , x \in \Omega} \\ & {T _ {\mathrm{geoavg}} \overset {\longrightarrow \infty} {\longrightarrow} \mathrm{max} ( T _ {i} ( x ) ) , x \in \Omega} \end{array}$$

Find : $X = \{\rho _ {1} , \rho _ {2} , . . . , \rho _ {N _ {E}} \} ^ {\mathrm{T}}$

$$\mathrm{Min} : T _ {\mathrm{geoav}} = \left( \frac {1} {| \Omega |} \sum _ {i = 1} ^ {N _ {E}} \int _ {\Omega _ {i}} ( \mathbf {N} _ {i} \mathbf {T} _ {i} ) ^ {m} d \Omega _ {i} \right) ^ {\frac {1} {m}}\tag{2}$$

$$\mathbf {s . t .} \mathbf {K T} = \mathbf {Q}\tag{3}$$

In this work, m is set to 10 for a smooth approximation function with well-defined derivatives [46].

The heat transport process is solved by the finite element method (FEM), so Eq. (1) needs to be rewritten in a discrete form:

$$\sum _ {i = 1} ^ {N _ {E}} \rho _ {i} V _ {i} \leq V _ {c}$$

$$\rho _ {\mathrm{min}} \leq \rho _ {i} \leq 1.0$$

where $N _ {\mathrm{E}}$ is the total number of elements, $\rho _ {i}$ represents the material density of the ith element; Ni, Ti, and $\Omega _ {i}$ denote the general shape function matrix, the vector of nodal temperature, and the domain of the ith element, respectively; K is the global conductivity matrix, T is the vector of nodal temperature, and Q is the vector of nodal load; $V _ {i}$ is the volume of the ith element, and $\rho _ {\mathrm{min}}$ is set to 0.001 to avoid the singularity of the equations. The thermal conductivity of the HT path is assumed to be 238 W/(m⋅K). The volume fraction constraint is 30%.

(b) Optimized result of Lin et al. [40]

(a) HT path 
Tmax =391K ∆T=98K

Tmax=489KΔT=196K

(c) $Q = 5 ~ \mathrm{W}$ 
Tmax=587K ΔT =294K 
(d) $Q = 10 \mathrm{W}$ 
(ce) $Q = 15 \mathrm{W}$

The topology optimization problem is solved using the Method of Moving Asymptotes (MMA) in COMSOL Multiphysics 6.0. As shown in Fig. 2(b), the mesh model consists of 25,920 square elements and 26,243 nodes. The optimized result is shown in Fig. 3(a). The black dendritic structure consists of a material with a thermal conductivity of 238 W/ (m⋅K), which equals to the value of neat Aluminum. While the gray part consists of a material with a thermal conductivity of 0.238 W/(m⋅K) due to $\rho _ {\mathrm {{m i n}}}$ being set to 0.001. The optimized result of Lin et al. [40] is shown in Fig. 3(b), and three stages of HT paths could be clearly identified in both results. The same number of paths in the 1st and 2nd stages can be found, and the paths in each stage have similar directions.

Fig. 3(c)–(e) show the temperature distributions under different thermal loads. The red arrows indicate conductive heat flux. Thermal loads of 5 W, 10 W, and 15 W result in maximum temperatures of 391 K, 489 $\mathrm{K,}$ and 587 K, respectively. The deviations between the maximum temperature and the boundary temperature (293 K) are 98 K, 196 K, and 294 $\mathrm{K,}$ respectively. The temperature difference is linearly related to the thermal load. It can be found that the heat can be transported by the HT path under different thermal loads. In this paper, the HT path with thermal load of 10 W (1000 W/m2 ) is taken as a benchmarking model to study the influences of damages.

## 4. Mathematical models of damage

In this work, the damage on HT paths is defined as no-thermal and thermal damage according to the cause of formation. The non-thermal damage can be caused by various non-thermal loads like corrosion, vibration, impact, etc., which can be described with a stochastic model of size and volume fraction. The shape of non-thermal damage is considered as the circle, so the typical radius can be used as the size indicator. The thermal damage is generated with the temperature increasing, which can be described with a probability model considering probability gradient and constraint temperature. These damage indicators are used as inputs for mathematical models of damage. The outputs should be the location and area of the damage region, and in this problem, they are coordinates of nodes in damage elements, which will be substituted by the material with low thermal conductivity (1% of the original material). The local, reference, limit, and constraint temperatures are also used in the mathematical models. The general model of damage can be described as:

$$[ \mathbf {x} , \mathbf {y} ] = f _ {1} ( V , R ) + f _ {2} \left( T _ {\mathrm{f}} , \beta \right)\tag{4}$$

where, [x, y] is the coordinate matrix of damage region; V and R represent the volume fraction and typical radius of non-thermal damage; T and β represent the constraint temperature and probability gradient of thermal damage. $f _ {1}$ and $f _ {2}$ are the stochastic model and probability model used to describe the non-thermal and thermal damages.

## 4.1. The mathematical model of non-thermal damage

In this work, the non-thermal damage is represented as circles with low thermal conductivity, so the coordinate matrix of damage regions can be described as the matrix of centers and radii, i.e., [x, y, R]. And the volume fraction, V is converted to the number of damages, N, which can be described as the damage generation process. Therefore, N is represented as a random number following the Poisson distribution [34]. For the HT path with area $s ,$ the fraction V is defined as follows:

$$V = \frac {\displaystyle \sum _ {1} ^ {N} \pi \cdot r _ {i} ^ {2}} {S}\tag{5}$$

where, $s$ can be obtained by:

$$S = V _ {\mathrm{c}} {\cdot} L ^ {2}\tag{6}$$

Let $V _ {0}$ and $R _ {0}$ represent the typical fraction and radius, respectively. N should be a positive integer, thus, its mathematical expectation $N _ {0}$ can be obtained by:

$$N _ {0} = \bigg [ \frac {V _ {0} {\cdot} S} {\pi {\cdot} R _ {0} ^ {2}} \bigg ]\tag{7}$$

whe $^ {\mathrm {{\small ~ \circ ,} ~}}$ the square brackets indicate that the input is rounded up.

The generation probability of damage is generally related to the configuration and working conditions of the HT path. In this paper, the generation probability of damage at point $( x _ {i} , y _ {i} )$ is denoted with $A _ {\mathrm{i}} ,$ which follows a uniform distribution. And for the simulation model with m nodes, the array $\{A _ {1} , A _ {2} , . . . , A _ {m} \}$ is obtained. A new array $\{A _ {i} \mid A _ {i} >$ $A ^ {*} \}$ is used to identify nodes with damage probabilities exceeding the threshold $A ^ {*}$ . Then, N elements are randomly selected to form the array $\{A _ {m 1} , A _ {m 2} , . . . , A _ {m N} \}$ , and the node numbers $\{m _ {1} , m _ {2} , . . . , m _ {N} \}$ of damage centers are determined.

Generally, the depth of non-thermal damage like pitting corrosion follows the normal distribution [47], and the radius in two-dimension is similar to the depth in three-dimension. Therefore, the radii of damages, {ri} (i = 1…N) follow the normal distribution with an expectation of $R _ {0}$ To ensure that $r _ {i}$ is positive and adheres to the three-sigma rule, its standard deviation σ is given as follows:

$$\sigma = \frac {R _ {0}} {3}\tag{8}$$

Additionally, overlapping damage will lead to the distortion of $V ,$ particularly when $N < 60$ and $R _ {0} > 3$ mm. Therefore, the mathematical model includes three assumptions:

(1) Uniform distribution for damage generation probability.

(2) No damage overlaps when $N < 60$

(3) No damage at the cold source.

The mathematical model of non-thermal damage can be described as Eq. (9):

$$\begin{array} {r l} & {[ \mathbf {x} , \mathbf {y} , \mathbf {R} ] = f _ {1} ( V _ {0} , R _ {0} , A )} \\ & {\left( \begin{array} {l l l} {N \left( x _ {i} ^ {2} - x _ {c} ^ {2} \right) + \left( y _ {i} ^ {2} - y _ {c} ^ {2} \right) \geq r _ {i} ,} & {i , j \in \{1 , 2 \cdots N \}} \\ {\sqrt {\left( x _ {i} ^ {2} - x _ {j} ^ {2} \right) + \left( y _ {i} ^ {2} - y _ {j} ^ {2} \right)} \geq r _ {i} + r _ {j} ,} & {\mathrm{for} N < 60} \end{array} \right.} \\ & {\left. \begin{array} {r l} {r _ {N \sim N} \left( R _ {0} , \frac {R _ {0} ^ {2}} {9} \right)} \\ {N \sim P ( N _ {0} )} \\ {A \sim U ( 0 , 1 )} \end{array} \right.} \end{array}\tag{9}$$

where, $( x _ {\mathrm{c}} , y _ {\mathrm{c}} )$ is the coordinate of the center of the cold source.

The mathematical model is solved using self-programming with MATLAB, while the reconstruction and heat transfer simulation of the HT path are performed in COMSOL Multiphysics. An example of the HT path with non-thermal damage is studied with a typical volume fraction, $V _ {0} = 10 \%$ , and a typical radius, $R _ {0} = 2 ~ \mathrm{mm}$

The damage parameters are shown in Table 1, and the geometric and mesh models of example are obtained in Fig. 4. The intact region (in gray) is composed of material with a thermal conductivity of 238 W/ $\mathrm{(m.K)} ,$ , while the damage region (in white) is composed of material with a thermal conductivity of 2.38 W/(m⋅K). The boundary conditions are provided in Table 2. The heat source is a constant heat load of 10 W, the bottom of the structure has a constant temperature of 293 K with a length of 2 mm, and the rest of boundary is adiabatic.

As shown in Fig. 4 and Table 1, the non-thermal damages are indicated by sixteen circles with different radii, while the volume fraction and the radius expectation are 6.67% and 1.87 mm. Circle No.14 has the maximum radius of 2.99 mm, while circle No.9 has the minimum radius of 0.48 mm. There are two circles (Nos. 9 and 14) at the bottom, nine circles (Nos. 1, 3, 5, 7, 8, 9, 10, 14, and 15) on the trunk and seven circles (Nos. 2, 4, 6, 11, 12, 13, and 16) on the branches. The mesh model consists of 39,390 triangular elements and 22,033 nodes.

## 4.2. The mathematical model of thermal damage

With the increasing of temperature, the thermal and mechanical performance of material are getting weaker, resulting in the increasing of thermal resistance and the thermal damage finally occurring in HT paths. To study the influences of thermal damage, a normalized temperature parameter $T _ {\mathfrak {n}}$ is defined as follows:

$$T _ {\mathrm{n}} = \left( {\frac {T - T _ {\mathrm{r}}} {T _ {\mathrm{lim}} - T _ {\mathrm{r}}}} \right) ^ {p}\tag{10}$$

where, T is the temperature of node; Tr is the reference temperature; $T _ {\mathrm{lim}}$ is the limit temperature of material; $p$ is a parameter related to mechanical properties.

Generally, the mechanical and thermal performances of materials decline rapidly with increasing temperature. It can be assumed that there is a constraint temperature $T _ {\mathrm{f}}$ exists. When the temperature exceeds $T _ {\mathrm{f}} ,$ the probability of thermal damage increases rapidly. Let $\beta$ represent the gradient of probability when $T = T _ {\mathrm{f}}$ Account for influences of β and $T _ {\mathrm{f}} , T _ {\mathrm{n}}$ is transformed by a hyperbolic tangent function to obtain $T _ {\mathrm{h}} ,$ which can indicate the probability of thermal damage. $T _ {\mathrm{h}}$ can be

obtained by:

$$T _ {\mathrm{h}} = \frac {\displaystyle \mathrm{tanh} \bigg ( \beta \cdot \frac {T _ {\mathrm{f}} - T _ {\mathrm{r}}} {T _ {\mathrm{lim}} - T _ {\mathrm{r}}} \bigg ) + \mathrm{tanh} \bigg [ \beta \cdot \bigg ( T _ {\mathrm{n}} - \frac {T _ {\mathrm{f}} - T _ {\mathrm{r}}} {T _ {\mathrm{lim}} - T _ {\mathrm{r}}} \bigg ) \bigg ]} {\displaystyle \mathrm{tanh} \bigg ( \beta \cdot \frac {T _ {\mathrm{f}} - T _ {\mathrm{r}}} {T _ {\mathrm{lim}} - T _ {\mathrm{r}}} \bigg ) + \mathrm{tanh} \bigg [ \beta \cdot \bigg ( 1 - \frac {T _ {\mathrm{f}} - T _ {\mathrm{r}}} {T _ {\mathrm{lim}} - T _ {\mathrm{r}}} \bigg ) \bigg ]}\tag{11}$$

It should be noted that β indicates the maximum gradient for the function $T _ {\mathrm{h}} = f ( T _ {\mathrm{n}} ) . \mathrm{For} p = 1 , T _ {\mathrm{n}}$ and T are linearly related, so β can be used to describe the maximum gradient for the function $T _ {\mathrm{h}} = f ( T )$

Let $T _ {\mathrm{r}} = 293 \mathrm{K} , T _ {\mathrm{lim}} = 908 \mathrm{K} , p = 1 , T _ {\mathrm{f}} = 375 \mathrm{K}$ Fig. 5(a) shows the relationships between $T _ {\mathrm{h}} , T _ {\mathrm{n,}}$ and T for different values of β. In Fig. 5(a), the blue line indicates the result of $T _ {\mathbf {n}}$ . The orange, yellow, purple, and green lines indicate results for $\beta = 13 ,$ , 14, 15, and 16, respectively. It can be found that $T _ {\mathfrak {n}}$ increases linearly from 0 to 1 as temperature increases, while $T _ {\mathrm{h}}$ increases nonlinearly from 0 to 1 as temperature increases. When ${T < 0.85 T _ {f} , \ T _ {h}}$ increases slowly, and the specific values of the maximum gradient are 0.0034, 0.0032, 0.0029, and 0.0026 for cases of β = 13, 14, 15, and 16, respectively; when $0.85 T _ {\mathrm{f}} < T < 1.15 T _ {\mathrm{f}} , T _ {\mathrm{h}}$ increases rapidly, and the specific values of the maximum gradient are $0.0109 , 0.0117 , 0.0124$ , and 0.0132 for cases of β = 13, 14, 15, and 16, respectively; when $T > 1.15 T _ {\mathrm{f}} ,$ the $T _ {\mathrm{h}}$ approaches 1, and the specific values of the maximum gradient are 0.0034, 0.0031, 0.0028, and 0.0026 for cases of β = 13, 14, 15, and 16 respectively. For $T {=} T _ {\mathrm{f}} , T _ {\mathrm{n}} {=} 0.13 , T _ {\mathrm{h}}$ is approximately equal to 0.5 for different values of β. For $T _ {\mathrm{h}} = 0.95 ,$ , the specific values of T are 445, 440, 436, and 432 K for cases of β = 13, 14, 15, and 16 respectively.

Let $T _ {\mathrm{r}} = 293 \mathrm{K} , T _ {\mathrm{lim}} = 908 \mathrm{K} , p = 1 , \beta = 14 . \mathrm{Fig.} 5 ( \mathrm{b} )$ shows the relationships between $T _ {\mathrm{h}}$ and T for different values of $T _ {\mathrm{f}}$ The blue line indicates the result of $T _ {\mathrm{n} \cdot}$ The orange, yellow, purple, and green lines indicate results of T = 370 K, 375 K, 380 K, and 385 K, respectively. The trends of $T _ {\mathrm{h}}$ and $T _ {\mathfrak {n}}$ are similar to those in Fig. 5(a). For $T _ {\mathrm{h}} = 0.05 ,$ , the specific values of T are 316 K, 319 K, 322 K, and 325 K for cases of $T _ {\mathrm{f}} =$ 370 K, 375 K, 380 K, and 385 K, respectively. For $T _ {\mathrm{h}} = 0.5 ,$ the specific values of T are 370 $\mathrm{K,}$ 375 $\mathrm{K,}$ 380 $\mathrm{K,}$ and 385 K for cases of $T _ {\mathrm{f}} = 370 \mathrm{K} ,$ 375 K, 380 K, and 385 K, respectively. For $T _ {\mathrm{h}} = 0.95 ,$ the specific values of T are 435 K, 440 $\mathrm{K,}$ 445 K, and 450 K for cases of $T _ {\mathrm{f}} = 370 \ \mathrm{K} , 375 \ \mathrm{K} ,$ 380 K, and 385 K, respectively. The range of high-probability region $( T _ {\mathrm{h}}$ > 0.95) decreases as $T _ {\mathrm{f}}$ increases; the range of transition region (0.05 < $T _ {\mathrm{h}} ~ < ~ 0.95 )$ remains essentially unchanged; and the range of lowprobability region $( T _ {\mathrm{h}} < 0.05 )$ increases as $T _ {\mathrm{f}}$ increases. It should be noted that there is no intersection point for $T _ {\mathrm{h}}$ in Fig. 5(b), so the order of the curves remains constant, which is different from Fig. 5(a). In summary, the slopes of the curves of $T _ {\mathrm{h}}$ are determined by $\beta ,$ while the changes in $T _ {\mathrm{f}}$ would cause translation along the abscissa.

(b) Variations of $T _ {\mathrm{h}} , T _ {\mathrm{n}}$ with $T ( \beta = 14 )$

(a) Variations of $T _ {\mathrm{h}} , T _ {\mathrm{n}}$ with ${\cal T} ( T _ {\mathrm{f}} {=} 375 \mathrm{K} )$ 
(c) Model validation with respect to the data of Sun et al. [48] Fig. 5. Variations of $T _ {\mathrm{h}} , \ T _ {\mathrm{n}}$ with different $T _ {\mathrm{f}}$ and β.

In Ref. [48], a dimensionless indicator is proposed to characterize the macro-scale damage of brittle materials, and the indicator also ranges between 0 and 1 but the mathematical model is different from Eq. (11). As shown in Fig. 5(c), with inputs of $T _ {\mathrm{r}} = 293 \mathrm{K} , T _ {\mathrm{lim}} = 1473 \mathrm{K} , p = 1 , \beta =$ $4 , T _ {\mathrm{f}} {=} 883 \mathrm{K} ,$ the results of the thermal damage model in this paper align well with the data from Ref. [48].

The mathematical model of thermal damage can be described as Eq. (12):

$$[ \mathbf {x} , \mathbf {y} ] = f _ {2} \left( T _ {\mathrm{f}} , \beta , T , T _ {r} , T _ {\mathrm{lim}} , p \right)\tag{12}$$

Fig. 6 shows the distribution of $T _ {\mathrm{h}}$ for different values of $T _ {\mathrm{f}}$ and $\beta$ From left to right are results for $T _ {\mathrm{f}} = 370 ~ \mathrm{K} , 375 ~ \mathrm{K} , 380 ~ \mathrm{K} ,$ and 385 K. From up to down are results for $\beta = 13 , 14 , 15$ , and 16. It can be found that with the increase of $\beta ,$ areas of the high-probability region (in red) and the low-probability region (in blue) increase, and the area of transition region (in yellow and green) decreases. Additionally, with the increase of $T _ {\mathrm{f}} ,$ the area of low-probability region increases while the area of high-probability region decreases.

Let the damage threshold be $0.99 ,$ meaning that the damage is considered to occur in areas for $T _ {\mathrm{h}} > 0.99$ . As shown in Fig. $^ {7 ,}$ the damage region with low conductivity is represented in white and the intact region with normal conductivity is represented in gray. The temperature threshold $T _ {\mathrm{t}}$ can be calculated using Eqs. (10) and (11) for $T _ {\mathrm{h}} = 0.99$ . It can be found that $T _ {\mathrm{t}}$ increases with the increase of β and $T _ {\mathrm{f}} ,$ causing the increase of damage region.

Fig. 8 shows the geometric model for $T _ {\mathrm{f}} = 375 \ \mathrm{K}$ and $\beta = 14$ with a damage volume fraction of 12.73%. Damage occurs in the white region composed of material with a thermal conductivity of 2.38 W/(m⋅K), while the intact region (in gray) is composed of material with a thermal conductivity of 238 W/(m⋅K). The boundary conditions are provided in Table 3. The heat source is a constant heat load of 10 W, the bottom of the structure has a constant temperature of 293 K with a length of 2 mm, and the rest of the boundary is adiabatic. The mesh model consists of approximately 37,688 triangular elements and $^ {21 , 149}$ nodes.

In summary, the thermal damage can be described with $T _ {\mathrm{f}}$ and β. Tf represents the temperature constraint in the HT path and indicates the temperature at which the probability of damage increases fastest. $\beta$ represents the maximum gradient of the probability of thermal damage with increasing temperature. Therefore, by appropriately defining Tf and $\beta ,$ the thermal damage of the HT path can be accurately simulated.

## 5. The damage tolerance indicating model

Fig. 9 shows the temperature distribution of the example from Section 4.1. It can be found that the damage significantly influences the temperature distribution compared to Fig. 3(d). As shown in the green rectangle in Fig. 9, damage at the branches leads to an increase in local temperature. The node with the maximum temperature of 649 K is located at the 3rd branch due to the damage with a radius of 0.83 mm blocking the heat transport path. Damage at the 2nd branch with a radius of 2.06 mm results in a higher temperature difference. As shown in the blue rectangle in Fig. 9, damage changes the directions of heat flux. In summary, the damage acts as an obstacle in the HT path, results in a longer heat transport path due to the low conductivity, and subsequently alters the thermal performance: the average temperature, $T _ {\mathrm{avg}} ,$ the maximum temperature, $T _ {\mathrm{max}} ,$ and the standard deviation of temperature, $s _ {T}$

The thermal performance of the HT path with and without damage is provided in Table 4. It can be found that the damage reduces the thermal performance by increasing $T _ {\mathrm{avg}} , \ T _ {\mathrm{max}}$ , and $s _ {T} ,$ with specific values of 20.25 K, 159.98 K, and 13.15 K, respectively. These three indicators can be used to characterize the tolerance by indicating the influences of damage on the global and local temperature distributions. To establish the quantitative characterization of tolerance for various damages, the inputs and outputs of the indicating model should be normalized. As shown in Eq. (5), V has already been normalized, and R can be normalized using $V _ {\mathrm{c}}$ and $L$ The thermal performance of HT path with damage should also be normalized using the results without damage. For Q = 10 W, Vc = 30% and L = 100 mm, $T _ {\mathrm{avg0}} = 428.05 \ : \mathrm{K} , T _ {\mathrm{max0}} = 488.79$ K and $\begin{array} {r} {S _ {T 0} = 36.34 ~ \mathrm{K} .} \end{array}$ The normalized parameters can be obtained as:

$$R _ {\mathrm{n}} = \frac {R} {\sqrt {\frac {V _ {c}} {\pi}} . L} , T _ {\mathrm{avg-n}} = \frac {T _ {\mathrm{avg}}} {T _ {\mathrm{avg0}}} , T _ {\mathrm{max-n}} = \frac {T _ {\mathrm{max}}} {T _ {\mathrm{max0}}} , S _ {T - \mathrm{n}} = \frac {S _ {T}} {S _ {T 0}}\tag{13}$$

where, $V _ {\mathrm{c}}$ and $L$ are indicators of HT path; $T _ {\mathrm{avg0}} , \ T _ {\mathrm{max0}} ,$ , and $s _ {T 0}$ are determined by $Q , V _ {\mathrm{c}} ,$ and $L ; T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and ST are determined by $Q , V _ {\mathrm{c}} , L ,$ $V ,$ and $R$

Based on the mathematical models of damage obtained as Eq. $^ {( 4 )} ,$ the damage tolerance indicating model is proposed with inputs of indicators of the HT paths, (Q, $V _ {c} ,$ L) and that of damage, $( V , R , T _ {f} , \beta ) ,$ and the outputs can be used to represent the damage tolerance of HT paths. The non-thermal and thermal damage tolerance indicating models can be obtained by Eq. (14):

$$\begin{array} {r} {E _ {\mathrm{nt}} = 1 / f _ {3} ( Q , V _ {c} , L , V , R )} \\ {E _ {\mathrm{t}} = 1 / f _ {4} ( Q , V _ {c} , L , T _ {f} , \beta )} \end{array}\tag{14}$$

where, $f _ {3}$ and $f _ {4}$ are the non-thermal and thermal damage models, respectively, and they are used to describe the effect of damages on the HT performance.

To obtain the explicit relationships between thermal performance and damage indicators, the HT path indicators are fixed. Therefore, $f _ {3}$ can be obtained as:

$$f _ {3} ( Q _ {0} , V _ {c 0} , L _ {0} , V , R ) = k _ {1} {\cdot} T _ {\mathrm{avg-n}} + k _ {2} {\cdot} T _ {\mathrm{max-n}} + k _ {3} {\cdot} S _ {T - \mathrm{n}}\tag{15}$$

where, Q0, $V _ {c 0}$ and $L _ {0}$ are the fixed HT path indicators; V and R are the damage indicators; $k _ {1} , k _ {2}$ and $k _ {3}$ are weight factors with their sum being 1. The subscripts $1 , \ 2 ,$ and 3 indicate the contributions of average temperature, maximum temperature and standard deviation of temperature, respectively. For instance, by setting vectors k of $( 1 , 0 , 0 ) , ( 0 ,$ 1, 0), and (0, 0, 1), $f _ {3}$ characterizes the average temperature, the maximum temperature, and the standard deviation, respectively. For the vector of (1/3, 1/3, 1/3), $f _ {3}$ is a comprehensive characterization of thermal performance. Therefore, $f _ {3}$ can be used to predict the thermal performance of the HT path with damage. For $k _ {1} = 1$ , the prediction value of average temperature is:

$$T _ {\mathrm{avg}} ^ {\ast} = f _ {3} {\cdot} T _ {\mathrm{avg0}}\tag{16}$$

Prediction values of $T _ {\mathrm{max}}$ and $s _ {T}$ can be also calculated.

According to the definition of the indicating model, when $f _ {3} = 1 ,$ there is no damage in the HT path. When $f _ {3} > 1$ , damage occurs in the HT path, and a larger value of $f _ {3}$ means a lower damage tolerance $E _ {\mathrm{nt}}$ and

reveals weaker thermal performance.

Similarly, $f _ {4}$ can be obtained as:

$$f _ {4} \left( Q _ {0} , V _ {c 0} , L _ {0} , T _ {\mathrm{f-n}} , \beta \right) = p _ {1} \cdot T _ {\mathrm{avg-n}} + p _ {2} \cdot T _ {\mathrm{max-n}} + p _ {3} \cdot S _ {T - \mathrm{n}}\tag{17}$$

where, $p _ {1} , p _ {2}$ and $p _ {3}$ are weight factors similar to $k _ {1} ,$ , k2 and $k _ {3} , T _ {\mathrm{f-n}}$ is the normalized value of $T _ {\mathrm{f}} ,$ which can be obtained as:

$$T _ {\mathrm{f-n}} = \frac {T _ {\mathrm{f}} - T _ {\mathrm{r}}} {T _ {\mathrm{lim}} - T _ {\mathrm{r}}}\tag{18}$$

To obtain the explicit form $\mathrm{of} f _ {3}$ and $f _ {4} ,$ the quantitative relationships between the thermal performances of HT paths and the inputs of the indicating models should be analyzed.

## 6. Results and discussions

## 6.1. The non-thermal damage model

An orthogonal design is used to study the relationship between thermal performance and non-thermal damage in the HT path. Thirty groups of non-thermal damage are generated by varying $V _ {0}$ from 2% to 12% in increments of 2% and $R _ {0}$ from 1 to 5 mm in increments of 1 mm. Table 5 shows the thermal performance of these groups. Fig. 10 shows the influences of damage on thermal performance, while Fig. 11 displays the temperature distribution based on the orthogonal design.

In Table 5 and Fig. 10, V, R, and N represent the volume fraction, the mean radius, and the number of damages in each group. The lower part of Fig. 10 shows the thermal performance with blue, orange, and olive bars indicating values of $T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and $s _ {T}$ The results are divided into

five groups from left to right with $V _ {0} = 2 , 4 , 6 , 8 , 10 ,$ and 12%, respectively. In each group, from left to right are results with $R _ {0} = 1 , 2 ,$ $3 , 4 ,$ and 5 mm, respectively. The upper part of Fig. 10 shows the actual fraction V and the mean radius $R ,$ which are indicated with purple circles and red triangles, respectively. As shown in Fig. 10 and Table $5 , T _ {\mathrm{avg}}$ tends to increase with increasing $V _ {0}$ and $R _ {0}$ However, there are fluctuations in $T _ {\mathrm{max}}$ and $s _ {T}$ due to the randomness in the damage model shown in Eq. (9).

Fig. 11 shows that nodes with maximum temperatures mostly located at regions blocked by damage, such as group $5 \ : ( V _ {O} = 2 \% , R _ {O} = 5$ mm), group $7 \ ( V _ {O} = 4 \% , R _ {O} = 2$ mm), group 1 $\bar {>} ( V _ {O} = 6 \% , R _ {O} = 5$ mm), group 20 $( V _ {0} = 8 \% , R _ {0} = 5$ mm), group 24 $( V _ {0} = 10 \% , R _ {0} = 4$ mm) and group 30 $( V _ {O} = 12 \% , R _ {O} = 5 \ \mathrm{mm} )$ . It is also found that when $V _ {0}$ is constant, the maximum temperature mostly occurs in groups with larger $R _ {0}$

To eliminate the influences of randomness, thirty samples are generated in each group. The numerical results are shown in Fig. 12(a), (b), and (c). The abscissa represents the actual fraction of damage and the ordinates represent $T _ {\mathrm{avg}} , \ T _ {\mathrm{max}}$ , and $s _ {T} ,$ respectively. The circle, triangle up, square, diamond, triangle down, and star indicate results of $V _ {O}$ = 2%, 4%, 6%, 8%, 10%, and 12%, respectively. The color of points indicates the mean radius of damage in each sample. Fig. 12(a) shows that the results of $T _ {\mathrm{avg}}$ are mainly between 428 K and 500 K, and a lower boundary of points can be fitted as $T _ {\mathrm{avg}} = 428 \mathrm{Kfor} 0 < V < 5 \%$ and $T _ {\mathrm{avg}}$ $= 115.1 {\cdot} V$ + 422.2 for $V > 5 \%$ Fig. 12(b) shows that results of $T _ {\mathrm{max}}$ are fairly scattered with an approximate range of 480 to 1300 K. The lower boundary of $T _ {\mathrm{max}}$ can be fitted as $T _ {\mathrm{max}} = 360.6 {\cdot} V$ + 481.4. In Fig. 12(c), the results of $s _ {T}$ are mainly between 33 K and 130 K with a lower boundary of $S _ {T} = 71.8 {\cdot} V + 33.8$

Fig. 12(d) shows the probability density functions and specific values of N and R in the group with $V _ {0} = 10 \%$ and $R _ {0} = 5 \mathrm{mm}$ . For $V _ {0} = 10 \%$ and $R _ {0} = 5$ mm, $N _ {0} = 4$ can be calculated using Eq. (7). The probability density functions of $N \sim P ( 4 )$ and $r \sim N ( 5 , \frac {25} {9} )$ are shown in the upper part of Fig. 12(d). The specific frequencies of N and R are shown in the lower part of Fig. 12(d). It should be noted that R in Fig. 12(d) represents the mean radius of damage for each sample. The results show that samples in the group with $V _ {0} = 10 \%$ and $R _ {0} = 5$ mm meet expectations. In summary, while the randomness of damage greatly influences the thermal performance of HT path, there are still rules to follow. Therefore, an analysis of mean results for damage and thermal performance is carried out to obtain quantitative characterizations.

Fig. 13 shows the influences of damage on the mean thermal performance of the HT path, and the blue, orange, and olive bars indicate the means of $T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and $S _ {T} \left( \mathrm{i.e.,} T _ {\mathrm{~avg}} ^ {\ast} , T _ {\mathrm{~max}} ^ {\ast} , \right$ and $S ^ {*} {} _ {T} )$ . The purple circles and red triangles indicate $V ^ {*}$ and $R ^ {*} ,$ which are the means of V and R. As can be found that the $T _ {\mathrm{~\tiny~max~}} ^ {\ast}$ increases with the growth of the volume fraction of damage. For groups with $V _ {0} = 2 \%$ and 10%, $T ^ {*} \mathrm {{_ {m a x}}}$ increases with the growth of the radius of damage. However, a reversed feature can be found in other groups, such as groups of $V _ {0} = 6 \%$ , and the detailed results are shown in Table $^ {6 .}$ It can be found that with the increase of $V _ {0}$ and $R _ {0} , T ^ {\ast} \mathrm {{a v g}}$ and $S ^ {*} {} _ {T}$ increase with some fluctuations, i.e., the damage tolerance worsens.

The thermal performance could be normalized by Eq. (13), and the first-order fittings of normalized results are shown in Fig. 14. The maximum values of $T ^ {*} {\mathrm{avg}} {\mathrm{-n}} , \ T ^ {*} {\mathrm{max}} {\mathrm{-n}}$ , and $S ^ {*} {} _ {T - \mathrm{n}}$ are 1.145, 2.408, and $4.321$ , respectively. It can be found that the damage has the greatest effect on $S ^ {*} \mathrm {_ {T - n}} ,$ , followed by $T ^ {*} {\bf {\sigma}} _ {\operatorname* {m a x - n}} ,$ and the least on $T ^ {*} {\mathfrak {a v g - n}}$ n. For T\*avg-n, the coefficients of $V ^ {*}$ and $R _ {\mathrm{~\scriptsize~n~}} ^ {*}$ are 0.8735 and 0.2497, indicating that $T ^ {*} {} _ {\mathsf{avg-n}}$ is more sensitive to $V ^ {*}$ . For $T ^ {*} {\bf \Pi} _ {\operatorname{max} - \mathrm{n}}$ and $S ^ {*} \mathrm {_ {T} ,}$ the effects of $V ^ {*}$ and $R _ {\mathrm{~\scriptsize~n~}} ^ {*}$ are similar. In summary, $T ^ {*} \mathrm{avg} _ {\mathrm{-n}} , \ T _ {\mathrm {~ \mathrm{~max} \mathrm{-n}}} ^ {*} ,$ and $S ^ {*} {} _ {T - \mathrm{n}}$ are positively correlated with $V ^ {*}$ and $R ^ {*} {\bf {\Omega}} _ {\bf {n}} ,$ meaning that the damage tolerance improves with decreasing V and R. When the volume fraction of damage is smaller than $12 \% ,$ with the growth of damage, the average temperature of the HT path increases slowly, while the maximum temperature increases quickly and the standard deviation of the temperature increases rapidly.

Based on results in Fig. 14 and Eq. (15), for $Q _ {0} = 10 \mathrm{W} , V _ {c 0} = 30 \% ,$ L0 $= 100$ mm, the non-thermal damage model can be obtained as:

$${\begin{array} {r l} {f _ {3} ( V , R )} & {= ( 0.8735 \cdot k _ {1} + 5.242 \cdot k _ {2} + 11.81 \cdot k _ {3} ) \cdot V} \\ & {+ \ ( 0.2497 \cdot k _ {1} + 4.611 \cdot k _ {2} + 9.745 \cdot k _ {3} ) \cdot {\frac {R} {\sqrt {V _ {c} / \pi} \cdot L}}} \\ & {+ \ ( 0.9761 \cdot k _ {1} + 0.8251 \cdot k _ {2} + 0.3294 \cdot k _ {3} )} \end{array}}\tag{19}$$

Based on Eqs. (5) and (6), V can be represented as:

$$V = \frac {\pi \cdot \sum _ {i} ^ {N} r _ {i} ^ {2}} {V _ {c} \cdot L ^ {2}}\tag{20}$$

In addition, R is the mean value of $r _ {i} ,$ so their relationship can be obtained as:

$$\sum _ {i} ^ {N} r _ {i} ^ {2} \ge N \cdot R ^ {2}\tag{21}$$

Therefore, V can be represented as:

$$V = k _ {4} \cdot \frac {\pi \cdot N \cdot R ^ {2}} {V _ {c} \cdot L ^ {2}}\tag{22}$$

where $k _ {4}$ is a factor that is larger than 1. By polynomial fitting of the results in Table $6 , k _ {4} = 1.13$ can be obtained. By substituting Eq. (22) into Eq. (19), the non-thermal damage model can be rewritten as:

(b) Results of $T _ {\mathrm{max}}$ for the samples

(a) Results of $T _ {\mathrm{avg}}$ for the samples 
(c) Results of $S _ {T}$ for the samples

(d) Probability densities and Frequencies of $N ,$ R

$${\begin{array} {r l} {f _ {3} ( N , R )} & {= ( 0.9871 \cdot k _ {1} + 5.923 \cdot k _ {2} + 13.35 \cdot k _ {3} ) \cdot {\frac {N \cdot R ^ {2}} {V _ {c} \cdot \left/ \pi \cdot L ^ {2} \right.}}} \\ & {+ \left. ( 0.2497 \cdot k _ {1} + 4.611 \cdot k _ {2} + 9.745 \cdot k _ {3} ) \cdot {\frac {R} {\sqrt {V _ {c} / \pi} \cdot L}} \right.} \\ & {+ \left. ( 0.9761 \cdot k _ {1} + 0.8251 \cdot k _ {2} + 0.3294 \cdot k _ {3} ) \right.} \end{array}}\tag{23}$$

$S ^ {*} {} _ {T - \mathrm{n}}$ are 0.9774, 0.9479, and 0.9480, respectively, indicating that second-order fittings are more accurate.

Based on the results of second-order fittings, Eqs. (19) and (23) can be rewritten as:

As shown in Fig. 14, the coefficients of determination for first-order fitting of $T ^ {*} \mathrm{avg} . \mathrm{n} , T ^ {*} \mathrm{max} . \mathrm{n} ,$ and $S ^ {*} {} _ {T - \mathrm{n}}$ are 0.8643, 0.7880, and 0.7089, respectively. To obtain a better non-thermal damage model, secondorder fittings are carried out with results shown in Fig. 15. The coefficients of determination of second-order fitting of $T ^ {\ast} \mathrm {_ {a v g - n}} , T ^ {\ast} \mathrm {_ {m a x - n}} ,$ and

$$\begin{array} {r l} {f _ {3} ( V , R )} & {= ( 2.163 . k _ {1} - 12.71 \cdot k _ {2} + 5.574 . k _ {3} ) \cdot V ^ {2}} \\ & {+ \left( 0.0907 \cdot k _ {1} + 0.8537 \cdot k _ {2} - 5.905 . k _ {3} \right) \cdot V} \\ & {+ \left( - 1.828 \cdot k _ {1} - 39.35 \cdot k _ {2} - 76.58 \cdot k _ {3} \right) \cdot \frac {R ^ {2}} {V _ {c} / \pi \cdot L ^ {2}}} \\ & {+ \left( 0.1344 \cdot k _ {1} + 5.699 \cdot k _ {2} + 7.322 \cdot k _ {3} \right) \cdot \frac {R} {\sqrt {V _ {c} / \pi \cdot L}}} \\ & {+ \left( 6.982 \cdot k _ {1} + 87.06 \cdot k _ {2} + 242.5 \cdot k _ {3} \right) \cdot V \frac {R} {\sqrt {V _ {c} / \pi} \cdot L}} \\ & {+ \left( 1.002 \cdot k _ {1} + 0.9501 \cdot k _ {2} + 0.973 \cdot k _ {3} \right)} \end{array}\tag{24}$$

$$\begin{array} {r l} {f _ {S} ( N , R )} & {= ( 2.7625 k _ {1} - 16.23 k _ {2} + 7.117 k _ {3} ) {\frac {N ^ {2} R ^ {4}} {V _ {2} ^ {2} \left/ N ^ {2} - L ^ {4} \right.}}} \\ & {+ ( 7.895 k _ {1} + 98.38 k _ {2} + 274.03 k _ {3} ) {\frac {N - R ^ {3}} {V _ {4} / N ^ {2} - L ^ {2}}}} \\ & {+ ( 1.025 k _ {1} + 0.9647 k _ {2} - 6.673 k _ {3} ) {\frac {N - R ^ {2}} {V _ {4} / N ^ {2} - L ^ {2}}}} \\ & {+ ( - 1.828 k _ {1} - 39.35 k _ {2} - 76.588 k _ {3} ) {\frac {R ^ {2}} {V _ {4} / N ^ {2} - L ^ {2}}}} \\ & {+ ( 0.1344 k _ {1} + 5.699 k _ {2} + 7.322 k _ {3} ) {\frac {R} {\sqrt {V _ {4} / N ^ {2} - L ^ {2}}}}} \\ & {+ ( 1.002 k _ {1} + 0.9501 k _ {2} + 0.9737 k _ {3} ) .} \end{array}\tag{25}$$

## 6.2. The thermal damage model

Temperature distributions of HT path with thermal damage are shown in Fig. 16. The thermal performance is revealed in Table 7 and V represents the volume fraction of thermal damage. The thermal damage model is obtained based on the data in Table 7. For cases of $\dot {\boldsymbol {\beta}} = 13$ with $T _ {\mathrm{f}} = 380$ K and 385 K, there is no thermal damage, while for the case of β $= 16$ with $T _ {\mathrm{f}} = 370 ~ \mathrm{K} ,$ , the maximum V is 28.09%.

In $1 \mathrm{Fig.} 16 , \beta$ increases from top to bottom, resulting in the decrease of transition area and the increase of high-temperature area. $T _ {\mathrm{f}}$ increases from left to right, resulting in a reversed feature. It can be found that with the increase of $\beta ,$ the generation probability of damage increases when reaching the threshold, that is, the damage tolerance worsens. With the increase of $T _ {\mathrm{f}} ,$ the temperature threshold of damage generation increases, that is, the damage tolerance improves.

Similar to Section 6.1, second-order fittings of normalized results are given in Fig. 17. The maximum values of $T _ {\mathrm{avg-n}} , T _ {\mathrm{max-n}} ,$ and ${\cal {S}} _ {T - \mathrm {{n}}}$ are 1.83,

7.09, and 21.32, respectively. It can be found that the damage has the greatest effect on $S _ {T \cdot \mathrm{n}} ,$ followed by $T _ {\mathrm{max-n}} ,$ and the least on $T _ {\mathrm{avg-n}}$ Unlike non-thermal damage, $T _ {\mathrm{avg-n}} , \ T _ {\mathrm{max-n}} ,$ and $s _ {T - \mathrm{n}}$ are positively correlated with β but negatively with $T _ {\mathrm{f}}$ Coefficients of determination for secondorder fitting of $T _ {\mathrm{avg-n}} , \ T _ {\mathrm{max-n}} ,$ , and $S _ {T - \mathrm{n}}$ are 0.9994, 0.9927, and 0.9940, respectively, indicating that fittings for thermal damage are better because there is no randomness.

Based on $\operatorname{Eq.} \left( 17 \right) ,$ the thermal damage model can be obtained as:

$$\begin{array} {r l} {f _ {4} ( \beta , T _ {t} )} & {= ( 0.0314 \cdot p _ {1} - 0.0304 \cdot p _ {2} + 0.4461 \cdot p _ {3} ) \cdot \beta ^ {2}} \\ & {+ \left( 0.257 \cdot p _ {1} + 3.904 \cdot p _ {2} + 9.422 \cdot p _ {3} \right) \cdot \beta} \\ & {+ \left( 312.5 \cdot p _ {1} + 892.9 \cdot p _ {2} + 5152 \cdot p _ {3} \right) \cdot \left( \frac {T _ {t} - T _ {\tau}} {T _ {\mathrm{im}}} \right) ^ {2}} \\ & {+ \left( 6.409 \cdot p _ {1} - 175.8 \cdot p _ {2} + 120.3 \cdot p _ {3} \right) \cdot \frac {T _ {t} - T _ {\tau}} {T _ {\mathrm{im}} - T _ {\tau}}} \\ & {+ \left( - 7.337 \cdot p _ {1} - 12.39 \cdot p _ {2} - 13.1.3 \cdot p _ {3} \right) \cdot \beta \frac {T _ {\tau} - T _ {\tau}} {T _ {\mathrm{im}} - T _ {\tau}}} \\ & {+ \left( - 1.324 \cdot p _ {1} - 14.56 \cdot p _ {2} - 75.75 \cdot p _ {3} \right)} \end{array}\tag{26}$$

## 6.3. The damage tolerance for HT path

## 6.3.1. The non-thermal damage tolerance

For a dendric HT path, the influences of non-thermal damage are characterized quantitatively as Eq. (24), and the predictions of HT performance can be obtained. Besides, the non-thermal damage tolerance $E _ {\mathrm{nt}}$ can be also calculated by Eq. (14). To investigate the influences of non-thermal damage on thermal performance and obtain the damage tolerances, forty additional samples are divided into four groups based on two damage indicators: $V _ {0} = 5 \% ,$ 9% and $R _ {0} = 2.3$ mm, 3.7 mm. The indicators of Groups 1, 2, 3, and 4 are 5% and 2.3 mm, 5% and 3.7 mm, 9% and 2.3 mm, and 9% and 3.7 mm, respectively. The thermal performance of samples is obtained using the numerical simulation and the indicating model, and the results are shown in Fig. 18.

The abscissa represents the sample number and “Average” is the average result of ten samples. The histogram shows the thermal performance and the prediction results of $T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and $s _ {T}$ The blue, orange, and red bars indicate the simulation results of $T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and $S _ {T} ,$ respectively, while the cyan, yellow, and purple bars indicate the prediction results of $T _ {\mathrm{avg}} , \ T _ {\mathrm{max}} ,$ , and $s _ {T}$ (i.e., $T ^ {*} {} _ {\mathrm{avg}} , \ T ^ {*} {} _ {\mathrm{max}} ,$ and $s ^ {*} {} _ {T} )$ , respectively. The blue, orange, and red lines indicate deviations of the simulation and prediction results of $T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and $s _ {T} ,$ , respectively. For “Avera $\mathbf {g} \mathbf {e} ^ {\mathbf {\gamma}} \mathbf {\Sigma} _ {\mathbf {i}}$ , V, R $\updownarrow , T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and $s _ {T}$ are the means of ten samples while $T ^ {*} {} _ {\mathrm{avg}} , T ^ {*} {} _ {\mathrm{max}}$ and $S ^ {*} {} _ {T}$ are predictions calculated using $\mathrm{Eq.~} ( 24 )$ . In the upper part of Fig. 18, purple circles and red triangles indicate the fraction, V and mean radius, R of each sample.

In ${\mathrm{Fig.~}} 18 ( {\mathrm{a}} ) ,$ sample No. 10 with $V = 3.48 \%$ and $R = 2.28$ mm has the worst thermal performance. For this sample, $T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ , and $s _ {T}$ are 451.93 K, 860.4 K, and 73.71 K, respectively; $T ^ {*} {} _ {\mathrm{avg}} , T ^ {*} {} _ {\mathrm{max}} ,$ and $S ^ {*} {} _ {T}$ are 439.02 K, 681.25 K, and 55.24 K, respectively; the deviations of $T _ {\mathrm{avg}} ,$ $T _ {\mathrm{max}} ,$ and $S _ {T} \mathrm{are} - 2.86 \% , - 20$ .82%, and − 25.06%, respectively. Sample No. 8 with $V = 3$ .48% and $R = 2.28$ mm has the best fitting results. For this sample, $T _ {\mathrm{avg}} ,$ Tmax, and $s _ {T}$ are 441.34 K, 647.04 K, and 48.44 $\mathrm{K,}$ respectively; $T ^ {*} {} _ {\mathrm{avg}} , T ^ {*} {} _ {\mathrm{max}} ,$ and $S ^ {*} {} _ {T}$ are 445.00 K, 748.58 K, and 65.11 $\mathrm{K,}$ respectively; the deviations of $T _ {\mathrm{avg}} ,$ Tmax, and ST are 0.83%, − 9.52% and 2.41%, respectively. For “Average”, $V , R , T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and $s _ {T}$ are 3.98%, 2.11 mm, 438.35 K, 698.28 K, and 52.17 $\mathrm{K,}$ respectively; $T ^ {*} {} _ {\mathrm{avg}} ,$ T\*max, and $S ^ {*} {} _ {T}$ are 440.32 $\mathrm{K,}$ 687.23 $\mathrm{K,}$ and 56.29 $\mathrm{K} ,$ respectively; the deviations of $T _ {\mathrm{avg}} ,$ Tmax, and $S _ {T}$ are 0.45%, − 1.58%, and 7.90%, respectively.

In Fig. 18(b), sample No. 5 with $V = 7.81 ^{\circ}$ % and $R = 3.78$ mm has the worst thermal performance. For this sample, Tavg, Tmax, and $s _ {T}$ are 454.68 K, 1057.72 K, and 115.91 K, respectively; $T ^ {*} {} _ {\mathrm{avg}} , T ^ {*} {} _ {\mathrm{max}} ,$ , and $S ^ {*} {} _ {T}$ are 461.46 K, 918.53 K, and 94.95 K, respectively; the deviations of $T _ {\mathrm{avg}} ,$

$T _ {\mathrm{max}} ,$ and $S _ {T}$ are $1.49 \% , - 13.16 \% ,$ and − 18.09%, respectively. Sample No. 4 with $V = 2.78 \%$ and $R ^ {*} = 2.90$ mm has the best fitting results. For this sample, $T _ {\mathrm{avg}} , \ T _ {\mathrm{max}} ,$ and $S _ {T}$ are 434.12 K, 748.79 K, and 52.20 K, respectively; $T ^ {*} {} _ {\mathrm{avg}} , T ^ {*} {} _ {\mathrm{max}} ,$ and $S ^ {*} {} _ {T}$ are 437.01 K, 674.25 K, and 53.03 K, respectively; the deviations of $T _ {\mathrm{avg}} , \ T _ {\mathrm{max}} ,$ and $s _ {T}$ are $0.66 \% , \ - 9.96 \%$ and 1.59%, respectively. For “Average”, V, R, $T _ {\mathrm{avg}} , \ T _ {\mathrm{max}} ,$ and S are 4.97%, 3.49 mm, 442.74 K, 821.96 $\mathrm{K,}$ and 72.03 $\mathrm{K,}$ respectively; $T ^ {*} {} _ {\mathrm{avg}} ,$ $T _ {\mathrm{~\tiny~max}} ^ {\ast} ,$ and $S ^ {*} {} _ {T}$ are 446.43 K, 778.04 K, and 69.26 K, respectively; the deviations of $T _ {\mathrm{avg}} , \ T _ {\mathrm{max}} ,$ and $s _ {T}$ are 0.83%, − 5.34%, and − 3.84%, respectively.

In Fig. 18(c), sample No. 4 with V = 14.28% and R = 2.49 mm has the worst thermal performance and the best fitting results. For this sample, $T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and $s _ {T}$ are 478.47 K, 1039.71 K, and 111.24 K, respectively; $T ^ {\ast} _ {\mathrm{avg}} , T ^ {\ast} _ {\mathrm{max}} ,$ , and $S ^ {*} {} _ {T}$ are 487.34, 987.36, and 113.81 K, respectively; the deviations of $T _ {\mathrm{avg}} , \ T _ {\mathrm{max}} ,$ and $S _ {T}$ are 1.85%, − 5.03%, and 2.31%, respectively. For “Average”, $V , R , T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and $s _ {T}$ are 8.72%, 2.37 mm, 455.72 K, 853.57 K, and 81.33 K, respectively; $T ^ {*} {} _ {\mathrm{avg}} , T ^ {*} {} _ {\mathrm{max}} ,$ and $S ^ {*} {} _ {T}$ are 459.09 K, 838.21 K, and 81.11 $\mathrm{K,}$ respectively; the deviations of $T _ {\mathrm{avg}} ,$ $T _ {\mathrm{max}}$ and $s _ {T}$ are 0.74%, − 1.8%, and − 0.27%, respectively.

In Fig. 18(d), sample No. 2 with $V = 13.48 \%$ and $R = 4.17$ mm has the worst thermal performance. For this sample, $T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and $s _ {T}$ are 504.79 K, 1354.75 K, and 133.46 K, respectively; $T ^ {*} {} _ {\mathrm{avg}} , T ^ {*} {} _ {\mathrm{max}}$ , and $S ^ {*} {} _ {T}$ are 498.85 K, 1207.68 K, and 155.71 $\mathrm{K,}$ respectively; the deviations of $T _ {\mathrm{avg}} , \ T _ {\mathrm{max}} ,$ and $s _ {T}$ $\cdot \ \mathrm{are} \ - 1.18 \% , \ - 10.86 \%$ , and $16.67 \% ,$ respectively. Sample No. 8 with $V = 8.48 \%$ and $R = 4.00$ mm has the best fitting results. For this sample, $T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and ST are 462.70 K, 956.48 $\mathrm{K} ,$ and 109.11 K, respectively; $T ^ {\ast} _ {\mathrm{avg}} , T _ {\mathrm{max}} ^ {\ast}$ , and $s ^ {*} {} _ {T}$ are 466.00 K, 960.57 K, and 103.20 $\mathrm{K,}$ respectively; the deviations of $T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and S are 0.71%, 0.43%, and − 5.41%, respectively. For “Average” $, V , R , T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and $s _ {T}$ are 10.19%, 3.78 mm, 476.32 K, 1108.89 K, and 117.14 K, respectively; $T ^ {*} {} _ {\mathrm{avg}} , T ^ {*} {} _ {\mathrm{max}} ,$ and $S ^ {*} {} _ {T}$ are 475.01 K, 1025.28 $\mathrm{K,}$ and 116.27 K, respectively; the deviations of $T _ {\mathrm{avg}} , \ T _ {\mathrm{max}} ,$ and $S _ {T} ~ \mathrm{are} ~ - 0.28 \% , ~ - 7.54 \%$ , and $- 0.74 \% ,$ , respectively.

Comparing the results of numerical simulations and prediction models, it can be found that the prediction of the model is reliable, which proves that the characterization of damage in indicating model is reasonable. It can be concluded that: (a) The tolerance indicating model can be used to predict the thermal performance of the HT path with nonthermal damage, and the maximum deviations of the tolerance indicating model are $0.83 \% , - 7.54 \%$ , and 7.90% for average $T _ {\mathrm{avg}} , T _ {\mathrm{max}}$ and $s _ {T} ,$ respectively; (b) $T _ {\mathrm{avg}}$ has the best prediction accuracy because it is the average result of the HT path, which eliminates some influences of randomness; (c) The prediction accuracy of $T _ {\mathrm{max}}$ decreases with increasing $V _ {0}$ and $R _ {0}$ because $T _ {\mathrm{max}}$ usually occurs near damage and increasing $V _ {0}$ and $R _ {0}$ reduce HT path near damage; (d) The prediction accuracy of $\textmd {‰}$ decreases with decreasing $V _ {0}$ and increasing $R _ {0}$ because decreasing V0 reduces the high-temperature area of the HT path while increasing $R _ {0}$ increases local temperature near damage, resulting in an increasing temperature gradient near damage.

By setting $k _ {1} = k _ {2} = k _ {3} = 1 / 3$ and substituting $\operatorname{Eq.} \left( 24 \right)$ into Eq. (14), the non-thermal damage tolerance $E _ {\mathrm{nt}}$ can be obtained:

$$E _ {\mathrm{nt}} ( V , R ) = \left( \begin{array} {l} {- 1.66 \cdot V ^ {2} + 1.65 \cdot V - 39.25 \cdot \frac {R ^ {2}} {V _ {c} / \pi \cdot L ^ {2}}} \\ {+ 4.39 \cdot \frac {R} {\sqrt {V _ {c} / \pi} \cdot L} + 112.18 \cdot V \cdot \frac {R} {\sqrt {V _ {c} / \pi} \cdot L} + 0.975} \end{array} \right) ^ {- 1}\tag{27}$$

$E _ {\mathrm{nt}}$ reveals the thermal performance of the HT path with non-thermal damage in consideration of the average temperature, maximum temperature, and the standard deviation of temperature. $E _ {\mathrm{nt}}$ ranges between 0 and 1, and a larger value of $E _ {\mathrm{nt}}$ means the certain non-thermal damage has less influence on HT performance, indicating the better damage tolerance for the HT path. Fig. 19 shows the non-thermal damage tolerances of samples and the average results for each group. The blue, yellow, red, and green lines represent the results for Groups 1, 2, 3, and $^ {4 ,}$ respectively. The minimum damage tolerance is 0.302 for sample No.

(a) Results with $V _ {0} = 5 \% , R _ {0} = 2$ 3mm 
(b) Results with $V _ {0} = 5 \% ,$ $R _ {0} = 3$ 7mm

3 in Group 2 with the maximum V = 16.33% and R = 5.00 mm among all samples. The maximum damage tolerance is 0.926 for sample No. 1 in Group 1 with the minimum $V = 2.12 \%$ and $R = 0.94$ mm among all samples. The average damage tolerance for Groups 1, 2, 3, and 4 are 0.752, 0.705, 0.602, and 0.478, respectively. In summary, for a specific damage condition, the damage tolerance of the HT path worsens with increasing volume fraction and radius of damage.

## 6.3.2. The thermal damage tolerance

To study the influence of thermal damage on thermal performance, the thermal performance of nine additional samples is obtained using the numerical simulation and the indicating model. The damage indicators of samples are shown in Table 8. Fig. 20 presents the simulation and prediction results. The abscissa represents the sample number while the histogram shows thermal performance and the prediction results of $T _ {\mathrm{avg}} , \ T _ {\mathrm{max}} ,$ and $s _ {T}$ The blue, orange, and red bars indicate simulation results of $T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and $s _ {T} ,$ respectively. The cyan, yellow, and purple bars indicate prediction results of $T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and $S _ {T} \left( \mathrm{i.e.,~} T _ {\mathrm{~avg}} ^ {\ast} , \ : T _ {\mathrm{~\max}} ^ {\ast} , \right$ and $S ^ {*} {} _ {T}$ , respectively. The blue, orange, and red lines indicate deviations between the simulation and prediction results of $T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and $s _ {T} ,$ respectively. In the upper part of Fig. 20, purple circles and red triangles indicate the fraction $V$ and temperature threshold $T _ {\mathrm{t}}$ of each sample. The green line at the top of Fig. 20 indicates the thermal damage tolerances $E _ {\mathrm{t}} ,$ which are calculated using Eqs. (14) and (26) with $q _ {1} = q _ {2}$ $= q _ {3} = 1 / 3$ . Similar to $E _ {\mathrm{nt}} , E _ {\mathrm{t}}$ ranges between 0 and 1, and a larger value of $E _ {\mathrm{t}}$ means the certain thermal damage has less influence on HT performance, indicating the better damage tolerance for the HT path. $E _ {\mathrm{t}}$ is obtained as:

$$E _ {\mathrm{t}} = \left[ \begin{array} {l} {0.149 {\cdot} \beta ^ {2} + 4.53 {\cdot} \beta + 2119 {\cdot} \left( \frac {T _ {\mathrm{f}} - T _ {\mathrm{r}}} {T _ {\mathrm{lim}} - T _ {\mathrm{r}}} \right) ^ {2}} \\ {- 16.36 {\cdot} \frac {T _ {\mathrm{f}} - T _ {\mathrm{r}}} {T _ {\mathrm{lim}} - T _ {\mathrm{r}}} - 50.34 {\cdot} \beta {\cdot} \frac {T _ {\mathrm{f}} - T _ {\mathrm{r}}} {T _ {\mathrm{lim}} - T _ {\mathrm{r}}} - 30.54} \end{array} \right] ^ {- 1}\tag{28}$$

Fig. 20 shows that sample No. 3 with $\beta = 13.5$ and $T _ {\mathrm{f}} = 383 \mathrm{K}$ has the best thermal performance but the worst predictions with the minimum V of 3.55%. For this sample, $T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and $s _ {T}$ are 428.19 K, 549.58 K, and 36.69 K, respectively; $T ^ {*} {} _ {\mathrm{avg}} , T ^ {*} {} _ {\mathrm{max}} ,$ and $S ^ {*} {} _ {T}$ are 429.53 K, 743.53 K, and 46.89 K, respectively; the deviations of $T _ {\mathrm{avg}} , T _ {\mathrm{max}}$ , and ST are all positive as values of 0.31%, 35.29%, and 27.82%, respectively. Sample No. 5 with $\beta = 14.5$ and $T _ {\mathrm{f}} = 378$ K has the best fitting results with $V =$ 13.14%. For this sample, Tavg, Tmax, and $s _ {T}$ are 492.97 K, 1769.97 K, and 240.43 $\mathrm{K,}$ respectively; $T ^ {*} {\mathrm{avg}} , T ^ {*} {\mathrm{max}} ,$ , and $S ^ {*} {} _ {T}$ are 494.75 K, 1752.31 $\mathrm{K,}$ and 238.76 K, respectively; the deviations of $T _ {\mathrm{avg}} , \ T _ {\mathrm{max}} ,$ and $s _ {T}$ are 0.36%, − 1.00%, and − 0.69%, respectively.

Results of nine additional samples in Fig. 20 prove the reliability of the prediction model, and further show that the model is effective in the characterization of thermal damage and damage tolerance. It can be concluded that: (a) The tolerance indicating model can be used to predict the thermal performance of the HT path with non-thermal damage, and the maximum deviations of the tolerance indicating model are

(c) Results with $V _ {0} = 9 \% , R _ {0} = 2$ 3mm 
(d) Results with $V _ {0} = 9 \%$ $R _ {0} = 3$ .7mm

0.90%, − 1.50%, and − 4.82% for $T _ {\mathrm{avg}} , T _ {\mathrm{max}} ,$ and $s _ {T} ,$ respectively, when the damage volume fraction is larger than 10.98% (sample $1 ) ; \left( \mathbf {b} \right) T _ {\mathrm{avg}}$ has the best prediction with the maximum deviation of 1.2%, because it is the average result of the HT path; (c) The prediction accuracy of $T _ {\mathrm{max}}$ and $S _ {T}$ improves with increasing β and decreasing $T _ {\mathrm{f}} ( \mathrm{i.e.} _ {\cdot}$ , increasing V). The deviation of $T _ {\mathrm{max}}$ is less than 6% when $V$ is greater than 6.93% (sample 2), while the deviation of $S _ {T}$ is less than 5% when V is greater than 10.98% (sample 1); (d) The damage tolerance is increasing with decreasing β and increasing $T _ {\mathrm{f}} \left( \mathrm{i.e.,} \right$ , decreasing $V ,$ the maximum damage tolerance is 0.787 for sample 3 with $\beta = 13.5$ and $T _ {\mathrm{f}} = 383 \ \mathrm{K} ,$ the minimum damage tolerance is 0.13 for sample 7 with $\beta = 15.5$ and $T _ {\mathrm{f}} =$ 373 K.

## 6.3.3. The relationships between volume fraction and damage tolerance

Based on the studies of non-thermal and thermal damages above, Fig. 21 shows the relationships between volume fraction and damage tolerance. The non-thermal damage tolerance $E _ {\mathrm{nt}}$ and thermal damage tolerance $E _ {\mathrm{t}}$ are obtained by Eqs. (27) and (28), respectively. Orange circles represent the results for forty samples of non-thermal damage, with a polynomial fitting result of $E _ {\mathrm{nt}}$ shown by the orange dashed line. Blue triangles represent the results for nine samples of thermal damage, with a polynomial fitting result of $E _ {\mathrm{t}}$ shown by the blue line. The temperature distributions of HT paths with non-thermal damage of $V =$ 13.48%, and thermal damage of $V = 13.14 \%$ are also shown in Fig. 21. It can be found that variations of non-thermal and thermal damage tolerance along with the volume fractions are similar, but $E _ {\mathrm{t}}$ is less than $E _ {\mathrm{nt}}$ with the same volume fraction, which indicates that for the dendric HT path, the tolerance of non-thermal damage is better than that of thermal damage under the same damage level.

## 7. Conclusion

In this work, two damage tolerance indicating models for an HT system with a dendritic path are established. The study case based on a typical VP problem is obtained using topologic optimization. A stochastic model and a probability model are constructed to characterize the non-thermal and thermal damages. The non-thermal damage caused by various non-thermal loads like corrosion, vibration, impact, etc. is described by a stochastic model of the radius and the volume fraction, and the thermal damage generated with the increasing temperature is described by a probability model of the maximum gradient of damage probability and the constraint temperature. The non-thermal and thermal damage models are obtained based on the numerical data, and the damage tolerances for the dendric HT path are calculated by the indicating models.

## The results show some conclusions:

1. The damage tolerance indicating models encompass the average temperature, $T _ {\mathrm{avg}} ,$ the maximum temperature, $T _ {\mathrm{max}} ,$ , and the standard deviation of temperature, $s _ {T} ,$ to evaluate the thermal performance of an HT path.

2. For non-thermal damages, the damage region increases while the thermal performance and tolerance decreases with the increasing volume fraction, V and radius, R of damage; however, the random ness of damages will lead to some singularities, especially for $T _ {\mathrm{max}}$

3. For thermal damages, the transition region increases, the hightemperature region decreases and the damage tolerance of the HT path is thus enhanced with the decrease of the maximum damage probability gradient, β and the increase of constraint temperature, $T _ {\mathrm{f}}$

4. The tolerances of non-thermal damages vary between 0.302 and 0.926 when the volume fraction and radius vary between 2.12% to 16.33% and 0.94 mm to 5.00 mm; the maximum deviations of the damage model are $0.83 \% , \ - 7.54 \%$ , and 7.90% for average $T _ {\mathrm{avg}} ,$ $T _ {\mathrm{max}} ,$ and $s _ {T} ,$ respectively.

5. The tolerances of thermal damages vary between 0.13 and 0.787 when $\beta$ and $T _ {\mathrm{f}}$ vary between 13.5 to 15.5 and 373 K to 383 K; the maximum deviations of the damage model are $0.90 \% , - 1.50 \%$ , and − 4.82% for average $T _ {\mathrm{avg}} , \ T _ {\mathrm{max}} ,$ , and $s _ {T} ,$ respectively, when the damage volume fraction is larger than 10.98%.

6. For a dendritic HT path with certain damages, the thermal performance can be obtained by the damage models, and the tolerance of non-thermal damage is better than that of thermal damage under the same damage level.

## CRediT authorship contribution statement

Jia-Xin Hu: Conceptualization, Methodology, Formal analysis, Investigation, Visualization, Writing – original draft. Li-Qiang Ai: Data curation, Writing – review & editing, Funding acquisition. Nan Liu: Validation, Resources, Writing – review & editing. Jian-Jun Gou: Supervision, Writing – review & editing, Funding acquisition. Chun-Lin Gong: Conceptualization, Resources, Supervision, Project administration.

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
