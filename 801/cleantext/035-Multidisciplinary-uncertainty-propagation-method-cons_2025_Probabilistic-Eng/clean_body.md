## 1. Introduction

Rockets, as critical spacecraft transportation systems, are exposed to random uncertainties throughout their lifecycle due to complex design, fabrication processes, and flight environments [1]. To improve performance and ensure reliability, accounting for these uncertainties at every design stage is essential [2,3]. Uncertainty-based multidisciplinary design optimization (UMDO) has emerged as a promising framework to systematically incorporate uncertainty into the design process [4–6]. By explicitly considering the interactions and synergies among different disciplines, UMDO not only enhances overall system performance but also reduces development costs and shortens the design cycle [7–9]. Within the UMDO process, however, the accuracy of multidisciplinary UP is crucial, as it directly affects the reliability of design outcomes.

Given the complexity and inherently multidisciplinary nature of rocket systems, decoupling the system during UP is often necessary. This enables independent analysis within each discipline and aligns with practical engineering design practices. In such cases, statistical moments are typically employed to describe the uncertainties of coupled state variables across disciplines. However, decoupling introduces a major limitation: correlations among state variables are usually neglected, leading to reduced accuracy in the independent UP process. For instance, the correlation between y1 and y2 is usually neglected when performing UP of system 3, as illustrated in Fig. 1. These correlations must be properly considered to ensure accurate results of UP.

Variables in UP can be broadly divided into two types: numerical variables and field variables.

A numerical variable, such as engine-specific impulse, is represented by a single scalar value whose variation is usually confined within a defined range. In contrast, a field variable is expressed as a vector distributed over a spatial or temporal domain (e.g., temperature field [10] or wind field [11]), with values that vary continuously across space or time. Compared to numerical variables, quantifying correlations among field variables poses a substantially greater challenge.

To address the challenge of incorporating correlations in UP, researchers have carried out extensive investigations [12–14]. For example, Yu integrated correlations between random variables such as wind speed and load demand into the unit commitment problem, improving UP accuracy [15]. Liu proposed an inverse uncertainty reconstruction method that considers correlations among friction coefficients, impact locations, and related factors, thereby enabling more stable and effective reconstruction of vehicle–vehicle collisions [16]. However, these studies primarily focus on correlations among input random variables within single-discipline UP, leaving multidisciplinary correlations largely unaddressed.

Research on incorporating correlations among input variables in multidisciplinary systems remains limited. Ghosh proposed a probabilistic analysis method based on a distributed multidisciplinary architecture to quantify the joint probability distribution of coupled variables during UP [17]. However, this approach is constrained when applied to correlated field variables.

Rocket systems often involve correlations among both numerical and field variables, which pose significant challenges for multidisciplinary UP. However, existing studies have not yet addressed multidisciplinary UP with correlated field variables. To overcome this gap, we propose a multidisciplinary UP method that explicitly incorporates correlated field random variables. By integrating a warm-start-based maximum entropy approach into the Nataf transformation, the method enables efficient and accurate handling of field variables. Furthermore, by introducing the reference, both numerical and field variables can be transformed simultaneously.

The main contributions of this work are summarized as follows.

1) The proposed method uniquely enables consideration of correlations among field variables within multidisciplinary UP—a capability not available in existing approaches—which significantly improves UP accuracy.

2) To address the computational challenges of calculating the probability density function (PDF) of field variables within the Nataf transformation, we introduce a warm-start strategy integrated with the maximum entropy method. This strategy accelerates the PDF optimization process by providing a superior initial guess.

The remainder of this paper is organized as follows: Section 2

presents the proposed multidisciplinary UP method for rocket systems. Section 3 validates the method using an analytical case. Section 4 applies the multidisciplinary UP method to a solid rocket system. Finally, conclusions are drawn in Section 5.

## 2. Multidisciplinary uncertainty propagation method considering correlated field variables for the rocket system

## 2.1. Multidisciplinary uncertainty propagation process considering correlated field variables

Taking the UP of a specific discipline in the rocket system as an example, we introduce the proposed multidisciplinary UP method. The overall process is illustrated in the flowchart in Fig. 2, with the detailed steps described as follows.

Step 1: Processing of propagated data from the disciplines in the upper level

After conducting uncertainty analysis of the disciplines in the upperlevel, the output samples $\pmb {X} ^ {\mathrm{C}} = \left\lceil \pmb {x} _ {1} ^ {\mathrm{C}} , \cdots , \pmb {x} _ {n} ^ {\mathrm{C}} , \cdots , \pmb {x} _ {n + f} ^ {\mathrm{C}} \right\rceil$ , where the superscript C indicates correlation among samples, are processed to obtain the statistical moment $\pmb {\mu} _ {\mathrm{previous}} ,$ the correlation coefficient matrix $\cdot \rho ,$ and the mode matrix $\varphi$ . The procedure is shown in Fig. 3, and the specific operations are as follows:

