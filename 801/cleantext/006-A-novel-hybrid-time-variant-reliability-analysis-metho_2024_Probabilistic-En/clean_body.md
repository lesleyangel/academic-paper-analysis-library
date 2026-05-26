## 1. Introduction

The reliability refers to the probability of a structure successfully achieving its intended functions during the entire lifespan under various uncertainties [1,2]. In the past few decades, many static reliability analysis methods [3–5] have been widely developed to measure the safety of structures. Time-variant uncertainties encountered in practical engineering [6], such as dynamic load and strength degradation, cannot be handled by those static methods. To address this issue, the time-variant reliability analysis (TRA) method has been developed recently. Generally, the TRA method can be classified into two main categories: extreme value-based methods and first passage-based methods.

In extreme value-based methods [7,8], time-variant reliability or failure probability is estimated by calculating the extreme value distribution of the limit-state function. In complex engineering applications, obtaining the probability characteristics of the extreme value analytically can be challenging. Simulation-based methods, such as Monte Carlo simulation (MCS) and importance sampling method [9], provide an alternative but expensive way to estimate the extreme value distribution. To reduce the computational burden, surrogate models, such as Kriging [10,11] and artificial neural networks [12,13], have been introduced into simulation-based methods. The single-loop Kriging (SILK) [14] method and mixed efficient global optimization (m-EGO) [15] method approximate the extreme value distribution based on constructed surrogate models of the extreme value function. The real-time estimation error-guided active learning Kriging (REAL) [16] method directly builds a surrogate model for the time-variant limit-state function.

In first passage-based methods, the failure probability is estimated by calculating the possibility that the out-crossing event occurs for the first time during a time interval [17,18]. The out-crossing event, according to the study [19], is defined as a system response crossing a specified threshold and entering the failure domain. Then, the out-crossing rate is defined as the probability that the out-crossing event occurs over a unit time. Based on whether or not the out-crossing rate should be calculated, the first passage-based method can be classified into two types: the out-crossing rate method and the time discretization-based TRA (TDTRA) method.

In the out-crossing rate method, the failure probability can be calculated by integrating the out-crossing rate under the assumption that all out-crossing events are mutually independent. Based on the above assumption, Andrieu-Renaud et al. [20] proposed the famous PHI2 method which approximates the out-crossing rate by the reliability indices and the autocorrelation of two successive time instants. Sudret [21] developed the improved PHI2 method which has a higher stability. However, those out-crossing rate methods may lead to large errors for the problems where out-crossing events are strongly dependent. To tackle the above problem, Madsen and Krenk [22] proposed a TRA method based on joint out-crossing rates. Hu and Du [23] combined the joint out-crossing rates and first-order reliability method (FORM) [24], and developed the joint out-crossing rates/FORM method.

In order to avoid computing the out-crossing rate, the TDTRA method has been developed recently. Jiang et al. [25] proposed the TRPD method in which the time-variant reliability problem is transformed into a time-invariant series system reliability problem through stochastic process discretization. Afterward, Jiang et al. [26] improved the TRPD method by simplifying the process of calculating time-variant reliability. Gong and Frangopol [27] developed the NEWREL method which calculates the most-probable point (MPP) at a large number of equidistant discrete time instants and then estimates the time-variant reliability based on the obtained MPPs. To achieve time-variant reliability with acceptable accuracy, the TDTRA methods introduced above should directly perform the FORM or MPP searches at numerous discrete time instants, which is computationally expensive. To address this issue, Zhang et al. [28] proposed an efficient TRA method based on approximating the MPP trajectory (MPPT), which can effectively reduce the number of MPP searches.

Based on the definition of uncertainty, there are two main types of uncertainties:

aleatory and epistemic uncertainties [29,30]. The aleatory uncertainties are caused by inherent variations of physical systems while the epistemic uncertainties are caused by the limitation of subjective cognitive level. The two categories of TRA methods mentioned above are based on probabilistic theory and can only solve problems with aleatory uncertainties. However, in many practical applications, epistemic uncertainties caused by the limitation of information or data of uncertain factors exist widely. In this situation, uncertain factors could be described as non-probabilistic interval variables [31]. Considering the time-variant effect, the non-probabilistic interval process model [32,33] was developed to describe time-variant epistemic uncertainties. Zhang et al. [34] proposed a linear uncertainty propagation method, in which the time-variant epistemic uncertainties are expressed as interval processes. Li et al. [35] developed a non-probabilistic TRA method to deal with problems involving time-variant interval variables.

Because there may exist both aleatory and epistemic uncertainties in a structure system, some reliability analysis methods considering hybrid uncertainties have been proposed [36–38]. However, research about TRA with hybrid uncertainties has been rarely performed. Shi et al. [39] proposed the second level limit state function to construct the hybrid time-variant reliability analysis (HTRA) model. Based on stochastic process discretization, Xie et al. [40] developed a multi-level meta-- model method to solve the TRA problems with stochastic and interval inputs. Zhao et al. [41] presented an envelope-function-based algorithm to deal with HTRA problems. However, in the above works about HTRA, time-variant epistemic uncertainties are not considered yet. Zhang et al. [42] proposed a new hybrid time-variant reliability model to handle time-variant epistemic uncertainties which are modeled as interval processes. They approximated the original limit-state function by a deep neural network, and then, the MCS method was used to estimate time-variant reliability. For HTRA in complex engineering applications, the limit-state function may contain a huge amount of random variables, stochastic processes, interval variables, and interval processes. In this situation, the difficulty and cost of exactly approximating the limit-state function will sharply rise.

According to previous research about TRA, based on time discretization, the failure probability can be estimated accurately with no need to construct complex approximated models of the time-variant limit-state function. In order to efficiently deal with HTRA problems with time-variant epistemic uncertainties in complex engineering applications, we develop an HTRA method by approximating the boundmost-probable point trajectory, referred to as the HABMPPT method. The main contributions of our work are as follows. (1) we propose the concept of the bound-most-probable point trajectory (BMPPT), which is defined as the moving trajectory of the bound-MPP (BMPP)in the independent standard normal space varying with time. (2) To estimate the failure probability efficiently, we linearize the lower and upper bounds of the time-variant limit-state function based on the BMPPT. (3) We use the active learning Kriging model to approximate the BMPPT which can significantly reduce the number of BMPP searches, to further improve the computational efficiency of the HABMPPT.

The remainder of this paper is organized as follows. Section 2 presents the conventional TRA problems only with stochastic uncertainties and TRA problems with hybrid uncertainties. Section 3 describes the proposed HABMPPT method in detail. To evaluate the effectiveness of the HABMPPT method, four examples are conducted in Section 4. Finally, conclusions are provided in Section 5.

## 2. Problem statement and direct solution method for HTRA

## 2.1. Time-variant reliability analysis problems

For conventional TRA, the uncertain variables are modeled as random variables or stochastic processes. The reliability can be defined as

$$P _ {\mathrm{r}} ( t _ {\mathrm{s}} , t _ {\mathrm{e}} ) = \mathrm{Pr} \{g ( \mathbf {X} , \mathbf {S} ( t ) , t ) < 0 , \forall t \in [ t _ {\mathrm{s}} , t _ {\mathrm{e}} ] \}\tag{1}$$

where Pr{⋅} denotes the probability of the safe or failure events occurring, $\mathbf {X} = [ X _ {1} , X _ {2} , . . . , X _ {n} ] ^ {\mathrm{T}}$ is an n-dimension random vector and $\mathbf {s} ( t ) =$ $[ S _ {1} ( t ) , S _ {2} ( t ) , . . . , S _ {m} ( t ) ] ^ {\mathrm{T}}$ is an m-dimension stochastic process vector, g(X, S(t), t) represents a general time-variant limit-state function. If g(X, S(t), $t ) > 0 ,$ the structure fails.

Based on probability theory and stochastic process models, the conventional TRA method was devised to evaluate the likelihood of a structure maintaining safe state throughout its lifecycle under timevariant uncertainties. In engineering applications, obtaining sufficient data for all uncertain variables can be challenging. To address this issue, interval process models were developed to portray time-variant epistemic uncertainties. The significant concepts of the interval process are introduced as follows.

For an interval process $\{I ( t ) , t \in T \}$ with the upper bound function $I ^ {\mathrm{U}} ( t )$ and lower bound function $I ^ {\mathrm{L}} ( t ) ,$ , the mid-value function $I ^ {\mathrm{M}} ( t )$ and radius function $I ^ {\mathrm{R}} ( t )$ can express as

$$I ^ {\mathrm {{M}}} ( t ) = \frac {I ^ {\mathrm {{U}}} ( t ) + I ^ {\mathrm {{L}}} ( t )} {2}\tag{2}$$

$$I ^ {\mathrm{R}} ( t ) = \frac {I ^ {\mathrm{U}} ( t ) - I ^ {\mathrm{L}} ( t )} {2}\tag{3}$$

For any two time instants $t _ {i} \in T$ and $t _ {j} \in T ,$ the auto-correlation function ρII(ti, tj) of I(t) can be defined as

$$\rho _ {I I} \left( t _ {i} , t _ {j} \right) = \frac {\mathrm{Cov} _ {I I} \left( t _ {i} , t _ {j} \right)} {\sqrt {I ^ {\mathrm{D}} \left( t _ {i} \right)} \sqrt {I ^ {\mathrm{D}} \left( t _ {j} \right)}}\tag{4}$$

where $\operatorname{Cov} _ {I I} ( t _ {i} , t _ {j} )$ is detailed in reference [32], $I ^ {\mathrm{D}} ( t _ {i} )$ and $I ^ {\mathrm{D}} ( t _ {j} )$ are the variance value of I(t) at time instants ti and tj.

Considering interval variables and interval process variables, the hybrid time-variant reliability can be defined as

