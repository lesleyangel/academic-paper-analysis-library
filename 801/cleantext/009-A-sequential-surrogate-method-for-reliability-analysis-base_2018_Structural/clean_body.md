## 1. Introduction

In engineering design, when uncertainties are involved, the failure probability $P _ {f}$ of the limit state function (LSF) g(x) should be examined. $P _ {f}$ is essentially a multi-dimensional integral formulated as

$$P _ {f} = \int \int \cdots \int _ {D} {\sf p} ( {\bf x} ) {\sf d} x _ {1} {\sf d} x _ {2} \cdot \cdot \cdot {\sf d} x _ {m}\tag{1}$$

where $D$ is the failure region defined as $D = \{\mathbf {x} | \mathbf {g} ( \mathbf {x} ) \leqslant 0 , \mathbf {x} \in \mathbb {R} ^ {m} \}$ ¼ f j ð Þ 2 gand p(x) is the joint probability function. The numerical integral and direct Monte Carlo Simulation (MCS) are difficult for a complex system with implicit time-consuming analysis models. To calculate the integral with the original LSF faces enormous computational challenges [1–2]. Therefore, different approximations of the LSF are adopted to improve the computational efficiency of reliability analysis.

The mean value method (MVM) [3–4] performs a first-order Taylor expansion of the LSF at the mean point (as shown in Fig. 1), in which the LSF is assumed to be normal distribution.

The MVM is one of the most efficient reliability methods. However, it requires the independent input variables obey normal distribution, which is difficult to be satisfied in practical problems. Moreover, the approximation error increases with the increase of the nonlinearity. Therefore, this method is appropriate for fast estimation of the structural reliability with low nonlinearity.

The first-order reliability method (FORM) [5–8] transforms random variables with different distributions into the same standard normal space U by Rosenblatt transformation [9] and then performs a first-order Taylor expansion at the most probable point (MPP) which has the maximum failure probability on the LSF (as shown in Fig. 1). Eventually, the normal distribution parameters (mean value and standard deviation) of LSF are figured out with the gradient of the approximation function, and then the failure probability is obtained analytically. Compared with the MVM, the FORM does not require the input variables to obey normal distribution and has a higher accuracy with the LSF expanded at the MPP. However, the optimization with an equality constraint to find the MPP increases the number of the LSF evaluations. Moreover, it increases the nonlinearity of the LSF g(x) during the Rosenblatt transformation, thus the approximation error is large when the nonlinearity of LSF is high [10–11].

The second-order reliability method (SORM) [7,12–13] is similar to the FORM. First, the input random variables are transformed into the standard normal space U to get the LSF G(u). Second, G(u) is expanded with second-order Taylor expansion at the MPP to obtain a quadratic hypersurface. Finally, the reliability of the approximate model is analyzed with analytical methods [10]. The SORM has a higher nonlinear adaptability than the FORM, but it needs to perform the time-consuming second-order gradients. Moreover, the adaptability to nonlinear boundary is still limited [10–11].

The response surface is a different commonly used reliability analysis method [14–16]. By sampling in the neighborhood of the design point, the local approximation model of LSF is constructed. Since the response surface model evaluation time is far less than that of the original LSF, it is possible to use the approximate model for Mont Carlo Simulation (MCS) or Importance Sampling (IS) [17–19]. However, since the accuracy of the response surface method is poor with numbered samples, the complex structural behavior might not be captured. When considering factors such as the failure boundary and probability density, more samples are required to improve the local accuracy. Therefore, iterative response surface reliability analysis methods are proposed [20–30], which increases the samples in the important region near the MPP, and gradually improves the accuracy of the approximation model. This type of iterative method is also known adaptive or active learning method [31–32,45]. In general, the response surface approximation model can be replaced by other surrogate model (also known as meto-model) techniques such as radial basis function (RBF), Kriging, support vector regression (SVR), artificial neutral net (ANN), etc. [18,33–44]. The existing methods converge in a local region after increasing the sample density of the important region in some degree, but the accuracy does not increase in the less important region.

In order to make full use of the information of the added samples to improve the approximate accuracy of the important and less important region, this paper proposes a sequential surrogate reliability method (SSRM) based on RBF. By adding points sequentially to the surrogate model, the failure features in the important region and on the boundary of the LSF are captured, and the failure probability is obtained with MCS by using the surrogate model. SSRM does not need to use the original LSF to search for MPP directly, but rather becomes close to the important area near MPP in the process of adding points, thus reducing the number of sample evaluations and avoiding the failure to find the optimal solution. Meanwhile, the SSRM method makes a trade-off between precision and computational cost.

The remainder of this paper is structured as follows. Section 2 introduces the surrogate model technology used in SSRM; Section 3 describes the implementation process of SSRM, and analyzes its characteristics; Section 4 verifies the effectiveness and efficiency of SSRM with several numerical examples; conclusions are given in Section 5.

## 2. Surrogate model