a) The output samples $\pmb {X} ^ {\mathrm{C}}$ include both numerical samples $\pmb {S} _ {\mathrm{N}} ^ {\mathrm{C}} = \left[ \pmb {x} _ {1} ^ {\mathrm{C}} , \cdots \right$ $, x _ {n} ^ {\mathrm{C}} ]$ and field samples $\pmb {S} _ {\mathrm{F}} ^ {\mathrm{C}} = \left[ \pmb {x} _ {n + 1} ^ {\mathrm{C}} , \cdots , \pmb {x} _ {n + f} ^ {\mathrm{C}} \right]$ , where $\pmb {x} _ {i} ^ {\mathrm{C}} ( i \in \{1 , . . . , n \} )$ is the vector with samples of the ith numerical variable, and $\pmb {x} _ {j} ^ {\mathrm{C}} ( j \in \{\pmb {n} + 1 , . . . , \pmb {n} + \pmb {f} \} )$ is the matrix with the samples of the jth field variable. Suppose the number of numerical samples is $n ,$ and the number of field samples is $f ,$ with all field samples having the same dimensionality $N _ {f}$ If there are no field samples, $S _ {\mathrm{F}} ^ {\mathrm{C}} = \{\phi \}$ . Similarly, if no numerical samples exist, ${\cal S} _ {\mathrm{N}} ^ {\mathrm{C}} = \{\phi \}$

b) The field samples $s _ {\mathrm {{F}}} ^ {\mathrm {{C}}}$ are mapped to a low-dimensional space by the proper orthogonal decomposition (POD) method. The mode matrix φ and mode coefficient matrix a of $s _ {\mathrm {{F}}} ^ {\mathrm {{C}}}$ can be calculated by:

$$\pmb {a} _ {j} = \pmb {S} _ {\mathrm{F} j} ^ {\mathrm{C}} \pmb {\varphi} _ {j} ^ {- 1} \quad ( j \in \{1 , . . . , f \} ) ,\tag{1}$$

where $s _ {\mathrm {{F}} j} ^ {\mathrm {{C}}}$ represents the $j \mathrm{th}$ correlated field samples of $\pmb {S} _ {\mathrm{F}} ^ {\mathrm{C}} ; \pmb {a} _ {j}$ and $\varphi _ {j}$ respectively denote the mode coefficient matrix and mode matrix obtained after dimensionality reduction of $s _ {\mathrm {{F}} j} ^ {\mathrm {{C}}}$

c) The first four statistical moments $\pmb {\mu} _ {\mathrm{previous}} = \left[ \pmb {\mu} _ {1} , \cdots \pmb {\mu} _ {n} , \pmb {\mu} _ {n + 1} , \cdots \pmb {\mu} _ {n + f} \right]$ of both the numerical samples $s _ {\mathrm {{N}}} ^ {\mathrm {{C}}}$ and the mode coefficients matrix a are calculated. For $\pmb {x} _ {i} ^ {\mathrm{C}} ( i \in \{1 , . . . , n \} )$ , their statistical moments are denoted as $\pmb {\mu} _ {i} ( \pmb {\mu} _ {i} \in \mathbb {R} ^ {1 \times 4} )$ , and computed through the formula of definition. For $\pmb {x} _ {j} ^ {\mathrm{C}} ( j \in \{n + 1 , . . . , n + f \} )$ , their statistical moments are denoted as $\left[ \pmb {\mu} _ {j 1} , \cdots , \pmb {\mu} _ {j f} \right] \left( \pmb {\mu} _ {j} \in \mathbb {R} ^ {L _ {j} \times 4} \right)$ that are directly calculated using the mode coefficients. The subscript $L _ {j}$ represents the dimensionality of the mode coefficients of the jth field variable, which is determined by the criterion of energy contribution in POD method.

d) The correlation coefficient matrix among the samples in $\pmb {X} ^ {\mathrm{C}}$ is computed, denoted as $\rho ,$ which consists of $\dot {} \rho _ {\mathrm{F}}$ and $\rho _ {\mathrm{N}}$ . The correlation coefficient among the field samples $s _ {\mathrm {{F}}} ^ {\mathrm {{C}}}$ is expressed as:

$${\pmb \rho} _ {\mathrm{F}} = \left[ \pmb {\rho} _ {\mathrm{F1}} , \pmb {\rho} _ {\mathrm{F2}} , \cdots , \pmb {\rho} _ {\mathrm{FN} _ {i}} \right] ,\tag{2}$$

where $\pmb {\rho} _ {\mathrm{F} j} ( j \in \{1 , . . . , N _ {f} \} )$ represents the Pearson correlation coefficient matrix of the data in the jth dimension of $s _ {\mathrm {{F}}} ^ {\mathrm {{C}}}$ , and $\pmb {\rho} _ {\mathrm{F} j} \in \mathbb {R} ^ {f \times f}$ . If the field samples are uncorrelated, $\rho _ {\mathrm{F} j} = 0$

$\rho _ {\mathrm{N}}$ is the correlation coefficient among the numerical samples $\pmb {S} _ {\mathrm{N}} ^ {\mathrm{C}}$ and the mode coefficients ${\pmb a} ,$ thus $\pmb {\rho} _ {\mathrm{N}} \in \mathbb {R} ^ {( n + l ) \times ( n + l )}$ . If no correlation exists, $\pmb {\rho} _ {\mathrm{N} i} = 0$

Step 2: Generation of independent input samples

