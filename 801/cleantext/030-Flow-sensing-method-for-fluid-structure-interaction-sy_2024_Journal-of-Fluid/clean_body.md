## 1. Introduction

Inspired by bio-inspiration such as flexible cilia structure of arthropods and fish lateral line system (Tao and Yu, 2012; Tri antafyllou et al., 2016; Zhai et al., 2021), flow sensing technology is proposed and widely used in physical science and engineering to obtain flow speed and direction (Wolf et al., 2018; Wang et al., 2022), distribute underwater sources (Zheng et al., 2018; Liu et al., 2018), reconstruct surface pressure of aircraft (Zhao et al., 2021), analysis fluid-structure stability (Yao et al., 2022), and optimize sensors (Xu et al., 2019) (Verma et al., 2020). Generally, the essence of flow sensing method is to obtain local or global flow properties from sensor measurements of the fluid or structure. In this method, flow modeling is required to map sensor measurements to flow properties.

In general, flow modeling methods can be divided into three types: white-box, black-box, and gray-box (Loiseau et al., 2018; Zhang et al., 2022). The white-box methods obtain accurate flow solutions directly by high-fidelity numerical method, but the computational time is considerably long. While the black-box and gray-box methods are data-driven modeling methods that can quickly obtain flow solutions with high accuracy. Specifically, the black-box methods build an input-output mapping model directly by surrogate model (Kou and Zhang, 2021) or machine learning approach (Calzolari and Liu, 2021) to predict the flow properties, which is an end-to-end model. The gray-box methods build low-dimensional reduced-order models (ROMs) (Kim, 2016; Rowley and Dawson, 2017) to approximate the flow properties, which reduces modeling difficulty of high-dimensional data by extracting the coherent structures in flow. Thus, both black-box and gray-box methods can rapidly and accurately forecast flow properties, and are widely used in flow sensing problems, such as steady flow or unsteady flow with static and moving structure.

For steady flow, (Zhao et al., 2021) constructed a compressed sensing method using proper orthogonal decomposition (POD), and achieved high-precision reconstruction of airfoil pressure by a few measurement data. Lu et al. (2022) used POD-Kriging to predict the flow field and applied it in uncertainty quantification analysis in CFD. Sabater et al. (2022) investigated predicting aircraft surface pressure distribution by three methods, which are Gaussian processes, POD combined with interpolation, and deep neural network (DNN). Zhang et al. (2021) constructed a multi-fidelity surrogate model of aerodynamic performance using DNN, and applied it to aerodynamic shape optimization. Sekar et al. (2019) proposed a fast prediction method of flow field over airfoils combining convolutional neural network (CNN) and deep multilayer perceptron. Similarly, Thuerey et al. (2020) proposed a deep learning approach for flow field prediction based on U-Net architecture. In above studies, many deep learning algorithms are used in the black-box methods, but only POD is used in the gray-box methods.

Similarly, flow sensing methods for unsteady flow with static structure have been comprehensively studied in recent years. To obtain dynamic evolution feature of unsteady flow, dynamic mode decomposition (DMD) (Schmid, 2010) based on frequency characteristics is used in the gray-box methods. Dang et al. (2021)) proposed a background flow sensing method for AUVs with arbitrary shapes based on DMD. Zhang et al. (2022) proposed a flow sensing method combining DMD and long short-term memory (LSTM) network, and achieved prediction of unsteady flow around a circular cylinder from sparse sensor measurements. Besides, various machine learning methods for unsteady flow reconstruction using sensor measurements are raised (Dubois et al., 2022), and applied in flow control (Castellanos et al., 2022). More methods based on ROMs and deep learning are also implemented in unsteady flow sensing. Fresca and Manzoni (2022) investigated a fusion modeling method for nonlinear time-dependent system by combining POD and DNN, and applied it to flow prediction around a cylinder. Han et al. (2019) raised a prediction method for unsteady wake flows by hybrid deep neural network, which is constituted by CNN, convolutional LSTM, and deconvolutional neural network. This method is further applied to unsteady transonic buffet flow prediction (Liu et al., 2022). In addition, the unsteady flow sensing methods have also been applied to assimilate data in subsurface flow system (Tang et al., 2021) and mechanism analysis of vortex-induced vibration (VIV) (Kou et al., 2017).

Unsteady flow with moving structure always arises in nature flows (Fang et al., 2022), long-span architecture (Gao et al., 2021), and aerospace engineering (Kou and Zhang, 2021), such as aeroelasticity, VIV, and flexible flow sensors. Since the unsteady flow with moving structure usually involves fluid-structure interaction (FSI), which is more complex than steady flow and unsteady flow with static structure, it brings more challenges for flow sensing methods in modeling strategy and accuracy. Li et al. (2019) used LSTM to forecast unsteady aerodynamics of airfoil pitching and plunging system under different flow conditions, but this study only focused on predicting aerodynamic coefficients. Rozov and Breitsamter (2021) proposed a data-driven method using CNN for predicting motion-induced unsteady pressure distributions. The modeling methods in aeroelasticity were reviewed by Kou and Zhang (2021), and the relevant methods have been applied in transonic aeroelastic optimization (Wang et al., 2018) and unsteady aerodynamic prediction of iced airfoils with pitching (Wang et al., 2022). Zhang et al. (2022) used DNN to model VIV responses of flexible pipes under oscillatory flow, and realized prediction of VIV displacements and vortex shedding frequency. Wolf et al. (2019) used LSTM to sense moving underwater source by measuring several artificial lateral lines. Zhou et al. (2015) achieved sensing distributed near-body pressure and inlet velocity through a few sensors on fish body. In addition to above sensing methods for local flow properties, researchers have also developed some flow sensing methods of entire flow field. Ma and Pan (2021) presented a ROM for dynamical systems with moving boundaries and achieved flow field prediction of the FSI system. Zhang et al. (2022) realized predicting the unsteady flow over a flexible cylinder using convolutional variational autoencoder and sparse identification of nonlinear dynamics. Most of the existing flow sensing research was only carried out on simple FSI systems, and the research on real-time flow sensing methods for complex FSI systems with multi flexible structures is insufficient, which is necessary and meaningful to biomimetic flow sensing.

Based on the previous introduction, both black-box and gray-box models are expected to deal with the flow sensing problem of complex FSI systems. However, complex FSI systems contain rich information about both structure and fluid, especially the flow field data is high-dimensional. Directly constructing flow sensing model using black-box model can lead to issues such as large network architecture, high computational complexity, and limited interpretability. Therefore, the black-box model is not prioritized.

The gray-box model can utilize ROMs such as POD to extract features from the structural and flow field data, effectively reducing data dimensionality, and mitigating the modeling complexity of the flow sensing model. However, the flow field may exhibit variations in flow characteristics and complexities at different locations. The conventional POD approach typically models the entire flow field without specifically focusing on regions with above mentioned variations. Therefore, it is crucial to propose a new POD modeling strategy to capture such variations of the flow field and ensure accurate modeling in local regions.

In this work, a novel flow sensing method is proposed to achieve the real-time prediction of flow field for FSI systems using structural deformation information. The essence of the proposed approach is constructing the mapping from structural deformation to flow field using a gray-box model, which combines POD, multilayer POD and DNN. Specifically, POD is first used to build a lowdimensional model for structural deformation. Since the POD modeling accuracy is hard to be guaranteed in complex flow regions, a multilayer POD strategy is raised for data reduction of flow field. With this strategy, the complex flow regions are identified according to POD reconstruction, subsequently a new layer POD can be built for the residual flow (Jia et al., 2022) of the identified regions. The new layer POD is built repeatedly until the POD modeling accuracy is satisfied. Afterwards, a DNN model is built to establish the map

between the mode coefficients of structure and fluid.

The contributions of the present work are as follows:

1. Combing POD, multilayer POD, and DNN, a real-time flow sensing method for FSI systems using structure measurements is proposed. The proposed method is capable of flow sensing challenges involving multiple sensors and complex unsteady flow, such as the FSI system with filaments set.

2. The multilayer POD model is raised to enhance the modeling accuracy of unsteady flow with little increase of modeling data and time, which is superior to the POD.

3. The proposed flow sensing method can handle flow sensing problems with transient flow conditions, and its suitability and spatialtemporal performance are verified.

The paper is organized as follows: Section 2 presents the basic procedure of flow sensing model via multilayer POD. Section 3 describes the numerical simulation method and model description of FSI systems. In Section 4, two test cases are carried out by the proposed method. Section 5 gives the conclusions of this paper.

## 2. Flow sensing method

## 2.1. Proper orthogonal decomposition