$$P _ {\mathrm{r}} ( t _ {\mathrm{s}} , t _ {\mathrm{e}} ) = \operatorname* {P r} \{g ( \mathbf {X} , \mathbf {Y} , \mathbf {S} ( t ) , \mathbf {I} ( t ) , t ) < 0 , \forall t \in [ t _ {\mathrm{s}} , t _ {\mathrm{e}} ] \}\tag{5}$$

where $\mathbf {Y} = [ Y _ {1} , Y _ {2} , . . . , Y _ {p} ] ^ {\mathrm{T}}$ and $\mathbf {I} ( \mathrm{t} ) = [ I _ {1} ( t ) , I _ {2} ( t ) , . . . , I _ {q} ( t ) ] ^ {\mathrm{T}}$ are the interval vector and interval processes vector, respectively. p and q are respectively the numbers of interval variables and processes. It is worth noting that all uncertain variables in the time-variant limit-state function are independent of each other in this paper.

Based on the definition above, the time-variant failure probability of a structure can be expressed as

$$\begin{array} {r l} & {P _ {\mathrm{f}} \big ( t _ {\mathrm{s}} , t _ {\mathrm{e}} \big ) = \operatorname* {P r} \{g ( \mathbf {X} , \mathbf {Y} , \mathbf {S} ( t ) , \mathbf {I} ( t ) , t ) \ge 0 , \exists t \in \left[ t _ {\mathrm{s}} , t _ {\mathrm{e}} \right] \}} \\ & {= 1 - P _ {\mathrm{r}} \big ( t _ {\mathrm{s}} , t _ {\mathrm{e}} \big )} \end{array}\tag{6}$$

## 2.2. Direct solution method for HTRA based on MCS

For general HTRA problems, it is challenging to obtain the analytical solutions to Eqs. (5) and (6). As a commonly used numerical method, the MCS can directly estimate the solutions to Eqs. (5) and (6) by sampling. The implementation of the MCS for solving HTRA problems is introduced as follows.

Due to the interval variables and processes in the limit-state function, the time-variant failure probability needs to be regarded as an interval variable $[ P _ {\mathrm{f}} ^ {\mathrm{L}} , P _ {\mathrm{f}} ^ {\mathrm{U}} ]$ , which can be formulated as

$$P _ {\mathrm{f}} ^ {\mathrm{L}} ( t _ {\mathrm{s}} , t _ {\mathrm{e}} ) = \operatorname* {P r} \{\operatorname* {m i n} _ {\mathbf {I} ( t ) \in [ \mathbf {Y} ^ {\mathrm{L}} ( t ) , \mathbf {I} ^ {\mathrm{U}} ] _ {t} )} g ( \mathbf {X} , \mathbf {Y} , \mathbf {S} ( t ) , \mathbf {I} ( t ) , t ) \ge 0 , \exists t \in [ t _ {\mathrm{s}} , t _ {\mathrm{e}} ] \}\tag{7}$$

$$P _ {\mathrm{f}} ^ {\mathrm{U}} ( t _ {s} , t _ {\mathrm{e}} ) = \operatorname* {P r} \left\{\operatorname* {m a x} _ {\mathbf {I} ( t ) \in \left[ \mathbf {I} ^ {\mathrm{L}} ( t ) , \mathbf {I} ^ {\mathrm{U}} \right] _ {t} )} g ( \mathbf {X} , \mathbf {Y} , \mathbf {S} ( t ) , \mathbf {I} ( t ) , t ) \ge 0 , \exists t \in [ t _ {s} , t _ {\mathrm{e}} ] \right\}\tag{8}$$

Then, the time interval [ts, te] is discretized into M time instants, then Eqs. (7) and (8) can be accordingly discretized into

$$P _ {\mathrm{f}} ^ {\mathrm{L}} ( t _ {s} , t _ {\mathrm{e}} ) = \mathrm{Pr} \{\operatorname* {m a x} _ {t _ {i} \in [ t _ {s} , t _ {\mathrm{e}} ]} \{\operatorname* {m i n} _ {\substack {\mathbf {I} ( t ) \in [ \mathbf {I} ^ {\mathrm{L}} ( t _ {i} ) , \mathbf {I} ^ {\mathrm{U}} ] _ {( t _ {i} )}}} g ( \mathbf {X} , \mathbf {Y} , \mathbf {S} ( t _ {i} ) , \mathbf {I} ( t _ {i} ) , t _ {i} ) | i = 1 , 2 , . . . , M \} \geq 0 \}\tag{9}$$

$$P _ {\mathrm{f}} ^ {\mathrm{U}} ( t _ {s} , t _ {\mathrm{e}} ) = \mathrm{Pr} \{\operatorname* {m a x} _ {t _ {i} \in [ t _ {s} , t _ {\mathrm{e}} ]} \{\operatorname* {m a x} _ {\mathrm{I} ( t ) \in [ [ \mathbf {X} ^ {\mathrm{L}} ( t _ {i} ) , \mathbf {I} ^ {\mathrm{U}} \backslash t _ {i} ) ]} g ( \mathbf {X} , \mathbf {Y} , \mathbf {S} ( t _ {i} ) , \mathbf {I} ( t _ {i} ) , t _ {i} ) | i = 1 , 2 , . . . , M \} \geq 0 \}\tag{10}$$

Based on the MCS method, N samples of the random variables and stochastic processes can be generated. The lower and upper bound vectors of the discretized limit-state function with the jth sample of uncertain variables can be given by

$$\mathbf {g} _ {j} ^ {\mathrm{L}} = \underset {\mathbf {I} ( t ) \in \left[ \mathbf {I} ^ {\mathrm{L}} , \mathbf {I} ^ {\mathrm{U}} \right]} {\operatorname* {m i n}} \left\{g \left( \mathbf {X} _ {j} , \mathbf {Y} , \mathbf {S} _ {j} ( t _ {i} ) , \mathbf {I} ( t _ {i} ) \right) \big | i = 1 , 2 , . . . , M \right\}\tag{11}$$

$$\mathbf {g} _ {j} ^ {\mathrm{U}} = \operatorname* {m a x} _ {\mathbf {Y} \in \left[ \mathbf {Y} ^ {\mathrm{L}} , \mathbf {Y} ^ {\mathrm{U}} \right]} \left\{g \left( \mathbf {X} _ {j} , \mathbf {Y} , \mathbf {S} _ {j} ( t _ {i} ) , \mathbf {I} ( t _ {i} ) \right) \big | i = 1 , 2 , . . . , M \right\}\tag{12}$$

It is noted that Eqs. (11) and (12) can be solved based on samples of interval variables Y and I(ti) $( i = 1 , 2 , . . . , M )$ . The samples of I(ti) can be generated according to the sampling algorithm proposed by Jiang et al. [32]. Then, the failure indicator functions $I ^ {\mathrm{L}} ( \mathbf {g} _ {j} ^ {\mathrm{L}} )$ and $I ^ {\mathrm{U}} ( \mathbf {g} _ {j} ^ {\mathrm{U}} )$ can be defined as

