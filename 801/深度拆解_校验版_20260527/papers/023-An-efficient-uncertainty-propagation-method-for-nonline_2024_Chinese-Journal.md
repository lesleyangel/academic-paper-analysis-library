# 论文深度拆解：An efficient uncertainty propagation method for nonlinear dynamics with distribution-free P-box processes

> 生成依据：`801/cleantext/023-An-efficient-uncertainty-propagation-method-for-nonline_2024_Chinese-Journal`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`023-An-efficient-uncertainty-propagation-method-for-nonline_2024_Chinese-Journal`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\An-efficient-uncertainty-propagation-method-for-nonline_2024_Chinese-Journal.pdf`
- 页数：23
- clean body 字符数：81033
- 摘要字符数：2126
- 参考文献条数：64
- 图题数：0
- 表题数：0
- 表格文件数：7
- 公式候选数：349
- 提取质量分：0.93
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "41 formula(s) need manual review."}]

## 1. 身份层

- 标题：An efficient uncertainty propagation method for nonlinear dynamics with distribution-free P-box processes
- 年份：2024
- 期刊/来源：Chinese Journal
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：方法/算法 + 数值验证型
- 研究对象：Peer review under responsibility of Editorial Committee of CJA. reference solutions based on the Monte Carlo method, with relative errors of less than 3%, the pro- posed method requires less than 0.2% calculation time. Although these probabilistic methods have achieved success in solving various UP problems, they still face the challenge that collecting sufficient information for constructing precise probability distributions of uncertainties may not always be possible. Specifically, several mul
- 主要方法：The distribution-free P-box process serves as an effective quantification model for time- varying uncertainties in dynamical systems when only imprecise probabilistic information is avail- able. This work develops an efficient method for propagating distribution-free P-box processes in nonlin- ear dynamics. Moreover, the Chebyshev method is introduced and modified to efficiently solve the interval ODEs.
- 主要证据：图表 0 个标题、公式 349 个候选、参考文献 64 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“Peer review under responsibility of Editorial Committee of CJA. reference solutions based on the Monte Carlo method, with relative errors of less than 3%, the pro- posed method req”，可以通过“The distribution-free P-box process serves as an effective quantification model for time- varying uncertainties in dynamical systems when only imprecise probabilistic information is avail- able. This work develops an eff”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：Although these probabilistic methods have achieved success in solving various UP problems, they still face the challenge that collecting sufficient information for constructing precise probability distributions of uncertainties may not always be possible. Then, Li et al.32 proposed a sparse regression method to improve the efficiency of the Chebyshev method. As a result, a large portion of the computational cost is significantly reduced.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：Peer review under responsibility of Editorial Committee of CJA. reference solutions based on the Monte Carlo method, with relative errors of less than 3%, the pro- posed method requires less than 0.2% calculation time. Although these probabilistic methods have achieved success in solving various UP problems, they still face the challenge that collecting sufficient information for constructing precise probability distributions of uncertainties may not always be possible. Specifically, several multi-objective problems need to be solved and can be expressed as follows: $$\begin{array}{c} \left\{\begin{array} {c} \displaystyle {\begin{array} {c} {{\mathrm{min}} \quad {\mathrm{[mean} ( F _ {W _ {m}} ) , \mathrm{var} ( F _ {W _ {m}} ) ]} \\ {F _ {s} \in F _ {W _ {m}} ^ {1}} \\ {{\mathrm{min}} \quad {\mathrm{[-mean} ( F _ {W _ {m}} ) , \mathrm{var} ( F _ {W _ {m}} ) ]} \end{array}}}} \\ {{\displaystyle {\begin{array} {c} {{\mathrm{min}} \quad {\mathrm{[mean} ( F _ {W _ {m}} ) , \mathrm{-var} ( F _ {W _ {m}} ) ]}} \\ {{\mathrm{~}}} \\ {{\mathrm{~}}} \\ {{\mathrm{~} \mathrm {f _ {s}} \in F _ {W _ {m}} ^ {1}}} \end{array}}} \\ {{\displaystyle {\mathrm{min}} \quad {\mathrm{[-mean} ( F _ {W _ {m}} ) , \mathrm{-var} ( F _ {W _ {m}} ) ]}}} \\ {{\displaystyle {\mathrm {f _ {s}} \in F _ {W _ {m}} ^ {1}} \quad {\mathrm{[-mean} ( F _ {W _ {m}} ) , \mathrm{-var} ( F _ {W _ {m}} ) ]}}} \\ {{\mathrm{~}}} \\ {{\mathrm{~} \mathrm{~} {\quad} \mathrm{~} {\quad} \mathrm{~} {\quad} \mathrm{~} {\quad} \mathrm{~} {\quad} \mathrm{~} {\quad} \mathrm{~} {\quad} \mathrm{~} {\quad} \mathrm{~} {\quad} \mathrm{~} {\quad} \mathrm{~}} \\ {{\mathrm{~}}} \\ {{\mathrm{~}}} \\ {{\mathrm{~}} \quad {\mathrm{~} \mathrm{~s.t.} \quad {\mathrm{~}} C F _ {s} \leqslant {\bf 0}}} \end{array}}} \end{array} \right.\tag{24}$$ The non-dominated solutions of these multi-objective problems will form the boundary of the 2-dimensional domain of mean and variance for a P-box.
- 问题来源：多来自工程瓶颈、计算/实验成本、复杂多物理场耦合、可靠性/不确定性传播或材料性能优化需求。
- 为什么重要：该类问题通常直接影响热防护设计、结构安全、飞行性能、能量管理、可靠性评估或材料服役性能。
- 研究边界：以本文模型、实验对象、材料体系、飞行轨迹、结构形式或数据集为边界；外推到其它平台或工况需谨慎。
- 可写作学习点：先给工程必要性，再把大问题压缩成可验证的模型/方法/性能指标问题。

## 4. 位置层：文献版图与 gap

- 已有研究分类推断：
  - 物理/数值模型类：提供机理和高保真基准，但成本较高或边界较窄。
  - 数据驱动/降阶/代理模型类：提升效率，但依赖数据覆盖和泛化验证。
  - 实验/测量类：提供真实证据，但工况、样本和尺度有限。
  - 优化/可靠性/不确定性类：处理设计决策，但常受模型复杂度和计算成本限制。
- 作者声明或文本中可见 gap：However, its application to nonlinear systems remains limited due to excessive computation. The proposed method is validated based on test cases, including a duffing oscillator, a vehicle ride, and an engineering black-box problem of launch vehicle trajectory. The proposed method also possesses the ability to handle complex black-box problems. �2024 Production and hosting by Elsevier Ltd. on behalf of Chinese Society of Aeronautics and Astronautics.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- 未在 Introduction 中稳定识别“带引用的 gap 句”，建议人工复核文献转折段。

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：The distribution-free P-box process serves as an effective quantification model for time- varying uncertainties in dynamical systems when only imprecise probabilistic information is avail- able. This work develops an efficient method for propagating distribution-free P-box processes in nonlin- ear dynamics. Moreover, the Chebyshev method is introduced and modified to efficiently solve the interval ODEs.
- 我判断的真实贡献：把一个具体工程/物理/材料问题转化为可计算、可验证的模型或实验流程，并通过结果图表证明其在效率、精度、可靠性、性能或解释力上的增量。
- 创新类型：方法/算法 + 数值验证型；偏方法/模型/工程应用/实验证据/集成框架之一。
- 创新强度：中等到较强，取决于是否具备清晰 baseline、跨工况验证和误差/性能指标。
- 可能被挑战处：
  - 是否充分比较最接近方法；
  - 训练/实验/仿真工况是否覆盖真实应用；
  - 参数、边界条件和材料/结构假设是否可复现；
  - 结论是否超出证据支持范围。

## 6. 方法层

- 方法目标：用可复现的模型、实验或计算流程回答选题层问题。
- 方法类型：方法/算法 + 数值验证型
- 输入：材料/结构/轨迹/工况/几何/传感器/样本/仿真参数等，需按方法章节和表格核查。
- 输出：性能指标、预测结果、优化方案、可靠性指标、温度/应力/流场/电热性能等。
- 关键步骤推断：
  1. 定义研究对象、几何/材料/工况边界；
  2. 建立理论、数值、实验或数据驱动模型；
  3. 设置参数、网格、样本、训练或测试条件；
  4. 与基准/实验/高保真模型对比；
  5. 用图表和误差/性能指标回收 claim。
- 关键假设：模型边界、材料参数、载荷/温度/流场条件、数据分布或实验测量条件。
- 复现信息充分性：中等。文本和表格提供主流程，但参数完整性、代码/数据开放性和 PDF 图像细节仍需人工核查。

## 7. 证据层

### 7.1 Claim-Evidence 全表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| This work develops an efficient method for propagating distribution-free P-box processes in nonlin- ear dynamics. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (53.8, 33.39, 247.13, 41.44)]] Chinese Journal of Aeronautics, (2024), | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The proposed method is validated based on test cases, including a duffing oscillator, a vehicle ride, and an engineering black-box problem of launch vehicle trajectory. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (53.8, 655.43, 276.23, 686.19)]] * Corresponding author. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The proposed method also possesses the ability to handle complex black-box problems. �2024 Production and hosting by Elsevier Ltd. on behalf of Chinese Society of Aeronautics and Astronautics. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (53.8, 33.39, 247.13, 41.44)]] Chinese Journal of Aeronautics, (2024), | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Different sources of uncertainties are generally represented by different models. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (53.8, 655.43, 276.23, 686.19)]] * Corresponding author. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Aleatory uncertainties, arising from the inherent physical randomness of systems and excitations, can be represented by the probabilistic model, when sufficient and precise data are available. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (53.8, 33.39, 247.13, 41.44)]] Chinese Journal of Aeronautics, (2024), | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| However, the uncertainties resulting from limited or poor-quality data, termed imprecision (a form of epistemic uncertainties), have to be represented by non-probabilistic models.3 When aleatory uncertainties and imprecision appear together and result in impre | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (53.8, 655.43, 276.23, 686.19)]] * Corresponding author. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (53.8, 33.39, 247.13, 41.44)]] Chinese Journal of Aeronautics, (2024), 37(12): 116-138 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (53.8, 655.43, 276.23, 686.19)]] * Corresponding author. E-mail address: leo | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (46.83, 185.41, 54.76, 228.51)]] 8 > > > > > > > > > > < | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (46.83, 235.59, 54.76, 270.69)]] > > > > > > > > > > : | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (303.87, 109.1, 311.81, 136.55)]] 8 > > > > < | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (303.87, 143.63, 311.81, 163.03)]] > > > > : | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 5, bbox (312.32, 503.63, 320.26, 533.68)]] 8 > > > > > < | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 5, bbox (312.32, 540.76, 320.26, 562.77)]] > > > > > : | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> The distribution-free P-box process serves as an effective quantification model for time- varying uncertainties in dynamical systems when only imprecise probabilistic information is avail- able. However, its application to nonlinear systems remains limited due to excessive computation. This work develops an efficient method for propagating distribution-free P-box processes in nonlin- ear dynamics. First, using the Covariance Analysis Describing Equation Technique (CADET), the dynamic problems with P-box processes are transformed into interval Ordinary Differential Equa- tions (ODEs). These equations provide the Mean-and-Covariance (MAC) bounds of the system responses in relation to the MAC bounds of P-box-process excitations. They also separate the pre- viously coupled P-box analysis and nonlinear-dynamic simulations into two sequential steps, including the MAC bound analysis of excitations and the MAC bounds calculation of responses by solving the interval ODEs. Afterward, a Gaussian assumption of the CADET is extended to the P-box form, i.e., the responses are approximate parametric Gaussian P-box processes. As a result, the probability bounds of the responses are approximated by using the solutions of the inter- val ODEs. Moreover, the Chebyshev method is introduced and modified to efficiently solve the interval ODEs. The proposed method is validated based on test cases, including a duffing oscillator, a vehicle ride, and an engineering black-box problem of launch vehicle trajectory. Compared to the
> * Corresponding author. E-mail address: leonwood@nwpu.edu.cn (C. GONG). Peer review under responsibility of Editorial Committee of CJA.
> reference solutions based on the Monte Carlo method, with relative errors of less than 3%, the pro- posed method requires less than 0.2% calculation time. The proposed method also possesses the ability to handle complex black-box problems.
> �2024 Production and hosting by Elsevier Ltd. on behalf of Chinese Society of Aeronautics and Astronautics. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/ licenses/by-nc-nd/4.0/).

### 7.4 摘要中文翻译

> 当只有不精确的概率信息可用时，无分布 P 盒过程可以作为动态系统中时变不确定性的有效量化模型。然而，由于计算量过多，其在非线性系统中的应用仍然受到限制。这项工作开发了一种在非线性动力学中传播无分布 P 盒过程的有效方法。首先，使用协方差分析描述方程技术（CADET），将 P 盒过程的动态问题转化为区间常微分方程（ODE）。这些方程提供了与 P 盒过程激励的 MAC 界限相关的系统响应的均值和协方差 (MAC) 界限。他们还将之前耦合的 P 盒分析和非线性动态模拟分成两个连续步骤，包括激励的 MAC 边界分析和通过求解区间 ODE 进行响应的 MAC 边界计算。然后，将 CADET 的高斯假设扩展到 P 盒形式，即响应是近似参数化高斯 P 盒过程。因此，通过使用区间 ODE 的解来近似响应的概率界限。此外，引入并修改了切比雪夫方法以有效求解区间常微分方程。所提出的方法基于测试用例进行了验证，包括达芬振荡器、车辆行驶和运载火箭轨迹的工程黑盒问题。与 * 通讯作者相比。 E-mail地址：leonwood@nwpu.edu.cn (C. CJA编委会负责同行评审。基于蒙特卡罗方法的参考解，相对误差小于3%，提出的方法需要小于0.2%的计算时间。
> 
> 所提出的方法还具有处理复杂黑盒问题的能力。 �2024年由爱思唯尔有限公司代表中国航空学会制作并主办。这是一篇遵循 CC BY-NC-ND 许可证 (http://creativecommons.org/licenses/by-nc-nd/4.0/) 的开放获取文章。

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusions

> This work defines the Uncertainty Propagation (UP) problem of nonlinear dynamics with distribution-free P-box processes. This problem is meaningful for engineering applications, where only imprecise probabilistic information of dynamic excitations is available. Then, a novel method is presented to efficiently solve the UP problem.
> 
> (1) The proposed UP analysis method decouples the analyses of distribution-free P-box and stochastic analyses of nonlinear systems. As a result, a large portion of the computational cost is significantly reduced. Moreover, an extended Gaussian assumption in P-box form is considered, i.e., the system responses are approximately parametric Gaussian P-box processes. This assumption makes it possible to evaluate the CDF bounds of the response by only obtaining the interval bounds of means and variances.
> 
> (2) The tests performed in this work verify the accuracy of the proposed method. The calculation of error bars shows that compared to the reference solutions, the relative errors of the proposed method are typically less than 1%. The evaluation of CDF bounds shows that the proposed method reaches the relative errors of less than 3%. The Gaussian assumption is therefore effective in providing the error bars with satisfactory precision. In addition, the error of probability-bound evaluation based on the assumption is also acceptable.
> 
> (3) Based on the efficiency of the Chebyshev method for solving interval ODEs, the proposed method only required less than 0.2% calculation time of the reference solutions.
> 
> Fig. 21 Baseline trajectory of launch vehicle.
> 
> (a) Variation in the error bar of $V _ {s} ^ {P . B .}$ with time.
> 
> (b) Approximation of the P-box of $V _ {s} ^ {P . B .}$ at 32.7 s. 
> Fig. 22 Results of launch-vehicle trajectory analysis of $V _ {z} ^ {\mathbf {P . B .}} ( t )$
> 
> (a) Variation in error bar of $Z ^ {\mathrm{P.B.}}$ with time.
> 
> (b) Approximation of P-box of $Z ^ {\mathrm{P.B.}}$ at 32.7 s. 
> Fig. 23 Results of launch-vehicle trajectory analysis of $Z ^ {\mathrm{P.B.}} ( t )$
> 
> (4) The capacity of the method in solving complex blackbox problems is demonstrated by the engineering application of the LV trajectory.

### 7.6 结论中文翻译

> 这项工作定义了具有无分布 P 盒过程的非线性动力学的不确定性传播 (UP) 问题。这个问题对于工程应用来说很有意义，因为工程应用中只能获得不精确的动态激励概率信息。然后，提出了一种有效解决UP问题的新方法。 (1)所提出的UP分析方法将无分布P盒分析和非线性系统随机分析解耦。结果，很大一部分计算成本显着降低。此外，还考虑了P盒形式的扩展高斯假设，即系统响应近似为参数化高斯P盒过程。此假设使得可以仅通过获取均值和方差的区间界限来评估响应的 CDF 界限。 (2)本工作中进行的测试验证了所提出方法的准确性。误差线的计算表明，与参考解相比，所提出方法的相对误差通常小于1%。 CDF界限评估表明，该方法的相对误差小于3%。因此，高斯假设可以有效地提供具有令人满意的精度的误差线。此外，基于假设的概率界限评估的误差也是可以接受的。 (3) 基于切比雪夫方法求解区间常微分方程的效率，该方法只需要参考解的不到 0.2% 的计算时间。 21 运载火箭的基线轨迹。 (a) $V _ {s} ^ {P 的误差线的变化。 (b) $V _ {s} ^ {P 的 P 盒的近似。 22 $V _ {z} ^ {\mathbf {P . 运载火箭轨迹分析结果
> 
> B .}} ( t )$ (a) $Z ^ {\mathrm{P.B.}}$ 误差线随时间的变化。 (b) $Z ^ {\mathrm{P.B.}}$ 在 32.7 秒处的 P 盒近似值。 23 $Z ^ {\mathrm{P.B.}} ( t )$ 运载火箭轨迹分析结果 (4) LV轨迹的工程应用证明了该方法解决复杂黑盒问题的能力。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 7515 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. Nonlinear dynamics with distribution-free P-box processes | 对象/条件/子问题展开 | 1464 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 2.1. Definition of distribution-free P-box processes | 对象/条件/子问题展开 | 4748 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 2.2. Uncertainty propagation problems under P-box processes | 对象/条件/子问题展开 | 6989 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 3. Proposed method | 方法建构 | 208 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 6 | 3.1. Transcription of P-box dynamics using CADET | 对象/条件/子问题展开 | 8691 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 3.2.1. Generation of P-box realizations by discretization technique | 对象/条件/子问题展开 | 2397 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 3.2.2. Domain analysis for mean and variance | 结果验证/讨论 | 9005 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 9 | 3.3. Chebyshev-polynomial-based method for interval ODEs | 方法建构 | 7934 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 10 | 3.4. Uncertainty propagation and a P-box Gaussian assumption | 对象/条件/子问题展开 | 3084 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 3.5. Entire procedure of proposed method | 方法建构 | 5311 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 12 | 4. Tests and setup | 对象/条件/子问题展开 | 2735 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 4.1.1. Duffing oscillator analysis | 结果验证/讨论 | 4927 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 14 | 4.1.2. Vehicle ride analysis | 结果验证/讨论 | 5463 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 15 | 4.2. Application in uncertainty propagation of LV ascent trajectory | 对象/条件/子问题展开 | 1710 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 16 | 4.2.1. Uncertainty propagation problems | 对象/条件/子问题展开 | 3608 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 17 | 4.2.2. Results and discussion | 结果验证/讨论 | 2164 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 18 | 5. Conclusions | 主张回收/边界说明 | 2183 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |

### 8.2 章节推进逻辑

- 摘要：通常按“问题重要性 -> 既有方法不足 -> 本文方法 -> 验证对象 -> 主要结果/性能增量”组织。
- Introduction：先把工程/学术问题放大，再通过文献分类制造 gap，最后收束到本文贡献。
- Method/Model：把 claim 变成可执行流程，读者需要在这里看到变量、假设、输入输出和边界。
- Results/Discussion：把方法有效性转化为图表证据，常通过对比、误差、趋势和敏感性说明。
- Conclusion：回收主要发现，通常也暴露外推边界和未来工作。

### 8.3 段落功能样例

| 段落来源 | 功能 | 推进方式 | 可学习点 |
| --- | --- | --- | --- |
| Introduction 前段 | 背景/重要性 | 从工程必要性进入研究对象 | 先建立“为什么要研究” |
| Introduction 文献段 | 文献分类/gap | 用 however/limited/remain 等转折缩小问题 | gap 要和后文方法一一对应 |
| Method 开头 | 方法总览 | 先给框架，再拆步骤 | 降低复杂方法的阅读成本 |
| Results 开头 | 验证设置 | 说明对比对象和指标 | 让审稿人知道证据如何支撑 claim |
| Conclusion | 主张回收 | 用编号或并列句总结贡献 | 不新增未验证 claim |

### 8.4 词频、词类、短语与语态

- 高频词：mathrm(611)；pmb(192)；left(108)；right(108)；p-box(100)；array(84)；big(73)；fig(58)；tag(54)；presented(53)；sigma(50)；bounds(47)；mean(47)；follows(45)；end(43)；begin(42)；processes(40)；nonlinear(39)；denotes(38)；cdf(38)
- 高频学术名词/术语：variance(26)；dynamics(24)；section(16)；information(14)；assumption(14)；probability(13)；interpolation(13)；approximation(11)；propagation(10)；realization(10)；covariance(9)；procedure(9)；subsection(9)；reference(9)；function(8)
- 高频学术动词：presented(53)；obtained(17)；introduced(7)；obtain(7)；investigated(6)；developed(6)；constructed(6)；evaluate(3)；compared(3)；demonstrate(2)；evaluated(2)；demonstrated(2)；validated(1)
- 高频形容词：interval(27)；probabilistic(15)；parametric(14)；stochastic(11)；basic(11)；relative(11)；leqslant(10)；table(10)；instant(9)；equal(9)；dynamic(8)；practical(8)；dynamical(7)；possible(7)；dimensional(7)
- 高频副词：respectively(27)；subsequently(5)；mathematically(5)；significantly(4)；finally(4)；accordingly(4)；efficiently(4)；generally(3)；recently(3)；easily(3)；usually(3)；widely(2)
- 高频二词短语：mathrm mathrm(166)；pmb mathrm(72)；mathrm pmb(43)；begin array(42)；end array(42)；pmb pmb(42)；mathrm right(36)；p-box processes(34)；mathrm big(33)；mathrm left(31)；left mathrm(29)；big mathrm(27)；right mathrm(27)；right tag(26)；left begin(25)
- 高频三词短语：mathrm mathrm mathrm(53)；pmb mathrm pmb(33)；mathrm pmb mathrm(28)；left begin array(25)；end array right(25)；array right tag(21)；begin array mathrm(17)；mathrm big mathrm(16)；mathrm end array(15)；mathrm quad mathrm(15)；pmb pmb pmb(14)；left mathrm mathrm(13)
- 被动语态估计：213
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：257
- 一般过去时线索：488
- 现在完成时线索：3
- 情态动词线索：68

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Peer review under responsibility of Editorial Committee of CJA. reference solutions based on the Monte Carlo method, with relative errors of less than 3%, the pro- posed method requires less than 0.2% calculation time.
  - 可迁移句型：{object} review under responsibility of Editorial Committee of CJA. reference solutions based on the Monte Carlo method, with relative errors of less than 3%, the pro- posed method requires less than 0.2% calculation time.
- 原句：The dynamic response evaluation of nonlinear systems is critical in most engineering problems.
  - 可迁移句型：{object} dynamic response evaluation of nonlinear systems is critical in most engineering problems.
- 原句：Specifically, several multi-objective problems need to be solved and can be expressed as follows: $$\begin{array}{c} \left\{\begin{array} {c} \displaystyle {\begin{array} {c} {{\mathrm{min}} \quad {\mathrm{[mean} ( F _ {W _ {m}} ) , \mathrm{var} ( F _ {W _ {m}} ) ]} \\ {F _ {s} \in F _ {W _ {m}} ^ {1}} \\ {{\mathrm{min}} \quad {\mathrm{[-mean} ( F _ {W _ {m}} ) , \mathrm{var} ( F _ {W _ {m}} ) ]} \end{array}}}} \\ {{\displaystyle {\begin{array} {c} {{\mathrm{min}} \quad {\mathrm{[mean} ( F _ {W _ {m}} ) , \mathrm{-var} ( F _ {W _ {m}} ) ]}} \\ {{\mathrm{~}}} \\ {{\mathrm{~}}} \\ {{\mathrm{~} \mathrm {f _ {s}} \in F _ {W _ {m}} ^ {1}}} \end{array}}} \\ {{\displaystyle {\mathrm{min}} \quad {\mathrm{[-mean} ( F _ {W _ {m}} ) , \mathrm{-var} ( F _ {W _ {m}} ) ]}}} \\ {{\displaystyle {\mathrm {f _ {s}} \in F _ {W _ {m}} ^ {1}} \quad {\mathrm{[-mean} ( F _ {W _ {m}} ) , \mathrm{-var} ( F _ {W _ {m}} ) ]}}} \\ {{\mathrm{~}}} \\ {{\mathrm{~} \mathrm{~} {\quad} \mathrm{~} {\quad} \mathrm{~} {\quad} \mathrm{~} {\quad} \mathrm{~} {\quad} \mathrm{~} {\quad} \mathrm{~} {\quad} \mathrm{~} {\quad} \mathrm{~} {\quad} \mathrm{~} {\quad} \mathrm{~}} \\ {{\mathrm{~}}} \\ {{\mathrm{~}}} \\ {{\mathrm{~}} \quad {\mathrm{~} \mathrm{~s.t.} \quad {\mathrm{~}} C F _ {s} \leqslant {\bf 0}}} \end{array}}} \end{array} \right.\tag{24}$$ The non-dominated solutions of these multi-objective problems will form the boundary of the 2-dimensional domain of mean and variance for a P-box.
  - 可迁移句型：{object}, several multi-objective problems need to be solved and can be expressed as follows: $$\begin{array}{c} \left\{\begin{array} {c} \displaystyle {\begin{array} {c} {{\mathrm{min}} \quad {\mathrm{[mean} ( F _ {W _ {m}} ) , \mathrm{var} ( F _ {W _ {m}} ) 
### gap/转折句
- 原句：However, its application to nonlinear systems remains limited due to excessive computation.
  - 可迁移句型：{object}, its application to nonlinear systems remains limited due to excessive computation.
- 原句：The proposed method is validated based on test cases, including a duffing oscillator, a vehicle ride, and an engineering black-box problem of launch vehicle trajectory.
  - 可迁移句型：{object} proposed method is validated based on test cases, including a duffing oscillator, a vehicle ride, and an engineering black-box problem of launch vehicle trajectory.
- 原句：The proposed method also possesses the ability to handle complex black-box problems. �2024 Production and hosting by Elsevier Ltd. on behalf of Chinese Society of Aeronautics and Astronautics.
  - 可迁移句型：{object} proposed method also possesses the ability to handle complex black-box problems. �2024 Production and hosting by Elsevier Ltd. on behalf of Chinese Society of Aeronautics and Astronautics.
- 原句：However, the uncertainties resulting from limited or poor-quality data, termed imprecision (a form of epistemic uncertainties), have to be represented by non-probabilistic models.3 When aleatory uncertainties and imprecision appear together and result in imprecise probabilistic information, both probabilistic and non-probabilistic models are inapplicable.
  - 可迁移句型：{object}, the uncertainties resulting from limited or poor-quality data, termed imprecision (a form of epistemic uncertainties), have to be represented by non-probabilistic models.3 When aleatory uncertainties and imprecision appear together and result in impr
### 方法提出句
- 原句：The distribution-free P-box process serves as an effective quantification model for time- varying uncertainties in dynamical systems when only imprecise probabilistic information is avail- able.
  - 可迁移句型：{object} distribution-free P-box process serves as an effective quantification model for time- varying uncertainties in dynamical systems when only imprecise probabilistic information is avail- able.
- 原句：This work develops an efficient method for propagating distribution-free P-box processes in nonlin- ear dynamics.
  - 可迁移句型：{object} study develops an efficient method for propagating distribution-free P-box processes in nonlin- ear dynamics.
- 原句：Moreover, the Chebyshev method is introduced and modified to efficiently solve the interval ODEs.
  - 可迁移句型：{object}, the Chebyshev method is introduced and modified to efficiently solve the interval ODEs.
- 原句：The proposed method is validated based on test cases, including a duffing oscillator, a vehicle ride, and an engineering black-box problem of launch vehicle trajectory.
  - 可迁移句型：{object} proposed method is validated based on test cases, including a duffing oscillator, a vehicle ride, and an engineering black-box problem of launch vehicle trajectory.
### 结果证明句
- 原句：Although these probabilistic methods have achieved success in solving various UP problems, they still face the challenge that collecting sufficient information for constructing precise probability distributions of uncertainties may not always be possible.
  - 可迁移句型：{object} these probabilistic methods have achieved success in solving various UP problems, they still face the challenge that collecting sufficient information for constructing precise probability distributions of uncertainties may not always be possible.
- 原句：The calculation of error bars shows that compared to the reference solutions, the relative errors of the proposed method are typically less than 1%.
  - 可迁移句型：{object} calculation of error bars shows that compared to the reference solutions, the relative errors of the proposed method are typically less than 1%.
- 原句：The evaluation of CDF bounds shows that the proposed method reaches the relative errors of less than 3%.
  - 可迁移句型：{object} evaluation of CDF bounds shows that the proposed method reaches the relative errors of less than 3%.
- 原句：22 Results of launch-vehicle trajectory analysis of $V _ {z} ^ {\mathbf {P .
  - 可迁移句型：22 {object} of launch-vehicle trajectory analysis of $V _ {z} ^ {\mathbf {P .
### 贡献收束句
- 原句：These equations provide the Mean-and-Covariance (MAC) bounds of the system responses in relation to the MAC bounds of P-box-process excitations.
  - 可迁移句型：{object} equations provide the Mean-and-Covariance (MAC) bounds of the system responses in relation to the MAC bounds of P-box-process excitations.
- 原句：Then, Li et al.32 proposed a sparse regression method to improve the efficiency of the Chebyshev method.
  - 可迁移句型：{object}, Li et al.32 proposed a sparse regression method to improve the efficiency of the Chebyshev method.
- 原句：As a result, a large portion of the computational cost is significantly reduced.
  - 可迁移句型：{object} a result, a large portion of the computational cost is significantly reduced.
### 边界/谨慎句
- 原句：The distribution-free P-box process serves as an effective quantification model for time- varying uncertainties in dynamical systems when only imprecise probabilistic information is avail- able.
  - 可迁移句型：{object} distribution-free P-box process serves as an effective quantification model for time- varying uncertainties in dynamical systems when only imprecise probabilistic information is avail- able.
- 原句：However, its application to nonlinear systems remains limited due to excessive computation.
  - 可迁移句型：{object}, its application to nonlinear systems remains limited due to excessive computation.
- 原句：However, the uncertainties resulting from limited or poor-quality data, termed imprecision (a form of epistemic uncertainties), have to be represented by non-probabilistic models.3 When aleatory uncertainties and imprecision appear together and result in imprecise probabilistic information, both probabilistic and non-probabilistic models are inapplicable.
  - 可迁移句型：{object}, the uncertainties resulting from limited or poor-quality data, termed imprecision (a form of epistemic uncertainties), have to be represented by non-probabilistic models.3 When aleatory uncertainties and imprecision appear together and result in impr
- 原句：Although these probabilistic methods have achieved success in solving various UP problems, they still face the challenge that collecting sufficient information for constructing precise probability distributions of uncertainties may not always be possible.
  - 可迁移句型：{object} these probabilistic methods have achieved success in solving various UP problems, they still face the challenge that collecting sufficient information for constructing precise probability distributions of uncertainties may not always be possible.

## 9. 引用风险层

- 正文引用簇估计：1
- 参考文献条数：64
- 可识别年份条目数：63
- 2021 年及以后参考文献数：23
- 2010 年以前经典文献数：10
- 高频来源粗略识别：Mech Syst Signal Process(12)；J Guid Contr Dyn(4)；Appl Math Model(4)；Nonlinear Dyn(4)；Probab Eng Mech(3)；J Eng Mech(2)；Comput Struct(2)；Reliab Eng Syst Saf(2)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- 1. Parameters of the dynamic model for launch- vehicle trajectory. J 1:624 �10�3 xex (rad /s) 7:292 �10�5 xey (rad /s) 0 xez (rad /s) 0
- 1. Luo YZ, Yang Z. A review of uncertainty propagation in orbital mechanics. Prog Aerosp Sci 2017;89:23–39.
- 2. Fu C, Sinou JJ, Zhu WD, et al. A state-of-the-art review on uncertainty analysis of rotor systems. Mech Syst Signal Process 2023;183:109619.
- 3. Faes M, Moens D. Recent trends in the modeling and quantification of non-probabilistic uncertainty. Arch Comput Meth Eng 2020;27(3):633–71.
- 4. Beer M, Ferson S, Kreinovich V. Imprecise probabilities in engineering analyses. Mech Syst Signal Process 2013;37(1– 2):4–29.
- 5. Shinozuka M. Monte Carlo solution of structural dynamics. Comput Struct 1972;2(5–6):855–74.
- 6. Geller DK. Linear covariance techniques for orbital rendezvous analysis and autonomous onboard mission planning. J Guid Contr Dyn 2006;29(6):1404–14.
- 7. Roberts J, Spanos P. Random vibration and statistical linearization. New York: Courier Corporation; 1990.
- 8. Dos Santos KRM, Kougioumtzoglou IA, Spanos PD. Hilbert transform–based stochastic averaging technique for determining the survival probability of nonlinear oscillators. J Eng Mech 2019;145(10):4019079.
- 9. Kougioumtzoglou IA, Spanos PD. Response and first-passage statistics of nonlinear oscillators via a numerical path integral approach. J Eng Mech 2013;139(9):1207–17.
- 10. Zhu WQ. Nonlinear stochastic dynamics and control in Hamiltonian formulation. Appl Mech Rev 2006;59(4):230–48.
- 11. Li J. Probability density evolution method: background, significance and recent developments. Probab Eng Mech 2016;44:111–7.
- 12. Chen GH, Yang DX. A unified analysis framework of static and dynamic structural reliabilities based on direct probability integral method. Mech Syst Signal Process 2021;158:107783.
- 13. Chen HS, Chen GH, Meng Z, et al. Stochastic dynamic analysis of nonlinear MDOF systems under combined Gaussian and Poisson noise excitation based on DPIM. Mech Syst Signal Process 2022;176:109163.
- 14. Prabhakar A, Fisher J, Bhattacharya R. Polynomial chaos-based analysis of probabilistic uncertainty in hypersonic flight dynamics. J Guid Contr Dyn 2010;33(1):222–34.

### 9.2 审稿风险清单

| 风险 | 具体表现 | 严重度 | 应对方式 |
| --- | --- | --- | --- |
| gap 风险 | gap 若只靠泛化措辞而非最近文献支撑，会显得不够真实 | P1 | 增补最近五年最接近工作并公平比较 |
| 方法必要性 | 若简单 baseline 已可解决问题，新模型复杂度会被质疑 | P1 | 加入消融、复杂度收益和边界条件说明 |
| 证据外推 | 单一算例/样本/轨迹/材料体系支撑大 claim | P1 | 扩展工况或明确适用边界 |
| 图表可读性 | 文本抽取无法确认图像细节 | P2 | 回看 PDF 图像、坐标轴、误差条和图例 |
| 公式/符号 | 公式抽取可能低置信或符号缺失 | P2 | 按 PDF 逐式核查变量定义 |

## 10. 复用层

- 可复用选题角度：把复杂工程/物理问题转化为“效率、精度、可靠性、性能或可解释性”的可验证改进。
- 可复用 gap 表达：已有方法在高保真、低成本、跨工况、耦合机制或工程适用性之间存在张力。
- 可复用贡献表达：提出/构建一个面向具体对象的模型或实验框架，并通过对比验证其精度、效率或性能收益。
- 可复用论证链：问题重要性 -> 文献分类 -> 明确 gap -> 方法设计 -> 验证设置 -> 图表证据 -> 结论回收。
- 可复用图表设计：先给对象/框架示意图，再给流程图/参数表，最后给对比结果、误差和敏感性图。
- 不可直接模仿：具体数据、实验平台、材料体系、仿真模型、团队资源和未公开代码。
- 迁移到自己论文的三件事：
  1. 让 Introduction 的 gap 与 Method 的输入输出一一对应；
  2. 让每个强 claim 至少对应一个图表、一个指标和一个对比对象；
  3. 在 Conclusion 中只回收已验证内容，主动标注适用边界。

## 11. 质量自检

- 模式：精细拆解
- 对象：单篇论文
- 样本边界是否清晰：是
- 十层字段是否覆盖：是
- Claim-Evidence 是否完成：是，基于自动抽取的强 claim 候选和图表/公式/参考文献证据
- 图表功能是否解释：是，但图像细节需 PDF 核查
- 引用策略是否解释：是
- 风险是否具体：是
- 可复用资产是否具体：是
- 不确定项：公式符号、图像细节、部分图表标题和真实段落位置仍需 PDF 视觉核查
- 下一步建议：若要用于正式写作模仿，应人工复核 PDF 中关键图、公式和 Introduction 文献转折段。
