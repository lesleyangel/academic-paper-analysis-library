## 1. Introduction

The technology development conducts the future launch vehicle to be durable, operable and cost effective [2]. Future space vehicles require more advanced thermal protection system (TPS) than the one currently used. This means that the TPS not only withstands serious temperature induced by aero-heating during launch and re-entry process, but also should be required to be lightweight, easily maintained and fully reusable [3]. Because the traditional TPS is unable to satisfy the requirements, the integrated thermal protection system (ITPS) concept has been developed to meet these goals, which provides an integrated structural component for thermo-mechanical load bearing and thermal protection function [4]. The ITPS using metallic materials and trapezoidal corrugated cores is presented in this article. The characteristic of fully reusable is the key feature for the future vehicle, hence a precise and rapidly stress analysis of the ITPS under thermal and mechanical loads is important in the reliable design.

The stress analysis of corrugated-core ITPS is more complicated than sandwich panels with continuous cores due to the discrete geometrical forms of the cores. As a result, many authors investigate the stress analysis of ITPS by 3D finite element method (FEM). The 3D FEM not only captures the stress distribution accurately, but also is capable of taking into account the complicate boundary conditions and the effects of temperature-dependent material properties. Many authors have studied the stress analysis of corrugated-core ITPS by 3D FEM.

Bapanapalli [5] put forward the concept of ITPS first, and studied the ITPS design approach by using 3D FEM. Sharma [6] developed a multifidelity design for the corrugated-core ITPS based on 3D FEM. Rajesh [7] also investigated the bending, vibration behaviors of corrugatedcore panel by using this method. However, the 3D FEM is time consuming for calculating the stress distribution of complicate geometrical structures, so that it is unable to satisfy the fast requirement of preliminary design.

In order to predict the static behaviors of this periodic structural plates economy, homogenization technique is required [8]. The earliest estimation of equivalent elastic properties of corrugated plate was found in the work of Seydel [9]. Since then, several authors have analyzed these corrugated core sandwich plates, see Refs. [10,11]. Until Briassoulis’s study [12] using Castigliano’s second theorem was developed, the precise of extensional and flexural rigidities of the corrugated plates was improved greatly. Following the approach introduced by Briassoulis, the transverse stiffness is not negligible for modeling thick plate in the study of Shimansky [13]. Samanta et al. [14] derived new formulas for the equivalent extensional rigidity of trapezoidal corrugated plates based on energy methods, and carried out static and dynamic analysis on the corrugated plates. Lewinski et al. [15] determined the transverse shear modulus for trapezoidal corrugated cores of sandwich plates by Castigliano’s second theorem. Liew et al. [16] proposed a mesh-free Galerkin method for the free vibration analysis of corrugated plates using the homogenization method based on the first shear deformation theory. Bartolozzi et al. [17] presented a new analytical technique for deriving the in-plane and out-of-plane equivalent rigidities of sinusoidal corrugated plates. Mohammadi et al. [18] following Bartolozzi’ s method had formulated the equivalent rigidities of trapezoidal corrugated plates. Gu et al. [1] presented an advanced method for the equivalent properties of corrugated-core ITPS based on energy approach and Castigliano’s second theorem. The method has ability to consider the effects of temperature dependent material properties.

By using the homogenization techniques, the entire panel can be analyzed as an equivalent sandwich plate, and the corrugated core is homogenized as an orthotropic layer [19]. Martinez [19] presented an analytical solution based on the first shear deformation theory (FSDT) to deal with the bending analysis of corrugated cores ITPS. Lewinski et al. [20–23] applied the homogenization techniques to calculate the bending, stability and vibrations of seven-layer beam and plate with trapezoidal corrugated cores. Plagianakos et al. [24] developed a higher-order layerwise theoretical framework, which enables prediction of the static response of thick sandwich composite plates. Pandey [25] presented a new layerwise plate formulation based on a ${\mathsf{C}} ^ {0}$ higherorder finite element model for static and free vibration analysis of sandwich plates. By combining with the study of Plagianakos and Pandey, Gu et al. [1] developed a new layerwise theory for solving the bending and dynamic analysis of trapezoidal corrugated core ITPS, which assumed higher-order displacement field for middle thick layer and first-order displacement field for top and bottom thin layers, and globally smeared through the laminate thickness.

The equivalent homogenization method can predict the structural displacement accurately, but it is difficult to get the stress distribution of the discrete geometrical structures [26]. Only a few researchers studied the approach for prediction of stress in web-core panel based on equivalent model without considering the influence of temperature. Romanoff [27,28] presented an analytical solution for the bending response of corrugated-core beams and plates. The stress analysis method in Martinez’s investigation [19] is developed by taking advantage of analytical method and FEM model, which can calculating the stress distribution of ITPS under thermal and mechanical loads. However, the method is incapable of solving the problem with taking into account the effects of transverse normal strain and temperature dependent material properties. A semi-analytical method for bending analysis of discrete core structures have been investigated by He [26], which captures the structural stress fluctuation accurately, but the method is incapable of predicting the stress in corrugated webs. While the prediction of stress is also introduced in the investigation of Gu [1], the normal stresses in the mid-plane of different sheets are carried out only. Currently, the max stress takes place at the surfaces of sheet due to thin plate easily occurs bending, therefore, the stress in the mid-plane is not enough to reflect the actual fact.

The objective of this paper is to propose an accurate and fast approach for calculating stress distribution of trapezoidal corrugated core ITPS under thermal and mechanical loads. The ITPS panel is homogenized into a thick sandwich plate. The temperature field for the entire panel is reduced according to the geometry of the corrugated-core. Based on the equivalent homogenized method and the ${\mathsf{C}} ^ {0}$ higher-order layerwise theory by our previous study [1], the approach for predicting stress distribution of ITPS is presented. By applying the equivalent sandwich model, the normal stresses and in-plane shear stresses in corrugated webs, top face sheet and bottom face sheet are calculated. In the prediction of stress, the influence of curvature is considered in the calculation of normal stresses. In addition, combining with the principle of structural mechanics, the stresses in the top face sheet caused by transverse pressure and those in the bottom face sheet induced from corrugated webs are involved in our study. The accuracy of the proposed method is verified by comparing with the available results from 3D FEM.

## 2. Homogenization method

As Figs. 1 and 2 shown, the ITPS panel is homogenized as an equivalent sandwich plate. Therefore, homogenization technique of the corrugated panel is necessary to study. In this section, the equivalent properties with temperature-dependent material properties needed to model a trapezoidal corrugated core are introduced. Fig. 1 shows a typical corrugated core panel with the key dimensions including the sheet thickness $h _ {1}$ and $h _ {3} ,$ the core sheet thickness $t _ {w} ,$ the core height $h _ {2} ,$ the web angle of the corrugation $\theta ,$ the core sheet spacing $p ,$ and the panel length and width a and b. In addition, Fig. 2 shows an equivalent sandwich plate with the key dimensions including the location of lower and upper surfaces of each layer $z _ {l} ^ {( 1 )} , z _ {u} ^ {( 1 )} , z _ {l} ^ {( 2 )} , z _ {u} ^ {( 2 )} , z _ {l} ^ {( 3 )} , z _ {u} ^ {( 3 )} . E _ {w} , \mu _ {w}$ and $\alpha _ {w}$ are the Young’s modulus, Poisson’s ratio and coefficient of thermal expansion of the isotropic material used to build the trapezoidal corrugated core.

## 2.1. Reduced temperature fields

Before the equivalent properties are derived, the temperature field of the ITPS panel is simplified in this subsection. $\Delta {T} ^ {( 1 )} ( x , y , z ) ;$ $\Delta {T} ^ {( 2 )} \left( x , y , z \right)$ and $\Delta T ^ {( 3 )} \left( x , y , z \right)$ are defined as the temperature fields for the bottom face sheets, the entire corrugated core and the top face sheets, respectively. As shown in Fig. 1, the ITPS panel is composed of two outer face sheets and a trapezoidal corrugated core. The height of the corrugated core needs to be thick enough to maintain the temperature of underlying structures within acceptable limits, and the outer face sheets are thin in comparison with the core. Therefore, the temperature fields through the thickness of the outer face sheets are treated as uniform. As a result, the variable z in $\Delta {T} ^ {( 1 )} \left( x , y , z \right)$ and $\Delta T ^ {( 3 )} \left( x , y , z \right)$ are vanished, and the temperature fields for the bottom and top face sheets are reduced to:

$$\Delta T ^ {( 1 )} = \Delta T ^ {( 1 )} ( x , y ) , \Delta T ^ {( 3 )} = \Delta T ^ {( 3 )} ( x , y )\tag{1}$$

The temperature field $\Delta {T} ^ {( 2 )} \left( x , y , z \right)$ for a unit cell that build the corrugated core can be divided into two parts Block 1 and Block 2 as shown in Fig. 3. For the Block 1, the temperature fields of part AB and CD are assumed to be uniform in y-direction in the half unit cell, because the length of the two parts in y-direction is significant short with respect to the length in x-direction, and the gradient of temperature distributions of the two parts in y-direction is small. The temperature fields for the horizontal corrugated sheets as parts AB and CD are reduced to $\Delta T ^ {( 2 )} ( x , y = y _ {B} , z = z _ {l} ^ {( 2 )} )$ and $\Delta T ^ {( 2 )} ( x , y = y _ {C} , z = z _ {u} ^ {( 2 )} )$ respectively, where $y _ {B}$ and yC are the location of point B and point C in ydirection. For the inclined corrugated sheets as part $B C ,$ the variable y in the temperature field $\Delta {T} ^ {( 2 )} \left( x , y , z \right)$ is replaced by $\begin{array} {r} {y _ {B} + \frac {z - z _ {l} ^ {( 2 )}} {\tan \theta}} \end{array}$

For the Block 2, the temperature fields for part A′B′ and C′D are reduced to $\Delta T ^ {( 2 )} ( x , y = y _ {B ^ {'}} , z = z _ {l} ^ {( 2 )} )$ and $\Delta T ^ {( 2 )} ( x , y = y _ {C ^ {'}} , z = z _ {u} ^ {( 2 )} )$ , respectively, where $y _ {B ^ {'}}$ and $y _ {C ^ {'}}$ are the location of point B′ and point C′ in y-direction. For part BC, the variable $y$ in the temperature field $\Delta {T} ^ {( 2 )} \left( x , y , z \right)$ is replaced by $y _ {B ^ {'}} - \frac {z - z _ {l} ^ {( 2 )}} {\mathrm{tan} \theta}$ . By using the treatment described above, the variable y in the temperature field for the entire core can be vanished, thus $\Delta {T} ^ {( 2 )} \left( x , y , z \right)$ will be reduced to a function with respect to x and ${\mathfrak {z}} ,$ which is given by:

$$\Delta T ^ {( 2 )} ( x , y , z ) = \Delta T _ {r} ^ {( 2 )} ( x , z )\tag{2}$$

## 2.2. Equivalent elastic properties

According to Bartolozzi’s study [17], a unit cell of the corrugated core can be divided into four sections by its center line as shown in $\mathrm{Fig} . \ 3 ,$ , and the origin of coordinate system is set at point O and the structure has a clamped boundary condition at this point from the study by Mohammadi [18]. Then the width of the corrugated core in $x \cdot$ direction is assumed to be significant small, hence the temperature distribution can be considered as uniform along x-direction. And a new homogenization approach for the problem of temperature-dependent material properties developed in our previous study [1] is used to formulate the equivalent properties.

Using the approach by Gu [1], the temperature-dependent equivalent elastic modulus in x-direction $E _ {x} ^ {( 2 )}$ , the equivalent elastic modulus in y-direction $E _ {y} ^ {( 2 )} :$ , the equivalent elastic modulus in z-direction $E _ {z} ^ {( 2 )}$ , the equivalent transverse shear modulus in yz-plane $G _ {y z} ^ {( 2 )}$ , the equivalent transverse shear modulus in xz-plane $G _ {x z} ^ {( 2 )}$ , and the equivalent in-plane shear modulus $G _ {x y} ^ {( 2 )}$ for the corrugated core are derived as:

$$E _ {x} ^ {( 2 )} = {\frac {t _ {w}} {p d _ {f}}} {\left( \int _ {0} ^ {d _ {f}} E _ {w} ^ {1} {\frac {d z ^ {\prime}} {\sin \theta}} + \int _ {\frac {d _ {f}} {\tan \theta}} ^ {\frac {p} {2}} E _ {w} ^ {2} d y ^ {\prime} \right)}\tag{3}$$

$$E _ {y} ^ {( 2 )} = \frac {t _ {w} p} {d _ {f} ( C _ {11} - ( C _ {13} ) ^ {2} / C _ {33} )}\tag{4}$$

$$E _ {z} ^ {( 2 )} = \frac {t _ {w} d _ {f} \mathrm{det} ( C _ {r} ^ {z} )} {p \mathrm{det} ( C ^ {z} )}\tag{5}$$

$$G _ {y z} ^ {( 2 )} = \frac {t _ {w} d _ {f} \mathrm{det} ( {\pmb C} _ {r} )} {p \mathrm{det} ( {\pmb C} )}\tag{6}$$

$$G _ {x z} ^ {( 2 )} = \frac {t _ {w} d _ {f}} {2 ( 1 + \mu _ {w} ) p \left( \int _ {0} ^ {d _ {f}} \frac {1} {E _ {w} ^ {1}} \frac {\mathrm{d} z ^ {\prime}} {\mathrm{sin} \theta} + \int _ {\frac {d _ {f}} {\mathrm{tan} \theta}} ^ {\frac {p} {2}} \frac {1} {E _ {w} ^ {2}} \mathrm{d} y ^ {\prime} \right)}\tag{7}$$

$$G _ {x y} ^ {( 2 )} = \frac {t _ {w}} {2 ( 1 + \mu _ {w} ) p d _ {f}} ( \int _ {0} ^ {d _ {f}} E _ {w} ^ {1} \frac {\mathrm{d} z ^ {\prime}} {\mathrm{sin} \theta} + \int _ {\frac {d _ {f}} {\mathrm{tan} \theta}} ^ {\frac {p} {2}} E _ {w} ^ {2} \mathrm{d} y ^ {\prime} )\tag{8}$$

where $E _ {w} ^ {1}$ is the temperature-dependent Young’s modulus for part $O C ,$ and $E _ {w} ^ {2}$ is the temperature-dependent Young’s modulus for part CD. By using the reduced temperature field $\mathrm{Eq.} ( 2 ) , E _ {w} ^ {1}$ is expressed as:

$$E _ {w} ^ {1} = E _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , z ) )\tag{9}$$