## 2.1 Construction of surrogate model

The goal of the surrogate model is to construct a prediction model of a complex or unknown model with the observation samples. Instinctually, surrogate model is an interpolation or regression model, which is also a branch of machine learning [47]. The common surrogate models include polynomial response surface method (PRSM) [48–49], radial basis function (RBF) [48–49], Kriging [50–52], support vector regression (SVR) [50–52] and artificial neutral net (ANN) [53]. Since RBF has good nonlinear adaptability and is easy to implement, this paper constructs the sequential surrogate model with RBF. Assume that the observation samples are presented as

$$S = \{( \mathbf {x} _ {i} , y _ {i} ) | i = 1 , 2 , \ldots , n \}\tag{2}$$

denoted by a matrix form

$$\begin{array} {r} {\mathbf {X} = \left[ \mathbf {x} _ {1} , \mathbf {x} _ {2} , \ldots , \mathbf {x} _ {n} \right] ^ {\mathrm{T}}} \\ {\mathbf {y} = \left[ y _ {1} , y _ {2} , \ldots , y _ {n} \right] ^ {\mathrm{T}}} \end{array}\tag{3}$$

where n is the sample size, X denotes the input sample matrix, y is the output sample vector. x is an m-dimensional design variable. RBF uses a series of linear combinations of radial basis functions to approximate the expensive limit state function, which can be formulated as

$${\widehat {\mathbf {y}}} ( \mathbf {x} ) = \sum _ {i = 1} ^ {n} \beta _ {i} \mathbf {f} ( \| \mathbf {x} - \mathbf {x} _ {i} \| ) = \mathbf {f} ( \mathbf {x} ) ^ {\mathrm{T}} \mathbf {\beta}\tag{4}$$

where $\hat {\mathbf {y}} ( \mathbf {x} )$ denotes the predictive response at point $\mathbf {x} , \beta _ {i}$ is the ith ð Þcomponent of the radial base coefficient vector b, and $\mathbf {f} ( \lVert \mathbf {x} - \mathbf {x} _ {i} \rVert )$ ðk  kÞ(see Table 1) is the ith component of the radial basis function vector f x . As shown in Table 1, $r = \| \mathbf {x} - \mathbf {x} _ {i} \|$ is the Euclidian distance ð Þ ¼ k  kbetween two samples, and c is the shape parameter.

Substitute the samples of Eq. (2) into Eq. (4),

$$\left[ \begin{array} {c} {y _ {1}} \\ {y _ {2}} \\ {\vdots} \\ {y _ {n}} \end{array} \right] = \left[ \begin{array} {c c c c} {\mathbf {f} ( r _ {11} )} & {\mathbf {f} ( r _ {12} )} & {\ldots} & {\mathbf {f} ( r _ {1 n} )} \\ {\mathbf {f} ( r _ {21} )} & {\mathbf {f} ( r _ {22} )} & {\ldots} & {\mathbf {f} ( r _ {2 n} )} \\ {\vdots} & {\vdots} & {\ddots} & {\vdots} \\ {\mathbf {f} ( r _ {n 1} )} & {\mathbf {f} ( r _ {n 2} )} & {\ldots} & {\mathbf {f} ( r _ {n n} )} \end{array} \right] \left[ \begin{array} {c} {\beta _ {1}} \\ {\beta _ {2}} \\ {\vdots} \\ {\beta _ {n}} \end{array} \right]\tag{5}$$

Rewritten as a matrix form

$$\mathbf {y} = \mathbf {F} \mathbf {\beta}\tag{6}$$

As the samples are different with each other, $\mathbf {F} \in \mathbb {R} ^ {n \times n}$ is a nonsingular matrix, and Eq. (6) has a unique solution $\mathbf {\beta} \mathbf {=} \mathbf {F} ^ {- 1} \mathbf {y}$ . Thus the prediction model is given by

$${\widehat {\mathbf {y}}} ( \mathbf {x} ) = \mathbf {f} ( \mathbf {x} ) ^ {\mathrm{T}} \mathbf {F} ^ {- 1} \mathbf {y}\tag{7}$$

where f(x) is related to the prediction point x and sample input matrix $\mathbf {x} ; \mathbf {F} ^ {- 1} \mathbf {y}$ is only related to X and y. For a new prediction sample x, f(x) is calculated one time to get its predicted valuey^ x .

It should be pointed out that the shape parameter c, which has a great influence on the accuracy of the model, is included in F and is determined by experience or other optimization criteria. This paper uses the cross-validation criteria to optimize the shape parameter c.

## 2.2. Validation of surrogate model

