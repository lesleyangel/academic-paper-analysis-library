# 论文深度拆解：033-hp-Adaptive-RPD-based-sequential-convex-programming-_2022_Aerospace-Science

> 生成依据：`801/cleantext/033-hp-Adaptive-RPD-based-sequential-convex-programming-_2022_Aerospace-Science`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`033-hp-Adaptive-RPD-based-sequential-convex-programming-_2022_Aerospace-Science`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\hp-Adaptive-RPD-based-sequential-convex-programming-_2022_Aerospace-Science-.pdf`
- 页数：16
- clean body 字符数：54990
- 摘要字符数：1221
- 参考文献条数：37
- 图题数：13
- 表题数：4
- 表格文件数：5
- 公式候选数：272
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "low_confidence_formulas", "severity": "medium", "message": "35 formula(s) need manual review."}]

## 1. 身份层

- 标题：033-hp-Adaptive-RPD-based-sequential-convex-programming-_2022_Aerospace-Science
- 年份：2022
- 期刊/来源：Aerospace Science
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：方法/算法 + 数值验证型
- 研究对象：Considering the high flight safety requirements and unpredictable flight states, improving the performance of trajectory optimization, including stability, computational efficiency, and result accuracy, is very important [4–6]. However, since SCP belongs to the direct method category, essentially, discretization is also a crucial factor affecting the accuracy of the solution and the efficiency. More importantly, the optimal trajectory with as high precision as possible can be obtained with fewer
- 主要方法：Communicated by Xingqun Zhan Sequential convex programming (SCP) methods have been developed to solve reentry trajectory optimization problems. Due to the oversimplified discretization and iteration, the accuracy and efficiency of the existing SCP methods can be further improved. In this paper, a SCP algorithm based on the hp- adaptive Radau pseudospectral discretization (RPD) is proposed.
- 主要证据：图表 17 个标题、公式 272 个候选、参考文献 37 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“Considering the high flight safety requirements and unpredictable flight states, improving the performance of trajectory optimization, including stability, computational efficiency”，可以通过“Communicated by Xingqun Zhan Sequential convex programming (SCP) methods have been developed to solve reentry trajectory optimization problems. Due to the oversimplified discretization and iteration, the accuracy and eff”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：Due to the oversimplified discretization and iteration, the accuracy and efficiency of the existing SCP methods can be further improved. In the last stage, the linearization error is reduced by several iterations without updating mesh, and the regularization technique is utilized to improve the convergence rate of this process. With comparable or even higher results accuracy, the CPU time reduced by 40%-70% when compared to other SCP methods, and is only twentieth of that of GPOPS-II.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：Considering the high flight safety requirements and unpredictable flight states, improving the performance of trajectory optimization, including stability, computational efficiency, and result accuracy, is very important [4–6]. However, since SCP belongs to the direct method category, essentially, discretization is also a crucial factor affecting the accuracy of the solution and the efficiency. More importantly, the optimal trajectory with as high precision as possible can be obtained with fewer discretized points through reasonable mesh updating.
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
- 作者声明或文本中可见 gap：However, in the general SCP methods, only the very simple destination and differential approximation methods are considered. For problems with relatively flat state variation, this method can obtain a high-precision solution, but once the fluctuation is violent, there will be a large discretization error because the uniformly distributed discretized points are difficult to capture the local regulation of some states. Since the trajectory accuracy is not directly calculated in the iteration process, it is necessary to evaluate the accuracy of the optimization results by the integral results $X _ {i n t}$ .
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- 未在 Introduction 中稳定识别“带引用的 gap 句”，建议人工复核文献转折段。

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：Communicated by Xingqun Zhan Sequential convex programming (SCP) methods have been developed to solve reentry trajectory optimization problems. Due to the oversimplified discretization and iteration, the accuracy and efficiency of the existing SCP methods can be further improved. In this paper, a SCP algorithm based on the hp- adaptive Radau pseudospectral discretization (RPD) is proposed.
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
| Communicated by Xingqun Zhan Sequential convex programming (SCP) methods have been developed to solve reentry trajectory optimization problems. | 摘要/引言/结论候选 | 图：Fig. 1. Coordinate system and states notations. ⎧ ⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Due to the oversimplified discretization and iteration, the accuracy and efficiency of the existing SCP methods can be further improved. | 摘要/引言/结论候选 | 图：Fig. 2. Division of segments and distribution of discretized points. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In this paper, a SCP algorithm based on the hp- adaptive Radau pseudospectral discretization (RPD) is proposed. | 摘要/引言/结论候选 | 图：Fig. 3. Sparsity pattern of the differentiation matrix. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In the proposed algorithm, the iteration process is divided into three stages depending on the characteristics of subproblems. | 摘要/引言/结论候选 | 表：Table 1 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In the last stage, the linearization error is reduced by several iterations without updating mesh, and the regularization technique is utilized to improve the convergence rate of this process. | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The proposed algorithm is validated and examined by a typical reentry example. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (41.17, 696.06, 197.43, 715.22)]] * Corresponding author | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Coordinate system and states notations. ⎧ ⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 2. Division of segments and distribution of discretized points. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 3. Sparsity pattern of the differentiation matrix. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4. Altitude histories for maximum longitudinal reentry. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 5. Ground tracks for maximum longitudinal reentry. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 6. Bank angle history and error of control defined by 1 −(u2 1 + u2 2). | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 7. Longitude-altitude curve updates during the iteration. (For interpretation of the colors in the figure(s), the reader is referred to the web version of  | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 8. Mean of five state residual and max differential error history. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 9. Number of discretized points and CPU time for each iteration. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 10. Optimal longitude-altitude curves obtained by different algorithms. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 11. Maximum residual history in different algorithms. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 1. Coordinate system and states notations. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 6. Bank angle history and error of control defined by $1 - ( u _ { 1 } ^ { 2 } + u _ { 2 } ^ { 2 } )$ | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (41.17, 696.06, 197.43, 715.22)]] * Corresponding author. E-mail address: le | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (70.83, 260.42, 118.71, 273.71)]] r′ = sinγ /D | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (70.98, 274.5, 167.15, 287.79)]] θ′ = cosγ sinψ/rD cosφ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 3, bbox (70.98, 288.57, 288.83, 316.39)]] φ′ = cosγ cosψ/rD γ ′ = [L cosσ/m + (υ2 -μ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 3, bbox (70.98, 332.17, 248.47, 345.46)]] ψ′ = [L sinσ/m cosγ + υ2 cosγ sinψ tanφ/r | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 3, bbox (91.32, 319.98, 281.54, 330.92)]] + rω2(cosγ cosφ + sinγ sinφ cosψ) cosφ]/υ2 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 3, bbox (91.93, 347.42, 359.82, 359.99)]] -2ωυ(tanγ cosψ cosφ -sinφ) + rω2 sinψ sinφ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.62; needs_review; source=equations; [page 3, bbox (61.55, 429.95, 557.7, 459.7)]] � L = ρυ2CL Sref/2 D = ρυ2C D Sref/2 (2) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> Communicated by Xingqun Zhan
> Sequential convex programming (SCP) methods have been developed to solve reentry trajectory optimization problems. Due to the oversimplified discretization and iteration, the accuracy and efficiency of the existing SCP methods can be further improved. In this paper, a SCP algorithm based on the hp- adaptive Radau pseudospectral discretization (RPD) is proposed. In the proposed algorithm, the iteration process is divided into three stages depending on the characteristics of subproblems. The constraint relaxation technique is applied in the first stage to ensure that the iteration is stable. During the second stage, the number and position of discretized points will be updated adaptively according to the discretization error and the curvature of state. In the last stage, the linearization error is reduced by several iterations without updating mesh, and the regularization technique is utilized to improve the convergence rate of this process. The proposed algorithm is validated and examined by a typical reentry example. With comparable or even higher results accuracy, the CPU time reduced by 40%-70% when compared to other SCP methods, and is only twentieth of that of GPOPS-II.

### 7.4 摘要中文翻译

> Xingqun Zhan 通讯 顺序凸规划（SCP）方法已被开发来解决再入轨迹优化问题。由于过于简化的离散化和迭代，现有SCP方法的准确性和效率可以进一步提高。本文提出了一种基于hp自适应Radau伪谱离散化(RPD)的SCP算法。在该算法中，根据子问题的特点将迭代过程分为三个阶段。第一阶段应用约束松弛技术以确保迭代稳定。在第二阶段，离散点的数量和位置将根据离散化误差和状态曲率自适应更新。在最后阶段，通过多次迭代来减少线性化误差而不更新网格，并利用正则化技术来提高该过程的收敛速度。通过一个典型的重入示例对所提出的算法进行了验证和检验。在结果精度相当甚至更高的情况下，与其他 SCP 方法相比，CPU 时间减少了 40%-70%，仅为 GPOPS-II 的二十分之一。

### 7.5 结论完整摘录

识别到的结论位置：6. Conclusions

> Trajectory optimization based on SCP is widely used in the aerospace community. The core of SCP is the convexification technology, especially the lossless convexification technology about non-convex control constraints. However, since SCP belongs to the direct method category, essentially, discretization is also a crucial factor affecting the accuracy of the solution and the efficiency. The main contribution of this paper is to improve the existing SCP method in terms of discretization and iteration, and the SCP with hp-adaptive RPD is proposed. The application of hp-adaptive RPD makes the scale of the subproblem in the iteration process gradually increase, thus improving the solving efficiency on the whole. More importantly, the optimal trajectory with as high precision as possible can be obtained with fewer discretized points through reasonable mesh updating. In addition, constraint relaxation and regularization techniques are used at the beginning and end of iteration, respectively, to make the proposed algorithm insensitive to initial values and achieve fast convergence at the end. Compared with other methods, the algorithm proposed in this paper has strong competitiveness.
> 
> Although the regularization term is added to the optimization objective in this paper to improve the convergence rate of the iteration process, its linear convergence property is not changed. In future work, we want to utilize the Hessian matrix of nonlinear functions as the weight of the regularization item, which may boost the algorithm’s performance even more.

### 7.6 结论中文翻译

> 基于SCP的轨迹优化在航空航天领域得到广泛应用。 SCP的核心是凸化技术，特别是关于非凸控制约束的无损凸化技术。但由于SCP属于直接法范畴，本质上，离散化也是影响求解精度和效率的关键因素。本文的主要贡献是在离散化和迭代方面改进了现有的SCP方法，提出了hp自适应RPD的SCP。 hp自适应RPD的应用使得迭代过程中子问题的规模逐渐增大，从而整体上提高了求解效率。更重要的是，通过合理的网格更新，可以用更少的离散点获得尽可能高精度的最优轨迹。此外，在迭代开始和结束时分别使用约束松弛和正则化技术，使所提出的算法对初始值不敏感，并在最后实现快速收敛。与其他方法相比，本文提出的算法具有很强的竞争力。虽然本文在优化目标中加入正则化项来提高迭代过程的收敛速度，但其线性收敛特性并未改变。在未来的工作中，我们希望利用非线性函数的Hessian矩阵作为正则化项的权重，这可能会进一步提高算法的性能。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 6278 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. Problem formulation | 方法建构 | 307 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 3 | 2.1. Motion equations | 对象/条件/子问题展开 | 3410 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 2.2. Choice of control variable | 对象/条件/子问题展开 | 1383 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 2.3. Optimal control problem | 对象/条件/子问题展开 | 2073 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 3. Convexification and discretization | 对象/条件/子问题展开 | 165 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 3.1. Convexification | 对象/条件/子问题展开 | 5662 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 3.2. Discretization and approximation | 对象/条件/子问题展开 | 2663 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 3.3. Convex optimization subproblem | 对象/条件/子问题展开 | 5267 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 4.1. Differential error and state curvature | 对象/条件/子问题展开 | 1842 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 4.2. hp-Adaptive RPD | 对象/条件/子问题展开 | 1983 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 4.3. Iteration process | 对象/条件/子问题展开 | 5694 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 5. Numerical simulations and discussion | 结果验证/讨论 | 1347 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 14 | 5.1. Solve by the proposed algorithm | 方法建构 | 3824 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 15 | 5.2. Convergence analysis of the proposed algorithm | 方法建构 | 5882 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 16 | 5.3. Comparison with other algorithms | 方法建构 | 4995 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 17 | 6. Conclusions | 主张回收/边界说明 | 1563 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |

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

- 高频词：pmb(82)；mathrm(61)；mathcal(53)；tag(49)；array(44)；optimization(43)；error(43)；points(43)；iteration(42)；stage(42)；lambda(40)；trajectory(36)；state(35)；frac(35)；discretized(34)；prime(34)；end(34)；algorithm(32)；discretization(30)；rpd(30)
- 高频学术名词/术语：optimization(43)；iteration(42)；discretization(30)；convergence(19)；segment(17)；relaxation(14)；reference(13)；solution(11)；regularization(11)；convexification(10)；section(9)；distribution(9)；performance(6)；normalization(6)；linearization(6)
- 高频学术动词：obtained(11)；obtain(5)；compared(4)；evaluate(3)；introduced(3)；optimized(1)；presented(1)；indicate(1)；demonstrate(1)；evaluated(1)
- 高频形容词：mathcal(53)；partial(28)；differential(26)；initial(23)；segment(17)；leqslant(16)；optimal(15)；terminal(13)；hp-adaptive(12)；variable(10)；pseudospectral(7)；polynomial(7)；table(7)；objective(6)；lossless(6)
- 高频副词：respectively(13)；gradually(10)；directly(4)；especially(3)；relatively(2)；finally(2)；generally(2)；rapidly(2)；slowly(2)；basically(2)；slightly(2)；significantly(2)
- 高频二词短语：pmb pmb(42)；discretized points(31)；begin array(22)；end array(22)；lambda lambda(22)；mathrm new(20)；trajectory optimization(17)；cpu time(17)；differential error(16)；array tag(14)；number discretized(13)；frac partial(13)；cos gamma(12)；iteration process(11)；hp-adaptive rpd(10)
- 高频三词短语：pmb pmb pmb(26)；lambda lambda lambda(15)；end array tag(14)；number discretized points(13)；left begin array(8)；end array right(8)；mathrm new mathrm(8)；trajectory optimization problem(7)；new mathrm new(7)；array right tag(6)；convex optimization subproblem(6)；frac partial partial(6)
- 被动语态估计：115
- `we + 动作动词` 主动句估计：1
- 一般现在时线索：289
- 一般过去时线索：266
- 现在完成时线索：1
- 情态动词线索：46

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Trajectory optimization plays a key role with regard to improved guidance and control for the reusable vehicle, especially in the reentry phase [1].
  - 可迁移句型：{object} optimization plays a key role with regard to improved guidance and control for the reusable vehicle, especially in the reentry phase [1].
- 原句：Considering the high flight safety requirements and unpredictable flight states, improving the performance of trajectory optimization, including stability, computational efficiency, and result accuracy, is very important [4–6].
  - 可迁移句型：{object} the high flight safety requirements and unpredictable flight states, improving the performance of trajectory optimization, including stability, computational efficiency, and result accuracy, is very important [4–6].
- 原句：The rapid generation of an accurate reference trajectory plays a crucial role in guidance effects and flight safety [11–13].
  - 可迁移句型：{object} rapid generation of an accurate reference trajectory plays a crucial role in guidance effects and flight safety [11–13].
- 原句：The trust region radius and the allowable iteration error vector are chosen as follows. $$\begin{array} {l} {\displaystyle \varDelta = \left[ \frac {20 \mathrm{km}} {R _ {e}} , \frac {20 \pi} {180} , \frac {20 \pi} {180} , \frac {20 \pi} {180} , \frac {20 \pi} {180} \right] ^ {T}} \\ {\displaystyle \epsilon = \left[ \frac {1 \mathrm{m}} {R _ {e}} , \frac {d _ {\varepsilon} \pi} {180} , \frac {d _ {\varepsilon} \pi} {180} , \frac {d _ {\varepsilon} \pi} {180} , \frac {d _ {\varepsilon} \pi} {180} \right] ^ {T} , \quad {d _ {\varepsilon} = 10} ^ {- 4}} \end{array}\tag{51}$$ (52) The initial and terminal conditions, the upper bounds of path constraints, and the model parameters are listed in Table 1.
  - 可迁移句型：{object} trust region radius and the allowable iteration error vector are chosen as follows. $$\begin{array} {l} {\displaystyle \varDelta = \left[ \frac {20 \mathrm{km}} {R _ {e}} , \frac {20 \pi} {180} , \frac {20 \pi} {180} , \frac {20 \pi} {180} , \frac {20
### gap/转折句
- 原句：However, in the general SCP methods, only the very simple destination and differential approximation methods are considered.
  - 可迁移句型：{object}, in the general SCP methods, only the very simple destination and differential approximation methods are considered.
- 原句：For problems with relatively flat state variation, this method can obtain a high-precision solution, but once the fluctuation is violent, there will be a large discretization error because the uniformly distributed discretized points are difficult to capture the local regulation of some states.
  - 可迁移句型：{object} problems with relatively flat state variation, this method can obtain a high-precision solution, but once the fluctuation is violent, there will be a large discretization error because the uniformly distributed discretized points are difficult to capt
- 原句：However, since SCP belongs to the direct method category, essentially, discretization is also a crucial factor affecting the accuracy of the solution and the efficiency.
  - 可迁移句型：{object}, since SCP belongs to the direct method category, essentially, discretization is also a crucial factor affecting the accuracy of the solution and the efficiency.
- 原句：More importantly, the optimal trajectory with as high precision as possible can be obtained with fewer discretized points through reasonable mesh updating.
  - 可迁移句型：{object} importantly, the optimal trajectory with as high precision as possible can be obtained with fewer discretized points through reasonable mesh updating.
### 方法提出句
- 原句：Communicated by Xingqun Zhan Sequential convex programming (SCP) methods have been developed to solve reentry trajectory optimization problems.
  - 可迁移句型：{object} by Xingqun Zhan Sequential convex programming (SCP) methods have been developed to solve reentry trajectory optimization problems.
- 原句：Due to the oversimplified discretization and iteration, the accuracy and efficiency of the existing SCP methods can be further improved.
  - 可迁移句型：{object} to the oversimplified discretization and iteration, the accuracy and efficiency of the existing SCP methods can be further improved.
- 原句：In this paper, a SCP algorithm based on the hp- adaptive Radau pseudospectral discretization (RPD) is proposed.
  - 可迁移句型：{object} This study, a SCP algorithm based on the hp- adaptive Radau pseudospectral discretization (RPD) is proposed.
- 原句：In the proposed algorithm, the iteration process is divided into three stages depending on the characteristics of subproblems.
  - 可迁移句型：{object} the proposed algorithm, the iteration process is divided into three stages depending on the characteristics of subproblems.
### 结果证明句
- 原句：With comparable or even higher results accuracy, the CPU time reduced by 40%-70% when compared to other SCP methods, and is only twentieth of that of GPOPS-II.
  - 可迁移句型：{object} comparable or even higher results accuracy, the CPU time reduced by 40%-70% when compared to other SCP methods, and is only twentieth of that of GPOPS-II.
- 原句：In this section, a typical reentry trajectory optimization problem for hypersonic vehicle dubbed CAV-H [36] will be used to demonstrate the proposed algorithm.
  - 可迁移句型：{object} this section, a typical reentry trajectory optimization problem for hypersonic vehicle dubbed CAV-H [36] will be used to demonstrate the proposed algorithm.
- 原句：Since the trajectory accuracy is not directly calculated in the iteration process, it is necessary to evaluate the accuracy of the optimization results by the integral results $X _ {i n t}$ .
  - 可迁移句型：{object} the trajectory accuracy is not directly calculated in the iteration process, it is necessary to evaluate the accuracy of the optimization results by the integral results $X _ {i n t}$ .
- 原句：The explicit Runge-Kutta (4,5) formula is used to obtain the integral results in this paper, and the definitions of the maximum error $\mathcal {E} _ {\mathrm{max}}$ , the average error $\mathcal {E} _ {\mathrm In this section, a typical reentry trajectory optimization problem for hypersonic vehicle dubbed CAV-H [36] will be used to demonstrate the proposed algorithm.
  - 可迁移句型：{object} explicit Runge-Kutta (4,5) formula is used to obtain the integral results in This study, and the definitions of the maximum error $\mathcal {E} _ {\mathrm{max}}$ , the average error $\mathcal {E} _ {\mathrm In this section, a typical reentry trajector
### 贡献收束句
- 原句：Due to the oversimplified discretization and iteration, the accuracy and efficiency of the existing SCP methods can be further improved.
  - 可迁移句型：{object} to the oversimplified discretization and iteration, the accuracy and efficiency of the existing SCP methods can be further improved.
- 原句：In the last stage, the linearization error is reduced by several iterations without updating mesh, and the regularization technique is utilized to improve the convergence rate of this process.
  - 可迁移句型：{object} the last stage, the linearization error is reduced by several iterations without updating mesh, and the regularization technique is utilized to improve the convergence rate of this process.
- 原句：With comparable or even higher results accuracy, the CPU time reduced by 40%-70% when compared to other SCP methods, and is only twentieth of that of GPOPS-II.
  - 可迁移句型：{object} comparable or even higher results accuracy, the CPU time reduced by 40%-70% when compared to other SCP methods, and is only twentieth of that of GPOPS-II.
- 原句：Trajectory optimization plays a key role with regard to improved guidance and control for the reusable vehicle, especially in the reentry phase [1].
  - 可迁移句型：{object} optimization plays a key role with regard to improved guidance and control for the reusable vehicle, especially in the reentry phase [1].
### 边界/谨慎句
- 原句：With comparable or even higher results accuracy, the CPU time reduced by 40%-70% when compared to other SCP methods, and is only twentieth of that of GPOPS-II.
  - 可迁移句型：{object} comparable or even higher results accuracy, the CPU time reduced by 40%-70% when compared to other SCP methods, and is only twentieth of that of GPOPS-II.
- 原句：However, in the general SCP methods, only the very simple destination and differential approximation methods are considered.
  - 可迁移句型：{object}, in the general SCP methods, only the very simple destination and differential approximation methods are considered.
- 原句：In this case, $n _ {r e l}$ in the approach stage is all 2, which means that only one differential constraint relaxation with parameter δr is required to make the subproblem feasible.
  - 可迁移句型：{object} this case, $n _ {r e l}$ in the approach stage is all 2, which means that only one differential constraint relaxation with parameter δr is required to make the subproblem feasible.
- 原句：In future work, we want to utilize the Hessian matrix of nonlinear functions as the weight of the regularization item, which may boost the algorithm’s performance even more.
  - 可迁移句型：{object} future work, we want to utilize the Hessian matrix of nonlinear functions as the weight of the regularization item, which may boost the algorithm’s performance even more.

## 9. 引用风险层

- 正文引用簇估计：25
- 参考文献条数：37
- 可识别年份条目数：54
- 2021 年及以后参考文献数：7
- 2010 年以前经典文献数：9
- 高频来源粗略识别：Guid. Control Dyn(9)；Sci. Technol(8)；Optim. Appl(2)；Ind. Electron(1)；Astronaut. Sci(1)；Aerosp. Sci(1)；Spacecr. Rockets(1)；Control Syst. Technol(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] B. Tian, W. Fan, R. Su, Q. Zong, Real-time trajectory and attitude coordination control for reusable launch vehicle in reentry phase, IEEE Trans. Ind. Electron. 62 (3) (2015) 1639–1650, https://doi .org /10 .1109 /TIE .2014 .2341553.
- [2] A.V. Rao, A survey of numerical methods for optimal control, Adv. Astronaut. Sci. 135 (1) (2010) 497–528, https://www.webofscience .com /wos /alldb /full -record /WOS : 000280501900030.
- [3] R. Chai, A. Savvaris, A. Tsourdos, S. Chai, Y. Xia, A review of optimization techniques in spacecraft flight trajectory design, Prog. Aerosp. Sci. 109 (2019) 100543, https:// doi .org /10 .1016 /j .paerosci .2019 .05 .003.
- [4] K.D. Mease, J. Kremer, Shuttle entry guidance revisited using nonlinear geometric methods, J. Guid. Control Dyn. 17 (6) (1994) 1350–1356, https://doi .org /10 .2514 /3 . 21355.
- [5] A. Caruso, A.A. Quarta, G. Mengali, M. Ceriotti, Shape-based approach for solar sail trajectory optimization, Aerosp. Sci. Technol. 107 (2020) 106363, https://doi .org /10 . 1016 /j .ast .2020 .106363.
- [6] Y. Zheng, X. Fu, M. Xu, Q. Li, M. Lin, Ascent trajectory design of small-lift launch vehicle using hierarchical optimization, Aerosp. Sci. Technol. 107 (2020) 106285, https:// doi .org /10 .1016 /j .ast .2020 .106285.
- [7] K. Mease, P. Teufel, H. Schoenenberger, D. Chen, S. Bharadwaj, Re-entry trajectory planning for a reusable launch vehicle, in: 24th Atmospheric Flight Mechanics Confer- ence, Portland, OR, U.S.A., 1999.
- [8] D.A. Benson, G.T. Huntington, T.P. Thorvaldsen, A.V. Rao, Direct trajectory optimization and costate estimation via an orthogonal collocation method, J. Guid. Control Dyn. 29 (6) (2006) 1435–1440, https://doi .org /10 .2514 /1.20478.
- [9] S. Kameswaran, L.T. Biegler, Convergence rates for direct transcription of optimal control problems using collocation at Radau points, Comput. Optim. Appl. 41 (1) (2008) 81–126, https://doi .org /10 .1007 /s10589 -007 -9098 -9.
- [10] D. Garg, et al., A unified framework for the numerical solution of optimal control problems using pseudospectral methods, Automatica 46 (11) (2010) 1843–1851, https:// doi .org /10 .1016 /j .automatica .2010 .06 .048.
- [11] P. Lu, Entry guidance and trajectory control for reusable launch vehicle, J. Guid. Control Dyn. 20 (1) (1997) 143–149, https://doi .org /10 .2514 /2 .4008.
- [12] S. Bharadwaj, A.V. Rao, K.D. Mease, Entry trajectory tracking law via feedback linearization, J. Guid. Control Dyn. 21 (5) (1998) 726–732, https://doi .org /10 .2514 /2 .4318.
- [13] P. Lu, J.M. Hanson, Entry guidance for the x-33 vehicle, J. Spacecr. Rockets 35 (3) (1998) 342–349, https://doi .org /10 .2514 /2 .3332.
- [14] P. Lu, Introducing computational guidance and control, J. Guid. Control Dyn. 40 (2) (2017) 193, https://doi .org /10 .2514 /1.G002745.
- [15] T. Sands, Deterministic artificial intelligence, London, United Kingdom, IntechOpen, 2020, Online.

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
