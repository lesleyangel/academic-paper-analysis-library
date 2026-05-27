# 论文深度拆解：A novel hybrid time-variant reliability analysis method through approximating bound-most-probable point trajectory

> 生成依据：`801/cleantext/006-A-novel-hybrid-time-variant-reliability-analysis-metho_2024_Probabilistic-En`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`006-A-novel-hybrid-time-variant-reliability-analysis-metho_2024_Probabilistic-En`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\A-novel-hybrid-time-variant-reliability-analysis-metho_2024_Probabilistic-En.pdf`
- 页数：13
- clean body 字符数：69015
- 摘要字符数：1890
- 参考文献条数：47
- 图题数：13
- 表题数：10
- 表格文件数：11
- 公式候选数：326
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "low_confidence_formulas", "severity": "medium", "message": "57 formula(s) need manual review."}]

## 1. 身份层

- 标题：A novel hybrid time-variant reliability analysis method through approximating bound-most-probable point trajectory
- 年份：2024
- 期刊/来源：Probabilistic En
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：方法/算法 + 数值验证型
- 研究对象：For the hybrid TRA (HTRA) problem considering the two kinds of uncertainties, the existing method needs to excessively evaluate the original time-variant limit-state function, which is too expensive for engineering problems. Due to the interval variables and processes in the limit-state function, the time-variant failure probability needs to be regarded as an interval variable $[ P _ {\mathrm{f}} ^ {\mathrm{L}} , P _ {\mathrm{f}} ^ {\mathrm{U}} ]$ , which can be formulated as $$P _ {\mathrm{f}} 
- 主要方法：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems. In general, stochastic and interval models are respectively used to describe aleatory and epistemic uncertainties. For the hybrid TRA (HTRA) problem considering the two kinds of uncertainties, the existing method needs to excessively evaluate the original time-variant limit-state function, which is too expensive for engineering problems.
- 主要证据：图表 23 个标题、公式 326 个候选、参考文献 47 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“For the hybrid TRA (HTRA) problem considering the two kinds of uncertainties, the existing method needs to excessively evaluate the original time-variant limit-state function, whic”，可以通过“Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems. In general,”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems. Moreover, we develop a HTRA method based on approximating BMPPT which can further improve the computational ef ficiency. Two numerical examples including a cantilever beam, and a 10-bar truss, and two engineering applications of the solid rocket engine shell and the rocket inter-stage structure are investigated, and the results reveal that the proposed method can solve the HTRA problems with high ac curacy and efficiency.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：For the hybrid TRA (HTRA) problem considering the two kinds of uncertainties, the existing method needs to excessively evaluate the original time-variant limit-state function, which is too expensive for engineering problems. Due to the interval variables and processes in the limit-state function, the time-variant failure probability needs to be regarded as an interval variable $[ P _ {\mathrm{f}} ^ {\mathrm{L}} , P _ {\mathrm{f}} ^ {\mathrm{U}} ]$ , which can be formulated as $$P _ {\mathrm{f}} ^ {\mathrm{L}} ( t _ {\mathrm{s}} , t _ {\mathrm{e}} ) = \operatorname* {P r} \{\operatorname* {m i n} _ {\mathbf {I} ( t ) \in [ \mathbf {Y} ^ {\mathrm{L}} ( t ) , \mathbf {I} ^ {\mathrm{U}} ] _ {t} )} g ( \mathbf {X} , \mathbf {Y} , \mathbf {S} ( t ) , \mathbf {I} ( t ) , t ) \ge 0 , \exists t \in [ t _ {\mathrm{s}} , t _ {\mathrm{e}} ] \}\tag{7}$$ $$P _ {\mathrm{f}} ^ {\mathrm{U}} ( t _ {s} , t _ {\mathrm{e}} ) = \operatorname* {P r} \left\{\operatorname* {m a x} _ {\mathbf {I} ( t ) \in \left[ \mathbf {I} ^ {\mathrm{L}} ( t ) , \mathbf {I} ^ {\mathrm{U}} \right] _ {t} )} g ( \mathbf {X} , \mathbf {Y} , \mathbf {S} ( t ) , \mathbf {I} ( t ) , t ) \ge 0 , \exists t \in [ t _ {s} , t _ {\mathrm{e}} ] \right\}\tag{8}$$ Then, the time interval [ts, te] is discretized into M time instants, then Eqs. Compared with the TDHTRA which directly searches BMPPs at all discrete time instants, the HABMPPT requires less than one-tenth number of FEs needed by the TDHTRA with similar accuracy in estimating the failure probability.
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
- 作者声明或文本中可见 gap：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems. In the past few decades, many static reliability analysis methods [3–5] have been widely developed to measure the safety of structures. Time-variant uncertainties encountered in practical engineering [6], such as dynamic load and strength degradation, cannot be handled by those static methods.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- In the past few decades, many static reliability analysis methods [3–5] have been widely developed to measure the safety of structures.

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems. In general, stochastic and interval models are respectively used to describe aleatory and epistemic uncertainties. For the hybrid TRA (HTRA) problem considering the two kinds of uncertainties, the existing method needs to excessively evaluate the original time-variant limit-state function, which is too expensive for engineering problems.
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
| Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems. | 摘要/引言/结论候选 | 图：Fig. 1. Schematic diagram of the MPPT. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| To address this issue, we propose the concept of bound-most-probable point trajectory (BMPPT) which can be used to construct the approximation of the limit-state hyper-surface. | 摘要/引言/结论候选 | 图：Fig. 2. Schematic diagram of the limit-state strip. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Moreover, we develop a HTRA method based on approximating BMPPT which can further improve the computational ef ficiency. | 摘要/引言/结论候选 | 图：Fig. 3. Procedure of the SSL for computing uL MPP(ti). | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Two numerical examples including a cantilever beam, and a 10-bar truss, and two engineering applications of the solid rocket engine shell and the rocket inter-stage structure are investigated, and the results reveal that the proposed method can solve the HTRA  | 摘要/引言/结论候选 | 表：Table 1 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In the past few decades, many static reliability analysis methods [3–5] have been widely developed to measure the safety of structures. | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| To address this issue, the time-variant reliability analysis (TRA) method has been developed recently. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 202.2, 690.38)]] * Corresponding author. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Schematic diagram of the MPPT. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 2. Schematic diagram of the limit-state strip. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 3. Procedure of the SSL for computing uL MPP(ti). | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 4. The flowchart of the proposed HABMPPT method. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 5. A corroded steel beam. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 6. Time-variant failure probability of the corroded steel beam. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 7. A 10-bar truss. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. Time-variant failure probability of the 10-bar truss. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 9. Schematic diagram of the solid rocket engine. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 10. Time-variant failure probability of the solid rocket engine shell. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. The model of the rocket inter-stage structure. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 12. Time-variant failure probability of the rocket inter-stage structure. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 3. Procedure of the SSL for computing ${ \bf u } _ { \mathrm { M P P } } ^ { \mathrm { L } } ( t _ { i } )$ | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 7 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 8 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 9 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 10 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 202.2, 690.38)]] * Corresponding author. E-mail address: chu | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 367.94, 716.91)]] https://doi.org/10.1016/j.probengmech.2023 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 2, bbox (48.08, 178.8, 291.01, 213.01)]] W Standard normal random vector transformed | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 2, bbox (306.6, 62.01, 539.1, 85.79)]] Zi Standard normal random vector transformed  | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 2, bbox (306.6, 82.93, 539.38, 106.71)]] P Standard interval vector transformed from | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 2, bbox (306.6, 103.85, 522.24, 139.93)]] ζk Standard interval vector transformed fr | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.6, 108.48, 350.37, 119.46)]] PL f (ts, te) = Pr | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.6, 163.87, 350.94, 174.85)]] PU f (ts, te) = Pr | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> In the engineering field, time-variant reliability analysis (TRA) is used to measure the safety level of structures under time-variant uncertainties. Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems. In general, stochastic and interval models are respectively used to describe aleatory and epistemic uncertainties. For the hybrid TRA (HTRA) problem considering the two kinds of uncertainties, the existing method needs to excessively evaluate the original time-variant limit-state function, which is too expensive for engineering problems. To address this issue, we propose the concept of bound-most-probable point trajectory (BMPPT) which can be used to construct the approximation of the limit-state hyper-surface. Moreover, we develop a HTRA method based on approximating BMPPT which can further improve the computational ef ficiency. First, based on time discretization, we transform the HTRA problem into a time-independent series- system reliability problem which can be solved by searching the bound-most-probable point (BMPP) at all discrete time instants. Then, with the BMPPT, the lower and upper bounds of the time-variant limit-state function are linearized into two Gaussian processes. Finally, the expansion optimal linear estimation and Monte Carlo simulation are performed to estimate the time-variant reliability. To avoid excessive BMPP searches, the active learning Kriging is used to approximate the BMPPT. Two numerical examples including a cantilever beam, and a 10-bar truss, and two engineering applications of the solid rocket engine shell and the rocket inter-stage structure are investigated, and the results reveal that the proposed method can solve the HTRA problems with high ac curacy and efficiency.

### 7.4 摘要中文翻译

> 在工程领域，时变可靠性分析（TRA）用于衡量时变不确定性下结构的安全水平。由于缺乏信息或数据，一些不确定性无法直接量化为随机模型，导致大多数问题同时存在偶发性和认知性不确定性。一般来说，随机模型和区间模型分别用于描述偶然和认知不确定性。对于考虑两种不确定性的混合TRA（HTRA）问题，现有方法需要过度评估原始时变极限状态函数，这对于工程问题来说代价太大。为了解决这个问题，我们提出了边界最可能点轨迹（BMPPT）的概念，它可用于构造极限状态超曲面的近似。此外，我们开发了一种基于近似BMPPT的HTRA方法，可以进一步提高计算效率。首先，基于时间离散化，我们将HTRA问题转化为与时间无关的串联系统可靠性问题，该问题可以通过在所有离散时刻搜索最有可能点（BMPP）来解决。然后，通过 BMPPT，时变极限状态函数的下限和上限被线性化为两个高斯过程。最后，进行扩展最优线性估计和蒙特卡罗模拟来估计时变可靠性。为了避免过多的 BMPP 搜索，使用主动学习克里金法来近似 BMPPT。
> 
> 对悬臂梁和10杆桁架的两个数值算例以及固体火箭发动机壳体和火箭级间结构的两个工程应用进行了研究，结果表明该方法能够高精度、高效地求解HTRA问题。

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusion

> In this paper, a novel HTRA method by approximating the BMPPT is proposed, which can effectively and efficiently solve the HTRA problems involving interval process variables. In the proposed method, based on time discretization, the HTRA problem can be transformed into a timeindependent series system reliability problem, which can be solved by obtaining BMPPs at all discrete time instants. To avoid directly searching BMPP at a large number of discrete time instants, we approximate the BMPPT by active learning Kriging to efficiently obtain all BMPPs. Combining the approximated BMPPT and MCS, the bounds of timevariant failure probability can be estimated. Four examples with random variables, stochastic process variables, interval variables and interval process variables are investigated, from which the following conclusions can be drawn.
> 
> (1) We propose the concept of the BMPPT. Based on the BMPPT, the bound time-variant limit-sate function of HTRA problems involving interval process variables can be linearized into two Gaussian processes, then the failure probability can be estimated efficiently.
> 
> (2) In the proposed HABMPPT, the active learning Kriging model is used to approximate the BMPPT to obtain BMPPs efficiently. Compared with the TDHTRA which directly searches BMPPs at all discrete time instants, the HABMPPT requires less than one-tenth number of FEs needed by the TDHTRA with similar accuracy in estimating the failure probability.
> 
> (3) The results of four examples show that, for the HABMPPT, the relative errors compared with MCS are typically smaller than 5 % which is acceptable for engineering problems.
> 
> This study proposes an efficient and effective method for solving HTRA problems involving interval process variables. However, the investigation of the HABMPPT in this paper is by no means exhaustive. For example, how to solve HTRA problem with correlated uncertainties, how to calculate BMPP more efficiently and accurately, and how to approximate the BMPPT dealing with unsmooth or discontinuous BMPPT, we are still a huge challenging task for the HBAMPPT method and need further study in the future.

### 7.6 结论中文翻译

> 本文提出了一种近似BMPPT的新型HTRA方法，可以有效且高效地解决涉及区间过程变量的HTRA问题。在所提出的方法中，基于时间离散化，HTRA问题可以转化为与时间无关的串联系统可靠性问题，可以通过获得所有离散时刻的BMPP来解决。为了避免在大量离散时刻直接搜索 BMPP，我们通过主动学习克里金法来近似 BMPPT，以有效地获得所有 BMPP。结合近似的 BMPPT 和 MCS，可以估计时变失效概率的界限。研究了随机变量、随机过程变量、区间变量和区间过程变量的四个例子，得出以下结论。 (1)我们提出了BMPPT的概念。基于BMPPT，涉及区间过程变量的HTRA问题的有界时变极限状态函数可以线性化为两个高斯过程，从而可以有效地估计失效概率。 (2)在所提出的HABMPPT中，主动学习克里金模型被用来近似BMPPT以有效地获得BMPP。与在所有离散时刻直接搜索 BMPP 的 TDHTRA 相比，HABMPPT 所需的 FE 数量不到 TDHTRA 所需的十分之一，并且在估计失效概率方面具有相似的精度。 (3) 四个算例的结果表明，对于HABMPPT，与MCS相比，相对误差通常小于5%，对于工程问题来说是可以接受的。本研究提出了一种解决涉及区间过程变量的 HTRA 问题的高效且有效的方法。
> 
> 然而，本文对 HABMPPT 的研究绝非详尽无遗。例如，如何解决具有相关不确定性的HTRA问题，如何更高效、准确地计算BMPP，以及如何近似处理不平滑或不连续的BMPPT，对于HBAMPPT方法来说仍然是一个巨大的挑战性任务，需要在未来进一步研究。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 8271 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2.1. Time-variant reliability analysis problems | 结果验证/讨论 | 3610 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 3 | 2.2. Direct solution method for HTRA based on MCS | 方法建构 | 4917 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 3.1. Definition of the bound-most-probable point trajectory | 对象/条件/子问题展开 | 2248 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 3.2. Approximation of the bound-most-probable point trajectory | 对象/条件/子问题展开 | 7161 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 3.3. Linearization of the bound of limit-state function | 对象/条件/子问题展开 | 11013 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 3.4. Estimation of time-variant failure probability using MCS | 对象/条件/子问题展开 | 4966 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 3.5. The implementation procedure of the HABMPPT | 对象/条件/子问题展开 | 756 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 4. Examples and discussions | 结果验证/讨论 | 1309 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 10 | 4.1. A corroded steel beam | 对象/条件/子问题展开 | 4199 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 4.2. A 10-bar truss | 对象/条件/子问题展开 | 5713 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 4.3. A solid rocket engine shell structure | 对象/条件/子问题展开 | 6897 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 4.4. A rocket inter-stage structure | 对象/条件/子问题展开 | 5071 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 5. Conclusion | 主张回收/边界说明 | 2142 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |

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

- 高频词：mathrm(443)；mathbf(328)；delta(277)；alpha(143)；big(118)；beta(88)；time(69)；interval(59)；frac(54)；habmppt(50)；rho(50)；time-variant(49)；function(49)；tag(49)；array(48)；mpp(43)；failure(42)；variables(41)；times(41)；left(40)
- 高频学术名词/术语：function(49)；failure(42)；probability(39)；reliability(26)；structure(22)；pressure(8)；characteristics(7)；estimation(7)；procedure(7)；optimization(6)；combustion(6)；discretization(5)；section(5)；expansion(5)；measure(4)
- 高频学术动词：estimated(11)；obtained(11)；obtain(11)；developed(10)；estimate(10)；investigated(6)；introduced(5)；construct(5)；evaluate(5)；constructed(4)；demonstrate(3)；compared(3)；propose(2)；presented(1)；develop(1)
- 高频形容词：interval(59)；time-variant(49)；stochastic(17)；table(16)；active(15)；initial(13)；equidistant(12)；epistemic(10)；efficient(9)；independent(9)；variable(9)；computational(7)；normal(7)；instant(7)；relative(7)
- 高频副词：respectively(33)；efficiently(8)；directly(7)；uniformly(5)；widely(4)；effectively(3)；accurately(3)；recently(2)；generally(2)；analytically(2)；significantly(2)；accordingly(2)
- 高频二词短语：delta delta(275)；mathbf alpha(125)；mathrm mathrm(113)；alpha mathbf(93)；mathbf mathrm(64)；mathbf mathbf(58)；mathrm big(52)；alpha beta(39)；big big(36)；beta mathbf(36)；mathrm mpp(34)；mpp mathrm(34)；failure probability(33)；time instants(33)；mathrm mathbf(32)
- 高频三词短语：delta delta delta(273)；mathbf alpha mathbf(87)；alpha mathbf alpha(82)；mathrm mpp mathrm(34)；mathbf alpha beta(33)；beta mathbf alpha(31)；mathbf mathbf mathbf(30)；mathrm mathrm mathrm(27)；alpha beta mathbf(23)；mathbf rho mathbf(23)；mathbf mathrm mpp(22)；rho mathbf rho(22)
- 被动语态估计：168
- `we + 动作动词` 主动句估计：7
- 一般现在时线索：254
- 一般过去时线索：358
- 现在完成时线索：0
- 情态动词线索：60

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Compared with the TDHTRA which directly searches BMPPs at all discrete time instants, the HABMPPT requires less than one-tenth number of FEs needed by the TDHTRA with similar accuracy in estimating the failure probability.
  - 可迁移句型：{object} with the TDHTRA which directly searches BMPPs at all discrete time instants, the HABMPPT requires less than one-tenth number of FEs needed by the TDHTRA with similar accuracy in estimating the failure probability.
### gap/转折句
- 原句：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems.
  - 可迁移句型：{object} in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems.
- 原句：In the past few decades, many static reliability analysis methods [3–5] have been widely developed to measure the safety of structures.
  - 可迁移句型：{object} the past few decades, many static reliability analysis methods [3–5] have been widely developed to measure the safety of structures.
- 原句：However, those out-crossing rate methods may lead to large errors for the problems where out-crossing events are strongly dependent.
  - 可迁移句型：{object}, those out-crossing rate methods may lead to large errors for the problems where out-crossing events are strongly dependent.
- 原句：However, the investigation of the HABMPPT in this paper is by no means exhaustive.
  - 可迁移句型：{object}, the investigation of the HABMPPT in This study is by no means exhaustive.
### 方法提出句
- 原句：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems.
  - 可迁移句型：{object} in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems.
- 原句：In general, stochastic and interval models are respectively used to describe aleatory and epistemic uncertainties.
  - 可迁移句型：{object} general, stochastic and interval models are respectively used to describe aleatory and epistemic uncertainties.
- 原句：For the hybrid TRA (HTRA) problem considering the two kinds of uncertainties, the existing method needs to excessively evaluate the original time-variant limit-state function, which is too expensive for engineering problems.
  - 可迁移句型：{object} the hybrid TRA (HTRA) problem considering the two kinds of uncertainties, the existing method needs to excessively evaluate the original time-variant limit-state function, which is too expensive for engineering problems.
- 原句：To address this issue, we propose the concept of bound-most-probable point trajectory (BMPPT) which can be used to construct the approximation of the limit-state hyper-surface.
  - 可迁移句型：{object} address this issue, we propose the concept of bound-most-probable point trajectory (BMPPT) which can be used to construct the approximation of the limit-state hyper-surface.
### 结果证明句
- 原句：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems.
  - 可迁移句型：{object} in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems.
- 原句：Two numerical examples including a cantilever beam, and a 10-bar truss, and two engineering applications of the solid rocket engine shell and the rocket inter-stage structure are investigated, and the results reveal that the proposed method can solve the HTRA problems with high ac curacy and efficiency.
  - 可迁移句型：{object} numerical examples including a cantilever beam, and a 10-bar truss, and two engineering applications of the solid rocket engine shell and the rocket inter-stage structure are investigated, and the results reveal that the proposed method can solve the 
- 原句：(3) The results of four examples show that, for the HABMPPT, the relative errors compared with MCS are typically smaller than 5 % which is acceptable for engineering problems.
  - 可迁移句型：(3) {object} results of four examples show that, for the HABMPPT, the relative errors compared with MCS are typically smaller than 5 % which is acceptable for engineering problems.
### 贡献收束句
- 原句：Moreover, we develop a HTRA method based on approximating BMPPT which can further improve the computational ef ficiency.
  - 可迁移句型：{object}, we develop a HTRA method based on approximating BMPPT which can further improve the computational ef ficiency.
- 原句：Simulation-based methods, such as Monte Carlo simulation (MCS) and importance sampling method [9], provide an alternative but expensive way to estimate the extreme value distribution.
  - 可迁移句型：{object} methods, such as Monte Carlo simulation (MCS) and importance sampling method [9], provide an alternative but expensive way to estimate the extreme value distribution.
- 原句：To reduce the computational burden, surrogate models, such as Kriging [10,11] and artificial neural networks [12,13], have been introduced into simulation-based methods.
  - 可迁移句型：{object} reduce the computational burden, surrogate models, such as Kriging [10,11] and artificial neural networks [12,13], have been introduced into simulation-based methods.
- 原句：Sudret [21] developed the improved PHI2 method which has a higher stability.
  - 可迁移句型：{object} [21] developed the improved PHI2 method which has a higher stability.
### 边界/谨慎句
- 原句：Based on whether or not the out-crossing rate should be calculated, the first passage-based method can be classified into two types: the out-crossing rate method and the time discretization-based TRA (TDTRA) method.
  - 可迁移句型：{object} on whether or not the out-crossing rate should be calculated, the first passage-based method can be classified into two types: the out-crossing rate method and the time discretization-based TRA (TDTRA) method.
- 原句：However, those out-crossing rate methods may lead to large errors for the problems where out-crossing events are strongly dependent.
  - 可迁移句型：{object}, those out-crossing rate methods may lead to large errors for the problems where out-crossing events are strongly dependent.
- 原句：As a commonly used numerical method, the MCS can directly estimate the solutions to Eqs.
  - 可迁移句型：{object} a commonly used numerical method, the MCS can directly estimate the solutions to Eqs.
- 原句：For example, how to solve HTRA problem with correlated uncertainties, how to calculate BMPP more efficiently and accurately, and how to approximate the BMPPT dealing with unsmooth or discontinuous BMPPT, we are still a huge challenging task for the HBAMPPT method and need further study in the future.
  - 可迁移句型：{object} example, how to solve HTRA problem with correlated uncertainties, how to calculate BMPP more efficiently and accurately, and how to approximate the BMPPT dealing with unsmooth or discontinuous BMPPT, we are still a huge challenging task for the HBAMPP

## 9. 引用风险层

- 正文引用簇估计：50
- 参考文献条数：47
- 可识别年份条目数：70
- 2021 年及以后参考文献数：17
- 2010 年以前经典文献数：14
- 高频来源粗略识别：Multidiscip. Optim(8)；Mech. Des(6)；Eng. Syst. Saf(4)；Eng. Mech(4)；J. Mech. Mater. Des(3)；Math. Model(2)；Struct(2)；Sound Vib(2)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] A. Singh, Z.P. Mourelatos, J. Li, Design for lifecycle cost using time-dependent reliability, J. Mech. Des. 132 (9) (2010), 091008, https://doi.org/10.1115/ 1.4002200.
- [2] Z. Meng, J. Zhao, C. Jiang, An efficient semi-analytical extreme value method for time-variant reliability analysis, Struct. Multidiscip. Optim. 64 (3) (2021) 1469–1480, https://doi.org/10.1007/s00158-021-02934-y.
- [3] H. Pang, T. Yu, B. Song, Failure mechanism analysis and reliability assessment of an aircraft slat, Eng. Fail. Anal. 60 (2016) 261–279, https://doi.org/10.1016/j. engfailanal.2015.11.032.
- [4] Z. Sun, J. Wang, R. Li, C. Tong, LIF: a new Kriging based learning function and its application to structural reliability analysis, Reliab. Eng. Syst. Saf. 157 (2017) 152–165, https://doi.org/10.1016/j.ress.2016.09.00.
- [5] G. Li, B. Li, H. Hu, A novel first–order reliability method based on performance measure approach for highly nonlinear problems, Struct. Multidiscip. Optim. 57 (4) (2018) 1593–1610, https://doi.org/10.1007/s00158-017-1830-1.
- [6] M. Di Paola, L. Galuppi, G. Royer Carfagni, Fractional viscoelastic characterization of laminated glass beams under time-varying loading, Int. J. Mech. Sci. 196 (2021), 106274, https://doi.org/10.1016/j.ijmecsci.2021.106274.
- [7] Z. Hu, X. Du, A sampling approach to extreme value distribution for time- dependent reliability analysis, J. Mech. Des. 135 (7) (2013), 071003, https://doi. org/10.1115/1.4023925.
- [8] Z. Wang, P. Wang, A nested extreme response surface approach for time-dependent reliability-based design optimization, J. Mech. Des. 134 (12) (2012), 121007, https://doi.org/10.1115/1.4007931.
- [9] W. Yun, Z. Lu, X. Jiang, L. Zhang, P. He, AK-ARBIS: an improved AK-MCS based on the adaptive radial-based importance sampling for small failure probability, Struct. Saf. 82 (2020), 101891, https://doi.org/10.1016/j.strusafe.2019.101891.
- [10] Z. Wang, W. Chen, Time-variant reliability assessment through equivalent stochastic process transformation, Reliab. Eng. Syst. Saf. 152 (2016) 166–175, https://doi.org/10.1016/j.ress.2016.02.008.
- [11] H. Liu, X. He, P. Wang, Z. Lu, Z. Yue, Time-dependent reliability analysis method based on ARBIS and Kriging surrogate model, Eng. Comput-Germany. 39 (3) (2022) 2035–2048, https://doi.org/10.1007/s00366-021-01570-w.
- [12] L. Cao, S.G. Gong, Y.R. Tao, S.Y. Duan, A RBFNN based active learning surrogate model for evaluating low failure probability in reliability analysis, Probab. Eng. Mech. 74 (2023), 103496, https://doi.org/10.1016/j.probengmech.2023.103496.
- [13] D. Zhang, N. Zhang, N. Ye, J. Fang, X. Han, Hybrid learning algorithm of radial basis function networks for reliability analysis, IEEE Trans. Reliab. 70 (3) (2021) 887–900, https://doi.org/10.1109/TR.2020.3001232.
- [14] Z. Hu, S. Mahadevan, A single-loop Kriging surrogate modeling for time-dependent reliability analysis, J. Mech. Des. 138 (6) (2016), 061406, https://doi.org/ 10.1115/1.4033428.
- [15] Z. Hu, X. Du, First order reliability method for time-variant problems using series expansions, Struct. Multidiscip. Optim. 51 (1) (2015) 1–21, https://doi.org/ 10.1007/s00158-014-1132-9.

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