A common method to estimate the accuracy of the surrogate model is the root mean square errors (RMSE). However, since RBF requires the model strictly goes through sample points, RMSE is a constant zero, leads to the failure of the model estimation. To avoid the problem, the cross-validation method is adopted. The samples are divided into K roughly equal-sized parts. For the kth part $( k = 1 , 2 , \cdots , K ) ,$ , the model is fitted with the other K 1 parts --- of the samples, and calculates the prediction error of the fitted model when predicting the kth part of the samples [47]. Crossvalidation can fully reflect the matching degree of the samples and the model. In particular, when K is equal to the sample size n, it is called leave-one-out cross-validation error (LOOCV) [47]. Thus, the RBF shape parameter c can be estimated by the following sub-optimization problem:

$$m i n \sum _ {c} ^ {n} [ y _ {i} - \widehat {\mathbf {y}} ( \mathbf {x} _ {i} ; S - \{( \mathbf {x} _ {i} , y _ {i} ) \} ) ] ^ {2}\tag{8}$$

In Eq. (8), it can be seen that the evaluation of LOOCV error requires n times construction of the surrogate model. However, the LOOCV error does not require additional verification points, which is capable of describing the matching degree between the samples and the prediction model. According to the surrogate model and obtained parameter c, a reliability analysis method based on the sequential surrogate model can be constructed.

## 3 Sequential surrogate reliability method

This section presents the detailed procedure of the proposed sequential surrogate reliability method (SSRM). SSRM uses the sequential surrogate model of LSF to add samples to refine the surrogate model, which is also named active learning method in the community of machine learning. To get more meaningful failure information of LSF, the added samples are selected in the neighborhood of the most probable point (MPP) and on the LSF hypersurface. However, when the added sampled is too close to the existing samples, the added information is small. Therefore, a constraint of minimum distance is required. With the criteria of adding samples, SSRM reduces the samples in the unimportant region with small failure probability. In the iterative process, the failure boundary of the LSF is approached step by step, and eventually a surrogate model of LSF which captures most failure information is obtained.

In order to facilitate the description of the algorithm, the independent random variables in original design space X are transformed into standard normal space U with Rosenblatt transformation [9], which are formulated as

$$u _ {i} = \mathrm{F} _ {U _ {i}} ^ {- 1} \mathrm{F} _ {X _ {i}} ( x _ {i} ) , ( i = 1 , 2 , \cdot \cdot \cdot , m )\tag{9}$$

where $X _ {i}$ is the ith random variable in the original space, $U _ {i}$ is the ith standard normal random variables, x and u are the values of the random variables, $\mathrm{F} _ {X _ {i}} ( \cdot )$ and $\mathsf{F} _ {U _ {i}} ( \cdot )$ are cumulative distribution functions (CDF) of $X _ {i}$ ðand $U _ {i} ,$ ð-Þ and m is the dimension of the variables. Therefore, the LSF in a vector form is formulated as

$$\mathbf {g} ( \mathbf {x} ) = \mathbf {g} [ \mathbf {F} _ {\mathbf {X}} ^ {- 1} \mathbf {F} _ {\mathbf {U}} ( \mathbf {u} ) ] = \mathbf {G} ( \mathbf {u} )\tag{10}$$

where $\mathbf {g} ( \mathbf {x} )$ is the LSF in the X space and ${\cal G} ( {\bf u} )$ is the LSF in the U space.

The following algorithm is implemented in the U space. The key step of SSRM is an iteration process with special initial and terminal conditions, which can be briefly described as follows