where, $\begin{array} {r} {z = \frac {z _ {l} ^ {( 2 )} + z _ {u} ^ {( 2 )}} {2} + z ^ {\prime}} \end{array}$ when $\frac {z _ {l} ^ {( 2 )} + z _ {u} ^ {( 2 )}} {2} \leqslant z \leqslant z _ {u} ^ {( 2 )}$ , and $\begin{array} {r} {z = \frac {z _ {l} ^ {( 2 )} + z _ {u} ^ {( 2 )}} {2} - z ^ {\prime}} \end{array}$ when $z _ {l} ^ {( 2 )} \leqslant z < \frac {z _ {l} ^ {( 2 )} + z _ {u} ^ {( 2 )}} {2}$ . And the shear modulus $\begin{array} {r} {G _ {w} ^ {1} = \frac {E _ {w} ^ {1}} {2 ( 1 + \mu _ {w} )} .} \end{array}$

In addition, when $\frac {z _ {l} ^ {( 2 )} + z _ {u} ^ {( 2 )}} {2} \leqslant z \leqslant z _ {u} ^ {( 2 )} , E _ {w} ^ {2}$ is obtained as:

$$E _ {w} ^ {2} = E _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , z = z _ {u} ^ {( 2 )} ) )\tag{10}$$

And when $z _ {l} ^ {( 2 )} \leqslant z < \frac {z _ {l} ^ {( 2 )} + z _ {u} ^ {( 2 )}} {2} , E _ {w} ^ {2}$ is obtained as:

$$E _ {w} ^ {2} = E _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , z = z _ {l} ^ {( 2 )} ) )\tag{11}$$

And the shear modulus $\begin{array} {r} {G _ {w} ^ {2} = \frac {E _ {w} ^ {2}} {2 ( 1 + \mu _ {w} )}} \end{array}$

In Eqs. (4) and (6), C is defined as ${\left[ \begin{array} {l l l} {C _ {11}} & {C _ {12}} & {C _ {13}} \\ & {C _ {22}} & {C _ {23}} \\ {s y m .} & & {C _ {33}} \end{array} \right]} ,$ , the details of coefficients of matrix C are highlighted in Appendix $\mathrm{A} ,$ and the matrix $c _ {r}$ is defined as $\left\lceil \begin{array} {l l} {C _ {22}} & {C _ {23}} \\ {C _ {23}} & {C _ {33}} \end{array} \right\rceil$

In Eq. (5), Cz is defined as $\left\{\begin{array} {l l l} {C _ {11} ^ {z}} & {C _ {12} ^ {z}} & {C _ {13} ^ {z}} \\ & {C _ {22} ^ {z}} & {C _ {23} ^ {z}} \\ {s y m .} & & {C _ {33} ^ {z}} \end{array} \right\} ,$ the details of coefficients of matrix $c ^ {z}$ are highlighted in Appendix B, and the matrix $C _ {r} ^ {z}$ is defined $\mathrm{as} \left[ {\begin{array} {l l} {C _ {11} ^ {z}} & {C _ {13} ^ {z}} \\ {C _ {13} ^ {z}} & {C _ {33} ^ {z}} \end{array}} \right]$

The equivalent Poisson’s ratio of the corrugated core are obtained as $\mu _ {x y} ^ {( 2 )} = \mu _ {w} , \mu _ {x z} ^ {( 2 )} = \mu _ {w} , \mu _ {y z} ^ {( 2 )} = 0$ (12)

## 2.3. Equivalent coefficients of thermal expansion

The temperature-dependent equivalent coefficients of thermal expansion $\pmb {\alpha} _ {T} ^ {( 2 )}$ for a half unit cell can be divided into three parts as shown in Fig. $3 . \alpha _ {T l} ^ {( 2 )} , \alpha _ {T 0} ^ {( 2 )}$ and $\pmb {\alpha} _ {T u} ^ {( 2 )}$ are the equivalent coefficients of thermal expansion for parts AB, BC and $C D _ {i}$ , respectively. $\alpha _ {T l} ^ {( 2 )} , \alpha _ {T u} ^ {( 2 )}$ are expressed as:

$$\alpha _ {T l} ^ {( 2 )} = \left[ 0 , \left( \frac {1} {2} - \frac {h _ {2}} {2 p \mathrm{tan} \theta} \right) \alpha _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , z = z _ {l} ^ {( 2 )} ) ) , 0 , 0 , 0 , 0 \right] ^ {\mathrm{T}}\tag{13}$$

$$\alpha _ {T u} ^ {( 2 )} = \left[ 0 , \left( \frac {1} {2} - \frac {h _ {2}} {2 p \mathrm{tan} \theta} \right) \alpha _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , z = z _ {u} ^ {( 2 )} ) ) , 0 , 0 , 0 , 0 \right] ^ {\mathrm{T}}\tag{14}$$

And ${\alpha} _ {T 0} ^ {( 2 )}$ is expressed as

$$\begin{array} {r l} & {\alpha _ {T 0} ^ {( 2 )} = \Bigg [ \alpha _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , z ) ) , \frac {h _ {2}} {p \tan \theta} \alpha _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , z ) ) , \alpha _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , z ) ) , 0 , c o t \theta} \\ & {\quad \quad \quad \alpha _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , z ) ) , 0 \Bigg ] ^ {\mathrm{T}}} \end{array}\tag{15}$$

when block 1 is selected as the half unit cell;

$$\begin{array} {r l} & {\alpha _ {T 0} ^ {( 2 )} = \Bigg [ \alpha _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , z ) ) , \frac {h _ {2}} {p \mathrm{tan} \theta} \alpha _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , z ) ) , \alpha _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , z ) ) , 0 , c o t ( \pi} \\ & {\qquad - \theta ) \alpha _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , z ) ) , 0 \Bigg ] ^ {\mathrm{T}}} \end{array}\tag{16}$$

when block 2 is selected as the half unit cell.

Consequently, the thermal strain vector $\pmb {\varepsilon _ {0} ^ {( 2 )}}$ for an half unit cell using the temperature fields Eqs. (1) and (2) is derived as:

$$\begin{array} {r l} & {\varepsilon _ {0} ^ {( 2 )} = \alpha _ {T} ^ {( 2 )} \Delta T ^ {( 2 )} ( x , y , z ) = \alpha _ {T 0} ^ {( 2 )} \Delta T _ {r} ^ {( 2 )} ( x , z ) + \alpha _ {T l} ^ {( 2 )} \Delta T _ {r} ^ {( 2 )} ( x , z = z _ {l} ^ {( 2 )} )} \\ & {\qquad + \alpha _ {T u} ^ {( 2 )} \Delta T _ {r} ^ {( 2 )} ( x , z = z _ {u} ^ {( 2 )} )} \end{array}\tag{17}$$

For bottom and top face sheets, the coefficients of thermal expansion $\pmb {\alpha} _ {T} ^ {( 1 )}$ and $\alpha _ {T} ^ {( 3 )}$ are written as:

$$\alpha _ {T} ^ {( 1 )} = \{\alpha _ {x} ^ {( 1 )} ( \Delta T ^ {( 1 )} ( x , y ) ) , \alpha _ {y} ^ {( 1 )} ( \Delta T ^ {( 1 )} ( x , y ) ) , 0 , 0 , 0 \} ^ {\mathrm{T}}\tag{18}$$

$$\alpha _ {T} ^ {( 3 )} = \{\alpha _ {x} ^ {( 3 )} ( \Delta T ^ {( 3 )} ( x , y ) ) , \alpha _ {y} ^ {( 3 )} ( \Delta T ^ {( 3 )} ( x , y ) ) , 0 , 0 , 0 \} ^ {\mathrm{T}}\tag{19}$$

where ${\alpha} _ {x} ^ {( k )}$ and ${\alpha} _ {v} ^ {( k )}$ are the coefficients of thermal expansion of the material used to build the outer face sheets in x and y directions as shown in Fig. 1.

## 3. Layerwise theory

After the equivalent properties of the corrugated panel have been known, a ${\sf C} ^ {0}$ higher-order finite element model is presented for the equivalent sandwich plate according to our previous work [1]. The theory assumes higher-order displacement field for middle layer and first-order displacement field for top and bottom layers. A higher-order layerwise theory by Plagianakos [24] is used for building the displacement field of the equivalent sandwich plate. The displacement field in middle layer through the thickness of the sandwich plate includes linear, quadratic and cubic polynominal distributions of the inplane displacements, in which the linear in-plane displacement field maintains the interlaminar displacement continuity. The effect of transverse normal strain is considered in the middle layer, so that linear, quadratic and cubic polynominal distributions are also included in out-of-plane displacement field of the middle layer. In this context, the displacement field in the middle layer takes the form:

$$\begin{array} {r l} & {u ^ {( 2 )} ( x , y , \zeta _ {( 2 )} ) = U ^ {( 2 )} ( x , y ) \Psi _ {1} ^ {( 2 )} ( \zeta _ {( 2 )} ) + U ^ {( 3 )} ( x , y ) \Psi _ {2} ^ {( 2 )} ( \zeta _ {( 2 )} )} \\ & {\phantom {u ^ {( 2 )} ( x , y ) \Psi _ {1} ^ {( 2 )} ( \zeta _ {( 2 )} )} + \alpha _ {x} ^ {( 2 )} ( x , y ) \Psi _ {4} ^ {( 2 )} ( \zeta _ {( 2 )} ) \nu ^ {( 2 )} ( x , y , \zeta _ {( 2 )} )} \\ & {\phantom {u ^ {( 2 )} ( x , y ) \Psi _ {1} ^ {( 2 )} ( \zeta _ {( 2 )} )} = V ^ {( 3 )} ( x , y ) \Psi _ {2} ^ {( 2 )} ( \zeta _ {( 2 )} )} \\ & {\phantom {u ^ {( 2 )} ( x , y ) \Psi _ {1} ^ {( 2 )} ( \zeta _ {( 2 )} )} + \alpha _ {y} ^ {( 2 )} ( x , y ) \Psi _ {4} ^ {( 2 )} ( \zeta _ {( 2 )} ) w ^ {( 2 )} ( x , y , \zeta _ {( 2 )} )} \\ & {\phantom {u ^ {( 2 )} ( x , y ) \Psi _ {1} ^ {( 2 )} ( \zeta _ {( 2 )} )} = W ^ {( 1 )} ( x , y ) \Psi _ {2} ^ {( 2 )} ( \zeta _ {( 2 )} )} \\ & {\phantom {u ^ {( 2 )} ( x , y ) \Psi _ {1} ^ {( 2 )} ( \zeta _ {( 2 )} )} + \lambda _ {z} ^ {( 2 )} ( x , y ) \Psi _ {4} ^ {( 2 )} ( \zeta _ {( 2 )} )} \end{array}\tag{20}$$

where $U ^ {( k )} , V ^ {( k )}$ and $U ^ {( k + 1 )} , V ^ {( k + 1 )}$ are the in-plane displacements at lower and upper surfaces of a kth layer (where $k = 1 , 2 , 3 )$ , and $W ^ {( 1 )} , W ^ {( 3 )}$ are the out-of-plane displacements of bottom and top layers, respectively. These terms represent the linear displacement field, effectively describing extension and rotation of the layer. The parameters $\Psi _ {1} ^ {( k )} , \Psi _ {2} ^ {( k )}$ are linear and $\Psi _ {3} ^ {( k )} , \Psi _ {4} ^ {( k )}$ are quadratic, cubic interpolation functions, respectively, through the kth layer thickness, as:

