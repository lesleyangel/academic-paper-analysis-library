# 论文深度拆解：A three-stage sequential convex programming approach for trajectory optimization

> 生成依据：`801/cleantext/016-A-three-stage-sequential-convex-programming-approa_2024_Aerospace-Science-an`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`016-A-three-stage-sequential-convex-programming-approa_2024_Aerospace-Science-an`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\A-three-stage-sequential-convex-programming-approa_2024_Aerospace-Science-an.pdf`
- 页数：16
- clean body 字符数：56428
- 摘要字符数：1181
- 参考文献条数：33
- 图题数：15
- 表题数：4
- 表格文件数：6
- 公式候选数：316
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "low_confidence_formulas", "severity": "medium", "message": "39 formula(s) need manual review."}]

## 1. 身份层

- 标题：A three-stage sequential convex programming approach for trajectory optimization
- 年份：2024
- 期刊/来源：Aerospace Science an
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：方法/算法 + 数值验证型
- 研究对象：需结合 Introduction 首段复核；自动抽取未找到显式问题句。
- 主要方法：Recently, sequential convex programming (SCP) has become a potential approach in trajectory optimization because of its high efficiency. To improve stability and discretization accuracy, a three-stage SCP approach based on the hp-adaptive Radau pseudospectral discretization is proposed in this paper. A dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional SCP approaches in terms of accuracy and efficiency.
- 主要证据：图表 19 个标题、公式 316 个候选、参考文献 33 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“需结合 Introduction 首段复核；自动抽取未找到显式问题句。”，可以通过“Recently, sequential convex programming (SCP) has become a potential approach in trajectory optimization because of its high efficiency. To improve stability and discretization accuracy, a three-stage SCP approach based ”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：To improve stability and discretization accuracy, a three-stage SCP approach based on the hp-adaptive Radau pseudospectral discretization is proposed in this paper. A dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional SCP approaches in terms of accuracy and efficiency. Taking online optimization results as guidance instructions [4,5] or constructing a “guidance model” based on offline trajectory optimization data [6] are the two main ways to realize advanced guidance.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：需结合 Introduction 首段复核；自动抽取未找到显式问题句。
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
- 作者声明或文本中可见 gap：Indirect methods [9] have great advantages in solving simple problems, but they are difficult to implement when the control system is a little complicated. However, it is typically difficult to solve an NLP problem, and the performance of the direct method is mostly governed by the nonlinear programming solver. Over the last few years, many scholars proposed using sequence convex optimization (SCP) approaches to solve trajectory optimization problems [11,12].
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- Over the last few years, many scholars proposed using sequence convex optimization (SCP) approaches to solve trajectory optimization problems [11,12].

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：Recently, sequential convex programming (SCP) has become a potential approach in trajectory optimization because of its high efficiency. To improve stability and discretization accuracy, a three-stage SCP approach based on the hp-adaptive Radau pseudospectral discretization is proposed in this paper. A dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional SCP approaches in terms of accuracy and efficiency.
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
| To improve stability and discretization accuracy, a three-stage SCP approach based on the hp-adaptive Radau pseudospectral discretization is proposed in this paper. | 摘要/引言/结论候选 | 图：Fig. 1. A hp Radau pseudospectral discretization scheme. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| A dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional SCP approaches in terms of accuracy and efficiency. | 摘要/引言/结论候选 | 图：Fig. 2. The flowchart of the improved three-stage SCP approach. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| On the other hand, with the development of computational guidance and control [3] technology, the distinction between trajectory optimization and guidance is gradually blurring. | 摘要/引言/结论候选 | 图：Fig. 3. Altitude vs. Longitude evolution. (MR means “mesh refinement” and FC means “fast convergence”.). | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Taking online optimization results as guidance instructions [4,5] or constructing a “guidance model” based on offline trajectory optimization data [6] are the two main ways to realize advanced guidance. | 摘要/引言/结论候选 | 表：Table 1 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| With the improvement of numerical optimization algorithms, it is possible to solve large-scale optimization problems quickly. | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Over the last few years, many scholars proposed using sequence convex optimization (SCP) approaches to solve trajectory optimization problems [11,12]. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 216.4, 690.38)]] * Corresponding author. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. A hp Radau pseudospectral discretization scheme. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 2. The flowchart of the improved three-stage SCP approach. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 3. Altitude vs. Longitude evolution. (MR means “mesh refinement” and FC means “fast convergence”.). | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 4. ψ evolution at e = 4.4 × 1010J in the third stage of iteration. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 5. Altitude time histories and ground track comparison. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 7. Max error vs. iteration with different algorithms. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 8. Mesh-Feature evolution in the second iteration stage. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 9. Altitude and velocity time histories comparison. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 10. Control time histories comparison. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 11. Max error vs. iteration with different algorithms. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 12. Mesh-Feature evolution in the second iteration stage. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 13. Sparsity pattern of all linear constraint coefficient matrixes: The differential matrix in (a) is composed of submatrices with the same structure which | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 14. Sparsity pattern of all linear constraint coefficient matrixes: Unlike the previous example, the trajectory here contains two phases, so the matrix rep | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 4. ψ evolution at $e = 4 . 4 \times 1 0 ^ { 1 0 } \mathrm { J }$ in the third stage of iteration. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 6. Control time histories comparison. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 216.4, 690.38)]] * Corresponding author. E-mail address: leo | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 332.06, 716.91)]] https://doi.org/10.1016/j.ast.2024.109128  | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 2, bbox (307.95, 60.18, 418.69, 78.68)]] P p : minimize J = φ [ x(P)( t(P) f | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (325.82, 84.9, 468.96, 99.73)]] subject to ˙x = f(p)( x(p), u(p)) , p = 1, ⋯, P | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (358.53, 99.58, 482.62, 114.41)]] c \le c(p)( x(p), u(p)) \lec, p = 1, ⋯, P | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (306.6, 305.6, 370.4, 321.78)]] f(p)( x(p), u(p)) = f(p) 0 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (370.89, 305.6, 442.23, 320.44)]] ( x(p)) + B(p)u(p) + f(p) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 2, bbox (419.19, 60.18, 448.8, 76.94)]] )] + ∑ P | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> Recently, sequential convex programming (SCP) has become a potential approach in trajectory optimization because of its high efficiency. To improve stability and discretization accuracy, a three-stage SCP approach based on the hp-adaptive Radau pseudospectral discretization is proposed in this paper. In most instances, the initial subproblem may risk infeasibility due to the undesignated initial guess. Therefore, we design a constraint relaxation stage for the SCP to enhance the feasibility of the subproblem as much as possible. Once the sub problem can be directly solved, the iteration enters the second stage, during which a mesh refinement algorithm based on discretization error analysis is utilized to decrease the discretization error to the tolerance. In the final stage, the damping term is introduced into the objective of the subproblem to suppress the oscillation of the solution and accelerate the convergence. A dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional SCP approaches in terms of accuracy and efficiency.

### 7.4 摘要中文翻译

> 最近，顺序凸规划（SCP）因其高效率而成为轨迹优化的潜在方法。为了提高稳定性和离散化精度，本文提出了一种基于hp自适应Radau伪谱离散化的三阶段SCP方法。在大多数情况下，由于未指定的初始猜测，初始子问题可能面临不可行的风险。因此，我们为SCP设计了一个约束松弛阶段，以尽可能增强子问题的可行性。一旦子问题可以直接求解，迭代进入第二阶段，在此阶段利用基于离散误差分析的网格细化算法将离散误差减小到容许范围内。最后阶段，在子问题的目标中引入阻尼项，以抑制解的振荡并加速收敛。以双通道控制再入轨迹优化和上升轨迹优化为例，仿真结果表明，该方法在精度和效率方面优于传统的SCP方法。

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusions

> In this paper, a three-stage sequential convex programming approach is proposed for general trajectory optimization problems. Based on constraint relaxation, mesh refinement, and iterative damping, the problems of poor iteration stability, large discretization error, and slow convergence speed of conventional SCP approaches are effectively improved. Numerical simulation results show that compared with other SCP approaches, the accuracy of the proposed approach (almost equivalent to GPOPS-II) is improved by 2–4 orders of magnitude, and the CPU time is reduced to a certain extent. The work in this paper further enhances the potential for onboard real-time application of SCP approaches. Moreover, the proposed approach is based on the general form of trajectory optimization problems, therefore, has universality for application.
> 
> The proposed approach still has some limitations. On the one hand, to further accelerate the convergence speed, line search can be used to determine the step size between iterations. On the other hand, it may be more efficient to approximate nonlinear constraints using quadratic functions (which require the use of BFPS, etc., to approximate the Hessian matrix) than simple linearization.

### 7.6 结论中文翻译

> 本文针对一般轨迹优化问题提出了一种三阶段顺序凸规划方法。基于约束松弛、网格细化和迭代阻尼，有效改善了传统SCP方法迭代稳定性差、离散化误差大、收敛速度慢的问题。数值模拟结果表明，与其他SCP方法相比，该方法的精度（几乎相当于GPOPS-II）提高了2~4个数量级，并且CPU时间有一定程度的减少。本文的工作进一步增强了 SCP 方法在机载实时应用的潜力。此外，所提出的方法基于轨迹优化问题的一般形式，因此具有应用的普适性。所提出的方法仍然有一些局限性。一方面，为了进一步加快收敛速度​​，可以使用线搜索来确定迭代之间的步长。另一方面，使用二次函数来逼近非线性约束（需要使用BFPS等来逼近Hessian矩阵）可能比简单的线性化更有效。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 5703 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. Problem formulation | 方法建构 | 3707 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 3 | 3. Methodology | 方法建构 | 468 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 3.1. Direct collocation method with hp RPD | 方法建构 | 7641 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 5 | 3.2. Fundamental of conventional SCP approach | 方法建构 | 11521 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 6 | 3.3. Improved hp-Adaptive mesh refinement algorithm | 方法建构 | 3154 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 7 | Algorithm 1 | 方法建构 | 3015 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 8 | 3.4. The three-stage scp approach | 方法建构 | 4335 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 9 | 4. Simulations and discussion | 结果验证/讨论 | 765 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 10 | 4.1. Reentry trajectory optimization with dual-channel control | 对象/条件/子问题展开 | 8757 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 4.2. Ascent trajectory optimization of launch vehicle | 对象/条件/子问题展开 | 1093 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | Table 4 | 对象/条件/子问题展开 | 4556 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 5. Conclusions | 主张回收/边界说明 | 1226 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |

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

- 高频词：mathbf(410)；delta(146)；mathrm(98)；right(89)；left(88)；array(74)；scp(51)；overline(49)；frac(46)；problem(45)；end(42)；big(41)；tag(39)；begin(37)；optimization(36)；leq(35)；trajectory(28)；control(26)；stage(26)；points(26)
- 高频学术名词/术语：optimization(36)；discretization(24)；iteration(21)；solution(20)；function(18)；convergence(15)；reference(15)；refinement(13)；collocation(9)；relaxation(8)；segment(8)；transcription(7)；dynamics(7)；guidance(6)；section(6)
- 高频学术动词：compared(5)；obtained(5)；indicate(2)；compare(2)；obtain(1)；constructed(1)；propose(1)；introduce(1)；evaluate(1)
- 高频形容词：mathcal(24)；refinement(13)；objective(11)；initial(10)；table(9)；original(8)；segment(8)；general(7)；terminal(7)；numerical(6)；pseudospectral(6)；optimal(5)；hp-adaptive(5)；dynamic(5)；boundary(5)
- 高频副词：respectively(9)；directly(6)；finally(5)；greatly(3)；typically(3)；generally(3)；firstly(3)；successfully(2)；adaptively(2)；explicitly(2)；strictly(2)；slightly(2)
- 高频二词短语：mathbf delta(114)；delta mathbf(112)；mathbf mathbf(86)；overline mathbf(40)；begin array(37)；end array(37)；left right(33)；mathbf left(33)；delta delta(28)；trajectory optimization(21)；left mathbf(20)；frac mathrm(20)；mathbf leq(19)；left begin(16)；array right(16)
- 高频三词短语：delta mathbf delta(111)；mathbf delta mathbf(101)；mathbf left right(21)；mathbf mathbf mathbf(20)；left begin array(16)；end array right(16)；delta delta delta(14)；mathbf delta delta(13)；leq overline mathbf(12)；mathbf end array(12)；end array tag(11)；right end array(11)
- 被动语态估计：84
- `we + 动作动词` 主动句估计：4
- 一般现在时线索：176
- 一般过去时线索：179
- 现在完成时线索：2
- 情态动词线索：37

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：The boundary function b of the endpoint (means initial and terminal) states and time of all phases is used to describe the boundary constraints. $$\begin{array} {r c l} {\displaystyle \mathcal {P} _ {p} : \mathrm{minimize} J} & {=} & {\displaystyle \varphi \Big [ {\pmb x} ^ {( P )} \left( t _ {f} ^ {( P )} \right) \Big ] + \sum _ {p = 1} ^ {P} \int _ {t _ {s} ^ {( P )}} ^ {t _ {f} ^ {( P )}} L ^ {( p )} \big ( \mathbf {x} ^ {( p )} , \mathbf {u} ^ {( p )} \big ) \mathrm{d} t} \\ {\mathrm{subject~to~} \dot {\mathbf {x}}} & {=} & {\mathbf {f} ^ {( p )} \big ( \mathbf {x} ^ {( p )} , \mathbf {u} ^ {( p )} \big ) , p = 1 , \cdots , P} \\ {\displaystyle \qquad \pmb {\mathbb {c}}} & {\leq} & {\mathbf {c} ^ {( p )} \left( x ^ {( p )} , u ^ {( p )} \right) \leq \overline {{\mathbf {c}}} , p = 1 , \cdots , P} \\ {\displaystyle \qquad \quad \mathbf {b}} & {\leq} & {\mathbf {b} \Big [ \mathbf {x} ^ {( 1 )} \left( t _ {s f} ^ {( 1 )} \right) , t _ {s f} ^ {( 1 )} , \cdots , \mathbf {x} ^ {( P )} \left( t _ {s f} ^ {( P )} \right) , t _ {s f} ^ {( P )} \Big ] \leq \overline {{\mathbf {b}}}} \end{array}\tag{1}$$ Dynamical constraints are crucial considerations in trajectory optimization, and the dynamical function $\mathbf {f} ^ {( p )}$ can generally be decomposed into three parts as shown in Eq.(2).
  - 可迁移句型：{object} boundary function b of the endpoint (means initial and terminal) states and time of all phases is used to describe the boundary constraints. $$\begin{array} {r c l} {\displaystyle \mathcal {P} _ {p} : \mathrm{minimize} J} & {=} & {\displaystyle \varph
### gap/转折句
- 原句：Indirect methods [9] have great advantages in solving simple problems, but they are difficult to implement when the control system is a little complicated.
  - 可迁移句型：{object} methods [9] have great advantages in solving simple problems, but they are difficult to implement when the control system is a little complicated.
- 原句：However, it is typically difficult to solve an NLP problem, and the performance of the direct method is mostly governed by the nonlinear programming solver.
  - 可迁移句型：{object}, it is typically difficult to solve an NLP problem, and the performance of the direct method is mostly governed by the nonlinear programming solver.
- 原句：Over the last few years, many scholars proposed using sequence convex optimization (SCP) approaches to solve trajectory optimization problems [11,12].
  - 可迁移句型：{object} the last few years, many scholars proposed using sequence convex optimization (SCP) approaches to solve trajectory optimization problems [11,12].
### 方法提出句
- 原句：Recently, sequential convex programming (SCP) has become a potential approach in trajectory optimization because of its high efficiency.
  - 可迁移句型：{object}, sequential convex programming (SCP) has become a potential approach in trajectory optimization because of its high efficiency.
- 原句：To improve stability and discretization accuracy, a three-stage SCP approach based on the hp-adaptive Radau pseudospectral discretization is proposed in this paper.
  - 可迁移句型：{object} improve stability and discretization accuracy, a three-stage SCP approach based on the hp-adaptive Radau pseudospectral discretization is proposed in This study.
- 原句：A dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional SCP approaches in terms of accuracy and efficiency.
  - 可迁移句型：{object} dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional SCP approaches in terms of accuracy and efficiency.
- 原句：On the other hand, with the development of computational guidance and control [3] technology, the distinction between trajectory optimization and guidance is gradually blurring.
  - 可迁移句型：{object} the other hand, with the development of computational guidance and control [3] technology, the distinction between trajectory optimization and guidance is gradually blurring.
### 结果证明句
- 原句：A dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional SCP approaches in terms of accuracy and efficiency.
  - 可迁移句型：{object} dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional SCP approaches in terms of accuracy and efficiency.
- 原句：Taking online optimization results as guidance instructions [4,5] or constructing a “guidance model” based on offline trajectory optimization data [6] are the two main ways to realize advanced guidance.
  - 可迁移句型：{object} online optimization results as guidance instructions [4,5] or constructing a “guidance model” based on offline trajectory optimization data [6] are the two main ways to realize advanced guidance.
- 原句：Simple discretization schemes and low-order numerical integration and differentiation were used for problem transcription in the early SCP approaches, which undoubtedly resulted in poor accuracy of results.
  - 可迁移句型：{object} discretization schemes and low-order numerical integration and differentiation were used for problem transcription in the early SCP approaches, which undoubtedly resulted in poor accuracy of results.
- 原句：The superscript (p) is used to indicate the phase to which variables belong, and the subscripts s and f represent the initial and terminal moments, respectively.
  - 可迁移句型：{object} superscript (p) is used to indicate the phase to which variables belong, and the subscripts s and f represent the initial and terminal moments, respectively.
### 贡献收束句
- 原句：To improve stability and discretization accuracy, a three-stage SCP approach based on the hp-adaptive Radau pseudospectral discretization is proposed in this paper.
  - 可迁移句型：{object} improve stability and discretization accuracy, a three-stage SCP approach based on the hp-adaptive Radau pseudospectral discretization is proposed in This study.
- 原句：Therefore, we design a constraint relaxation stage for the SCP to enhance the feasibility of the subproblem as much as possible.
  - 可迁移句型：{object}, we design a constraint relaxation stage for the SCP to enhance the feasibility of the subproblem as much as possible.
- 原句：A dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional SCP approaches in terms of accuracy and efficiency.
  - 可迁移句型：{object} dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional SCP approaches in terms of accuracy and efficiency.
- 原句：With the improvement of numerical optimization algorithms, it is possible to solve large-scale optimization problems quickly.
  - 可迁移句型：{object} the improvement of numerical optimization algorithms, it is possible to solve large-scale optimization problems quickly.
### 边界/谨慎句
- 原句：In most instances, the initial subproblem may risk infeasibility due to the undesignated initial guess.
  - 可迁移句型：{object} most instances, the initial subproblem may risk infeasibility due to the undesignated initial guess.
- 原句：The second term is a linear function about u which should be a reasonable choice to ensure linearity, and matrix $\mathbf {B} ^ {( p )}$ could be approximated as constant in each iteration.
  - 可迁移句型：{object} second term is a linear function about u which should be a reasonable choice to ensure linearity, and matrix $\mathbf {B} ^ {( p )}$ could be approximated as constant in each iteration.
- 原句：It should be noted that all variables are dimensionless when solving the problem.
  - 可迁移句型：{object} should be noted that all variables are dimensionless when solving the problem.
- 原句：On the other hand, it may be more efficient to approximate nonlinear constraints using quadratic functions (which require the use of BFPS, etc., to approximate the Hessian matrix) than simple linearization.
  - 可迁移句型：{object} the other hand, it may be more efficient to approximate nonlinear constraints using quadratic functions (which require the use of BFPS, etc., to approximate the Hessian matrix) than simple linearization.

## 9. 引用风险层

- 正文引用簇估计：24
- 参考文献条数：33
- 可识别年份条目数：52
- 2021 年及以后参考文献数：10
- 2010 年以前经典文献数：9
- 高频来源粗略识别：Sci. Technol(5)；Spacecr. Rockets(2)；Program(2)；Ind. Electron(1)；Aeosp. Sci(1)；Astronautical Sci(1)；Control Syst. Technol(1)；Aerosp. Electron. Syst(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] P. Lu, Entry guidance and trajectory control for reusable launch vehicle, J. Guidance, Control, Dyn. 20 (1) (1997) 143–149, https://doi.org/10.2514/ 2.4008.
- [2] D.B. Doman, M.W. Oppenheimer, M.A. Bolender, Progress in guidance and control research for space access and hypersonic vehicles, in: Proceedings of the 45th IEEE Conference on Decision and Control, 2006, https://doi.org/10.1109/ CDC.2006.377649.
- [3] P. Lu, Introducing computational guidance and control, J. Guidance, Control, Dyn. 40 (2) (2017) 193, https://doi.org/10.2514/1.G002745.
- [4] P. Sarmah, C. Chawla, R. Padhi, A nonlinear approach for re-entry guidance of reusable launch vehicles using model predictive static programming, in: 2008 16th Mediterranean Conference on Control and Automation, Ajaccio, Corsica, France, 2008, https://doi.org/10.1109/MED.2008.4602026.
- [5] B. Tian, W. Fan, R. Su, Q. Zong, Real-time trajectory and attitude coordination control for reusable launch vehicle in reentry phase, IEEE Trans. Ind. Electron. 62 (3) (2015) 1639–1650, https://doi.org/10.1109/TIE.2014.2341553.
- [6] Y. Shi, Z. Wang, A deep learning-based approach to real-time trajectory optimization for hypersonic vehicles, AIAA Scitech 2020 Forum, 2020, https://doi. org/10.2514/6.2020-0023.
- [7] R. Chai, A. Savvaris, A. Tsourdos, S. Chai, Y. Xia, A review of optimization techniques in spacecraft flight trajectory design, Prog. Aeosp. Sci. 109 (2019) 100543, https://doi.org/10.1016/j.paerosci.2019.05.003.
- [8] A.V. Rao, A survey of numerical methods for optimal control, Adv. Astronautical Sci. 135 (1) (2010) 497–528, https://doi.org/10.1166/1.6337.
- [9] E. Bryson, Applied optimal control: optimization, estimation and control, Taylor & Francis Group, New York, 1975.
- [10] M. Kelly, An introduction to trajectory optimization: how to do your own direct collocation, SIAM Rev 59 (4) (2017) 849–904, https://doi.org/10.1137/ 16M1062569.
- [11] R. Foust, S. Chung, F.Y. Hadaegh, Optimal guidance and control with nonlinear dynamics using sequential convex programming, J. Guidance, Control, Dyn. 43 (4) (2019) 633–644, https://doi.org/10.2514/1.G004590.
- [12] X. Liu, P. Lu, B. Pan, Survey of convex optimization for aerospace applications, Astrodynamics 1 (1) (2017) 23–40, https://doi.org/10.1007/s42064-017-0003-8.
- [13] J.M.Carson Açıkmes¸e, L. Blackmore, Lossless convexification of nonconvex control bound and pointing constraints of the soft landing optimal control problem, IEEE Trans. Control Syst. Technol. 21 (6) (2013) 2104–2113, https://doi.org/10.1109/ TCST.2012.2237346.
- [14] S. Boyd, S.P. Boyd, L. Vandenberghe: Convex optimization, Cambridge University Press, 2004.
- [15] J. Wang, N. Cui, A pseudospectral-convex optimization algorithm for rocket landing guidance, in: 2018 AIAA Guidance, Navigation, and Control Conference, Kissimmee, Florida, 2018, https://doi.org/10.2514/6.2018-1871.

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
