# 论文深度拆解：A heat flux distribution prediction method for hypersonic flight vehicle along trajectory based on POD and TSCN

> 生成依据：`801/cleantext/001-A-heat-flux-distribution-prediction-method-for-hyperson_2025_Aerospace-Scien`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`001-A-heat-flux-distribution-prediction-method-for-hyperson_2025_Aerospace-Scien`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\A-heat-flux-distribution-prediction-method-for-hyperson_2025_Aerospace-Scien.pdf`
- 页数：12
- clean body 字符数：47330
- 摘要字符数：1356
- 参考文献条数：37
- 图题数：13
- 表题数：5
- 表格文件数：7
- 公式候选数：156
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "low_confidence_formulas", "severity": "medium", "message": "7 formula(s) need manual review."}]

## 1. 身份层

- 标题：A heat flux distribution prediction method for hypersonic flight vehicle along trajectory based on POD and TSCN
- 年份：2025
- 期刊/来源：Aerospace Scien
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：模型/预测 + 对比验证型
- 研究对象：Accurate and rapid determination of heat flux distribution along trajectories is essential for hypersonic flight vehicles. Accurately determining heat flux distribution is essential for the design and operation of the vehicle. Integrating the proposed HFDP method with CST simulations eliminates the need for CFD calculations, which typically require at least 15 min per time step in traditional CHT analysis.
- 主要方法：To address this issue, we propose a data-driven heat flux distribution prediction method using proper orthogonal decomposition (POD) and temporal-spatial convolu tional network (TSCN) to replace CFD simulations in CHT analysis. This method derives the surface heat flux modes using POD to enhance the modeling accuracy. Subsequently, a TSCN model, capable of extracting tem poral and spatial features from recent flight states and non-uniform wall temperatures affecting CFD, is devel oped to efficiently predict the low-dimensional mode coefficients, which can then be swiftly reconstructed into the heat flux distribution.
- 主要证据：图表 18 个标题、公式 156 个候选、参考文献 37 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“Accurate and rapid determination of heat flux distribution along trajectories is essential for hypersonic flight vehicles. Accurately determining heat flux distribution is essentia”，可以通过“To address this issue, we propose a data-driven heat flux distribution prediction method using proper orthogonal decomposition (POD) and temporal-spatial convolu tional network (TSCN) to replace CFD simulations in CHT an”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：Data-driven models can rapidly provide accurate results after training, significantly reducing the computational workload of CFD simulations. Yang et al. [2] applied proper orthogonal decomposition (POD) and an improved Gaussian process regression for steady-state heat flux distribution prediction (HFDP). Point-by-point modeling can improve geometric variations adaptability and localized feature utilization.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：Accurate and rapid determination of heat flux distribution along trajectories is essential for hypersonic flight vehicles. Accurately determining heat flux distribution is essential for the design and operation of the vehicle. Integrating the proposed HFDP method with CST simulations eliminates the need for CFD calculations, which typically require at least 15 min per time step in traditional CHT analysis.
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
- 作者声明或文本中可见 gap：However, transient computational fluid dynamics (CFD) is time-consuming, which makes conjugate heat transfer (CHT) analysis prohibitively expensive. However, accurately obtaining the heat flux distribution along the flight trajectory is challenging due to the influence of transient conjugate heat transfer (CHT). However, they overlooked the effects of transient CHT on heat flux, which arise from wall temperature variations caused by aerodynamic heating along the trajectory.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- We believe there are three main challenges: (1) The transient heat flux distribution is influenced by both historical flight states and wall temperature, yet existing methods struggle to manage the temporal dimensions of the input; (2) The high-dimensional distribution of heat flux results in models that are prone to overfitting and exhibit poor accuracy; (3) When applying a aerodynamic reduced-order model (ROM) in conjunction with other physical models in analysis such as CHT, it is necessary for ROM to possess accuracy, generalization, and stability [27].

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：To address this issue, we propose a data-driven heat flux distribution prediction method using proper orthogonal decomposition (POD) and temporal-spatial convolu tional network (TSCN) to replace CFD simulations in CHT analysis. This method derives the surface heat flux modes using POD to enhance the modeling accuracy. Subsequently, a TSCN model, capable of extracting tem poral and spatial features from recent flight states and non-uniform wall temperatures affecting CFD, is devel oped to efficiently predict the low-dimensional mode coefficients, which can then be swiftly reconstructed into the heat flux distribution.
- 我判断的真实贡献：把一个具体工程/物理/材料问题转化为可计算、可验证的模型或实验流程，并通过结果图表证明其在效率、精度、可靠性、性能或解释力上的增量。
- 创新类型：模型/预测 + 对比验证型；偏方法/模型/工程应用/实验证据/集成框架之一。
- 创新强度：中等到较强，取决于是否具备清晰 baseline、跨工况验证和误差/性能指标。
- 可能被挑战处：
  - 是否充分比较最接近方法；
  - 训练/实验/仿真工况是否覆盖真实应用；
  - 参数、边界条件和材料/结构假设是否可复现；
  - 结论是否超出证据支持范围。

## 6. 方法层

- 方法目标：用可复现的模型、实验或计算流程回答选题层问题。
- 方法类型：模型/预测 + 对比验证型
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
| To address this issue, we propose a data-driven heat flux distribution prediction method using proper orthogonal decomposition (POD) and temporal-spatial convolu tional network (TSCN) to replace CFD simulations in CHT analysis. | 摘要/引言/结论候选 | 图：Fig. 2. Scheme of surface temperature and heat flux after spatial discretization. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The proposed method was employed to predict the heat flux distribution of the re-entry capsule along the return trajectory, achieving an average relative prediction error below 2 % by the TSCN model built on the samples from 15 possible trajectories. | 摘要/引言/结论候选 | 图：Fig. 1. Illustration of conjugate heat transfer integrating CFD and CST. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Above all, the heat flux distributions along a new trajectory can be obtained within an hour by the proposed method, with an efficiency increase of about 200 times in comparison with traditional CHT analysis. | 摘要/引言/结论候选 | 图：Fig. 3. Illustration of conjugate heat transfer integrating HFDP model and CST. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Data-driven models can rapidly provide accurate results after training, significantly reducing the computational workload of CFD simulations. | 摘要/引言/结论候选 | 表：Table 1 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Yang et al. [2] applied proper orthogonal decomposition (POD) and an improved Gaussian process regression for steady-state heat flux distribution prediction (HFDP). | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Their studies indicate that dimensionality reduction-based modeling is promising for efficient HFDP. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 343.9, 716.91)]] https://doi.org/10.1016 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 2. Scheme of surface temperature and heat flux after spatial discretization. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 1. Illustration of conjugate heat transfer integrating CFD and CST. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 3. Illustration of conjugate heat transfer integrating HFDP model and CST. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 4. The procedure of heat flux distribution prediction method. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 6. The structure of convolution block: (a) TCN; (b) CNN. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 7. Test trajectories and range of possible trajectories. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. Schematic of the re-entry capsule’s model and trajectory. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 9. Schematic of the re-entry capsule’s model and trajectory. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 10. The combination of varying input sequence lengths and output. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. The prediction results along 3 test trajectories. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. Comparison of predicted and actual heat flux distributions at critical time points: (a) extremum heat flux; (b) extremum spatially averaged absolute er | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 13. Heat flux prediction along 3 test trajectories: (a) test 50 times; (b) test 200 times; (c) test 800 times. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 5. Dilated causal convolution. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 343.9, 716.91)]] https://doi.org/10.1016/j.ast.2025.110283 R | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (346.11, 110.41, 359.73, 127.85)]] ⎥⎥⎦= | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.6, 113.83, 327.87, 126.86)]] q(t) = | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (321.73, 158.49, 327.87, 166.46)]] = | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.6, 217.3, 335.87, 230.35)]] qk = -λf | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (337.38, 220.45, 367.56, 235.83)]] ∂y = -λf | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (419.75, 110.41, 462.68, 127.85)]] ⎥⎥⎦and T(t) = | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (368.56, 211.91, 560.02, 235.83)]] Te k -Tw k-1 ye (2) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> Accurate and rapid determination of heat flux distribution along trajectories is essential for hypersonic flight vehicles. However, transient computational fluid dynamics (CFD) is time-consuming, which makes conjugate heat transfer (CHT) analysis prohibitively expensive. To address this issue, we propose a data-driven heat flux distribution prediction method using proper orthogonal decomposition (POD) and temporal-spatial convolu tional network (TSCN) to replace CFD simulations in CHT analysis. This method derives the surface heat flux modes using POD to enhance the modeling accuracy. Subsequently, a TSCN model, capable of extracting tem poral and spatial features from recent flight states and non-uniform wall temperatures affecting CFD, is devel oped to efficiently predict the low-dimensional mode coefficients, which can then be swiftly reconstructed into the heat flux distribution. The proposed method was employed to predict the heat flux distribution of the re-entry capsule along the return trajectory, achieving an average relative prediction error below 2 % by the TSCN model built on the samples from 15 possible trajectories. Above all, the heat flux distributions along a new trajectory can be obtained within an hour by the proposed method, with an efficiency increase of about 200 times in comparison with traditional CHT analysis.

### 7.4 摘要中文翻译

> 准确快速地确定沿轨迹的热通量分布对于高超音速飞行器至关重要。然而，瞬态计算流体动力学 (CFD) 非常耗时，这使得共轭传热 (CHT) 分析成本高昂。为了解决这个问题，我们提出了一种数据驱动的热通量分布预测方法，使用适当的正交分解（POD）和时空卷积网络（TSCN）来代替CHT分析中的CFD模拟。该方法利用POD推导出表面热流模态，以提高建模精度。随后，开发了一个 TSCN 模型，能够从最近的飞行状态和影响 CFD 的不均匀壁温中提取时间和空间特征，以有效预测低维模态系数，然后可以快速将其重建为热通量分布。该方法用于预测返回舱沿返回轨迹的热通量分布，基于 15 个可能轨迹样本建立的 TSCN 模型实现了低于 2% 的平均相对预测误差。最重要的是，该方法可以在一个小时内获得沿着新轨迹的热通量分布，与传统的CHT分析相比，效率提高了约200倍。

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusion

> In this study, we proposed a heat flux distribution prediction method for hypersonic flight vehicles based on POD and TSCN. The method was validated by predicting the heat flux distribution along the return trajectory of the re-entry capsule. The conclusions of this study are summarized as follows:
> 
> • The proposed method predicted the heat flux distribution at each time step in about 0.035 s, effectively replacing time-consuming CFD calculations to perform CHT analysis. This allows for obtaining heat flux distributions along a new trajectory within an hour, with an efficiency increase of about 200 times in comparison with traditional CHT analysis.
> 
> • The predicted heat flux distributions of the re-entry capsule along the return trajectory achieved an average relative prediction error below 2 %, outperforming traditional heat flux prediction methods without accounting for recent states.
> 
> • The proposed method can achieve better accuracy when using the first 19 modes of the heat flux distribution and the four most recent flight states, which are the most important parameters for POD and TSCN, respectively.
> 
> • The TSCN model, employing dropout-based Bayesian approximation, produced prediction intervals that encompassed over 90 % of the calculated heat flux distribution, demonstrating reliability by preventing error accumulation, which is crucial for coupling analysis along the trajectory.

### 7.6 结论中文翻译

> 在本研究中，我们提出了一种基于POD和TSCN的高超声速飞行器热流分布预测方法。通过预测沿返回舱返回轨迹的热通量分布来验证该方法。本研究的结论总结如下： • 所提出的方法在大约0.035 s内预测了每个时间步的热通量分布，有效地替代了耗时的CFD计算来执行CHT分析。这样可以在一小时内获得沿新轨迹的热通量分布，与传统 CHT 分析相比，效率提高约 200 倍。 • 再入舱沿返回轨迹的预测热通量分布实现了低于 2% 的平均相对预测误差，优于传统的热通量预测方法（无需考虑近期状态）。 • 当使用热通量分布的前19个模态和最近的四个飞行状态（分别是POD和TSCN最重要的参数）时，所提出的方法可以获得更好的精度。 • TSCN 模型采用基于 dropout 的贝叶斯近似，生成的预测区间包含超过 90% 的计算热通量分布，通过防止误差积累证明了可靠性，这对于沿轨迹的耦合分析至关重要。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 8543 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. Problem description | 对象/条件/子问题展开 | 6173 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 3.1. Heat flux distribution prediction method | 方法建构 | 8251 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 3.2. Temporal-spatial convolution | 对象/条件/子问题展开 | 3653 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 4.1. Physical model and dataset sampling | 方法建构 | 3474 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 6 | 4.2. Modelling | 方法建构 | 6050 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 7 | 4.3. Discussion | 结果验证/讨论 | 9125 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 8 | 5. Conclusion | 主张回收/边界说明 | 1408 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 9 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 275 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：heat(120)；flux(109)；distribution(56)；time(44)；trajectory(39)；prediction(39)；temperature(37)；mathrm(35)；states(33)；wall(31)；flight(30)；along(30)；trajectories(28)；error(28)；cfd(26)；widehat(24)；convolution(22)；cst(20)；accuracy(20)；sum(20)
- 高频学术名词/术语：distribution(56)；prediction(39)；temperature(37)；convolution(22)；dimensionality(14)；duration(12)；performance(8)；condition(7)；validation(7)；contribution(7)；influence(6)；section(5)；capture(5)；accumulation(5)；structure(4)
- 高频学术动词：predicted(19)；compared(7)；predict(6)；derived(6)；indicate(4)；developed(3)；obtain(3)；introduced(2)；demonstrated(2)；demonstrate(2)；obtained(2)；constructed(2)；presented(2)；reveal(2)；validate(2)
- 高频形容词：temporal(17)；spatial(16)；boundary(16)；transient(15)；recent(14)；traditional(12)；historical(11)；relative(11)；thermal(10)；aerodynamic(10)；table(9)；potential(8)；causal(8)；computational(6)；neural(6)
- 高频副词：respectively(13)；spatially(8)；fully(7)；typically(6)；temporally(5)；additionally(5)；accurately(4)；highly(4)；specifically(4)；subsequently(4)；efficiently(3)；extremely(3)
- 高频二词短语：heat flux(109)；flux distribution(43)；wall temperature(22)；flight states(16)；flow field(11)；calculated heat(11)；along trajectory(10)；re-entry capsule(10)；flux prediction(9)；flux distributions(9)；predicted heat(8)；averaged absolute(8)；absolute error(8)；cfd cst(7)；temperature distribution(7)
- 高频三词短语：heat flux distribution(43)；calculated heat flux(11)；heat flux prediction(9)；heat flux distributions(9)；predicted heat flux(8)；averaged absolute error(8)；flux distribution prediction(6)；spatially averaged absolute(6)；flux distribution along(5)；recent flight states(5)；wall temperature distribution(5)；heat flux temperature(5)
- 被动语态估计：107
- `we + 动作动词` 主动句估计：1
- 一般现在时线索：114
- 一般过去时线索：429
- 现在完成时线索：2
- 情态动词线索：25

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Accurate and rapid determination of heat flux distribution along trajectories is essential for hypersonic flight vehicles.
  - 可迁移句型：{object} and rapid determination of heat flux distribution along trajectories is essential for hypersonic flight vehicles.
- 原句：Accurately determining heat flux distribution is essential for the design and operation of the vehicle.
  - 可迁移句型：{object} determining heat flux distribution is essential for the design and operation of the vehicle.
- 原句：Spatially, precise heat flux information is critical for optimizing geometry, structure, materials, and thermal protection system.
  - 可迁移句型：{object}, precise heat flux information is critical for optimizing geometry, structure, materials, and thermal protection system.
- 原句：Furthermore, we selected several critical time points in Test Trajectory 2 to assess the agreement between predicted and actual heat flux distributions, as shown in Fig.
  - 可迁移句型：{object}, we selected several critical time points in Test Trajectory 2 to assess the agreement between predicted and actual heat flux distributions, as shown in Fig.
### gap/转折句
- 原句：However, transient computational fluid dynamics (CFD) is time-consuming, which makes conjugate heat transfer (CHT) analysis prohibitively expensive.
  - 可迁移句型：{object}, transient computational fluid dynamics (CFD) is time-consuming, which makes conjugate heat transfer (CHT) analysis prohibitively expensive.
- 原句：However, accurately obtaining the heat flux distribution along the flight trajectory is challenging due to the influence of transient conjugate heat transfer (CHT).
  - 可迁移句型：{object}, accurately obtaining the heat flux distribution along the flight trajectory is challenging due to the influence of transient conjugate heat transfer (CHT).
- 原句：However, they overlooked the effects of transient CHT on heat flux, which arise from wall temperature variations caused by aerodynamic heating along the trajectory.
  - 可迁移句型：{object}, they overlooked the effects of transient CHT on heat flux, which arise from wall temperature variations caused by aerodynamic heating along the trajectory.
- 原句：However, such methodologies are inefficient in global heat flux modeling and suffer from limited generalization capabilities.
  - 可迁移句型：{object}, such methodologies are inefficient in global heat flux modeling and suffer from limited generalization capabilities.
### 方法提出句
- 原句：To address this issue, we propose a data-driven heat flux distribution prediction method using proper orthogonal decomposition (POD) and temporal-spatial convolu tional network (TSCN) to replace CFD simulations in CHT analysis.
  - 可迁移句型：{object} address this issue, we propose a data-driven heat flux distribution prediction method using proper orthogonal decomposition (POD) and temporal-spatial convolu tional network (TSCN) to replace CFD simulations in CHT analysis.
- 原句：This method derives the surface heat flux modes using POD to enhance the modeling accuracy.
  - 可迁移句型：{object} method derives the surface heat flux modes using POD to enhance the modeling accuracy.
- 原句：Subsequently, a TSCN model, capable of extracting tem poral and spatial features from recent flight states and non-uniform wall temperatures affecting CFD, is devel oped to efficiently predict the low-dimensional mode coefficients, which can then be swiftly reconstructed into the heat flux distribution.
  - 可迁移句型：{object}, a TSCN model, capable of extracting tem poral and spatial features from recent flight states and non-uniform wall temperatures affecting CFD, is devel oped to efficiently predict the low-dimensional mode coefficients, which can then be swiftly recons
- 原句：The proposed method was employed to predict the heat flux distribution of the re-entry capsule along the return trajectory, achieving an average relative prediction error below 2 % by the TSCN model built on the samples from 15 possible trajectories.
  - 可迁移句型：{object} proposed method was employed to predict the heat flux distribution of the re-entry capsule along the return trajectory, achieving an average relative prediction error below 2 % by the TSCN model built on the samples from 15 possible trajectories.
### 结果证明句
- 原句：Data-driven models can rapidly provide accurate results after training, significantly reducing the computational workload of CFD simulations.
  - 可迁移句型：{object} models can rapidly provide accurate results after training, significantly reducing the computational workload of CFD simulations.
- 原句：Their studies indicate that dimensionality reduction-based modeling is promising for efficient HFDP.
  - 可迁移句型：{object} studies indicate that dimensionality reduction-based modeling is promising for efficient HFDP.
- 原句：Using compact singular value decomposition [31], POD efficiently decomposed $q ,$ represented as $$q = U _ {R} \Sigma _ {R} {V _ {R}} ^ {T}\tag{8}$$ where R is the rank of $q ,$ U is the left singular matrix, and V is the right singular mat Using the optimal parameters derived in previous section, the HFDP at each time point was achieved with an average prediction time of about 0.035 s.
  - 可迁移句型：{object} compact singular value decomposition [31], POD efficiently decomposed $q ,$ represented as $$q = U _ {R} \Sigma _ {R} {V _ {R}} ^ {T}\tag{8}$$ where R is the rank of $q ,$ U is the left singular matrix, and V is the right singular mat Using the optima
- 原句：The spatio-temporal heat fluxes (both calculated and predicted) along the three test trajectories are shown in Fig.
  - 可迁移句型：{object} spatio-temporal heat fluxes (both calculated and predicted) along the three test trajectories are shown in Fig.
### 贡献收束句
- 原句：This method derives the surface heat flux modes using POD to enhance the modeling accuracy.
  - 可迁移句型：{object} method derives the surface heat flux modes using POD to enhance the modeling accuracy.
- 原句：Data-driven models can rapidly provide accurate results after training, significantly reducing the computational workload of CFD simulations.
  - 可迁移句型：{object} models can rapidly provide accurate results after training, significantly reducing the computational workload of CFD simulations.
- 原句：Yang et al. [2] applied proper orthogonal decomposition (POD) and an improved Gaussian process regression for steady-state heat flux distribution prediction (HFDP).
  - 可迁移句型：{object} et al. [2] applied proper orthogonal decomposition (POD) and an improved Gaussian process regression for steady-state heat flux distribution prediction (HFDP).
- 原句：Point-by-point modeling can improve geometric variations adaptability and localized feature utilization.
  - 可迁移句型：{object} modeling can improve geometric variations adaptability and localized feature utilization.
### 边界/谨慎句
- 原句：Moreover, the inverse heat conduction methods are only applicable for ground tests or flights where sensor measurements are available.
  - 可迁移句型：{object}, the inverse heat conduction methods are only applicable for ground tests or flights where sensor measurements are available.
- 原句：Dimensionality reduction-based modeling efficiently lowers the complexity of high-dimensional heat flux distributions by retaining only the dominant modes.
  - 可迁移句型：{object} reduction-based modeling efficiently lowers the complexity of high-dimensional heat flux distributions by retaining only the dominant modes.
- 原句：However, such methodologies are inefficient in global heat flux modeling and suffer from limited generalization capabilities.
  - 可迁移句型：{object}, such methodologies are inefficient in global heat flux modeling and suffer from limited generalization capabilities.

## 9. 引用风险层

- 正文引用簇估计：35
- 参考文献条数：37
- 可识别年份条目数：38
- 2021 年及以后参考文献数：28
- 2010 年以前经典文献数：2
- 高频来源粗略识别：Sci. Technol(6)；Fluids(3)；J. Aeronaut(2)；Aerosp. Eng(2)；Gases(1)；Technol(1)；Aircr(1)；Thermophys. Heat. Trans(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] Z. Wang, S.F. Song, X. Wang, et al., Summary and prospect of data-driven aerothermal modeling prediction methods[J], Phys. Gases 9 (4) (2024) 39–55.
- [2] Y. Yang, Y. Xue, W. Zhao, et al., Fast flow field prediction of three-dimensional hypersonic vehicles using an improved gaussian process regression algorithm[J], Phys. Fluids 36 (1) (2024).
- [3] C. Nie, J. Huang, X. Wang, et al., Fast aeroheating prediction method for complex shape vehicles based on proper orthogonal decomposition[J], Acta Aerodynamica Sinica 35 (6) (2017) 760–765.
- [4] J. Zhang, C. Nie, Cai Jinsheng, et al., A reduced-order model for fast predicting ionized flows of hypersonic vehicles along flight trajectory[J], Chin. J. Aeronaut. 37 (1) (2024) 89–105.
- [5] X. Chen, W.A Fan, Machine learning rapid prediction of the aerothermodynamic environment for near-space hypersonic unmanned aircraft[J], Tsinghua Sci. Technol. 30 (2) (2024) 682–694.
- [6] E.R. Dreyer, B.J. Grier, J.J. McNamara, et al., Rapid steady-state hypersonic aerothermodynamic loads prediction using reduced fidelity models[J], J. Aircr. 58 (3) (2021) 663–676.
- [7] Z.C. Zhang, T.Y. Gao, L. Zhang, et al., Aeroheating agent model based on radial basis function neural network[J], Acta Aeronautica et Astronautica Sinica 42 (4) (2021) 524167.
- [8] W. Li, W. Zhao, G. Dai, et al., A deep learning approach for wall heat flux prediction across various wall temperatures[J], Aerosp. Sci. Technol. 158 (2025) 109934.
- [9] Z. Wang, Z. Wang, X. Wang, et al., A data-driven aeroheating prediction model[J], Acta Aerodynamica Sinica 41 (5) (2023) 12–19.
- [10] Y. Yang, S. Yao, Y. Xue, et al., A variable fidelity approach for predicting aerodynamic wall quantities of hypersonic vehicles using the ConvNeXt encoder- decoder framework[J], Aerosp. Sci. Technol. 155 (2024) 109605.
- [11] G. Dai, W. Zhao, S. Yao, et al., Machine learning strategy for wall heat flux prediction in aerodynamic heating[J], J. Thermophys. Heat. Trans. 37 (2) (2023) 424–434.
- [12] G. Dai, W. Zhao, S. Yao, et al., Deep-learning strategy based on convolutional neural network for wall heat flux prediction[J], AIAA J. 61 (11) (2023) 4772–4782.
- [13] W. Yao, R.K Jaiman, Feedback control of unstable flow and vortex-induced vibration using the eigensystem realization algorithm[J], J. Fluid. Mech. 827 (2017) 394–414.
- [14] Righi M., Düzel S., Anderegg D., et al. ROM-based uncertainties quantification of flutter speed prediction of the BSCW wing[C], AIAA Scitech 2022 Forum. 2022: 0179.
- [15] C. Ruiz, J.´A. Acosta, A. Ollero, Aerodynamic reduced-order Volterra model of an ornithopter under high-amplitude flapping[J], Aerosp. Sci. Technol. 121 (2022) 107331.

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