$$I ^ {\mathrm{L}} \left( \mathbf {g} _ {j} ^ {\mathrm{L}} \right) = \left\{\begin{array} {l l} {1 , \quad \mathrm{max} \left( \mathbf {g} _ {j} ^ {\mathrm{L}} \right) \geq 0} \\ {0 , \quad \mathrm{otherwise}} \end{array} \right.\tag{13}$$

$$I ^ {\mathrm{U}} \Big ( \mathbf {g} _ {j} ^ {\mathrm{U}} \Big ) = \left\{\begin{array} {l l} {1 ,} & {\operatorname* {m a x} \Big ( \mathbf {g} _ {j} ^ {\mathrm{U}} \Big ) \geq 0} \\ {0 ,} & {\mathrm{otherwise}} \end{array} \right.\tag{14}$$

Thus, the failure probability can be estimated by

$$P _ {\mathrm{~f~}} ^ {\mathrm{L}} ( t _ {s} , t _ {e} ) \approx E \Big ( I ^ {\mathrm{L}} \left( \mathbf {g} _ {j} ^ {\mathrm{L}} \right) \Big )\tag{15}$$

$$P _ {\mathrm{~f~}} ^ {\mathrm{U}} ( t _ {s} , t _ {e} ) \approx E \Big ( I ^ {\mathrm{U}} \big ( \mathbf {g} _ {j} ^ {\mathrm{U}} \big ) \Big )\tag{16}$$

where E(⋅) is the expectation operator.

The MCS method is widely acknowledged for its excellent computational accuracy given sufficient samples, which will result in high computational costs due to numerical simulations for engineering problems. In order to effectively and efficiently solve the HTRA problem, this paper presents a novel hybrid time-variant reliability analysis method. The results calculated by the MCS are used to verify the proposed method.

## 3. The proposed method

## 3.1. Definition of the bound-most-probable point trajectory

For a time-variant reliability analysis with only stochastic uncertainty, we discretize the design lifetime $[ t _ {s} ,$ t ] into M time instants which are denoted as $t _ {i} ( i = 1 , 2 , . . . , M )$ , and the time-variant reliability problem is transformed into a time-independent series system reliability problem. Then, the FORM method is performed at each time instant to solve the time-independent subproblems. For the FORM method, the key step is to calculate the MPP which is defined as the most probable point in the failure domain. After that, the instantaneous limit-state function g (X, S(ti), ti) is linearized at the corresponding MPP and the failure of probability can be estimated analytically.

Based on the research of the AMPPT method [28], the stochastic variables X and S(t ) are transformed into independent standard normal random variables W and Zi. Simultaneously, g(X, S(ti), ti) is transformed into $g _ {i} ^ {\prime} \ ( \boldsymbol {\mathsf{W}} , \ \mathbf {Z} _ {i} )$ in the independent standard normal space (U-space). Then, the curve composed of all MPPs in the U-space is defined as MPPT. The schematic diagram in Fig. 1 shows the projection of the MPPT on the $U _ {1} - U _ {2}$ plane.

For time-variant reliability analysis under hybrid uncertainties, due to interval variables and interval process variables, the instantaneous limit-state in U-space is not a single hyper-surface but a strip with lower bound $s ^ {\mathrm{L}}$ and upper bound $s _ {\mathrm{~:~}} ^ {\mathrm{U}}$ , as is shown in $\mathrm{Fig.~} 2$

The lower and upper-bound MPP (LBMPP and UBMPP) in Fig. 2 represent two points with the shortest distance to U-space origin among all of points respectively on $s ^ {\mathrm{L}}$ and $s ^ {\mathrm{u}}$ . If we connect the LBMPPs of all discrete time instants, an LBMPP trajectory (LBMPPT) ${\bf u} _ {\mathrm{MPP}} ^ {\mathrm{L}} ( t ) ( t \in [ t _ {s} ,$ $t _ {\mathrm{e}} ] )$ can be obtained in the U-space. Similarly, the UBMPP trajectory (UBMPPT) $\mathbf {u} _ {\mathrm{MPP}} ^ {\mathrm{U}} ( t ) \ ( t \in \ [ t _ {s} , \ t _ {\mathrm{e}} ] )$ can be constructed by connecting the UBMPPs of all time instants. In this paper, the LBMPPT and UBMPPT are collectively referred as BMPPT.

## 3.2. Approximation of the bound-most-probable point trajectory

To search the LBMPPs and UBMPPs, the normalization is carried out to transform Y into standard interval variables P. It is noted that I(t) can be represented by q uncorrelated interval vectors based on the truncated interval K-L expansion [43]. The kth component of I(t) can be expressed as

$$I _ {k} ( t ) = I _ {k} ^ {\mathrm{M}} ( t ) + \sum _ {n = 1} ^ {n _ {\mathrm{t}}} I _ {k} ^ {\mathrm{R}} ( t ) \sqrt {\lambda _ {n}} \varphi _ {n} ( t ) \zeta _ {n}\tag{17}$$

where $n _ {\mathrm{t}}$ is the number of truncated terms of K-L expansion, $\zeta _ {n} \in [ - 1 , 1 ]$ $( n = 1 , 2 , . . . , n _ {\mathrm{t}} )$ are standard independent interval variables that satisfy $\textstyle \sum _ {n = 1} ^ {n _ {t}} \zeta _ {n} ^ {2} \leq 1 . \ \lambda _ {n}$ and $\varphi _ {n}$ represent the eigenvalues and eigenfunctions of the auto-correlation coefficient function respectively. Then, I(t) can be represented by $\mathbf {Q} = [ \zeta _ {1} , \zeta _ {2} , . . . , \zeta _ {q} ]$ , where $\zeta _ {k} = [ \zeta _ {1} , \zeta _ {2} , . . . , \zeta _ {n _ {t}} ] ^ {\mathrm{T}} ( k = 1 , 2 ,$ …, $q )$ $\mathbf {u} _ {\mathrm{MPP}} ^ {\mathrm{L}} ( t _ {i} ) = [ \mathbf {u} _ {\mathrm{MPP,W}} ^ {\mathrm{L}} ( t _ {i} ) , \mathbf {u} _ {\mathrm{MPP} , Z _ {i}} ^ {\mathrm{L}} ( t _ {i} ) ]$ and ${\bf u} _ {\mathrm{MPP}} ^ {\mathrm{U}} ( t _ {i} ) = [ {\bf u} _ {\mathrm{MPP,W}} ^ {\mathrm{U}} ( t _ {i} )$ ${\bf u} _ {\mathrm{MPP} , Z _ {i}} ^ {\mathrm{U}} ( t _ {i} ) ]$ can be respectively calculated by

$$\begin{array} {r} {\underset {\mathbf {u} _ {\mathrm{MPP}} ^ {\mathrm{L}} \left( t _ {i} \right)} {\mathrm{min}} \left\| \mathbf {u} _ {\mathrm{MPP}} ^ {\mathrm{L}} \big ( t _ {i} \big ) \right\|} \\ {\mathrm{s.t.} \quad \underset {\mathbf {P} , \mathbf {Q} _ {i}} {\mathrm{min}} G \Big ( \mathbf {u} _ {\mathrm{MPP,W}} ^ {\mathrm{L}} \big ( t _ {i} \big ) , \mathbf {u} _ {\mathrm{MPP} , Z _ {i}} ^ {\mathrm{L}} \big ( t _ {i} \big ) , \mathbf {P} , \mathbf {Q} , t _ {i} \Big ) = 0} \end{array}\tag{18}$$

$$\begin{array} {r} {\underset {\mathbf {u} _ {\mathrm{MPP}} ^ {\mathrm{U}} ( t _ {i} )} {\mathrm{min}} \left\| \mathbf {u} _ {\mathrm{MPP}} ^ {\mathrm{U}} ( t _ {i} ) \right\|} \\ {\mathrm{s.t.} \quad \underset {\mathbf {P} , \mathbf {Q} _ {i}} {\mathrm{max}} G \Bigl ( \mathbf {u} _ {\mathrm{MPP,W}} ^ {\mathrm{U}} \bigl ( t _ {i} \bigr ) , \mathbf {u} _ {\mathrm{MPP} , Z _ {i}} ^ {\mathrm{U}} ( t _ {i} ) , \mathbf {P} , \mathbf {Q} , t _ {i} \Bigr ) = 0} \end{array}\tag{19}$$

where the subscripts W and Zi represent the components in the subspace of W and $\mathbf {Z} _ {i} ,$ respectively. $G ( \mathbf {u} _ {\mathrm{MPP,W}} ^ {\mathrm{L}} ( t _ {i} ) , \mathbf {u} _ {\mathrm{MPP} , Z _ {i}} ^ {\mathrm{L}} ( t _ {i} ) , \mathbf {P} , \mathbf {Q} , t _ {i} )$ represents the limit-state function of g(X, Y, S(ti), I(ti), ti) transformed to the independent standard space. Equations (18) and (19) are two-layer nesting optimization problems which are solved by the sequential single-loop (SSL) method [44]. In the SSL method, the two-layer nesting optimization is decomposed into an inner-layer optimization for interval analysis and an outer-layer optimization for searching the LBMPP. The interval analysis and LBMPP search are performed independently in each iteration. The solution of the complicated two-layer nesting optimization will be obtained when the convergence condition is satisfied. The flowchart of the SSL method is shown in Fig. 3.

As aforementioned, the BMPPT $\mathbf {u} _ {\mathrm{MPP}} ^ {\mathrm{L}} ( t ) ~ ( t \in [ t _ {s} , t _ {e} ] )$ and $\mathbf {u} _ {\mathrm{MPP}} ^ {\mathrm{U}} ( t ) \ ( t \in [ t _ {s}$ $t _ {e} ] )$ , are considered as the functions over time which can be expressed by sufficient LBMPPs and UBMPPs at discrete time instants. However, a large number of SSL analyses will lead to a heavy computational burden which is unacceptable in engineering applications. To reduce the computational cost, the active learning Kriging is employed to approximate the BMPPT in the proposed method.

We take the LBMPPT as an example to build its approximation model by active learning Kriging. First, the time interval $[ t _ {s} , ~ t _ {\mathrm{e}} ]$ is discretized into $n _ {\mathrm{init}}$ time instants uniformly. Then, the LBMPPs at the discrete time instants are searched to obtain the initial training samples $\{( t _ {i} , \mathbf {u} _ {\mathrm{MPP}} ^ {\mathrm{L}} ( t _ {i} ) )$ ${\left| i {= 1 , 2 , . . . , n _ {i n i t}} \right\}}$ for constructing an initial Kriging model ${\widehat {u}} _ {\mathrm {{M P P}}} ^ {\mathrm{L}} ( t )$ with a n + m dimension output. For simplicity, the jth $( j = 1 , 2 , . . . , n \textrm -$ + m) dimension of ${\widehat {u}} _ {\mathrm {{M P P}}} ^ {\mathrm{L}} ( t )$ is denoted as ${\widehat {u}} _ {\mathrm{MPP} , j} ^ {\mathrm{L}} ( t )$ . It can be expressed by Eq. (20).

$${\widehat {u}} _ {\mathrm{MPP} , j} ^ {\mathrm{L}} ( t ) = f ( t ) + s ( t )\tag{20}$$

where ${\widehat {u}} _ {\mathrm{MPP} , j} ^ {\mathrm{L}} ( t )$ represents the approximation of the jth component of LMPPs ${\widehat {u}} _ {\mathrm{MPP} , j} ^ {\mathrm{L}} ( t )$ by the Kriging model, f(t) is the basis function of a regression model and s(t) is a stationary Gaussian process with zero mean and variance $\sigma ^ {2}$ . More details about the Kriging model can refer to Ref. [4].

To obtain a high-fidelity model of LBMPPT, the active learning process is carried out to refine the model ${\widehat {u}} _ {\mathrm{MPP}} ^ {\mathrm{L}} ( t )$ . In active learning, the active learning function is first defined, such as the prediction error or the real response value. Then new training samples are selected based on the characteristics of the model constructed by existent training samples and active learning function. In this paper, an active learning function $e ^ {\mathrm{L}} ( t )$ is defined in Eq. (21) to update the training sample set.

$$e ^ {\mathrm{L}} ( t ) = \frac {\sum _ {j = 1} ^ {n + m} e _ {j} ^ {\mathrm{L}} ( t )} {n + m}\tag{21}$$

As is shown in $( 21 ) , e _ {j} ^ {L} ( t ) ( j {=} 1 , 2 , . . . , n {+} m )$ are given equal weights to measure the prediction uncertainty of the multi-output model ${\widehat {u}} _ {\mathrm {{M P P}}} ^ {\mathrm{L}} ( t )$ The training samples with larger prediction uncertainty affect the approximation accuracy of the model significantly. In the active learning process, the candidate time instant $t ^ {*}$ is identified as

$$t ^ {*} = \arg \operatorname* {m a x} _ {t \in [ t _ {s} , t _ {\mathrm{c}} ]} e ^ {\mathrm{L}} ( t )\tag{22}$$

Then, an SSL procedure is carried out to search the LBMPP at $t ^ {*} ,$ and the sample $( t ^ {*} , \mathbf {u} _ {\mathrm{MPP}} ^ {\mathrm{L}} ( t ^ {*} ) )$ is added into the training sample set to update the Kriging model ${\widehat {u}} _ {\mathrm {{M P P}}} ^ {\mathrm{L}} ( t )$ . When the termination criterion in Eq. (23) is satisfied, we will obtain the LBMPPT model ${\widehat {u}} _ {\mathrm {{M P P}}} ^ {\mathrm{L}} ( t )$ with sufficient accuracy.

$$e ^ {\mathrm{L}} ( t ^ {*} ) \leq e _ {\mathrm{target}} ^ {\mathrm{L}}\tag{23}$$

## 3.3. Linearization of the bound of limit-state function

After approximating the BMPPT by ${\widehat {u}} _ {\mathrm {{M P P}}} ^ {\mathrm{L}} ( t )$ and ${\widehat {u}} _ {\mathrm {{M P P}}} ^ {\mathrm{U}} ( t )$ , the bounds of the limit-state function will be linearized. The lower and upper bounds of the instantaneous transformed limit-state function $G ( \mathbf {W} , \mathbf {Z} _ {i} , \mathbf {P} ,$ $\mathbf {Q} , t _ {i} )$ are respectively denoted as $G ^ {\mathrm{L}} ( \mathbf {W} , \mathbf {Z} _ {i} , \mathbf {P} , \mathbf {Q} , t _ {i} )$ and $G ^ {\mathrm{U}} ( \mathbf {W} , \mathbf {Z} _ {i} , \mathbf {P} , \mathbf {Q} , t _ {i} )$ For convenience, the linearization of $G ^ {\mathrm{L}} ( \mathbf {W} , \mathbf {Z} _ {i} , \mathbf {P} , \mathbf {Q} , t _ {i}$ ) is treated as an example.

Based on the FORM and approximated LBMPPT $\widehat {u} _ {\mathrm{MPP}} ^ {\mathrm{L}} ( t ) , G ^ {\mathrm{L}} ( \mathbf {W} , \mathbf {Z} _ {i} , \mathbf {P} ,$ $\mathbf {Q} , t _ {i} )$ is linearized at ${\widehat {u}} _ {\mathrm{MPP}} ^ {\mathrm{L}} ( t _ {i} )$ as

$$\begin{array} {r l} & {G ^ {\mathrm{L}} ( \mathbf {W} , \mathbf {Z} _ {i} , \mathbf {P} , \mathbf {Q} , t _ {i} ) \approx H ^ {\mathrm{L}} ( t _ {i} )} \\ & {= - \beta ^ {\mathrm{L}} ( t _ {i} ) + \big ( \mathbf {\alpha} \mathbf {\alpha} \big _ {\mathrm{W}} ^ {\mathrm{L}} ( t _ {i} ) \big ) ^ {T} \mathbf {W} + \Big ( \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} _ {\mathrm{Z} _ {i}} ^ {\mathrm{L}} ( t _ {i} ) \Big ) ^ {T} \mathbf {Z} _ {i}} \end{array}\tag{24}$$

where $\beta ^ {\mathrm{L}} ( t _ {i} )$ and $\mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\beta} \alpha ^ {\mathrm{~L~}} ( \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha \beta} \mathbf {\alpha} \mathbf {\alpha \beta} \mathbf {\alpha} \mathbf {\alpha \beta} \mathbf {\alpha} \mathbf {\alpha \beta} \mathbf {\alpha \beta} \mathbf {\alpha} \mathbf {\alpha \beta} \mathbf {\alpha \beta} \mathbf {\alpha \beta} \mathbf {\alpha \beta} \mathbf {\alpha \beta} \mathbf {\alpha \beta \beta} \mathbf \mathbf {\alpha \beta \beta} \mathbf \alpha \beta \beta \beta \mathbf {\alpha \beta} \mathbf \alpha \beta \mathbf {\alpha \beta \beta \beta \alpha} \mathbf \mathbf \beta \alpha \beta \beta \beta \beta \alpha \beta \mathbf \beta \beta \mathbf \alpha \beta \beta \mathbf \alpha \beta \mathbf \beta \beta \mathbf \alpha \beta \mathbf \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta$ respectively represent the instantaneous reliability index and the unit gradient vector at time instant ti. $\beta ^ {\mathrm{L}} ( t _ {i} )$ and $\mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\beta} \alpha ^ {\mathrm{~L~}} ( \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\alpha} \mathbf {\beta} \mathbf {\alpha \alpha} \mathbf {\alpha} \mathbf {\beta \alpha} \mathbf {\alpha \beta} \mathbf {\alpha \alpha} \mathbf {\beta \alpha} \mathbf {\alpha \beta} \mathbf {\alpha \beta} \mathbf {\alpha \beta} \mathbf {\alpha \beta} \mathbf {\alpha \beta} \mathbf {\alpha \beta} \mathbf {\alpha \beta \beta \alpha} \mathbf \beta \beta \beta \alpha \beta \mathbf {\alpha} \beta \beta \mathbf \alpha \beta \beta \mathbf \alpha \beta \beta \alpha \beta \beta \beta \alpha \beta \beta \mathbf \alpha \beta \beta \beta \mathbf \alpha \beta \beta \mathbf \alpha \beta \beta \mathbf \beta \alpha \beta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta$ can be calculated by