The cumulative distribution functions (CDFs) of the input variables of current discipline are respectively calculated based on the first four statistical moments of $\pmb {\mu} _ {\mathrm{previous}}$ and $\pmb {\mu} _ {\mathrm{current.}}$ , which are respectively from the upper-level discipline and the source input variables. The inverse CDF method is then applied to respectively generate independent input samples $\widehat {\pmb X} _ {\mathrm{previous}} ^ {\mathrm{I}} = \left\lceil \widehat {\pmb x} _ {1} ^ {\mathrm{I}} , . . . , \widehat {\pmb x} _ {n} ^ {\mathrm{I}} , \widehat {\pmb a} _ {1} ^ {\mathrm{I}} , . . . , \widehat {\pmb a} _ {f} ^ {\mathrm{I}} \right\rceil$ and $\widehat {\pmb X} _ {\mathrm{current}} ^ {\mathrm{I}} = \left[ \widehat {\pmb x} _ {a} ^ {\mathrm{I}} , \cdots \widehat {\pmb x} _ {a + c} ^ {\mathrm{I}} \right]$ , where the superscript I indicates independent samples, $\textstyle [ {\widehat {\pmb x}} _ {1} ^ {\mathrm{I}} , \cdots , {\widehat {\pmb x}} _ {n} ^ {\mathrm{I}} ]$ are the independent numerical samples, $\left[ \widehat {\pmb {a}} _ {1} ^ {\mathrm{I}} , . . . , \widehat {\pmb {a}} _ {f} ^ {\mathrm{I}} \right]$ are the independent mode coefficient samples, and c denotes the number of source input variables. The input variables for the current discipline are assumed to be mutually independent.

Step 3: Correlation transformation of the generated samples of input variables from the upper-level discipline

The correlation transformation method, applicable to both numerical and field samples, is presented in Section 2.2. In this step, this method is used to transform independent input samples $\widehat {\pmb {X}} _ {\mathrm{previous}} ^ {\mathrm{I}}$ into correlated input samples $\widehat {\pmb {X}} _ {\mathrm{previous}} ^ {\mathrm{C}}$

Step 4: Uncertainty analysis using the current discipline model

The source input samples $\widehat {\pmb X} _ {\mathrm{current}} ^ {\mathrm{I}}$ and the correlated input samples $\widehat {\pmb {X}} _ {\mathrm{previous}} ^ {\mathrm{C}}$ from the discipline of the upper-level are fed into the current discipline model for uncertainty analysis. The output samples $\pmb {y} ^ {\mathrm{c}}$ of the current discipline are thereby obtained.

## 2.2. Correlation transformation method for both numerical and field samples

The Nataf transformation requires selecting a reference variable, relative to which samples of other variables are transformed using the provided correlation coefficient matrix. In general, the choice of reference variable does not significantly affect the transformation results. To achieve the correlation transformation of both numerical and field samples, the method selects a certain field sample $\pmb {x} _ {j} ^ {\mathrm{I}} ( j \in \{n + 1 , . . . , n + f \} )$ and its corresponding resampled mode coefficient matrix $\widehat {\pmb {a}} _ {j} ^ {\mathrm{I}} ( j \in \{1 , . . . , f \} )$ as the reference for the transformation of other field samples and numerical samples, respectively. The correlation transformation is illustrated in Fig. 4, and the detailed steps are as follows:

a) Using $\widehat {\pmb {a}} _ {j} ^ {\mathrm{I}} ( j \in \{1 , . . . , f \} )$ as the reference, the improved Nataf transformation method based on warm-start-based maximum entropy is applied to transform the independent samples $\widehat {\pmb X} ^ {\mathrm{I}} = \left\lceil \widehat {\pmb x} _ {1} ^ {\mathrm{I}} , \cdots , \widehat {\pmb x} _ {n} ^ {\mathrm{I}} , \widehat {\pmb a} _ {1} ^ {\mathrm{I}} , \cdots \right$ L ${\widehat {\mathbf {a}}} _ {f} ^ {\mathrm{I}} \Big |$ based on the correlation coefficien ${\bf \mathcal {P}} _ {\mathrm{N}}$ of the numerical samples, yielding the correlated numerical samples $\widehat {\pmb {S}} _ {\mathrm{N}} ^ {\mathrm{C}} = \left[ \widehat {\pmb {x}} _ {1} ^ {\mathrm{C}} , \cdots , \widehat {\pmb {x}} _ {n} ^ {\mathrm{C}} \right]$

b) Based on the mode matrix $\varphi ,$ the mode coefficients $\left[ \widehat {\pmb {a}} _ {1} ^ {\mathrm{I}} , . . . , \widehat {\pmb {a}} _ {f} ^ {\mathrm{I}} \right]$ are used to reconstruct the independent field samples $\widehat {\pmb {S}} _ {\mathrm{F}} ^ {\mathrm{I}} = \left[ \widehat {\pmb {x}} _ {n + 1} ^ {\mathrm{I}} , \cdots \right$ $\widehat {\pmb {x}} _ {n + f} ^ {\mathrm{I}} \Big ]$ by

$$\widehat {\pmb {S}} _ {\mathrm{F} j} ^ {\mathrm{I}} = \widehat {\pmb {a}} _ {j} ^ {C} \pmb {\varphi} _ {j} \quad ( j \in \{1 , . . . , f \} ) .\tag{3}$$