$$\left\{\begin{array} {l} {{\displaystyle \Delta u _ {k} = \mathrm{argmin} \ | {\bf u} | \ | \ {\bf s} . \mathrm{t} . \left\{\begin{array} {c} {{\hat {\bf G}} \displaystyle ( {\bf u} ; S _ {k - 1} ) = 0} \\ {\displaystyle ( {\bf u} ; S _ {k - 1} ) \geqslant {\bf d} _ {\mathrm{min}} ( S _ {k - 1} )} \\ {{\bf u} _ {\mathrm{L}} \leqslant {\bf u} \leqslant {\bf u} _ {\mathrm{U}} , {\bf u} \in {\bf R} ^ {m}} \end{array} \right.}} \\ {{\displaystyle \qquad \} \ \Delta S _ {k} = \left\{( \Delta {\bf u} _ {k} , {\bf g} ( \Delta {\bf u} _ {k} ) ) \right\}} \\ {{\displaystyle \qquad S _ {k} = S _ {k - 1} \ \sqcup \Delta S _ {k}}} \\ {\displaystyle P _ {k} = \mathrm {P _ {M C S}} \{{\hat {\bf G}} ( {\bf u} ; S _ {k} ) \leqslant 0 \} , k = 1 , 2 , 3 , \ldots} \\ {\displaystyle \ \mathrm{Start} : S _ {0} , P _ {0} = \mathrm {P _ {M C S}} \{{\hat {\bf G}} ( {\bf u} ; S _ {0} ) \leqslant 0 \}} \\ {{\displaystyle \mathrm{Stop} : k \geqslant k _ {\mathrm{max}} \ \mathrm{or} \ ( | P _ {k} - P _ {k - 1} | \leqslant \varepsilon _ {a} \ \& {\delta} \stackrel {| P _ {k} - P _ {k - 1} |} {P _ {k}} \leqslant \varepsilon _ {r} )}} \end{array} \right.\tag{11}$$

where $\Delta {\bf u} _ {k}$ is the sample added in the kth iteration, u denotes the Euclidean distance between u and the coordinate origin O. Since the joint probability density function (PDF) of the standard random variables is given by

$$\mathbf {p} ( \mathbf {u} ) = \prod _ {i = 1} ^ {m} {\frac {1} {\sqrt {2}}} \exp \left( - {\frac {u _ {i} ^ {2}} {2}} \right) = 2 ^ {- m / 2} \exp \left( - {\frac {\left\| \mathbf {u} \right\| ^ {2}} {2}} \right) .\tag{12}$$

when u gets the minimum value, $\mathfrak {p} ( \mathfrak {u} )$ has the maximum failure probability (see Fig. 2). $S _ {k}$ is the sample set in the kth iteration, $\hat {\bf G} ( {\bf u} ; S _ {k} )$ represents the surrogate model of LSF based on $S _ {k} ,$ ui is ð Þthe ith input variable of the sample set $S _ {k - 1}$ which totally has a number of $| S _ {k - 1} |$ samples. d u; $\pmb {S} _ {k - 1} )$ is the minimum distance j  j ð  Þbetween the currently sample and the existing samples, and ${\bf d} _ {\mathrm{min}} ( {\pmb S} _ {{\pmb k} - 1} )$ is the target minimum distance (for more details see Step 4). $\mathbf {u} _ {\mathrm{L}}$  Þand $\mathbf {u} _ {\mathrm{U}}$ are the lower and upper bounds of variables, m is the dimension of LSF, $P _ {k}$ is the failure probability in the kth iteration, S0 is the initial sample set constructed with Latin hypercube sampling (LHS) [46], $P _ {0}$ is the failure probability based on the Monte Carlo simulation (MCS) with the initial surrogate model of LSF, $k _ {\mathrm{max}}$ is the maximum number of samples allowed to add, $\varepsilon _ {\mathrm{a}}$ and $\varepsilon _ {\mathrm{r}}$ denote absolute and relative errors, respectively.

The procedure of SSRM is shown in Fig. 3, and more detailed steps of the algorithm are summarized as follows:

Step 1: Selecting the initial sample points by LHS and calculating the responses of LSF to obtain the initial sample set $S _ {0}$ . Since the interval probability $\mathsf{P} \{- 5 \leqslant U _ {i} \leqslant 5 \}$ 0:99999943 of each dimenf g sion contains most information, here we set the lower and upper bounds of LHS to be 5 and 5 respectively. For the problem with small standard deviation, the initial sample number can be taken as $| S _ {0} | = m + 1$ , while for the large standard deviation and highj j ¼ þnonlinear problems, the initial sample number can be set as $| S _ {0} | = 2 m + 1$ , where m is the dimension of random variables.

j ¼ þStep 2: Using the initial samples to construct the initial surrogate model of LSF, $\hat {\mathbf {G}} ( \mathbf {u} ; S _ {0} )$ , and optimizing the model shape parameter c. Here the surrogate model uses RBF which strictly goes through the sample points and has strong nonlinear adaptability (see Sections 2.1 and 2.2) and is built with the authors’ in-house MATLAB toolbox.

Step 3: Using the initial surrogate model $\hat {\mathbf {G}} ( \mathbf {u} ; S _ {0} )$ for reliability ð Þanalysis with MCS. In order to eliminate the errors induced by different random samples, the MCS reliability analysis uses the same random samples which can be reproduced with the same random seed. Therefore, the initial failure probability $P _ {0} = \mathrm{P} _ {\mathrm{MCS}} \{\hat {\mathrm{G}} ( \mathbf {u} ; S _ {0} ) \leqslant 0 \}$ is presented as

$$\mathrm{P} _ {\mathrm{MCS}} \{\widehat {\mathsf{G}} ( \mathbf {u} ; S _ {0} ) \leqslant 0 \} \approx \frac {1} {N} \sum _ {j = 1} ^ {N} \mathrm{I} ( \widehat {\mathbf {G}} ( \mathbf {u} _ {j} ; S _ {0} ) )\tag{13}$$

and the coefficient of variation (COV) for MCS is given by

$$\mathrm{COV} ( P _ {\mathrm{MCS}} ) = \sqrt {\frac {1 - P _ {\mathrm{MCS}}} {P _ {\mathrm{MCS}} N}}\tag{14}$$

where uj is an m-dimensional sample generated by the standard normal distribution, N is the total number of samples for MCS, and I is the indicator function, defined as

$$\operatorname{I} ( x ) = {\left\{\begin{array} {l l} {1 , i f x \leqslant 0} \\ {0 , i f x > 0} \end{array} \right.}\tag{15}$$

Step 4: Solving the optimization problem in Eq. (11) to search for the new sample. As the optimization problem has an inequality constraint of minimum distance which is not differentiable, gradient-based optimization algorithm, such as sequential quadratic programing (SQP), cannot be utilized here. Therefore, the genetic algorithm (GA) which is not restricted by the differentiability is adopted here, and it is complemented with the MATLAB optimization toolbox. In addition, the minimum distance between the current sample u and the existing samples ui is given by

$$\mathrm{d} ( \mathbf {u} ; S _ {k - 1} ) = \operatorname* {m i n} _ {\mathbf {u} _ {i}} \left\{\| \mathbf {u} - \mathbf {u} _ {i} \| | ( \mathbf {u} _ {i} , \mathbf {g} ( \mathbf {u} _ {i} ) ) \in \mathsf{S} _ {k - 1} \right\}\tag{16}$$

To give a reasonable value of the target minimum distance, the number of samples, the dimension of LSF and the interval width of the variables in each dimension should be taken into account. Such a target value can be defined as

$$\mathsf{d} _ {\operatorname* {m i n}} ( S _ {k - 1} ) = \lambda \underset {\mathbf {u} _ {i}} {\operatorname* {m a x}} \underset {\mathbf {u} _ {j}} {\operatorname* {m i n}} \{\| \mathbf {u} _ {i} - \mathbf {u} _ {j} \| | ( \mathbf {u} _ {i} , \mathbf {g} ( \mathbf {u} _ {i} ) ) , ( \mathbf {u} _ {j} , \mathbf {g} ( \mathbf {u} _ {j} ) ) \in S _ {k - 1} , i \neq j \}\tag{17}$$

where k is a scale factor in the range 0.1 to 0.5 (this paper takes $\lambda = 0.2 )$ , which balances the local and global search. Moreover, ¼the optimization problem contains an equality constraint. Therefore, the total constraints are very strong, which makes GA inefficient and difficult to converge in the high-dimensional problem. According to the idea of penalty function method, the optimization problem with strong constraints in Eq. (11) can be transformed into an approximate unconstrained optimization problem:

$$\Delta {\mathbf {u}} _ {k} = \underset {\mathbf {u}} {\mathrm{argmin}} \ \frac {( 1 + \lVert \mathbf {u} \rVert ) | \hat {\mathbf {G}} ( \mathbf {u} ; S _ {k - 1} ) |} {\left[ \frac {\mathrm{d} ( \mathbf {u} ; S _ {k - 1} )} {1 + \exp ( - 20 ( \mathrm{d} ( \mathbf {u} ; S _ {k - 1} ) - \mathrm{d} _ {\operatorname* {m i n}} ( S _ {k - 1} ) ) )} \right]}\tag{18}$$

where the symbols are the same as Eq. (11). If $\hat {\bf G} ( {\bf u} ; S _ {k - 1} ) = 0 ,$ , the ð  Þ ¼objective function gets the minimum value. However, if $\hat {\mathbf {G}} ( \mathbf {u} ; S _ {k - 1} ) \approx 0 ,$ the objective function value decreases with u. When ð  Þ u is too close to existing samples, say d u; $S _ {k - 1} ) < \mathsf{d} _ {\operatorname* {m i n}} ( S _ {k - 1} )$ , the ð  Þ ð  Þobjective function increase rapidly, which ensures the original inequality constraint to work. As an unconstrained optimization problem, the transformed problem is easier to solve for the highdimensional problems. However, the process of searching for new samples is not as accurate as the original optimization problem, which decreases the global accuracy of the surrogate model.

Step 5: Estimating the sample found in Step 4 with practical LSF G u to obtain the sample set $\Delta S _ {k} = \{( \Delta \mathbf {u} _ {k} , \mathbf {G} ( \Delta \mathbf {u} _ {k} ) ) \}$ and then ð Þupdating the sample set $\mathsf{S} _ {k} = S _ {k - 1} \cup \Delta S _ {k}$

Step 6: Updating the surrogate model of LSF $\hat {\bf G} ( {\bf u} ; S _ {k} )$ and optimizing the shape parameter c.

Step 7: Estimating the failure reliability with the updated surrogate model with MCS, which can be presented as $P _ {k} = \mathrm{P} _ {\mathrm{MCS}} \{\hat {\mathrm{G}} ( \mathbf {u} ; S _ {k} ) \leqslant 0 \}$ and calculated with Eq. (13). Here the ¼ f ð Þ gsamples used in MCS are the same as Step 3.

Step 8: Convergence check. If one of the termination conditions, (a) the maximum iteration condition $\iota \geqslant k _ {\mathrm{max}} , ( \mathbf {b} )$ the relative convergence condition $| P _ {k} - P _ {k - 1} | / P _ {k} \leqslant \varepsilon _ {r} ( = 1 \times 10 ^ {- 4} )$ and the absolute convergence condition $| P _ {k} - P _ {k - 1} | \leqslant \varepsilon _ {a} ( = 1 \times 10 ^ {- 3} )$ , is satisfied, go jto Step 9, otherwise set $k = k + 1$ j ð¼  Þ and then go to Step 4.

Step 9: End of SSRM.

The main procedures of SSRM are the construction of surrogate model and the criterion to add points, which are also the core to guarantee the accuracy and efficiency in the iteration process. SSRM automatically increases the samples in the important region with large failure probability, which makes full use of the information of PDF and each sample. In addition, since the minimum distance constraint of the samples works, SSRM increases the number of the samples in the less important region when the important region includes enough points. Therefore, SSRM does not require many initial samples. After each surrogate model update, MCS reliability analysis is performed to achieve the estimation of failure probability. Since most of the failure features near the MPP and the LSF boundary are captured by the surrogate model iteratively, the MCS based estimation has a good accuracy. Moreover, if the time of a single evaluation of the surrogate model is far less than that of the original LSF, the cost of model parameter optimization, MCS and GA based on the surrogate model is acceptable. Therefore, SSRM shows its superiority of accuracy and efficiency, when LSF is defined by time-consuming model, such as expensive finite element analyses.

## 4. Numerical examples

In this section, seven examples are used to perform SSRM, and the results are compared with those of MCS and some other existing methods. Example 1–3 are of different nonlinearity, example 4 is the LSF of a speed reducer shaft with variables under different distributions, example 5 is a cantilever tube structure with highdimensional variable space, example 6 is a nonlinear oscillator with six random variables, and example 7 demonstrates the sensitivity of SSRM in high-dimensional problems. Assuming the transformed random variables in U space to be u $\in [ - 5 , 5 ] , i = 1 , 2 , \cdots , m ,$ the initial samples are selected by LHS, 2 ½  ¼ - - -and the sample size is m + 1 or 2m + 1, where m is the number of the random variables. In these examples, FORM and SORM are realized by Isight5.6, a software for multidisciplinary design optimization (MDO), while SSRM and MCS are implemented with the authors’ in-house Matlab codes. In order to quantify the error, results of MCS are taken as the references, and random seeds are selected to obtain the same samples for MCS in each example.

## 4.1. Circular pipe structure

Considering a circular pipe with circumferential through-wall crack subjected to a bending moment, the LSF is given by [4]:

$${\bf g} ( {\bf X} ) = 4 t \sigma _ {f} R ^ {2} \left( \cos \left( {\frac {\theta} {2}} \right) - {\frac {1} {2}} \sin ( \theta ) \right) - M\tag{19}$$

where $\sigma _ {f} , \theta ,$ M, R and t are flow stress, half-crack angle, applied bending moment, radius of the pipe and thickness of the pipe, respectively. $R = 0.3377$ m, t = 0.03377 m, $M = 3 ~ \times ~ 10 ^ {6}$ Nm. $\sigma _ {f}$ and h are random variables. The statistical properties of the random variables involved in the problem are illustrated in Table 2.

As shown in Fig. 4, three initial samples are selected and four extra samples are added iteratively. The approximate LSFs of FORM, SORM and SSRM are close to each other in the neighborhood of the MPP due to the low nonlinearity. In the region far away from the MPP, the approximate LSF of FORM has a poor accuracy, while SORM and SSRM have better accuracies with the approximate LSFs closer to the original LSF. As shown in Table 3, SSRM has the best accuracy with a relative error of 0.0175%. As the initial sample size is small, the initial surrogate $\mathrm{LSF} \hat {\mathbf {G}} _ {\mathrm{SSRM}} ( \mathbf {u} )$ in Fig. $4 ( \mathsf{a} )$ is ð Þfar away from the original LSF, however, after 4 iterations, they are almost the same (See Table 4).

## 4.2. Hyper-sphere bound problem

This example considers a hyper-sphere bound with higher nonlinearity, and the LSF is given by

$$\begin{array} {r} {\mathbf {g} ( \mathbf {X} ) = 1 - X _ {1} ^ {3} - X _ {2} ^ {3}} \end{array}\tag{20}$$

As shown in Fig. 5, three initial samples are selected and nine extra samples are added iteratively. As expected, Table 5 illustrates that SSRM obtains more accurate result with fewer samples. Since the approximation of the LSF can be improved step by step in the process of adding points, the accuracy is significantly improved. FORM and SORM cannot capture most of the failure features of the important region due to the high nonlinearity, however SSRM updates the surrogate of LSF, thus a good approximation in the important region and its neighborhood are obtained. As shown in Fig. $5 \left( \mathsf{a} \right)$ , the initial surrogate model is not accurate, and the added points are far away from the original LSF at first, however, as the iteration goes on, the added points get closer to the LSF. Thus, each point makes contributions to the improvement of the accuracy of the LSF boundary, especially in the important region. Meanwhile, the region far away from the MPP and the LSF boundary has a few samples and the probability is very small, hence the region has little effect on the estimation. That is the reason why SSRM improves the accuracy with fewer samples.

## 4.3. Cantilever beam

This is also an example with higher nonlinearity, a cantilever beam with rectangular cross section subjected to uniformly distributed loading [20,53]. The LSF with respect to the maximum deflection at the free end being greater than l/325, is given by

$${\bf g} = {\frac {l} {325}} - {\frac {w b l ^ {4}} {8 E I}}\tag{21}$$

where $I = b h ^ {3} / 12 ,$ where w, b, l, E, I and h are load per unit, width, span, modulus of elasticity, moment of inertia of the cross section and depth, respectively. The random variables are w and h, as shown in Table 6. Assuming E and l are $2.6 \times 10 ^ {4}$ MPa and 6 m respectively, the LSF is reduced to

$$\mathbf {g} ( \mathbf {X} ) = 18.46154-74769.23 {\frac {X _ {1}} {X _ {2} ^ {3}}}\tag{22}$$

As shown in Fig. 6, five initial samples are selected and 13 extra samples are added iteratively. Table 7 and Fig. 6 show that SSRM obtains a good accuracy with $P _ {f} {=} 0.009499$ and 18 LSF evaluations. Meanwhile, Fig. 6(a) shows that the added samples are all near the LSF boundary, and keeps minimum distance to each other. It means that all the samples contribute a lot to obtain the failure probability with a good approximation to the LSF boundary. Moreover, it can be observed that the accuracy in the region near $\bf {u} = ( - 4 , \frac {} {}$ 4) is relatively poor. However, since the region is far from the mean point $\mathbf {u} = ( 0 , 0 )$ , the probability is very small, which means that the poor accuracy does not affect the estimation of the failure probability (See Table 8).

## 4.4. Speed reducer shaft

In this section, considering the LSF of the reducer axis of multivariate random variables with different distributions [9]

$$g ( X ) = S - 32 / ( \pi D ^ {3} ) \sqrt {F ^ {2} L ^ {2} / 16 + T ^ {2}}\tag{23}$$

In this example, 6 initial samples are selected and 38 extra samples are added iteratively. Fig. 7 shows that the initial value of $P _ {f}$ is far from the MCS result, due to the small number of samples. However, with the increase of the samples during the iteration, the capture ability of the SSRM for the failure boundary is increased. Hence, $P _ {f}$ converges in a few iterations. As expected, the results in Table 9 show that SSRM has a good adaptability and accuracy for this multidimensional problem (See Fig. 8).

(a) Initial iteration.

(b) Iteration #1.

(c) Iteration #2.

(d) Iteration #3.

(e) Iteration #4.

(f) Iterative process of $P _ {f}$

## 4.5. Cantilever tube problem

To further demonstrate the performance of SSRM in the case of different distributions in high dimensions, consider the following cantilever tube problem, the LSF is defined as follows [6]: (See Table 10).

$$g ( X ) = S _ {y} - \sqrt {\sigma _ {x} ^ {2} + 3 \tau _ {z x} ^ {2}}\tag{24}$$

## where

(a) Initial iteration.

(b) Iteration #1. 
Comparison of different reliability methods for the hyper-sphere problem.

(e) Iteration #4. 
(f) Iteration #5. 
Distributions of random variables for the cantilever beam.

25

$$\tau _ {z x} = T d / ( 2 J )$$

$$J = 2 I$$

$$I = ( \pi / 64 ) [ d ^ {4} - ( d - 2 t ) ^ {4} ]$$

$$M = F _ {1} L _ {1} \cos ( \theta _ {1} ) + F _ {2} L _ {2} \cos ( \theta _ {2} )$$

$$A = ( \pi / 4 ) [ d ^ {2} - ( d - 2 t ) ^ {2} ]$$

$$h = d / 2$$

$$\sigma _ {x} = ( P + F _ {1} \sin ( \theta _ {1} ) + F _ {2} \sin ( \theta _ {1} ) ) / A + M h / I$$

(c) Iteration #2.

(d) Iteration #3.

(g) Iteration #6.

(h) Iteration #7.

(i) Iteration #8.

(i) Iteration #9.

(k) Iterative process of Pf.

(a) Samples and LSF in U-space.

(b) Iterative process of $P _ {f}$

a Directional Sampling. 
b Response Surface. 
c Splines. 
d Neural networks. 
e Important Sampling. These results are from Schueremans [53].

a The distribution parameters are mean and standard deviation respectively. 
b The distribution parameters are lower and upper bound respectively.

Constants $\theta _ {1} = 5 ^ {^{\circ}} , \theta _ {2} = 10 ^ {^{\circ}}$

¼ ¼In this example, 10 initial samples are selected and 8 extra samples are added iteratively. As a nine-dimensional problem, the computational cost for FORM and SORM to solve the MPP increases dramatically but not improve the accuracy effectively, while SSRM converges to the MCS result with 8 iterations (see Fig. 9). Though the dimension of the variables is high, the uniform distribution interval and the coefficient of variation are small, thus the nonlinearity near the design point is not very high. Therefore, the failure features can be captured by SSRM with a few samples; accordingly, a good estimation of the failure probability (see Table 11) is achieved (See Fig. 10).

## 4.6. Dynamic response of a nonlinear oscillator

This example consists of a nonlinear undamped single degree of freedom system with six random variables [20,34,53]. The LSF is given by

$$\mathbf {g} ( c _ {1} , c _ {2} , m , r , t _ {1} , F _ {1} ) = 3 r - | \frac {2 F _ {1}} {m \omega _ {0} ^ {2}} \sin ( \frac {\omega _ {0} t _ {1}} {2} ) |\tag{26}$$

where $\omega _ {0} = \sqrt {( c _ {1} + c _ {2} ) / m}$ The random variables are given in Table 12.

In this problem, 13 initial samples are selected and 6 extra samples are added as shown in Fig. 11. As expected, the $P _ {f}$ of SSRM in Table 13 is also close to that of MCS with a relative error of 1.623%. Since the result of MCS is also with a coefficient of variation of 2.2%, the relative error of SSRM is acceptable. However, the total LSF evaluations of SSRM are 19, which is smaller than the existing methods (See Fig. 12).

## 4.7. High-dimensional problem

This example which is from Bourinet [54] aims to evaluate the performance of SSRM to deal with high-dimensional problems. Failure probabilities with different numbers of random variables are discussed. The LSF is formulated as (See Table 14).

$$\mathbf {g} ( \mathbf {X} ) = m + 3 \sigma \sqrt {m} - \sum _ {i = 1} ^ {m} X _ {i}\tag{27}$$

where m is the number of random variables, $X _ {i} ( i = 1 , 2 , \cdots , m )$ are ð ¼ - - - Þindependent random variables which follow the lognormal distribution with mean value $\mu = 1$ and standard deviation $\sigma = 0.2$ . The transformed LSF in U space is presented as

a Directional Sampling. 
b Response Surface. 
c Splines. 
d Neural networks. 
e Important Sampling. These results are from Schueremans et. al. (2005) [53]. 
f Active Learning. 
g Learning Function U. 
h Expected Feasibility Function. These results are from Echard et al. (2011) [34].

Iteration process of SSRM for the nonlinear oscillator.

$$\operatorname{g} ( \mathbf {U} ) = m + 3 \sigma {\sqrt {m}} - \sum _ {i = 1} ^ {m} \exp \left( \ln {\frac {\mu ^ {2}} {\sqrt {\mu ^ {2} + \sigma ^ {2}}}} + U _ {i} {\sqrt {\ln \left( {\frac {\sigma ^ {2}} {\mu ^ {2}}} + 1 \right)}} \right)\tag{28}$$

In this example, three cases (m = 40, 100 and 250) are discussed. The results are shown in Table 15, where results of FORM, SORM, 2 SMART and MCS are from reference [54]. As shown in Table 15, for m = 40, 81 initial samples are selected and 117 extra samples are added iteratively; for m = 100, 201 initial samples are selected and 147 extra samples are added iteratively; for $m = 250 , 501$ initial samples are selected and 233 extra samples are added iteratively. Fig. 11 shows the iterative processes of different cases. As expected, the number of added samples increases with the dimension of LSF. Moreover, when the dimension is high, it is difficult to find the accurate most probable point, and the accuracy of Taylor approximation is poor, therefore FORM and SORM have more errors. The accuracy of SSRM is slightly lower than 2 SMART, but the number of LSF evaluations is just about 5.3% to 6.9% of 2 SMART. Thus, SSRM balances the accuracy and the number of sample points.

a Subset simulation by Support-vector Margin Algorithm for Reliability Estimation [54].

## 5. Conclusions

In this paper, an efficient method for reliability analysis named SSRM is proposed. This method searches for new sample points, which involve the information about the joint probability density function and the limit state function, to refine the surrogate model of LSF iteratively. The sequential surrogate model captures more meaningful failure features in the important region, while reduces the samples in the region with low failure probability. In each iteration, MCS is used to evaluate the failure probability. Thus, a sequence of approximate failure probabilities is obtained. Several examples including numerical and engineering cases demonstrate that SSRM has a good adaptability to the LSFs with different nonlinearity and dimensions. For low-dimensional problems, SSRM has a significant advantage over existing methods in terms of accuracy and efficiency; for high-dimensional problems, SSRM has comparable precision to existing methods and higher efficiency. However, as the parameter optimization of the surrogate model, MCS, and GA take a number of surrogate evaluations, SSRM shows its superiority only when the LSFs are time-consuming implicit functions (e.g. finite element analysis). In the future study, the information of the computationally cheap low-fidelity model can be involved to construct a variable-fidelity surrogate model, so that the number of time-consuming high-fidelity sample points is expected to be further reduced.

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
