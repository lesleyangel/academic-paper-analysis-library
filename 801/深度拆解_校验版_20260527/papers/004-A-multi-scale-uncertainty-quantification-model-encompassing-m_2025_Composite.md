# 论文深度拆解：A multi-scale uncertainty quantification model encompassing minimum-size unit cells for effective properties of plain woven composites

> 生成依据：`801/cleantext/004-A-multi-scale-uncertainty-quantification-model-encompassing-m_2025_Composite`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`004-A-multi-scale-uncertainty-quantification-model-encompassing-m_2025_Composite`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\A-multi-scale-uncertainty-quantification-model-encompassing-m_2025_Composite.pdf`
- 页数：21
- clean body 字符数：73458
- 摘要字符数：1526
- 参考文献条数：46
- 图题数：24
- 表题数：10
- 表格文件数：14
- 公式候选数：435
- 提取质量分：0.93
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "66 formula(s) need manual review."}]

## 1. 身份层

- 标题：A multi-scale uncertainty quantification model encompassing minimum-size unit cells for effective properties of plain woven composites
- 年份：2025
- 期刊/来源：Composite
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：实验/测量 + 性能分析型
- 研究对象：Thus, for plain woven composites with uncertainties of at least three scales, i.e., composite, fiber bundle, fiber, and matrix, the primary challenge in uncertainty quantification by Monte Carlo method is the unaffordable computational burden.
- 主要方法：However, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of inter- scale correlations, and unaffordable computational cost of massive simulations are three primary problems at present. In this work, an innovative model with high accuracy and feasible cost for the mechanical property prediction of plain woven composites is developed encompassing minimum-size unit cells and multi-scale un- certainty quantification. The uncertainties of geometry are described by uniform distributions for fiber, fiber bundle and composite scales, respectively; that of constituent properties is described by normal distributions for fiber and matrix, and its propagations 
- 主要证据：图表 34 个标题、公式 435 个候选、参考文献 46 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“Thus, for plain woven composites with uncertainties of at least three scales, i.e., composite, fiber bundle, fiber, and matrix, the primary challenge in uncertainty quantification ”，可以通过“However, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of inter- scale correlations, and unaffordable computational cost of massive simulations are three primary problems at p”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：For the cost control, minimum-size unit cells are formulated by exhaustive analysis of structural symmetries to reduce the computational cost without accuracy compromising for the single simulation, and 1/8 and 1/16 unit cells compared with traditional full-size ones are obtained. The evolution convergence for statistical uncertainties of effective properties is finally obtained with totally reduced computational cost of 89%. Such method tend to outcome true results as the number of simulations increases [16].
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：Thus, for plain woven composites with uncertainties of at least three scales, i.e., composite, fiber bundle, fiber, and matrix, the primary challenge in uncertainty quantification by Monte Carlo method is the unaffordable computational burden.
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
- 作者声明或文本中可见 gap：However, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of inter- scale correlations, and unaffordable computational cost of massive simulations are three primary problems at present. However, the mold making, dimensional processing and high temperature in the composite manufacturing bring about various uncertainties of geometric and constituent parameters in multiple scales, thus, it is crucial to quantify these uncertainties to hold the prediction accuracy of composites properties [5,6]. However, this approach involves a significant amount of computationally intensive simulations to explore the entire uncertainty space.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- However, the mold making, dimensional processing and high temperature in the composite manufacturing bring about various uncertainties of geometric and constituent parameters in multiple scales, thus, it is crucial to quantify these uncertainties to hold the prediction accuracy of composites properties [5,6].

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：However, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of inter- scale correlations, and unaffordable computational cost of massive simulations are three primary problems at present. In this work, an innovative model with high accuracy and feasible cost for the mechanical property prediction of plain woven composites is developed encompassing minimum-size unit cells and multi-scale un- certainty quantification. The uncertainties of geometry are described by uniform distributions for fiber, fiber bundle and composite scales, respectively; that of constituent properties is described by normal distributions for fiber and matrix, and its propagations to bundle and composite scales are realized by Nataf transformation methods with the consideration of parameter correlations.
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
| However, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of inter- scale correlations, and unaffordable computational cost of massive simulations are three primary problems at present. | 摘要/引言/结论候选 | 图：Fig. 1. Multi-scale uncertainty quantification process. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In this work, an innovative model with high accuracy and feasible cost for the mechanical property prediction of plain woven composites is developed encompassing minimum-size unit cells and multi-scale un- certainty quantification. | 摘要/引言/结论候选 | 图：Fig. 3. Reflection symmetry diagram. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Such type of material is developed by embedding fabric fibers into resin or ceramic matrix to take advantages of both the fiber and matrix. | 摘要/引言/结论候选 | 图：Fig. 2. Structure with translational symmetry. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Such method tend to outcome true results as the number of simulations increases [16]. | 摘要/引言/结论候选 | 表：Table 2 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In this work, we have tried to develop a method to reduce the computational cost of the single simulation without any compromise in simulation accuracy. | 摘要/引言/结论候选 | 表：Table 3 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Compared to analytical methods, the numerical ones, primarily represented by the Finite Element Method, can capture more local details, and enhance the calculation accuracy. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (37.59, 206.16, 417.63, 223.92)]] Yu-Cheng Yang a, Jian-Jun Gou a,*, C | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Multi-scale uncertainty quantification process. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 3. Reflection symmetry diagram. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 2. Structure with translational symmetry. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 6. Fiber bundles and unit cells. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 7. Geometric parameters of unit cells for fiber bundles. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. Boundaries of unit cells for fiber bundles. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 9. Plain woven composite and unit cells. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 10. Geometric parameters of unit cells for plain woven composites. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. Boundaries of unit cells for plain woven composite. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. Fiber bundle uncertainty input frequency histogram. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 13. Plain woven composite uncertainty input frequency histogram. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 14. Multi-scale uncertainty propagation process. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 15. Displacement fields of fiber bundles for different calculation cases. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 16. Displacement fields of plain woven composites for different calculation cases. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 17. Relative difference to UC1 (fiber bundles). | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 8 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 9 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 10 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 11 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 12 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 13 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 14 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (37.59, 206.16, 417.63, 223.92)]] Yu-Cheng Yang a, Jian-Jun Gou a,*, Chun-Lin Gong a, Yue- | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (42.63, 669.07, 202.04, 690.38)]] * Corresponding author. E-mail address: jj.gou@nwpu.edu. | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 336.41, 716.91)]] https://doi.org/10.1016/j.compstruct.2024. | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (62.87, 119.77, 69.01, 127.74)]] = | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (384.77, 172.62, 557.68, 187.26)]] i (i = x, y, z) (7) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (334.55, 172.67, 369.94, 187.26)]] i = uMm+1 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 3, bbox (306.6, 194.08, 557.68, 219.27)]] where u(*) i represents the displacement i | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (37.59, 259.01, 288.67, 273.04)]] εi = εm i + αiΔT (2) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> The uncertainty quantification is crucial to the high-precision prediction of composites’ effective properties. However, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of inter- scale correlations, and unaffordable computational cost of massive simulations are three primary problems at present. In this work, an innovative model with high accuracy and feasible cost for the mechanical property prediction of plain woven composites is developed encompassing minimum-size unit cells and multi-scale un- certainty quantification. For the accuracy holding, an uncertainty analysis process consists of the traceability description, inter-scale propagation and quantification is established. The uncertainties of geometry are described by uniform distributions for fiber, fiber bundle and composite scales, respectively; that of constituent properties is described by normal distributions for fiber and matrix, and its propagations to bundle and composite scales are realized by Nataf transformation methods with the consideration of parameter correlations. For the cost control, minimum-size unit cells are formulated by exhaustive analysis of structural symmetries to reduce the computational cost without accuracy compromising for the single simulation, and 1/8 and 1/16 unit cells compared with traditional full-size ones are obtained. The evolution convergence for statistical uncertainties of effective properties is finally obtained with totally reduced computational cost of 89%.

### 7.4 摘要中文翻译

> 不确定性量化对于复合材料有效性能的高精度预测至关重要。然而，多尺度参数的输入不确定性不明确、尺度间相关性的复杂不确定性传播以及大规模模拟的计算成本难以承受是目前的三个主要问题。在这项工作中，开发了一种具有高精度和可行成本的创新模型，用于平纹编织复合材料的机械性能预测，包括最小尺寸单元和多尺度不确定性量化。为了保持精度，建立了由溯源描述、尺度间传播和量化组成的不确定性分析流程。几何形状的不确定性分别通过纤维、纤维束和复合材料尺度的均匀分布来描述；成分性质的分布用纤维和基体的正态分布来描述，其向束和复合尺度的传播是通过考虑参数相关性的Nataf变换方法实现的。为了控制成本，通过对结构对称性的详尽分析来制定最小尺寸晶胞，以在不影响单次模拟精度的情况下降低计算成本，并获得与传统全尺寸晶胞相比的1/8和1/16晶胞。最终获得有效属性​​统计不确定性的演化收敛，计算成本总共降低了89%。

### 7.5 结论完整摘录

识别到的结论位置：6. Conclusions

> In this work, an uncertainty quantification model with high accuracy and feasible cost is developed for the effective mechanical properties of plain woven composites. In this model, uncertainties of geometric and constituent parameters are analyzed through the processes of traceability, inter-scale propagation, and quantification. Minimum size unit cells are developed through exhaustive analysis of the structural symmetries for the fiber bundle and plain woven composite to reduce the
> 
> (i) p
> 
> (h) αx
> 
> computational cost without compromising accuracy. Some conclusions are obtained:
> 
> 1. For fiber bundles, the minimum unit cell with 1/8 size is developed based on three translational, two reflectional and one 180◦ rotational symmetries; the minimum unit cell is validated by larger ones and References with the largest deviation of 3.5 %, and the uncertainty analysis cost is reduced by 82 %.
> 
> 2. For the plain woven composites, the minimum unit cell with 1/16 size is developed based on three translational, two reflectional and two 180◦ rotational symmetries; the minimum unit cell is validated by the comparison with larger ones, and the uncertainty analysis cost is reduced by 94 %.
> 
> 3. The total efficiency of the uncertainty quantification of plain woven composites is improved by 89 % considering the minimum unit cells of both composites and fiber bundles.
> 
> 4. For the uncertainties of fiber bundles, most effective properties have relatively low kurtosis values, and Ezb, vxyb, and αxb present relatively high absolute skewness values; the out-plane effective properties are more strongly related to the input fiber properties, while the in-plane ones are more strongly related to the input matrix properties.
> 
> 5. For the uncertainties of plain woven composites, most effective properties have relatively low kurtosis values, and $\nu _ {x y p} , \nu _ {x z p} , G _ {y x p}$ and $\alpha _ {x p}$ present relatively high absolute skewness values; the in-plane effective properties are more strongly related to the input fiber bundle properties, while the out-plane ones are more strongly related to the input matrix properties.

### 7.6 结论中文翻译

> 在这项工作中，为平纹编织复合材料的有效机械性能开发了一种具有高精度和可行成本的不确定性量化模型。在该模型中，通过可追溯、尺度间传播和量化的过程来分析几何参数和构成参数的不确定性。通过对纤维束和平织复合材料的结构对称性进行详尽分析来开发最小尺寸晶胞，以在不影响精度的情况下降低 (i) p (h) αx 计算成本。得到了一些结论： 1.对于纤维束，1/8尺寸的最小晶胞是基于3个平移对称、2个反射对称和1个180°旋转对称建立的；最小晶胞通过较大晶胞和参考文献进行验证，最大偏差为3.5%，不确定性分析成本降低82%。对于平纹编织复合材料，基于三个平移对称、两个反射对称和两个180°旋转对称开发了1/16尺寸的最小晶胞；通过与较大晶胞的比较验证最小晶胞，不确定性分析成本降低94%。考虑到复合材料和纤维束的最小晶胞，平织复合材料不确定性量化的总效率提高了 89%。对于纤维束的不确定性，大多数有效属性具有相对较低的峰度值，Ezb、vxyb和αxb呈现相对较高的绝对偏度值；面外有效属性与输入光纤属性的相关性更强，而面内有效属性与输入矩阵属性的相关性更强。
> 
> 对于平纹编织复合材料的不确定性，大多数有效性能具有相对较低的峰度值，并且 $\nu _ {x y p} 、\nu _ {x z p} 、G _ {y x p}$ 和 $\alpha _ {x p}$ 呈现相对较高的绝对偏度值；面内有效属性与输入纤维束属性的相关性更强，而面外有效属性与输入矩阵属性的相关性更强。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 6007 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. Multi-scale uncertainty quantification model | 方法建构 | 922 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 3 | 3. Minimum-size unit cells and model parameterizations | 方法建构 | 427 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 3.1. Constitutive equation and constituent parameters | 对象/条件/子问题展开 | 2601 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 3.2.1. Translational symmetric structure | 对象/条件/子问题展开 | 3700 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 3.2.2. Summary of symmetry | 对象/条件/子问题展开 | 5770 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 3.3. Unit cells and their parameterization | 对象/条件/子问题展开 | 168 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 3.3.1. Microscale fiber bundle | 对象/条件/子问题展开 | 12841 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 3.3.2. Mesoscale woven composite material | 对象/条件/子问题展开 | 11849 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 4. Parameter uncertainty and propagation model | 方法建构 | 256 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 11 | 4.1. Traceability description of parameter uncertainty | 对象/条件/子问题展开 | 2495 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 4.2.1. Multiscale uncertainty propagation process | 对象/条件/子问题展开 | 1736 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 4.2.2. The multivariate gaussian distribution | 对象/条件/子问题展开 | 1987 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 4.2.3. Nataf transformation | 对象/条件/子问题展开 | 5895 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 15 | 5.1. Analysis of model accuracy and efficiency | 方法建构 | 3783 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 16 | 5.2.1. Microscale uncertainty analysis | 结果验证/讨论 | 5124 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 17 | 5.2.2. Mesoscale uncertainty analysis | 结果验证/讨论 | 4383 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 18 | 6. Conclusions | 主张回收/边界说明 | 2140 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 19 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 343 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：delta(130)；array(112)；rightarrow(98)；unit(75)；fiber(73)；properties(58)；uncertainty(58)；begin(56)；end(56)；parameters(54)；cell(49)；tag(47)；woven(46)；effective(45)；plain(43)；left(43)；right(43)；boundary(41)；modulus(41)；matrix(39)
- 高频学术名词/术语：distribution(36)；displacement(30)；expansion(25)；correlation(24)；transformation(17)；function(14)；calculation(14)；quantification(13)；difference(13)；propagation(11)；x-direction(11)；structure(10)；direction(10)；y-direction(10)；simulation(9)
- 高频学术动词：obtained(18)；compared(9)；developed(5)；constructed(4)；obtain(3)；validated(3)；develop(2)；derived(2)；predicted(1)；indicated(1)；presented(1)；estimate(1)；derive(1)
- 高频形容词：effective(45)；boundary(41)；symmetric(37)；displacement(30)；geometric(25)；coefficient(25)；thermal(24)；elastic(23)；table(23)；normal(21)；antisymmetric(18)；constituent(16)；relative(13)；rotational(12)；computational(11)
- 高频副词：respectively(21)；strongly(13)；normally(4)；relatively(4)；specifically(3)；finally(3)；similarly(3)；widely(2)；mostly(2)；primarily(2)；uniformly(2)；progressively(2)
- 高频二词短语：rightarrow delta(83)；begin array(56)；end array(56)；unit cell(47)；plain woven(43)；delta rightarrow(38)；fiber bundle(31)；effective properties(31)；boundary conditions(30)；unit cells(28)；delta end(27)；fiber bundles(25)；left begin(25)；array right(25)；woven composites(24)
- 高频三词短语：delta rightarrow delta(31)；delta end array(27)；rightarrow delta rightarrow(26)；left begin array(25)；end array right(25)；plain woven composites(24)；end array tag(23)；rightarrow delta end(23)；array end array(21)；qquad rightarrow delta(20)；plain woven composite(19)；rightarrow delta delta(18)
- 被动语态估计：132
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：297
- 一般过去时线索：281
- 现在完成时线索：3
- 情态动词线索：40

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 未稳定识别，需从对应章节人工补充。
### gap/转折句
- 原句：However, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of inter- scale correlations, and unaffordable computational cost of massive simulations are three primary problems at present.
  - 可迁移句型：{object}, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of inter- scale correlations, and unaffordable computational cost of massive simulations are three primary problems at present.
- 原句：However, the mold making, dimensional processing and high temperature in the composite manufacturing bring about various uncertainties of geometric and constituent parameters in multiple scales, thus, it is crucial to quantify these uncertainties to hold the prediction accuracy of composites properties [5,6].
  - 可迁移句型：{object}, the mold making, dimensional processing and high temperature in the composite manufacturing bring about various uncertainties of geometric and constituent parameters in multiple scales, thus, it is crucial to quantify these uncertainties to hold the 
- 原句：However, this approach involves a significant amount of computationally intensive simulations to explore the entire uncertainty space.
  - 可迁移句型：{object}, this approach involves a significant amount of computationally intensive simulations to explore the entire uncertainty space.
- 原句：Thus, for plain woven composites with uncertainties of at least three scales, i.e., composite, fiber bundle, fiber, and matrix, the primary challenge in uncertainty quantification by Monte Carlo method is the unaffordable computational burden.
  - 可迁移句型：{object}, for plain woven composites with uncertainties of at least three scales, i.e., composite, fiber bundle, fiber, and matrix, the primary challenge in uncertainty quantification by Monte Carlo method is the unaffordable computational burden.
### 方法提出句
- 原句：However, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of inter- scale correlations, and unaffordable computational cost of massive simulations are three primary problems at present.
  - 可迁移句型：{object}, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of inter- scale correlations, and unaffordable computational cost of massive simulations are three primary problems at present.
- 原句：In this work, an innovative model with high accuracy and feasible cost for the mechanical property prediction of plain woven composites is developed encompassing minimum-size unit cells and multi-scale un- certainty quantification.
  - 可迁移句型：{object} This study, an innovative model with high accuracy and feasible cost for the mechanical property prediction of plain woven composites is developed encompassing minimum-size unit cells and multi-scale un- certainty quantification.
- 原句：The uncertainties of geometry are described by uniform distributions for fiber, fiber bundle and composite scales, respectively; that of constituent properties is described by normal distributions for fiber and matrix, and its propagations to bundle and composite scales are realized by Nataf transformation methods with the consideration of parameter correlations.
  - 可迁移句型：{object} uncertainties of geometry are described by uniform distributions for fiber, fiber bundle and composite scales, respectively; that of constituent properties is described by normal distributions for fiber and matrix, and its propagations to bundle and c
- 原句：Such type of material is developed by embedding fabric fibers into resin or ceramic matrix to take advantages of both the fiber and matrix.
  - 可迁移句型：{object} type of material is developed by embedding fabric fibers into resin or ceramic matrix to take advantages of both the fiber and matrix.
### 结果证明句
- 原句：Such method tend to outcome true results as the number of simulations increases [16].
  - 可迁移句型：{object} method tend to outcome true results as the number of simulations increases [16].
- 原句：1 shows the multi-scale uncertainty quantification process, which contains three primary sub-processes: microscale uncertainty quantification, uncertainty propagation, and mesoscale uncertainty quantification.
  - 可迁移句型：1 shows the multi-scale uncertainty quantification process, which contains three primary sub-processes: microscale uncertainty quantification, uncertainty propagation, and mesoscale uncertainty quantification.
- 原句：Finally, the uncertainty quantification of the effective properties for plain woven composites is achieved.
  - 可迁移句型：{object}, the uncertainty quantification of the effective properties for plain woven composites is achieved.
- 原句：15 (a), (b), (c) and (d) shown the displacement fields obtained in the calculations of elastic modulus in x-direction, y-direction, zdirection, and that of thermal expansion coefficient for fiber bundles, respectively.
  - 可迁移句型：15 (a), (b), (c) and (d) shown the displacement fields obtained in the calculations of elastic modulus in x-direction, y-direction, zdirection, and that of thermal expansion coefficient for fiber bundles, respectively.
### 贡献收束句
- 原句：For the cost control, minimum-size unit cells are formulated by exhaustive analysis of structural symmetries to reduce the computational cost without accuracy compromising for the single simulation, and 1/8 and 1/16 unit cells compared with traditional full-size ones are obtained.
  - 可迁移句型：{object} the cost control, minimum-size unit cells are formulated by exhaustive analysis of structural symmetries to reduce the computational cost without accuracy compromising for the single simulation, and 1/8 and 1/16 unit cells compared with traditional fu
- 原句：The evolution convergence for statistical uncertainties of effective properties is finally obtained with totally reduced computational cost of 89%.
  - 可迁移句型：{object} evolution convergence for statistical uncertainties of effective properties is finally obtained with totally reduced computational cost of 89%.
- 原句：Theoretically, executing a sufficient number of Monte Carlo samples can provide a reliable measure of uncertainty.
  - 可迁移句型：{object}, executing a sufficient number of Monte Carlo samples can provide a reliable measure of uncertainty.
- 原句：To address this computational burden, the usual choice is to reduce the simulation number by surrogate models like the Radial Basis Function [11], Gaussian processes [12], Polynomial Chaos Expansion [13], etc.
  - 可迁移句型：{object} address this computational burden, the usual choice is to reduce the simulation number by surrogate models like the Radial Basis Function [11], Gaussian processes [12], Polynomial Chaos Expansion [13], etc.
### 边界/谨慎句
- 未稳定识别，需从对应章节人工补充。

## 9. 引用风险层

- 正文引用簇估计：18
- 参考文献条数：46
- 可识别年份条目数：49
- 2021 年及以后参考文献数：9
- 2010 年以前经典文献数：18
- 高频来源粗略识别：Compos Struct(7)；Compos Sci Technol(5)；Compos B Eng(2)；Compos A Appl Sci Manuf(2)；Comput Methods Appl Mech Eng(2)；Aeronaut J(1)；In International conference on composite materials(1)；A coupled FE-FFT multiscale method for progressive damage analysis of(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] ˙Inal O, Katnam KB, Potluri P, Soutis C. Progress in interlaminar toughening of aerospace polymer composites using particles and non-woven veils. Aeronaut J 2022;126:222–48.
- [2] Amraei J, Rogala T, Katunin A, Premanand A, et al. Thermomechanical fatigue behavior of CF/PEKK composite under low and ultrasonic frequencies. Compos B Eng 2024;281:111539.
- [3] Abtew MA. A comprehensive review on advancements, innovations and applications of 3D warp interlock fabrics and its composite materials. Compos B Eng 2024;278:111395.
- [4] Ivanov DS, Lomov SV. 2 - Modelling the structure and behaviour of 2D and 3D woven composites used in aerospace applications. In: Irving PE, Soutis C, editors. Polymer Composites in the Aerospace Industry. Woodhead Publishing; 2015. p. 21–52.
- [5] Potter, K. D., Understanding the origins of defects and variability in composites manufacture. In International conference on composite materials (ICCM)-17, Edinburgh, UK (2009): p. 18.
- [6] Mesogitis TS, Skordos AA, Long AC. Uncertainty in the manufacturing of fibrous thermosetting composites: A review. Compos A Appl Sci Manuf 2014;57:67–75.
- [7] Greene MS, Xu H, Tang S, Chen W, Liu WK. A generalized uncertainty propagation criterion from benchmark studies of microstructured material systems. Comput Methods Appl Mech Eng 2013;254:271–91.
- [8] Fang G, Wang B, Liang J. A coupled FE-FFT multiscale method for progressive damage analysis of 3D braided composite beam under bending load. Compos Sci Technol 2019;181:107691.
- [9] Zhu C, Zhu P, Liu Z. Uncertainty analysis of mechanical properties of plain woven carbon fiber reinforced composite via stochastic constitutive modeling. Compos Struct 2019;207:684–700.
- [10] Wang B, Fang G, Wang H, Liang J, Dai F, Meng S. Uncertainty modelling and multiscale simulation of woven composite twisted structure. Compos Sci Technol 2022;217:109118.
- [11] Tao W, Zhu P, Xu C, Liu Z. Uncertainty quantification of mechanical properties for three-dimensional orthogonal woven composites Part II: Multiscale simulation. Compos Struct 2020;235:111764.
- [12] Bostanabad R, Liang B, Gao J, Liu WK, Cao J, Zeng D, et al. Uncertainty quantification in multiscale simulation of woven fiber composites. Comput Methods Appl Mech Eng 2018;338:506–32.
- [13] Zhang H, Zhang L, Xu C, Liu Z, Zhu P. Global sensitivity analysis of mechanical properties in hybrid single lap aluminum-CFRP (plain woven) joints based on uncertainty quantification. Compos Struct 2022;280:114841.
- [14] Shi B, Deng Z. Multiscale reliability analysis of composite structures based on computer vision. Compos Struct 2022;292:115587.
- [15] Mishra S, Schwab C. Sparse tensor multi-level Monte Carlo finite volume methods for hyperbolic conservation laws with random initial data. Math Comp 2012;81: 1979–2018.

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