c) Setting $\pmb {x} _ {j} ^ {\mathrm{I}} ( j \in \{n + 1 , . . . , n + f \} )$ as the reference, the improved Nataf transformation method based on warm-start-based maximum entropy is applied to transform $\widehat {\pmb {S}} _ {\mathrm{F}} ^ {\mathrm{I}}$ based on the correlation coefficient $\rho _ {\mathrm{F}}$ of the field samples, yielding correlated field samples $\widehat {\pmb {S}} _ {\mathrm{F}} ^ {\mathrm{C}} = \left\lceil \widehat {\pmb {x}} _ {n + 1} ^ {\mathrm{C}} \right\rceil$ $\cdots , \widehat {\pmb {x}} _ {n + f} ^ {\mathrm{C}} \bigg ]$

The correlated numerical samples $\widehat {\pmb {S}} _ {\mathrm{N}} ^ {\mathrm{C}} = [ \widehat {\pmb {x}} _ {1} ^ {\mathrm{C}} , \cdots , \widehat {\pmb {x}} _ {n} ^ {\mathrm{C}} ]$ obtained in step a) and the correlated field samples $\widehat {\pmb {S}} _ {\mathrm{F}} ^ {\mathrm{C}} = \left\lceil \widehat {\pmb {x}} _ {n + 1} ^ {\mathrm{C}} , \cdots , \widehat {\pmb {x}} _ {n + f} ^ {\mathrm{C}} \right\rceil$ obtained in step c) are combined to form the correlated input samples $\widehat {\pmb x} ^ {\mathrm{C}} = \lceil \widehat {\pmb x} _ {1} ^ {\mathrm{C}} , \cdots , \widehat {\pmb x} _ {n} ^ {\mathrm{C}}$ $\widehat {\pmb {x}} _ {n + 1} ^ {\mathrm{C}} , \cdots , \widehat {\pmb {x}} _ {n + f} ^ {\mathrm{C}} \bigg ]$

2.2.1. Improved Nataf transformation method based on warm-start-based maximum entropy

We introduce a warm-start strategy to accelerate the computation of variable PDFs using the maximum entropy method within the Nataf transformation. The specific process is illustrated in ${\mathrm{Fig.~}} 5 ,$ and the detailed steps are described as follows.

a) Calculate the first four statistical moments μ of the independent samples zI . When zI is numerical sample, $\pmb {\mu} _ {i} \in \mathbb {R} ^ {1 \times 4}$ . When $\pmb {z} _ {i} ^ {\mathrm{I}}$ is field sample, $\pmb {\mu} _ {i} = \left[ \pmb {\mu} _ {i 1} , \cdots \pmb {\mu} _ {i N _ {f}} \right] \left( \pmb {\mu} _ {i} \in \mathbb {R} ^ {N _ {f} \times 4} \right)$

b) When zI is numerical sample, skip this step. When zI are field samples, calculating the sum of the differences $\Delta _ {j}$ between the statistical moments $\pmb {\mu} _ {i j} \left( j \in \left\{1 , \cdots , N _ {f} \right\} \right)$ (mean, standard deviation, skewness and kurtosis) and the corresponding standard normal distribution moments, as shown in Eq. (4).

$$\Delta _ {j} = \sum _ {t = 1} ^ {4} \mu _ {i j , t} - \mu _ {t} ^ {\mathrm{s}} ( i \in \{1 , 2 , \cdots f \} ) ,\tag{4}$$

where $\mu _ {i j , t}$ represents the tth order moment in the $\mu _ {i j} , \mu _ {i j , 1}$ denotes the mean; $\mu _ {i j , 2}$ 2 denotes the standard deviation; $\mu _ {i j , 3}$ denotes the skewness; $\mu _ {i j , 4}$ denotes the kurtosis; $\mu _ {1} ^ {\mathrm{S}} = 0 , \mu _ {2} ^ {\mathrm{S}} = 1 , \mu _ {3} ^ {\mathrm{S}} = 0 , \mu _ {4} ^ {\mathrm{S}} = 3$ . Then, the elements of Δ are sorted in ascending order. Subsequently, $\mu _ {i j}$ are reordered according to their corresponding $\Delta _ {j}$ values.

c) Next, the maximum entropy method is used to calculate the PDF of the samples. In the optimization process of calculating the jth PDF of $\pmb {z} _ {i} ^ {\mathrm{I}} ( i \in \{1 , . . . , f \} )$ , the optimal coefficient from the $( j {\cdot} 1 ) ^ {\mathrm{th}}$ PDF calculation is used as the initial coefficient for the jth PDF calculation.

d) Subsequently, the independent samples $\pmb {z} ^ {\mathrm{I}}$ are transformed into the standard normal space to obtain $\pmb {z} ^ {\mathrm{I} , S}$ based on $\boldsymbol {F} ( \pmb {z} )$ by the following linear transformation.

$$\pmb {z} ^ {\mathrm{I} , \mathrm{S}} = \phi ^ {- 1} \left( F ( \pmb {z} ^ {\mathrm{I}} ) \right) ,\tag{5}$$

where $\phi ^ {- 1} ( \cdot )$ represents the inverse function of the standard normal CDF.

e) Further, the Nataf inverse transformation is used to convert $\pmb {z} ^ {\mathrm{I} , S}$ into correlated samples $\pmb {z} ^ {\mathrm{C}}$