A uniformly sampled snapshot sequence for unsteady flow field and structural deformation in FSI system by numerical simulation (such as velocity components of fluid, discrete point coordinates of the structure, etc.) is described as

$$\mathbf {D} = [ \mathbf {D} _ {1} , \mathbf {D} _ {2} , \cdots , \mathbf {D} _ {r} ]$$

where r is the number of the snapshots. $\mathbf {D} _ {i} ( i = 1 , 2 , \cdots , r )$ is an n-dimensional column vector, and n is the number of mesh elements for fluid or structure mesh. Define the mean value of D as d, which represents the mean flow of the fluid or the baseline shape of the structure. In this paper, d for the structure is the location of the flexible structure without forces, but for the fluid, d needs to be calculated by

$$\overline {{\mathbf {d}}} = \sum _ {i = 1} ^ {r} \mathbf {D} _ {i} \int _ {\mathbf {\Omega}} r\tag{1}$$

d represents the common item of all snapshots, which is also regarded as mode 0 in POD modeling. So, we usually first standardize the original data by removing d. The standardized data $\mathbf {d} = [ \mathbf {d} _ {1} , \mathbf {d} _ {2} , \cdots , \mathbf {d} _ {r} ]$ can be calculated by subtracting d from D. There are two type of POD algorithms, including standard POD and snapshot-POD (Wu et al., 2018). The standard POD is a universal algorithm whether at $n \leq r \mathrm{or} n > r$ . While when $n \gg r ,$ the snapshot-POD needs less memory and is more efficient comparing with standard POD. Hence, in this paper, the standard POD (as described in Table Algorithm 1) and snapshot-POD (as described in Table Algorithm 2) are used to model structural deformation and flow field, respectively. Details of these algorithms can be found in Appendix A.

Through POD modeling, $\mathbf {D} _ {i}$ can be approximately expressed as

$$\mathbf {D} _ {i} \approx [ \pmb {\xi} _ {1} , \pmb {\xi} _ {2} , \cdots , \pmb {\xi} _ {m} ] \mathbf {a} _ {i} + \mathbf {\overline {{d}}}\tag{2}$$

where, $\pmb {\xi} = [ \pmb {\xi} _ {1} , \pmb {\xi} _ {2} , \cdots , \pmb {\xi} _ {m} ] \in \mathbb {R} ^ {n \times m}$ represents the first m dominant POD modes, and $\mathbf {a} _ {i} = \left[ \pmb {a} _ {i} ^ {1} , \pmb {a} _ {i} ^ {2} , \cdots , \pmb {a} _ {i} ^ {m} \right] ^ {\mathrm{T}} \in \mathbb {R} ^ {m \times 1}$ represents the POD mode coefficients corresponding to ξ of Di.

(a) Modeling

## 2.2. Deep neural network

DNN is widely used in classification and regression due to its strong nonlinear mapping, self-learning and self-adapting abilities. A typical DNN model includes an input layer, the hidden layers and an output layer. The architecture of a DNN model is shown in Fig. 1. In this paper, the DNN model is trained by a backpropagation algorithm (Sun et al., 2020) and used to establish the mapping between the POD mode coefficients of structural deformation and flow properties, which is defined as ψ:

$$\mathbf {t} = \psi ( \mathbf {s} )\tag{3}$$

where, s and t represent the input and output data of the DNN, respectively. In this paper, s represents the mode coefficients of structure, and t represents the mode coefficients of fluid.

For all the cases considered in this work involving DNN, a grouped modeling approach is employed. Specifically, each group consists of coefficients corresponding to every five flow modes, resulting in an output dimension of five for the DNN. The input dimension of the DNN is consistent with the dimension of the mode coefficients of the structure. After conducting several investigations, we have decided to use four hidden layers, with each layer containing twelve neurons. The activation functions of the hidden layers and output layer are considered to be tanh and linear functions, respectively. The training algorithm used is Bayesian Regularization with an initial learning rate of 0.01, and the maximum number of training epochs is set to 3000. Mean squared error is chosen as the metric to measure network performance.

## 2.3. Flow sensing model via multilayer POD

The modeling and forecasting architectures of the proposed method are shown in $\mathrm{Fig}$ . 2. In the modeling stage, the model mapping structural deformation to flow properties is built. In the forecasting stage, the trained model is applied to forecast the flow field with inputs of structural deformation. Details are introduced in the following.

The modeling stage is shown in Fig. 2(a). First, the FSI system data is obtained through numerical simulation, including snapshots of original flow field and structural deformation, which are described as $\mathbf {D} _ {\mathrm{f}} = [ \mathbf {D} _ {\mathrm{f} , 1} , \mathbf {D} _ {\mathrm{f} , 2} , \cdots , \mathbf {D} _ {\mathrm{f} , r} ] = [ D _ {\mathrm{f} , i , j} ] n _ {\mathrm{f}} \times r$ and ${\bf D} _ {\mathrm{s}} = [ {\bf D} _ {\mathrm{s} , 1} , {\bf D} _ {\mathrm{s} , 2} , \cdots$ $\mathbf {D} _ {\mathrm{s} , r} ] = [ D _ {\mathrm{s} , i , j} ] n _ {\mathrm{s}} \times r ,$ respectively. where, r is the number of the snapshots, $n _ {\mathrm{f}}$ and $n _ {s}$ are the data dimension of flow field and structural deformation, respectively.

Thereafter, a POD model $f _ {\mathrm{POD}}$ for structure and a multilayer POD model $f _ {\mathrm{multilayer-POD}}$ for fluid are established, respectively. We construct the POD model using structural deformation data, then the modes $\pmb {\xi} _ {\mathrm{s}} = [ \pmb {\xi} _ {\mathrm{s} , 1} , \pmb {\xi} _ {\mathrm{s} , 2} , \cdots , \pmb {\xi} _ {\mathrm{s} , m _ {\mathrm{s}}} ] \in \mathbb {R} ^ {n _ {\mathrm{s}} \times m _ {\mathrm{s}}}$ and corresponding mode coefficients $\mathbf {a} _ {\mathrm{s}} = [ \mathbf {a} _ {\mathrm{s} , 1} , \mathbf {a} _ {\mathrm{s} , 2} , \cdots , \mathbf {a} _ {\mathrm{s} , r} ] \in \mathbb {R} ^ {m _ {\mathrm{s}} \times r}$ of the structure are obtained, and can be expressed by

$$[ \xi _ {\mathrm{s}} , \mathbf {a} _ {\mathrm{s}} ] = f _ {\mathrm{POD}} ( \mathbf {D} _ {\mathrm{s}} )\tag{4}$$

where $m _ {s}$ is the number of the structural modes, which is determined by error analysis of POD reconstruction. $\mathbf {D} _ {\mathrm{s}}$ can be approximately expressed with high accuracy, that is,

$${\bf D} _ {\mathrm{s}} \approx {\bf D} _ {\mathrm{s}} ^ {'} = f _ {\mathrm{POD}} ^ {'} ( \pmb {\xi} _ {\mathrm{s}} , \mathbf {a} _ {\mathrm{s}} )\tag{5}$$

where ${\bf \delta D} _ {\mathrm{s}} ^ {'}$ is the POD reconstruction result of structural deformation, which is close to ${\bf D} _ {\mathrm{s}}$ in value. $f _ {\mathrm{POD}} ^ {'}$ represents the POD reconstruction for $f _ {\mathrm{POD}}$

For fluid, we construct the multilayer POD using flow field data. First, we build the first-layer $\mathrm{POD} f _ {\mathrm{POD-1}}$ of the whole flow field, then the dominant flow modes $\boldsymbol {\xi} _ {\mathrm{f}} ^ {1}$ and corresponding mode coefficients $\mathbf {a} _ {\mathrm{f}} ^ {1}$ can be obtained based on the energy proportion of modes.

$$\left[ \pmb {\xi} _ {\mathrm{f}} ^ {1} , \mathbf {a} _ {\mathrm{f}} ^ {1} \right] = f _ {\mathrm{POD-1}} \left( \mathbf {D} _ {\mathrm{f}} \right)\tag{6}$$