$$\begin{array} {r l} & {\quad \beta ^ {\mathrm{L}} ( t _ {i} ) = \left\| \widehat {\mathbf {u}} _ {\mathrm{MPP}} ^ {\mathrm{L}} ( t _ {i} ) \right\|} \\ & {\quad \mathbf {\alpha} ^ {\mathrm{L}} ( t _ {i} ) = \left[ \mathbf {\alpha} \mathbf {{\alpha}} \mathbf {{_ {W} ^ {\mathrm{L}}}} ( t _ {i} ) , \mathbf {\alpha} \mathbf {{_ {C} ^ {\mathrm{L}}}} ( t _ {i} ) \right]} \\ & {\quad \quad \mathbf {\alpha} \mathbf {{_ {W} ^ {\mathrm{L}}}} ( t _ {i} ) = \frac {\widehat {\mathbf {u}} _ {\mathrm{MPP,W}} ^ {\mathrm{L}} ( t _ {i} )} {\beta ^ {\mathrm{L}} ( t _ {i} )}} \\ & {\quad \quad \mathbf {\alpha} \mathbf {{_ {C} ^ {\mathrm{L}}}} ( t _ {i} ) = \frac {\widehat {\mathbf {u}} _ {\mathrm{MP,Z} _ {i}} ^ {\mathrm{L}} ( t _ {i} )} {\beta ^ {\mathrm{L}} ( t _ {i} )}} \end{array}\tag{25}$$

According to $\mathtt {E q .} ( 24 )$ , the linear combination $H ^ {\mathrm{L}} ( t _ {i} )$ of the independent standard normal variables W and $\mathbf {Z} _ {i}$ should be a normal random variable. The mean and variance of $H ^ {\mathrm{L}} ( t _ {i} )$ can be computed by Eqs. (26) and (27), respectively.

$$\begin{array} {r l} {E \big [ H ^ {\mathrm{L}} ( t _ {i} ) \big ] =} & {E \Big [ - \beta ^ {\mathrm{L}} ( t _ {i} ) + \big ( \mathbf {{\boldsymbol {\mathsf{a}}}} _ {\mathrm{W}} ^ {\mathrm{L}} ( t _ {i} ) \big ) ^ {T} \mathbf {W} + \Big ( \mathbf {{\boldsymbol {\mathsf{a}}}} _ {\mathrm{Z} _ {i}} ^ {\mathrm{L}} ( t _ {i} ) \Big ) ^ {T} \mathbf {Z} _ {i} \Big ] = E \big ( - \beta ^ {\mathrm{L}} ( t _ {i} ) \big )} \\ & {+ \big ( \mathbf {{\boldsymbol {\mathsf{a}}}} _ {\mathrm{W}} ^ {\mathrm{L}} ( t _ {i} ) \big ) ^ {T} E ( \mathbf {W} ) + \Big ( \mathbf {{\boldsymbol {\mathsf{a}}}} _ {\mathrm{Z} _ {i}} ^ {\mathrm{L}} ( t _ {i} ) \Big ) ^ {T} E ( \mathbf {Z} _ {i} )} \end{array}$$

$$= - \beta ^ {\mathrm{L}} ( t _ {i} )\tag{26}$$

$$\begin{array} {r l r} {{D \big [ H ^ {\mathrm{L}} ( t _ {i} ) \big ] = D \Big [ - \beta ^ {\mathrm{L}} ( t _ {i} ) + \big ( \pmb {\alpha} _ {\mathrm{W}} ^ {\mathrm{L}} ( t _ {i} ) \big ) ^ {T} \mathbf {W} + \Big ( \pmb {\alpha} _ {\mathrm{Z} _ {i}} ^ {\mathrm{L}} ( t _ {i} ) \Big ) ^ {T} \mathbf {Z} _ {i} \Big ]}} \\ & {} & {= D \big ( - \beta ^ {\mathrm{L}} ( t _ {i} ) \big ) + \big \| \pmb {\alpha} _ {\mathrm{W}} ^ {\mathrm{L}} ( t _ {i} ) \big \| ^ {2} D ( \mathbf {W} ) + \big \| \pmb {\alpha} _ {\mathrm{Z} _ {i}} ^ {\mathrm{L}} ( t _ {i} ) \big \| ^ {2} D ( \mathbf {Z} _ {i} )} \\ & {} & {= \| \frac {\widehat {\mathbf {u}} _ {\mathrm{MPP,W}} ^ {\mathrm{L}} ( t _ {i} )} {\beta ^ {\mathrm{L}} ( t _ {i} )} \| ^ {2} + \| \frac {\widehat {\mathbf {u}} _ {\mathrm{MPP,Z} _ {i}} ^ {\mathrm{L}} ( t _ {i} )} {\beta ^ {\mathrm{L}} ( t _ {i} )} \| ^ {2} = 1} \end{array}\tag{27}$$

