# 论文深度拆解：Multidisciplinary uncertainty propagation method considering correlated field variables for rocket systems

> 生成依据：`801/cleantext/035-Multidisciplinary-uncertainty-propagation-method-cons_2025_Probabilistic-Eng`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`035-Multidisciplinary-uncertainty-propagation-method-cons_2025_Probabilistic-Eng`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\Multidisciplinary-uncertainty-propagation-method-cons_2025_Probabilistic-Eng.pdf`
- 页数：12
- clean body 字符数：38115
- 摘要字符数：1403
- 参考文献条数：28
- 图题数：14
- 表题数：8
- 表格文件数：8
- 公式候选数：221
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "low_confidence_formulas", "severity": "medium", "message": "35 formula(s) need manual review."}]

## 1. 身份层

- 标题：Multidisciplinary uncertainty propagation method considering correlated field variables for rocket systems
- 年份：2025
- 期刊/来源：Probabilistic Eng
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：实验/测量 + 性能分析型
- 研究对象：To improve performance and ensure reliability, accounting for these uncertainties at every design stage is essential [2,3]. Compared to numerical variables, quantifying correlations among field variables poses a substantially greater challenge. To address the challenge of incorporating correlations in UP, researchers have carried out extensive investigations [12–14].
- 主要方法：However, existing uncertainty propagation (UP) methods for multidisciplinary systems often neglect correlations among field variables, leading to reduced accuracy. To overcome this limitation, we propose a multidisciplinary UP method that explicitly incorporates these correlations. To accelerate the calculation of the probability density function of field variables within the Nataf transformation, we further introduce a warm-start strategy integrated with the maximum entropy method.
- 主要证据：图表 22 个标题、公式 221 个候选、参考文献 28 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“To improve performance and ensure reliability, accounting for these uncertainties at every design stage is essential [2,3]. Compared to numerical variables, quantifying correlation”，可以通过“However, existing uncertainty propagation (UP) methods for multidisciplinary systems often neglect correlations among field variables, leading to reduced accuracy. To overcome this limitation, we propose a multidisciplin”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：However, existing uncertainty propagation (UP) methods for multidisciplinary systems often neglect correlations among field variables, leading to reduced accuracy. In the case study of UP across multiple disciplines of a solid rocket system, using Monte Carlo simulation (MCS) as the benchmark, incorporating variable correlations yields notable improve ments: the standard deviation accuracy of velocity and total energy at the first-stage separation point increased by 22.75 % and 32.57 %, respectively, while the accuracy of their lower bounds improved by 5.20 % and 4.20 %. These results demonstrate that the proposed method effectively addresses UP problems involving both numerical and field correlated variables, significantly enhancing the accuracy of UP.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：To improve performance and ensure reliability, accounting for these uncertainties at every design stage is essential [2,3]. Compared to numerical variables, quantifying correlations among field variables poses a substantially greater challenge. To address the challenge of incorporating correlations in UP, researchers have carried out extensive investigations [12–14].
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
- 作者声明或文本中可见 gap：However, existing uncertainty propagation (UP) methods for multidisciplinary systems often neglect correlations among field variables, leading to reduced accuracy. In the case study of UP across multiple disciplines of a solid rocket system, using Monte Carlo simulation (MCS) as the benchmark, incorporating variable correlations yields notable improve ments: the standard deviation accuracy of velocity and total energy at the first-stage separation point increased by 22.75 % and 32.57 %, respectively, while the accuracy of their lower bounds improved by 5.20 % and 4.20 %. By explicitly considering the interactions and synergies among different disciplines, UMDO not only enhances overall system performance but also reduces development costs and shortens the design cycle [7–9].
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- To address the challenge of incorporating correlations in UP, researchers have carried out extensive investigations [12–14].

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：However, existing uncertainty propagation (UP) methods for multidisciplinary systems often neglect correlations among field variables, leading to reduced accuracy. To overcome this limitation, we propose a multidisciplinary UP method that explicitly incorporates these correlations. To accelerate the calculation of the probability density function of field variables within the Nataf transformation, we further introduce a warm-start strategy integrated with the maximum entropy method.
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
| To overcome this limitation, we propose a multidisciplinary UP method that explicitly incorporates these correlations. | 摘要/引言/结论候选 | 图：Fig. 1. Illustration of multidisciplinary UP. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In the case study of UP across multiple disciplines of a solid rocket system, using Monte Carlo simulation (MCS) as the benchmark, incorporating variable correlations yields notable improve ments: the standard deviation accuracy of velocity and total energy at | 摘要/引言/结论候选 | 图：Fig. 2. Flowchart of multidisciplinary UP considering variable correlations in a specific discipline. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| These results demonstrate that the proposed method effectively addresses UP problems involving both numerical and field correlated variables, significantly enhancing the accuracy of UP. | 摘要/引言/结论候选 | 图：Fig. 3. Procedure for processing propagation data. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| To improve performance and ensure reliability, accounting for these uncertainties at every design stage is essential [2,3]. | 摘要/引言/结论候选 | 表：Table 1 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| By explicitly considering the interactions and synergies among different disciplines, UMDO not only enhances overall system performance but also reduces development costs and shortens the design cycle [7–9]. | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| These correlations must be properly considered to ensure accurate results of UP. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 200.1, 690.38)]] * Corresponding author. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Illustration of multidisciplinary UP. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 2. Flowchart of multidisciplinary UP considering variable correlations in a specific discipline. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 3. Procedure for processing propagation data. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 4. Procedure of correlation transformation for both numerical and field samples. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 5. Process of the improved Nataf transformation method based on warm-start-based maximum entropy. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 7. Comparison of correlation coefficients computed between field samples c1 and c2 | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 8. PDF of output variable e. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 9. Relationship of UP in the solid rocket system. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 10. Comparison of correlation among the numerical variables and the mode coefficients in the engine discipline. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 11. Comparison of correlation between thrust and mass in the engine discipline. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 12. Comparison of PDFs for the velocity at the first-stage rocket separation point. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 13. Comparison of PDFs for the total energy at the first-stage rocket separation point. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 6. UP relations in the analytical test. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 7. Comparison of correlation coefficients computed between field samples $\pmb { c } _ { 1 }$ and $\pmb { c } _ { 2 }$ | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 7 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 8 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 200.1, 690.38)]] * Corresponding author. E-mail address: chu | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 348.83, 716.91)]] https://doi.org/10.1016/j.probengmech.2025 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 3, bbox (37.59, 558.29, 205.15, 578.51)]] level, the output samples XC = [ xC 1,⋯,xC | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 3, bbox (318.5, 610.33, 387.48, 627.87)]] ρF = [ρF1, ρF2, ⋯, ρFNi | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (61.57, 640.83, 198.06, 661.11)]] ] and field samples SC F = [ xC n+1,⋯,xC n+f | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.6, 392.07, 560.01, 406.27)]] aj = SC Fjφ-1 j (j ∈{1, …, f}), (1) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (318.5, 513.49, 559.99, 527.88)]] definition. For xC j (j ∈{n + 1,…,n + f}), their statist | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 3, bbox (318.5, 647.56, 559.98, 673.81)]] cient matrix of the data in the jth dimens | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> Throughout a rocket’s lifecycle, numerous random uncertainties can significantly influence performance. However, existing uncertainty propagation (UP) methods for multidisciplinary systems often neglect correlations among field variables, leading to reduced accuracy. To overcome this limitation, we propose a multidisciplinary UP method that explicitly incorporates these correlations. For variables propagated from upper-level disciplines, the Nataf transformation is applied to generate correlated input samples for the current discipline, which then serve as the basis for uncertainty analysis. To accelerate the calculation of the probability density function of field variables within the Nataf transformation, we further introduce a warm-start strategy integrated with the maximum entropy method. In the case study of UP across multiple disciplines of a solid rocket system, using Monte Carlo simulation (MCS) as the benchmark, incorporating variable correlations yields notable improve ments: the standard deviation accuracy of velocity and total energy at the first-stage separation point increased by 22.75 % and 32.57 %, respectively, while the accuracy of their lower bounds improved by 5.20 % and 4.20 %. These results demonstrate that the proposed method effectively addresses UP problems involving both numerical and field correlated variables, significantly enhancing the accuracy of UP.

### 7.4 摘要中文翻译

> 在火箭的整个生命周期中，大量的随机不确定性会显着影响性能。然而，现有的多学科系统的不确定性传播（UP）方法经常忽略场变量之间的相关性，导致精度降低。为了克服这一限制，我们提出了一种明确包含这些相关性的多学科 UP 方法。对于上层学科传播的变量，应用Nataf变换生成当前学科的相关输入样本，作为不确定性分析的基础。为了加速 Nataf 变换中场变量概率密度函数的计算，我们进一步引入了与最大熵方法相结合的热启动策略。在固体火箭系统多学科UP案例研究中，以蒙特卡洛模拟（MCS）为基准，引入变量相关性，取得了显着的改进：第一级分离点速度和总能量的标准差精度分别提高了22.75%和32.57%，下界精度提高了5.20%和4.20%。这些结果表明，所提出的方法有效地解决了涉及数值和场相关变量的UP问题，显着提高了UP的准确性。

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusion

> In this study, we propose a multidisciplinary UP method that accounts for correlations among field state variables during propagation. The main conclusions are as follows.
> 
> 1) Using the improved Nataf transformation with a warm-start-based maximum entropy approach, correlated field variables can be accurately generated. In the solid rocket case, the maximum error of the resampled field samples was 3.08 %.
> 
> 2) By introducing a reference during correlation transformation, the method handles both numerical and field variables. In the solid rocket study, this enabled correlation transformation for key time points (numerical) as well as thrust and mass (field variables).
> 
> 3) The proposed method enhances the accuracy of multidisciplinary UP for complex systems. Specifically, for the solid rocket system, the standard deviation accuracy of velocity and total energy at first-stage separation improved by 22.75 % and 32.57 %, respectively, while the lower-bound accuracy improved by 5.20 % and 4.20 %, respectively.
> 
> Notably, the proposed method requires correlated field variables to have the same dimension. Future work could address this limitation by introducing a preprocessing step to unify field variable dimensions before UP analysis, with the approach tailored to the characteristics of each problem.

### 7.6 结论中文翻译

> 在本研究中，我们提出了一种多学科 UP 方法，该方法可以解释传播过程中场状态变量之间的相关性。主要结论如下。 1）使用改进的Nataf变换和基于热启动的最大熵方法，可以准确地生成相关场变量。在固体火箭情况下，重采样现场样本的最大误差为 3.08%。 2）通过在相关变换过程中引入参考，该方法可以处理数值变量和场变量。在固体火箭研究中，这使得关键时间点（数值）以及推力和质量（场变量）能够进行相关变换。 3）所提出的方法提高了复杂系统多学科UP的准确性。其中，固体火箭系统第一级分离速度和总能量标准差精度分别提高了22.75%和32.57%，下限精度分别提高了5.20%和4.20%。值得注意的是，所提出的方法要求相关场变量具有相同的维度。未来的工作可以通过在 UP 分析之前引入预处理步骤来统一场变量维度，并根据每个问题的特征定制方法来解决这一限制。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 4826 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2.1. Multidisciplinary uncertainty propagation process considering correlated field variables | 对象/条件/子问题展开 | 7018 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 2.2. Correlation transformation method for both numerical and field samples | 方法建构 | 6351 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 2.2.2. Nataf transformation | 对象/条件/子问题展开 | 3286 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 2.2.3. Maximum entropy method | 方法建构 | 3298 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 6 | 2.3. POD method | 方法建构 | 1937 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 7 | 3. Method validation by the analytical test | 方法建构 | 4211 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 8 | 4.1. Problem description | 对象/条件/子问题展开 | 2009 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 4.2. Uncertainty propagation analysis of the solid rocket system considering field variable correlations | 结果验证/讨论 | 2810 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 10 | 5. Conclusion | 主张回收/边界说明 | 1312 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 11 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 313 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：pmb(157)；mathrm(156)；variables(72)；samples(61)；field(56)；widehat(48)；left(45)；right(45)；correlation(39)；numerical(36)；rho(32)；correlations(29)；transformation(27)；tag(27)；cdots(24)；multidisciplinary(22)；uncertainty(21)；among(21)；variable(21)；input(21)
- 高频学术名词/术语：correlation(39)；transformation(27)；reference(11)；function(9)；propagation(9)；optimization(6)；probability(6)；velocity(6)；distribution(5)；density(5)；section(5)；dimensionality(5)；deviation(5)；skewness(5)；separation(5)
- 高频学术动词：obtained(11)；obtain(4)；compared(3)；introduce(3)；presented(3)；propose(2)；indicate(2)；estimate(1)；estimated(1)；constructed(1)；validate(1)；evaluate(1)
- 高频形容词：numerical(36)；multidisciplinary(22)；variable(21)；coefficient(21)；independent(15)；statistical(13)；normal(11)；current(8)；original(8)；previous(7)；relative(6)；total(6)；aerodynamic(6)；analytical(4)；specific(4)
- 高频副词：respectively(12)；subsequently(5)；accurately(5)；usually(4)；directly(3)；typically(3)；similarly(3)；effectively(3)；closely(3)；explicitly(2)；primarily(2)；significantly(2)
- 高频二词短语：pmb mathrm(84)；widehat pmb(47)；mathrm mathrm(26)；pmb pmb(24)；field variables(20)；field samples(19)；mathrm cdots(16)；correlation coefficient(15)；maximum entropy(14)；correlations among(13)；rho mathrm(13)；nataf transformation(12)；mathrm left(12)；mathrm right(12)；samples widehat(12)
- 高频三词短语：widehat pmb mathrm(46)；pmb mathrm cdots(14)；pmb mathrm mathrm(13)；samples widehat pmb(12)；pmb mathrm right(11)；samples pmb mathrm(10)；mathrm widehat pmb(9)；cdots widehat pmb(9)；int infty infty(9)；correlation coefficient matrix(8)；pmb pmb pmb(8)；pmb rho mathrm(8)
- 被动语态估计：68
- `we + 动作动词` 主动句估计：6
- 一般现在时线索：133
- 一般过去时线索：216
- 现在完成时线索：2
- 情态动词线索：18

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Rockets, as critical spacecraft transportation systems, are exposed to random uncertainties throughout their lifecycle due to complex design, fabrication processes, and flight environments [1].
  - 可迁移句型：{object}, as critical spacecraft transportation systems, are exposed to random uncertainties throughout their lifecycle due to complex design, fabrication processes, and flight environments [1].
- 原句：To improve performance and ensure reliability, accounting for these uncertainties at every design stage is essential [2,3].
  - 可迁移句型：{object} improve performance and ensure reliability, accounting for these uncertainties at every design stage is essential [2,3].
- 原句：Given the complexity and inherently multidisciplinary nature of rocket systems, decoupling the system during UP is often necessary.
  - 可迁移句型：{object} the complexity and inherently multidisciplinary nature of rocket systems, decoupling the system during UP is often necessary.
- 原句：However, existing studies have not yet addressed multidisciplinary UP with correlated fiel The Nataf transformation requires selecting a reference variable, relative to which samples of other variables are transformed using the provided correlation coefficient matrix.
  - 可迁移句型：{object}, existing studies have not yet addressed multidisciplinary UP with correlated fiel The Nataf transformation requires selecting a reference variable, relative to which samples of other variables are transformed using the provided correlation coefficien
### gap/转折句
- 原句：However, existing uncertainty propagation (UP) methods for multidisciplinary systems often neglect correlations among field variables, leading to reduced accuracy.
  - 可迁移句型：{object}, existing uncertainty propagation (UP) methods for multidisciplinary systems often neglect correlations among field variables, leading to reduced accuracy.
- 原句：Within the UMDO process, however, the accuracy of multidisciplinary UP is crucial, as it directly affects the reliability of design outcomes.
  - 可迁移句型：{object} the UMDO process, however, the accuracy of multidisciplinary UP is crucial, as it directly affects the reliability of design outcomes.
- 原句：However, decoupling introduces a major limitation: correlations among state variables are usually neglected, leading to reduced accuracy in the independent UP process.
  - 可迁移句型：{object}, decoupling introduces a major limitation: correlations among state variables are usually neglected, leading to reduced accuracy in the independent UP process.
- 原句：Compared to numerical variables, quantifying correlations among field variables poses a substantially greater challenge.
  - 可迁移句型：{object} to numerical variables, quantifying correlations among field variables poses a substantially greater challenge.
### 方法提出句
- 原句：However, existing uncertainty propagation (UP) methods for multidisciplinary systems often neglect correlations among field variables, leading to reduced accuracy.
  - 可迁移句型：{object}, existing uncertainty propagation (UP) methods for multidisciplinary systems often neglect correlations among field variables, leading to reduced accuracy.
- 原句：To overcome this limitation, we propose a multidisciplinary UP method that explicitly incorporates these correlations.
  - 可迁移句型：{object} overcome this limitation, we propose a multidisciplinary UP method that explicitly incorporates these correlations.
- 原句：To accelerate the calculation of the probability density function of field variables within the Nataf transformation, we further introduce a warm-start strategy integrated with the maximum entropy method.
  - 可迁移句型：{object} accelerate the calculation of the probability density function of field variables within the Nataf transformation, we further introduce a warm-start strategy integrated with the maximum entropy method.
- 原句：These results demonstrate that the proposed method effectively addresses UP problems involving both numerical and field correlated variables, significantly enhancing the accuracy of UP.
  - 可迁移句型：{object} results demonstrate that the proposed method effectively addresses UP problems involving both numerical and field correlated variables, significantly enhancing the accuracy of UP.
### 结果证明句
- 原句：These results demonstrate that the proposed method effectively addresses UP problems involving both numerical and field correlated variables, significantly enhancing the accuracy of UP.
  - 可迁移句型：{object} results demonstrate that the proposed method effectively addresses UP problems involving both numerical and field correlated variables, significantly enhancing the accuracy of UP.
- 原句：These correlations must be properly considered to ensure accurate results of UP.
  - 可迁移句型：{object} correlations must be properly considered to ensure accurate results of UP.
- 原句：In general, the choice of reference variable does not significantly affect the transformation results.
  - 可迁移句型：{object} general, the choice of reference variable does not significantly affect the transformation results.
- 原句：To achieve the correlation transformation of both numerical and field samples, the method selects a certain field sample $\pmb {x} _ {j} ^ {\mathrm{I}} ( j \in \{n + 1 , . . . , n + f \} )$ and its corresponding resampled mode coefficient matrix $\widehat {\pmb {a}} _ {j} ^ {\mathrm{I}} ( j \in \{1 , . . . , f \} )$ as the reference for the transformation of other field samples and numerical samples, respectively.
  - 可迁移句型：{object} achieve the correlation transformation of both numerical and field samples, the method selects a certain field sample $\pmb {x} _ {j} ^ {\mathrm{I}} ( j \in \{n + 1 , . . . , n + f \} )$ and its corresponding resampled mode coefficient matrix $\wideha
### 贡献收束句
- 原句：However, existing uncertainty propagation (UP) methods for multidisciplinary systems often neglect correlations among field variables, leading to reduced accuracy.
  - 可迁移句型：{object}, existing uncertainty propagation (UP) methods for multidisciplinary systems often neglect correlations among field variables, leading to reduced accuracy.
- 原句：In the case study of UP across multiple disciplines of a solid rocket system, using Monte Carlo simulation (MCS) as the benchmark, incorporating variable correlations yields notable improve ments: the standard deviation accuracy of velocity and total energy at the first-stage separation point increased by 22.75 % and 32.57 %, respectively, while the accuracy of their lower bounds improved by 5.20 % and 4.20 %.
  - 可迁移句型：{object} the case study of UP across multiple disciplines of a solid rocket system, using Monte Carlo simulation (MCS) as the benchmark, incorporating variable correlations yields notable improve ments: the standard deviation accuracy of velocity and total ene
- 原句：To improve performance and ensure reliability, accounting for these uncertainties at every design stage is essential [2,3].
  - 可迁移句型：{object} improve performance and ensure reliability, accounting for these uncertainties at every design stage is essential [2,3].
- 原句：By explicitly considering the interactions and synergies among different disciplines, UMDO not only enhances overall system performance but also reduces development costs and shortens the design cycle [7–9].
  - 可迁移句型：{object} explicitly considering the interactions and synergies among different disciplines, UMDO not only enhances overall system performance but also reduces development costs and shortens the design cycle [7–9].
### 边界/谨慎句
- 原句：By explicitly considering the interactions and synergies among different disciplines, UMDO not only enhances overall system performance but also reduces development costs and shortens the design cycle [7–9].
  - 可迁移句型：{object} explicitly considering the interactions and synergies among different disciplines, UMDO not only enhances overall system performance but also reduces development costs and shortens the design cycle [7–9].
- 原句：Research on incorporating correlations among input variables in multidisciplinary systems remains limited.
  - 可迁移句型：{object} on incorporating correlations among input variables in multidisciplinary systems remains limited.
- 原句：Future work could address this limitation by introducing a preprocessing step to unify field variable dimensions before UP analysis, with the approach tailored to the characteristics of each problem.
  - 可迁移句型：{object} work could address this limitation by introducing a preprocessing step to unify field variable dimensions before UP analysis, with the approach tailored to the characteristics of each problem.

## 9. 引用风险层

- 正文引用簇估计：12
- 参考文献条数：28
- 可识别年份条目数：28
- 2021 年及以后参考文献数：15
- 2010 年以前经典文献数：4
- 高频来源粗略识别：Eng. Eng. Mech(7)；Multidiscip. Optim(3)；Spacecraft Rockets(1)；Aero. Eng(1)；Aeosp. Sci(1)；Therm. Eng(1)；J. Electr. Power Energy Syst(1)；Electr. Electron. Eng(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] X. Du, W. Chen, Efficient uncertainty analysis methods for multidisciplinary robust design, AIAA J. 40 (3) (2002) 545–552.
- [2] N. Zou, C. Gong, L. Zhang, et al., A novel hybrid time-variant reliability analysis method through approximating bound-most-probable point trajectory, Probab. Eng. Eng. Mech. 75 (2024) 103558.
- [3] L. Casalino, F. Masseni, D. Pastrone, Uncertainty analysis and robust design for a hybrid rocket upper stage, J. Spacecraft Rockets 56 (5) (2019) 1424–1431.
- [4] C. Wang, H. Fan, X. Qiang, A review of uncertainty-based multidisciplinary design optimization methods based on intelligent strategies, Symmetry-Basel 15 (10) (2023) 1875.
- [5] Z. Liu, Z. Song, P. Zhu, A novel polynomial chaos expansion-based method for feedback-coupled multidisciplinary design optimization under metamodel uncertainty, Struct. Multidiscip. Optim. 65 (5) (2022) 117.
- [6] M.R. Setayandeh, Surrogate model–based robust multidisciplinary design optimization of an unmanned aerial vehicle, J. Aero. Eng. 34 (4) (2021) 04021029.
- [7] W. Yao, X. Chen, W. Luo, et al., Review of uncertainty-based multidisciplinary design optimization methods for aerospace vehicles, Prog. Aeosp. Sci. 47 (6) (2011) 450–479.
- [8] H. Zhu, H. Luo, P. Wang, et al., Uncertainty analysis and design optimization of solid rocket motors with finocyl grain, Struct. Multidiscip. Optim. 62 (2020) 3521–3537.
- [9] H.Z. Huang, X. Zhang, W. Yuan, Collaborative reliability analysis under the environment of multidisciplinary design optimization, Concurr. Eng. 19 (3) (2011) 245–254.
- [10] F. Alhama, A. Campo, Network simulation of the rapid temperature changes in the composite nozzle wall of an experimental rocket engine during a ground firing test, Appl. Therm. Eng. 23 (1) (2003) 37–47.
- [11] S. Li, K. Gurley, Y. Guo, et al., Numerical investigation of turbulence effect on flight trajectory of spherical windborne debris: a multi-layered approach, Probab. Eng. Eng. Mech. 77 (2024) 103661.
- [12] H. Lü, J. Zhang, X. Huang, et al., Robust-based design optimization of powertrain mounting system based on full vehicle model involving parametric uncertainty and correlation, Probab. Eng. Eng. Mech. 79 (2025) 103726.
- [13] Q. Tu, S. Miao, F. Yao, et al., An improved wind power uncertainty model for day- ahead robust scheduling considering spatio-temporal correlations of multiple wind farms, Int. J. Electr. Power Energy Syst. 145 (2023) 108674.
- [14] N. Yang, S. Liu, Y. Deng, et al., An improved robust SCUC approach considering multiple uncertainty and correlation, IEEJ Trans. Electr. Electron. Eng. 16 (1) (2021) 21–34.
- [15] D. Yu, N. Ghadimi, Reliability constraint stochastic UC by considering the correlation of random variables with Copula theory, IET Renew. Power Gener. 13 (14) (2019) 2587–2593.

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
