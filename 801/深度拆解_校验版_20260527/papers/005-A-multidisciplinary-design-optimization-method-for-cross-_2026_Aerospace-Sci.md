# 论文深度拆解：A multidisciplinary design optimization method for cross-domain vehicles based on distributed-centralized augmented Lagrangian coordination

> 生成依据：`801/cleantext/005-A-multidisciplinary-design-optimization-method-for-cross-_2026_Aerospace-Sci`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`005-A-multidisciplinary-design-optimization-method-for-cross-_2026_Aerospace-Sci`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\A-multidisciplinary-design-optimization-method-for-cross-_2026_Aerospace-Sci.pdf`
- 页数：18
- clean body 字符数：62929
- 摘要字符数：1363
- 参考文献条数：38
- 图题数：18
- 表题数：4
- 表格文件数：7
- 公式候选数：260
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "low_confidence_formulas", "severity": "medium", "message": "59 formula(s) need manual review."}]

## 1. 身份层

- 标题：A multidisciplinary design optimization method for cross-domain vehicles based on distributed-centralized augmented Lagrangian coordination
- 年份：2026
- 期刊/来源：Aerospace Sci
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：方法/算法 + 数值验证型
- 研究对象：However, since the flight of this type of vehicle covers both aerospace and aviation domains, the mission and flight environment are complex, and its multidisciplinary design needs to comprehensively consider the flight environment of in-orbit operation and re-entry flight, and the configuration is more complex, which will directly affect the aerodynamic, structural and trajectory disciplines with high timeconsumption and high computational cost, making it more difficult and longer to solve the 
- 主要方法：A nested multidisciplinary design optimization method based on augmented Lagrangian coordination and joint geometric/aerodynamic/structural disciplines modeling is proposed to address the problem of inefficient solving in high time-consuming disciplines such as aerodynamic, structural, and trajectory, brought by the complexity of the cross-domain vehicle configurations. Firstly, integrated geometric-aerodynamic-structural parametric modeling based on the 3D CST method is proposed to realize joint geometric/aerodynamic/structural modeling. Second, a distributed-centralized augmented Lagrangian coordination method that balances efficiency and parallel computation is proposed with an adaptive a
- 主要证据：图表 22 个标题、公式 260 个候选、参考文献 38 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“However, since the flight of this type of vehicle covers both aerospace and aviation domains, the mission and flight environment are complex, and its multidisciplinary design needs”，可以通过“A nested multidisciplinary design optimization method based on augmented Lagrangian coordination and joint geometric/aerodynamic/structural disciplines modeling is proposed to address the problem of inefficient solving i”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：The optimization results show that during the whole mission, the optimized design shape increases the payload mass by 70.2 % based on the initial shape, and the performance is significantly improved, which verifies the effectiveness of the distributed-centralized augmented Lagrangian coordination multidisciplinary design optimization method proposed in this paper. Cross-domain vehicles combine the typical features of aviation and space vehicles, can fly remotely in the atmosphere and transatmosphere, and have the characteristics of a large airspace and wide velocity domain, which have shown great application value in both military and civil fields, and thus have received extensive attention from scholars at home and abroad [1,2]. Parallel solving of subproblems can effectively improve the solving efficiency.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：However, since the flight of this type of vehicle covers both aerospace and aviation domains, the mission and flight environment are complex, and its multidisciplinary design needs to comprehensively consider the flight environment of in-orbit operation and re-entry flight, and the configuration is more complex, which will directly affect the aerodynamic, structural and trajectory disciplines with high timeconsumption and high computational cost, making it more difficult and longer to solve the problem. The research findings provide new insights for multidisciplinary design optimization and offer important guidance for engineering practice applications.
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
- 作者声明或文本中可见 gap：However, since the flight of this type of vehicle covers both aerospace and aviation domains, the mission and flight environment are complex, and its multidisciplinary design needs to comprehensively consider the flight environment of in-orbit operation and re-entry flight, and the configuration is more complex, which will directly affect the aerodynamic, structural and trajectory disciplines with high timeconsumption and high computational cost, making it more difficult and longer to solve the problem. However, there is a strong nonlinear coupling between different disciplines of the cross-domain vehicle, and the traditional discipline decoupling design method makes it difficult to consider the synergistic effect generated by the mutual coupling between disciplines, which may lead to the loss of the overall optimal solution of the system, thus reducing the overall performance of the vehicle [4]. Among them, all three types of methods, CO, CSSO, and BLISS, decompose the original complex problems into two-level structural problems and then solve them, but their convergence has not yet been strictly theoretically supported; comparatively speaking, ATC methods have been widely used to deal with multilevel structural problems under strict mathematical convergence requirements [14].S.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- However, there is a strong nonlinear coupling between different disciplines of the cross-domain vehicle, and the traditional discipline decoupling design method makes it difficult to consider the synergistic effect generated by the mutual coupling between disciplines, which may lead to the loss of the overall optimal solution of the system, thus reducing the overall performance of the vehicle [4].

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：A nested multidisciplinary design optimization method based on augmented Lagrangian coordination and joint geometric/aerodynamic/structural disciplines modeling is proposed to address the problem of inefficient solving in high time-consuming disciplines such as aerodynamic, structural, and trajectory, brought by the complexity of the cross-domain vehicle configurations. Firstly, integrated geometric-aerodynamic-structural parametric modeling based on the 3D CST method is proposed to realize joint geometric/aerodynamic/structural modeling. Second, a distributed-centralized augmented Lagrangian coordination method that balances efficiency and parallel computation is proposed with an adaptive asynchronous multiplier update strategy to update the penalty weights.
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
| A nested multidisciplinary design optimization method based on augmented Lagrangian coordination and joint geometric/aerodynamic/structural disciplines modeling is proposed to address the problem of inefficient solving in high time-consuming disciplines such a | 摘要/引言/结论候选 | 图：Fig. 1. The cross-domain vehicle mission profile. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Firstly, integrated geometric-aerodynamic-structural parametric modeling based on the 3D CST method is proposed to realize joint geometric/aerodynamic/structural modeling. | 摘要/引言/结论候选 | 图：Fig. 2. Parameterized mesh for initial vehicle structure. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Second, a distributed-centralized augmented Lagrangian coordination method that balances efficiency and parallel computation is proposed with an adaptive asynchronous multiplier update strategy to update the penalty weights. | 摘要/引言/结论候选 | 图：Fig. 3. The design structure matrix of the cross-domain vehicle. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The optimization results show that during the whole mission, the optimized design shape increases the payload mass by 70.2 % based on the initial shape, and the performance is significantly improved, which verifies the effectiveness of the distributed-centrali | 摘要/引言/结论候选 | 表：Table 2 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Cross-domain vehicles combine the typical features of aviation and space vehicles, can fly remotely in the atmosphere and transatmosphere, and have the characteristics of a large airspace and wide velocity domain, which have shown great application value in bo | 摘要/引言/结论候选 | 表：Table 3 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Parallel solving of subproblems can effectively improve the solving efficiency. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (42.63, 669.07, 179.99, 690.38)]] * Corresponding author. E-mail addre | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. The cross-domain vehicle mission profile. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 2. Parameterized mesh for initial vehicle structure. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 3. The design structure matrix of the cross-domain vehicle. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 4. The distributed-centralized ALC method solution model. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 5. The distributed-centralized ALC method solving process. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 6. The decomposition structure of the mathematical example. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 7. Changes in the objective value and iteration count for different ALC methods when the consistency constraint convergence condition is taken as 1e-2,1e-3 | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. Variation of computational time for different ALC methods when the consistency constraint convergence condition is taken as 1e-2,1e-3,1e-4,1e-5. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 9. Consistency-constrained convergence case. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 10. The sensitivity analysis results for each parameter. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. The comprehensive sensitivity rankings for each CST parameter. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. MDO process based on the distributed-centralized ALC method. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 13. Optimization iteration history for the optimization objective. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 14. CAD changes before and after optimization. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 15. Stress and deformation distribution of optimized aircraft. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (42.63, 669.07, 179.99, 690.38)]] * Corresponding author. E-mail address: su@nwpu.edu.cn ( | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 359.77, 716.91)]] https://doi.org/10.1016/j.ast.2025.111499  | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.59, 57.98, 344.26, 76.81)]] S(ψ) = ∑ n | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (334.38, 75.61, 342.66, 84.08)]] i=0 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.6, 226.36, 366.84, 249.51)]] ⎩ ζnormal(η) = CM2 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (315.38, 239.68, 366.44, 253.59)]] ζspan(η) = \pmCT2 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (314.99, 311.86, 353.12, 324.89)]] X(ψ, η) = η | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (314.99, 330.39, 391.16, 345.65)]] Y(ψ, η) = CN2(η) N1(η)(ψ)CM2 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> A nested multidisciplinary design optimization method based on augmented Lagrangian coordination and joint geometric/aerodynamic/structural disciplines modeling is proposed to address the problem of inefficient solving in high time-consuming disciplines such as aerodynamic, structural, and trajectory, brought by the complexity of the cross-domain vehicle configurations. Firstly, integrated geometric-aerodynamic-structural parametric modeling based on the 3D CST method is proposed to realize joint geometric/aerodynamic/structural modeling. Second, a distributed-centralized augmented Lagrangian coordination method that balances efficiency and parallel computation is proposed with an adaptive asynchronous multiplier update strategy to update the penalty weights. Finally, the X37-like vehicle in the cross-domain vehicle is taken as an object, and its nested multi- disciplinary design optimization process is established to carry out the optimization design with the goal of optimal mass. The optimization results show that during the whole mission, the optimized design shape increases the payload mass by 70.2 % based on the initial shape, and the performance is significantly improved, which verifies the effectiveness of the distributed-centralized augmented Lagrangian coordination multidisciplinary design optimization method proposed in this paper.

### 7.4 摘要中文翻译

> 针对跨域车辆配置的复杂性带来的气动、结构、轨迹等高耗时学科求解效率低下的问题，提出一种基于增强拉格朗日协调和几何/气动/结构学科联合建模的嵌套多学科设计优化方法。首先，提出基于3D CST方法的集成几何-气动-结构参数化建模，实现几何/气动/结构联合建模。其次，提出了一种平衡效率和并行计算的分布式集中式增强拉格朗日协调方法，并采用自适应异步乘子更新策略来更新惩罚权重。最后以跨域车辆中的类X37车辆为对象，建立其嵌套的多学科设计优化流程，以最优质量为目标进行优化设计。优化结果表明，在整个任务过程中，优化后的设计形状在初始形状的基础上增加了有效载荷质量70.2%，性能显着提升，验证了本文提出的分布式集中式增强拉格朗日协调多学科设计优化方法的有效性。

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusion

> To address the low computational efficiency of solving complex cross-domain vehicle configurations due to high computational time consumption, this paper focuses on the discipline coupling characteristics of cross-domain vehicles. Based on the 3D CST method, it implements geometric/aerodynamic/structural co-simulation. A distributedcentralized ALC method is proposed with convergence analysis. Through mathematical formulation, we evaluate the computational efficiency, parallel scalability, and solution accuracy of distributed, distributed parallel, centralized, dominant, and distributed-centralized ALC methods. Results indicate that compared to dominant ALC and centralized ALC, the proposed distributed-centralized ALC method minimizes both coupled and decoupled variables while achieving the highest computational efficiency. Relative to distributed ALC and distributed parallel ALC, it yields the smallest solution errors and exhibits reduced susceptibility to local optima. Finally, the feasibility and effectiveness of the proposed method were further validated by solving a cross-domain aircraft multidisciplinary optimization problem. The research findings provide new insights for multidisciplinary design optimization and offer important guidance for engineering practice applications.

### 7.6 结论中文翻译

> 针对计算时间消耗大导致求解复杂跨域车辆配置计算效率低的问题，本文重点研究跨域车辆的学科耦合特性。基于3D CST方法，实现几何/气动/结构联合仿真。通过收敛分析，提出了一种分布式集中式ALC方法。通过数学公式，我们评估了分布式、分布式并行、集中式、主导式和分布式集中式 ALC 方法的计算效率、并行可扩展性和求解精度。结果表明，与主导 ALC 和集中式 ALC 相比，所提出的分布式集中式 ALC 方法最大限度地减少了耦合变量和解耦变量，同时实现了最高的计算效率。相对于分布式 ALC 和分布式并行 ALC，它产生最小的解误差，并且对局部最优的敏感性降低。最后，通过解决跨域飞机多学科优化问题，进一步验证了所提方法的可行性和有效性。研究成果为多学科设计优化提供了新见解，为工程实践应用提供了重要指导。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 7257 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2.1. Mission requirements | 对象/条件/子问题展开 | 903 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 2.2. Joint geometric/aerodynamic/structural modeling based on the 3D CST method | 方法建构 | 2034 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 2.2.1. Geometry | 对象/条件/子问题展开 | 3345 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 2.2.2. Aerodynamics | 对象/条件/子问题展开 | 2214 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 2.2.3. Structure | 对象/条件/子问题展开 | 1618 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 2.3.1. Trajectory | 对象/条件/子问题展开 | 1553 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 2.3.2. Thermal protection | 对象/条件/子问题展开 | 944 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 2.3.3. Mass | 对象/条件/子问题展开 | 498 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 2.4. Design structure matrix | 对象/条件/子问题展开 | 156 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 3. Distributed-centralized ALC method | 方法建构 | 6290 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 12 | 3.1. Distributed-centralized ALC model | 方法建构 | 4545 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 13 | 3.2. Distributed-centralized ALC method-solving strategy | 方法建构 | 5616 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 14 | 3.3. Convergence analysis | 结果验证/讨论 | 5508 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 15 | 3.4. Numerical case studies | 对象/条件/子问题展开 | 264 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 16 | 3.4.1. Definition of the problem | 对象/条件/子问题展开 | 5414 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 17 | 3.4.2. Problem-solving | 对象/条件/子问题展开 | 3414 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 18 | 3.4.3. Analysis of results | 结果验证/讨论 | 2054 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 19 | Table 6 | 对象/条件/子问题展开 | 1868 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 20 | 4. Multidisciplinary design optimization for the cross-domain vehicle | 对象/条件/子问题展开 | 298 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 21 | 4.1. Overview of the optimization problem | 对象/条件/子问题展开 | 570 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 22 | 4.2. Sensitivity analysis | 结果验证/讨论 | 629 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 23 | 4.3. Optimization methods and processes | 方法建构 | 143 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 24 | 4.4. Optimization results | 结果验证/讨论 | 2764 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 25 | 5. Conclusion | 主张回收/边界说明 | 1301 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 26 | Funding | 对象/条件/子问题展开 | 93 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 27 | Replication of results | 结果验证/讨论 | 203 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 28 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 371 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：mathbf(220)；alc(132)；mathrm(87)；problem(66)；big(64)；subproblems(62)；coupling(56)；distributed(56)；array(56)；master(44)；quad(43)；convergence(42)；parallel(41)；cdots(39)；optimization(38)；variables(36)；left(34)；right(34)；psi(31)；tag(29)
- 高频学术名词/术语：convergence(42)；optimization(38)；solution(26)；structure(18)；function(18)；iteration(16)；relationship(15)；coordination(11)；computation(10)；equation(9)；reference(9)；protection(8)；introduction(7)；decomposition(7)；condition(7)
- 高频学术动词：compared(11)；obtained(5)；obtain(4)；optimized(4)；introduced(3)；estimated(2)；validated(2)；indicate(2)；constructed(1)；revealed(1)；validate(1)；evaluate(1)
- 高频形容词：structural(20)；dominant(20)；objective(20)；aerodynamic(19)；computational(17)；local(17)；multidisciplinary(14)；optimal(14)；table(12)；traditional(9)；thermal(8)；geometric(8)；parametric(7)；original(6)；adaptive(6)
- 高频副词：respectively(7)；mainly(5)；directly(3)；early(3)；relatively(3)；usually(3)；widely(2)；significantly(2)；consecutively(2)；finally(2)；continuously(2)；slightly(2)
- 高频二词短语：mathbf mathbf(72)；master problem(29)；distributed-centralized alc(29)；quad quad(29)；begin array(28)；end array(28)；distributed alc(25)；overline mathbf(22)；big big(21)；distributed parallel(20)；centralized alc(18)；parallel alc(18)；dominant alc(18)；mathbf cdots(17)；mathbf big(17)
- 高频三词短语：quad quad quad(26)；mathbf mathbf mathbf(23)；distributed parallel alc(18)；left begin array(12)；end array right(12)；alc distributed parallel(12)；big big big(12)；big mathbf mathbf(11)；mathbf mathbf big(11)；array right tag(10)；mathbf cdots mathbf(10)；end array tag(10)
- 被动语态估计：97
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：233
- 一般过去时线索：380
- 现在完成时线索：1
- 情态动词线索：46

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：The research findings provide new insights for multidisciplinary design optimization and offer important guidance for engineering practice applications.
  - 可迁移句型：{object} research findings provide new insights for multidisciplinary design optimization and offer important guidance for engineering practice applications.
### gap/转折句
- 原句：However, since the flight of this type of vehicle covers both aerospace and aviation domains, the mission and flight environment are complex, and its multidisciplinary design needs to comprehensively consider the flight environment of in-orbit operation and re-entry flight, and the configuration is more complex, which will directly affect the aerodynamic, structural and trajectory disciplines with high timeconsumption and high computational cost, making it more difficult and longer to solve the problem.
  - 可迁移句型：{object}, since the flight of this type of vehicle covers both aerospace and aviation domains, the mission and flight environment are complex, and its multidisciplinary design needs to comprehensively consider the flight environment of in-orbit operation and r
- 原句：However, there is a strong nonlinear coupling between different disciplines of the cross-domain vehicle, and the traditional discipline decoupling design method makes it difficult to consider the synergistic effect generated by the mutual coupling between disciplines, which may lead to the loss of the overall optimal solution of the system, thus reducing the overall performance of the vehicle [4].
  - 可迁移句型：{object}, there is a strong nonlinear coupling between different disciplines of the cross-domain vehicle, and the traditional discipline decoupling design method makes it difficult to consider the synergistic effect generated by the mutual coupling between dis
- 原句：Tosserams [16–18] et a Traditional structural parametric modeling mainly relies on various CAD tools [22]; however, CAD-based parametric modeling is inefficient and costly, difficult to achieve changes in aerodynamic/structural topology and layout, and unsuitable for large-scale design space exploration.
  - 可迁移句型：{object} [16–18] et a Traditional structural parametric modeling mainly relies on various CAD tools [22]; however, CAD-based parametric modeling is inefficient and costly, difficult to achieve changes in aerodynamic/structural topology and layout, and unsuitab
- 原句：However, the geometric meaning of parameters in NURBS-based models remains ambiguous, hindering the derivation of universal principles.
  - 可迁移句型：{object}, the geometric meaning of parameters in NURBS-based models remains ambiguous, hindering the derivation of universal principles.
### 方法提出句
- 原句：A nested multidisciplinary design optimization method based on augmented Lagrangian coordination and joint geometric/aerodynamic/structural disciplines modeling is proposed to address the problem of inefficient solving in high time-consuming disciplines such as aerodynamic, structural, and trajectory, brought by the complexity of the cross-domain vehicle configurations.
  - 可迁移句型：{object} nested multidisciplinary design optimization method based on augmented Lagrangian coordination and joint geometric/aerodynamic/structural disciplines modeling is proposed to address the problem of inefficient solving in high time-consuming disciplines
- 原句：Firstly, integrated geometric-aerodynamic-structural parametric modeling based on the 3D CST method is proposed to realize joint geometric/aerodynamic/structural modeling.
  - 可迁移句型：{object}, integrated geometric-aerodynamic-structural parametric modeling based on the 3D CST method is proposed to realize joint geometric/aerodynamic/structural modeling.
- 原句：Second, a distributed-centralized augmented Lagrangian coordination method that balances efficiency and parallel computation is proposed with an adaptive asynchronous multiplier update strategy to update the penalty weights.
  - 可迁移句型：{object}, a distributed-centralized augmented Lagrangian coordination method that balances efficiency and parallel computation is proposed with an adaptive asynchronous multiplier update strategy to update the penalty weights.
- 原句：The optimization results show that during the whole mission, the optimized design shape increases the payload mass by 70.2 % based on the initial shape, and the performance is significantly improved, which verifies the effectiveness of the distributed-centralized augmented Lagrangian coordination multidisciplinary design optimization method proposed in this paper.
  - 可迁移句型：{object} optimization results show that during the whole mission, the optimized design shape increases the payload mass by 70.2 % based on the initial shape, and the performance is significantly improved, which verifies the effectiveness of the distributed-cen
### 结果证明句
- 原句：The optimization results show that during the whole mission, the optimized design shape increases the payload mass by 70.2 % based on the initial shape, and the performance is significantly improved, which verifies the effectiveness of the distributed-centralized augmented Lagrangian coordination multidisciplinary design optimization method proposed in this paper.
  - 可迁移句型：{object} optimization results show that during the whole mission, the optimized design shape increases the payload mass by 70.2 % based on the initial shape, and the performance is significantly improved, which verifies the effectiveness of the distributed-cen
- 原句：Cross-domain vehicles combine the typical features of aviation and space vehicles, can fly remotely in the atmosphere and transatmosphere, and have the characteristics of a large airspace and wide velocity domain, which have shown great application value in both military and civil fields, and thus have received extensive attention from scholars at home and abroad [1,2].
  - 可迁移句型：{object} vehicles combine the typical features of aviation and space vehicles, can fly remotely in the atmosphere and transatmosphere, and have the characteristics of a large airspace and wide velocity domain, which have shown great application value in both m
- 原句：Tosserams [16–18] et a Traditional structural parametric modeling mainly relies on various CAD tools [22]; however, CAD-based parametric modeling is inefficient and costly, difficult to achieve changes in aerodynamic/structural topology and layout, and unsuitable for large-scale design space exploration.
  - 可迁移句型：{object} [16–18] et a Traditional structural parametric modeling mainly relies on various CAD tools [22]; however, CAD-based parametric modeling is inefficient and costly, difficult to achieve changes in aerodynamic/structural topology and layout, and unsuitab
- 原句：In addition, in the outer loop, suppose x∗ is a KKT point of the problem (19), $\left\{\overline {{\mathbf {x}}} _ {k} ^ {*} \right\}$ is the local minimum of the relaxation problem (20) under fixed parameters $\mathbf {v} ^ {k}$ and $\mathbf {w} ^ {k}$ Considering only the consistency constraints, the augmented Lagrangian function of the distributed-centralized ALC model is shown in the following equation. $$f _ {A L} ( \overline {{\mathbf {x}}} , \mathbf {v} , \mathbf {w} ) = \sum _ {j = 1} ^ {M} f _ {j} \Big ( \mathbf {x} _ {j} , \mathbf {y} _ {j} \Big ) + \sum _ {j = 1} ^ {M} \mathbf {v} _ {j} ^ {\mathrm{T}} \mathbf {c} _ {j} \big ( \overline {{\mathbf {x}}} _ {j} \big ) + \sum _ {j = 1} ^ {M} \parallel \mathbf {w} _ {j} \circ \mathbf {c} _ {j} \left( \overline {{\mathbf {x}}} _ {j} \right) \parallel _ {2} ^ {2}$$ $$\begin{array} {r l} & {s . \mathrm{t} . {\overline {{\mathbf {x}}}} _ {j} = \left[ \mathbf {x} _ {j} , \mathbf {y} _ {j} \right]} \\ & {\mathbf {c} _ {j} \left( {\overline {{\mathbf {x}}}} _ {j} \right) = \mathbf {S} _ {j} \mathbf {y} ^ {k - 1} - \mathbf {y} _ {j} ^ {k}} \end{array}\tag{27}$$ where $\begin{array} {r l} {\overline {{\mathbf {x}}} =} & {{} [ \overline {{\mathbf {x}}} _ {1} , \quad \cdots , \quad \overline {{\mathbf {x}}} _ {M} ] , \quad \mathbf {v} = \quad [ \mathbf {v} _ {1} , \quad \cdots , \quad \mathbf {v} _ {M} ] , \mathbf {w} = \quad [ \mathbf {w} _ {1} , \quad \cdots , \quad} \end{array}$ $\mathbf w _ {M} ] , \mathbf c ( \overline {{\mathbf x}} ) = [ \mathbf c _ {1} ( \overline {{\mathbf x}} _ {1} ) , \cdots , \mathbf c _ {M To address the low computational efficiency of solving complex cross-domain vehicle configurations due to high computational time consumption, this paper focuses on the discipline coupling characteristics of cross-domain vehicles.
  - 可迁移句型：{object} addition, in the outer loop, suppose x∗ is a KKT point of the problem (19), $\left\{\overline {{\mathbf {x}}} _ {k} ^ {*} \right\}$ is the local minimum of the relaxation problem (20) under fixed parameters $\mathbf {v} ^ {k}$ and $\mathbf {w} ^ {k}$ 
### 贡献收束句
- 原句：The optimization results show that during the whole mission, the optimized design shape increases the payload mass by 70.2 % based on the initial shape, and the performance is significantly improved, which verifies the effectiveness of the distributed-centralized augmented Lagrangian coordination multidisciplinary design optimization method proposed in this paper.
  - 可迁移句型：{object} optimization results show that during the whole mission, the optimized design shape increases the payload mass by 70.2 % based on the initial shape, and the performance is significantly improved, which verifies the effectiveness of the distributed-cen
- 原句：Parallel solving of subproblems can effectively improve the solving efficiency.
  - 可迁移句型：{object} solving of subproblems can effectively improve the solving efficiency.
- 原句：Tosserams has put the Alternating Direction Method of Multipliers (ADMM) combined with Augmented Lagrangian (AL) coordination method and applied it to the solution process of the ATC method, which significantly reduces the solution cost of the ATC method [15], and based on this, he proposed the application of Augmented The Augmented Lagrangian Coordination (ALC) method for solving MDO problems with Lagrangian relaxation is proposed [16–18], which breaks the limitation that the problem must be decomposed according to the hierarchical structure in the ATC method, and can deal with both hierarchical and non-hierarchical problems, with better convergence and lower computational cost, and becomes the most efficient method for solving the problem.
  - 可迁移句型：{object} has put the Alternating Direction Method of Multipliers (ADMM) combined with Augmented Lagrangian (AL) coordination method and applied it to the solution process of the ATC method, which significantly reduces the solution cost of the ATC method [15], 
- 原句：The method avoids tedious work such as data conversion and transfer between different disciplines, and greatly improves the modeling and solving efficiency.
  - 可迁移句型：{object} method avoids tedious work such as data conversion and transfer between different disciplines, and greatly improves the modeling and solving efficiency.
### 边界/谨慎句
- 原句：However, there is a strong nonlinear coupling between different disciplines of the cross-domain vehicle, and the traditional discipline decoupling design method makes it difficult to consider the synergistic effect generated by the mutual coupling between disciplines, which may lead to the loss of the overall optimal solution of the system, thus reducing the overall performance of the vehicle [4].
  - 可迁移句型：{object}, there is a strong nonlinear coupling between different disciplines of the cross-domain vehicle, and the traditional discipline decoupling design method makes it difficult to consider the synergistic effect generated by the mutual coupling between dis
- 原句：The convergence of the updating strategy is analyzed at the level of both inner and outer loops: Firstly, in the inner loop, for the kth iteration, when the Lagrange multipliers and penalty weights are fixed with the coupling information, each subproblem is solved as a subsequence ${\bf o f} \{\overline {{\bf x}} ^ {k} \}$ , since its Lagrange multipliers $\mathbf {v} ^ {k}$ are fixed, and the penalty weights satisfy: $\mathbf {w} ^ {k} > \mathbf {0}$ According to Proposition 4.2.1 in reference [33], assume that f and h are continuous functions, that X is a closed set, and that the constraint set $\{x \in X | h ( x ) = 0 \}$ is nonempty.
  - 可迁移句型：{object} convergence of the updating strategy is analyzed at the level of both inner and outer loops: Firstly, in the inner loop, for the kth iteration, when the Lagrange multipliers and penalty weights are fixed with the coupling information, each subproblem 
- 原句：In addition, in the outer loop, suppose x∗ is a KKT point of the problem (19), $\left\{\overline {{\mathbf {x}}} _ {k} ^ {*} \right\}$ is the local minimum of the relaxation problem (20) under fixed parameters $\mathbf {v} ^ {k}$ and $\mathbf {w} ^ {k}$ Considering only the consistency constraints, the augmented Lagrangian function of the distributed-centralized ALC model is shown in the following equation. $$f _ {A L} ( \overline {{\mathbf {x}}} , \mathbf {v} , \mathbf {w} ) = \sum _ {j = 1} ^ {M} f _ {j} \Big ( \mathbf {x} _ {j} , \mathbf {y} _ {j} \Big ) + \sum _ {j = 1} ^ {M} \mathbf {v} _ {j} ^ {\mathrm{T}} \mathbf {c} _ {j} \big ( \overline {{\mathbf {x}}} _ {j} \big ) + \sum _ {j = 1} ^ {M} \parallel \mathbf {w} _ {j} \circ \mathbf {c} _ {j} \left( \overline {{\mathbf {x}}} _ {j} \right) \parallel _ {2} ^ {2}$$ $$\begin{array} {r l} & {s . \mathrm{t} . {\overline {{\mathbf {x}}}} _ {j} = \left[ \mathbf {x} _ {j} , \mathbf {y} _ {j} \right]} \\ & {\mathbf {c} _ {j} \left( {\overline {{\mathbf {x}}}} _ {j} \right) = \mathbf {S} _ {j} \mathbf {y} ^ {k - 1} - \mathbf {y} _ {j} ^ {k}} \end{array}\tag{27}$$ where $\begin{array} {r l} {\overline {{\mathbf {x}}} =} & {{} [ \overline {{\mathbf {x}}} _ {1} , \quad \cdots , \quad \overline {{\mathbf {x}}} _ {M} ] , \quad \mathbf {v} = \quad [ \mathbf {v} _ {1} , \quad \cdots , \quad \mathbf {v} _ {M} ] , \mathbf {w} = \quad [ \mathbf {w} _ {1} , \quad \cdots , \quad} \end{array}$ $\mathbf w _ {M} ] , \mathbf c ( \overline {{\mathbf x}} ) = [ \mathbf c _ {1} ( \overline {{\mathbf x}} _ {1} ) , \cdots , \mathbf c _ {M To address the low computational efficiency of solving complex cross-domain vehicle configurations due to high computational time consumption, this paper focuses on the discipline coupling characteristics of cross-domain vehicles.
  - 可迁移句型：{object} addition, in the outer loop, suppose x∗ is a KKT point of the problem (19), $\left\{\overline {{\mathbf {x}}} _ {k} ^ {*} \right\}$ is the local minimum of the relaxation problem (20) under fixed parameters $\mathbf {v} ^ {k}$ and $\mathbf {w} ^ {k}$ 

## 9. 引用风险层

- 正文引用簇估计：29
- 参考文献条数：38
- 可识别年份条目数：41
- 2021 年及以后参考文献数：6
- 2010 年以前经典文献数：16
- 高频来源粗略识别：Multidisciplinary Opt(7)；Integr. Manuf. Sys(2)；Technol(1)；Measure. Technol(1)；Spacecr. Rockets(1)；Electrotechnol(1)；Integr. Manuf.Sys(1)；Transp. Eng(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] R. Hu, J.H. Meng, et al., Integrated structure/mechanism design of cross-domain wing-body fusion variant vehicle, Unmanned Sys. Technol. 7 (2) (2024) 51–64.
- [2] C.J. Li, F.C. Liu, N. Liu, et al., Design of inertial guidance device and anti-shock measurement method for cross-domain vehicle, Electron. Measure. Technol. 47 (5) (2024) 167–172.
- [3] S.B. Luo, Integrated Design of Airframe-Engine For Hypersonic Vehicle, Science Press, Beijing, 2018.
- [4] X., Q. Chen, et al., Multidisciplinary Design Optimization Theory and Application of Hypersonic Vehicle, Science Press, Beijing, 2020.
- [5] R. Balling, M.R. Rawlings, Collaborative optimization with disciplinary conceptual design, Struct. Multidisciplinary Opt. 20 (3) (2000) 232–241.
- [6] L.L. Yang, W.L. Li, X.L. Kong, H. Xu, Mixed uncertainty robust Cooperative optimization design method, Comp Integr Manuf Sys. 27 (11) (2021) 3282–3290.
- [7] R.D. Braun, A.A. Moore, I.M. Kroo, Collaborative approach to launch vehicle design, J. Spacecr. Rockets 34 (4) (1997) 478–486.
- [8] C. Ye, S.H. Miao, C. Li, W.C. Yang, D.D. Sun, Co-optimization of transmission and distribution grids based on improved parallel subspace algorithm, J. Electrotechnol. 33 (23) (2018) 5509–5522.
- [9] J. Sobieszczanski-Sobieski, S. Kodiyalam, BLISS/S: a new method for two-level structural optimization, Struct. Multidisciplinary Opt. 21 (1) (2001) 1–13.
- [10] P. Jiang, L. Kuang, X.Y. Shao, M. Xiao, An approximate model-based Co- optimization approach for two-stage integrated systems, China Mech. Eng. 23 (4) (2012) 395–402.
- [11] H.M. Kim, N.F. Michelena, P.Y. Papalambros, T. Jiang, Target cascading in optimal system design, in: ASME 2000 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference 12, 2020.
- [12] J. Sun, T. Qu, D.X. Nie, M. Thürer, C.D. Li, G.Q. Huang, Dual-channel multilevel distribution network location-inventory problem, Comp. Integr. Manuf.Sys. 27 (11) (2021) 3305–3317.
- [13] X.L. He, J. Chen, S.J. E, D.Y. Tang, L.M. Zhang, Optimization design of suspension parameters of undervehicle equipment based on objective cascade analysis, J. Transp. Eng. 21 (6) (2021) 321–330.
- [14] N. Michelena, H. Park, P.Y. Papalambros, Convergence properties of analytical target cascading, AIAA J 41 (5) (2003) 897–905.
- [15] S. Tosserams, L.F.P. Etman, P.Y. Papalambros, J.E. Rooda, An augmented lagrangian relaxation for analytical target cascading using the alternating direction method of multipliers, Struct. Multidisciplinary Opt. 31 (3) (2006) 176–189.

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