$$\begin{array} {l} {{\Psi _ {1} ^ {( k )} = ( 1 - \zeta _ {( k )} ) / 2 , \quad \Psi _ {2} ^ {( k )} = ( 1 + \zeta _ {( k )} ) / 2 , \quad \Psi _ {3} ^ {( k )} = {\displaystyle {\frac {h _ {k}} {2}}} ( \zeta _ {( k )} ^ {2} - 1 ) , \quad \Psi _ {4} ^ {( k )}}} \\ {{{}}} \\ {{{} = {\displaystyle {\frac {h _ {k}} {2}}} \zeta _ {( k )} ( \zeta _ {( k )} ^ {2} - 1 )}} \end{array}\tag{21}$$

and $\zeta _ {( k )}$ is the local thickness coordinate of the kth layer, which is given by:

$$\zeta _ {( k )} = \frac {2} {h _ {k}} z - \frac {z _ {l} ^ {( k )} + z _ {u} ^ {( k )}} {h _ {k}}\tag{22}$$

where $h _ {k}$ is the thickness of the kth layer, $z _ {l} ^ {( k )}$ and $z _ {u} ^ {( k )}$ are the z-axis coordinate of lower and upper surfaces of the kth layer as shown in Fig. 2, respectively.

Both bottom and top layers of the equivalent sandwich plate is used a first-order variation of in-plane displacement field, and the first-order displacement field is able to keep the interlaminar displacement continuity. In addition, transverse displacement for the bottom and top layers are considered to be uniform through the thickness. As a result, the linear in-plane displacement fields $U ^ {( k )} , V ^ {( k )}$ and $U ^ {( k + 1 )} , V ^ {( k + 1 )}$ are used in the in-plane displacements of bottom and top layers. In bottom and top layers, $W ^ {( 1 )}$ and $W ^ {( 3 )}$ are used in the out-of-plane displacements without taking into account the effects of transverse normal strain. The displacement fields for the bottom and top layers are given by:

$$\begin{array} {r l} & {u ^ {( 1 )} ( x , y , \zeta _ {( 1 )} ) = U ^ {( 1 )} ( x , y ) \Psi _ {1} ^ {( 1 )} ( \zeta _ {( 1 )} ) + U ^ {( 2 )} ( x , y ) \Psi _ {2} ^ {( 1 )} ( \zeta _ {( 1 )} ) v ^ {( 1 )} ( x , y , \zeta _ {( 1 )} )} \\ & {\qquad = V ^ {( 1 )} ( x , y ) \Psi _ {1} ^ {( 1 )} ( \zeta _ {( 1 )} ) + V ^ {( 2 )} ( x , y ) \Psi _ {2} ^ {( 1 )} ( \zeta _ {( 1 )} ) w ^ {( 1 )} ( x , y , \zeta _ {( 1 )} )} \\ & {\qquad = W ^ {( 1 )} ( x , y )} \end{array}\tag{23}$$

$$\begin{array} {l} {{u ^ {( 3 )} ( x , y , \zeta _ {( 3 )} ) = U ^ {( 3 )} ( x , y ) \Psi _ {1} ^ {( 3 )} ( \zeta _ {( 3 )} ) + U ^ {( 4 )} ( x , y ) \Psi _ {2} ^ {( 3 )} ( \zeta _ {( 3 )} ) v ^ {( 3 )} ( x , y , \zeta _ {( 3 )} )}} \\ {{\ \qquad = V ^ {( 3 )} ( x , y ) \Psi _ {1} ^ {( 3 )} ( \zeta _ {( 3 )} ) + V ^ {( 4 )} ( x , y ) \Psi _ {2} ^ {( 3 )} ( \zeta _ {( 3 )} ) w ^ {( 3 )} ( x , y , \zeta _ {( 3 )} )}} \\ {{\ \qquad = W ^ {( 3 )} ( x , y )}} \end{array}\tag{24}$$

## 3.1. Strain-displacement relations

The strain-displacement relations corresponding to Eqs. (20), (23) and (24) are given by:

For the middle layer,

$$\begin{array} {r l} & {\mathcal {E} _ {x x} ^ {( 2 )} = U _ {x} ^ {( 3 )} \Psi _ {1} ^ {( 1 )} + U _ {x} ^ {( 3 )} \Psi _ {2} ^ {( 2 )} + \alpha _ {x x} ^ {( 2 )} \Psi _ {3} ^ {( 2 )} + \lambda _ {x y} ^ {( 3 )} \Psi _ {4} ^ {( 2 )} \xi _ {x y} ^ {( 2 )}} \\ & {\quad = V _ {y y} ^ {( 3 )} \Psi _ {1} ^ {( 1 )} + V _ {y} ^ {( 3 )} \Psi _ {2} ^ {( 2 )} + \alpha _ {y y} ^ {( 3 )} \Psi _ {3} ^ {( 2 )} + \lambda _ {y y} ^ {( 3 )} \Psi _ {4} ^ {( 2 )} \xi _ {x z} ^ {( 2 )}} \\ & {\quad = \frac {W ^ {( 3 )} - W ^ {( 1 )}} {h _ {2}} + 2 \zeta _ {( 2 )} \alpha _ {z} ^ {( 2 )} + ( 3 \zeta _ {( 2 )} ^ {2} - 1 ) \lambda _ {z} ^ {( 2 )} \gamma _ {y z} ^ {( 2 )} = W _ {y} ^ {( 1 )} \Psi _ {1} ^ {( 2 )} + W _ {y} ^ {( 3 )} \Psi _ {2} ^ {( 2 )}} \\ & {\quad \quad + \alpha _ {z y} ^ {( 2 )} \Psi _ {3} ^ {( 2 )} + \lambda _ {z y} ^ {( 2 )} \Psi _ {4} ^ {( 2 )} + \frac {V ^ {( 3 )} - V ^ {( 2 )}} {h _ {2}} + 2 \zeta _ {( 2 )} \alpha _ {y} ^ {( 3 )} + ( 3 \zeta _ {( 2 )} ^ {2} - 1 ) \lambda _ {y} ^ {( 2 )} \gamma _ {x z} ^ {( 2 )}} \\ & \quad = W _ {x} ^ {( 1 )} \Psi _ {1} ^ {( 2 )} + W _ {x} ^ {( 3 )} \Psi _ {2} ^ {( 2 )} + \alpha _ {x x} ^ ( 2 ) \end{array}$$

For the bottom layer,

$$\begin{array} {r l} & {\varepsilon _ {x x} ^ {( 1 )} = U _ {, x} ^ {( 1 )} \Psi _ {1} ^ {( 1 )} + U _ {, x} ^ {( 2 )} \Psi _ {2} ^ {( 1 )} \varepsilon _ {y y} ^ {( 1 )} = V _ {, y} ^ {( 1 )} \Psi _ {1} ^ {( 1 )} + V _ {, y} ^ {( 2 )} \Psi _ {2} ^ {( 1 )} \gamma _ {y z} ^ {( 1 )}} \\ & {\quad \quad = W _ {, y} ^ {( 1 )} + \frac {V ^ {( 2 )} - V ^ {( 1 )}} {h _ {1}} \gamma _ {x z} ^ {( 1 )} = W _ {, x} ^ {( 1 )} + \frac {U ^ {( 2 )} - U ^ {( 1 )}} {h _ {1}} \gamma _ {x y} ^ {( 1 )}} \\ & {\quad \quad = U _ {, y} ^ {( 1 )} \Psi _ {1} ^ {( 1 )} + U _ {, y} ^ {( 2 )} \Psi _ {2} ^ {( 1 )} + V _ {, x} ^ {( 1 )} \Psi _ {1} ^ {( 1 )} + V _ {, x} ^ {( 2 )} \Psi _ {2} ^ {( 1 )}} \end{array}\tag{26}$$

For the top layer,

$$\begin{array} {r l} & {\varepsilon _ {x x} ^ {( 3 )} = U _ {, x} ^ {( 3 )} \Psi _ {1} ^ {( 3 )} + U _ {, x} ^ {( 4 )} \Psi _ {2} ^ {( 3 )} \varepsilon _ {y y} ^ {( 3 )} = V _ {, y} ^ {( 3 )} \Psi _ {1} ^ {( 3 )} + V _ {, y} ^ {( 4 )} \Psi _ {2} ^ {( 3 )} \gamma _ {y z} ^ {( 3 )}} \\ & {\quad \quad = W _ {, y} ^ {( 3 )} + \frac {V ^ {( 4 )} - V ^ {( 3 )}} {h _ {3}} \gamma _ {x z} ^ {( 3 )} = W _ {, x} ^ {( 3 )} + \frac {U ^ {( 4 )} - U ^ {( 3 )}} {h _ {3}} \gamma _ {x y} ^ {( 3 )}} \\ & {\quad \quad = U _ {, y} ^ {( 3 )} \Psi _ {1} ^ {( 3 )} + U _ {, y} ^ {( 4 )} \Psi _ {2} ^ {( 3 )} + V _ {, x} ^ {( 3 )} \Psi _ {1} ^ {( 3 )} + V _ {, x} ^ {( 4 )} \Psi _ {2} ^ {( 3 )}} \end{array}\tag{27}$$

## 3.2. Stress-strain relations

The stress-strain relation for any discrete layer is assumed to exhibit linear elastic behavior. The constitutive equation of the equivalent sandwich plate subjected to thermal loads has the form:

$${\pmb \sigma} ^ {( k )} = {\pmb Q} ^ {( k )} ( {\pmb \varepsilon} ^ {( k )} - {\pmb \varepsilon} _ {\bf 0} ^ {( k )} )\tag{28}$$

where $Q ^ {( k )}$ is the stiffness matrix of a kth layer, and ${\pmb \sigma} ^ {( k )} , {\pmb \varepsilon} ^ {( k )}$ and $\pmb {\varepsilon _ {0} ^ {( k )}}$ are the stress, strain and thermal strain vectors, respectively.

For the middle layer, the stiffness matrix $Q ^ {( 2 )}$ can be written in a general symmetric matrix form as:

$$Q ^ {( 2 )} = \left[ \begin{array} {c c c c c c c} {Q _ {11} ^ {( 2 )}} & {Q _ {12} ^ {( 2 )}} & {Q _ {13} ^ {( 2 )}} & {0} & {0} & {0} \\ {Q _ {12} ^ {( 2 )}} & {Q _ {22} ^ {( 2 )}} & {Q _ {23} ^ {( 2 )}} & {0} & {0} & {0} \\ {Q _ {13} ^ {( 2 )}} & {Q _ {23} ^ {( 2 )}} & {Q _ {33} ^ {( 2 )}} & {0} & {0} & {0} \\ {0} & {0} & {0} & {Q _ {44} ^ {( 2 )}} & {0} & {0} \\ {0} & {0} & {0} & {0} & {Q _ {55} ^ {( 2 )}} & {0} \\ {0} & {0} & {0} & {0} & {0} & {Q _ {66} ^ {( 2 )}} \end{array} \right]\tag{29}$$

where

$$\begin{array} {r l} & {Q _ {11} ^ {( 2 )} = \cfrac {1 - \mu _ {y z} ^ {( 2 )} \mu _ {z y} ^ {( 2 )}} {E _ {y} ^ {( 2 )} E _ {z} ^ {( 2 )} \Delta ^ {( 2 )}} , \quad Q _ {12} ^ {( 2 )} = \cfrac {\mu _ {y x} ^ {( 2 )} + \mu _ {z x} ^ {( 2 )} \mu _ {y z} ^ {( 2 )}} {E _ {y} ^ {( 2 )} E _ {z} ^ {( 2 )} \Delta ^ {( 2 )}} , \quad Q _ {22} ^ {( 2 )}} \\ & {\phantom {\frac {0} {1 - \mu _ {x z} ^ {( 2 )} \mu _ {z x} ^ {( 2 )}}} = \cfrac {1 - \mu _ {x y} ^ {( 2 )} \mu _ {z x} ^ {( 2 )}} {E _ {x} ^ {( 2 )} E _ {z} ^ {( 2 )} \Delta ^ {( 2 )}} , \quad Q _ {23} ^ {( 2 )} = \cfrac {\mu _ {z y} ^ {( 2 )} + \mu _ {x y} ^ {( 2 )} \mu _ {z x} ^ {( 2 )}} {E _ {x} ^ {( 2 )} E _ {z} ^ {( 2 )} \Delta ^ {( 2 )}} , \quad Q _ {33} ^ {( 2 )} = \cfrac {1 - \mu _ {x y} ^ {( 2 )} \mu _ {y x} ^ {( 2 )}} {E _ {x} ^ {( 2 )} E _ {y} ^ {( 2 )} \Delta ^ {( 2 )}} ,} \end{array}$$