where $\begin{array} {r} {\boldsymbol {\mathfrak {E}} _ {\mathrm{f}} ^ {1} = [ \boldsymbol {\mathfrak {E}} _ {\mathrm{f} , 1} ^ {1} , \boldsymbol {\mathfrak {E}} _ {\mathrm{f} , 2} ^ {1} , \cdots , \boldsymbol {\mathfrak {E}} _ {\mathrm{f} , m _ {i , 1}} ^ {1} ] \in \mathbb {R} ^ {n _ {i} \times m _ {\mathrm{f} , 1}} , \mathbf {a} _ {\mathrm{f}} ^ {1} = [ \mathbf {a} _ {\mathrm{f} , 1} ^ {1} , \mathbf {a} _ {\mathrm{f} , 2} ^ {1} , \cdots , \mathbf {a} _ {\mathrm{f} , r} ^ {1} ] \in \mathbb {R} ^ {m _ {i , 1} \times r}} \end{array}$ . m , is the number of the fluid modes of the first-layer POD. Through POD reconstruction and error analysis, the reconstructed flow $\mathbf {D} _ {\mathrm{f}} ^ {1} {} ^ {'} = [ \mathbf {D} _ {\mathrm{f} , 1} ^ {1} {} ^ {'} , \mathbf {D} _ {\mathrm{f} , 2} ^ {1} {} ^ {'} , \cdots , \mathbf {D} _ {\mathrm{f} , r} ^ {1} ] \in \mathbb {R} ^ {n _ {\mathrm{f}} \times r}$ by the first layer POD model is solved by

$${\bf D} _ {\mathrm{f}} ^ {1 ^ {'}} = f _ {\mathrm{POD} - 1} ^ {'} \left( \xi _ {\mathrm{f}} ^ {1} , \mathbf {a} _ {\mathrm{f}} ^ {1} \right)\tag{7}$$

In order to evaluate the reconstructed performance of the first-layer POD model for fluid, mean reconstructed error $\mathbf {E} _ {\mathrm{f}} ^ {1} \ =$ $\lbrack E _ {\mathrm{f} , 1} ^ {1} , E _ {\mathrm{f} , 2} ^ {1} , \cdots , E _ {\mathrm{f} , n _ {\mathrm{f}}} ^ {1} \rbrack ^ {\mathrm{T}} \in \mathbb {R} ^ {n _ {\mathrm{f}} \times 1}$ is defined, which is solved by

$$\mathbf {E} _ {\mathrm{f}} ^ {1} = \frac {1} {r} \sum _ {j = 1} ^ {r} \left| \mathbf {D} _ {\mathrm{f} , j} - \mathbf {D} _ {\mathrm{f} , j} ^ {1} \right|\tag{8}$$

Then, an error threshold σ is defined and used to identify the modeling region of next layer POD. We define the modeling region of the first-layer POD is $\mathbf {S} ^ {1} = \left[ S _ {1} ^ {1} , S _ {2} ^ {1} , \cdots , S _ {n _ {t}} ^ {1} \right] ^ {\mathrm{T}}$ . The modeling region of the second-layer POD is obtained by $\mathbf {S} ^ {2} = \left[ S _ {1} ^ {2} , S _ {2} ^ {2} , \cdots , S _ {n _ {\mathrm{f} , 2}} ^ {2} \right] ^ {\mathrm{T}} =$ $\big [ S _ {c 1} ^ {1} , S _ {c 2} ^ {1} , \cdots , S _ {c n _ {\mathrm{f.2}}} ^ {1} \big ] ^ {\mathrm{T}}$ , which satisfies $\{c 1 , c 2 , \cdots , c n _ {\mathrm{f,2}} \} = \{i | i = 1 , 2 , \cdots , n _ {\mathrm{f}} , E _ {\mathrm{f} , i} ^ {1} > \sigma \} . n _ {\mathrm{f,2}}$ is the modeling data dimension of the second-layer POD, and satisfies $n _ {\mathrm{f} , 2} \leq n _ {\mathrm{f}}$ , which means the modeling efficiency of the second-layer POD is superior to that of the first-layer POD. In the meanwhile, the residual flow $\mathbf {D} _ {\mathrm{f}} ^ {2} = [ \mathbf {D} _ {\mathrm{f} , 1} ^ {2} , \mathbf {D} _ {\mathrm{f} , 2} ^ {2} , \cdots , \mathbf {D} _ {\mathrm{f} , r} ^ {2} ] \in \mathbb {R} ^ {n _ {\mathrm{f} , 2} \times r}$ can be obtained by subtracting the reconstructed flow from the original flow, which stands for the detail item of flow (Jia et al., 2022).

$$\mathbf {D} _ {\mathrm{f}} ^ {2} = \left[ D _ {\mathrm{f} , i , j} - D _ {\mathrm{f} , i , j} ^ {1} \right] _ {i = c 1 , c 2 , \cdots , c n _ {\mathrm{f} , 2} , j = 1 , 2 , \cdots , r}\tag{9}$$

Then, similar to the first layer POD, we construct the second-layer $\mathrm{POD} f _ {\mathrm{POD-2}}$ for the residual flow of the first-layer and perform the corresponding reconstruction error analysis. The new layer POD is constructed repeatedly until the reconstruction error satisfies the modeling requirements. Here, the modeling process of the kth-layer POD $( k = 2 , 3 , \cdots , z )$ is given by

$$\left\{\begin{array} {l l} {\displaystyle \Big [ \xi _ {t} ^ {k} , \mathbf {a} _ {t} ^ {k} \Big ] = f _ {\mathrm{POD-} k} \Big ( \mathbf {D} _ {t} ^ {k} \Big )} \\ {\displaystyle \mathbf {D} _ {t} ^ {k ^ {\prime}} = f _ {\mathrm{POD-} k} \Big ( \xi _ {t} ^ {k} , \mathbf {a} _ {t} ^ {k} \Big )} \\ {\displaystyle \mathbf {E} _ {t} ^ {k} = \frac {1} {r} \sum _ {j = 1} ^ {r} \Big | \mathbf {D} _ {t , j} ^ {k} - \mathbf {D} _ {t , j} ^ {k ^ {\prime}} \Big |} \\ {\displaystyle \mathbf {D} _ {t} ^ {k + 1} = \Big [ D _ {t , i , j} ^ {k} - D _ {t , i , j} ^ {k} \Big ] _ {i = c _ {1} , c _ {2} , . . . , c _ {n , k} , j = 1 , 2 , . . . , r}} \end{array} \right.\tag{10}$$

where, $\pmb {\xi} _ {\mathrm{f}} ^ {k} = [ \pmb {\xi} _ {\mathrm{f} , 1} ^ {k} , \pmb {\xi} _ {\mathrm{f} , 2} ^ {k} , \cdots , \pmb {\xi} _ {\mathrm{f} , m _ {\mathrm{f} , k}} ^ {k} ] \in \mathbb {R} ^ {n _ {\mathrm{f} , k} \times m _ {\mathrm{f} , k}}$ and $\mathbf {a} _ {\mathrm{f}} ^ {k} = [ \mathbf {a} _ {\mathrm{f,1}} ^ {k} , \mathbf {a} _ {\mathrm{f,2}} ^ {k} , \cdots , \mathbf {a} _ {\mathrm{f,\itr}} ^ {k} ] \in \mathbb {R} ^ {m _ {\mathrm {f , {k}}} \times r}$ are flow modes and corresponding mode coefficients of the kth-layer POD, respectively. $\mathbf {D} _ {\mathrm{f}} ^ {k ^ {^ {\prime}}} = [ \mathbf {D} _ {\mathrm{f} , 1} ^ {k} , \mathbf {D} _ {\mathrm{f} , 2} ^ {k ^ {^ {\prime}}} , \cdots , \mathbf {D} _ {\mathrm{f} , r} ^ {k ^ {^ {\prime}}} ] \in \mathbb {R} ^ {n _ {\mathrm{f} , k} \times r}$ and $\mathbf {E} _ {\mathrm{f}} ^ {k} = [ E _ {\mathrm{f} , 1} ^ {k} , E _ {\mathrm{f} , 2} ^ {k} , \cdots , E _ {\mathrm{f} , n _ {\mathrm{f} , k}} ^ {k} ] ^ {\mathrm{T}} \in \mathbb {R} ^ {n _ {\mathrm{f} , k} \times 1}$ represent the reconstructed flow and mean reconstructed error by the kth-layer POD, respectively. $\mathbf {D} _ {\mathrm{f}} ^ {k + 1} = [ \mathbf {D} _ {\mathrm{f} , 1} ^ {k + 1} , \mathbf {D} _ {\mathrm{f} , 2} ^ {k + 1} , \cdots , \mathbf {D} _ {\mathrm{f} , r} ^ {k + 1} ] \in \mathbb {R} ^ {n _ {\mathrm{f} , k + 1} \times r}$ is the residual flow of the kth-layer POD, and also represents the modeling data of the (k+1)th-layer POD. $\mathbf {S} ^ {k + 1} = \left[ S _ {1} ^ {k + 1} , S _ {2} ^ {k + 1} , \cdots , S _ {n _ {t k + 1}} ^ {k + 1} \right] ^ {\mathrm{T}} = \left[ S _ {c 1} ^ {k} , S _ {c 2} ^ {k} , \cdots , S _ {c n _ {t k + 1}} ^ {k} \right] ^ {\mathrm{T}}$ represents the modeling region of the (k+1)th-layer POD, which satisfies $\{c 1 , c 2 , \cdots , c n _ {\mathrm{f} , k + 1} \} = \{i | i = 1 , 2 , \cdots , n _ {\mathrm{f} , k} , E _ {\mathrm{f} , i} ^ {k} > \sigma \} . n _ {\mathrm{f} , k + 1}$ is the modeling data dimension of the (k+1)th-layer POD, and satisfies $n _ {\mathrm{f} , k + 1} \leq n _ {\mathrm{f} , k}$ . When $\mathbf {S} ^ {k + 1} = \mathbf {D} _ {\mathrm{f}} ^ {k + 1} = \varnothing$ , the multilayer POD model is obtained, that is,

$$\left[ \boldsymbol {\xi} _ {\mathrm{f}} , \mathbf {a} _ {\mathrm{f}} \right] = f _ {\mathrm{multilayer-POD}} \left( \mathbf {D} _ {\mathrm{f}} \right)\tag{11}$$

where $f _ {\mathrm{multilayer-POD}} = \{f _ {\mathrm{POD-1}} , f _ {\mathrm{POD-2}} , \cdots , f _ {\mathrm{POD-2}} \} . \xi _ {\mathrm{f}} = \{\xi _ {\mathrm{f}} ^ {1} , \xi _ {\mathrm{f}} ^ {2} , \cdots , \xi _ {\mathrm{f}} ^ {z} \}$ and $\mathbf {a} _ {\mathrm{f}} = \{\mathbf {a} _ {\mathrm{f}} ^ {1} , \mathbf {a} _ {\mathrm{f}} ^ {2} , \cdots , \mathbf {a} _ {\mathrm{f}} ^ {z} \}$ are the fluid modes and the corresponding mode coefficients of all POD layers in fmultilayer− POD, respectively. Through the multilayer POD, Df can be approximately expressed with the error below $\sigma ,$ that is,

$$\mathbf {D} _ {\mathrm{f}} \approx \mathbf {D} _ {\mathrm{f}} ^ {'} = f _ {\mathrm{multilayer-POD}} ^ {'} \left( \pmb {\xi} _ {\mathrm{f}} , \mathbf {a} _ {\mathrm{f}} \right)\tag{12}$$

Furthermore, a DNN model $f _ {\mathrm{DNN}}$ is used to establish the mapping between structure and fluid. The mode coefficients of the POD for structure are taken as the input of the DNN, and the mode coefficients of the multilayer POD for fluid are taken as the output of the DNN. The mapping can be expressed as

$${\bf a} _ {\mathrm{f}} = f _ {\mathrm{DNN}} ( {\bf a} _ {\mathrm{s}} )\tag{13}$$

So far, the flow sensing model for the FSI system has been built by combing the POD for structure, multilayer POD for fluid, and DNN for structure and fluid modes coefficients, which is given by

$$\mathbf {D} _ {\mathrm{s}} {\longleftrightarrow} _ {\dot {f} _ {\mathrm{POD}}} ^ {f _ {\mathrm{POD}}} \mathbf {a} _ {\mathrm{s}} \overset {f _ {\mathrm{DNN}}} {} \mathbf {a} _ {\mathrm{f}} {\longleftrightarrow} _ {\dot {f} _ {\mathrm{multilayer-POD}}} ^ {f _ {\mathrm{multilayer-POD}}} \mathbf {D} _ {\mathrm{f}}\tag{14}$$

The forecasting stage is as shown in Fig. 2(b). First, the structure snapshot $\widehat {\mathbf {D}} _ {\mathrm{s}}$ sat a new moment is given, then the corresponding structural mode coefficients $\widehat {\mathbf {a}} _ {\mathrm{s}}$ can be solved by the POD model fPOD for structure. Thereafter, the structural mode coefficients $\widehat {\mathbf {a}} _ {\mathrm{s}}$ are fed into the trained DNN $f _ {\mathrm{DNN}}$ to obtain the fluid mode coefficients $\widehat {\mathbf {a}} _ {\mathrm{f}}$ of multilayer POD.

$$\widehat {\mathbf {a}} _ {\mathrm{f}} = f _ {\mathrm{DNN}} ( \widehat {\mathbf {a}} _ {\mathrm{s}} )\tag{15}$$

Furthermore, the corresponding fluid flow $\widehat {\mathbf {D}} _ {\mathrm{f}} ^ {1} , \widehat {\mathbf {D}} _ {\mathrm{f}} ^ {2} , \cdots , \widehat {\mathbf {D}} _ {\mathrm{f}} ^ {z}$ of each layer POD can be obtained by POD reconstruction.

$$\widehat {\mathbf {D}} _ {\mathrm{f}} ^ {k ^ {^ {\prime}}} = f _ {\mathrm{POD} - k} ^ {^ {\prime}} \big ( \xi _ {\mathrm{f}} , \widehat {\mathbf {a}} _ {\mathrm{f}} \big )\tag{16}$$

Finally, the forecasted flow field $\widehat {\mathbf {D}} _ {\mathrm{f}}$ is obtained by fusing the forecasted flow field by all POD layers.

$$\widehat {{\mathbf {D}}} _ {\mathrm{f}} = \widehat {{\mathbf {D}}} _ {\mathrm{f}} ^ {1} \oplus \widehat {{\mathbf {D}}} _ {\mathrm{f}} ^ {2} \oplus \cdots \oplus \widehat {{\mathbf {D}}} _ {\mathrm{f}} ^ {z}\tag{17}$$

where, ⊕ represent the operator of element-wise summation.

## 3. Numerical simulation methods and model description of the FSI systems

## 3.1. Lattice Boltzmann method for fluid

In present study, the flow field is solved by the lattice Boltzmann equation (Chen and Doolen, 1998), expressed as

$$\frac {\partial f} {\partial t} + \mathbf {e} \cdot \nabla f + \mathbf {F} \cdot \nabla f = \pmb {\Omega}\tag{18}$$

where $f$ represents the velocity distribution function of the fluid particles, andF represents the external force exerted on the fluid particles. t is time, and e is the velocity of the fluid particles. Ω represents the collision term of the governing equation, which represents the collision relationship between fluid particles. After temporal and spatial discretization, Eq. (18) can be converted into

$$f _ {i} ( \mathbf {x} + \mathbf {e} _ {i} \cdot {\boldsymbol {\Delta}} t , t + {\boldsymbol {\Delta}} t ) - f _ {i} ( \mathbf {x} , t ) = \Omega _ {i} ( \mathbf {x} , t ) + {\boldsymbol {\Delta}} t \cdot \mathbf {F} _ {i} ( \mathbf {x} , t ) i = 0 , 1 , \cdots , m - 1\tag{19}$$

where x is the location of the fluid particle, Δt is the time step of discretization. i represents different motion direction of fluid particles, and the number of the directions is m. In the paper, the 2D fluid-structure model and the widely used D2Q9 lattice velocity model are adopted, so $m = 9$ here. $f _ {i} ( {\bf x} , t )$ represents the distribution function of the fluid particles located at position x and time t with velocity $\mathbf {e} _ {i}$ $\mathbf {e} _ {i} , \mathbf {F} _ {i}$ are respectively the ith component of velocity and external force. $\pmb {\Omega} _ {i}$ represents the collision term, which is a nonlinear function of $f _ {i}$ and expressed by

$$\Omega _ {i} = \frac {1} {\tau} \left( f _ {i} ^ {( e q )} - f _ {i} \right)\tag{20}$$

where τ is the relaxation time and given by

$$\tau = \frac {1} {2} + \frac {\upsilon} {c _ {s} ^ {2} \cdot \Delta t}\tag{21}$$

where υ and $c _ {s}$ represent the kinematic viscosity coefficient of fluid and the lattice speed of sound, respectively. $f _ {i} ^ {( e q )}$ represents the equilibrium distribution function corresponding to $f _ {i} ,$ and can be expressed by

$$f _ {i} ^ {( e q )} = \rho w _ {i} \left[ 1 + \frac {\mathbf {e} _ {i} \cdot \mathbf {u}} {c _ {s} ^ {2}} + \frac {\left( \mathbf {e} _ {i} \cdot \mathbf {u} \right) ^ {2}} {2 c _ {s} ^ {4}} - \frac {\mathbf {u} ^ {2}} {2 c _ {s} ^ {2}} \right]\tag{22}$$

where $\rho$ and u are respectively the density and macroscopic velocity of fluid, $w _ {i}$ represent the weight coefficients of $\mathbf {e} _ {i}$ .

Considering the effect of the external force on fluid momentum and momentum flux (Guo et al., 2002), the expression of $\mathbf {F} _ {i}$ can be expressed by

$$\mathbf {F} _ {i} = \left( 1 - \frac {1} {2 \tau} \right) \cdot w _ {i} \cdot \left[ \frac {\mathbf {e} _ {i} - \mathbf {u}} {c _ {s} ^ {2}} + \frac {\mathbf {e} _ {i} \cdot \mathbf {u}} {c _ {s} ^ {4}} \mathbf {e} _ {i} \right] \cdot \mathbf {f}\tag{23}$$

where f is the force density acting on fluid. Then the macroscopic quantities (density and velocity) of fluid can be calculated by

$$\rho = \sum _ {i = 0} ^ {m - 1} f _ {i}\tag{24}$$

$$\rho \mathbf {{u}} = \sum _ {i = 0} ^ {m - 1} \mathbf {{e}} _ {i} f _ {i} + \frac {1} {2} \mathbf {{f}} \Delta t = \rho \mathbf {{u}} ^ {*} + \frac {1} {2} \mathbf {{f}} \Delta t\tag{25}$$

where u∗is defined as the intermediate velocity.

## 3.2. Finite element method for structure

In this work, the dynamic response of flexible structure is obtained by the nonlinear finite element method (FEM), in which each filament of the structure is regarded as a series of Euler–Bernoulli beam, and each beam element has two boundary nodes. The dynamic equation of the structure is as follows.

$${\bf M} \ddot {\bf X} ( t ) + {\bf C} \dot {\bf X} ( t ) + {\bf F} _ {\mathrm{int}} ( {\bf X} ) - {\bf F} _ {\mathrm{ext}} ( t ) = 0\tag{26}$$

where, M and C are respectively the mass and damping matrix of the structure. $\mathbf {X} , {\dot {\mathbf {X}}} ,$ and $\ddot {\mathbf {X}}$ are respectively the displacement, velocity and acceleration of the boundary nodes of the structure. $\mathbf {F} _ {\mathrm{int}}$ represents the internal force resulted from structural deformation, which is a nonlinear function of $\mathbf {X} , \mathbf {F} _ {\mathrm{ext}}$ represents the external forces acting on the structure, which can be described as follows

$${\bf F} _ {\mathrm{ext}} ( s _ {l} , t ) = - \int _ {\Pi _ {l}} {\bf f} d \nu + {\bf F} _ {\mathrm{oth}} ( s _ {l} , t )\tag{27}$$

where, $\Pi _ {l}$ represents the fluid point domain corresponding to the lth Lagrangian point, as is shown in $\mathrm{Fig.~} 3 , \mathbf {f}$ represents the force density within Πl that is only affected by the Lagrangian point, $\mathbf {F} _ {\mathrm{oth}}$ is other external force, such as gravity.

X, $\dot {\mathbf {X}} ,$ and $\ddot {\mathbf {X}}$ of the structure can be solved (Gong et al., 2018) by the Newmark-β method and Newton-Raphson method.

## 3.3. Immersed boundary method

The immersed boundary method (IBM) is adopted to achieve the interface data exchange between fluid and structure. In the IBM, the fluid and structure use two independent sets of grids and coordinate systems (Oxy for fluid and O′ s for structure), as is shown in Fig. 3. The fluid is discretized by a series of regular Eulerian points. The structural boundary Γ immersed in the fluid is discretized by a series of Lagrangian points, which are the structural boundary nodes in Section 3.2, and will move when the structure is deformed. Each Lagrangian point has its corresponding fluid point domain in the Cartesian coordinate system. All Eulerian points in this domain are influenced by the corresponding Lagrangian point, and the information exchange between Lagrangian points and Eulerian points is achieved by the interpolation operations as follows.

The fluid velocity u $\mathbf {\Gamma} ( \mathbf {X} , t )$ at Lagrangian point X can be obtained by interpolating the fluid velocity ${\bf u} ( {\bf x} , t )$ at Eulerian point x, which is expressed by

$$\mathbf {u} ( \mathbf {X} , t ) = \sum _ {\Pi} \mathbf {u} ( \mathbf {x} , t ) \delta ( \mathbf {x} - \mathbf {X} ) \Delta x \Delta y\tag{28}$$

where δ represents the three-point Dirac delta function (Roma et al., 1999), Δx and $\Delta y$ are respectively the size of the lattice in x and y-direction, here $\Delta x = \Delta y$ . Then the structural boundary velocity U(X, t) is equal to the fluid velocity ${\bf u} ( {\bf X} , t )$ due to the non-slip boundary condition. Then, Eq. (25) can be expressed under the Lagrangian frame as

$$\rho ( \mathbf {X} , t ) \cdot \mathbf {U} ( \mathbf {X} , t ) = \rho ( \mathbf {X} , t ) \cdot \mathbf {u} ^ {*} ( \mathbf {X} , t ) + \frac {1} {2} \mathbf {f} ^ {'} ( \mathbf {X} , t ) \Delta t\tag{29}$$

where $\rho ( {\mathbf {X}} , t )$ and ${\bf u} ^ {*} ( {\bf X} , t )$ are respectively calculated by interpolating the fluid density $\rho ( \mathbf {x} , t )$ and intermediate velocity $\mathbf {u} ^ {*} ( \mathbf {x} , t )$ similar to Eq. (28). Since the force density $\mathbf {f} ^ {'} ( \mathbf {X} , t )$ at Lagrangian point X can be obtained by solving Eq. (29), the force density $\mathbf {f} \left( \mathbf {x} , t \right)$ at Eulerian point x can be further solved by

$$\mathbf {f} ( \mathbf {x} , t ) = \sum _ {\Gamma} \mathbf {f} ^ {\prime} ( \mathbf {X} , t ) \delta ( \mathbf {x} - \mathbf {X} ) \Delta s\tag{30}$$

where, $\Delta s$ is the length of the structural boundary element. Finally, the flow properties are updated by substituting the force density

f(x, t) into Eq. (25).

The numerical simulation method for a FSI system with flexible structure is obtained by combining the LBM, IBM and FEM, and this simulation framework is named IB-LB-FEM (Gong et al., 2018). The solution process of the numerical simulation is shown in Fig. 4. The present numerical simulation method used in the paper has been fully validated (Gong et al., 2018; Harwood et al., 2018; Connor and Revell, 2019).

## 4. Test cases

## 4.1. Physical models and numerical settings of the FSI systems

The proposed flow sensing method is applied in two FSI systems. The first FSI system is the 2D flow past a flexible filament clamped behind a cylinder, denoted as case A. The computational domain is a rectangle of $4.1 D \times 25 D ,$ , as is shown in Fig. 5. D represents the diameter of the cylinder, which is defined as $D = 0.10 \mathrm{m}$ . The inlet velocity is uniform, expressed by

$$u ( 0 , y ) = \overline {{u}}\tag{31}$$

where u represents the mean velocity of the fluid.

The second FSI system is the flow past a 2D flexible filament set, denoted as case B. The computational domain is a rectangle of 3h × 90h, as is shown in Fig. 6. h represents the height of the filament. The number of the filaments is 51, and the spacing between adjacent filaments is h. The inlet velocity profile for the computational domain is

$$u ( 0 , y ) = 1.5 \overline {{u}} ^ {y} \frac {( 6 h - y )} {9 h ^ {2}} ( 0 \leq y \leq 3 h )\tag{32}$$

In above cases, the dimensionless bending rigidity K and mass ratio M are used to describe material properties, which are computed by Eq. (33) and (34). The Reynolds number of the fluid is given by Eq. (35).

$$K = \frac {E I} {\rho _ {f} \overline {{u}} ^ {2} h ^ {3}}\tag{33}$$

$$M = \frac {\rho _ {s} b} {\rho _ {f} h}\tag{34}$$

(a)

(b)

$$R e = \frac {\overline {{u}} \cdot l} {\upsilon}\tag{35}$$

where, $\rho _ {s}$ and $\rho _ {f}$ are the densities of the fluid and structure, b is the thickness of one filament, E and I are respectively the Young’s modulus and cross-sectional moment of inertia of the filaments. l represents the characteristic length, where l = D in case A and l = h in case B. The values of the parameters are shown in Table 1.

In two cases, the fluid grid width for spatial discretization is $\Delta s = 0.02 l$ , and each filament is discretized by 20 FEM elements. The grid independence of two cases is fully validated, which can be found in Appendix B.

In case A, the motion period of the flexible filament is 0.578 s, while the snapshot sampling interval for the flow field and structural deformation is 0.00224 s. In case B, the motion period of the flexible filament set is 3.33 s, while the snapshot sampling interval for the flow field and structural deformation is 0.0125 s. The details of the numerical simulation results of two cases can be seen in Appendix C.

## 4.2. Case A: 2D flow past a flexible filament clamped behind a cylinder

## 4.2.1. POD for structure

Fig. 7 shows the oscillation amplitude envelope of the flexible filament. The trajectory of the free end during a motion period is in the shape of 8, which is very similar to the results observed in the literature (Gong et al., 2018; Favier et al., 2014).

The POD for structure is established by the coordinates of the uniform discrete points of the filament from the train set. Fig. 8(a) shows the characteristics of first 4 structural modes at moment of $\pmb {t = 0.112 s}$ . The baseline represents the static shape of the filament without external forces. The total energy proportion of the first 4 structural modes reaches 99.96%. Then the maximum reconstructed error $E _ {\mathrm{s}}$ is used to evaluate the reconstruction accuracy of the POD model for structure, which is defined as:

$$E _ {\mathrm{s}} = \operatorname* {m a x} ( | \mathbf {P} ^ {'} - \mathbf {P} | )\tag{36}$$

where, $\mathbf {p} ^ {\prime}$ and P are respectively the reconstructed and real coordinates of the structural discrete points. In this paper, we define $E _ {\mathrm{s}} \leq$ $1.0 \times 10 ^ {- 3} D$ as the condition for satisfying the reconstruction accuracy.

The number of the structural modes can affect the reconstructed accuracy of the POD model. As is shown in Fig. 9, when 10 modes are involved in modeling the POD for structure, Es is $8.88 \times 10 ^ {- 4} D ,$ , which is smaller than $1.0 \times 10 ^ {- 3} D$ and satisfies the reconstructed

accuracy of the structure. Therefore, we select 10 structural modes to build the POD for structure. Fig. 8(b) compares the real filament and corresponding reconstructed filament at the moment of $t = 0.112 s ,$ , and the similarity between the real and reconstructed shapes illustrates that the POD for structure is of high accuracy.

## 4.2.2. Multilayer POD for fluid

The multilayer POD for fluid could model flow properties, including x-component of velocity $\mathbf {V} _ {x} ,$ y-component of velocity $\mathbf {V} _ {y} ,$ pressure p, etc. In this paper, we take ${\bf V} _ {x}$ as an example, the corresponding mean flow and first 4 POD modes are shown in Fig. 10. The total energy proportion of the first 8 modes reaches 99.28%, which satisfies the condition of energy threshold in Appendix A. Therefore, we select 8 modes to build the first-layer POD for fluid.

The reconstruction error is shown in Fig. 11(a). It can be seen that the error is mainly concentrated in the region around the filament and wake region. The region with large error coincides with the region involving complex flow structures, which indicates that the POD model with 8 modes cannot effectively extract the flow information of complex flow. We define an error threshold $\sigma = 0.02 \mathrm{m/s}$ to extract the modeling region for the POD model in next layer. Then we take the region that satisfies the condition $\mathbf {E} _ {\mathrm{f}} ^ {1} > \sigma$ as the modeling region for next layer, as is shown in Fig. 11(b). Similarly, the reconstruction error of the second-layer POD model is computed, shown in Fig. 11(c). The modeling region for the third-layer is selected by the threshold $\sigma ,$ and is shown in Fig. 11(d). Further, the reconstruction error $\mathbf {E} _ {\mathrm{f}} ^ {3}$ is plotted in Fig. 11(e), which satisfies the condition $\begin{array} {r} {\mathbf {E} _ {\mathrm{f}} ^ {3} \leq \sigma .} \end{array}$ . It can be seen that the reconstruction error de creases almost by an order of magnitude for each layer, which indicates that the multilayer POD did greatly improve the model accuracy, especially in local region with complex flow structures.

The modeling parameters and performance indicators of the multilayer POD are shown in Table 2, where, N is the layer number of the multilayer POD model, m is the number of the selected POD modes, $\gamma _ {\mathrm{E}}$ represents the energy proportion of the first m modes of current layer POD, $\gamma _ {S}$ represents the modeling region proportion, which corresponds to the dimension of modeling data n. $\widehat {E} _ {\mathrm{f}} ^ {j}$ represents the maximum $\mathbf {E} _ {\mathrm{f}} ^ {j} ;$ α is the region proportion that satisfies $\mathbf {E} _ {\mathrm{f}} ^ {j} > \sigma _ {\mathrm{i}}$ , which represents the modeling region for next layer; $T _ {\mathrm{POD}}$ is the modeling time of current layer POD.

It can be seen that the POD model in second and third layer needs more modeling modes than the first-layer POD, but the dimension of the modeling data is significantly smaller than that of the first layer, which is the determinant factor in efficient POD modeling. It also consumes less storage space of the selected POD modes. In comparison to the first-layer POD model, the data dimension for the second-layer POD model is reduced by 36.81% and the modeling time is reduced by 33.52%, while the data dimension for the thirdlayer POD is reduced by 97.54% and the modeling time is reduced by 96.43%.

(a) $p _ {0}$ and $u _ {0}$ with the flow constant inflow conditions.

(b) $p _ {0}$ and $u _ {0}$ with transient flow conditions. 
(c) $p _ {0}$ and $\mathrm{d} u _ {0} / \mathrm{d} t$ with transient flow conditions.

(a) From 4.500 to 5.058 s.

(b) From 5.499 to 6.058 s.

(a) The forecasted velocity isolines, where the unit is m/s. 
(b) The forecasted isobars, where the unit is Pa.

(a) 
(b)

## 4.2.3. Training and forecasting

The duration of the train set is 2.890 s and includes 1290 snapshot samples for the flow field and structural deformation, while the duration of the test set is 1.590 s and includes 710 snapshot samples. After respectively building the POD model for the filament and the multilayer POD model for the flow field, the DNN is used to map the POD mode coefficients of structure to all the mode coefficients of the multilayer POD of fluid. Then, the flow sensing model for $\mathbf {V} _ {x}$ is established by combing the POD for structure, the DNN for mode coefficients, and the multilayer POD for fluid.

Similarly, the other flow properties can also be modeled by the flow sensing modeling method. Currently, only the flow sensing models of $\mathbf {V} _ {x} , \mathbf {V} _ {y} ,$ and p are trained, while $\mathbf {V} _ {x} , \mathbf {V} _ {y} , \mathbf {p} ,$ magnitude of velocity $| \mathbf {V} | ,$ and Vorticity ω are forecasted. Fig. 12 shows the forecasted results at $t = 1.196 ~ s$ in the test set. It can be seen that the forecasted results agree well with the results by numerical simulation in general, and the forecasting error is mainly remained in the near wake region of the filament. Besides, due to the modeling regions in each layer of the multilayer POD are different, there are visible numerical variations on the boundary of the modeling region for the second and third POD layers in the error contours. It also consumes less storage space of the selected POD modes It also consumes less storage space of the selected POD modes Owning to the forecasting error is small, this phenomenon does not result in unsmooth streamlines. As shown in Fig. 13, it can be seen that the forecasted streamlines are basically consistent with the real values.

In order to assess the performance of the proposed flow sensing method via multilayer POD, we analyze the effect of the number of

POD layers. The root mean square error (RMSE) e is used as a forecasting performance index, which is expressed by

$$e = \| \textbf {V} - \textbf {V} \| _ {2}\tag{37}$$

where $\| \cdot \| _ {2}$ represents the 2-norm.

Fig. 14 illustrates the temporal performance of the flow sensing model changing with the number of layers within the forecast time of 1.590 s. The time evolution of the error shows that the proposed method has a stable temporal performance due to the fact that the forecasting at different moments is independent and the forecasting error do not accumulate over time for the DNN model. In addition, the error exhibits a basic periodic variation. This is due to the periodic evolution pattern of the FSI system under constant inlet velocity, resulting in periodic distribution of the POD modeling error. Consequently, the flow field prediction error reconstructed from DNNpredicted mode coefficients also exhibit close approximation to periodic variations.

When there is only one layer, the multilayer POD model degenerates to the POD modeling method for structure. For simplicity, we denote the models with 1, 2, 3 layers as model-1, model-2, and model-3, respectively. Furthermore, the forecasted velocity at the moment of $t _ {1} = 0.202 s , t _ {2} = 0.618 s$ , and $t _ {3} = 1.322$ s is compared in Figs. 15 and 16, where the display region is within $1 \leq x / D \leq 20$ and $0 \leq y / D \leq 4.1$

For model-1, it is obvious that the forecasting error by the single-layer POD is much larger than those by the two and three-layer POD. There are visible differences between the forecasted velocity isolines and the reference value, while the differences are mainly on the region around the filament and in the wake. For model-2, the forecasting error is obviously reduced due to modeling the residual flow through the second-layer POD for fluid. However, it still shows obvious forecasting error in the region near the filament, which causes jitter of the velocity isolines within a small range at the corresponding position. Model-3 by the three-layer POD has the smallest forecasting error. The forecasted velocity isolines are quite similar to the referenced ones.

The forecasted pressure at the three moments is compared in Figs. 17 and 18. With an increase in the number of layers, the forecasting error of pressure gradually decreases, consistent with the trend observed in the forecasting error of the velocity magnitude field. The prediction error of the pressure field for each model is concentrated within the envelope of the filament motion, and it is more pronounced compared to error in the velocity field. This is because the pressure on both sides of the filament exhibits significant step changes, which is a typical feature of strong nonlinear flow structure. The linearization assumption of POD leads to noticeable Gibbs phenomenon in the flow field reconstruction in this region. As a result, the forecasted isobars are consistent with referenced ones in most regions but significantly unsmooth in the region near the filament.

## 4.2.4. Case A study with transient flow conditions

The previous case solely validated the proposed flow sensing method for a FSI system with constant inflow conditions. However, in real-world scenarios, the inflow magnitude is not constant and may change. Therefore, to better test the proposed flow sensing method’s performance under off-reference and transient conditions, this section conducted a case study with transient flow conditions. As shown in Fig. 19, we designed a random variation pattern for the inflow velocity over time, the total simulation time is 21.5 s. More specifically, the duration of the train set is 13.44 s, encompassing of 6000 snapshot samples. The inlet velocity varies within the range of 0.85 to 1.10 m/s, corresponding to Reynolds numbers spanning from 85 to 110. The duration of the test set is 8.06 s and the test set includes 3599 snapshot samples. The inlet velocity of the test set in the initial 5.5 s is also within the range of 0.85 to 1.10 m/s. In the following 2.56 s, the inlet velocity is randomly variated within the range of 0.72 to 1.20 m/s. Under these conditions, the FSI system exhibits complex, dynamic, unstable, and stochastic characteristics. The flow behavior may contain more modes, and the structural response will also exhibit long transient modal interactions.

Fig. 20 shows the forecasted results by proposed flow sensing method at t = 1.590 s in the test set. The forecasted results generally match well with the numerical simulation results, while the forecasting error primarily occurs near the filament and in the downstream region. Unlike other field data, the forecasted pressure field shows significant error in the inlet region.

To analyze the reason why the error of the pressure field at the inlet is large, we compared the variation curves of pressure p0, velocity $u _ {0} ,$ and the derivative of velocity with respect to time $\mathrm{d} u _ {0} / \mathrm{d} t$ under both constant and transient flow conditions, at point $( 0 ,$ 2D) in the flow. These curves are shown in Fig. 21. When u0 remains constant, $p _ {0}$ demonstrates a periodic evolution pattern matching the structural deformation period. While when $u _ {0}$ varies with time, the changing trend of $p _ {0}$ is consistent with that of du0 $/ \mathrm{d} t$ In this FSI system, pressure varies due to inlet flow conditions and boundary conditions provided ${\mathbf {b}} \mathbf {y}$ the structure. Specifically, under constant flow conditions, pressure varies exclusively result from filament motion. While, under transient flow conditions, the pressure is affected by changes in inlet velocity and filament motion, with changes in inlet velocity being the primary factor in the inlet region. As a result, this results in significant prediction error when using structural deformation to predict the pressure field in the inlet region.

As shown in Fig. 22, the forecasted streamlines are smooth and generally agree with the actual values. From the perspective of prediction error in multiple physical quantities, Case A shows lower accuracy when considering transient flow conditions compared to the given reference conditions. However, the predicted results are still reasonable, providing initial evidence for the applicability of the proposed method.

(a) Time histories of tip displacement in x-direction 
(b) Time histories of tip displacement in y-direction

To further analyze the temporal performance of the method, Fig. 23 shows the curve of RMSE of the predicted velocity field within the forecast time of 8.06 s. The randomness of the inlet velocity makes the behavior of the FSI system more dynamic and stochastic, resulting in none periodic distribution pattern, which is different from that observed in Fig. 14. Notably, the prediction error is small in the initial 5.5 s. However, after 5.5 s, the prediction error increases significantly resulting in none applicability of the method. This is due to the fact that the inlet velocity exceeds the range of the train set. Consequently, new flow patterns of the fluid, and motion patterns of the structure appear. In the case of the structure, Fig. 24 illustrates the comparison of oscillation amplitude envelope of the flexible filament before and after 5.5 s. A noticeable difference in the filament’s motion patterns can be observed. The established flow sensing model based on data with Reynolds numbers ranging from 85 to 100 cannot accurately predict the flow properties with these new patterns.

The forecasted results of the velocity and pressure are displayed at three selected moments $( t _ {1} = 2.970 s , t _ {2} = 4.682 s$ , and $t _ {3} = 5.327$ s), as shown in Fig. 25, where the display region is consistent with Fig. 15. The predicted velocity isolines and isobars at different moments closely match the referenced ones, with the velocity isolines appearing relatively smooth. However, significant fluctuations are observed in the predicted isobars on both sides of the filament, consisting with the observations in Fig. 17.

Overall, the proposed flow sensing method can be applied to the FSI system with transient conditions, but with a limitation of the transient conditions for the train set.

## 4.3. Case B: Flow past 2D flexible filament set

## 4.3.1. POD for structure

The POD for structure is established in case B, and the modeling process is similar to case A. We select the filament set without external forces as the baseline, and use it to build POD model. Fig. 26(a) shows the characteristics of the first 4 structural modes at moment of $t = 2.36 s$ . The baseline represents the static shape of the filament without external forces. The total energy proportion of the first 4 structural modes reaches 99.10%. As is shown in Fig. 27, when the number of the modes in modeling POD reaches 11, Es is reduced to $7.50 \times 10 ^ {- 4} h ,$ which is smaller than $1.0 \times 10 ^ {- 3} h$ and satisfies the reconstructed accuracy of the structure. Therefore, 11 structural modes are used to build the POD for structure. Fig. 26(b) compares the real filament and corresponding reconstructed filament at the moment of $t = 2.36 s ,$ , and the shapes of the reconstructed filaments are similar to the real shapes. In comparison to case A, the structure of case B is more complex, which contains more flexible filaments, thus the data dimension ns of structural deformation information is much higher than that of case A. The results of POD reconstruction illustrate that the POD for structure can greatly decrease the input dimension of flow sensing model with high accuracy, which is practical in the flow sensing problems with multiple sensors.

## 4.3.2. Multilayer POD for fluid

The multilayer POD for fluid of case B is established, and the modeling process is similar to case A. We also take $\mathbf {V} _ {x}$ as an example, the corresponding mean flow and first 4 POD modes are shown in Fig. 28. The total energy proportion of the first 4 modes reaches 99.59%, which satisfies the condition of energy threshold in Appendix A. Therefore, we select 4 modes to build the first-layer POD for fluid.

(a) Range (maximum, minimum and time-averaged value) of the tip deflection of each filament. 
(b) Time histories of tip deflection of the $40 ^ {\mathrm{th}}$ filament.

The reconstruction error of the first-layer POD is shown in Fig. 29(a). It can be seen that the reconstruction error is mainly concentrated in the region involving the second half the filament set (from 25th to 51th filament). Specifically, it is observed that the angular amplitude increases gradually over the filament set (see Fig. 43(a) in Appendix B), which means the fluid instability increases gradually over the filament set. Along with the development of the instability, coherent vortices appear up to around the 25th filament, and the intensity of coherent vortices becomes higher gradually over the following filaments. Correspondingly, the reconstruction error also increases gradually over the filament set. Therefore, the POD modeling accuracy in this region decreases due to the complexity of the flow field.

Then we define the error threshold σ = 0.2m /s to extract the modeling region for the second-layer, as is shown in Fig. 29(b). Similarly, the reconstruction error of the second-layer POD model is computed, shown in Fig. 29(c). It can be seen that the error is concentrated in the region around the waving trajectory of the rear filaments, and the error is much smaller than that of the first-layer. Successively, the modeling region for the third-layer POD is selected by the threshold σ, and is shown in Fig. 29(d). Further, the reconstructed error of the third-layer POD is computed and plotted in Fig. 29(e). It can be seen that the reconstructed error of the thirdlayer POD satisfies the condition $\begin{array} {r} {\mathbf {E} _ {\mathrm{f}} ^ {3} \leq \sigma .} \end{array}$ . Similar to case A, the reconstructed error in case B decreases almost by an order of magnitude for each layer, which indicates that the multilayer POD did greatly improve the model accuracy, especially in complex flow region with coherent vortices.

The modeling parameters and performance indicators of the multilayer POD are shown in Table 3. It can be seen that the POD model in second and third layer needs more modeling modes than the first-layer POD, but the dimension of the modeling data is significantly smaller than that of the first-layer. In comparison to the first-layer POD model, the data dimension for the second-layer POD model is reduced by 71.62% and the modeling time is reduced by 78.75%, while the data dimension for the third-layer POD is reduced by 98.96% and the modeling time is reduced by 97.91%. It is obvious to see that the POD modeling efficiency is improved, and the storage space of the selected POD modes is reduced.

(a) The structural deformations and the fluid velocity magnitude during one flow period, where the unit is m/s. 
(b) Time evolution of tip displacement of the filament during 4.48 s.

## 4.3.3. Training and forecasting

The duration of the train set is 13.33 s and includes 1066 snapshot samples for the flow field and structural deformation, while the duration of the test set is 9.19 s and includes 735 snapshot samples. Same as in Section 4.2.3, after respectively building the POD model for the filament and the multilayer POD model for the flow field, the DNN is used to map the POD mode coefficients of structure to all the mode coefficients of the multilayer POD of fluid. Then the flow sensing models for $\mathbf {V} _ {x}$ and $\mathbf {V} _ {y}$ are respectively established.

Fig. 30 shows the forecasted results at t = 7.25 s in the test set. It can be seen that the forecasted results agree well with the reference in general, and the forecasting error is mainly remained in the region around the rear filaments and the regions behind. The comparison of the forecasted and real streamlines in the region of $8 \leq x / h \leq 72$ and $0 \leq y / h \leq 3$ , is shown in Fig. 31. It can be seen that in the region containing the filaments from first to 15th, the coherent vortices are small and all of them are confined to the spacing between the filaments. The positions and shapes of forecasted vortices match well with the referenced ones. In the region with the filaments from 16th to 30th, as the fluid instability increases, the coherent vortices present larger scales and begin to tend to across the spacings. While the positions and shapes of the forecasted vortices also match well with the referenced ones. In the region containing the filaments from 31th to 51th, the fluid instability develops to a large level and then remains almost constant, the vortices expand and move upward beyond the filaments. The complexity of the coherent vortices causes slight differences between the forecasted and referenced vortices. Overall, the superior forecasting performance for vortices illustrates the proposed method can deal with the flow sensing problems with multiple complex flow structures.

(a) The structural deformations and the magnitude of fluid velocity during one flow period, where the unit is m/s.

(b) Time evolution of tip displacement in x-direction for the filaments during 22.52 s.

Furthermore, we analyze the effect of the number of POD layers on the model performance. Fig. 31 illustrates the stable temporal performance of the flow sensing model changing with the number of layers during the forecast time of 9.19 s. The forecasted velocity at the moments of $t _ {1} = 1.46 , t _ {2} = 4.73 s ,$ and $t _ {3} = 8.78$ s are compared in Figs. 33 and 34. The display region is within $35 \leq x / h \leq 65$ and $0 \leq y / h \leq 3 ,$ which involves 26 filaments from 26th to 51th.

It is obvious that the forecasting error by the single-layer POD is much larger than those by the two and three-layer POD. There are visible differences between the forecasted velocity isolines and the referenced ones in the region around the rear filaments. For model-2, the forecasting error is obviously reduced and closer to the reference. The forecasting error is concentrated in the small region near the rear filaments, which is significantly smaller due to modeling the residual flow through the second-layer POD for fluid. The threelayer POD has the smallest forecasting error. The forecasted velocity isolines are quite similar to the referenced ones. Besides, the time evolution of the error in Fig. 32 shows that the stable temporal performance of the proposed method is also embodied in current case.

The forecasted pressure at the three moments is compared in Figs. 35 and 36. With an increase in the number of layers, the forecasting error of pressure gradually decreases. The prediction error for each model is concentrated in the region near the rear filaments. Due to the relatively smooth variation of the pressure field, the forecasted isobars are also relatively smooth, and they do not exhibit the fluctuations observed in Case A.

(c) Time evolution of tip displacement in y-direction for the filaments during 22.52 s.

## 4.3.4. Case B study with transient flow conditions

To further validate the proposed flow sensing method’s performance under off-reference and transient conditions, the case B study with transient flow conditions is also conducted. Fig. 37 illustrates the random variation pattern of the inflow velocity over time, ranging from 0.915 to 1.079 m/s. According to Eq.(32), the range of the maximum inlet velocity is 1.37 to 1.62 m/s, corresponding to the Reynolds numbers ranging from 137 to 162. The total simulation time is 72.0 s. Specifically, the duration of the train set is 50.0 s and includes 4000 snapshot samples for the flow field and structural deformation, while the duration of the test set is 22.0 s and includes 1760 snapshot samples.

Fig. 38 shows the forecasted results by the proposed flow sensing method at t = 2.55 s in the test set. The forecasted results generally match well with the numerical simulation results, with the forecasting error primarily occurs near the rear filaments and in the downstream region. Consistent with the results of Case A, the forecasting accuracy under transient flow conditions is lower than that under the given constant flow conditions. Moreover, the forecasted pressure field results also indicate significant error in the inlet region.

The comparison of the forecasted and real streamlines is shown in Fig. 39. It can be seen that the positions and shapes of forecasted vortices basically agree with the referenced ones in most regions. While in the region near x/h = 30 and x/h = 38, a few vortices cannot be predicted. Overall, when compared with the velocity prediction error in Fig. 38, the spatial distribution of streamline prediction error shows consistency with that of the velocity.

Fig. 40 shows the variation of RMSE of the forecasted velocity field within the forecast time of 22.0 s. It can be seen that the error distribution is random. The forecasted results of the velocity and pressure are displayed at three selected moments $( t _ {1} = 10.250 s , t _ {2} =$ 18.188 s, and $t _ {3} = 20.963 ~ \mathrm{s} )$ , as shown in Fig. 41. The display region is within $20 \leq x / h \leq 80$ and $0 \leq y / h \leq 3$ , which involves 41 filaments from 11th to 51th. The forecasted velocity isolines and isobars at different moments show some differences from the referenced ones, but they generally match well with referenced ones and appear relatively smooth.

To summarize, when the velocity of the inlet flow undergoes random changes, the proposed method still demonstrates excellent spatial-temporal forecasting performance for flow sensing problems of complex FSI system.

## 5. Conclusions

In this work, a flow sensing method for FSI systems via multilayer POD is proposed. Two applications are carried out to validate and assess the proposed method. Conclusions are drawn as follows:

(a) Time evolution of tip displacement in x-direction for the filaments during 72.0 s. 
(b) Time evolution of tip displacement in y-direction for the filaments during 72.0 s.

In particular, when using the above two algorithms to build model using the same data D, if $\gamma = \gamma ^ {*}$ , there are: $\pmb {m} = \pmb {m} ^ {*} , \pmb {\xi} = \pmb {\xi} ^ {*}$ , and a

1. The proposed method can deal with the flow sensing problems with high-dimensional sensor measurements. For the fluid, the forecasted flow properties are close to the references, and the forecasting accuracy in the regions with complex flow structures can also be ensured due to the multilayer POD model. Moreover, the forecasting error do not accumulate over time, which shows the stable temporal performance of the proposed method.

2. The raised multilayer POD model can greatly improve the flow field modeling accuracy. The reconstruction error of flow field decreases almost by an order of magnitude for each layer in two cases.

3. The proposed flow sensing method can handle complex FSI system with multiple flexible filaments and address flow sensing problem with transient conditions. However, when it is applied in flow sensing problem with transient conditions, the method only suitable for a certain range of Reynolds numbers, which is the limitation in forecasting transient flows.

## CRediT authorship contribution statement

Xuyi Jia: Methodology, Writing – original draft, Data curation. Chunlin Gong: Investigation, Supervision, Writing – review & editing. Wen Ji: Visualization, Validation, Formal analysis. Chunna Li: Methodology, Writing – review & editing, Funding acquisition.

## Omitted Tables

- [Table 1 omitted; saved to tables/table_001.md]
- [Table 2 omitted; saved to tables/table_002.md]
- [Table 3 omitted; saved to tables/table_003.md]
- [Table 4 omitted; saved to tables/table_004.md]