$$\pmb {z} ^ {\mathrm{C}} = F ^ {- 1} \left( \phi \left( \pmb {L} _ {0} \pmb {z} ^ {\mathrm{I} , S} \right) \right) ,\tag{6}$$

where $\scriptstyle L _ {0}$ is the upper triangular matrix obtained from the Cholesky decomposition of $\rho$

## 2.2.2. Nataf transformation

The Nataf transformation maps correlated random variables into independent standard normal variables by leveraging each variable’s marginal CDF and the Pearson correlation coefficient matrix [18–20].

The Pearson correlation coefficient, denoted as $\rho ,$ quantifies the degree of linear correlation between two variables, ranging from − 1 to 1. The close ${\rho}$ is to 1, the stronger the positive correlation; the closer ρ is to − 1, the stronger the negative correlation.

For a set of linearly correlated random variables $\pmb {x} = [ \pmb {x} _ {1} , \pmb {x} _ {2} , \pmb {\cdots} \pmb {x} _ {n} ] ^ {\mathrm{T}} ,$ their correlations are represented by the correlation coefficient matrix $\rho = [ \rho _ {i j} ] _ {n \times n} ;$ where the Pearson correlation coefficient $\rho _ {i j}$ is calculated using the following function:

$$\rho _ {i j} = \frac {\mathrm{cov} \left( x _ {i} , x _ {j} \right)} {\sigma _ {x _ {i}} \sigma _ {x _ {j}}} ,\tag{7}$$

where $\sigma _ {x _ {i}}$ and $\sigma _ {x _ {j}}$ are the standard deviations of $x _ {i}$ and $x _ {j} ,$ respectively.

Subsequently, we use Eq. (8) to transform the random variable x from the original space to the standard normal space, yielding a standard normal random variable z.

$$z _ {i} = \phi ^ {- 1} ( F _ {i} ( x _ {i} ) ) ,\tag{8}$$

where $\phi ^ {- 1} ( \cdot )$ represents the inverse function of the standard normal CDF; $F _ {i} ( \cdot )$ denotes the marginal CDF of the variable xi.

Let the correlation coefficient matrix of z be $\rho _ {0} = \left[ \rho _ {0 i j} \right] _ {n \times n}$ . The transformation from $\rho _ {i j}$ in the original space to $\rho _ {0 i j}$ in the standard normal space can be achieved through the following formula [21]:

$$\begin{array} {l} {\displaystyle \rho _ {i j} = \int _ {- \infty} ^ {\infty} \int _ {- \infty} ^ {\infty} \left[ \frac {F _ {i} ^ {- 1} \left( \phi ( z _ {i} ) \right) - \mu _ {i}} {\sigma _ {i}} \right]} \\ {\displaystyle \left[ \frac {F _ {j} ^ {- 1} \left( \phi \left( z _ {j} \right) \right) - \mu _ {j}} {\sigma _ {j}} \right] \phi ( z _ {i} , z _ {j} , \rho _ {0 i j} ) d z _ {i} d z _ {j}} \end{array} ,\tag{9}$$

where $\phi \left( z _ {i} , z _ {j} , \rho _ {0 i j} \right)$ is the joint probability density function of variables zi and $z _ {j} ,$ whose correlation coefficient is $\rho _ {0 i j}$

Since the correlation coefficient matrix $\rho _ {0}$ is usually symmetric, it can be decomposed using the Cholesky decomposition:

$${\rho} _ {0} = {\cal L} _ {0} {\cal L} _ {0} ^ {T} ,\tag{10}$$

where $\scriptstyle L _ {0}$ is the lower triangular matrix from the Cholesky decomposition.

Subsequently, the standard normal correlated variables z can be converted into independent standard normal variables y through a linear transformation described by Eq. (11).

$$\pmb {y} = \pmb {L} _ {0} ^ {- 1} \pmb {z} .\tag{11}$$

The Nataf transformation can be succinctly summarized as:

$$\pmb {y} = \pmb {L} _ {0} ^ {- 1} \phi ^ {- 1} ( F ( \pmb {x} ) ) = \mathrm{Nataf} ( \pmb {x} ) .\tag{12}$$

The inverse Nataf transformation can be applied to generate correlated random variables with specific distributions:

$${\pmb x} = {\pmb F} ^ {- 1} ( \phi ( {\pmb L} _ {0} {\pmb y} ) ) = \mathrm{Nataf} ^ {- 1} ( {\pmb y} ) .\tag{13}$$

## 2.2.3. Maximum entropy method

For random variables with complex, realistic distributions, the maximum entropy method can accurately estimate their PDFs using a sufficient number of statistical moments as constraints during the optimization of characteristic parameters [22,23].

In this study, to achieve precise UP, the first four statistical moments of random variables $\pmb {\mu} = [ \mu _ {1} , \mu _ {2} , \mu _ {3} , \mu _ {4} ]$ were chosen as constraints in constructing the maximum entropy model. These moments are: the mean $\mu _ {1 {:}}$ , standard deviation $\mu _ {2} ,$ skewness $\mu _ {3} {\mathrm{:}}$ , and kurtosis $\mu _ {4}$ . The first four moments were chosen as constraints for two main reasons:

(1) They effectively characterize the fundamental properties of an arbitrary uncertainty distribution, including location, dispersion, asymmetry, and tail behavior.

(2) As the moment order increases, the sample moments estimated from finite data become progressively unstable and more sensitive to noise or outliers.

Under these constraints, the entropy of the probability density function $p ( x )$ for a random variable can be computed by:

$$H ( x ) = - \int _ {- \infty} ^ {+ \infty} p ( x ) \ln p ( x ) \mathrm{d} \mathbf {x} .\tag{14}$$

The constraints applied to the model are defined as follows:

$$\left\{\begin{array} {l l} {\displaystyle \int _ {- \infty} ^ {+ \infty} p ( x ) \mathrm{d} \mathrm{x} = 1} \\ {\displaystyle \int _ {- \infty} ^ {+ \infty} ( x - \mu ) ^ {i} p ( x ) d \mathrm{x} = \mu _ {i} \ i = 1 , 2 , 3 , 4} \end{array} \right. .\tag{15}$$

To maximize the entropy, the Lagrange function is constructed:

$$\begin{array} {r l} & {L = - \displaystyle \int _ {- \infty} ^ {+ \infty} p ( x ) \ln p ( x ) \mathrm{d} \mathbf {x} + \left( \lambda _ {0} + 1 \right) \left( \int _ {- \infty} ^ {+ \infty} p ( x ) \mathrm{d} \mathbf {x} - 1 \right)} \\ & {\quad \quad + \displaystyle \sum _ {i = 1} ^ {4} \left( \lambda _ {i} \left( \int _ {- \infty} ^ {+ \infty} {( x - \mu )} ^ {i} p ( x ) d \mathbf {x} - \mu _ {i} \right) \right) .} \end{array}\tag{16}$$

Setting the partial derivative of L with respect to $p ( x )$ to zero, yields the expression for p(x):

$$p ( {\pmb x} ) = \exp \left\{\lambda _ {0} + \sum _ {i = 1} ^ {4} \left( {\pmb x} - {\pmb \mu} \right) ^ {i} \lambda _ {i} \right\} .\tag{17}$$

Equation (17) expresses the probability distribution that maximizes entropy while satisfying the specified central moment constraints. To determine the corresponding Lagrange multipliers, we formulate the following optimization problem:

$$\begin{array} {l} {\displaystyle \mathrm{given} \ \mu = \left[ \mu _ {1} , \mu _ {2} , \mu _ {3} , \mu _ {4} \right]} \\ {\displaystyle \mathrm{find} \lambda = \left[ \lambda _ {0} , \lambda _ {1} , \lambda _ {2} , \lambda _ {3} , \lambda _ {4} \right]} \\ {\displaystyle \operatorname* {m i n} _ {\scriptstyle {\begin{array} {l} {R} \end{array}}} R = \sum _ {i = 0} ^ {4} r _ {i} ^ {2}} \\ {r _ {i} = \displaystyle \int _ {- \infty} ^ {+ \infty} \left( x - \mu \right) ^ {i} p ( x ) d \mathbf x - \mu _ {i}} \end{array} .\tag{18}$$

The characteristic parameters $\lambda _ {i}$ are obtained by solving the above optimization problem. Therefore, we can determine the probability density function using the maximum entropy principle.

## 2.3. POD method

The POD method is widely used for constructing reduced-order models. Its main goal is to represent high-dimensional data in a lowerdimensional space via a linear combination of basis modes. POD has found extensive applications in the modeling and analysis of field data across engineering and scientific computations [24–26]. The procedure of the POD method is outlined as follows.

(1) The field data $x ( \boldsymbol n \times \boldsymbol p )$ is first standardized by subtracting its mean, yielding the standardized data x:

$$\begin{array} {r} {\overline {{\pmb {x}}} = \Big [ \pmb {x} _ {1} - \pmb {\mu} _ {x _ {1}} , \pmb {x} _ {2} - \pmb {\mu} _ {x _ {2}} , . . . \pmb {x} _ {p} - \pmb {\mu} _ {x _ {p}} \Big ] ,} \end{array}\tag{19}$$

where $\pmb {\mu} _ {x} = \left\lceil \mu _ {x _ {1}} , \cdots \mu _ {x _ {p}} \right\rceil$ denotes the mean for each dimension of the field samples x; p indicates the dimensionality; n represents the number of samples in x.

(2) The covariance matrix C of x can be computed as follows:

$${\pmb {C}} = {\overline {{\pmb {x}}} ^ {T}} {\overline {{\pmb {x}}}} / n .\tag{20}$$

(3) The mode coefficients a and modes φ of the covariance matrix are computed through:

$$C \varphi = {\pmb {a}} \varphi .\tag{21}$$

(4) The field data x can be approximated as a linear combination of modes φ:

$$\pmb {x} = \overline {{\pmb {x}}} + \sum _ {i = 1} ^ {k} a _ {i} \varphi _ {i} ,\tag{22}$$

where k represents the number of truncated modes. The selection of k is typically specified by the analysis of energy contribution:

$$I {=} \frac {\sum _ {i = 1} ^ {k} a _ {i}} {\sum _ {i = 1} ^ {n} a _ {i}} .\tag{23}$$

In practical applications, to ensure accurate reduced-order modeling, the cumulative energy contribution of the retained modes is typically required to exceed 99 % [27]. For scenarios demanding higher precision, modes accounting for more than 99.9 % of the total energy should be retained.

## 3. Method validation by the analytical test

We conducted an analytical test case consisting of four subsystems to validate the proposed method. The propagated uncertainties included both numerical and field variables.

The relationships governing uncertainty propagation among the subsystems are illustrated in ${\mathrm{Fig.~}} 6$ The analytical models for the four subsystems are as follows:

Subsystem 1:

$$\left\{\begin{array} {l l} {b _ {1} = a _ {1} + 2 a _ {2}} \\ {b _ {2} = 4 a _ {1} + a _ {2}} \end{array} \right. ,\tag{24}$$

Subsystem 2:

$$\left\{\begin{array} {l} {c _ {1} = 2 b _ {1} t ^ {2} + b _ {2}} \\ {c _ {2} = 4 b _ {1} + b _ {2} t ^ {2}} \end{array} \right. t \in [ 0 , 10 ] ,\tag{25}$$

Subsystem 3:

$$\left\{\begin{array} {l l} {{d _ {1} = 2 b _ {1} + 3 b _ {2} - 40}} \\ {{d _ {2} = - 3 b _ {1} + b _ {2} + 20}} \end{array} \right. ,\tag{26}$$

Subsystem 4:

$$e = \int _ {0} ^ {5} c _ {1} + c _ {2} d c - d _ {1} - d _ {2} ,\tag{27}$$

where, $a _ {1}$ and $a _ {2}$ are numerical input variables for Subsystem 1, following normal distributions N(3, 1) and $N ( 1 , 0 ) ,$ respectively; state variables $b _ {1}$ and $b _ {2}$ are numerical output variables from Subsystem 1, which serve as input variables for Subsystems 2 and $_ {3 ;}$ state variables $\pmb {c} _ {1}$ and $\pmb {c} _ {2}$ are field output variables from Subsystem 2, which serve as input variables for Subsystem 4; state variables d and d are numerical output variables for Subsystem 3, and together with $\pmb {c} _ {1}$ and $\mathbf {c} _ {2} ,$ serve as input variables for Subsystem $4 ;$ e is the final output variable of Subsystem 4.

Subsystems 1 and 3 are linear systems, while Subsystem 2 is a timevarying nonlinear system, and Subsystem 4 is a nonlinear system. In this system, the interactions among subsystems are primarily represented by variables b, c, and d. The outputs of Subsystems 2 and 3, namely c and d, respectively, exhibit correlation due to their shared input. Therefore, considering the correlation between input variables c and d is crucial to obtain an accurate output e from the overall system.

By applying the POD method, $\pmb {c} _ {1}$ and $\pmb {c} _ {2}$ are reduced in dimensionality. Subsequently, we obtain the mode coefficients $\boldsymbol {a} _ {c 1}$ and $\mathbf {\boldsymbol {a}} _ {c 2} ,$ , based on their energy proportion.

During the resampling process for numerical variables, $\boldsymbol {a} _ {c 1}$ is used as the reference for correlation transformation. Table 1 compares the correlation coefficients for the original and resampled samples. The close alignment of these coefficients demonstrates the method’s ability to accurately capture the correlation between the state variables.

Similarly, for the field variables, correlation transformation is performed using c1 as the reference. Fig. 7 illustrates the Pearson correlation coefficient samples between $\pmb {c} _ {1}$ and $\pmb {c} _ {2}$ for both the original and resampled samples. The close similarity between these results further reinforces the method’s efficacy in accurately capturing the correlations among the field state variables.

The MCS results serve as a benchmark for performance comparison here. Table 2 presents the first four statistical moments $\{\mu _ {1} , \mu _ {2} , \mu _ {3} , \mu _ {4} \}$ of the output variable e obtained through the multidisciplinary UP method, with and without correlation consideration. The results show that

incorporating correlations produces moments that closely match those obtained via the MCS method, while drastically reducing the number of response function evaluations nf (1000 compared to ${10} ^ {6}$ with MCS). Although the relative error for skewness $\mu _ {3}$ is relatively high, its impact remains minor due to the small magnitude of the value.

Using these statistical moments, the PDF of e is obtained via the maximum entropy method, as shown in Fig. 8. When correlations are accounted for, the computed PDF closely matches the MCS result, whereas ignoring correlations produces noticeable deviations. This emphasizes the critical importance of including correlations among intermediate variables to prevent substantial errors in multidisciplinary uncertainty propagation.

## 4. Multidisciplinary uncertainty propagation of a solid rocket system

## 4.1. Problem description

This case examines the accurate propagation of uncertainties in a solid rocket system encompassing aerodynamic, engine, and trajectory disciplines. The UP relationships within the system are illustrated in Fig. 9.

In this system, the aerodynamic discipline propagates uncertainties in lift and drag coefficients across different operating conditions to the trajectory discipline, while the engine discipline conveys uncertainties in thrust, mass, and critical time points. Additionally, the trajectory discipline accounts for uncertainties in atmospheric density and local sound velocity, collectively influencing the uncertainty of velocity and total energy at the first-stage separation point.

Aerodynamic analysis is performed using computational fluid dynamics (CFD) to evaluate aerodynamic performance. In the engine discipline, a zero-dimensional internal ballistics simulation is employed, with thrust and mass normalized across different combustion intervals [28]. Consequently, the output uncertainty variables from the engine discipline are the thrust and mass (as field variables) and key time points (as numerical variables). Trajectory planning utilizes a three-degrees-of-freedom particle motion model, with uncertainty analysis conducted around a nominal trajectory. To enhance computational efficiency in the UP process, polynomial chaos expansion (PCE) is applied to surrogate the computationally intensive aerodynamic and engine models. The source uncertainty variables for each discipline are summarized in Tables 3–5.

In Table $^ {5 ,}$ the mean values of the variables are not provided, as they vary in real time during flight. The uncertainty of the wind field is represented by the uncertainty of the angle of attack.

Among the input uncertainty variables in the trajectory discipline, the lift and drag coefficients are numerical variables that exhibit correlation. Similarly, the thrust and mass (field variables) and the key time points (numerical variables) are also correlated.

## 4.2. Uncertainty propagation analysis of the solid rocket system considering field variable correlations

In the aerodynamic discipline, we compared the correlation coefficients of the lift and drag coefficients between the original (baseline) samples and the resampled samples, as presented in Table 6. The maximum relative error in the correlations is only 0.24 %, confirming that the proposed method accurately preserves the correlations among

(a) Heatmap of numerical variable correlations of the original samples

(b) Heatmap of numerical variable correlations of the resampled samples

numerical variables.

In the engine discipline, the POD method is initially employed to map thrust into a low-dimensional space. Mode coefficients $a _ {1} , a _ {2} ,$ , and $a _ {3}$ are retained based on their energy proportion, and their correlations with key time points are then modeled. Fig. 10 compares correlations among the numerical samples and mode coefficients for both original and resampled data, showing a maximum relative error of 5.80 %.

Furthermore, Fig. 11 presents a comparison of correlation coefficients for thrust and mass across different sample sets, showing a maximum relative error of 3.08 %. These results indicate that the proposed method can effectively capture correlations for both numerical and field variables during UP.

The results obtained using the MCS method serve as a reference to verify the multidisciplinary UP outcomes, as presented in Tables 7 and 8. In the tables, the lower bound $l _ {b}$ denotes the uncertainty lower bound associated with the velocity and total energy at the first-stage separation point, which directly impacts the key metrics of rocket orbital insertion.

The results indicate that, accounting for correlations, the accuracy of the standard deviation $\mu _ {2}$ for the velocity and total energy at the firststage separation point is improved by 22.75 % and 32.57 %, respectively, and the accuracy of the lower bound lb is enhanced by 5.20 % and 4.20 %, respectively. Since the lower bound is a crucial parameter in rocket design, a 5 % improvement is considered numerically significant. Although the relative error of skewness $\mu _ {3}$ is large, the effect on the output variable is small due to its small value. The PDFs for the velocity and total energy at the first-stage separation point are obtained using the maximum entropy method, as illustrated in Figs. 12 and 13, based on these statistical parameters.

Notably, the PDF curves generated by the proposed method closely match the reference PDF, with mean discrepancies below 0.2 % and standard deviations under 6 %. Ignoring correlations among state variables during propagation can cause significant deviations in multidisciplinary UP analysis. The proposed method effectively accounts for these correlations, enabling accurate uncertainty quantification across different variable types.

## 5. Conclusion

In this study, we propose a multidisciplinary UP method that accounts for correlations among field state variables during propagation. The main conclusions are as follows.

1) Using the improved Nataf transformation with a warm-start-based maximum entropy approach, correlated field variables can be accurately generated. In the solid rocket case, the maximum error of the resampled field samples was 3.08 %.

2) By introducing a reference during correlation transformation, the method handles both numerical and field variables. In the solid rocket study, this enabled correlation transformation for key time points (numerical) as well as thrust and mass (field variables).

3) The proposed method enhances the accuracy of multidisciplinary UP for complex systems. Specifically, for the solid rocket system, the standard deviation accuracy of velocity and total energy at first-stage separation improved by 22.75 % and 32.57 %, respectively, while the lower-bound accuracy improved by 5.20 % and 4.20 %, respectively.

Notably, the proposed method requires correlated field variables to have the same dimension. Future work could address this limitation by introducing a preprocessing step to unify field variable dimensions before UP analysis, with the approach tailored to the characteristics of each problem.

## CRediT authorship contribution statement

Siyi Du: Writing – review & editing, Writing – original draft, Validation, Software, Methodology, Data curation. Chunna Li: Writing – review & editing, Supervision, Project administration, Funding acquisition. Yang Liu: Visualization, Methodology, Investigation. Chunlin Gong: Supervision, Project administration.

## Omitted Tables

- [Table 1 omitted; saved to tables/table_001.md]
- [Table 2 omitted; saved to tables/table_002.md]
- [Table 3 omitted; saved to tables/table_003.md]
- [Table 4 omitted; saved to tables/table_004.md]
- [Table 5 omitted; saved to tables/table_005.md]
- [Table 6 omitted; saved to tables/table_006.md]
- [Table 7 omitted; saved to tables/table_007.md]
- [Table 8 omitted; saved to tables/table_008.md]