$$Q _ {13} ^ {( 2 )} = \frac {\mu _ {x z} ^ {( 2 )} + \mu _ {x y} ^ {( 2 )} \mu _ {y z} ^ {( 2 )}} {E _ {x} ^ {( 2 )} E _ {y} ^ {( 2 )} \Delta ^ {( 2 )}} , Q _ {44} ^ {( 2 )} = G _ {y z} ^ {( 2 )} , \quad Q _ {55} ^ {( 2 )} = G _ {x z} ^ {( 2 )} , \quad Q _ {66} ^ {( 2 )} = G _ {x y} ^ {( 2 )}$$

$$\begin{array} {l} {{\Delta ^ {( 2 )} = \displaystyle \frac {1} {E _ {x} ^ {( 2 )} E _ {y} ^ {( 2 )} E _ {z} ^ {( 2 )}} | \begin{array} {c c} {{1 \quad - \mu _ {y x} ^ {( 2 )} - \mu _ {z x} ^ {( 2 )}}} \\ {{- \mu _ {x y} ^ {( 2 )} 1 \quad - \mu _ {z y} ^ {( 2 )} | , \mu _ {y x} ^ {( 2 )} = \displaystyle \frac {E _ {y} ^ {( 2 )}} {E _ {x} ^ {( 2 )}} \mu _ {x y} ^ {( 2 )} ,}} \\ {{- \mu _ {x z} ^ {( 2 )} - \mu _ {y z} ^ {( 2 )} 1}} \end{array} | \mu _ {y} ^ {( 2 )} ,}} \\ {{\phantom {\Delta ^ {( 2 )} = \displaystyle \frac {E _ {z} ^ {( 2 )}} {E _ {x} ^ {( 2 )}} \mu _ {x z} ^ {( 2 )} ,} \quad \quad \mu _ {z y} ^ {( 2 )} = \displaystyle \frac {E _ {z} ^ {( 2 )}} {E _ {y} ^ {( 2 )}} \mu _ {y z} ^ {( 2 )}}} \end{array}$$

And the vectors $\pmb {\sigma} ^ {( 2 )} , \pmb {\varepsilon} ^ {( 2 )}$ and $\pmb {\varepsilon _ {0}} ^ {( 2 )}$ for the middle layer are written as:

$${\pmb {\sigma}} ^ {( 2 )} = [ \sigma _ {x x} ^ {( 2 )} \qquad \sigma _ {y y} ^ {( 2 )} \qquad \sigma _ {z z} ^ {( 2 )} \qquad \sigma _ {y z} ^ {( 2 )} \qquad \sigma _ {x z} ^ {( 2 )} \qquad \sigma _ {x y} ^ {( 2 )} \qquad \sigma _ {x y} ^ {( 2 )} ] ^ {T}\tag{30}$$

$$\varepsilon ^ {( 2 )} = [ \varepsilon _ {x x} ^ {( 2 )} \varepsilon _ {y y} ^ {( 2 )} \varepsilon _ {z z} ^ {( 2 )} \gamma _ {y z} ^ {( 2 )} \gamma _ {x z} ^ {( 2 )} \gamma _ {x y} ^ {( 2 )} T ^ {( 2 )}\tag{31}$$

$$\begin{array} {r} {\varepsilon _ {\boldsymbol {\mathfrak {0}}} ^ {( 2 )} = [ \varepsilon _ {0 x x} ^ {( 2 )} \qquad \varepsilon _ {0 y y} ^ {( 2 )} \qquad \varepsilon _ {0 z z} ^ {( 2 )} \qquad \gamma _ {0 y z} ^ {( 2 )} \qquad \gamma _ {0 x z} ^ {( 2 )} \qquad \gamma _ {0 x y} ^ {( 2 )} T ^ {( 2 )}} \end{array}\tag{32}$$

For the bottom and top layers, $Q ^ {( k )}$ will be ${\mathrm{~\AA~}} 5 \times 5$ stiffness matrix with respect to global x-y axis, where $k = 1$ or 3. $Q ^ {( k )}$ is given by:

$$Q ^ {( k )} = \left[ \begin{array} {c c c c c} {{\widetilde Q _ {11} ^ {( k )}}} & {{\widetilde Q _ {12} ^ {( k )}}} & {{0}} & {{0}} & {{0}} \\ {{\widetilde Q _ {12} ^ {( k )}}} & {{\widetilde Q _ {22} ^ {( k )}}} & {{0}} & {{0}} & {{0}} \\ {{0}} & {{0}} & {{Q _ {44} ^ {( k )}}} & {{0}} & {{0}} \\ {{0}} & {{0}} & {{0}} & {{Q _ {55} ^ {( k )}}} & {{0}} \\ {{0}} & {{0}} & {{0}} & {{0}} & {{Q _ {66} ^ {( k )}}} \end{array} \right]\tag{33}$$

where $\widetilde {Q} _ {i j} ^ {( k )} = Q _ {i j} ^ {( k )} - \frac {Q _ {i 3} ^ {( k )} Q _ {j 3} ^ {( k )}} {Q _ {33} ^ {( k )}}$ = i( , 1,2,3) j

And the vectors $\pmb {\sigma} ^ {( k )} , \pmb {\varepsilon} ^ {( k )}$ and $\pmb {\varepsilon _ {0} ^ {( k )}}$ for bottom and top layers can be written as:

$$\pmb {\sigma} ^ {( k )} = [ \sigma _ {x x} ^ {( k )} \qquad \sigma _ {y y} ^ {( k )} \qquad \sigma _ {y z} ^ {( k )} \qquad \sigma _ {x z} ^ {( k )} \qquad \sigma _ {x y} ^ {( k )} ] ^ {T}\tag{34}$$

$${\pmb {\varepsilon}} ^ {( k )} = [ {\pmb {\varepsilon}} _ {x x} ^ {( k )} \qquad {\pmb {\varepsilon}} _ {y y} ^ {( k )} \qquad {\pmb {\gamma}} _ {y z} ^ {( k )} \qquad {\pmb {\gamma}} _ {x z} ^ {( k )} \qquad {\pmb {\gamma}} _ {x y} ^ {( k )} ] ^ {T}\tag{35}$$

$$\begin{array} {r} {\varepsilon _ {0} ^ {( k )} = [ \varepsilon _ {0 x x} ^ {( k )} \qquad \varepsilon _ {0 y y} ^ {( k )} \qquad \gamma _ {0 y z} ^ {( k )} \qquad \gamma _ {0 x z} ^ {( k )} \qquad \gamma _ {0 x y} ^ {( k )} ] ^ {T}} \end{array}\tag{36}$$

## 3.3. Finite element formulation

According to Gu’s study [1], a four-noded ${\sf C} ^ {0}$ isoparametric element with 16 degrees of freedom per node is presented to develop the finite element model. The displacement components vector $\pmb {u} ^ {( k )}$ for a jth element of any kth layer is expressed as:

$$\pmb {u} _ {j} ^ {( k )} = \{u _ {j} ^ {( k )} , \nu _ {j} ^ {( k )} , w _ {j} ^ {( k )} \} ^ {\mathrm{T}}\tag{37}$$

Substituting Eq. (37) into Eq. (20), Eq. (23) and Eq. $( 24 ) , \pmb {u} _ {j} ^ {( k )}$ becomes

$${\pmb u} _ {j} ^ {( k )} = {\pmb S} ^ {( k )} {\pmb d} _ {j}\tag{38}$$

where, $\pmb {S} ^ {( k )}$ is shape function matrix for any element, and the displacement variables $\pmb {d} _ {j}$ for a jth element is given by:

$$\begin{array} {l} {{d _ {j}}} \\ {{\ = \{U _ {j} ^ {( 1 )} , U _ {j} ^ {( 2 )} , U _ {j} ^ {( 3 )} , U _ {j} ^ {( 4 )} , V _ {j} ^ {( 1 )} , V _ {j} ^ {( 2 )} , V _ {j} ^ {( 3 )} , V _ {j} ^ {( 4 )} , W _ {j} ^ {( 1 )} , W _ {j} ^ {( 3 )} , \alpha _ {j , x} ^ {( 2 )} , \alpha _ {j , y} ^ {( 2 )} , \alpha _ {j , z} ^ {( 2 )} , \lambda _ {j , x} ^ {( 2 )} , \lambda _ {j , y} ^ {( 2 )} , \lambda _ {j , z} ^ {( 2 )} \}}} \end{array}\tag{39}$$

A four-noded element is used in this work, thus the approximations of the displacement variables for an element take the following type:

$${\pmb d} _ {j} = \sum _ {i = 1} ^ {4} N _ {i} {\pmb d} _ {j} ^ {i ( e )} = N {\pmb d} _ {j} ^ {( e )}\tag{40}$$

$$\begin{array} {r} {\mathrm{where} \qquad \boldsymbol {C} ^ {\mathrm{o}} \qquad \mathrm{shape} \qquad \mathrm{functions} \qquad N _ {i} = \frac {1} {4} ( 1 + \xi _ {i} \xi ) ( 1 + \eta _ {i} \eta )} \end{array}$$

$( i = 1 , 2 , 3 , 4 ) ,$ and $\xi , \eta$ are nodal coordinate. In addition, $\pmb {d} _ {i} ^ {( e )}$ is a nodal displacement vector for a jth element. Substituting Eq. (40) into $\mathrm{Eq.~} ( 38 ) \mathrm{,~} \dot {{\mathbf {u}} _ {i} ^ {( k )}}$ is given by:

$$\pmb {u} _ {j} ^ {( k )} = [ \pmb {S} _ {1} ^ {( k )} , \pmb {S} _ {2} ^ {( k )} , \pmb {S} _ {3} ^ {( k )} , \pmb {S} _ {4} ^ {( k )} ] \pmb {d} _ {j} ^ {( e )}\tag{41}$$

The details of ${\pmb S} _ {i} ^ {( k )}$ for a kth layer of the equivalent sandwich plate are highlighted in Appendix C. By substituting Eq. (40) into Eq. (25)–(27), the strain components vector $\pmb {\varepsilon} _ {j} ^ {( k )}$ for a jth element can be obtained as:

$$\pmb {\varepsilon} _ {j} ^ {( k )} = [ \pmb {B} _ {1} ^ {( k )} , \pmb {B} _ {2} ^ {( k )} , \pmb {B} _ {3} ^ {( k )} , \pmb {B} _ {4} ^ {( k )} ] \pmb {d} _ {j} ^ {( e )}\tag{42}$$

where, the details of differential operator matrix ${\pmb B} _ {i} ^ {( k )}$ for a kth layer are

highlighted in Appendix D.

By applying the principle of virtual work and using $\operatorname{Eq.}$ (40), the system equation of motion for a jth element of the finite element model subjected to a simultaneous $\pmb \varepsilon ^ {( k )}$ can be expressed in matrix form as:

$${K _ {j}} {d _ {j} ^ {\left( e \right)}} = {f _ {q j}} + {f _ {T j}}\tag{43}$$

where the plate stiffness matrix $K _ {j}$ for a jth element is given by:

$$\begin{array} {r} {\pmb {K _ {j}} = \displaystyle \sum _ {k = 1} ^ {3} \int _ {V _ {( k )}} [ \pmb {B} _ {1} ^ {( k )} \pmb {B} _ {2} ^ {( k )} \pmb {B} _ {3} ^ {( k )} \pmb {B} _ {4} ^ {( k )} ] ^ {T} \pmb {Q} _ {j} ^ {( k )} [ \pmb {B} _ {1} ^ {( k )} \pmb {B} _ {2} ^ {( k )} \pmb {B} _ {3} ^ {( k )} \pmb {B} _ {4} ^ {( k )} ] \mathrm{d} V} \end{array}\tag{44}$$

and the mechanical loads vector $\textbf {\textit {f}} _ {q j}$ and thermal loads vector $\pmb {f} _ {T j}$ are, respectively:

$$\begin{array} {r} {\pmb {f} _ {\pmb {q} j} = \displaystyle \sum _ {k = 1} ^ {3} \int _ {V _ {( k )}} \{\pmb {S} _ {1} ^ {( k )} , \pmb {S} _ {2} ^ {( k )} , \pmb {S} _ {3} ^ {( k )} , \pmb {S} _ {4} ^ {( k )} \} ^ {T} \pmb {p} _ {j} ^ {( k )} \mathrm{d} V} \end{array}\tag{45}$$

$$\begin{array} {r l} & {\pmb {f} _ {T} ^ {j} = \displaystyle \sum _ {k = 1} ^ {3} \int _ {V _ {( k )}} [ \pmb {B} _ {1} ^ {( k )} , \pmb {B} _ {2} ^ {( k )} , \pmb {B} _ {3} ^ {( k )} , \pmb {B} _ {4} ^ {( k )} ] ^ {T} \pmb {Q} _ {j} ^ {( k )} \pmb {\varepsilon} _ {0 j} ^ {( k )} \mathrm{d} V} \\ & {= \displaystyle \sum _ {k = 1} ^ {3} \int _ {V _ {( k )}} [ \pmb {B} _ {1} ^ {( k )} , \pmb {B} _ {2} ^ {( k )} , \pmb {B} _ {3} ^ {( k )} , \pmb {B} _ {4} ^ {( k )} ] ^ {T} \pmb {Q} _ {j} ^ {( k )} \pmb {\alpha} _ {T j} ^ {( k )} \Delta T _ {j} ^ {( k )} \mathrm{d} V} \end{array}\tag{46}$$

where, $\pmb {p} _ {j} ^ {( k )} = [ p _ {j x} ^ {( k )} , p _ {j y} ^ {( k )} , p _ {j z} ^ {( k )} ] ^ {T} , p _ {j x} ^ {( k )} , p _ {j y} ^ {( k )} , p _ {j z} ^ {( k )}$ are the mechanical loads for a jth element of any kth layer along $x , y$ and z axis, respectively. The vector ${\alpha} _ {T j} ^ {( k )}$ is the coefficients of thermal expansion for a jth element of any kth layer, and $\Delta T _ {j} ^ {( k )}$ is a prescribed temperature field.

## 3.4. Application cases

The bending and transient dynamic responses of ITPS panels are predicted using the developed methodology. Concerning the current ${\mathsf{C}} ^ {0}$ higher-order finite element, reduced integration was used for the shear terms and full integration for the in-plane terms in all cases studied. No hourglassing modes were observed among the ones studied due to cubic approximation of the transverse displacement in the xy-plane for middle layer. $\textsf {A 3} \times 3$ Gauss-Legendre integration scheme for full integration and a $2 \times 2$ Gauss-Legendre integration scheme for reduced integration are required, respectively. For bottom and top layers, the full and reduced integration schemes are chosen as $3 \times 3$ and $1 \times 1 ,$ respectively. Moreover, the shear correction factor κ of $^ {5 / 6}$ is introduced to the shear terms for bottom and top layers, due to the displacement fields for these layers are based on the first-order shear deformation theory. For describing the temperature fields in the corrugated core, a half unit cell must contain one element in y-direction at least.

## 4. Prediction of stress

By using the equivalent sandwich model described in Section $^ {3 ,}$ the method for stress distribution of ITPS under temperature and mechanical environment is introduced in this section.

## 4.1. Stress calculation in corrugated webs of ITPS

In this subsection, the method for normal stresses (along x - and y -axis) and in-plane shear stress in corrugated webs are studied.

## 4.1.1. Normal strain in the mid-plane of corrugated webs

According to the characteristic of trapezoidal corrugated core, the normal strain along x -axis in the mid-plane of corrugated webs is expressed by using the strain-displacement relationship (25), as:

$$\varepsilon _ {x x} ^ {w} ( \overline {{x}} , \overline {{y}} ) = \varepsilon _ {x x} ^ {( 2 )} ( x , y ^ {c} , \zeta _ {( 2 )} )\tag{47}$$

where, $\begin{array} {r} {y ^ {c} = y _ {B} + \frac {h _ {2} ( \zeta _ {( 2 )} + 1 )} {2 \tan \theta}} \end{array}$ in the part BC of corrugated webs as shown in Fig. 3, and $y ^ {c} = y _ {B ^ {'}} - \frac {h _ {2} ( \zeta _ {( 2 )} + 1 )} {2 \mathrm{tan} \theta}$ in the part $B ^ {\prime} C ^ {\prime}$ of corrugated webs as shown in Fig. 3.

It is observed from Fig. 4 that the displacement $\delta _ {\bar {y}}$ along y -axis consists of the projection of displacements $\delta _ {z}$ and $\delta _ {v}$ on y -axis. The normal strain in the mid-plane of corrugated webs $\varepsilon _ {\bar {y} \bar {y}} ^ {w}$ can be derived as:

$$\begin{array} {r} {\varepsilon _ {y \overline {{y}}} ^ {w} ( \overline {{x}} , \overline {{y}} ) = \frac {\delta _ {\overline {{y}}}} {l} = \frac {\delta _ {z} \sin \theta + \delta _ {y} \cos \theta} {l} = \frac {\delta _ {z}} {h _ {2}} \mathrm{sin} ^ {2} \theta + \frac {\delta _ {y}} {l _ {y}} \mathrm{cos} ^ {2} \theta} \\ {= \varepsilon _ {z z} ^ {( 2 )} ( x , y ^ {c} , \zeta _ {( 2 )} ) \mathrm{sin} ^ {2} \theta + \varepsilon _ {y y} ^ {( 2 )} ( x , y ^ {c} , \zeta _ {( 2 )} ) \mathrm{cos} ^ {2} \theta} \end{array}\tag{48}$$

where, l is the length of corrugated web; $l _ {y}$ is the projection length of corrugated web on y-axis; yc is similar with the description in Eq. (47).

## 4.1.2. Curvature in corrugated webs induced by global bending moment

Due to the corrugated webs are thin plate, the bending behavior occurs easy in the corrugated webs. Hence the stresses appeared in the top and bottom surfaces of face sheets are greater than the stresses in the mid-plane. As a result, the influence of curvature must be considered in the calculation of normal stresses. According to Martinez’s study [19], both the curvatures along x - and y -directions in the corrugated webs are affected by ITPS bending, thus the curvatures in corrugated webs induced by ITPS bending are studied in this section. The relation between the curvature in corrugated web along x -direction and the curvature along x-direction can be written as:

$$\kappa _ {x} ^ {w} = \cos \theta \kappa _ {x}\tag{49}$$

where, the curvature along x-direction $\kappa _ {x}$ can be derived by the rotation angle along x-direction $\theta _ {x}$ , and it is expressed as:

$$\kappa _ {x} = \frac {\partial \theta _ {x}} {\partial x} = \frac {\partial} {\partial x} \Bigg ( \frac {\partial u ^ {( 2 )}} {\partial z} \Bigg )\tag{50}$$

Combining the displacement field in the middle layer (25) with $\begin{array} {r} {\zeta _ {( 2 )} = \frac {2} {h _ {2}} z - \frac {z _ {l} ^ {( 2 )} + z _ {u} ^ {( 2 )}} {h _ {2}}} \end{array}$ , the curvature in corrugated web along x -direction is expressed as:

$$\begin{array} {r l} & {\kappa _ {\bar {x}} ^ {w} ( \bar {x} , \overline {{y}} ) = \mathrm{cos} \theta \Bigg [ \frac {U _ {, x} ^ {( 3 )} ( x , y ^ {c} ) - U _ {, x} ^ {( 2 )} ( x , y ^ {c} )} {h _ {2}} + 2 \zeta _ {( 2 )} \alpha _ {x , x} ^ {( 2 )} ( x , y ^ {c} )} \\ & {\qquad + \left. ( 3 \zeta _ {( 2 )} ^ {2} - 1 ) \lambda _ {x , x} ^ {( 2 )} ( x , y ^ {c} ) \right]} \end{array}\tag{51}$$

The curvature induced by bending of ITPS can be derived by the Castigliano’s second theorem and the principle of structural mechanics. Firstly, half of corrugated core is selected as shown in Fig. 5, and the origin of coordinate system yAz is set at point A and the structure has a clamped boundary condition at this point. For part AB, the inner forces at an arbitrary point, as shown in ${\mathrm{Fig.~}} 5 ,$ are:

$$M _ {1} = H h _ {2} + V ( p - y ) - M _ {0}\tag{52}$$

$$N _ {1} = H\tag{53}$$

$$T _ {1} = V\tag{54}$$

where, $H ,$ V and $M _ {0}$ are the horizontal force, vertical force and moment forced at the free end (point D in Fig. 5), and $0 \leqslant y \leqslant f$

For part $B C ,$ the inner forces are:

$$M _ {2} = H ( h _ {2} - z ) + V \biggl ( p - \frac {z} {{\mathrm{tan}} \theta} \biggl ) - M _ {0}\tag{55}$$

$$N _ {2} = H {\cos} \theta - V {\sin} \theta\tag{56}$$

$$T _ {2} = H \mathrm{sin} \theta + V \mathrm{cos} \theta\tag{57}$$

where, $0 \leqslant z \leqslant h _ {2}$

For part CD, the inner forces are:

$$M _ {3} = V ( p - y ) - M _ {0}\tag{58}$$

$$N _ {3} = H\tag{59}$$

$$T _ {3} = V\tag{60}$$

where, $\begin{array} {r} {f + \frac {h _ {2}} {{\tan \theta}} \leqslant y \leqslant p .} \end{array}$ Applying the Castigliano’s theorem, the horizontal and vertical displacements $\delta _ {H} , \delta _ {V}$ , and its rotation $\delta _ {M _ {0}}$ at the free end point D as illustrated in Fig. 5 are derived as:

(61)

$$\begin{array} {r l} & \begin{array} {r l} {\Lambda _ {1 ^ {\prime}} - \int _ {0} ^ {1} ( \frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\sin \theta} ) d y} \\ {+} & {\int _ {0} ^ {1} ( \frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\sin \theta} ) d y} \\ {+} & {\int _ {0} ^ {1} ( \frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\sin \theta} ) d x \leq \frac {\sin \theta} {\sin \theta}} \\ {- \int _ {0} ^ {1} \sqrt {\frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\sin \theta}} \frac {\sin \theta} {\sin \theta} \mathrm{d} y} \\ {+} & {\int _ {0} ^ {1} \sqrt {\frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\cos \theta}} \frac {\sin \theta} {\sin \theta} \mathrm{d} y} \\ {- \int _ {0} ^ {1} ( \frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\sin \theta} - \frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\sin \theta} ) d y} \\ {- \int _ {0} ^ {1} ( \frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\sin \theta} - \frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\sin \theta} ) d x} \\ - \int _ {0} ^ {1} ( \frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\sin \theta} + \frac {\sin \theta} {\sin \theta} + \frac \end{array} \end{array}\tag{62}$$

