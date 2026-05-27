# 论文深度拆解：An inter-scale stiffness propagation method with nonintrusive modeling of stochastic porosity in unidirectional composites

> 生成依据：`801/cleantext/026-An-inter-scale-stiffness-propagation-method-with-_2026_Computer-Methods-in-A`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`026-An-inter-scale-stiffness-propagation-method-with-_2026_Computer-Methods-in-A`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\An-inter-scale-stiffness-propagation-method-with-_2026_Computer-Methods-in-A.pdf`
- 页数：22
- clean body 字符数：70902
- 摘要字符数：1809
- 参考文献条数：55
- 图题数：24
- 表题数：10
- 表格文件数：11
- 公式候选数：286
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "40 formula(s) need manual review."}]

## 1. 身份层

- 标题：An inter-scale stiffness propagation method with nonintrusive modeling of stochastic porosity in unidirectional composites
- 年份：2026
- 期刊/来源：Computer Methods in A
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：实验/测量 + 性能分析型
- 研究对象：Quantifying this inherent stochasticity is therefore essential for reliable prediction and design of composite structures. These constraints highlight the need for variance-aware modeling strategies that remain accurate at finite, feasible volumes rather than relying on asymptotically large RVEs [18].
- 主要方法：However, explicitly modeling pores with prescribed geometry at the composite-scale leads to prohibitive computational cost for uncertainty quantification. This study proposes an inter-scale stiffness propagation method linking matrix-scale stochastic porosity to stiffness uncertainty of unidirec tional fiber-reinforced (UD) composites. In such nonintrusive modeling of porosity, the local volume effect strongly influences the quantification accuracy.
- 主要证据：图表 34 个标题、公式 286 个候选、参考文献 55 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“Quantifying this inherent stochasticity is therefore essential for reliable prediction and design of composite structures. These constraints highlight the need for variance-aware m”，可以通过“However, explicitly modeling pores with prescribed geometry at the composite-scale leads to prohibitive computational cost for uncertainty quantification. This study proposes an inter-scale stiffness propagation method l”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：The results show that the nonintrusive modeling of stochastic porosity enables reliable stiffness propagation and efficient pore-induced uncertainty quantification. Fiber-reinforced composites achieve high specific stiffness and strength by embedding stiff fibers in matrix; yet microstructural variability - irregular fiber packing and matrix porosity - almost inevitably arises during manufacturing [1,2]. In particular, pores that form in the matrix regions between fibers can further reduce stiffness; studies on short-glass-fiber thermoplastics with random orientations have shown that even modest increases in porosity may lead to appreciable decreases in the effective Young’s modulus [4].
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：Quantifying this inherent stochasticity is therefore essential for reliable prediction and design of composite structures. These constraints highlight the need for variance-aware modeling strategies that remain accurate at finite, feasible volumes rather than relying on asymptotically large RVEs [18].
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
- 作者声明或文本中可见 gap：However, explicitly modeling pores with prescribed geometry at the composite-scale leads to prohibitive computational cost for uncertainty quantification. In practice, RVEs cannot be enlarged indefinitely because high-fidelity simulations of very large domains are computationally prohibitive, particularly for architectures lacking clear scale separation [18]. These constraints highlight the need for variance-aware modeling strategies that remain accurate at finite, feasible volumes rather than relying on asymptotically large RVEs [18].
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- In practice, RVEs cannot be enlarged indefinitely because high-fidelity simulations of very large domains are computationally prohibitive, particularly for architectures lacking clear scale separation [18].
- These constraints highlight the need for variance-aware modeling strategies that remain accurate at finite, feasible volumes rather than relying on asymptotically large RVEs [18].
- Moreover, pore statistics measured from a few exemplars carry epistemic uncertainty (incomplete distributional knowledge) in addition to aleatory variability [37].
- In practice, manufacturers often treat a porosity below ${\sim} 2$ % as acceptable [38], but lack confidence in how rarer or larger pores might affect performance.

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：However, explicitly modeling pores with prescribed geometry at the composite-scale leads to prohibitive computational cost for uncertainty quantification. This study proposes an inter-scale stiffness propagation method linking matrix-scale stochastic porosity to stiffness uncertainty of unidirec tional fiber-reinforced (UD) composites. In such nonintrusive modeling of porosity, the local volume effect strongly influences the quantification accuracy.
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
| This study proposes an inter-scale stiffness propagation method linking matrix-scale stochastic porosity to stiffness uncertainty of unidirec tional fiber-reinforced (UD) composites. | 摘要/引言/结论候选 | 图：Fig. 1. Representative stochastic pore realizations under different Poisson intensities and radius-distribution parameters. The parameter values shown here are chosen for illustrative purposes only and do not correspond quantitatively to the simulation input | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Finally, the stiffness calculation model at the composite-scale is developed, and the uncertainty induced by pores at the matrix-scale is quantified by Monte Carlo simulation. | 摘要/引言/结论候选 | 图：Fig. 2. Definition of the sampling distance r and local volumes V1, V2 in the Monte Carlo scheme for estimating the cross-volume covariance of local | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The results show that the nonintrusive modeling of stochastic porosity enables reliable stiffness propagation and efficient pore-induced uncertainty quantification. | 摘要/引言/结论候选 | 图：Fig. 3. Representative pore realizations of the matrix RVEs with four normalized sizes, used to analyze variance-volume scaling and cross-property correlations. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Fiber-reinforced composites achieve high specific stiffness and strength by embedding stiff fibers in matrix; yet microstructural variability - irregular fiber packing and matrix porosity - almost inevitably arises during manufacturing [1,2]. | 摘要/引言/结论候选 | 表：Table 1 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In particular, pores that form in the matrix regions between fibers can further reduce stiffness; studies on short-glass-fiber thermoplastics with random orientations have shown that even modest increases in porosity may lead to appreciable decreases in the ef | 摘要/引言/结论候选 | 表：Table 2 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Inter-scale stochastic modeling offers a rational method to link matrix-scale stochasticity with composite-scale response by homogenizing over a representative volume element (RVE) while tracking the propagation of statistical fluctuations. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (39.0, 203.61, 375.12, 234.3)]] Yu-Cheng Yang a, Zi-Qian Wang a, Jian- | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Representative stochastic pore realizations under different Poisson intensities and radius-distribution parameters. The parameter values shown here are  | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 2. Definition of the sampling distance r and local volumes V1, V2 in the Monte Carlo scheme for estimating the cross-volume covariance of local | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 3. Representative pore realizations of the matrix RVEs with four normalized sizes, used to analyze variance-volume scaling and cross-property correlations. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4. Geometry and FE schematic of the three normalized fiber-bundle RVEs. (a) Geometric configuration of the RVEb with embedded pores. (b) FE meshes used for | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 5. Histograms of sampled pore radii and corresponding pore volumes derived from the truncated Gaussian distribution, serving as the input statistics for th | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 6. Indicator covariance kernel CY(r) computed from the stochastic pore realizations, showing an exponential decay with separation and a correlation length  | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 7. Monte Carlo analysis of the covariance of local porosity fields. (a) Covariance Cmodel ϕ plotted against V2 for several fixed V1 and correlation | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 8. Residual diagnostics for the Mat´ern-kernel fit of the covariance model. (a-c) Residuals versus separation distance R, geometric mean volume Vg, and the | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 9. Variance-volume power-law fits (log-log) for porosity and effective moduli. Fitted data and corresponding regression lines are shown for each property;  | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 10. Leave-one-volume-out validation of the variance-volume power-law model. Each point compares the empirical variance at the held-out volume with the corr | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 11. Correlation between porosity and homogenized mechanical properties across sampling volumes, with 95 % Fisher confidence bands. (a) Correlations ρ(X, Φ) | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. Frobenius-distance analysis of correlation matrices across RVE volumes. (a) Engineering constants (E, ν, G), showing slightly larger dis tances at smal | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 13. Parity comparison of empirical and modeled covariance entries across sampling volumes. The close alignment along the 1:1 line indicates that the covari | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 14. Variance-volume power-law fits (log-log) for homogenized composite properties across RVEb1, RVEb2 and RVEb3. Linear trends with slopes αi ≈1 confirm th | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 15. Correlation between stiffness components and porosity ρ(Xi, Φ) versus sampling volume V for the composite-scale RVEs (Fisher 95 % confidence bands). Th | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 7 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 8 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 9 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 11 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (39.0, 203.61, 375.12, 234.3)]] Yu-Cheng Yang a, Zi-Qian Wang a, Jian-Jun Gou a,* , Xiao-B | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (44.05, 612.44, 205.56, 633.69)]] * Corresponding author. E-mail address: jj.gou@nwpu.edu. | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (39.0, 642.88, 372.42, 664.19)]] https://doi.org/10.1016/j.cma.2025.118720 R | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (62.93, 137.36, 114.99, 150.39)]] P{N(V) = k} = | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (127.5, 137.36, 507.57, 155.89)]] k! e-λp\|V\|, k = 0, 1, 2, … (1) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 4, bbox (39.01, 156.75, 507.59, 180.27)]] Counts on disjoint subsets are independent | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (62.93, 216.5, 101.09, 240.01)]] fR(r) = 1 σ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 4, bbox (82.77, 292.23, 110.45, 311.42)]] ) = ⋃ N(ω) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> A B S T R A C T
> Porosity is a primary source of stiffness uncertainty in fiber-reinforced composites. However, explicitly modeling pores with prescribed geometry at the composite-scale leads to prohibitive computational cost for uncertainty quantification. This study proposes an inter-scale stiffness propagation method linking matrix-scale stochastic porosity to stiffness uncertainty of unidirec tional fiber-reinforced (UD) composites. In such nonintrusive modeling of porosity, the local volume effect strongly influences the quantification accuracy. Pores in the matrix are modeled as spheres distributed by a Poisson point process. Their radius follows a truncated Gaussian law, leading to a porosity field whose covariance follows a Mat´ern-type form independent of local volume. The decay of porosity variance with increasing volume size, attributed to local volume
> * Corresponding author. E-mail address: jj.gou@nwpu.edu.cn (J.-J. Gou).
> https://doi.org/10.1016/j.cma.2025.118720 Received 28 October 2025; Received in revised form 15 December 2025; Accepted 29 December 2025
> averaging, is confirmed, indicating a similar behavior in finite element (FE) homogenization at the matrix-scale. The variance of matrix stiffness is found to decrease with growing local volume size, and its consistent negative correlation with porosity is thereby established. The stiffness- porosity joint distribution is then constructed by the conditional Gaussian mapping method. Finally, the stiffness calculation model at the composite-scale is developed, and the uncertainty induced by pores at the matrix-scale is quantified by Monte Carlo simulation. The results show that the nonintrusive modeling of stochastic porosity enables reliable stiffness propagation and efficient pore-induced uncertainty quantification.

### 7.4 摘要中文翻译

> 摘要 孔隙率是纤维增强复合材料刚度不确定性的主要来源。然而，在复合尺度上使用规定的几何形状对孔隙进行显式建模会导致不确定性量化的计算成本过高。本研究提出了一种将矩阵尺度随机孔隙率与单向纤维增强（UD）复合材料的刚度不确定性联系起来的尺度间刚度传播方法。在这种非侵入式孔隙率建模中，局部体积效应强烈影响量化精度。基质中的孔隙被建模为通过泊松点过程分布的球体。它们的半径遵循截断高斯定律，导致孔隙率场的协方差遵循与局部体积无关的马特恩型形式。孔隙率方差随着体积尺寸的增加而衰减，归因于局部体积*通讯作者。电子邮箱地址：jj.gou@nwpu.edu.cn（J.-J. Gou）。 https://doi.org/10.1016/j.cma.2025.118720 2025 年 10 月 28 日收到； 2025 年 12 月 15 日收到修订版； 2025 年 12 月 29 日接受的平均值已得到确认，表明矩阵尺度的有限元 (FE) 均质化具有类似的行为。发现基体刚度的方差随着局部体积尺寸的增大而减小，从而建立了其与孔隙率一致的负相关关系。然后通过条件高斯映射方法构建刚度-孔隙度联合分布。最后，建立了复合尺度的刚度计算模型，并通过蒙特卡罗模拟量化了基体尺度孔隙引起的不确定性。结果表明，随机孔隙度的非侵入式建模能够实现可靠的刚度传播和有效的孔隙引起的不确定性量化。

### 7.5 结论完整摘录

识别到的结论位置：8. Conclusion

> This study presents a nonintrusive, RVE-based inter-scale method for propagating stochastic porosity effects from the matrix scale to stiffness uncertainty in UD composites. The proposed method integrates stochastic geometry, FE homogenization, and Monte Carlo sampling into a unified multiscale uncertainty-quantification process. Some conclusions are obtained:
> 
> (1) At the matrix-scale, pores are represented by a Boolean model consisting of Poisson-distributed centers and truncated-Gaussian radii. The resulting porosity field exhibits Mat´ern-type spatial covariance and variance-volume scaling governed by local statistical averaging. This model captures both spatial correlation and volume dependence of porosity and can be directly superimposed on standard FE analyses compatible with the deterministic mechanics solver.
> 
> (2) High-fidelity homogenization of porous-matrix RVEs establishes a quantitative stiffness-porosity relationship. The variance of stiffness components decays with increasing averaging volume following a power-law form, whereas the stiffness-porosity correlation remains strongly negative and nearly volume-invariant over the scales investigated. These trends provide a quan titative basis for selecting statistically representative RVE sizes and for constructing inter-scale stochastic mappings.
> 
> (3) Comprehensive uncertainty propagation from pore geometry to composite-scale material properties is achieved through a twostage Monte Carlo construction. The resulting porosity and element-wise stiffness fields provide statistically consistent inputs for composite-scale FE analyses, enabling efficient and reliable quantification of pore-induced stiffness uncertainty.
> 
> Overall, the proposed inter-scale method offers a physics-consistent and computationally feasible route for incorporating stochastic porosity into composite-scale analyses. It provides practical support for reliability-oriented design and quality assessment of UD
> 
> composites.

### 7.6 结论中文翻译

> 本研究提出了一种非侵入式、基于 RVE 的跨尺度方法，用于将随机孔隙率效应从基体尺度传播到 UD 复合材料的刚度不确定性。该方法将随机几何、有限元均质化和蒙特卡洛采样集成到统一的多尺度不确定性量化过程中。得到了一些结论：(1)在矩阵尺度上，孔隙由泊松分布中心和截断高斯半径组成的布尔模型表示。由此产生的孔隙度场表现出马特恩型空间协方差和由局部统计平均控制的方差体积缩放。该模型捕获了孔隙率的空间相关性和体积依赖性，并且可以直接叠加在与确定性力学求解器兼容的标准有限元分析上。 (2) 多孔基体 RVE 的高保真均质化建立了定量的刚度-孔隙率关系。刚度分量的方差随着幂律形式的平均体积的增加而衰减，而刚度-孔隙度相关性在研究的尺度上保持强烈的负值并且几乎体积不变。这些趋势为选择具有统计代表性的 RVE 大小和构建尺度间随机映射提供了定量基础。 (3)通过两级蒙特卡罗构造实现了从孔隙几何形状到复合尺度材料特性的综合不确定性传播。由此产生的孔隙率和单元刚度场为复合尺度有限元分析提供统计上一致的输入，从而能够有效、可靠地量化孔隙引起的刚度不确定性。
> 
> 总体而言，所提出的跨尺度方法为将随机孔隙率纳入复合尺度分析提供了物理一致且计算上可行的途径。它为UD复合材料的可靠性设计和质量评估提供了实际支持。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 8919 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. Inter-scale stiffness propagation method with stochastic porosity | 方法建构 | 2893 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 3 | 3. Matrix-scale RVE model of stochastic pores | 方法建构 | 4883 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 4. Statistical features and modeling of porosity field | 方法建构 | 501 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 5 | 4.1. Statistical features of pores field | 对象/条件/子问题展开 | 2787 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 4.2. Statistical features of porosity field | 对象/条件/子问题展开 | 6545 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 4.3. Statistical modeling of porosity field covariance | 方法建构 | 1134 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 8 | 5. Statistical feature of matrix-scale effective properties | 对象/条件/子问题展开 | 1061 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 5.1. Stiffness and porosity sampling of RVE size | 对象/条件/子问题展开 | 2553 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 5.2. FE-based homogenization procedure | 对象/条件/子问题展开 | 3188 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 5.3. Stiffness and porosity variance decay with RVE size | 对象/条件/子问题展开 | 1093 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 5.4. Joint distribution modeling of stiffness-porosity | 方法建构 | 3373 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 13 | 6.1. Nonintrusive mesh-level sampling in composite scale | 对象/条件/子问题展开 | 6079 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 6.2. Computational efficiency | 对象/条件/子问题展开 | 3339 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 15 | 7. Results and discussions | 结果验证/讨论 | 575 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 16 | 7.1. Statistical features of pore and porosity | 对象/条件/子问题展开 | 3284 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 17 | 7.2. Joint distribution of stiffness-porosity | 对象/条件/子问题展开 | 7791 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 18 | 7.3. Mesh independence and correlation discretization effects | 对象/条件/子问题展开 | 3630 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 19 | 7.4. Stochastic FE demonstration | 对象/条件/子问题展开 | 3877 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 20 | 8. Conclusion | 主张回收/边界说明 | 1978 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 21 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 296 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：phi(125)；mathrm(106)；porosity(83)；mathbf(71)；sigma(55)；stiffness(52)；covariance(48)；big(48)；stochastic(45)；tag(44)；pore(43)；volume(41)；correlation(40)；rve(39)；left(38)；right(37)；local(33)；matrix(31)；volumes(31)；pores(28)
- 高频学术名词/术语：porosity(83)；stiffness(52)；covariance(48)；correlation(40)；variance(24)；statistics(24)；homogenization(19)；section(19)；distance(17)；variability(15)；element(14)；distribution(14)；structure(14)；realization(14)；propagation(11)
- 高频学术动词：obtained(11)；evaluated(6)；introduced(5)；estimated(4)；constructed(3)；compared(3)；evaluate(3)；validate(2)；reveal(2)；presented(2)；developed(2)；demonstrate(2)；predicted(2)；indicate(2)；introduce(2)
- 高频形容词：stochastic(45)；local(33)；spatial(24)；effective(23)；consistent(18)；statistical(17)；mathcal(17)；nonintrusive(15)；element(14)；table(14)；independent(12)；spherical(12)；volume-invariant(12)；normal(11)；geometric(10)
- 高频副词：nearly(10)；directly(8)；statistically(7)；primarily(6)；strongly(5)；consistently(5)；approximately(5)；computationally(4)；independently(4)；uniformly(4)；highly(4)；essentially(4)
- 高频二词短语：monte carlo(25)；sigma phi(23)；mathbf mathbf(22)；overline phi(13)；porosity field(12)；big big(12)；mathrm mathrm(12)；composite scale(11)；effective properties(10)；left right(10)；poisson ratios(10)；rho phi(10)；variance-volume scaling(9)；stochastic porosity(9)；mathbf omega(9)
- 高频三词短语：left varepsilon right(6)；phi mathbf phi(5)；mathbf mathbf mathbf(5)；phi big big(5)；sigma phi left(5)；mathrm rve mathrm(5)；mathbf phi mathbf(4)；mathbf mathbf big(4)；left sigma right(4)；sigma phi tag(4)；sigma phi big(4)；phi sigma phi(4)
- 被动语态估计：131
- `we + 动作动词` 主动句估计：2
- 一般现在时线索：237
- 一般过去时线索：414
- 现在完成时线索：4
- 情态动词线索：23

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Quantifying this inherent stochasticity is therefore essential for reliable prediction and design of composite structures.
  - 可迁移句型：{object} this inherent stochasticity is therefore essential for reliable prediction and design of composite structures.
- 原句：When the domain is below a critical threshold, statistical volume elements (SVEs) exhibit significant sample-to-sample variability; studies on carbon-fiber systems have identified the approximate critical RVE size [5].
  - 可迁移句型：{object} the domain is below a critical threshold, statistical volume elements (SVEs) exhibit significant sample-to-sample variability; studies on carbon-fiber systems have identified the approximate critical RVE size [5].
- 原句：To examine spatial variability, RVEs of different sizes are usually constructed: larger RVEs are suitable for periodic or translationally symmetric boundary conditions, while smaller RVEs are necessary to capture matrix-scale defects such as matrix pores between fibers and their impact on bundle scale mechanical properties [14–17].
  - 可迁移句型：{object} examine spatial variability, RVEs of different sizes are usually constructed: larger RVEs are suitable for periodic or translationally symmetric boundary conditions, while smaller RVEs are necessary to capture matrix-scale defects such as matrix pores
### gap/转折句
- 原句：However, explicitly modeling pores with prescribed geometry at the composite-scale leads to prohibitive computational cost for uncertainty quantification.
  - 可迁移句型：{object}, explicitly modeling pores with prescribed geometry at the composite-scale leads to prohibitive computational cost for uncertainty quantification.
- 原句：In practice, RVEs cannot be enlarged indefinitely because high-fidelity simulations of very large domains are computationally prohibitive, particularly for architectures lacking clear scale separation [18].
  - 可迁移句型：{object} practice, RVEs cannot be enlarged indefinitely because high-fidelity simulations of very large domains are computationally prohibitive, particularly for architectures lacking clear scale separation [18].
- 原句：These constraints highlight the need for variance-aware modeling strategies that remain accurate at finite, feasible volumes rather than relying on asymptotically large RVEs [18].
  - 可迁移句型：{object} constraints highlight the need for variance-aware modeling strategies that remain accurate at finite, feasible volumes rather than relying on asymptotically large RVEs [18].
- 原句：Numerical experiments demonstrate that the mean stiffness is nearly volume-invariant; the variance follows a power-law decay $\operatorname{Var} [ X _ {i} ( V ) ] = B _ {i} | V | ^ {- \alpha _ {i}}$ ; and the correlation between X and $\phi _ {V}$ remains strong and almost independent of the volume.
  - 可迁移句型：{object} experiments demonstrate that the mean stiffness is nearly volume-invariant; the variance follows a power-law decay $\operatorname{Var} [ X _ {i} ( V ) ] = B _ {i} | V | ^ {- \alpha _ {i}}$ ; and the correlation between X and $\phi _ {V}$ remains stron
### 方法提出句
- 原句：However, explicitly modeling pores with prescribed geometry at the composite-scale leads to prohibitive computational cost for uncertainty quantification.
  - 可迁移句型：{object}, explicitly modeling pores with prescribed geometry at the composite-scale leads to prohibitive computational cost for uncertainty quantification.
- 原句：This study proposes an inter-scale stiffness propagation method linking matrix-scale stochastic porosity to stiffness uncertainty of unidirec tional fiber-reinforced (UD) composites.
  - 可迁移句型：{object} study proposes an inter-scale stiffness propagation method linking matrix-scale stochastic porosity to stiffness uncertainty of unidirec tional fiber-reinforced (UD) composites.
- 原句：In such nonintrusive modeling of porosity, the local volume effect strongly influences the quantification accuracy.
  - 可迁移句型：{object} such nonintrusive modeling of porosity, the local volume effect strongly influences the quantification accuracy.
- 原句：Pores in the matrix are modeled as spheres distributed by a Poisson point process.
  - 可迁移句型：{object} in the matrix are modeled as spheres distributed by a Poisson point process.
### 结果证明句
- 原句：The results show that the nonintrusive modeling of stochastic porosity enables reliable stiffness propagation and efficient pore-induced uncertainty quantification.
  - 可迁移句型：{object} results show that the nonintrusive modeling of stochastic porosity enables reliable stiffness propagation and efficient pore-induced uncertainty quantification.
- 原句：Fiber-reinforced composites achieve high specific stiffness and strength by embedding stiff fibers in matrix; yet microstructural variability - irregular fiber packing and matrix porosity - almost inevitably arises during manufacturing [1,2].
  - 可迁移句型：{object} composites achieve high specific stiffness and strength by embedding stiff fibers in matrix; yet microstructural variability - irregular fiber packing and matrix porosity - almost inevitably arises during manufacturing [1,2].
- 原句：In particular, pores that form in the matrix regions between fibers can further reduce stiffness; studies on short-glass-fiber thermoplastics with random orientations have shown that even modest increases in porosity may lead to appreciable decreases in the effective Young’s modulus [4].
  - 可迁移句型：{object} particular, pores that form in the matrix regions between fibers can further reduce stiffness; studies on short-glass-fiber thermoplastics with random orientations have shown that even modest increases in porosity may lead to appreciable decreases in 
- 原句：Numerical experiments demonstrate that the mean stiffness is nearly volume-invariant; the variance follows a power-law decay $\operatorname{Var} [ X _ {i} ( V ) ] = B _ {i} | V | ^ {- \alpha _ {i}}$ ; and the correlation between X and $\phi _ {V}$ remains strong and almost independent of the volume.
  - 可迁移句型：{object} experiments demonstrate that the mean stiffness is nearly volume-invariant; the variance follows a power-law decay $\operatorname{Var} [ X _ {i} ( V ) ] = B _ {i} | V | ^ {- \alpha _ {i}}$ ; and the correlation between X and $\phi _ {V}$ remains stron
### 贡献收束句
- 原句：The results show that the nonintrusive modeling of stochastic porosity enables reliable stiffness propagation and efficient pore-induced uncertainty quantification.
  - 可迁移句型：{object} results show that the nonintrusive modeling of stochastic porosity enables reliable stiffness propagation and efficient pore-induced uncertainty quantification.
- 原句：In particular, pores that form in the matrix regions between fibers can further reduce stiffness; studies on short-glass-fiber thermoplastics with random orientations have shown that even modest increases in porosity may lead to appreciable decreases in the effective Young’s modulus [4].
  - 可迁移句型：{object} particular, pores that form in the matrix regions between fibers can further reduce stiffness; studies on short-glass-fiber thermoplastics with random orientations have shown that even modest increases in porosity may lead to appreciable decreases in 
- 原句：By introducing explicit spatial correlation and scale dependence, the proposed method enables stochastic propagation from the matrix scale to t A nonintrusive, RVE-based inter-scale method is developed to propagate stochastic porosity effects from the matrix-scale to the stiffness field.
  - 可迁移句型：{object} introducing explicit spatial correlation and scale dependence, the proposed method enables stochastic propagation from the matrix scale to t A nonintrusive, RVE-based inter-scale method is developed to propagate stochastic porosity effects from the ma
- 原句：This compact, physics-based generator allows direct control of the mean porosity and provides the stochastic input for all composite-scale statistics.
  - 可迁移句型：{object} compact, physics-based generator allows direct control of the mean porosity and provides the stochastic input for all composite-scale statistics.
### 边界/谨慎句
- 原句：In particular, pores that form in the matrix regions between fibers can further reduce stiffness; studies on short-glass-fiber thermoplastics with random orientations have shown that even modest increases in porosity may lead to appreciable decreases in the effective Young’s modulus [4].
  - 可迁移句型：{object} particular, pores that form in the matrix regions between fibers can further reduce stiffness; studies on short-glass-fiber thermoplastics with random orientations have shown that even modest increases in porosity may lead to appreciable decreases in 
- 原句：A high-fidelity RVE model of a porous composite may contain hundreds of millions of elements, making it impractical for routine analysis [19].
  - 可迁移句型：{object} high-fidelity RVE model of a porous composite may contain hundreds of millions of elements, making it impractical for routine analysis [19].

## 9. 引用风险层

- 正文引用簇估计：28
- 参考文献条数：55
- 可识别年份条目数：68
- 2021 年及以后参考文献数：27
- 2010 年以前经典文献数：4
- 高频来源粗略识别：Methods Appl. Mech. Eng(6)；Struct(6)；Mech(3)；Sci. Manuf(2)；Mater(1)；Comput(1)；Neurosci(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- Lomov, Detailed characterization of voids in multidirectional carbon fiber/epoxy composite laminates using X-ray micro-computed tomography, Compos. A: Appl. Sci. Manuf. 125 (2019) 105532, https://doi.org/10.1016/j.compositesa.2019.105532. [2] S.H.R. Sanei, E.J. Barsotti, D. Leonhardt, R.S. FertigIII, Characterization, synthetic generation, and statistical equivalence of composite microstructures, J. Compos. Mater. 51 (2017) 1817–1829, https://doi.org/10.1177/0021998316662133. [3] M. Petrolo, A.
- Pagani, M.
- Trombini, E.
- Carrera, Voids effect on micromechanical response of elastoplastic fiber-reinforced polymer composites using 1D higher- order theories, Mech. Mater. 184 (2023) 104747, https://doi.org/10.1016/j.mechmat.2023.104747. [4] Porous materials reinforced with short fibers: unbiased full-field assessment of several homogenization strategies in elasticity: mechanics of Advanced Materials and Structures: Vol 29, No 20 - Get Access, (n.d.). https://www.tandfonline.com/doi/full/10.1080/15376494.2021.1880674 
- Savvas, G.
- Stefanou, M.
- Papadrakakis, Determination of RVE size for random composites with local volume fraction variation, Comput. Methods Appl. Mech. Eng. 305 (2016) 340–358, https://doi.org/10.1016/j.cma.2016.03.002. [8] T.H. Hoang, M. Guerich, J. Yvonnet, Determining the size of RVE for nonlinear random composites in an incremental computational homogenization framework, J. Eng. Mech. 142 (2016) 04016018, https://doi.org/10.1061/(ASCE)EM.1943-7889.0001057. [9] E. Ghossein, M. L´evesque, Homogenization models for pr
- Grigoriu, Stochastic Calculus: Applications in Science and Engineering, Springer Science & Business Media, 2013. [12] J. Ma, S. Sahraee, P. Wriggers, L. De Lorenzis, Stochastic multiscale homogenization analysis of heterogeneous materials under finite deformations with full uncertainty in the microstructure, Comput. Mech. 55 (2015) 819–835, https://doi.org/10.1007/s00466-015-1136-3. [13] S.R.
- Arwade, G.
- Deodatis, Variability response functions for effective material properties, Probabilistic Eng. Mech. 26 (2011) 174–181, https://doi.org/ 10.1016/j.probengmech.2010.11.005. [14] J.-J.
- Gou, H.
- Zhang, Y.-J.
- Dai, S.
- Li, W.-Q.
- Tao, Numerical prediction of effective thermal conductivities of 3D four-directional braided composites, Compos. Struct. 125 (2015) 499–508, https://doi.org/10.1016/j.compstruct.2015.02.009. [15] J.-J.

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