If $G ^ {\mathrm{L}} ( \mathbf {W} , \mathbf {Z} , \mathbf {P} , \mathbf {Q} , t )$ is linearized at each LBMPP of ${\widehat {u}} _ {\mathrm{MPP}} ^ {\mathrm{L}} ( t )$ , we will obtain a Gaussian process $H ^ {\mathrm{L}} ( t )$ whose mean function $\cdot \mu ^ {\mathrm{L}} ( t )$ and standard deviation function $\sigma ^ {\mathrm{L}} ( t )$ are calculated by

$$\begin{array} {l} {\mu ^ {\mathrm{L}} ( t ) {=} - \beta ^ {\mathrm{L}} ( t )} \\ {{\sigma ^ {\mathrm{L}} ( t ) {=} 1}} \end{array}\tag{28}$$

The autocorrelation function $\rho ^ {\mathrm{L}} ( t _ {1} , t _ {2} )$ of $H ^ {\mathrm{L}} ( t )$ is given by

$$\begin{array} {r} {\rho ^ {\mathrm{L}} \big ( t _ {1} , t _ {2} \big ) = \big ( \mathbf {4} \mathbf {w} \big ( t _ {1} \big ) \big ) ^ {T} \mathbf {4} \mathbf {w} \big ( t _ {2} \big ) + \big ( \mathbf {4} \mathbf {z} _ {i} ( t _ {1} ) \big ) ^ {T} \mathbf {C} \big ( t _ {1} , t _ {2} \big ) \mathbf {a} _ {\mathrm{Z} _ {i}} ( t _ {2} \big )} \end{array}\tag{29}$$

where the $m \times m$ correlation coefficient matrix $\mathbf {C} ( t _ {1} , t _ {2} )$ is expressed by

$$\mathbf {C} ( t _ {1} , t _ {2} ) = \left[ {\begin{array} {c c c c c} {\rho _ {\mathrm{Z}} ^ {\mathrm{L}} ( Z _ {1} ( t _ {1} ) , Z _ {1} ( t _ {2} ) )} & {0} & {\cdots} & {0} \\ {0} & {\rho _ {\mathrm{Z}} ^ {\mathrm{L}} ( Z _ {2} ( t _ {1} ) , Z _ {2} ( t _ {2} ) )} & {\cdots} & {0} \\ {\vdots} & {\vdots} & {\ddots} & {\vdots} \\ {0} & {0} & {\cdots} & {\rho _ {\mathrm{Z}} ^ {\mathrm{L}} ( Z _ {m} ( t _ {1} ) , Z _ {m} ( t _ {2} ) )} \end{array}} \right] _ {m \times \mathrm{~H~W~}}\tag{30}$$

where $Z _ {i} ( t _ {1} )$ and $\mathsf{Z} _ {i} ( t _ {2} ) ( i {=} 1 , 2 , . . . , m )$ are two standard normal variables transformed from stochastic process $Y _ {i} ( t )$ at time instants $t _ {1}$ and $t _ {2}$ $\rho _ {Z} ^ {\mathrm{L}} ( Z _ {i} ( t _ {1} ) , Z _ {i} ( t _ {2} ) )$ presents the correlation coefficient of $Z _ {i} ( t _ {1} )$ and $Z _ {i} ( t _ {2} )$ which is detailed in reference [45].

## 3.4. Estimation of time-variant failure probability using MCS

Based on the BMPPT model L MPP(t) and U MPP(t), the lower and upper bounds of the limit-state function are transformed into two Gaussian processes $H ^ {\mathrm{L}} ( t )$ and $H ^ {\mathrm{U}} ( t )$ . Thus, the HTRA problem is transformed into two TRA with only stochastic uncertainty. In this paper, the expansion optimal linear estimation (EOLE) [46] is employed to generate the samples of $H ^ {\mathrm{L}} ( t )$ and $H ^ {\mathrm{U}} ( t )$

With $n _ {\mathrm{d}}$ equidistant time instants selected within the time interval $[ t _ {s} ,$ $t _ {\mathrm{e}} ] ,$ the covariance matrix $\Sigma ^ {\mathrm{L}}$ of $H ^ {\mathrm{L}} ( t )$ is expressed by

$$\pmb {\Sigma} ^ {\mathrm{L}} = \left[ \begin{array} {c c c c} {c ^ {\mathrm{L}} \big ( t _ {1} , t _ {1} \big )} & {c ^ {\mathrm{L}} \big ( t _ {1} , t _ {2} \big )} & {\cdots} & {c ^ {\mathrm{L}} \big ( t _ {1} , t _ {n _ {\mathrm{d}}} \big )} \\ {c ^ {\mathrm{L}} \big ( t _ {2} , t _ {1} \big )} & {c ^ {\mathrm{L}} \big ( t _ {2} , t _ {2} \big )} & {\cdots} & {c ^ {\mathrm{L}} \big ( t _ {2} , t _ {n _ {\mathrm{d}}} \big )} \\ {\vdots} & {\vdots} & {\ddots} & {\vdots} \\ {c ^ {\mathrm{L}} \big ( t _ {n _ {\mathrm{d}}} , t _ {1} \big )} & {c ^ {\mathrm{L}} \big ( t _ {n _ {\mathrm{d}}} , t _ {2} \big )} & {\cdots} & {c ^ {\mathrm{L}} \big ( t _ {n _ {\mathrm{d}}} , t _ {n _ {\mathrm{d}}} \big )} \end{array} \right] _ {n _ {\mathrm{d}} \times n _ {\mathrm{d}}}\tag{31}$$

where $c ^ {\mathrm{L}} ( t _ {i} , t _ {j} ) = \sigma ^ {\mathrm{L}} ( t _ {i} ) \sigma ^ {\mathrm{L}} ( t _ {j} ) \rho ^ {\mathrm{L}} ( t _ {1} , t _ {2} ) ( i , j = 1 , 2 , . . . , n _ {\mathrm{d}} )$ is the covariance of $H ^ {\mathrm{L}} ( t _ {i} )$ and $H ^ {\mathrm{L}} ( t _ {j} )$ . The eigenvalues and eigenvectors of $\Sigma ^ {\mathrm{L}}$ are respectively denoted as $\lambda _ {h} ^ {\mathrm{L}}$ and $\mathbf {Q} _ {h} ^ {\mathrm{L}} ( h = 1 , 2 , . . . , n _ {\mathrm{d}} )$ . With the mean function $\mu ^ {\mathrm{L}} ( t )$ , the Gaussian process $H ^ {\mathrm{L}} ( t )$ is approximated by the series expansion as

$$H ^ {\mathrm{L}} ( t ) \approx \mu ^ {\mathrm{L}} ( t ) + \sigma ^ {\mathrm{L}} ( t ) \sum _ {h = 1} ^ {p ^ {\mathrm{L}}} \frac {\xi _ {h}} {\sqrt {\lambda _ {h} ^ {\mathrm{L}}}} \big ( \mathbf {Q} _ {h} ^ {\mathrm{L}} \big ) ^ {T} \mathbf {\vec {p}} ^ {\mathrm{L}} ( t )\tag{32}$$

where $\xi _ {h} ~ ( h = 1 , 2 , . . . , p ^ {\mathrm{L}} )$ are independent standard normal random variables, $\mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\rho} \mathbf {\ p} ^ {\mathrm{L}} ( t )$ is the correlation vector $\left[ \rho ^ {L} ( t , t _ {1} ) , \rho ^ {L} ( t , t _ {2} ) , . . . , \rho ^ {L} ( t , t _ {p ^ {L}} ) \right] ^ {\mathrm{T}}$ , $p ^ {\mathrm{L}}$ represents the number of expansion terms, and $p ^ {\mathrm{L}} \leq n _ {\mathrm{d}}$ . When $p ^ {\mathrm{L}} = n _ {\mathrm{d}}$ there is no truncation error.

By varying $\xi _ {h} ,$ we obtain a sample $\mathrm{H} ^ {\mathrm{L}} = [ h _ {1} , h _ {2} , . . . , h _ {n _ {d}} ]$ of $H ^ {\mathrm{L}} ( t )$ at nd equidistant time instants. Then, the indicator function $I ( \mathbf {H} ^ {\mathrm{L}} )$ is defined as