(63)

where, $\begin{array} {r} {\mathrm{d} I _ {w} = \frac {t _ {w} ^ {3} \mathrm{d} b} {12} , \mathrm{d} A _ {w} = t _ {w} \mathrm{d} b . E _ {w} ^ {1} , E _ {w} ^ {2}} \end{array}$ and $E _ {w} ^ {3}$ are the temperature-dependent Young’s modulus for part AB, BC and CD, respectively. $G _ {w} ^ {1} , G _ {w} ^ {2}$ and $G _ {w} ^ {3}$ are the temperature-dependent shear modulus for part AB, BC and CD, respectively.

By substituting Eqs. (61)–(63) into Eq. (52)–(60), the following system of equations will be written as:

$$\left\{\begin{array} {l} {\delta _ {H}} \\ {\delta _ {V}} \\ {\delta _ {M _ {0}}} \end{array} \right\} = \frac {1} {\mathrm{d} b} C ^ {s t} \left\{\begin{array} {l} {H} \\ {V} \\ {M _ {0}} \end{array} \right\} = \frac {1} {\mathrm{d} b} \left[ \begin{array} {l l l} {C _ {11} ^ {s t}} & {C _ {12} ^ {s t}} & {C _ {13} ^ {s t}} \\ & {C _ {22} ^ {s t}} & {C _ {23} ^ {s t}} \\ {s y m} & & {C _ {33} ^ {s t}} \end{array} \right] \left\{\begin{array} {l} {H} \\ {V} \\ {M _ {0}} \end{array} \right\}\tag{64}$$

where, the detail of coefficients of matrix Cst is highlighted in Appendix E.

In order to calculate the inner forces $H , \ V , \ M _ {0}$ for part CD under bending behavior, the boundary conditions $\delta _ {H} = 0 , \delta _ {V} = 0$ are imposed, and Eq. (64) can be rewritten as:

$$\frac {1} {\mathrm{d} b} \left[ \begin{array} {l l l} {C _ {11} ^ {s t}} & {C _ {12} ^ {s t}} & {C _ {13} ^ {s t}} \\ & {C _ {22} ^ {s t}} & {C _ {23} ^ {s t}} \\ {s y m} & & {C _ {33} ^ {s t}} \end{array} \right] \left\{\begin{array} {l} {H} \\ {V} \\ {M _ {0}} \end{array} \right\} = \left\{\begin{array} {l} {0} \\ {0} \\ {\delta _ {M _ {0}}} \end{array} \right\}\tag{65}$$

By employing the displacement field $\nu ^ {( 2 )}$ in the middle layer (25), the rotation angle distribution along y-direction is expressed as:

$$\theta _ {y} ^ {( 2 )} ( x , y , \zeta _ {( 2 )} ) = \frac {\partial \nu ^ {( 2 )} ( x , y , \zeta _ {( 2 )} )} {\partial z} = \frac {V ^ {( 3 )} - V ^ {( 2 )}} {h _ {2}} + 2 \zeta _ {( 2 )} \alpha _ {y} ^ {( 2 )} + ( 3 \zeta _ {( 2 )} ^ {2} - 1 ) \lambda _ {y} ^ {( 2 )}\tag{66}$$

