# 论文深度拆解：009-A-sequential-surrogate-method-for-reliability-analysis-base_2018_Structural

> 生成依据：`801/cleantext/009-A-sequential-surrogate-method-for-reliability-analysis-base_2018_Structural`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`009-A-sequential-surrogate-method-for-reliability-analysis-base_2018_Structural`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\A-sequential-surrogate-method-for-reliability-analysis-base_2018_Structural-.pdf`
- 页数：12
- clean body 字符数：37071
- 摘要字符数：1343
- 参考文献条数：54
- 图题数：14
- 表题数：12
- 表格文件数：15
- 公式候选数：118
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "low_confidence_formulas", "severity": "medium", "message": "13 formula(s) need manual review."}]

## 1. 身份层

- 标题：009-A-sequential-surrogate-method-for-reliability-analysis-base_2018_Structural
- 年份：2018
- 期刊/来源：Structural
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：实验/测量 + 性能分析型
- 研究对象：By updating the surrogate model with the new points, the surrogate model of LSF becomes more and more accurate in the important region with a high failure probability and on the LSF boundary. Moreover, the accuracy of the unimportant region is further improved within the iteration due to the minimum distance con- straint. Several numerical examples show that SSRM improves the accuracy of the surrogate model in the important region around the failure boundary with a small number of samples and ha
- 主要方法：A radial basis function (RBF) based sequential surrogate reliability method (SSRM) is proposed, in which a special optimization problem is solved to update the surrogate model of the limit state function (LSF) iteratively. By updating the surrogate model with the new points, the surrogate model of LSF becomes more and more accurate in the important region with a high failure probability and on the LSF boundary. Several numerical examples show that SSRM improves the accuracy of the surrogate model in the important region around the failure boundary with a small number of samples and has a better adaptability to the nonlinear LSF, hence increases the accuracy and efficiency of the reliability 
- 主要证据：图表 26 个标题、公式 118 个候选、参考文献 54 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“By updating the surrogate model with the new points, the surrogate model of LSF becomes more and more accurate in the important region with a high failure probability and on the LS”，可以通过“A radial basis function (RBF) based sequential surrogate reliability method (SSRM) is proposed, in which a special optimization problem is solved to update the surrogate model of the limit state function (LSF) iterativel”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：Moreover, the accuracy of the unimportant region is further improved within the iteration due to the minimum distance con- straint. Several numerical examples show that SSRM improves the accuracy of the surrogate model in the important region around the failure boundary with a small number of samples and has a better adaptability to the nonlinear LSF, hence increases the accuracy and efficiency of the reliability analysis. �2018 Elsevier Ltd. Therefore, different approximations of the LSF are adopted to improve the computational efficiency of reliability analysis.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：By updating the surrogate model with the new points, the surrogate model of LSF becomes more and more accurate in the important region with a high failure probability and on the LSF boundary. Moreover, the accuracy of the unimportant region is further improved within the iteration due to the minimum distance con- straint. Several numerical examples show that SSRM improves the accuracy of the surrogate model in the important region around the failure boundary with a small number of samples and has a better adaptability to the nonlinear LSF, hence increases the accuracy and efficiency of the reliability analysis. �2018 Elsevier Ltd.
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
- 作者声明或文本中可见 gap：The numerical integral and direct Monte Carlo Simulation (MCS) are difficult for a complex system with implicit time-consuming analysis models. However, it requires the independent input variables obey normal distribution, which is difficult to be satisfied in practical problems. Compared with the MVM, the FORM does not require the input variables to obey normal distribution and has a higher accuracy with the LSF expanded at the MPP.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- To calculate the integral with the original LSF faces enormous computational challenges [1–2].
- Moreover, the adaptability to nonlinear boundary is still limited [10–11].

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：A radial basis function (RBF) based sequential surrogate reliability method (SSRM) is proposed, in which a special optimization problem is solved to update the surrogate model of the limit state function (LSF) iteratively. By updating the surrogate model with the new points, the surrogate model of LSF becomes more and more accurate in the important region with a high failure probability and on the LSF boundary. Several numerical examples show that SSRM improves the accuracy of the surrogate model in the important region around the failure boundary with a small number of samples and has a better adaptability to the nonlinear LSF, hence increases the accuracy and efficiency of the reliability analysis. �2018 Elsevier Ltd.
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
| A radial basis function (RBF) based sequential surrogate reliability method (SSRM) is proposed, in which a special optimization problem is solved to update the surrogate model of the limit state function (LSF) iteratively. | 摘要/引言/结论候选 | 图：Fig. 1. Approximations of LSF in X and U space. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Moreover, the accuracy of the unimportant region is further improved within the iteration due to the minimum distance con- straint. | 摘要/引言/结论候选 | 图：Fig. 2. Initial surrogate in U-Space. ‘‘ ” denotes the initial samples, and ‘‘ ” denotes the added sample based on the initial surrogate model. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Several numerical examples show that SSRM improves the accuracy of the surrogate model in the important region around the failure boundary with a small number of samples and has a better adaptability to the nonlinear LSF, hence increases the accuracy and effic | 摘要/引言/结论候选 | 图：Fig. 3. Flow chart of SSRM. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Therefore, different approximations of the LSF are adopted to improve the computational efficiency of reliability analysis. | 摘要/引言/结论候选 | 表：Table 1 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The mean value method (MVM) [3–4] performs a first-order Taylor expansion of the LSF at the mean point (as shown in Fig. | 摘要/引言/结论候选 | 表：Table 2 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The first-order reliability method (FORM) [5–8] transforms random variables with different distributions into the same standard normal space U by Rosenblatt transformation [9] and then performs a first-order Taylor expansion at the most probable point (MPP) wh | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 2, bbox (100.92, 83.83, 227.09, 101.19)]] GSORM(u)=0 gMVM(x)=0 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Approximations of LSF in X and U space. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 2. Initial surrogate in U-Space. ‘‘ ” denotes the initial samples, and ‘‘ ” denotes the added sample based on the initial surrogate model. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 3. Flow chart of SSRM. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4. Iterative process of SSRM for the circular pipe structure. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 5. Iterative process of SSRM for the hyper-sphere problem. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 6. Iterative process of SSRM for the cantilever beam. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 7. Iterative process of SSRM for the speed reducer shaft. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. Cantilever tube [6]. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 9. Iterative process of SSRM for the cantilever tube. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 10. Nonlinear oscillator [34]. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. Iterative process of SSRM for the high-dimensional problem for m = 40, 100 and 250. Fig. 11. Iterative process of SSRM for the nonlinear oscillator. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 2. Initial surrogate in U-Space. $" \underbrace { \mathbf { \phi } } _ { \mathrm { ~ \tiny ~ ~ } } \cdot \mathbf { \psi } ^ { \star }$ denotes the initial  | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 11. Iterative process of SSRM for the nonlinear oscillator. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. Iterative process of SSRM for the high-dimensional problem for m = 40, 100 and 250. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 9 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 8 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 10 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 13 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (100.92, 83.83, 227.09, 101.19)]] GSORM(u)=0 gMVM(x)=0 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (88.29, 110.0, 283.29, 120.37)]] μ GFORM(u)=0 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (211.92, 148.68, 246.0, 155.78)]] LSF G(u)=0 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (91.28, 157.3, 123.48, 164.41)]] LSF g(x)=0 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.62; needs_review; source=equations; [page 2, bbox (370.32, 723.51, 484.79, 741.82)]] Gaussian expð�cr2Þ Inverse Multiquadric ð | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (303.08, 98.88, 310.47, 151.64)]] 8 > > > > > > > > > > > > > > > < | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (303.08, 158.24, 310.47, 203.46)]] > > > > > > > > > > > > > > > : | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (354.88, 696.93, 375.28, 704.03)]] g(x)=0 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> A radial basis function (RBF) based sequential surrogate reliability method (SSRM) is proposed, in which a special optimization problem is solved to update the surrogate model of the limit state function (LSF) iteratively. The objective of the optimization problem is to find a new point to maximize the probability density function (PDF), subject to the constraints that the new point is on the approximated LSF and the minimum distance to the existing points is greater than or equal to a given distance. By updating the surrogate model with the new points, the surrogate model of LSF becomes more and more accurate in the important region with a high failure probability and on the LSF boundary. Moreover, the accuracy of the unimportant region is further improved within the iteration due to the minimum distance con- straint. SSRM takes advantage of the information of PDF and LSF to capture the failure features, which decrease the samples of implicit LSF defined by expensive finite element analysis. Several numerical examples show that SSRM improves the accuracy of the surrogate model in the important region around the failure boundary with a small number of samples and has a better adaptability to the nonlinear LSF, hence increases the accuracy and efficiency of the reliability analysis. �2018 Elsevier Ltd. All rights reserved.

### 7.4 摘要中文翻译

> 提出了一种基于径向基函数（RBF）的顺序代理可靠性方法（SSRM），该方法通过解决特殊的优化问题来迭代更新极限状态函数（LSF）的代理模型。优化问题的目标是找到一个新点来最大化概率密度函数（PDF），但受到新点位于近似LSF上并且到现有点的最小距离大于或等于给定距离的约束。通过用新点更新代理模型，LSF代理模型在失效概率较高的重要区域和LSF边界上变得越来越准确。此外，由于最小距离约束，不重要区域的精度在迭代中进一步提高。 SSRM利用PDF和LSF的信息来捕获失效特征，这减少了由昂贵的有限元分析定义的隐式LSF的样本。数值算例表明，SSRM以较少的样本量提高了失效边界周围重要区域代理模型的精度，并且对非线性LSF具有更好的适应性，从而提高了可靠性分析的精度和效率。 �2018 爱思唯尔有限公司

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusions

> In this paper, an efficient method for reliability analysis named SSRM is proposed. This method searches for new sample points, which involve the information about the joint probability density function and the limit state function, to refine the surrogate model of LSF iteratively. The sequential surrogate model captures more meaningful failure features in the important region, while reduces the samples in the region with low failure probability. In each iteration, MCS is used to evaluate the failure probability. Thus, a sequence of approximate failure probabilities is obtained. Several examples including numerical and engineering cases demonstrate that SSRM has a good adaptability to the LSFs with different nonlinearity and dimensions. For low-dimensional problems, SSRM has a significant advantage over existing methods in terms of accuracy and efficiency; for high-dimensional problems, SSRM has comparable precision to existing methods and higher efficiency. However, as the parameter optimization of the surrogate model, MCS, and GA take a number of surrogate evaluations, SSRM shows its superiority only when the LSFs are time-consuming implicit functions (e.g. finite element analysis). In the future study, the information of the computationally cheap low-fidelity model can be involved to construct a variable-fidelity surrogate model, so that the number of time-consuming high-fidelity sample points is expected to be further reduced.

### 7.6 结论中文翻译

> 本文提出了一种有效的可靠性分析方法SSRM。该方法通过搜索新的样本点，涉及联合概率密度函数和极限状态函数的信息，迭代地细化LSF代理模型。顺序代理模型在重要区域捕获更有意义的故障特征，同时减少故障概率较低区域的样本。在每次迭代中，MCS 用于评估故障概率。因此，获得了近似故障概率的序列。数值和工程案例表明SSRM对不同非线性和维数的LSF具有良好的适应性。对于低维问题，SSRM在精度和效率方面较现有方法具有显着优势；对于高维问题，SSRM 具有与现有方法相当的精度和更高的效率。然而，由于代理模型、MCS和GA的参数优化需要多次代理评估，只有当LSF是耗时的隐函数（例如有限元分析）时，SSRM才显示出其优越性。在未来的研究中，可以涉及计算廉价的低保真模型的信息来构建可变保真代理模型，从而有望进一步减少耗时的高保真样本点的数量。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 5648 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2.1 Construction of surrogate model | 方法建构 | 3597 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 3 | 2.2. Validation of surrogate model | 方法建构 | 1463 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 3 Sequential surrogate reliability method | 方法建构 | 12871 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 5 | 4. Numerical examples | 对象/条件/子问题展开 | 1096 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 4.1. Circular pipe structure | 对象/条件/子问题展开 | 1406 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 4.2. Hyper-sphere bound problem | 对象/条件/子问题展开 | 1379 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 4.3. Cantilever beam | 对象/条件/子问题展开 | 1542 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 4.4. Speed reducer shaft | 对象/条件/子问题展开 | 870 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 4.5. Cantilever tube problem | 对象/条件/子问题展开 | 287 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | where | 对象/条件/子问题展开 | 1841 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 4.6. Dynamic response of a nonlinear oscillator | 对象/条件/子问题展开 | 841 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 4.7. High-dimensional problem | 对象/条件/子问题展开 | 2285 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 5. Conclusions | 主张回收/边界说明 | 1454 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |

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

- 高频词：mathbf(122)；samples(65)；lsf(63)；ssrm(45)；mathrm(45)；surrogate(42)；failure(32)；sample(31)；mcs(30)；initial(28)；tag(27)；variables(27)；accuracy(26)；random(25)；iteration(25)；probability(23)；region(21)；problem(21)；reliability(19)；left(19)
- 高频学术名词/术语：failure(32)；iteration(25)；probability(23)；reliability(19)；function(17)；optimization(14)；nonlinearity(11)；distribution(10)；approximation(10)；distance(10)；section(9)；estimation(8)；information(8)；dimension(8)；adaptability(6)
- 高频学术动词：obtained(6)；obtain(5)；presented(4)；constructed(3)；construct(3)；compared(2)；demonstrate(2)；evaluate(2)；predicted(1)；optimize(1)；estimate(1)；estimated(1)
- 高频形容词：initial(28)；table(17)；important(16)；leqslant(15)；original(11)；boundary(10)；normal(9)；sequential(8)；iterative(7)；radial(5)；relative(5)；high-dimensional(5)；numerical(4)；computational(4)；local(4)
- 高频副词：iteratively(10)；respectively(7)；eventually(2)；strictly(2)；essentially(1)；analytically(1)；finally(1)；commonly(1)；gradually(1)；sequentially(1)；directly(1)；instinctually(1)
- 高频二词短语：mathbf mathbf(58)；random variables(20)；failure probability(16)；important region(12)；initial samples(12)；samples selected(11)；iteration iteration(11)；samples added(10)；mathrm mathbf(9)；extra samples(9)；response surface(8)；begin array(8)；end array(8)；right tag(8)；surrogate lsf(8)
- 高频三词短语：mathbf mathbf mathbf(28)；initial samples selected(10)；extra samples added(9)；samples added iteratively(8)；samples selected extra(7)；selected extra samples(7)；iteration iteration iteration(7)；left begin array(6)；end array right(6)；hat mathbf mathbf(5)；mathbf mathbf ldots(4)；mathbf ldots mathbf(4)
- 被动语态估计：94
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：224
- 一般过去时线索：162
- 现在完成时线索：0
- 情态动词线索：21

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：By updating the surrogate model with the new points, the surrogate model of LSF becomes more and more accurate in the important region with a high failure probability and on the LSF boundary.
  - 可迁移句型：{object} updating the surrogate model with the new points, the surrogate model of LSF becomes more and more accurate in the important region with a high failure probability and on the LSF boundary.
- 原句：Moreover, the accuracy of the unimportant region is further improved within the iteration due to the minimum distance con- straint.
  - 可迁移句型：{object}, the accuracy of the unimportant region is further improved within the iteration due to the minimum distance con- straint.
- 原句：Several numerical examples show that SSRM improves the accuracy of the surrogate model in the important region around the failure boundary with a small number of samples and has a better adaptability to the nonlinear LSF, hence increases the accuracy and efficiency of the reliability analysis. �2018 Elsevier Ltd.
  - 可迁移句型：{object} numerical examples show that SSRM improves the accuracy of the surrogate model in the important region around the failure boundary with a small number of samples and has a better adaptability to the nonlinear LSF, hence increases the accuracy and effi
- 原句：In engineering design, when uncertainties are involved, the failure probability $P _ {f}$ of the limit state function (LSF) g(x) should be examined. $P _ {f}$ is essentially a multi-dimensional integral formulated as $$P _ {f} = \int \int \cdots \int _ {D} {\sf p} ( {\bf x} ) {\sf d} x _ {1} {\sf d} x _ {2} \cdot \cdot \cdot {\sf d} x _ {m}\tag{1}$$ where $D$ is the failure region defined as $D = \{\mathbf {x} | \mathbf {g} ( \mathbf {x} ) \leqslant 0 , \mathbf {x} \in \mathbb {R} ^ {m} \}$ ¼ f j ð Þ 2 gand p(x) is the joint probability function.
  - 可迁移句型：{object} engineering design, when uncertainties are involved, the failure probability $P _ {f}$ of the limit state function (LSF) g(x) should be examined. $P _ {f}$ is essentially a multi-dimensional integral formulated as $$P _ {f} = \int \int \cdots \int _ {
### gap/转折句
- 原句：The numerical integral and direct Monte Carlo Simulation (MCS) are difficult for a complex system with implicit time-consuming analysis models.
  - 可迁移句型：{object} numerical integral and direct Monte Carlo Simulation (MCS) are difficult for a complex system with implicit time-consuming analysis models.
- 原句：To calculate the integral with the original LSF faces enormous computational challenges [1–2].
  - 可迁移句型：{object} calculate the integral with the original LSF faces enormous computational challenges [1–2].
- 原句：However, it requires the independent input variables obey normal distribution, which is difficult to be satisfied in practical problems.
  - 可迁移句型：{object}, it requires the independent input variables obey normal distribution, which is difficult to be satisfied in practical problems.
- 原句：However, the optimization with an equality constraint to find the MPP increases the number of the LSF evaluations.
  - 可迁移句型：{object}, the optimization with an equality constraint to find the MPP increases the number of the LSF evaluations.
### 方法提出句
- 原句：A radial basis function (RBF) based sequential surrogate reliability method (SSRM) is proposed, in which a special optimization problem is solved to update the surrogate model of the limit state function (LSF) iteratively.
  - 可迁移句型：{object} radial basis function (RBF) based sequential surrogate reliability method (SSRM) is proposed, in which a special optimization problem is solved to update the surrogate model of the limit state function (LSF) iteratively.
- 原句：By updating the surrogate model with the new points, the surrogate model of LSF becomes more and more accurate in the important region with a high failure probability and on the LSF boundary.
  - 可迁移句型：{object} updating the surrogate model with the new points, the surrogate model of LSF becomes more and more accurate in the important region with a high failure probability and on the LSF boundary.
- 原句：Several numerical examples show that SSRM improves the accuracy of the surrogate model in the important region around the failure boundary with a small number of samples and has a better adaptability to the nonlinear LSF, hence increases the accuracy and efficiency of the reliability analysis. �2018 Elsevier Ltd.
  - 可迁移句型：{object} numerical examples show that SSRM improves the accuracy of the surrogate model in the important region around the failure boundary with a small number of samples and has a better adaptability to the nonlinear LSF, hence increases the accuracy and effi
- 原句：The numerical integral and direct Monte Carlo Simulation (MCS) are difficult for a complex system with implicit time-consuming analysis models.
  - 可迁移句型：{object} numerical integral and direct Monte Carlo Simulation (MCS) are difficult for a complex system with implicit time-consuming analysis models.
### 结果证明句
- 原句：Several numerical examples show that SSRM improves the accuracy of the surrogate model in the important region around the failure boundary with a small number of samples and has a better adaptability to the nonlinear LSF, hence increases the accuracy and efficiency of the reliability analysis. �2018 Elsevier Ltd.
  - 可迁移句型：{object} numerical examples show that SSRM improves the accuracy of the surrogate model in the important region around the failure boundary with a small number of samples and has a better adaptability to the nonlinear LSF, hence increases the accuracy and effi
- 原句：The mean value method (MVM) [3–4] performs a first-order Taylor expansion of the LSF at the mean point (as shown in Fig.
  - 可迁移句型：{object} mean value method (MVM) [3–4] performs a first-order Taylor expansion of the LSF at the mean point (as shown in Fig.
- 原句：The first-order reliability method (FORM) [5–8] transforms random variables with different distributions into the same standard normal space U by Rosenblatt transformation [9] and then performs a first-order Taylor expansion at the most probable point (MPP) which has the maximum failure probability on the LSF (as shown in Fig.
  - 可迁移句型：{object} first-order reliability method (FORM) [5–8] transforms random variables with different distributions into the same standard normal space U by Rosenblatt transformation [9] and then performs a first-order Taylor expansion at the most probable point (MP
- 原句：As shown in Table 1, $r = \| \mathbf {x} - \mathbf {x} _ {i} \|$ is the Euclidian distance ð Þ ¼ k  kbetween two samples, and c is the shape parameter.
  - 可迁移句型：{object} shown in Table 1, $r = \| \mathbf {x} - \mathbf {x} _ {i} \|$ is the Euclidian distance ð Þ ¼ k  kbetween two samples, and c is the shape parameter.
### 贡献收束句
- 原句：Moreover, the accuracy of the unimportant region is further improved within the iteration due to the minimum distance con- straint.
  - 可迁移句型：{object}, the accuracy of the unimportant region is further improved within the iteration due to the minimum distance con- straint.
- 原句：Several numerical examples show that SSRM improves the accuracy of the surrogate model in the important region around the failure boundary with a small number of samples and has a better adaptability to the nonlinear LSF, hence increases the accuracy and efficiency of the reliability analysis. �2018 Elsevier Ltd.
  - 可迁移句型：{object} numerical examples show that SSRM improves the accuracy of the surrogate model in the important region around the failure boundary with a small number of samples and has a better adaptability to the nonlinear LSF, hence increases the accuracy and effi
- 原句：Therefore, different approximations of the LSF are adopted to improve the computational efficiency of reliability analysis.
  - 可迁移句型：{object}, different approximations of the LSF are adopted to improve the computational efficiency of reliability analysis.
- 原句：The sequential surrogate model captures more meaningful failure features in the important region, while reduces the samples in the region with low failure probability.
  - 可迁移句型：{object} sequential surrogate model captures more meaningful failure features in the important region, while reduces the samples in the region with low failure probability.
### 边界/谨慎句
- 原句：In engineering design, when uncertainties are involved, the failure probability $P _ {f}$ of the limit state function (LSF) g(x) should be examined. $P _ {f}$ is essentially a multi-dimensional integral formulated as $$P _ {f} = \int \int \cdots \int _ {D} {\sf p} ( {\bf x} ) {\sf d} x _ {1} {\sf d} x _ {2} \cdot \cdot \cdot {\sf d} x _ {m}\tag{1}$$ where $D$ is the failure region defined as $D = \{\mathbf {x} | \mathbf {g} ( \mathbf {x} ) \leqslant 0 , \mathbf {x} \in \mathbb {R} ^ {m} \}$ ¼ f j ð Þ 2 gand p(x) is the joint probability function.
  - 可迁移句型：{object} engineering design, when uncertainties are involved, the failure probability $P _ {f}$ of the limit state function (LSF) g(x) should be examined. $P _ {f}$ is essentially a multi-dimensional integral formulated as $$P _ {f} = \int \int \cdots \int _ {
- 原句：1), in which the LSF is assumed to be normal distribution.
  - 可迁移句型：1), in which the {object} is assumed to be normal distribution.
- 原句：Moreover, the adaptability to nonlinear boundary is still limited [10–11].
  - 可迁移句型：{object}, the adaptability to nonlinear boundary is still limited [10–11].
- 原句：The response surface is a different commonly used reliability analysis method [14–16].
  - 可迁移句型：{object} response surface is a different commonly used reliability analysis method [14–16].

## 9. 引用风险层

- 正文引用簇估计：20
- 参考文献条数：54
- 可识别年份条目数：53
- 2021 年及以后参考文献数：0
- 2010 年以前经典文献数：31
- 高频来源粗略识别：Struct Saf(8)；Probab Eng Mech(5)；Struct Eng Mech(2)；Prog Aerosp Sci(1)；Application of First-order(1)；First-order and Second-order Reliability Methods. Springer Us(1)；First Order Saddlepoint Approximation for Reliability Analysis. Aiaa J(1)；Nucl Eng Des(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] Crespo LG, Kenny SP, Giesy DP. The Nasa Langley Multidisciplinary Uncertainty Quantification Challenge//AIAA Non-Deterministic Approaches Conference, 2015.
- [2] Yao W, Chen X, Luo W, et al. Review of Uncertainty-based Multidisciplinary Design Optimization Methods for Aerospace Vehicles. Prog Aerosp Sci 2011;47 (1):450–79.
- [3] Choi SK, Canfield RA, Grandhi RV. Reliability-based Structural Design. London: Springer; 2007. p. 207–12.
- [4] Verma AK, Srividya A, Karanki DR. Reliability and Safety Engineering. Springer; 2009. p. 15–167.
- [5] Cawlfield JD. Application of First-order (form) and Second-order (sorm) Reliability Methods: Analysis and Interpretation of Sensitivity Measures Related to Groundwater Pressure Decreases and Resulting Ground Subsidence. Sensitivity Anal, 317–327.
- [6] Du X. Unified Uncertainty Analysis By the First Order Reliability Method. J Mech Des, 2008;130(9).
- [7] Haldar A, Mahadevan S. First-order and Second-order Reliability Methods. Springer Us 1995:27–52.
- [8] Verderaime V. Illustrated Structural Application of Universal First-order Reliability Method. Nasa Sti/recon Technical Report N, 1994, 95(August 1994).
- [9] Du X, Sudjianto A. First Order Saddlepoint Approximation for Reliability Analysis. Aiaa J 2004;42(6):1199–207.
- [10] Faragher J. Probabilistic Methods for the Quantification of Uncertainty and Error in Computational Fluid Dynamics Simulations.
- [11] Mitteau JC. Error Evaluations for the Computation of Failure Probability in Static Structural Reliability Problems. Probab Eng Mech 1999;14(1):119–35.
- [12] Cizelj L, Mavko B, Riesch-oppermann H. Application of First and Second Order Reliability Methods in the Safety Assessment of Cracked Steam Generator Tubing. Nucl Eng Des 1994;147(3):359–68.
- [13] Der kiureghian. Second-order Reliability Approximations. J Eng Mech 1987;113(8):1208–1225.
- [14] Faravelli L. Response-surface Approach for Reliability Analysis. J Eng Mech 1989;115(12):2763–81.
- [15] Faravelli L. Structural Reliability Via Response Surface. Nonlinear Stochastic Mechanics, 1992.

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
