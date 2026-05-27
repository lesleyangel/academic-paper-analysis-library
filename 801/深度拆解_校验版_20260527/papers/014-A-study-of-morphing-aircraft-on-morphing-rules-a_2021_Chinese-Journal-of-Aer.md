# 论文深度拆解：014-A-study-of-morphing-aircraft-on-morphing-rules-a_2021_Chinese-Journal-of-Aer

> 生成依据：`801/cleantext/014-A-study-of-morphing-aircraft-on-morphing-rules-a_2021_Chinese-Journal-of-Aer`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`014-A-study-of-morphing-aircraft-on-morphing-rules-a_2021_Chinese-Journal-of-Aer`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\A-study-of-morphing-aircraft-on-morphing-rules-a_2021_Chinese-Journal-of-Aer.pdf`
- 页数：12
- clean body 字符数：29803
- 摘要字符数：2120
- 参考文献条数：42
- 图题数：0
- 表题数：0
- 表格文件数：6
- 公式候选数：42
- 提取质量分：0.93
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "7 formula(s) need manual review."}]

## 1. 身份层

- 标题：014-A-study-of-morphing-aircraft-on-morphing-rules-a_2021_Chinese-Journal-of-Aer
- 年份：2021
- 期刊/来源：Chinese Journal of Aer
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：实验/测量 + 性能分析型
- 研究对象：Morphing aircraft can meet requirements of multi-mission during the whole flight due to changingthe aerodynamic shape,soit isnecessary tostudyits morphingrules along the trajectory.How- ever, trajectory planning considering morphing variables requires a huge number of expensive CFD computations due to the morphing in view of aerodynamic performance. For simple and less-constrained problems, the RPM can quickly obtain the ideal solution; but for complex problems, the RPM needs higher-dimensional 
- 主要方法：Under the given missions and trajectory, to alleviate computational cost and improve trajectory-planning efficiency for morphing aircraft, an offline optimization method is proposed based on Multi-Fidelity Kriging (MFK) modeling. The angle of attack, Mach number, sweep angle and axial position of the morphing wing are defined as variables for generating training data for building the MFK models, in which many inviscid aerody- namic solutions are used as low-fidelity data, while the less high-fidelity data are obtained by solving vis- cous flow. Then the built MFK models of the lift, drag and pressure centre at the different angles of attack and Mach numbers are used to predict the aerodynami
- 主要证据：图表 0 个标题、公式 42 个候选、参考文献 42 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“Morphing aircraft can meet requirements of multi-mission during the whole flight due to changingthe aerodynamic shape,soit isnecessary tostudyits morphingrules along the trajectory”，可以通过“Under the given missions and trajectory, to alleviate computational cost and improve trajectory-planning efficiency for morphing aircraft, an offline optimization method is proposed based on Multi-Fidelity Kriging (MFK) ”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：Under the given missions and trajectory, to alleviate computational cost and improve trajectory-planning efficiency for morphing aircraft, an offline optimization method is proposed based on Multi-Fidelity Kriging (MFK) modeling. The results indicate that a complex trajectory can take advantage of morphing rules in keeping good aerodynamic performance, and the proposed method is more efficient than trajectory optimization by reducing 86% of the computing time. �2020 Chinese Society of Aeronautics and Astronautics. 7 presented the results obtained from the numerical simulations and experimental wind tunnel tests of a morphing wing, which can benefit the research of morphing rules.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：Morphing aircraft can meet requirements of multi-mission during the whole flight due to changingthe aerodynamic shape,soit isnecessary tostudyits morphingrules along the trajectory.How- ever, trajectory planning considering morphing variables requires a huge number of expensive CFD computations due to the morphing in view of aerodynamic performance. For simple and less-constrained problems, the RPM can quickly obtain the ideal solution; but for complex problems, the RPM needs higher-dimensional interpolation polynomials to obtain an approximate solution. During trajectory planning, aerodynamic forces need to be computed to provide inputs for solving trajectory equations iteratively.
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
- 作者声明或文本中可见 gap：Zhang et al. and Chen et al. studied the aerodynamic characteristics of the morphing swept wing and the variable span wing, and proposed a method to improve the lift and drag characteristics of the missile during the flight,11–13 but the trajectory was not considered in their study. The greatest difficulty is that the change of the sweep angle and/or the position of the wing make(s) the dynamic design of the flight and the trajectory characteristics of aircraft more complicated, especially for studying morphing rules along the trajectory.14 To obtain the morphing rules along the trajectory of a morphing aircraft, trajectory optimization is commonly used,15 which can be classified as indirect methods and direct methods.16,17 The indirect methods are sensitive to the initial value, which make the problem difficult to solve. However, like other global optimization algorithms, the PSO has low convergence accuracy and slow convergence rate.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- 未在 Introduction 中稳定识别“带引用的 gap 句”，建议人工复核文献转折段。

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：Under the given missions and trajectory, to alleviate computational cost and improve trajectory-planning efficiency for morphing aircraft, an offline optimization method is proposed based on Multi-Fidelity Kriging (MFK) modeling. The angle of attack, Mach number, sweep angle and axial position of the morphing wing are defined as variables for generating training data for building the MFK models, in which many inviscid aerody- namic solutions are used as low-fidelity data, while the less high-fidelity data are obtained by solving vis- cous flow. Then the built MFK models of the lift, drag and pressure centre at the different angles of attack and Mach numbers are used to predict the aerodynamic performance of the morphing aircraft, which keeps the optimal sweep angle and axial position of the wing during trajectory planning.
- 我判断的真实贡献：把一个具体工程/物理/材料问题转化为可计算、可验证的模型或实验流程，并通过结果图表证明其在效率、精度、可靠性、性能或解释力上的增量。
- 创新类型：实验/测量 + 性能分析型；偏方法/模型/工程应用/实验证据/集成框架之一。
- 创新强度：中等到较强，取决于是否具备清晰 baseline、跨工况验证和误差/性能指标。
- 可能被挑战处：
  - 是否充分比较最接近方法；
  - 训练/实验/仿真工况是否覆盖真实应用；
  - 参数、边界条件和材料/结构假设是否可复现；
  - 结论是否超出证据支持范围。

## 6. 方法层

- 方法目标：用可复现的模型、实验或计算流程回答选题层问题。
- 方法类型：实验/测量 + 性能分析型
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
| Under the given missions and trajectory, to alleviate computational cost and improve trajectory-planning efficiency for morphing aircraft, an offline optimization method is proposed based on Multi-Fidelity Kriging (MFK) modeling. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (53.8, 33.39, 243.16, 41.44)]] Chinese Journal of Aeronautics, (2021), | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The results indicate that a complex trajectory can take advantage of morphing rules in keeping good aerodynamic performance, and the proposed method is more efficient than trajectory optimization by reducing 86% of the computing time. �2020 Chinese Society of  | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (53.8, 655.43, 276.23, 686.19)]] * Corresponding author. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| 7 presented the results obtained from the numerical simulations and experimental wind tunnel tests of a morphing wing, which can benefit the research of morphing rules. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (53.8, 33.39, 243.16, 41.44)]] Chinese Journal of Aeronautics, (2021), | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Zhang et al. and Chen et al. studied the aerodynamic characteristics of the morphing swept wing and the variable span wing, and proposed a method to improve the lift and drag characteristics of the missile during the flight,11–13 but the trajectory was not con | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (53.8, 655.43, 276.23, 686.19)]] * Corresponding author. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| To further improve the efficiency for trajectory planning, many inviscid aerodynamic simulations are performed to obtain lowfidelity data, and few viscous solutions are obtained as highfidelity data. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (53.8, 33.39, 243.16, 41.44)]] Chinese Journal of Aeronautics, (2021), | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| This model is cheap to be built by using quite few highfidelity data, and shows small approximation error. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (53.8, 655.43, 276.23, 686.19)]] * Corresponding author. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (53.8, 33.39, 243.16, 41.44)]] Chinese Journal of Aeronautics, (2021), 34(7): 232-243 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (53.8, 655.43, 276.23, 686.19)]] * Corresponding author. E-mail address: Leo | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (46.83, 122.54, 54.76, 155.21)]] 8 > > > > > > < | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (46.83, 162.29, 54.76, 186.9)]] > > > > > > : | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.62; needs_review; source=equations; [page 6, bbox (232.95, 612.19, 529.15, 621.95)]] a = 0� a = 2� a = 4� a = 6� a = 8� | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.62; needs_review; source=equations; [page 7, bbox (252.96, 87.84, 544.57, 97.6)]] a = 0� a = 2� a = 4� a = 6� a = 8� | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 7, bbox (123.48, 292.34, 544.58, 300.33)]] Ma = 0.35 Ma = 0.5 Ma = 0.65 Ma = 0.8 Ma = 0.95 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 8, bbox (123.59, 89.6, 536.14, 97.6)]] Ma = 0.35 Ma = 0.5 Ma = 0.65 Ma = 0.8 Ma = 0.95 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> Morphing aircraft can meet requirements of multi-mission during the whole flight due to changingthe aerodynamic shape,soit isnecessary tostudyits morphingrules along the trajectory.How- ever, trajectory planning considering morphing variables requires a huge number of expensive CFD computations due to the morphing in view of aerodynamic performance. Under the given missions and trajectory, to alleviate computational cost and improve trajectory-planning efficiency for morphing aircraft, an offline optimization method is proposed based on Multi-Fidelity Kriging (MFK) modeling. The angle of attack, Mach number, sweep angle and axial position of the morphing wing are defined as variables for generating training data for building the MFK models, in which many inviscid aerody- namic solutions are used as low-fidelity data, while the less high-fidelity data are obtained by solving vis- cous flow. Then the built MFK models of the lift, drag and pressure centre at the different angles of attack and Mach numbers are used to predict the aerodynamic performance of the morphing aircraft, which keeps the optimal sweep angle and axial position of the wing during trajectory planning. Hence, the morphing rules can becorrespondinglyacquiredalong the trajectory, as well as keepthe aircraft with the bestaerodynamic performanceduringthe wholetask. The trajectoryplanningofamorphingaircraft was performed with the optimal aerodynamic performance based on the MFK models, built by only using 240 low-fidelity data and 110 high-fidelity data. The results indicate that a complex trajectory can take advantage of morphing rules in keeping good aerodynamic performance, and the proposed method is more efficient than trajectory optimization by reducing 86% of the computing time. �2020 Chinese Society of Aeronautics and Astronautics. Production and hosting by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).
> * Corresponding author. E-mail address: Leonwood@nwpu.edu.cn (C. GONG). Peer review under responsibility of Editorial Committee of CJA.

### 7.4 摘要中文翻译

> 变形飞机由于气动形状的改变，可以满足整个飞行过程中的多任务要求，因此有必要研究其沿轨迹的变形规则。然而，由于考虑气动性能的变形，考虑变形变量的轨迹规划需要大量昂贵的CFD计算。在给定的任务和轨迹下，为了降低变形飞行器的计算成本并提高轨迹规划效率，提出了一种基于多保真克里金（MFK）建模的离线优化方法。定义攻角、马赫数、后掠角和变形机翼的轴向位置作为生成训练数据的变量，用于构建MFK模型，其中许多无粘性空气动力学解被用作低保真度数据，而较少的高保真度数据则通过求解粘性流获得。然后利用建立的不同迎角和马赫数下的升力、阻力和压力中心的MFK模型来预测变形飞机的气动性能，从而在轨迹规划时保持机翼的最佳后掠角和轴向位置。因此，可以沿着轨迹相应地获取变形规则，并使飞机在整个任务过程中保持最佳的气动性能。仅使用240个低保真数据和110个高保真数据建立的MFK模型，以最佳气动性能对变形飞机进行轨迹规划。
> 
> 结果表明，复杂的轨迹可以利用变形规则来保持良好的气动性能，并且该方法比轨迹优化更有效，减少了 86% 的计算时间。 �2020 中国航空学会。由 Elsevier Ltd 制作和托管。这是一篇遵循 CC BY-NC-ND 许可证 (http://creativecommons.org/licenses/by-nc-nd/4.0/) 的开放获取文章。 * 通讯作者。电子邮箱地址：Leonwood@nwpu.edu.cn（C.同行评审由CJA编委会负责。

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusions

> To avoid huge computational cost and improve the efficiency for studying morphing rules of a morphing aircraft along the trajectory, a method based on the MFK model is proposed. The flight states need to be specially chosen within the range of velocity and angle of attack, for which surrogates need to be built to obtain optimum shapes. Attention needs to be paid for the limitations of the morphing ranges, when selecting morphing shapes for computing low- and high-fidelity data. The MFK models are proved to be accurate for predicting aerodynamic performance by the leave-one-out cross validations. The results for studying the morphing rules of the aircraft which can change its sweep angle and axial position of the wing indicate:
> 
> (1) The computational cost can be greatly reduced by using the MFK model in comparison with traditional trajectory planning by reducing 86% of the computing time.
> 
> (2) The morphing of the aircraft along the trajectory is monotonous in each task stage, which demonstrates that morphing rules are suitable for structure organization.
> 
> (3) The proposed method provides a potentially-efficient way for studying morphing rules along trajectory of morphing aircraft.
> 
> MFK model is proposed to study the morphing rules of morphing aircraft. However, the morphing parts of the aircraft are mainly the wings, and there are not many variables involved. Since the proposed method is based on the MFK model, even with more morphing variables, the data increment needed for building the MFK models is more less than trajectory optimization. Thus, in the future, the morphing of the whole aircraft can be considered and the morphing parameters of the aircraft can be more for further study. Moreover, only one kind of the multi-fidelity model, MFK, is used in this paper, so other multi-fidelity models, such as the multifidelity model based on Radial Basis Function (RBF), can be studied and compared in the future.

### 7.6 结论中文翻译

> 为了避免巨大的计算成本并提高研究变形飞行器沿轨迹的变形规则的效率，提出了一种基于MFK模型的方法。需要在速度和攻角范围内专门选择飞行状态，为此需要构建代理以获得最佳形状。 Attention needs to be paid for the limitations of the morphing ranges, when selecting morphing shapes for computing low- and high-fidelity data. The MFK models are proved to be accurate for predicting aerodynamic performance by the leave-one-out cross validations.研究可改变后掠角和机翼轴向位置的飞行器变形规律的结果表明：（1）与传统的轨迹规划相比，使用MFK模型可以大大降低计算成本，减少86%的计算时间。 (2) 飞行器沿轨迹的变形在每个任务阶段都是单调的，这表明变形规则适合结构组织。 (3)该方法为研究变形飞机沿轨迹的变形规则提供了一种潜在有效的方法。 MFK model is proposed to study the morphing rules of morphing aircraft. However, the morphing parts of the aircraft are mainly the wings, and there are not many variables involved.由于该方法基于MFK模型，即使有更多的变形变量，构建MFK模型所需的数据增量也比轨迹优化少。因此，未来可以考虑整个飞行器的变形，对飞行器的变形参数进行更多的研究。
> 
> 而且，本文只使用了一种多保真模型MFK，因此以后可以对其他多保真模型，例如基于径向基函数（RBF）的多保真模型进行研究和比较。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 4214 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. Problem description | 对象/条件/子问题展开 | 2570 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 3.1. Method of studying morphing rules along trajectory | 方法建构 | 2043 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 3.2. Dynamic model | 方法建构 | 1511 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 5 | 3.3. Multi-fidelity Kriging model | 方法建构 | 2697 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 6 | 3.4. Leave-one-out cross validation | 对象/条件/子问题展开 | 1762 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 3.5. Morphing shape optimization in different flight states | 对象/条件/子问题展开 | 1434 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 4.1. Results of aerodynamic performance simulation | 结果验证/讨论 | 1255 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 9 | 4.2. Results of MFK modeling | 方法建构 | 1848 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 10 | 4.3. Results of optimization | 结果验证/讨论 | 871 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 11 | 4.4. Morphing rules along trajectory | 对象/条件/子问题展开 | 863 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | (1) Acceleration and climbing stage | 对象/条件/子问题展开 | 1034 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | (2) Deceleration and descent stage | 对象/条件/子问题展开 | 866 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | (3) Acceleration and descent stage | 对象/条件/子问题展开 | 4251 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 15 | 5. Conclusions | 主张回收/边界说明 | 1940 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |

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

- 高频词：morphing(61)；mathrm(59)；trajectory(55)；aircraft(49)；wing(45)；angle(39)；fig(34)；sweep(32)；data(28)；flight(26)；stage(25)；position(24)；aerodynamic(24)；rules(24)；mfk(24)；low(21)；axial(21)；optimization(18)；planning(17)；velocity(17)
- 高频学术名词/术语：position(24)；optimization(18)；velocity(17)；high-fidelity(16)；acceleration(15)；performance(11)；pressure(8)；low-fidelity(8)；limitation(8)；deceleration(7)；validation(7)；characteristics(5)；interpolation(5)；multi-fidelity(5)；function(5)
- 高频学术动词：obtain(12)；obtained(6)；presented(3)；compared(2)；predicted(2)；evaluate(2)；investigated(1)；introduced(1)；construct(1)；indicate(1)
- 高频形容词：aerodynamic(24)；axial(21)；descent(14)；table(12)；computational(7)；initial(6)；optimal(6)；leqslant(6)；coefficient(6)；longitudinal(5)；pseudo-spectral(4)；viscous(4)；obvious(4)；experimental(3)；dynamic(3)
- 高频副词：respectively(11)；accordingly(5)；finally(3)；directly(3)；greatly(3)；totally(3)；commonly(2)；sharply(2)；usually(2)；specially(2)；actively(1)；especially(1)
- 高频二词短语：sweep angle(31)；morphing rules(24)；axial position(20)；position wing(18)；morphing aircraft(15)；trajectory planning(14)；mathrm low(13)；angle axial(12)；high-fidelity data(11)；mathrm mathrm(11)；descent stage(10)；aerodynamic performance(9)；along trajectory(9)；trajectory optimization(9)；studying morphing(8)
- 高频三词短语：axial position wing(16)；sweep angle axial(12)；angle axial position(12)；studying morphing rules(8)；morphing rules along(7)；rules along trajectory(7)；acceleration descent stage(6)；mathrm low mathrm(5)；acceleration climbing stage(5)；change sweep angle(4)；morphing rules morphing(4)；rules morphing aircraft(4)
- 被动语态估计：76
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：178
- 一般过去时线索：161
- 现在完成时线索：0
- 情态动词线索：55

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Morphing aircraft can meet requirements of multi-mission during the whole flight due to changingthe aerodynamic shape,soit isnecessary tostudyits morphingrules along the trajectory.How- ever, trajectory planning considering morphing variables requires a huge number of expensive CFD computations due to the morphing in view of aerodynamic performance.
  - 可迁移句型：{object} aircraft can meet requirements of multi-mission during the whole flight due to changingthe aerodynamic shape,soit isnecessary tostudyits morphingrules along the trajectory.How- ever, trajectory planning considering morphing variables requires a huge n
- 原句：In the whole process, MFK modeling is the most critical step.
  - 可迁移句型：{object} the whole process, MFK modeling is the most critical step.
- 原句：Even by using surrogate models, many expensive viscous CFD analyses are still necessary.
  - 可迁移句型：{object} by using surrogate models, many expensive viscous CFD analyses are still necessary.
- 原句：The root-mean-square error and the relative root-meansquare error are used to evaluate model accuracy, the expressions of which are as follows: $$R _ {\mathrm{MSE}} = \sqrt {\frac {1} {l} \sum _ {i = 1} ^ {l} {( y _ {i} - \hat {y} _ {i} )} ^ {2}}\tag{ð5Þ}$$ $$R _ {\mathrm{RMSE}} = \frac {\sqrt {\frac {1} {l} \displaystyle \sum _ {i = 1} ^ {l} \left( y _ {i} - \hat {y} _ {i} \right) ^ {2}}} {y ^ -}\tag{ð6Þ}$$ in which l is the number of samples; $y _ {i}$ and $\hat {y} _ {i}$ are the true and predicted values, respectively; y- is the average of $y _ {i}$ To build the MFK models, flight states about the Mach number and the angle of attack should be specially chosen with respect to flight envelop.
  - 可迁移句型：{object} root-mean-square error and the relative root-meansquare error are used to evaluate model accuracy, the expressions of which are as follows: $$R _ {\mathrm{MSE}} = \sqrt {\frac {1} {l} \sum _ {i = 1} ^ {l} {( y _ {i} - \hat {y} _ {i} )} ^ {2}}\tag{ð5Þ}
### gap/转折句
- 原句：The greatest difficulty is that the change of the sweep angle and/or the position of the wing make(s) the dynamic design of the flight and the trajectory characteristics of aircraft more complicated, especially for studying morphing rules along the trajectory.14 To obtain the morphing rules along the trajectory of a morphing aircraft, trajectory optimization is commonly used,15 which can be classified as indirect methods and direct methods.16,17 The indirect methods are sensitive to the initial value, which make the problem difficult to solve.
  - 可迁移句型：{object} greatest difficulty is that the change of the sweep angle and/or the position of the wing make(s) the dynamic design of the flight and the trajectory characteristics of aircraft more complicated, especially for studying morphing rules along the trajec
- 原句：However, like other global optimization algorithms, the PSO has low convergence accuracy and slow convergence rate.
  - 可迁移句型：{object}, like other global optimization algorithms, the PSO has low convergence accuracy and slow convergence rate.
- 原句：However, for morphing aircraft, due to the morphing of the wing in its shape and position, a huge amount of CFD simulations are needed, which is unbearable.
  - 可迁移句型：{object}, for morphing aircraft, due to the morphing of the wing in its shape and position, a huge amount of CFD simulations are needed, which is unbearable.
- 原句：To further improve the efficiency for trajectory planning, many inviscid aerodynamic simulations are performed to obtain lowfidelity data, and few viscous solutions are obtained as highfidelity data.
  - 可迁移句型：{object} further improve the efficiency for trajectory planning, many inviscid aerodynamic simulations are performed to obtain lowfidelity data, and few viscous solutions are obtained as highfidelity data.
### 方法提出句
- 原句：Under the given missions and trajectory, to alleviate computational cost and improve trajectory-planning efficiency for morphing aircraft, an offline optimization method is proposed based on Multi-Fidelity Kriging (MFK) modeling.
  - 可迁移句型：{object} the given missions and trajectory, to alleviate computational cost and improve trajectory-planning efficiency for morphing aircraft, an offline optimization method is proposed based on Multi-Fidelity Kriging (MFK) modeling.
- 原句：The angle of attack, Mach number, sweep angle and axial position of the morphing wing are defined as variables for generating training data for building the MFK models, in which many inviscid aerody- namic solutions are used as low-fidelity data, while the less high-fidelity data are obtained by solving vis- cous flow.
  - 可迁移句型：{object} angle of attack, Mach number, sweep angle and axial position of the morphing wing are defined as variables for generating training data for building the MFK models, in which many inviscid aerody- namic solutions are used as low-fidelity data, while th
- 原句：Then the built MFK models of the lift, drag and pressure centre at the different angles of attack and Mach numbers are used to predict the aerodynamic performance of the morphing aircraft, which keeps the optimal sweep angle and axial position of the wing during trajectory planning.
  - 可迁移句型：{object} the built MFK models of the lift, drag and pressure centre at the different angles of attack and Mach numbers are used to predict the aerodynamic performance of the morphing aircraft, which keeps the optimal sweep angle and axial position of the wing 
- 原句：The trajectoryplanningofamorphingaircraft was performed with the optimal aerodynamic performance based on the MFK models, built by only using 240 low-fidelity data and 110 high-fidelity data.
  - 可迁移句型：{object} trajectoryplanningofamorphingaircraft was performed with the optimal aerodynamic performance based on the MFK models, built by only using 240 low-fidelity data and 110 high-fidelity data.
### 结果证明句
- 原句：The results indicate that a complex trajectory can take advantage of morphing rules in keeping good aerodynamic performance, and the proposed method is more efficient than trajectory optimization by reducing 86% of the computing time. �2020 Chinese Society of Aeronautics and Astronautics.
  - 可迁移句型：{object} results indicate that a complex trajectory can take advantage of morphing rules in keeping good aerodynamic performance, and the proposed method is more efficient than trajectory optimization by reducing 86% of the computing time. �2020 Chinese Societ
- 原句：7 presented the results obtained from the numerical simulations and experimental wind tunnel tests of a morphing wing, which can benefit the research of morphing rules.
  - 可迁移句型：7 presented the results obtained from the numerical simulations and experimental wind tunnel tests of a morphing wing, which can benefit the research of morphing rules.
- 原句：This model is cheap to be built by using quite few highfidelity data, and shows small approximation error.
  - 可迁移句型：{object} model is cheap to be built by using quite few highfidelity data, and shows small approximation error.
- 原句：4 shows the surface mesh of the aircraft, which is the unstructured mesh, and the size of the meshes on the head and wings is small.
  - 可迁移句型：4 shows the surface mesh of the aircraft, which is the unstructured mesh, and the size of the meshes on the head and wings is small.
### 贡献收束句
- 原句：Under the given missions and trajectory, to alleviate computational cost and improve trajectory-planning efficiency for morphing aircraft, an offline optimization method is proposed based on Multi-Fidelity Kriging (MFK) modeling.
  - 可迁移句型：{object} the given missions and trajectory, to alleviate computational cost and improve trajectory-planning efficiency for morphing aircraft, an offline optimization method is proposed based on Multi-Fidelity Kriging (MFK) modeling.
- 原句：Zhang et al. and Chen et al. studied the aerodynamic characteristics of the morphing swept wing and the variable span wing, and proposed a method to improve the lift and drag characteristics of the missile during the flight,11–13 but the trajectory was not considered in their study.
  - 可迁移句型：{object} et al. and Chen et al. studied the aerodynamic characteristics of the morphing swept wing and the variable span wing, and proposed a method to improve the lift and drag characteristics of the missile during the flight,11–13 but the trajectory was not 
- 原句：During trajectory planning, aerodynamic forces need to be computed to provide inputs for solving trajectory equations iteratively.
  - 可迁移句型：{object} trajectory planning, aerodynamic forces need to be computed to provide inputs for solving trajectory equations iteratively.
- 原句：To further improve the efficiency for trajectory planning, many inviscid aerodynamic simulations are performed to obtain lowfidelity data, and few viscous solutions are obtained as highfidelity data.
  - 可迁移句型：{object} further improve the efficiency for trajectory planning, many inviscid aerodynamic simulations are performed to obtain lowfidelity data, and few viscous solutions are obtained as highfidelity data.
### 边界/谨慎句
- 原句：The trajectoryplanningofamorphingaircraft was performed with the optimal aerodynamic performance based on the MFK models, built by only using 240 low-fidelity data and 110 high-fidelity data.
  - 可迁移句型：{object} trajectoryplanningofamorphingaircraft was performed with the optimal aerodynamic performance based on the MFK models, built by only using 240 low-fidelity data and 110 high-fidelity data.
- 原句：An aircraft with morphing wing can actively change the sweep angle and/or the position of the wing during flight,1–3 and the wing shape or the profile of the wing will change accordingly, so that the aircraft can maintain good aerodynamic performance during the whole trajectory under the given flight missions4 Compared with fixed-wing aircraft, morphing aircraft has many advantages, for example, it can adapt to a wide range of speed and airspacem5 NASA analyzed the morphing swept wing aircraft at transonic speed, and obtained the morphing rules of changing sweep angle,6 which only considered the aerodynamic characteristics.
  - 可迁移句型：{object} aircraft with morphing wing can actively change the sweep angle and/or the position of the wing during flight,1–3 and the wing shape or the profile of the wing will change accordingly, so that the aircraft can maintain good aerodynamic performance dur
- 原句：The greatest difficulty is that the change of the sweep angle and/or the position of the wing make(s) the dynamic design of the flight and the trajectory characteristics of aircraft more complicated, especially for studying morphing rules along the trajectory.14 To obtain the morphing rules along the trajectory of a morphing aircraft, trajectory optimization is commonly used,15 which can be classified as indirect methods and direct methods.16,17 The indirect methods are sensitive to the initial value, which make the problem difficult to solve.
  - 可迁移句型：{object} greatest difficulty is that the change of the sweep angle and/or the position of the wing make(s) the dynamic design of the flight and the trajectory characteristics of aircraft more complicated, especially for studying morphing rules along the trajec
- 原句：The shooting method only discretizes control variables and can obtain high precision solutions with less optimization parameters.
  - 可迁移句型：{object} shooting method only discretizes control variables and can obtain high precision solutions with less optimization parameters.

## 9. 引用风险层

- 正文引用簇估计：0
- 参考文献条数：42
- 可识别年份条目数：42
- 2021 年及以后参考文献数：0
- 2010 年以前经典文献数：6
- 高频来源粗略识别：Chin J Aeronaut(10)；J Ballist(2)；Flight Dynam(2)；Acta Aeronaut Astronaut Sin(2)；J Aerosp Sci Technol(1)；J Aircr(1)；Acta Armament(1)；Study of a variable sweep wing in sub or transonic flow(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- 1. Wang XG, Chen Q, Wang ZY. Multi-task trajectory design and simulation for long-range swing-wing cruise missile. J Ballist 2018; 30(3): 13–24 [Chinese].
- 2. Lyu JC, Dong YF, Chen YK. Rules of the optimal variable sweep wing in low and medium height. J Flight Dynam 2016; 32(2): 24–7 [Chinese].
- 3. Ajaj RM, Beaverstock CS, Friswell MI. Morphing aircraft: The need for a new design philosophy. J Aerosp Sci Technol 2016;49:154–66.
- 4. Weisshaar TA. Morphing aircraft systems: historical perspectives and future challenges. J Aircr 2013;50(2):337–53.
- 5. Yang GT, Tang SJ, Zhao LD, et al. Dynamic modeling and response of a morphing UAV with variable sweep and variable span. Acta Armament 2014; 35(1): 102–7 [Chinese].
- 6. Manie F, Rehbach C. Study of a variable sweep wing in sub or transonic flow. 11th international council of the aeronautical sciences; 1979.
- 7. Oliviu SG, Koreanschi A, Botez RM. A new non-linear vortex lattice method: Applications to wing aerodynamic optimizations. Chin J Aeronaut 2016;29(5):1178–95.
- 8. Koreanschi A, Gabor OS, Acotto J, et al. Optimization and design of an aircraft’s morphing wing-tip demonstrator for drag reduc- tion at low speed, Part I- Aerodynamic optimization using genetic, bee colony and gradient descent algorithms. Chin J Aeronaut 2017;30(1):149–63.
- 9. Koreanschi A, Gabor OS, Acotto J, et al. Optimization and design of an aircraft’s morphing wing-tip demonstrator for drag reduc- tion at low speeds, Part II- Experimental validation using Infra- Red transition measurement from wind tunnel tests. Chin J Aeronaut 2017;30(1):170–80.
- 10. Ren H, Zhiping Q. Transient aeroelastic responses and flutter analysis of a variable-span wing during the morphing process. Chin J Aeronaut 2013;26(6):81–9.
- 11. Zhang GP, Duan CY. Study on aerodynamic characteristics of tactical missile with morphing wings. Flight Dynam 2011; 29(1): 54–8 [Chinese].
- 12. Chen Q, Yin WL, Bai P. System design and characteristics analysis of a variable-sweep and variable-span wing-body. Acta Aeronaut Astronaut Sin 2010; 31(3): 506–13 [Chinese].
- 13. Chen YK, Dong YF, Peng JJ. Analysis for drag characteristic of variable swept wing-body. Flight Dynam 2014; 32(4): 308–11 [Chinese].
- 14. Huang MH, Tang QG, Zhang QB, et al. Morphing swept wing tactical missile conceptual design and optimization trajectory of hypersonic vehicle. Tact Missile Technol 2016; 5(2): 10–24 [Chinese]. (1) The computational cost can be greatly reduced by using the MFK model in comparison with traditional trajec- tory planning by reducing 86% of the computing time. (2) The morphing of the aircraft along the trajectory is monotonous in each task stage, which demonstrates that morphing rules are suitable
- 15. Yong EM, Chen L, Tang GJ. Review for numerical methods of spacecraft trajectory optimization. J Astronaut 2008; 29(2): 397– 406 [Chinese].

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