Subsequently, the rotation at the free end (see Fig. 5) is written as:

$$\delta _ {M _ {0}} = \theta _ {y} ^ {( 2 )} ( x , y _ {D} , 1 )\tag{67}$$

where, $y _ {D}$ is the location of point D in y-direction.

By substituting Eq. (67) into Eq. (65), the horizontal force H, the vertical force V and the moment $M _ {0}$ at point D can be derived. By substituting H, V and $M _ {0}$ at point D into $\operatorname{Eq.}$ (55), the moment distribution $M _ {2}$ for part BC can be obtained. Then the flexural differential equation for part BC of corrugated core is expressed as:

$$E _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , z ) ) d I _ {w} \varkappa _ {\bar {y}} ^ {w m} ( z ) = M _ {2} ( z )\tag{68}$$

As a result, the curvature distribution ${\kappa _ {\bar {\nu}} ^ {w m}}$ along $\bar {y}$ -direction for part BC induced by bending of ITPS can be obtained.

## 4.1.3. Curvature in corrugated webs induced by transverse shear force

From Martinez’s study, the curvature $\kappa _ {\overline {{x}}}$ along x -direction of corrugated webs is only affected by the bending behavior of ITPS, but the curvature $\kappa _ {\bar {y}}$ along y -direction of corrugated webs is affected by two cases: the bending deformation of ITPS; the shear deformation of ITPS. The formulae for curvature in corrugated webs induced by bending of ITPS is already obtained in Section 4.1.2, thus the formulae for curvature in corrugated webs induced by shear deformation of ITPS will be derived in this section.

Similarly, the curvature in corrugated webs induced by shear deformation of ITPS can also be derived by the Castigliano’s theorem and the principle of structural mechanics. In order to calculate the inner forces H, V, M0 for part CD under shear behavior, the boundary conditions $\delta _ {V} = 0 , \delta _ {M _ {0}} = 0$ are imposed, and Eq. (64) can be rewritten as:

$$\frac {1} {\mathrm{d} b} [ \begin{array} {l l l} {C _ {11} ^ {s t}} & {C _ {12} ^ {s t}} & {C _ {13} ^ {s t}} \\ & {C _ {22} ^ {s t}} & {C _ {23} ^ {s t}} \\ {s y m} & & {C _ {33} ^ {s t}} \end{array} ] \{\begin{array} {l} {H} \\ {V} \\ {M _ {0}} \end{array} \} = \{\begin{array} {l} {\delta _ {H}} \\ {0} \\ {0} \end{array} \}\tag{69}$$

The horizontal displacement $\delta _ {H}$ at the free end can be derived by employing the strain-displacement relationship in the middle layer (25), as:

$$\delta _ {{\cal H}} = \gamma _ {y z} ^ {( 2 )} ( x , y _ {D} , 1 ) h _ {2}\tag{70}$$

By substituting Eq. (70) into Eq. (69), the inner forces H, $V , M _ {0}$ can be obtained. Then substituting the inner forces into Eq. (55), the moment distribution $M _ {2}$ in part BC (see Fig. 5) will be gained. The flexural differential equation for part BC can be expressed by the moment distribution, as:

$$E _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , z ) ) \mathrm{d} I _ {w} \varkappa _ {\overline {{y}}} ^ {w s} ( z ) = M _ {2} ( z )\tag{71}$$

As a result, the curvature distribution ${\kappa _ {\overline {{y}}}} ^ {w s}$ along y -direction for part BC induced by shear deformation of ITPS can be obtained.

## 4.1.4. Shear strain in corrugated webs

From He’s study [26], the in-plane shear strain in corrugated webs is expressed as:

$$\gamma _ {\overline {{{x y}}}} ^ {( 2 )} ( \overline {{{x}}} , \overline {{{y}}} ) = \mathrm{sin} \theta \left( \frac {\partial u ^ {( 2 )} ( x , y ^ {c} , \zeta _ {( 2 )} )} {\partial z} + \frac {\partial w ^ {( 2 )} ( x , y ^ {c} , \zeta _ {( 2 )} )} {\partial x} \right)\tag{72}$$

By substituting the strain-displacement relationship (25) into Eq. (72), the in-plane shear strain in corrugated webs can be rewritten as:

$$\begin{array} {r l} & {\gamma _ {\overline {{x y}}} ^ {( 2 )} ( \overline {{x}} , \overline {{y}} ) = \mathrm{sin} \theta \Bigg ( \frac {U ^ {( 3 )} ( x , y ^ {c} ) - U ^ {( 2 )} ( x , y ^ {c} )} {h _ {2}} + 2 \zeta _ {( 2 )} \alpha _ {x} ^ {( 2 )} ( x , y ^ {c} )} \\ & {\qquad + \left( 3 \zeta _ {( 2 )} ^ {2} - 1 \right) \lambda _ {x} ^ {( 2 )} ( x , y ^ {c} ) + W _ {, x} ^ {( 1 )} ( x , y ^ {c} ) \Psi _ {1} ^ {( 2 )} + W _ {, x} ^ {( 3 )} ( x , y ^ {c} ) \Psi _ {2} ^ {( 2 )}} \\ & {\qquad + \left. \alpha _ {z , x} ^ {( 2 )} ( x , y ^ {c} ) \Psi _ {3} ^ {( 2 )} + \lambda _ {z , x} ^ {( 2 )} ( x , y ^ {c} ) \Psi _ {4} ^ {( 2 )} \right)} \end{array}\tag{73}$$

## 4.1.5. Constitutive relationship in corrugated webs

Using the formulae of normal strains described in Section 4.1.1 and the constitutive relations, the normal stresses in x - and y -directions of the mid-plane of corrugated webs are able to be obtained as:

$$\sigma _ {x x} ^ {c , m i d} = E _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , \zeta _ {( 2 )} ) ) [ \varepsilon _ {x x} ^ {( 2 )} ( x , y ^ {c} , \zeta _ {( 2 )} ) - \alpha _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , \zeta _ {( 2 )} ) ) \Delta T _ {r} ^ {( 2 )} ( x , \zeta _ {( 2 )} ) ] ,\tag{74}$$

$$\sigma _ {\bar {y} \bar {y}} ^ {c , m i d} = E _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , \zeta _ {( 2 )} ) ) [ \varepsilon _ {z z} ^ {( 2 )} ( x , y ^ {c} , \zeta _ {( 2 )} ) - \alpha _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , \zeta _ {( 2 )} ) ) \Delta T _ {r} ^ {( 2 )} ( x , \zeta _ {( 2 )} ) ]\tag{75}$$

where, $\Delta T _ {r} ^ {( 2 )}$ is the reduced temperature field described in Eq. (2).

The normal stress distribution through the thickness direction of

corrugated web is needed to consider the influence of curvature in corrugated web. The normal stress $\sigma _ {x x} ^ {c}$ in x -direction of corrugated web is only affected by bending behavior of ITPS, and it is expressed as:

$$\begin{array} {r l} & {\sigma _ {x x} ^ {c} ( \overline {{x}} , \overline {{y}} , \overline {{z}} ) = E _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , \zeta _ {( 2 )} ) ) [ \varepsilon _ {x x} ^ {( 2 )} ( x , y ^ {c} , \zeta _ {( 2 )} ) + \overline {{z}} \kappa _ {x} ^ {w} ( x , y ^ {c} , \zeta _ {( 2 )} )} \\ & {\qquad - \alpha _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , \zeta _ {( 2 )} ) ) \Delta T _ {r} ^ {( 2 )} ( x , \zeta _ {( 2 )} ) ]} \end{array}\tag{76}$$

where, $\begin{array} {r} {- \frac {t _ {w}} {2} \leqslant \overline {{z}} \leqslant \frac {t _ {w}} {2} .} \end{array}$

The normal stress $\sigma _ {\overline {{y}} \overline {{y}}} ^ {c}$ in y -direction of corrugated web affected by bending and shear deformation of ITPS is expressed as:

$$\begin{array} {r} {\sigma _ {\bar {y} \bar {y}} ^ {c} = E _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , \zeta _ {( 2 )} ) ) [ \varepsilon _ {z z} ^ {( 2 )} ( x , y ^ {c} , \zeta _ {( 2 )} ) + \mp ( \kappa _ {\bar {y}} ^ {w} ( x , y ^ {c} , \zeta _ {( 2 )} ) + \kappa _ {\bar {y}} ^ {w s} ( x , y ^ {c} , \zeta _ {( 2 )} ) )} \\ {- \alpha _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , \zeta _ {( 2 )} ) ) \Delta T _ {r} ^ {( 2 )} ( x , \zeta _ {( 2 )} ) ] ( 77 )} \end{array}\tag{7}$$

According to the description of in-plane shear strain in Section 4.1.4, the in-plane shear stress $\sigma _ {x y} ^ {c}$ for corrugated webs is written as:

$$\sigma _ {\overline {{x}} \overline {{y}}} ^ {c} = G _ {w} ( \Delta T _ {r} ^ {( 2 )} ( x , \zeta _ {( 2 )} ) ) \gamma _ {\overline {{x}} \overline {{y}}} ^ {( 2 )} ( \overline {{x}} , \overline {{y}} )\tag{78}$$

## 4.2. Stress calculation in bottom and top face sheets of ITPS

In this subsection, the method for normal stresses (along x-axis and y-axis) and in-plane shear stress in bottom and top face sheets of ITPS are studied.

## 4.2.1. Normal strain in the mid-plane of bottom and top face sheets

By using the strain-displacement relationships (26) and (27) for bottom and top face sheets of ITPS, the normal strains in x- and ydirections for the mid-plane of bottom face sheets are, respectively:

$$\varepsilon _ {x x} ^ {( 1 )} ( x , y , \zeta _ {( 1 )} ) = U _ {, x} ^ {( 1 )} ( x , y ) \Psi _ {1} ^ {( 1 )} + U _ {, x} ^ {( 2 )} ( x , y ) \Psi _ {2} ^ {( 1 )}\tag{79}$$

$$\varepsilon _ {y y} ^ {( 1 )} ( x , y , \zeta _ {( 1 )} ) = V _ {, y} ^ {( 1 )} ( x , y ) \Psi _ {1} ^ {( 1 )} + V _ {, y} ^ {( 2 )} ( x , y ) \Psi _ {2} ^ {( 1 )}\tag{80}$$

And the normal strains in x- and $y -$ directions for the mid-plane of top face sheets are, respectively:

$$\varepsilon _ {x x} ^ {( 3 )} ( x , y , \zeta _ {( 3 )} ) = U _ {, x} ^ {( 3 )} ( x , y ) \Psi _ {1} ^ {( 3 )} + U _ {, x} ^ {( 4 )} ( x , y ) \Psi _ {2} ^ {( 3 )}\tag{81}$$

$$\varepsilon _ {y y} ^ {( 3 )} ( x , y , \zeta _ {( 3 )} ) = V _ {, y} ^ {( 3 )} ( x , y ) \Psi _ {1} ^ {( 3 )} + V _ {, y} ^ {( 4 )} ( x , y ) \Psi _ {2} ^ {( 3 )}\tag{82}$$

## 4.2.2. Curvature in bottom face sheets

The curvature in the bottom face sheets of ITPS can be derived by the rotation angle distribution. By applying the displacement field (23), the curvature along x- and y- directions for the bottom face sheets of ITPS are:

$$\mathcal {\kappa} _ {x} ^ {( 1 )} = \frac {\partial \theta _ {x} ^ {( 1 )}} {\partial x} = \frac {1} {h _ {1}} ( U _ {, x} ^ {( 2 )} - U _ {, x} ^ {( 1 )} )\tag{83}$$

$$\mathcal {K} _ {y} ^ {( 1 )} = \frac {\partial \theta _ {y} ^ {( 1 )}} {\partial y} = \frac {1} {h _ {1}} ( V _ {, y} ^ {( 2 )} - V _ {, y} ^ {( 1 )} )\tag{84}$$

Due to the corrugated webs deliver the forces suffering on the top face sheets to the bottom face sheets, local deformation of the bottom face sheets is produced, and the local deformation changes the curvature in the bottom face sheets. In order to obtain the curvature of bottom face sheets induced by local deformation, the bottom face sheets of ITPS should be scattered by the length 2p (see Fig. 6) of a unit cell of corrugated core. For the discrete bottom face sheets, clamped boundary condition is imposed on the both ends (see Fig. 6). As shown in Fig. 6, F1 and $F _ {2}$ are the inner forces through corrugated webs imposing on the discrete bottom face sheets. By using the method for normal stresses in the mid-plane of corrugated webs in Section 4.1.5, F1 and $F _ {2}$ are obtained as:

$$\begin{array} {r l} & {F _ {1} = \sigma _ {\bar {y} \bar {y}} ^ {c , m i d} ( y _ {B} ) t _ {w} \mathrm{sin} \theta} \\ & {\quad = E _ {\bar {y}} \left( \Delta T _ {r} ^ {\left( 2 \right)} ( x , - 1 ) \right) \left[ \varepsilon _ {z z} ^ {\left( 2 \right)} ( x , y _ {B} , - 1 ) - \alpha _ {\bar {y}} \left( \Delta T _ {r} ^ {\left( 2 \right)} ( x , - 1 ) \right) \right] t _ {w} \mathrm{sin} \theta} \end{array}\tag{85}$$

$$\begin{array} {r l} & {F _ {2} {=} \sigma _ {\bar {y} \bar {y}} ^ {c , m i d} ( y _ {B ^ {\prime}} ) t _ {w} \mathrm{sin} \theta} \\ & {\quad = E _ {\bar {y}} ( \Delta T _ {r} ^ {( 2 )} ( x , - 1 ) ) [ \varepsilon _ {z z} ^ {( 2 )} ( x , y _ {B ^ {\prime}} , - 1 ) - \alpha _ {\bar {y}} ( \Delta T _ {r} ^ {( 2 )} ( x , - 1 ) ) ] t _ {w} \mathrm{sin} \theta} \end{array}\tag{86}$$

Then applying the method of statically indeterminate problem, the distributions of moment in bottom face sheets are calculated, and the expressions of moment in the bottom face sheets can be written as:

$$M ( \overline {{{y}}} ) = F _ {A} \overline {{{y}}} - M _ {A} \qquad ( 0 \leqslant \overline {{{y}}} \leqslant f )\tag{87}$$

$$M ( \overline {{{y}}} ) = F _ {A} \overline {{{y}}} - F _ {1} ( \overline {{{y}}} - f ) - M _ {A} \qquad ( f \leqslant \overline {{{y}}} \leqslant 2 p - f )\tag{88}$$

$$M ( {\overline {{y}}} ) = F _ {A} {\overline {{y}}} - F _ {1} ( {\overline {{y}}} - f ) - F _ {2} ( {\overline {{y}}} - 2 p + f ) - M _ {A} \qquad ( 2 p - f \leqslant {\overline {{y}}} \leqslant 2 p )\tag{89}$$

where, $\begin{array} {r} {f = \frac {p - h _ {2} \mathrm{cot} \hat {\theta}} {2} .} \end{array}$

For the discrete bottom face sheets, $M _ {A}$ and $F _ {A}$ are:

$$M _ {A} = \frac {1} {( 2 p ) ^ {2}} [ F _ {1} ( 2 p - f ) ^ {2} f + F _ {2} ( 2 p - f ) f ^ {2} ]\tag{90}$$

(a). σ,x=0.4m

(c). σ, x=0.4m

$$F _ {A} = \frac {1} {( 2 p ) ^ {2}} [ F _ {1} ( 2 p - f ) ^ {2} + F _ {2} f ^ {2} + 4 M _ {A} p ]\tag{91}$$

The curvature induced by local deformation in the bottom face sheets can be obtained by using the flexural differential equation and the distributions of moment above-mentioned, and it is expressed as:

$$\kappa _ {l o c a l} ^ {( 1 )} ( \overline {{y}} ) = \frac {M ( \overline {{y}} )} {E _ {y} ^ {( 1 )} I ^ {( 1 )}}\tag{92}$$

where, $E _ {v} ^ {( 1 )}$ is the Young’s modulus along y-direction for bottom face sheets, $I ^ {( 1 )}$ is the moment of inertia for bottom face sheets.

## 4.2.3. Curvature in top face sheets

With similar to the bottom face sheets, the curvatures along x- and $y -$ directions for the top face sheets are written as:

$$\mathcal {K} _ {x} ^ {( 3 )} = \frac {\partial \theta _ {x} ^ {( 3 )}} {\partial x} = \frac {1} {h _ {3}} ( U _ {, x} ^ {( 4 )} - U _ {, x} ^ {( 3 )} )\tag{93}$$

$$\mathcal {K} _ {y} ^ {( 3 )} = \frac {\partial \theta _ {y} ^ {( 3 )}} {\partial y} = \frac {1} {h _ {3}} ( V _ {, y} ^ {( 4 )} - V _ {, y} ^ {( 3 )} )\tag{94}$$

Because the extreme out-of-plane aerodynamic pressure is applied on the top face sheets of ITPS, the curvature in the top face sheet should consider the influence of local displacements by aerodynamic pressure. The top face sheet endures uniform loads in the study, and the top face sheet of ITPS can be considered as a multi-span continuous plate supported at the locations of the corrugated webs along x-direction [26]. From He’s study [26], the top face sheet between two adjacent supports can be taken as a clamped–clamped plate in cylindrical bending, and the rotation angles of the top face sheet in the supports are zero due to the symmetry of the structure. By applying the principle of structural mechanics, the moment distribution in the top face sheet can be expressed as:

$$M ( y ) = \frac {P L ^ {2}} {12} - \frac {1} {2} P L y + \frac {1} {2} P y ^ {2}\tag{95}$$

where, P is the uniform pressure applied on the top face sheets, L is the length between two adjacent supports. By employing the flexural differential equation and the moment distributions above-mentioned, the

(b). σ×) x=0.2mm

(d). σ, x=0.2m

(c). $\sigma _ {y y} ^ {z 1} , x {=} 0.4 m$

(d). $\sigma _ {\mathrm{y} y} ^ {z 1} , \kappa {=} 0.2 \ m$

(c). $\pmb {\sigma} _ {\mathbf {y} \mathbf {y}} ^ {z _ {2}} , \pmb {x} {=} \pmb {0} . 4 \mathbf {m}$

(d). $\sigma _ {y y} ^ {z _ {2}} , \kappa {=} 0.2 m$

curvature induced by local displacement in the top face sheets can be written as:

$$\mathcal {K} _ {l o c a l} ^ {( 3 )} ( y ) = \frac {M ( y )} {E _ {y} ^ {( 3 )} I ^ {( 3 )}}\tag{96}$$

where, $E _ {y} ^ {( 3 )}$ is the Young’s modulus along y-direction for top face sheets, $I ^ {( 3 )}$ is the moment of inertia for top face sheets.

## 4.2.4. Shear strain in bottom and top face sheets

Applying the strain-displacement relationships (23) and (24), the inplane shear strains for bottom and top face sheet is written as:

$$\gamma _ {x y} ^ {( k )} ( x , y , \zeta _ {( k )} ) = U _ {, y} ^ {( k )} \Psi _ {1} ^ {( k )} + U _ {,} ^ {( k + 1 )} \Psi _ {2} ^ {( k )} + V _ {, x} ^ {( k )} \Psi _ {1} ^ {( k )} + V _ {, x} ^ {( k + 1 )} \Psi _ {2} ^ {( k )}\tag{97}$$

where, $k = 1 , 3 ,$

## 4.2.5. Constitutive relationship in bottom and top face sheets

Using the formulae of normal strains described in Section 4.2.1 and the constitutive relations, the normal stresses in x- and y- directions of the mid-plane of corrugated webs are able to be obtained as:

$$\begin{array} {r l} & {\sigma _ {x x} ^ {( k ) , m i d} = \widetilde {Q} _ {11} ^ {( k )} ( \Delta T ^ {( k )} ( x , y ) ) [ \varepsilon _ {x x} ^ {( k )} ( x , y ) + \mu _ {x y} ^ {( k )} \varepsilon _ {y y} ^ {( k )} ( x , y )} \\ & {\quad \quad \quad - \alpha _ {x} ^ {( k )} ( \Delta T ^ {( k )} ( x , y ) ) \Delta T ^ {( k )} ( x , y ) ]} \end{array}\tag{98}$$

(c). 02) =04mm

(c). $\sigma _ {y y} ^ {\mathsf{m}} , \mathsf{x} {=} 0.4 \mathsf{m}$

(b). σ×x x=0.2m

(d). $\sigma _ {y y} ^ {\mathsf{m}} , \mathsf{x} {=} 0.2 \mathsf{m}$

(d) σ21, x=0.2mm

$$\begin{array} {c} {{\sigma _ {y y} ^ {( k ) , m i d} = \widetilde {Q} _ {22} ^ {( k )} ( \Delta T ^ {( k )} ( x , y ) ) [ \varepsilon _ {y y} ^ {( k )} ( x , y ) + \mu _ {y x} ^ {( k )} \varepsilon _ {x x} ^ {( k )} ( x , y )}} \\ {{- \alpha _ {y} ^ {( k )} ( \Delta T ^ {( k )} ( x , y ) ) \Delta T ^ {( k )} ( x , y ) ]}} \end{array}\tag{99}$$

where, $k = 1 , 3$ . For the juncture of the horizontal corrugated core sheets and the outer face sheets as the parts AB, CC′ and A′B′ (see Fig. 3), the normal stresses should be corrected. The correction method is that the normal stress ${\sigma _ {y y} ^ {( k )}}$ in $\operatorname{Eq.} ( 99 )$ is multiplied by a correction factor $E _ {y} ^ {( k )} h _ {k}$ 
$\overline {{E _ {y} ^ {( k )} h _ {k} + E _ {\overline {{\nu}}} ^ {( 2 )} t _ {w}}}$

The normal stress distributions through the thickness direction of bottom and top face sheets are needed to consider the influence of curvature. The normal stresses in x- and y-directions of the bottom face sheets are expressed as:

$$\begin{array} {r l} & {\sigma _ {x x} ^ {( 1 )} = \widetilde {Q} _ {11} ^ {( 1 )} ( \Delta T ^ {( 1 )} ( x , y ) ) [ \varepsilon _ {x x} ^ {( 1 )} ( x , y ) + z ^ {( 1 )} \kappa _ {x} ^ {( 1 )} ( x , y ) + \mu _ {x y} ^ {( 1 )} ( \varepsilon _ {y y} ^ {( 1 )} ( x , y )} \\ & {\phantom {\sigma _ {x x} ^ {( 1 )} =} + z ^ {( 1 )} \kappa _ {y} ^ {( 1 )} ( x , y ) + z ^ {( 1 )} \kappa _ {l o c a l} ^ {( 1 )} ( x , \overline {{y}} ) ) {- \alpha _ {x} ^ {( 1 )}} ( \Delta T ^ {( 1 )} ( x , y ) ) \Delta T ^ {( 1 )} ( x , y ) ]} \\ & {\phantom {\sigma _ {x x} ^ {( 1 )} =}} \\ & {\phantom {\sigma _ {x x} ^ {( 1 )} =} \mathcal {\widetilde {Q}} _ {22} ^ {( 1 )} ( \Delta T ^ {( 1 )} ( x , y ) ) [ \varepsilon _ {y y} ^ {( 1 )} ( x , y ) + z ^ {( 1 )} \kappa _ {y} ^ {( 1 )} ( x , y ) + z ^ {( 1 )} \kappa _ {l o c a l} ^ {( 1 )} ( x , \overline {{y}} )} \\ & {\phantom {\sigma _ {x y} ^ {( 1 )} =} + \mu _ {y x} ^ {( 1 )} ( \varepsilon _ {x x} ^ {( 1 )} ( x , y ) + z ^ {( 1 )} \kappa _ {x} ^ {( 1 )} ( x , y ) ) {- \alpha _ {y} ^ {( 1 )}} ( \Delta T ^ {( 1 )} ( x , y ) ) \Delta T ^ {( 1 )} ( x , y ) ]} \end{array}\tag{100}$$

(101)

(c). $\sigma _ {y y} ^ {z _ {2}} , x {=} 0.4 m$

(d). $\sigma _ {\mathrm{yy}} ^ {z _ {2}} , \kappa {=} 0.2 \mathrm{m}$

(c). $\sigma _ {\mathsf{y} \mathsf{y}} ^ {\mathsf{m}} , \mathsf{x} {=} 0.4 \mathsf{m}$

(d). $\pmb {\sigma} _ {\mathbf {y} \mathbf {y}} ^ {m} , \mathbf {x} {=} 0.2 \mathbf {m}$

where, $\begin{array} {r} {- \frac {h _ {1}} {2} \leqslant z ^ {( 1 )} \leqslant \frac {h _ {1}} {2} .} \end{array}$

With taking into account the curvature induced by local displacements by aerodynamic pressure, the normal stresses in x- and y-directions of top face sheet is expressed as:

$$\begin{array} {c} {{\sigma _ {x x} ^ {( 3 )} = \widetilde {Q} _ {11} ^ {( 3 )} ( \Delta T ^ {( 3 )} ( x , y ) ) [ \varepsilon _ {x x} ^ {( 3 )} ( x , y ) + z ^ {( 3 )} \kappa _ {x} ^ {( 3 )} ( x , y ) + \mu _ {x y} ^ {( 3 )} ( \varepsilon _ {y y} ^ {( 3 )} ( x , y )}} \\ {{+ z ^ {( 3 )} \kappa _ {y} ^ {( 3 )} ( x , y ) + z ^ {( 3 )} \kappa _ {l o c a l} ^ {( 3 )} ( x , \overline {{{y}}} ) ) - \alpha _ {x} ^ {( 3 )} ( \Delta T ^ {( 3 )} ( x , y ) ) \Delta T ^ {( 3 )} ( x , y ) ]}} \end{array}\tag{102}$$