$$I \big ( \mathbf {H} ^ {\mathrm{L}} \big ) = \left\{\begin{array} {l l} {1 ,} & {\mathrm{if} \underset {i = 1} {\overset {n _ {d}} {\operatorname* {m a x}}} h _ {i} \ge 0} \\ {0 ,} & {\mathrm{otherwise}} \end{array} \right.\tag{33}$$

As is shown in Eq. (33), a failure occurs if I(HL ) = 1. By generating $N _ {\mathrm{MCS}}$ samples ${\bf {H}} _ {j} ^ {\mathrm {{L}}}$ of $H ^ {\mathrm{L}} ( t )$ , the upper bound of time-variant failure probability $P _ {\mathrm{f}} ^ {\mathrm{U}} \left( t _ {s} , t _ {e} \right)$ is given as

$$P _ {\mathrm{f}} ^ {\mathrm{U}} ( t _ {\mathrm{s}} , t _ {\mathrm{e}} ) \approx \sum _ {j = 1} ^ {N _ {\mathrm{MCS}}} I \Big ( \mathbf {H} _ {j} ^ {\mathrm{L}} \Big ) \Big / N _ {\mathrm{MCS}}\tag{34}$$

Similarly, with $N _ {\mathrm{MCS}}$ samples ${\bf {H}} _ {k} ^ {\mathrm{U}}$ of $H ^ {\mathrm{U}} ( t )$ , the lower bound of timevariant failure probability $P _ {\mathrm{f}} ^ {\mathrm{L}} ( t _ {s} , t _ {e} )$ is estimated by

$$P _ {\mathrm{f}} ^ {\mathrm{L}} ( t _ {\mathrm{s}} , t _ {\mathrm{e}} ) \approx \sum _ {j = 1} ^ {N _ {\mathrm{MCS}}} I \big ( \mathbf {H} _ {k} ^ {\mathrm{U}} \big ) \big / N _ {\mathrm{MCS}}\tag{35}$$

Since the time-variant reliability analysis is based on the built Kriging models, there is no need to evaluate the complex original limitstate functions. Then, the parameters $n _ {\mathrm{d}} , p ^ {\mathrm{L}} , p ^ {\mathrm{U}} ;$ , and $N _ {\mathrm{MCS}}$ can be set to relatively large values to achieve higher accuracy.

## 3.5. The implementation procedure of the HABMPPT

The complete procedure of the proposed method contains three main parts. First, the BMPPT is approximated by the active learning Kriging model. Second, the lower and upper bounds of the time-variant limitstate function are linearized to Gaussian processes $H ^ {\mathrm{L}} ( t )$ and $H ^ {\mathrm{U}} ( t )$ based on the approximated BMPPT. Third, the samples of the two transformed Gaussian processes are generated and the lower and upper bounds of the time-variant failure probability $P _ {\mathrm{f}} ^ {\mathrm{L}} ( t _ {s} , t _ {e} )$ and $P _ {\mathrm{f}} ^ {\mathrm{U}} ( t _ {s} , t _ {e} )$ are estimated by MCS. The implementation procedure of the proposed HABMPPT method is summarized in Table 1, and its flowchart is illustrated in Fig. 4.

## 4. Examples and discussions

In this section, two numerical examples including a cantilever beam, and a 10-bar truss, and two engineering applications of the solid rocket engine shell and the rocket inter-stage structure are investigated to validate the proposed HABMPPT method. To further verify the proposed method, the classical MCS method and an HTRA method based on time discretization (TDHTRA) are also used to solve these examples. In the TDHTRA, the BMPPT is constructed by directly searching the BMPPs at all discrete time instants, and then the same procedure as HABMPPT is performed to estimate the bound of the failure probability. The evaluation numbers of the original limit-state function $N _ {\mathrm{FE}}$ and the relative errors of time-variant failure probability εL and $\varepsilon _ {\mathrm{f}} ^ {\mathrm{U}}$ are used to evaluate the performance of the methods. For the TDHTRA and the HABMPPT, the number of BMPP searches $N _ {\mathrm{BMPP}}$ is also used to measure the efficiency of estimation. According to reference [28], considering both efficiency and accuracy of the active learning process, the initial sampling number and the target error of the approximated BMPPT are respectively set to 3 and $10 ^ {- 4}$ . All the examples are repeatedly solved 10 times by each method to evaluate their robustness.

## 4.1. A corroded steel beam

In the second example, we consider a corroded simply-supported steel beam [15]. The structure of the steel beam is shown in Fig. 5. The beam has a span of L and an initial rectangular cross-section of $b _ {0} \times$ h . Due to corrosion, the width b(t) and height h(t) of the cross-section decrease with time. b(t) and h(t) are modeled as two non-stationary interval processes. The mid-value, radius and auto-correlation functions of b(t) and h(t) are given by

$$\begin{array} {r l} & {b ^ {\mathrm{M}} ( t ) {=} 0.2-2 k t} \\ & {b ^ {\mathrm{R}} ( t ) {=} 0.01} \\ & {\rho _ {b b} ( t _ {1} , t _ {2} ) = \exp ( {- | t _ {1} - t _ {2} | / 3} )} \end{array}\tag{36}$$

$$\begin{array} {r l} & {{\boldsymbol {h}} ^ {\mathrm{M}} ( t ) = 0.04-2 k t} \\ & {{\boldsymbol {h}} ^ {\mathrm{R}} ( t ) = 0.002} \\ & {\rho _ {h h} ( t _ {1} , t _ {2} ) = \exp ( {- | t _ {1} - t _ {2} |} / {3} )} \end{array}\tag{37}$$

where k is the corrosion rate. Furthermore, this simply-supported steel beam experiences two types of loads: a self-weight-induced load that is uniformly distributed on the structure and a concentrated dynamic load F(t) at the midpoint of the beam.

The failure event occurs if the maximum stress of the beam surpasses the yield limit σ of steel. The time-variant limit-state function of this problem is defined as

$$g ( \sigma , L , \rho , b ( t ) , h ( t ) , F ( t ) ) = \left( \frac {F ( t ) L} {4} + \frac {\rho b ( t ) h ( t ) L ^ {2}} {8} \right) - \frac {b ( t ) h ( t ) ^ {2}} {4} \sigma\tag{38}$$

where $\rho$ is the density of the material. The probabilistic characteristics of all variables are summarized in Table 2.

As is shown in Table $^ {2 ,}$ the dynamic load F(t) is modeled as a stationary Gaussian process. Considering the uncertainty of material properties, the yield limit E and the density ρ are respectively viewed as a random variable and an interval variable.

For the MCS, the investigated time range [0, 30] months is discretized into 200 evenly spaced time instants, and $1 \times 10 ^ {6}$ samples of the stochastic variables are generated at each time instant. For efficient and accurate interval analysis, 300 samples of each interval variable and process are generated, respectively. For the TDHTRA, three different cases (TDHTRA-30, TDHTRA-100 and TDHTRA-200) are considered, where the discrete time instants are set to 30, 100 and 200 accordingly. For the proposed HABMPPT, we evenly discretize the time interval [0, 30] into three time instants to create the initial training samples. After linearizing the lower and upper bounds of limit-state function, 200 equidistant time instants are used to estimate the time-variant failure probability.

After adding one more LBMPP and UBMPP, the approximated LBMPPT and UBMPPT satisfy the requirement of accuracy. Fig. 6 illustrates the curves of time-variant failure probability obtained by the MCS, TDHTRA and HABMPPT. Table 3 shows the results of solving the example by all the methods.

As is seen in Fig. 6, during the time span under consideration, the HABMPPT is more accurate than the TDHTRA-30 and TDHTRA-100. According to Table 3, the lower and upper bounds of the failure probability calculated by the HABMPPT are $\stackrel - {5} . 252 \times 10 ^ {- 2}$ and $3.853 \times 10 ^ {- 1}$ , respectively. The relative errors are respectively 0.57 % and 2.33 %. For the TDHTRA, the accuracy is gradually improved, when the number of discrete time points increases from 30 to 200. The TDHTRA and HABMPPT achieve similar accuracy with 200 discrete time points. Considering that the TDHTRA and HABMPPT employ the same procedure to estimate the bound of failure probability after obtaining all BMPPs, the accuracy of HABMPPT will increase with the increase of the number of discrete time points as same as TDHTRA.

In terms of the estimation efficiency, the proposed HABMPPT method requires 8 BMPP searches with 27137 FEs. By the TDHTRA-30, TDHTRA-100 and TDHTRA-200, the number of FEs needed are respectively 144849, 379132 and 863499, which are much more than that by the HABMPPT. In summary, the results of this example demonstrate that the proposed HABMPPT is more efficient and shows high accuracy.

## 4.2. A 10-bar truss

A 10-bar truss $[ 26 , 39 ]$ shown in Fig. 7 is used to illustrate the performance of the proposed HABMPPT method. The length of the horizontal and vertical bar is L. $A _ {i} ( i = 1 , 2 , . . . , 10 )$ and E denote the cross-sectional areas and the elastic modulus of the bars, respectively. It is seen in Fig. 7 that joint 4 is subjected to a vertical load $F _ {1} ( t ) ,$ , and joint 2 is under a horizontal load $F _ {3} ( t )$ and a vertical load F2(t). In this example, the horizontal load is viewed as an interval process, while the two vertical loads are described as stationary Gaussian processes. The maximum deflection $d _ {\mathrm{m}} ( t )$ of the truss is required to be smaller than or equal to the allowable displacement $d ( t ) = d _ {0} ( 1-0.02 t )$ , where d0 is the initial value of d(t). The limit-state function is given by

$$g ( t ) = d _ {m} ( t ) - d ( t )\tag{39}$$

where $d _ {\mathrm{m}} ( t )$ can be calculated by Eqs. (40)-(42).

(a) The lower bound

(b) The upper bound

Probabilistic characteristics of the variables of the 10-bar truss.

$$\left\{\begin{array} {l l} {N _ {1} ( t ) = F _ {5} ( t ) - \frac {\sqrt {2}} {2} N _ {8} ( t ) , N _ {2} ( t ) = - \frac {\sqrt {2}} {2} N _ {10} ( t )} \\ {N _ {3} ( t ) = - F _ {1} ( t ) - 2 F _ {2} ( t ) + F _ {3} ( t ) - \frac {\sqrt {2}} {2} N _ {8} ( t )} \\ {N _ {4} ( t ) = - F _ {2} ( t ) + F _ {3} ( t ) - \frac {\sqrt {2}} {2} N _ {10} ( t )} \\ {N _ {5} ( t ) = - F _ {2} ( t ) - \frac {\sqrt {2}} {2} N _ {8} ( t ) - \frac {\sqrt {2}} {2} N _ {10} ( t ) , N _ {6} ( t ) = - \frac {\sqrt {2}} {2} N _ {10} ( t )} \\ {N _ {2} ( t ) = \sqrt {2} \big ( F _ {1} ( t ) + F _ {2} ( t ) \big ) + N _ {8} ( t ) , N _ {8} ( t ) = \frac {a _ {20}} {a _ {11} a _ {2} - a _ {12} a _ {21}}} \\ {N _ {9} ( t ) = \sqrt {2} F _ {2} ( t ) + N _ {10} ( t ) , N _ {10} ( t ) = \frac {a _ {11} b _ {2} ( t )} {a _ {11} a _ {2} - a _ {12} a _ {11}}} \end{array} \right$$

$$\left\{\begin{array} {l} {\displaystyle a _ {11} = \left( \frac {1} {A _ {1}} + \frac {1} {A _ {3}} + \frac {1} {A _ {5}} + \frac {2 \sqrt {2}} {A _ {7}} + \frac {2 \sqrt {2}} {A _ {8}} \right) \frac {L} {2 E}} \\ {\displaystyle a _ {12} = a _ {21} = \frac {L} {2 A _ {5} E}} \\ {\displaystyle a _ {22} = \left( \frac {1} {A _ {2}} + \frac {1} {A _ {4}} + \frac {1} {A _ {6}} + \frac {2 \sqrt {2}} {A _ {9}} + \frac {2 \sqrt {2}} {A _ {10}} \right) \frac {L} {2 E}} \\ {\displaystyle b _ {1} ( t ) = \left( \frac {F _ {2}} {A _ {1}} - \frac {F _ {1} + 2 F _ {2} - F _ {3} ( t )} {A _ {3}} - \frac {F _ {2}} {A _ {5}} - \frac {2 \sqrt {2} \left( F _ {1} + F _ {2} \right)} {A _ {7}} \right) \frac {\sqrt {2} L} {2 E}} \\ {\displaystyle b _ {2} ( t ) = \left( \frac {\sqrt {2} \left( F _ {3} ( t ) - F _ {2} \right)} {A _ {4}} - \frac {\sqrt {2} F _ {2}} {A _ {5}} - \frac {4 F _ {2}} {A _ {9}} \right) \frac {L} {2 E}} \end{array} \right.\tag{40}$$

(41)

$$d _ {m} ( t ) = \left( \sum _ {i = 1} ^ {6} \frac {N _ {i} ^ {0} ( t ) N _ {i} ( t )} {A _ {i}} + \sqrt {2} \sum _ {i = 7} ^ {10} \frac {N _ {i} ^ {0} ( t ) N _ {i} ( t )} {A _ {i}} \right) \frac {L} {E}\tag{42}$$

where $N _ {i} ^ {0}$ can be calculated by Eqs. (40) and (41) with a substitution of $F _ {1} ( t ) = F _ {3} ( t ) = 0$ and $F _ {2} ( t ) = 1$ . The probabilistic characteristics of all involved variables are listed in Table 4.

As is shown in Table $^ {4 ,}$ there are in total 16 uncertain variables.

(a) The lower bound

(b) The upper bound

When using MCS, the time interval [0, 10] years under investigation is discretized into 100 equally spaced time instants, and $1 \times {10} ^ {6}$ samples are generated at each time instant. 100 samples of each interval variable and each interval process are respectively generated for efficient and accurate interval analysis. The TDHTRA with three different settings is employed to solve the HTRA problem, where the discrete time points are respectively 60, 80 and 100. For the proposed HABMPPT, we select three equidistant time instants to obtain the initial training samples. After linearizing the lower and upper bounds of the limit-state function, 100 equidistant time instants are used to estimate the time-variant failure probability. In this example, an extra LBMPP and an extra UBMPP are added before meeting the required accuracy of the approximated LBMPPT and UBMPPT.

Fig. 8 shows the curves of the time-variant failure probability obtained by the MCS, TDHTRA and HABMPPT. To investigate the efficiency and accuracy of the HABMPPT, Table 5 gives the results by the three methods.

As is shown in Fig. 8, the curves obtained by the proposed HABMPPT are quite close to the curves estimated by the MCS. With respect to Table 5, the HABMPPT has the lowest relative errors of 4.72 % and 3.17 % in comparison with the MCS, demonstrating that the HABMPPT method can accurately solve the HTRA problem of the 10-bar truss. For the TDHTRA, the accuracy improves obviously as the number of the discrete time points increases from 60 to 100. When using the same number of equidistant time points, the TDHTRA has close relative computational errors with the HABMPPT. Based on the above results, the accuracy of HABMPPT also can be improved as the increase of the number of discrete time points in this example.

In terms of calculation efficiency, the MCS calls the original limitstate function $1 \times 10 ^ {10}$ times, while the HABMPPT only requires 2690 FEs. In the three TDHTRA cases, the number of FEs needed are 28603, 38129 and 47647, respectively. In conclusion, the result shows that the HABMPPT is more efficient than the MCS. Furthermore, with similar accuracy, the HABMPPT shows higher efficiency than the TDHTRA in this example.

## 4.3. A solid rocket engine shell structure

In this example, the HTRA of the shell structure of a solid rocket engine [28] is carried out by the MCS, TDHTRA and HABMPPT. Solid rocket engines are widely utilized as boosters for launches. Generally, a solid rocket engine is composed of three main parts: a metal shell, an insulation layer, and a propellant grain. The combustion chamber is located through the opening in the cylindrical metal shell which contains the solid propellant grain. After being lit, the solid propellant burns in the combustion chamber to transform chemical energy into heat energy. Then, under high heat and pressure, the combustion product is created. The combustion product flows through the nozzle and is accelerated. The high-speed flow can procedure thrust due to counter-acting force.

A schematic diagram of the solid-propellant engine is shown in Fig. 9, where $D _ {s}$ is the inner diameter of the shell, $D _ {\mathrm{t0}}$ is the initial diameter of the nozzle throat, L and $H _ {0}$ are respectively the length and initial thickness of the propellant. The shell of the engine bears a high pressure. Affected by the rising temperature, the allowable pressure of the shell can be calculated by $P _ {\mathrm{a}} ( t ) = ( 1-0.002 t ) P _ {\mathrm{a} 0} ,$ where $P _ {\mathrm{a0}}$ is the initial value of $P _ {\mathrm{a}} ( t )$ . The failure event occurs, if the pressure P(t) beard by the shell is larger than $P _ {\mathrm {{a}}} ( t )$ . Thus, the time-variant limit-state function is defined as

$$g ( t ) = k P ( t ) - P _ {\mathrm{a}} ( t )\tag{43}$$

where k is a stochastic process parameter according to the combustion

instability [47]. The calculation of $P ( t )$ is introduced as follows.

Under the erosion, the diameter of the nozzle throat is considered as a non-stationary interval process $D _ {\mathrm{t}} ( t )$ , and the characteristic function is given by

$$\begin{array} {r l} & {D _ {\mathrm{t}} ^ {\mathrm{M}} ( t ) = ( 62.5 + k _ {\mathrm{e}} ( t - 7 ) ) {\times} 10 ^ {- 3}} \\ & {D _ {\mathrm{t}} ^ {\mathrm{R}} ( t ) {=} 3 {\times} 10 ^ {- 3}} \\ & {\rho _ {D _ {\mathrm{t}} D _ {\mathrm{t}}} ( t _ {1} , t _ {2} ) = \exp ( - | t _ {1} - t _ {2} | / 3 )} \end{array}\tag{44}$$

where $k _ {\mathrm{e}}$ is the rate of throat erosion. The areas of the nozzle throat and the burning surface of the engine are respectively denoted as $A _ {\mathrm{t}} ( t )$ and $A _ {\mathrm{b}} ( t )$ . The propellant thickness H(t), the propellant mass M(t), the volume V(t) of the combustion chamber and the pressure P(t) can be determined by

$$\begin{array} {l} {\displaystyle \frac {d H ( t )} {d t} = - a P ^ {n} ( t )} \\ {\displaystyle \frac {d V ( t )} {d t} = - A _ {\mathrm{b}} ( t ) \frac {d H ( t )} {d t}} \\ {\displaystyle \frac {d M ( t )} {d t} = - \rho \frac {d V ( t )} {d t}} \\ {\displaystyle \frac {d P ( t )} {d t} = \frac {\Gamma ^ {2} C ^ {\ast} A _ {\mathrm{t}}} {V ( t )} \left( \rho \frac {A _ {\mathrm{b}} ( t )} {A _ {\mathrm{t}}} C ^ {\ast} a P ^ {n} ( t ) - P ( t ) \right)} \end{array}\tag{45}$$

where $\rho$ represents the density of the propellant, and $C ^ {*}$ is the chamber characteristic velocity. The constant parameters $^ {a ,}$ n and Γ are respectively set as $7.9752 \times 10 ^ {- 6}$ , 0.4365 and 0.6528.

The Runge-Kutta method is used to solve the differential equation system in Eq. (45), with the initial conditions in the following

$$\begin{array} {r l} & {H ( 0 ) = H _ {0} {=} 0.06 \mathrm{~m}} \\ & {V ( 0 ) = \pi L ( R _ {\mathrm{s}} - H _ {0} ) ^ {2}} \\ & {M ( 0 ) = \rho L \pi \big ( D _ {\mathrm{s}} ^ {2} - \big ( D _ {\mathrm{s}} - 2 H _ {0} \big ) ^ {2} \big ) / 4} \\ & {P ( 0 ) {=} 2 \times 10 ^ {6} \mathrm{Pa}} \end{array}\tag{46}$$

where $R _ {s}$ is the inner radius of the shell. To avoid directly solving the above differential equation system, we construct a response surface of P (t) with variables of $t , C ^ {*} , \rho$ and $D _ {\mathrm{t}} ( t )$ , which is expressed as

$${\begin{array} {r l} & {P ( t ) = w _ {1} t ^ {2} + w _ {2} t + w _ {3}} \\ & {w _ {1} = 6.55974 \times 10 ^ {7} D _ {\mathrm{t}} ^ {2} ( t ) + 8.91389 \times 10 ^ {2} C ^ {*} D _ {\mathrm{t}} ( t ) + 7.78199 \times 10 ^ {2} \rho D _ {\mathrm{t}} ( t )} \\ & {- 1.37082 \times 10 ^ {7} D _ {\mathrm{t}} ( t ) + 4.57878 \times 10 ^ {5}} \\ & {w _ {2} = 1.11247 \times 10 ^ {8} D _ {\mathrm{t}} ^ {2} ( t ) + 3.87030 \times 10 ^ {3} C ^ {*} D _ {\mathrm{t}} ( t ) + 3.50012 \times 10 ^ {3} \rho D _ {\mathrm{t}} ( t )} \\ & {- 3.80820 \times 10 ^ {7} D _ {\mathrm{t}} ( t ) + 1.40404 \times 10 ^ {6}} \\ & {w _ {3} = 1.71633 \times 10 ^ {9} D _ {\mathrm{t}} ^ {2} ( t ) + 4.14416 \times 10 ^ {4} C ^ {*} D _ {\mathrm{t}} ( t ) + 3.69908 \times 10 ^ {4} \rho D _ {\mathrm{t}} ( t )} \\ & {- 4.71555 \times 10 ^ {8} D _ {\mathrm{t}} ( t ) + 1.7090 \times 10 ^ {7}} \end{array}}\tag{47}$$

The probabilistic characteristics of all involved variables are listed in Table 6.

In this example, the investigated time interval is [7,10] seconds. For the MCS, the time interval is discretized into 300 equidistant time instants, and $1 \times 10 ^ {7}$ samples of the stochastic variables are generated at each time instant. For efficient and accurate interval analysis, 100 samples of interval variable $P _ {a 0}$ and interval process $D _ {\mathrm{t}} ( t )$ are respectively generated. The HTRA problem is solved using the TDHTRA, where the discrete time instants are set to 300. For the HABMPPT, we select three equidistant time instants of the investigated time interval $[ 7 , 10 ]$ to obtain the initial training samples. After linearizing the lower and upper bounds of limit-state function, 300 equidistant time instants are used to estimate the time-variant failure probability.

Fig. 10 shows the curves of the time-variant failure probability obtained by each method. Table 7 displays the detailed results.

It can be seen that the failure probability curves obtained by the HABMPPT and TDHTRA-300 are both close to those obtained by the MCS. As is shown in Table 7, at 10 s, the lower and upper bounds of the failure probability estimated by the HABMPPT are $1.120 \times 10 ^ {- 4}$ and $2.962 \times 10 ^ {- 3}$ , respectively. In comparison with the MCS, the relative errors of the failure probability calculated by the HABMPPT are respectively 3.70 % and 0.71 %, and similar to the errors by calculated TDHTRA-300.

In terms of the estimation efficiency, the number of FEs needed by the $\mathbf {M C S i s 3 \times 10 ^ {11}}$ . For the TDHTRA-300, the number of BMPP searches is 600, and the number of FEs needed is 46246. However, the HABMPPT only requires 8 BMPPT searches with 944 FEs, which is much less than those required by the other two methods. In total, the results of this example demonstrate that the HABMPPT can solve the HTRA problem with high accuracy and show higher efficiency than the MCS and the HABMPPT.

## 4.4. A rocket inter-stage structure

We consider the HTRA of a rocket inter-stage structure as the last example. The inter-stage is a structural component which forms the connection between the lower and upper stages of a multi-stage launch vehicle.

The most common form of rocket inter-stage is the orthogonal stiffened cylindrical shell structure. As shown in Fig. 11(a), the inter-stage structure contains 70 axial frames and 11 ring frames. The height H and the radius R of the structure are 0.7 m and 1 m, respectively. We construct the finite element model of the inter-stage structure, which is shown in Fig. 11(b). The inter-stage structure is subjected to two types of dynamic loads: an axial load F(t) and a uniformly distributed pressure P (t). Moreover, the upper end of the inter-stage structure is under fixedsupported constraints. The material properties of the structure are listed in Table 8.

In this HTRA problem, the failure occurs, if the maximum von Mise stress $\sigma _ {\mathrm{max}}$ of the inter-stage structure exceeds the yield strength $\sigma _ {s *}$ The time-variant limit-state function can be expressed as

$$g ( t ) = \sigma _ {\mathrm{max}} ( h , w _ {\mathrm{a}} , w _ {\mathrm{r}} , T _ {\mathrm{s}} , F ( t ) , P ( t ) ) - \sigma _ {s}\tag{48}$$

where h is the height of frames; $w _ {\mathrm{a}}$ and $w _ {\mathrm{r}} {\tt a r e} ,$ respectively, the thickness of the axial and ring frames; $T _ {s}$ represents the thickness of the shell. Due to the uncertainty caused by manufacturing, h, $w _ {\mathrm{a}} , ~ w _ {\mathrm{r}} ,$ and $T _ {s}$ are

(a) The lower bound

(b) The upper bound

(a) Geometric model

(b) Finite element model

modeled as random variables. With the limited information of the yield strength, $\sigma _ {s}$ is considered as an interval variable.

During the powered ascent, the axial acceleration of the rocket increases with time, the axial dynamic load F(t) is modeled as a nonstationary Gaussian process, and the characteristic functions are given by

$$\begin{array} {r l} & {\mu _ {F} ( t ) {= 2 \times 10 ^ {6} + ( t / 120 ) ^ {1.5} \times 10 ^ {6}}} \\ & {\sigma _ {F} ( t ) {= 1 \times 10 ^ {5}}} \\ & {\rho _ {F F} ( t _ {1} , t _ {2} ) = \exp ( - | t _ {1} - t _ {2} | / 120 )} \end{array}\tag{49}$$

The dynamic pressure bear by the rocket skin increases followed by decreases and is difficult to measure precisely. Therefore, the uniformly distributed pressure P(t) is considered as a nonstationary interval process, and the midpoint, radius and autocorrelation coefficient function are, respectively, expressed as

$$\begin{array} {r l} & {P ^ {\mathrm{M}} ( t ) {= 72500} \mathrm{exp} \Big ( - \big ( \big ( t - 47.67 \big ) / 19.3 \big ) ^ {2} \Big )} \\ & {P ^ {\mathrm{R}} ( t ) {= 2500} \mathrm{exp} \Big ( - \big ( \big ( t - 47.67 \big ) / 19.3 \big ) ^ {2} \Big )} \\ & {\rho _ {P P} \big ( t _ {1} , t _ {2} \big ) {=} \mathrm{exp} ( - | t _ {1} - t _ {2} | / 6 )} \end{array}\tag{50}$$

The probabilistic characteristics of all variables of the rocket interstage structure are listed in Table 9.

The finite element model of the rocket inter-stage structure consists of $^ {57 , 529}$ shell elements. To avoid excessive performing finite element analyses, we construct a back propagation neural network (BPNN) model of $\sigma _ {\mathrm{max}}$ . In order to calculate the probability of failure, the investigated time range [0, 120] seconds is discretized into 120 uniformly distributed time instants in the MCS, and $2 \times 10 ^ {6}$ samples are generated at each time instant. 300 samples of each interval variable and interval process are respectively generated to perform interval analysis. For the proposed HABMPPT, three equidistant time instants selected from [0, 120] seconds are used to obtain the initial training samples. After linearizing the lower and upper bounds of limit-state function, 120 equidistant time instants are used to estimate the time-variant failure probability. In this HTRA problem, the average number of added LBMPPs and UBMPPs selected by active learning function are respectively 5.2 and 5.2.

(a) The lower bound

(b) The upper bound

Fig. 12 shows the curves of the time-variant failure probability obtained by the MCS and HABMPPT. Table 10 gives the detailed results of the two methods.

As shown in Fig. 12, the failure probability curves obtained by the HABMPPT and MCS are in a good fit. According to Table 10, the lower and upper bounds of the failure probability calculated by the HABMPPT are $1 . \overset - {128} \times 10 ^ {- 3}$ and $5.134 \times 10 ^ {- 3} ,$ respectively. Compared with the result of the MCS, the relative errors are respectively 2.27 % and 2.91 %.

In terms of estimation efficiency, the proposed HABMPPT method only requires 16.4 BMPP searches with 15903 FEs on average. The number of FEs needed by the MCS is $7.2 \times 10 ^ {10}$ which is much larger than the one of the HABMPPT method. In summary, the results demonstrate that the proposed HABMPPT is more efficient and shows high accuracy in HTRA problems involving interval processes.

## 5. Conclusion

In this paper, a novel HTRA method by approximating the BMPPT is proposed, which can effectively and efficiently solve the HTRA problems involving interval process variables. In the proposed method, based on time discretization, the HTRA problem can be transformed into a timeindependent series system reliability problem, which can be solved by obtaining BMPPs at all discrete time instants. To avoid directly searching BMPP at a large number of discrete time instants, we approximate the BMPPT by active learning Kriging to efficiently obtain all BMPPs. Combining the approximated BMPPT and MCS, the bounds of timevariant failure probability can be estimated. Four examples with random variables, stochastic process variables, interval variables and interval process variables are investigated, from which the following conclusions can be drawn.

(1) We propose the concept of the BMPPT. Based on the BMPPT, the bound time-variant limit-sate function of HTRA problems involving interval process variables can be linearized into two Gaussian processes, then the failure probability can be estimated efficiently.

(2) In the proposed HABMPPT, the active learning Kriging model is used to approximate the BMPPT to obtain BMPPs efficiently. Compared with the TDHTRA which directly searches BMPPs at all discrete time instants, the HABMPPT requires less than one-tenth number of FEs needed by the TDHTRA with similar accuracy in estimating the failure probability.

(3) The results of four examples show that, for the HABMPPT, the relative errors compared with MCS are typically smaller than 5 % which is acceptable for engineering problems.

This study proposes an efficient and effective method for solving HTRA problems involving interval process variables. However, the investigation of the HABMPPT in this paper is by no means exhaustive. For example, how to solve HTRA problem with correlated uncertainties, how to calculate BMPP more efficiently and accurately, and how to approximate the BMPPT dealing with unsmooth or discontinuous BMPPT, we are still a huge challenging task for the HBAMPPT method and need further study in the future.

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
