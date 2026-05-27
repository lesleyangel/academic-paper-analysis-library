# 论文深度拆解：A sparse reconstruction method of physical field via multi-source sensors for flight vehicle

> 生成依据：`801/cleantext/011-A-sparse-reconstruction-method-of-physical-field-via_2025_Aerospace-Science`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`011-A-sparse-reconstruction-method-of-physical-field-via_2025_Aerospace-Science`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\A-sparse-reconstruction-method-of-physical-field-via_2025_Aerospace-Science-.pdf`
- 页数：13
- clean body 字符数：42099
- 摘要字符数：1812
- 参考文献条数：47
- 图题数：22
- 表题数：1
- 表格文件数：5
- 公式候选数：134
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "low_confidence_formulas", "severity": "medium", "message": "20 formula(s) need manual review."}]

## 1. 身份层

- 标题：A sparse reconstruction method of physical field via multi-source sensors for flight vehicle
- 年份：2025
- 期刊/来源：Aerospace Science
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：实验/测量 + 性能分析型
- 研究对象：When various physical properties, such as pressure and heat flux, need to be measured simultaneously, different sensors will be installed for corresponding properties, which increases the number of sensors, leading to measuring complexity and cost. Measuring distributed loads of physical fields like force and heat on surface is essential for aerodynamic design, integrated thermal protection system analysis, health monitoring, and flight control of flight vehicle [1–3]. However, the limited senso
- 主要方法：Given that different physical fields under the same flow conditions are correlated, a sparse reconstruction method utilizing information from different types of sensors is proposed to reduce the number of sensors and improve reconstruction accuracy. Meanwhile, a theoretical analysis is conducted to determine the minimum number of multi-source sensors required by the proposed method to achieve target reconstruction accuracy. The method is achieved by three steps.
- 主要证据：图表 23 个标题、公式 134 个候选、参考文献 47 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“When various physical properties, such as pressure and heat flux, need to be measured simultaneously, different sensors will be installed for corresponding properties, which increa”，可以通过“Given that different physical fields under the same flow conditions are correlated, a sparse reconstruction method utilizing information from different types of sensors is proposed to reduce the number of sensors and imp”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：Given that different physical fields under the same flow conditions are correlated, a sparse reconstruction method utilizing information from different types of sensors is proposed to reduce the number of sensors and improve reconstruction accuracy. Meanwhile, a theoretical analysis is conducted to determine the minimum number of multi-source sensors required by the proposed method to achieve target reconstruction accuracy. The method is achieved by three steps.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：When various physical properties, such as pressure and heat flux, need to be measured simultaneously, different sensors will be installed for corresponding properties, which increases the number of sensors, leading to measuring complexity and cost. Measuring distributed loads of physical fields like force and heat on surface is essential for aerodynamic design, integrated thermal protection system analysis, health monitoring, and flight control of flight vehicle [1–3]. However, the limited sensor locations on the fight vehicle surface poses challenges in obtaining complete field data.
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
- 作者声明或文本中可见 gap：However, the limited sensor locations on the fight vehicle surface poses challenges in obtaining complete field data. To address this issue, researchers have developed sparse reconstruction methods to reconstruct physical filed data from limited sensor measurements. Originating in signal processing, CS leverages signal sparsity to reconstruct complete signals from limited observations and has been widely used for sparse reconstruction of high-dimensional physical field data [7,8].
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- Originating in signal processing, CS leverages signal sparsity to reconstruct complete signals from limited observations and has been widely used for sparse reconstruction of high-dimensional physical field data [7,8].
- This poses significant challenges for space-constrained applications, such as smart micro aerial vehicles [28,29].

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：Given that different physical fields under the same flow conditions are correlated, a sparse reconstruction method utilizing information from different types of sensors is proposed to reduce the number of sensors and improve reconstruction accuracy. Meanwhile, a theoretical analysis is conducted to determine the minimum number of multi-source sensors required by the proposed method to achieve target reconstruction accuracy. The method is achieved by three steps.
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
| Given that different physical fields under the same flow conditions are correlated, a sparse reconstruction method utilizing information from different types of sensors is proposed to reduce the number of sensors and improve reconstruction accuracy. | 摘要/引言/结论候选 | 图：Fig. 1. Schematic diagram for sparse reconstruction of physical field data using multi-source sensor measurements. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Meanwhile, a theoretical analysis is conducted to determine the minimum number of multi-source sensors required by the proposed method to achieve target reconstruction accuracy. | 摘要/引言/结论候选 | 图：Fig. 2. Procedure of determining the minimum number of the multi-source sensors. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The method is achieved by three steps. | 摘要/引言/结论候选 | 图：Fig. 3. Modeling process of the sparse reconstruction model using POD-RBFNN. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The results indicate that, compared with traditional single-source reconstruction method, the proposed method can decrease the total sensor number by about 50% with the same accuracy level, and with the same total number of sensors, the sparse reconstruction e | 摘要/引言/结论候选 | 表：Table 1 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| To address this issue, researchers have developed sparse reconstruction methods to reconstruct physical filed data from limited sensor measurements. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 214.3, 690.38)]] * Corresponding author. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| To address this, Sha et al. [11] proposed an improved CS method that incorporates a fully connected neural network to refine the solution process of basis coefficients. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 326.84, 716.91)]] https://doi.org/10.101 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Schematic diagram for sparse reconstruction of physical field data using multi-source sensor measurements. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 2. Procedure of determining the minimum number of the multi-source sensors. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 3. Modeling process of the sparse reconstruction model using POD-RBFNN. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 4. The architecture of RBFNN with n inputs and m outputs. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 5. Flowchart of multi-source sensor location optimization. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 6. Schematic diagram and dimensional specifications of the reentry capsule. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 7. Dominant POD modes of pressure on the surfaces of the reentry capsule; the unit is Pa. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. Dominant POD modes of heat flux on the surfaces of the reentry capsule; the unit is W/m2. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 9. POD reconstruction error via the number of modes: (a) pressure and (b) heat flux. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 10. Comparison of reconstruction errors between single-source and multi-source sensors: (a) pressure and (b) heat flux. (Here, n donates the number of sing | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 11. The optimum multi-source sensor locations obtained from 10 optimizations. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. Sparse reconstruction results of the test sample with the worst reconstruction accuracy(Ma = 8.0617, α = − 24.75∘, H = 45.981km). | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 13. Sparse reconstruction results of the test sample with the best reconstruction accuracy (Ma = 8.9746, α = − 22.97∘, H = 48.594km). | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 14. Schematic of sensor redundancy mechanism. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 15. Comparison of reconstruction errors with different noise levels between single-source and multi-source sensors. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 214.3, 690.38)]] * Corresponding author. E-mail address: leo | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 326.84, 716.91)]] https://doi.org/10.1016/j.ast.2025.110685  | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (314.98, 340.19, 339.73, 353.43)]] Y1 = f1 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (314.99, 350.62, 339.73, 363.84)]] Y2 = f2 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (317.37, 363.94, 354.28, 383.0)]] ⋮ Yt = ft(Dt) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (314.99, 589.24, 352.12, 631.2)]] Y1 = f1(D) Y2 = f2(D) ⋮ Yt = ft(D) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.6, 652.64, 349.19, 665.67)]] where, D = | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 3, bbox (37.59, 706.94, 218.43, 724.43)]] subsequently constructed. where, Yi = [ Yi | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> Communicated by Huihe Qiu
> The physical field reconstruction depending on sensors installed sparsely on the surface can provide more valuable and detailed information for design, control, and maintenance of flight vehicles. When various physical properties, such as pressure and heat flux, need to be measured simultaneously, different sensors will be installed for corresponding properties, which increases the number of sensors, leading to measuring complexity and cost. Given that different physical fields under the same flow conditions are correlated, a sparse reconstruction method utilizing information from different types of sensors is proposed to reduce the number of sensors and improve reconstruction accuracy. Meanwhile, a theoretical analysis is conducted to determine the minimum number of multi-source sensors required by the proposed method to achieve target reconstruction accuracy. The method is achieved by three steps. Firstly, with proper orthogonal decomposition algorithm, the modes of each physical field are recognized and extracted. Then, by using radial basis function neural network, the mapping from measurements of multi-source sensors to mode coefficients of multiple physical fields is created. Lastly, for given total number of sensors, the optimization model to determine the optimum locations and types of sensors is built, and solved by differential evolution algorithm. As a verification case, the pressure and heat flux fields of reentry capsule in hypersonic, are reconstructed. The results indicate that, compared with traditional single-source reconstruction method, the proposed method can decrease the total sensor number by about 50% with the same accuracy level, and with the same total number of sensors, the sparse reconstruction error can be reduced by 16% to 99%.

### 7.4 摘要中文翻译

> 邱辉和通讯 基于表面稀疏安装的传感器进行物理场重建，可以为飞行器的设计、控制和维护提供更有价值、更详细的信息。当需要同时测量压力、热通量等多种物理特性时，需要针对相应的特性安装不同的传感器，从而增加了传感器的数量，导致测量复杂度和成本。鉴于相同流动条件下不同物理场的相关性，提出了一种利用不同类型传感器信息的稀疏重建方法，以减少传感器数量并提高重建精度。同时，进行了理论分析，确定了该方法实现目标重建精度所需的最少多源传感器数量。该方法通过三个步骤实现。首先，通过适当的正交分解算法，识别并提取各个物理场的模式。然后，通过使用径向基函数神经网络，创建从多源传感器的测量到多个物理场的模式系数的映射。最后，对于给定的传感器总数，建立优化模型以确定传感器的最佳位置和类型，并通过差分进化算法求解。作为验证案例，重建了高超声速再入舱的压力场和热流场。
> 
> 结果表明，与传统的单源重建方法相比，在相同精度水平下，该方法可减少传感器总数约50%，且在传感器总数相同的情况下，稀疏重建误差可减少16%~99%。

### 7.5 结论完整摘录

识别到的结论位置：4. Conclusions

> This study presents a sparse reconstruction method for multiple physical field data based on multi-source sensor measurements. The method uses POD-RBFNN to build an efficient sparse reconstruction model via multi-source sensor measurements. It incorporates the DE algorithm for sensor location optimization, providing optimum multisource sensor locations and the corresponding sparse reconstruction model. The method is validated through the sparse reconstruction of two reentry capsule physical fields. The key conclusions are summarized below.
> 
> 1. The proposed method leverages multi-source sensor measurements to construct the sparse reconstruction model, significantly reducing the number of sensors. It determines the minimum number of sensors required to ensure high reconstruction accuracy based on system observability.
> 
> 2. Repeated optimizations demonstrate the method’s strong robustness, reflected in low variance of reconstruction errors, consistent sensor types and locations, and a physically meaningful distribution of optimum sensor locations.
> 
> 3. Compared to the single-source reconstruction method, the proposed method excels in accurately reconstructing multiple physical fields with a limited number of sensors and achieves even better performance when more sensors are available.
> 
> 4. The effectiveness of the proposed method under measurement noise is validated. Even under different noise levels, the minimum number of multi-source sensors remains stable, demonstrating noiseindependent performance.

### 7.6 结论中文翻译

> 本研究提出了一种基于多源传感器测量的多个物理场数据的稀疏重建方法。该方法使用 POD-RBFNN 通过多源传感器测量构建高效的稀疏重建模型。它结合了传感器位置优化的DE算法，提供最佳的多源传感器位置和相应的稀疏重建模型。通过两个再入舱物理场的稀疏重建对该方法进行了验证。主要结论总结如下。所提出的方法利用多源传感器测量来构建稀疏重建模型，显着减少传感器的数量。它根据系统可观测性确定确保高重建精度所需的最小传感器数量。反复的优化证明了该方法的强大鲁棒性，体现在重建误差的低方差、一致的传感器类型和位置以及最佳传感器位置的物理意义分布。与单源重建方法相比，该方法擅长用有限数量的传感器精确重建多个物理场，并且在更多传感器可用时实现更好的性能。验证了所提方法在测量噪声下的有效性。即使在不同的噪声水平下，多源传感器的最小数量也保持稳定，表现出与噪声无关的性能。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 8247 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. Methods | 方法建构 | 372 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 3 | 2.1. Sparse reconstruction method via multi-source sensors | 方法建构 | 5015 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 2.2. Minimum number of the multi-source sensors | 对象/条件/子问题展开 | 140 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 2.2.1. Determine the rank of physical field data | 对象/条件/子问题展开 | 3772 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 2.2.2. Determine the minimum number of sensors | 对象/条件/子问题展开 | 2653 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 2.3. Sparse reconstruction model using rom-based surrogate | 方法建构 | 5385 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 8 | 2.4. Sensor location optimization using de algorithm | 方法建构 | 2156 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 9 | 3. Test case | 对象/条件/子问题展开 | 223 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 3.1. Description of physical model | 方法建构 | 671 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 11 | 3.2. Modeling parameters analysis | 方法建构 | 2845 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 12 | 3.3. Reconstruction results | 结果验证/讨论 | 6120 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 13 | 3.4. Analysis of sensor noise | 结果验证/讨论 | 2003 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 14 | 4. Conclusions | 主张回收/边界说明 | 1521 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 15 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 350 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：mathbf(174)；reconstruction(144)；sparse(108)；sensor(74)；field(70)；sensors(58)；physical(55)；data(51)；number(47)；multi-source(43)；heat(40)；left(39)；right(39)；flux(39)；rank(38)；pressure(34)；optimization(27)；measurements(26)；fields(25)；array(25)
- 高频学术名词/术语：reconstruction(144)；pressure(34)；optimization(27)；location(14)；function(14)；section(11)；performance(7)；measurement(5)；observability(5)；turbulence(4)；information(4)；ensure(4)；proportion(4)；temperature(3)；representation(3)
- 高频学术动词：obtained(11)；constructed(6)；validated(5)；compared(4)；optimized(3)；obtain(3)；presented(3)；demonstrate(3)；developed(2)；construct(2)；predicted(2)；investigate(1)；optimize(1)；derived(1)；propose(1)
- 高频形容词：physical(55)；partial(20)；neural(7)；measurement(5)；high-dimensional(4)；theoretical(4)；total(4)；objective(4)；traditional(4)；table(4)；consistent(4)；thermal(3)；computational(3)；significant(3)；mathcal(3)
- 高频副词：respectively(8)；subsequently(6)；accurately(5)；generally(4)；directly(4)；additionally(4)；similarly(3)；effectively(3)；specifically(3)；significantly(3)；theoretically(3)；relatively(3)
- 高频二词短语：sparse reconstruction(102)；field data(40)；heat flux(39)；physical field(37)；mathbf mathbf(31)；number sensors(26)；sensor measurements(23)；left mathbf(23)；minimum number(21)；multi-source sensor(21)；pressure heat(21)；mathbf right(20)；sensor locations(19)；reconstruction accuracy(15)；operatorname rank(15)
- 高频三词短语：physical field data(26)；pressure heat flux(21)；sensor location optimization(14)；left mathbf right(14)；minimum number sensors(13)；heat flux fields(13)；multi-source sensor measurements(11)；heat flux field(11)；sparse reconstruction accuracy(9)；multiple physical field(9)；displaystyle frac partial(9)；frac partial partial(9)
- 被动语态估计：80
- `we + 动作动词` 主动句估计：1
- 一般现在时线索：116
- 一般过去时线索：251
- 现在完成时线索：2
- 情态动词线索：38

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Measuring distributed loads of physical fields like force and heat on surface is essential for aerodynamic design, integrated thermal protection system analysis, health monitoring, and flight control of flight vehicle [1–3].
  - 可迁移句型：{object} distributed loads of physical fields like force and heat on surface is essential for aerodynamic design, integrated thermal protection system analysis, health monitoring, and flight control of flight vehicle [1–3].
- 原句：However, CS requires optimization to solve basis coefficients and is inherently NP-hard, posing challenges for ensuring sparse reconstruction accuracy.
  - 可迁移句型：{object}, CS requires optimization to solve basis coefficients and is inherently NP-hard, posing challenges for ensuring sparse reconstruction accuracy.
- 原句：Unlike CS, which requires optimizing basis coefficients, these models directly map sparse sensor measurements to physical field data.
  - 可迁移句型：{object} CS, which requires optimizing basis coefficients, these models directly map sparse sensor measurements to physical field data.
### gap/转折句
- 原句：However, the limited sensor locations on the fight vehicle surface poses challenges in obtaining complete field data.
  - 可迁移句型：{object}, the limited sensor locations on the fight vehicle surface poses challenges in obtaining complete field data.
- 原句：To address this issue, researchers have developed sparse reconstruction methods to reconstruct physical filed data from limited sensor measurements.
  - 可迁移句型：{object} address this issue, researchers have developed sparse reconstruction methods to reconstruct physical filed data from limited sensor measurements.
- 原句：Originating in signal processing, CS leverages signal sparsity to reconstruct complete signals from limited observations and has been widely used for sparse reconstruction of high-dimensional physical field data [7,8].
  - 可迁移句型：{object} in signal processing, CS leverages signal sparsity to reconstruct complete signals from limited observations and has been widely used for sparse reconstruction of high-dimensional physical field data [7,8].
- 原句：However, CS requires optimization to solve basis coefficients and is inherently NP-hard, posing challenges for ensuring sparse reconstruction accuracy.
  - 可迁移句型：{object}, CS requires optimization to solve basis coefficients and is inherently NP-hard, posing challenges for ensuring sparse reconstruction accuracy.
### 方法提出句
- 原句：Given that different physical fields under the same flow conditions are correlated, a sparse reconstruction method utilizing information from different types of sensors is proposed to reduce the number of sensors and improve reconstruction accuracy.
  - 可迁移句型：{object} that different physical fields under the same flow conditions are correlated, a sparse reconstruction method utilizing information from different types of sensors is proposed to reduce the number of sensors and improve reconstruction accuracy.
- 原句：Meanwhile, a theoretical analysis is conducted to determine the minimum number of multi-source sensors required by the proposed method to achieve target reconstruction accuracy.
  - 可迁移句型：{object}, a theoretical analysis is conducted to determine the minimum number of multi-source sensors required by the proposed method to achieve target reconstruction accuracy.
- 原句：The method is achieved by three steps.
  - 可迁移句型：{object} method is achieved by three steps.
- 原句：Lastly, for given total number of sensors, the optimization model to determine the optimum locations and types of sensors is built, and solved by differential evolution algorithm.
  - 可迁移句型：{object}, for given total number of sensors, the optimization model to determine the optimum locations and types of sensors is built, and solved by differential evolution algorithm.
### 结果证明句
- 原句：Meanwhile, a theoretical analysis is conducted to determine the minimum number of multi-source sensors required by the proposed method to achieve target reconstruction accuracy.
  - 可迁移句型：{object}, a theoretical analysis is conducted to determine the minimum number of multi-source sensors required by the proposed method to achieve target reconstruction accuracy.
- 原句：The method is achieved by three steps.
  - 可迁移句型：{object} method is achieved by three steps.
- 原句：The results indicate that, compared with traditional single-source reconstruction method, the proposed method can decrease the total sensor number by about 50% with the same accuracy level, and with the same total number of sensors, the sparse reconstruction error can be reduced by 16% to 99%.
  - 可迁移句型：{object} results indicate that, compared with traditional single-source reconstruction method, the proposed method can decrease the total sensor number by about 50% with the same accuracy level, and with the same total number of sensors, the sparse reconstruct
- 原句：Fukami et al. [15] employed convolutional neural networks to achieve sparse reconstruction of the 2D cylinder wake and sea surface temperature field.
  - 可迁移句型：{object} et al. [15] employed convolutional neural networks to achieve sparse reconstruction of the 2D cylinder wake and sea surface temperature field.
### 贡献收束句
- 原句：Communicated by Huihe Qiu The physical field reconstruction depending on sensors installed sparsely on the surface can provide more valuable and detailed information for design, control, and maintenance of flight vehicles.
  - 可迁移句型：{object} by Huihe Qiu The physical field reconstruction depending on sensors installed sparsely on the surface can provide more valuable and detailed information for design, control, and maintenance of flight vehicles.
- 原句：Given that different physical fields under the same flow conditions are correlated, a sparse reconstruction method utilizing information from different types of sensors is proposed to reduce the number of sensors and improve reconstruction accuracy.
  - 可迁移句型：{object} that different physical fields under the same flow conditions are correlated, a sparse reconstruction method utilizing information from different types of sensors is proposed to reduce the number of sensors and improve reconstruction accuracy.
- 原句：The results indicate that, compared with traditional single-source reconstruction method, the proposed method can decrease the total sensor number by about 50% with the same accuracy level, and with the same total number of sensors, the sparse reconstruction error can be reduced by 16% to 99%.
  - 可迁移句型：{object} results indicate that, compared with traditional single-source reconstruction method, the proposed method can decrease the total sensor number by about 50% with the same accuracy level, and with the same total number of sensors, the sparse reconstruct
- 原句：To address this, Sha et al. [11] proposed an improved CS method that incorporates a fully connected neural network to refine the solution process of basis coefficients.
  - 可迁移句型：{object} address this, Sha et al. [11] proposed an improved CS method that incorporates a fully connected neural network to refine the solution process of basis coefficients.
### 边界/谨慎句
- 原句：However, the limited sensor locations on the fight vehicle surface poses challenges in obtaining complete field data.
  - 可迁移句型：{object}, the limited sensor locations on the fight vehicle surface poses challenges in obtaining complete field data.
- 原句：To address this issue, researchers have developed sparse reconstruction methods to reconstruct physical filed data from limited sensor measurements.
  - 可迁移句型：{object} address this issue, researchers have developed sparse reconstruction methods to reconstruct physical filed data from limited sensor measurements.
- 原句：In early studies, compressed sensing [6] (CS) was commonly used to construct sparse reconstruction models.
  - 可迁移句型：{object} early studies, compressed sensing [6] (CS) was commonly used to construct sparse reconstruction models.
- 原句：Originating in signal processing, CS leverages signal sparsity to reconstruct complete signals from limited observations and has been widely used for sparse reconstruction of high-dimensional physical field data [7,8].
  - 可迁移句型：{object} in signal processing, CS leverages signal sparsity to reconstruct complete signals from limited observations and has been widely used for sparse reconstruction of high-dimensional physical field data [7,8].

## 9. 引用风险层

- 正文引用簇估计：36
- 参考文献条数：47
- 可识别年份条目数：78
- 2021 年及以后参考文献数：64
- 2010 年以前经典文献数：2
- 高频来源粗略识别：Sci. Technol(7)；Fluids(5)；J. Aeronaut(3)；China Technol. Sci(2)；Comput. Phys(2)；Mach. Intell(2)；Fluids Struct(2)；Struct(2)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] W. Xiong, C. Zhu, D. Guo, C. Hou, Z. Yang, Z. Xu, L. Qiu, H. Yang, K. Li, Y. Huang, Bio-inspired, intelligent flexible sensing skin for multifunctional flying perception, Nano Energy 90 (2021) 106550, https://doi.org/10.1016/j.nanoen.2021.106550.
- [2] Y. Huang, C. Zhu, W. Xiong, Y. Wang, Y. Jiang, L. Qiu, D. Guo, C. Hou, S. Jiang, Z. Yang, B. Wang, L. Wang, Z. Yin, Flexible smart sensing skin for “fly-by-feel” morphing aircraft, Sci. China Technol. Sci. 65 (1) (2022) 1–29, https://doi.org/ 10.1007/s11431-020-1793-0.
- [3] M.N. Mowla, D. Asadi, T. Durhasan, J.R. Jafari, M. Amoozgar, Recent advancements in morphing applications: architecture, artificial intelligence integration, challenges, and future trends-a comprehensive survey, Aerosp. Sci. Technol. 161 (2025) 110102, https://doi.org/10.1016/j.ast.2025.110102.
- [4] P. Dubois, T. Gomez, L. Planckaert, L. Perret, Machine learning for fluid flow reconstruction from limited measurements, J. Comput. Phys. 448 (2022) 110733, https://doi.org/10.1016/j.jcp.2021.110733.
- [5] J.E. Santos, Z.R. Fox, A. Mohan, D.O. Malley, H. Viswanathan, N. Lubbers, Development of the Senseiver for efficient field reconstruction from sparse observations, Nat. Mach. Intell. 5 (2023) 1317–1325, https://doi.org/10.1038/ s42256-023-00746-x.
- [6] D.L. Donoho, Compressed sensing, IEEE Trans. Inf. Theory 52 (4) (2006) 1289–1306, https://doi.org/10.1109/TIT.2006.871582.
- [7] L. Mathelin, K. Kasper, H. Abou Kandil, Observable dictionary learning for high‑dimensional statistical inference, Arch. Comput. Methods Eng. 25 (2018) 103–120, https://doi.org/10.1007/s11831-017-9219-2.
- [8] J.L. Callaham, K. Maeda, S.L. Brunton, Robust flow reconstruction from limited measurements via sparse representation, Phys. Rev. Fluids 4 (2019) 103907, https://doi.org/10.1103/PhysRevFluids.4.103907.
- [9] Z. Bai, T. Wimalajeewa, Z. Berger, G. Wang, M. Glauser, P.K. Varshney, Low- dimensional approach for reconstruction of airfoil data via compressive sensing, AIAA J. 53 (4) (2015) 920–933, https://doi.org/10.2514/1.J053287.
- [10] Y. Sha, Y. Xu, Q. Yang, Y. Wei, C. Wang, Research on pressure reconstruction of cavitation hydrofoil surface based on compressed sensing, Ocean Eng. 260 (2022) 112036, https://doi.org/10.1016/j.oceaneng.2022.112036.
- [11] Y. Sha, Y. Xu, Y. Wei, C. Wang, Prediction of pressure fields on cavitation hydrofoil based on improved compressed sensing technology, Phys. Fluids 36 (2024) 013321, https://doi.org/10.1063/5.0189088.
- [12] S.L. Brunton, B.R. Noack, P. Koumoutsakos, Machine learning for fluid mechanics, Annu. Rev. Fluid Mech. 52 (2020) 477–508, https://doi.org/10.1146/annurev- fluid-010719-060214.
- [13] Y. Li, J. Chang, C. Kong, W. Bao, Recent progress of machine learning in flow modeling and active flow control, Chin. J. Aeronaut. 35 (4) (2022) 14–44, https:// doi.org/10.1016/j.cja.2021.07.027.
- [14] X. Jia, C. Gong, W. Ji, C. Li, An accuracy-enhanced transonic flow prediction method fusing deep learning and a reduced-order model, Phys. Fluids 36 (2024) 056101, https://doi.org/10.1063/5.0204152.
- [15] K. Fukami, R. Maulik, N. Ramachandra, K. Fukagata, K. Taira, Global field reconstruction from sparse sensors with Voronoi tessellation-assisted deep learning, Nat. Mach. Intell. 3 (11) (2021) 945–951, https://doi.org/10.1038/ s42256-021-00402-2.

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