$$\begin{array} {r l} & {\sigma _ {y y} ^ {( 3 )} = \widetilde {Q} _ {22} ^ {( 3 )} ( \Delta T ^ {( 3 )} ( x , y ) ) [ \varepsilon _ {y y} ^ {( 3 )} ( x , y ) + z ^ {( 3 )} \kappa _ {y} ^ {( 3 )} ( x , y ) + z ^ {( 3 )} \kappa _ {l o c a l} ^ {( 3 )} ( x , \overline {{y}} )} \\ & {\quad \quad \quad \quad + \mu _ {y x} ^ {( 3 )} ( \varepsilon _ {x x} ^ {( 3 )} ( x , y ) + z ^ {( 3 )} \kappa _ {x} ^ {( 3 )} ( x , y ) ) - \alpha _ {y} ^ {( 3 )} ( \Delta T ^ {( 3 )} ( x , y ) ) \Delta T ^ {( 3 )} ( x , y ) ]} \end{array}\tag{103}$$

where, $\begin{array} {r} {- \frac {h _ {3}} {2} \leqslant z ^ {( 3 )} \leqslant \frac {h _ {3}} {2} .} \end{array}$

According to the description of in-plane shear strain in Section $4.2.4 ,$ the in-plane shear stresses for bottom and top face sheet is written as:

(c). $\sigma _ {y y} ^ {z 1} , x {=} 0.4 m$

(d). $\sigma _ {\mathrm{y} y} ^ {z 1} , \kappa {=} 0.2 \ m$

(c). $\sigma _ {y y} ^ {z 2} , x {=} 0.4 m$

(d). $\pmb {\sigma} _ {\mathbf {y} \mathbf {y}} ^ {z 2} , \pmb {x} {=} \mathbf {0} . 2 \mathbf {m}$

$$\sigma _ {x y} ^ {( k )} = Q _ {66} ^ {( k )} \left( \Delta T ^ {( k )} ( x , y ) \right) \gamma _ {x y} ^ {( k )} ( x , y , \zeta _ {( k )} )\tag{104}$$

where, $k = 1 , 3$

## 5. Numerical examples

The numerical examples have been focused on three cases: stress distributions of ITPS subjected to uniform transverse pressure; stress distributions of ITPS subjected to thermal loads; stress distributions of ITPS subjected to both uniform transverse pressure and thermal loads.

## 5.1. Stress distributions of ITPS subjected to uniform transverse pressure

For verification of the effectiveness of the present models to predict the stress distributions of ITPS, a corrugated core ITPS panel with following dimensions is analyzed:

$$\begin{array} {l} {{{\boldsymbol {p}} = 0.05 ~ {\mathrm{m}} , ~ h _ {2} = 0.08 ~ {\mathrm{m}} , ~ h _ {3} = 0.002 ~ {\mathrm{m}} , ~ h _ {1} = 0.003 ~ {\mathrm{m}} , ~ t _ {w} = 0.002 ~ {\mathrm{m}} , ~ \theta}} \\ {{{\boldsymbol {\mathit {\sigma}}} = 75 ^{\circ} .}} \end{array}$$

And the panel dimensions are $0.8 \mathrm{m} \times 0.8 \mathrm{m}$ . The face sheets and corrugated cores are all made of PM2000 (material properties of PM2000 are listed in Table 1). The ITPS panel is simply supported on four edges of bottom face sheets subjected to a transverse loading p = 0.1 MPa. A 3D finite element analysis is employed for the ITPS panel using the commercial Nastran finite element program. Fournoded shell elements are applied to model the face sheets and corrugated sheets of the ITPS panel. The FEM model consisted of 47474 nodes and 37440 elements to guarantee convergence. Convergence study has been investigated in literature [1], while the stresses are calculated by the proposed method with the mesh size of 32 × 32 in the

(c). om, =0.4m 
y(m) 
(c). Bottom face sheet

(b). Top face sheet

example.

Figs. 7–9 show the normal stresses in the mid-plane, upper surface and lower surface of the corrugated webs, respectively. Figs. 10–12 show the normal stresses in the mid-plane, upper surface and lower surface of the top face sheets, respectively. Figs. 13–15 show the normal stresses in the mid-plane, upper surface and lower surface of the bottom face sheets, respectively. And Fig. 16 shows the in-plane shear stresses in the mid-plane of the corrugated webs, top face sheets and bottom face sheets, respectively. As a result, the stresses obtained by the present method agree well with those given by 3D finite element analysis.

(c). $\pmb {\sigma} _ {\mathbf {y} \mathbf {y}} ^ {z 1} , \pmb {\mathrm{x}} \pmb {=} \pmb {0} . 4 \mathbf {m}$

(d). $\sigma _ {\mathrm{yy}} ^ {z 1} , \kappa {=} 0.2 \mathrm{m}$

(c). $\pmb {\sigma} _ {\mathbf {y} \mathbf {y}} ^ {z _ {2}} , \pmb {\mathrm{x}} \pmb {=} \pmb {0.4 \mathrm{m}}$

However, there have some differences between the proposed method and 3D FEM results. As shown in Figs. 7–9 and 13, the present method is unable to predict the normal stresses accurately in the edges of panel as same as the stresses in the middle area of panel. As shown in Figs. 10 and 13, the stresses by present method are different with the FEM results at adjacent points between outer face sheets and webs, because the present method is incapable of considering the effects of stress concentration. From Fig. 16, only the trend and magnitude of shear stresses can be captured by the present method, because the equivalent sandwich plate is different with the actual model, and it is unable to capture the accurate stress distribution.

## 5.2. Stress distributions of ITPS subjected to thermal loads

In this subsection, the study has been focused on the stress analysis of ITPS panel subjected to thermal loads. The ITPS panel dimensions and material properties are all the same as those of the ITPS panel in Section 5.1. The material properties of PM2000 are listed in Table 1,

(d). $\sigma _ {\mathrm{yy}} ^ {z 1} , \kappa {=} 0.2 \ m$

(c). ${\mathfrak {\sigma}} _ {\mathbf {y} \mathbf {y}} ^ {\mathsf{m}} ,$ x=0.4m

$$\pmb {\sigma} _ {y y} ^ {z 1} , \pmb {x} {=} \pmb {0} . 4 \pmb {\mathrm{m}}$$

and the functions of Young’s modulus and coefficient of thermal expansion fitted on the data are rationally created as:

$$E = - 0.0917 T + 220.5073 ( {\mathrm{GPa}} ) , \alpha _ {T} = 0.0048 T + 10.6063 ( 10 ^ {- 6} / {} ^{\circ} \mathrm{C} )$$

The ITPS panel is simply supported on four edges of bottom face sheets and a linear temperature field ΔT is imposed on the entire panel. The temperature field for the bottom face sheets is $\Delta T _ {1} = 50 \quad \mathrm {~ ( ^ {o} C )}$ , the temperature field for the top face sheets is $\Delta T _ {3} = 250 ( ^{\circ} \mathrm{C} )$ , and the temperature field for the corrugated core is $\begin{array} {r} {\Delta T _ {2} = 250 \frac {z - z _ {l} ^ {( 2 )}} {h _ {2}} + 50 \bigg ( 1 - \frac {z - z _ {l} ^ {( 2 )}} {h _ {2}} \bigg )} \end{array}$ ° ( C) . According to the convergence study in literature [1], the mesh size of $32 \times 32$ is used to model the equivalent plate. The 3D finite element model employed for the ITPS panel is same as this in Section 5.1.

Figs. 17–19 show the normal stresses in the mid-plane, upper surface and lower surface of the corrugated webs, respectively. Figs. 20–22 show the normal stresses in the mid-plane, upper surface and lower surface of the top face sheets, respectively. Figs. 23–25 show the normal stresses in the mid-plane, upper surface and lower surface of the bottom face sheets, respectively. And Fig. 26 shows the in-plane shear stresses in the mid-plane of the corrugated webs, top face sheets and bottom face sheets, respectively. As a result, the stresses obtained by the present method agree well with those given by 3D finite element analysis. However, there have some differences between the proposed method and 3D FEM results. As shown in Figs. 17 and 18, the present method is unable to predict the normal stresses accurately in the edges of panel as same as the stresses in the middle area of panel. As shown in Figs. 20 and 21, the present method cannot predict the normal stresses accurately in the outer surfaces of top face sheet subjected to temperature distribution, only the trend of stresses can be captured.

(c). ${\sigma} _ {y y} ^ {m} ,$ x=0.4m

(d). ${\sigma} _ {\mathbf {y} {\mathbf {y}} ^ {\prime}} ^ {m}$ x=0.2m

5.3. Stress distributions of ITPS subjected to uniform transverse pressure and thermal loads

The stress distributions of ITPS panel considering temperature-dependent mechanical properties subjected to thermal and mechanical loads is compared here with the FEM results. The ITPS panel dimensions and material properties are all the same as those of the ITPS panel in Section 5.1. The ITPS panel is simply supported on four edges of bottom face sheets. The top face sheets are subjected to transverse loading $p = 0.1$ MPa on and the same linear temperature distribution ΔT as that in Section 5.2 is imposed on the entire panel. According to the convergence study above, the mesh size of 32 × 32 is used to model the equivalent plate.

(c). $\pmb {\sigma} _ {y y} ^ {z _ {2}} , \pmb {x} {=} \pmb {0.4 m}$ 
(c). $\sigma _ {y y} ^ {z 1} , x {=} 0.4 m$

(d). $\sigma _ {y y} ^ {z 1} , \kappa {=} 0.2 \ m$

(d). $\sigma _ {\mathrm{yy}} ^ {z 2} , \kappa {=} 0.2 \ m$

Figs. 27–29 show the normal stresses in the mid-plane, upper surface and lower surface of the corrugated webs, respectively. Figs. 30–32 show the normal stresses in the mid-plane, upper surface and lower surface of the top face sheets, respectively. Figs. 33–35 show the normal stresses in the mid-plane, upper surface and lower surface of the bottom face sheets, respectively. And Fig. 36 shows the in-plane shear stresses in the mid-plane of the corrugated webs, top face sheets and bottom face sheets, respectively. According to Figs. 27–36, the stress distributions by the proposed method have an excellent agreement with the FEM results. However, there have some differences between the proposed method and 3D FEM results. As shown in Figs. 27 and 28, the present method is unable to predict the normal stresses accurately in the edges of panel as same as the stresses in the middle area of panel.

(c). Bottom face sheet

(b). Top face sheet

(c). $\pmb {\sigma} _ {y y} ^ {m} , \pmb {x} {=} 0.4 \pmb {m}$

(d). ${\sigma} _ {y y} ^ {m} ,$ x=0.2m 
y(m)

## 6. Conclusions

This paper deals with the stress analysis of trapezoidal corrugated core ITPS panel subjected to thermal and mechanical loads. The equivalent rigidities method with temperature-dependent material properties and the ${\mathsf{C}} ^ {0}$ higher-order layerwise theory for equivalent sandwich plate introduced in our previous study [1] are used in this paper. By combining the equivalent sandwich model with the principle of structural mechanics, the normal and in-plane shear stress in corrugated webs, top face sheet and bottom face sheet are calculated, respectively. And the stresses induced by local deformations are considered in the prediction of stress. The comparisons between the results obtained by the present method and the FEM results have shown that the present method gives acceptable results for stress of ITPS panel subjected to thermal and mechanical loads. Otherwise, the present method is simpler and accurately, which can give a further economy for predicting stress distribution of ITPS panel.

(b). σ×x=02m 
(d). $\sigma _ {y y} ^ {\mathsf{m}} , \mathsf{x} {=} 0.2 \mathsf{m}$

(c). $\pmb {\sigma} _ {y y} ^ {z 1} , \pmb {x} {=} \pmb {0} . 4 \pmb {\mathrm{m}}$

(d). ${\mathfrak {o}} _ {\mathbf {y} \mathbf {y}} ^ {Z 1} ,$ x=0.2m

(c). ${\mathfrak {o}} _ {\mathbf {y} \mathbf {y}} ^ {z _ {2}} ,$ x=0.4m

(b). σx x=0.2m

(c). ${\sigma} _ {y y} ^ {m} ,$ x=0.4m

(c). $\sigma _ {y y} ^ {z 1} , x {=} 0.4 m$

(d). $\sigma _ {y y} ^ {z 1} , \kappa {=} 0.2 \ m$

(c). $\pmb {\sigma} _ {y y} ^ {z _ {2}} , \pmb {x} {=} \pmb {0.4 m}$

(d). $\sigma _ {\mathrm{yy}} ^ {z 2} , \kappa {=} 0.2 \ m$

(c). Bottom face sheet

## Omitted Tables

- [Table 1 omitted; saved to tables/table_001.md]
