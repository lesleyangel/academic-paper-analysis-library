# 论文深度拆解：An efficient thermal optimization model with integrated force paths, fully-decomposed hierarchies and hybrid genetic operations for a flight wing

> 生成依据：`801/cleantext/022-An-efficient-thermal-optimization-model-with-integrated-fo_2025_Aerospace-Sc`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`022-An-efficient-thermal-optimization-model-with-integrated-fo_2025_Aerospace-Sc`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\An-efficient-thermal-optimization-model-with-integrated-fo_2025_Aerospace-Sc.pdf`
- 页数：16
- clean body 字符数：56494
- 摘要字符数：1720
- 参考文献条数：43
- 图题数：15
- 表题数：5
- 表格文件数：5
- 公式候选数：101
- 提取质量分：0.93
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "7 formula(s) need manual review."}]

## 1. 身份层

- 标题：An efficient thermal optimization model with integrated force paths, fully-decomposed hierarchies and hybrid genetic operations for a flight wing
- 年份：2025
- 期刊/来源：Aerospace Sc
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：方法/算法 + 数值验证型
- 研究对象：The surface thermal radiation can only dissipate part of the heat, and it is essential to manage the considerable heat that enters the airframe, especially the heat in high-temperature regions that needs to be transported to low-temperature regions within a very short time. Such large number of variables leads to long chromosome, great population size and high optimization cost; thus, certain population size reduction is essential for a feasible optimization model.
- 主要方法：In order to form a great optimization space, the variable is fully decomposed into six hierarchies of topology, angle, heat width, force width, width factor and height factor, and the two-, three- and five-hierarchy models are supplemented to verify its enhancing effect on the optimization perfor mance. Due to the intricate relevance among multiple hierarchies, a hybrid strategy based on the genetic al gorithm is developed instead of the conventional sequential strategy, in which a binary coding scheme is adopted to uniformly describe the discrete and continuous variables, and the selection, crossover and mutation of different hierarchies are operated simultaneously during the genetic optimi
- 主要证据：图表 20 个标题、公式 101 个候选、参考文献 43 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“The surface thermal radiation can only dissipate part of the heat, and it is essential to manage the considerable heat that enters the airframe, especially the heat in high-tempera”，可以通过“In order to form a great optimization space, the variable is fully decomposed into six hierarchies of topology, angle, heat width, force width, width factor and height factor, and the two-, three- and five-hierarchy mode”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：In the hidden layer, the radial basis function is used as the activation function of the neurons, and the widely used Gauss function is adopted as the kernel function as shown in Eq. The RBF neural network is employed to reduce the population size and the optimization cost. Some conclusions are obtained: (1) The fully-decomposed variable hierarchy results into great optimization performance.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：The surface thermal radiation can only dissipate part of the heat, and it is essential to manage the considerable heat that enters the airframe, especially the heat in high-temperature regions that needs to be transported to low-temperature regions within a very short time. Such large number of variables leads to long chromosome, great population size and high optimization cost; thus, certain population size reduction is essential for a feasible optimization model.
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
- 作者声明或文本中可见 gap：However, the inconsistent transfer paths and multi-hierarchy variables lead to a complex and time-consuming optimization problem. To address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by RBF neural network surrogate model. However, the high density and low service temperature of above metal-based composites lead to their limited application in flight vehicles.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- Such Ground path method is widely used in the optimization of beam- and truss-type force-bearing structures [39,40], while the application in heat path and heat-force integrated path is very limited.
- However, the mutual influence among different hierarchies of variables is not considered in such sequential optimization method, and the so-called hybrid optimization method is a more effective alternate [41,42].

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：In order to form a great optimization space, the variable is fully decomposed into six hierarchies of topology, angle, heat width, force width, width factor and height factor, and the two-, three- and five-hierarchy models are supplemented to verify its enhancing effect on the optimization perfor mance. Due to the intricate relevance among multiple hierarchies, a hybrid strategy based on the genetic al gorithm is developed instead of the conventional sequential strategy, in which a binary coding scheme is adopted to uniformly describe the discrete and continuous variables, and the selection, crossover and mutation of different hierarchies are operated simultaneously during the genetic optimization. To address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by RBF neural network surrogate model.
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
| Due to the intricate relevance among multiple hierarchies, a hybrid strategy based on the genetic al gorithm is developed instead of the conventional sequential strategy, in which a binary coding scheme is adopted to uniformly describe the discrete and continu | 摘要/引言/结论候选 | 图：Fig. 1. The heat-force integrated path. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The concept of heat pipe, proposed by Grover et al. [19] in 1963, is a heat transfer element with extremely high thermal conductivity, which realizes rapid heat transport through the phase change and flow of the cooling medium, and the equivalent thermal condu | 摘要/引言/结论候选 | 图：Fig. 2. The fully decomposed path variable hierarchies. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In the hidden layer, the radial basis function is used as the activation function of the neurons, and the widely used Gauss function is adopted as the kernel function as shown in Eq. | 摘要/引言/结论候选 | 图：Fig. 3. Genetic selection, crossover and mutation operators. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| (4). $$h _ {j} ( \pmb {x} ) = \exp \left( - \frac {\| \pmb {x} - \pmb {c} _ {j} \| ^ {2}} {2 \sigma _ {j} ^ {2}} \right)$$ $$\parallel \pmb {x} - \pmb {c} _ {j} \parallel ^ {2} = \sum _ {i = 1} ^ {n} \left( \pmb {x} _ {i} - \pmb {c} _ {j i} \right) ^ {2}$$ $$\ | 摘要/引言/结论候选 | 表：Table 1 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The RBFNN is used to pre-evaluate and screen the individuals, i.e., the individuals are firstly ordered by their fitness values that predicted by RBFNN model, a certain amount (assumed to be 50 % in this work) of individuals with low fitness values are then In | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The path variable is fully decomposed into six hierarchies of topology, angle, heat width, force width, width factor and height factor to form a great optimization space, and a hybrid strategy based on the genetic algorithm is proposed to consider the complex  | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (37.59, 223.4, 431.0, 254.08)]] Jian-Jun Gou a,*, Hao-Dong Niu a, Shu- | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. The heat-force integrated path. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 2. The fully decomposed path variable hierarchies. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 3. Genetic selection, crossover and mutation operators. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4. The multi-hierarchy optimization process. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 5. Ground path and mesh. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 6. Optimization process of different population strategies (force-only paths, mass problem). | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 7. Optimization process of different optimization models (force-only paths, mass problem). | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 8. Optimization process of the integrated path (mass problem). | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 9. The temperature, stress and displacement fields of the optimal individuals (integrated paths, mass problem). | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 10. The optimal values of each variable (integrated paths, mass problem). | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. Optimization process and deviations of different optimization models (force-only paths, aeroelastic problem). | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 12. Optimization process of the integrated path (aeroelastic problem). | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 13. The temperature, stress and displacement fields of the optimal individuals (integrated paths, aeroelastic problem). | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 14. The optimal values of each variable (integrated paths, aeroelastic problem). | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 15. The path maximum temperature along with the thermal insulation layer mass. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (37.59, 223.4, 431.0, 254.08)]] Jian-Jun Gou a,*, Hao-Dong Niu a, Shu-Zhen Jia b, Jia-Xin  | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 336.1, 690.38)]] * Corresponding authors. E-mail addresses:  | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 368.28, 716.91)]] https://doi.org/10.1016/j.ast.2025.109950  | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (307.95, 460.57, 560.01, 483.18)]] XWF = XWW/XW XHF = XHH/H (1) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 5, bbox (306.59, 620.33, 560.01, 644.24)]] F(Ni) = 2 -SP + 2(SP -1) Ni -1 N -1 (3) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 6, bbox (38.95, 646.97, 78.7, 660.06)]] hj(x) = exp | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 6, bbox (38.95, 670.72, 96.8, 689.54)]] ‖ x -cj ‖2 = ∑ n | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 6, bbox (86.91, 688.29, 95.19, 696.76)]] i=1 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> Editor: Mr Damiano Casalino
> Lightweighting of the thermal system is the key issue for high-speed vehicles, and the integrated optimization of heat-force transfer path is one of the most promising techniques. However, the inconsistent transfer paths and multi-hierarchy variables lead to a complex and time-consuming optimization problem. In this work, the inte grated path with I-type force path and rectangular heat transport path on both sides of the force web is pre- designed for a high-speed wing. In order to form a great optimization space, the variable is fully decomposed into six hierarchies of topology, angle, heat width, force width, width factor and height factor, and the two-, three- and five-hierarchy models are supplemented to verify its enhancing effect on the optimization perfor mance. Due to the intricate relevance among multiple hierarchies, a hybrid strategy based on the genetic al gorithm is developed instead of the conventional sequential strategy, in which a binary coding scheme is adopted to uniformly describe the discrete and continuous variables, and the selection, crossover and mutation of different hierarchies are operated simultaneously during the genetic optimization. To address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by RBF neural network surrogate model. Finally, the wing is optimized with objectives of the minimum mass and minimum aeroelastic influence quantity, and the model effectiveness is verified by the great objective reductions of 35.7 % and 19.3 %, respectively.

### 7.4 摘要中文翻译

> 编辑：Damiano Casalino 先生 热系统轻量化是高速车辆的关键问题，而热力传递路径的综合优化是最有前途的技术之一。然而，不一致的传输路径和多层次变量导致了复杂且耗时的优化问题。在这项工作中，为高速机翼预先设计了在力网两侧具有I型力路径和矩形热传输路径的集成路径。为了形成大的优化空间，将变量充分分解为拓扑、角度、热宽度、力宽度、宽度因子和高度因子六个层次，并补充二、三、五层次模型来验证其对优化性能的增强效果。由于多个层次之间错综复杂的相关性，提出了一种基于遗传算法的混合策略来代替传统的顺序策略，其中采用二进制编码方案来统一描述离散变量和连续变量，并在遗传优化过程中同时操作不同层次的选择、交叉和变异。针对多变量层次导致的种群规模过大和优化成本高等问题，基于RBF神经网络代理模型对个体的预评价和筛选，构建了一种有效损失有限的种群缩减方法。最后以最小质量和最小气动弹性影响量为目标对机翼进行了优化，分别达到了35.7%和19.3%的大幅目标降低，验证了模型的有效性。

### 7.5 结论完整摘录

识别到的结论位置：6. Conclusions

> In this work, a heat and force integrated path optimization model is developed for the radial-beam wing of a high-speed vehicle. The path variable is fully decomposed into six hierarchies of topology, angle, heat width, force width, width factor and height factor to form a great optimization space, and a hybrid strategy based on the genetic algorithm is proposed to consider the complex relevance and conduct the simultaneous optimization of multi-hierarchy variables. The RBF neural network is employed to reduce the population size and the optimization cost. The integrated heat-force system is then optimized with objectives of minimum mass and minimum aeroelastic influence quantity. Some conclusions are obtained:
> 
> (1) The fully-decomposed variable hierarchy results into great optimization performance. The mass reductions of five-hierarchy model compared with the two- and three-hierarchy ones are 31.6 % and 15.6 %, respectively; the aeroelastic influence quantity reductions of five-hierarchy model compared with the two- and three-hierarchy ones are 11.6 % and 6.1 %, respectively.
> 
> (2) The complex relevance among different hierarchies is effectively considered by the hybrid optimization strategy; the optimization cost with multiple-hierarchy variables is greatly reduced (50 %) with limited effectiveness compromise (0.2 %) by the developed population reduction method based on the RBF neural network.
> 
> (3) For the force-only path without consideration of aerodynamic heating effects, the path mass is 0.647 kg after the minimum mass optimization, and the relative mass reductions are 71.5 % and 68.4 % in comparsion with the Ground path and the 1st qualified path, respectively; the final aeroelastic influence quantity is 5.85 % after the minimum aeroelastic influence quantity optimization, and the relative quantity reduction is 37.6 % in comparsion with the 1st qualified path.
> 
> (4) For the heat-force integrated path, 9 paths with mass of 1.80 kg are reserved, and the relative mass reductions are 42.7 % and 35.7 % in comparsion with the Ground and the 1st qualified path, respectively, in the minimum mass optimization; the aeroelastic influence quantity is reduced by 19.3 % comparing with the 1st qualified path in the minimum aeroelastic influence quantity optimization.
> 
> (5) In comparison with the force-only path, a total mass reduction of 0.08 to1.54 kg in absolute terms and 4.1 % to 45.3 % in relative terms is obtained by the integrated heat-force path.

### 7.6 结论中文翻译

> 在这项工作中，为高速车辆的径向梁翼开发了热力集成路径优化模型。将路径变量充分分解为拓扑、角度、热宽度、力宽度、宽度因子和高度因子6个层次，形成巨大的优化空间，并提出基于遗传算法的混合策略考虑复杂的相关性，对多层次变量进行同时优化。采用RBF神经网络来减少种群规模和优化成本。然后以最小质量和最小气动弹性影响量为目标优化集成热力系统。得到了一些结论： (1)完全分解的变量层次结构带来了良好的优化性能。五层模型与两层、三层模型相比质量减少分别为31.6%和15.6%；五层模型气动弹性影响量较二层、三层模型分别减少了11.6%和6.1%。 (2)混合优化策略有效考虑了不同层次之间的复杂关联性；通过基于 RBF 神经网络开发的种群缩减方法，多层次变量的优化成本大大降低 (50%)，而有效性折衷有限 (0.2%)。
> 
> (3) 对于不考虑气动热效应的纯力路径，最小质量优化后的路径质量为0.647 kg，与地面路径和第一合格路径相比，相对质量减少分别为71.5%和68.4%；最小气动弹性影响量优化后最终气动弹性影响量为5.85%，相对第一条合格路径减少了37.6%。 (4) 对于热力积分路径，预留了9条质量为1.80 kg的路径，在最小质量优化中，与地面和第1条合格路径相比，相对质量减少分别为42.7%和35.7%；最小气动弹性影响量优化中气动弹性影响量较第1条合格路径减少了19.3%。 (5) 与仅力路径相比，通过积分热力路径获得的总质量绝对减少了 0.08 至 1.54 kg，相对减少了 4.1% 至 45.3%。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 7698 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. The integrated heat-force path and fully decomposed variable hierarchies | 对象/条件/子问题展开 | 6667 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 3.1. Unified chromosome encoding of discrete and continuous variables | 对象/条件/子问题展开 | 1517 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 3.2. Hybrid genetic operators of multi-hierarchy variables | 对象/条件/子问题展开 | 3751 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 3.3. The population size reduction method | 方法建构 | 2573 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 6 | 3.4. The optimization process | 对象/条件/子问题展开 | 2514 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 4.1.1. Ground path and mesh | 对象/条件/子问题展开 | 2500 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 4.1.2. Governing equations | 对象/条件/子问题展开 | 2980 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 4.1.3. Boundary conditions | 对象/条件/子问题展开 | 1083 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 4.2. Mathematical description of optimization model | 方法建构 | 4534 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 11 | 5.1.1. The force-only path optimization | 对象/条件/子问题展开 | 4929 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 5.1.2. The heat-force integrated path optimization | 对象/条件/子问题展开 | 4617 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 5.2.1. The force-only path optimization | 对象/条件/子问题展开 | 1668 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 5.2.2. The heat-force integrated path optimization | 对象/条件/子问题展开 | 3812 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 15 | 5.3. Effectiveness of integrated path optimization | 对象/条件/子问题展开 | 1576 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 16 | 6. Conclusions | 主张回收/边界说明 | 2486 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 17 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 474 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：path(150)；optimization(105)；heat(74)；respectively(62)；width(61)；fig(52)；generation(51)；force(42)；mass(42)；variables(42)；paths(39)；population(39)；thermal(36)；partial(36)；integrated(34)；factor(34)；mathrm(33)；variable(32)；individuals(31)；reduction(31)
- 高频学术名词/术语：optimization(105)；generation(51)；population(39)；reduction(31)；temperature(30)；influence(20)；quantity(19)；insulation(16)；fitness(13)；function(11)；pressure(10)；displacement(10)；increment(9)；conductivity(8)；presence(8)
- 高频学术动词：obtained(16)；reveal(11)；indicate(9)；optimized(6)；indicated(6)；compared(5)；obtain(4)；developed(4)；constructed(3)；optimize(2)；predicted(2)；evaluated(1)；evaluate(1)；presented(1)
- 高频形容词：thermal(36)；partial(36)；variable(32)；individual(22)；aerodynamic(21)；aeroelastic(18)；optimal(14)；genetic(14)；reveal(11)；displacement(10)；total(9)；original(9)；increment(9)；continuous(8)；final(8)
- 高频副词：respectively(62)；force-only(15)；especially(8)；finally(7)；widely(5)；fully(5)；simultaneously(4)；usually(3)；uniformly(3)；effectively(3)；separately(2)；closely(2)
- 高频二词短语：integrated path(23)；frac partial(18)；width factor(17)；height factor(17)；aeroelastic influence(17)；generation increases(17)；influence quantity(16)；insulation layer(16)；force width(15)；path optimization(14)；heat width(14)；factor height(13)；width heat(13)；force-only path(13)；mathrm max(13)
- 高频三词短语：aeroelastic influence quantity(16)；width factor height(13)；factor height factor(13)；width width factor(12)；mathbf cdot mathbf(11)；angle force width(11)；force width heat(11)；width heat width(11)；partial frac partial(11)；thermal insulation layer(10)；heat width width(10)；frac partial partial(9)
- 被动语态估计：168
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：339
- 一般过去时线索：409
- 现在完成时线索：0
- 情态动词线索：54

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：The surface thermal radiation can only dissipate part of the heat, and it is essential to manage the considerable heat that enters the airframe, especially the heat in high-temperature regions that needs to be transported to low-temperature regions within a very short time.
  - 可迁移句型：{object} surface thermal radiation can only dissipate part of the heat, and it is essential to manage the considerable heat that enters the airframe, especially the heat in high-temperature regions that needs to be transported to low-temperature regions within
- 原句：Such large number of variables leads to long chromosome, great population size and high optimization cost; thus, certain population size reduction is essential for a feasible optimization model.
  - 可迁移句型：{object} large number of variables leads to long chromosome, great population size and high optimization cost; thus, certain population size reduction is essential for a feasible optimization model.
- 原句：The final output approximate function can be described as: $$\begin{array} {l} {{\displaystyle y _ {k} ( {\pmb x} ) = \sum _ {j = 1} ^ {J} w _ {j k} h _ {j} ( {\pmb x} )}} \\ {{\displaystyle j = 1 , ~ 2 , J}} \\ {{\displaystyle k = 1 , ~ 2 , K}} \end{array}\tag{5}$$ where J and K are the neuron number of hidden and output layers, respectively; wjk is the connection weight from the jth neuron of hidden layer to the kth neuron of output layer.
  - 可迁移句型：{object} final output approximate function can be described as: $$\begin{array} {l} {{\displaystyle y _ {k} ( {\pmb x} ) = \sum _ {j = 1} ^ {J} w _ {j k} h _ {j} ( {\pmb x} )}} \\ {{\displaystyle j = 1 , ~ 2 , J}} \\ {{\displaystyle k = 1 , ~ 2 , K}} \end{arra
### gap/转折句
- 原句：However, the inconsistent transfer paths and multi-hierarchy variables lead to a complex and time-consuming optimization problem.
  - 可迁移句型：{object}, the inconsistent transfer paths and multi-hierarchy variables lead to a complex and time-consuming optimization problem.
- 原句：To address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by RBF neural network surrogate model.
  - 可迁移句型：{object} address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by R
- 原句：However, the high density and low service temperature of above metal-based composites lead to their limited application in flight vehicles.
  - 可迁移句型：{object}, the high density and low service temperature of above metal-based composites lead to their limited application in flight vehicles.
- 原句：(2) The complex relevance among different hierarchies is effectively considered by the hybrid optimization strategy; the optimization cost with multiple-hierarchy variables is greatly reduced (50 %) with limited effectiveness compromise (0.2 %) by the developed population reduction method based on the RBF neural network.
  - 可迁移句型：(2) {object} complex relevance among different hierarchies is effectively considered by the hybrid optimization strategy; the optimization cost with multiple-hierarchy variables is greatly reduced (50 %) with limited effectiveness compromise (0.2 %) by the dev
### 方法提出句
- 原句：In order to form a great optimization space, the variable is fully decomposed into six hierarchies of topology, angle, heat width, force width, width factor and height factor, and the two-, three- and five-hierarchy models are supplemented to verify its enhancing effect on the optimization perfor mance.
  - 可迁移句型：{object} order to form a great optimization space, the variable is fully decomposed into six hierarchies of topology, angle, heat width, force width, width factor and height factor, and the two-, three- and five-hierarchy models are supplemented to verify its 
- 原句：Due to the intricate relevance among multiple hierarchies, a hybrid strategy based on the genetic al gorithm is developed instead of the conventional sequential strategy, in which a binary coding scheme is adopted to uniformly describe the discrete and continuous variables, and the selection, crossover and mutation of different hierarchies are operated simultaneously during the genetic optimization.
  - 可迁移句型：{object} to the intricate relevance among multiple hierarchies, a hybrid strategy based on the genetic al gorithm is developed instead of the conventional sequential strategy, in which a binary coding scheme is adopted to uniformly describe the discrete and co
- 原句：To address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by RBF neural network surrogate model.
  - 可迁移句型：{object} address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by R
- 原句：Finally, the wing is optimized with objectives of the minimum mass and minimum aeroelastic influence quantity, and the model effectiveness is verified by the great objective reductions of 35.7 % and 19.3 %, respectively.
  - 可迁移句型：{object}, the wing is optimized with objectives of the minimum mass and minimum aeroelastic influence quantity, and the model effectiveness is verified by the great objective reductions of 35.7 % and 19.3 %, respectively.
### 结果证明句
- 原句：In the hidden layer, the radial basis function is used as the activation function of the neurons, and the widely used Gauss function is adopted as the kernel function as shown in Eq.
  - 可迁移句型：{object} the hidden layer, the radial basis function is used as the activation function of the neurons, and the widely used Gauss function is adopted as the kernel function as shown in Eq.
- 原句：(4). $$h _ {j} ( \pmb {x} ) = \exp \left( - \frac {\| \pmb {x} - \pmb {c} _ {j} \| ^ {2}} {2 \sigma _ {j} ^ {2}} \right)$$ $$\parallel \pmb {x} - \pmb {c} _ {j} \parallel ^ {2} = \sum _ {i = 1} ^ {n} \left( \pmb {x} _ {i} - \pmb {c} _ {j i} \right) ^ {2}$$ $$\pmb {c} _ {j} = \left[ c _ {j 1} , c _ {j 2} , . . . , c _ {j n} \right] ^ {\mathrm{T}}\tag{4}$$ where x is the input vector, subscript j indicates the jth neuron of hidden layer, hj(x) is the jth radial basis function, and cj and σj are the center and width of the radial basis, respectively.
  - 可迁移句型：(4). $$h _ {j} ( \pmb {x} ) = \exp \left( - \frac {\| \pmb {x} - \pmb {c} _ {j} \| ^ {2}} {2 \sigma _ {j} ^ {2}} \right)$$ $$\parallel \pmb {x} - \pmb {c} _ {j} \parallel ^ {2} = \sum _ {i = 1} ^ {n} \left( \pmb {x} _ {i} - \pmb {c} _ {j i} \right) ^ {2}$$ $$\
- 原句：Some conclusions are obtained: (1) The fully-decomposed variable hierarchy results into great optimization performance.
  - 可迁移句型：{object} conclusions are obtained: (1) The fully-decomposed variable hierarchy results into great optimization performance.
### 贡献收束句
- 原句：The RBF neural network is employed to reduce the population size and the optimization cost.
  - 可迁移句型：{object} RBF neural network is employed to reduce the population size and the optimization cost.
- 原句：(2) The complex relevance among different hierarchies is effectively considered by the hybrid optimization strategy; the optimization cost with multiple-hierarchy variables is greatly reduced (50 %) with limited effectiveness compromise (0.2 %) by the developed population reduction method based on the RBF neural network.
  - 可迁移句型：(2) {object} complex relevance among different hierarchies is effectively considered by the hybrid optimization strategy; the optimization cost with multiple-hierarchy variables is greatly reduced (50 %) with limited effectiveness compromise (0.2 %) by the dev
- 原句：(4) For the heat-force integrated path, 9 paths with mass of 1.80 kg are reserved, and the relative mass reductions are 42.7 % and 35.7 % in comparsion with the Ground and the 1st qualified path, respectively, in the minimum mass optimization; the aeroelastic influence quantity is reduced by 19.3 % comparing with the 1st qualified path in the minimum aeroelastic influence quantity optimization.
  - 可迁移句型：(4) {object} the heat-force integrated path, 9 paths with mass of 1.80 kg are reserved, and the relative mass reductions are 42.7 % and 35.7 % in comparsion with the Ground and the 1st qualified path, respectively, in the minimum mass optimization; the aeroela
### 边界/谨慎句
- 原句：To address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by RBF neural network surrogate model.
  - 可迁移句型：{object} address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by R
- 原句：The surface thermal radiation can only dissipate part of the heat, and it is essential to manage the considerable heat that enters the airframe, especially the heat in high-temperature regions that needs to be transported to low-temperature regions within a very short time.
  - 可迁移句型：{object} surface thermal radiation can only dissipate part of the heat, and it is essential to manage the considerable heat that enters the airframe, especially the heat in high-temperature regions that needs to be transported to low-temperature regions within
- 原句：However, the high density and low service temperature of above metal-based composites lead to their limited application in flight vehicles.
  - 可迁移句型：{object}, the high density and low service temperature of above metal-based composites lead to their limited application in flight vehicles.
- 原句：The RBFNN is used to pre-evaluate and screen the individuals, i.e., the individuals are firstly ordered by their fitness values that predicted by RBFNN model, a certain amount (assumed to be 50 % in this work) of individuals with low fitness values are then In this work, a heat and force integrated path optimization model is developed for the radial-beam wing of a high-speed vehicle.
  - 可迁移句型：{object} RBFNN is used to pre-evaluate and screen the individuals, i.e., the individuals are firstly ordered by their fitness values that predicted by RBFNN model, a certain amount (assumed to be 50 % in This study) of individuals with low fitness values are t

## 9. 引用风险层

- 正文引用簇估计：18
- 参考文献条数：43
- 可识别年份条目数：44
- 2021 年及以后参考文献数：14
- 2010 年以前经典文献数：12
- 高频来源粗略识别：N. Y(3)；Sci. Technol(3)；Spacecr. Rockets(3)；J. Aeronaut(2)；Relat. Mater(2)；Therm. Eng(2)；Alloys Compd(1)；Mater(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] J. Liu, X. Zhou, H. xin, High-Si reinforced Al matrix composites prepared by powder semi-solid squeeze, J. Alloys Compd. 726 (2017) 772–778.
- [2] J. Xie, J. Ma, M. Liao, W. Guo, L. Huang, P. Gao, H. Xiao, Reinforcement of thermally-conductive SiC/Al composite with 3D-interpenetrated network structure by various SiC foam ceramic skeletons, Ceram. Int. 47 (2021) 30869–30879.
- [3] Z. Zhang, Z. Wei, Z. Li, B. Hou, R. Xue, H. Xia, Z. Shi, SiC honeycomb reinforced Al matrix composite with improved tribological performance, Ceram. Int. 47 (2021) 23376–23385.
- [4] C. Yan, W. Lifeng, R. Jianyue, Multi-functional SiC/Al composites for aerospace applications, Chin. J. Aeronaut. 21 (2008) 578–584.
- [5] Z. Shen, G. Ji, J.-F. Silvain, From 1D to 2D arrangements of graphite flakes in an aluminium matrix composite: impact on thermal properties, Scr. Mater. 183 (2020) 86–90.
- [6] C. Zhang, R. Wang, Z. Cai, C. Peng, Y. Feng, L. Zhang, Effects of dual-layer coatings on microstructure and thermal conductivity of diamond/Cu composites prepared by vacuum hot pressing, Surf. Coat. Technol. 277 (2015) 299–307.
- [7] E.A. Ekimov, N.V. Suetin, A.F. Popovich, V.G. Ralchenko, Thermal conductivity of diamond composites sintered under high pressures, Diam. Relat. Mater. 17 (2008) 838–843.
- [8] Q. Cui, C. Chen, C. Yu, T. Lu, H. Long, S. Yan, A.A. Volinsky, J. Hao, Effect of molybdenum particles on thermal and mechanical properties of graphite flake/ copper composites, Carbon. N. Y. 161 (2020) 169–180.
- [9] B. Liu, D.Q. Zhang, X.F. Li, X.H. Guo, J. Shi, Z.J. Liu, Q.G. Guo, The microstructures and properties of graphite flake/copper composites with high volume fractions of graphite flake, New Carbon Mater. 35 (2020) 58–65.
- [10] T. Schwanekamp, System studies on active thermal protection of a hypersonic suborbital passenger transport vehicle, in: Proceedings of the 19th AIAA International Space Planes and Hypersonic Systems and Technologies Conference, Atlanta, GA, 2014. June 16-20.
- [11] X.-S. Liu, Q.-G. Fu, H. Wang, Q. Song, Microstructure, thermophysical property and ablation behavior of high thermal conductivity carbon/carbon composites after heat-treatment, Chin. J. Aeronaut. 33 (2020) 1541–1548.
- [12] X. Zhang, X. Li, G. Yuan, Z. Dong, G. Ma, B. Rand, Large diameter pitch-based graphite fiber reinforced unidirectional carbon/carbon composites with high thermal conductivity densified by chemical vapor infiltration, Carbon. N. Y. 114 (2017) 59–69.
- [13] G. Yuan, X. Li, Z. Dong, X. Xiong, B. Rand, Z. Cui, Y. Cong, J. Zhang, Y. Li, Z. Zhang, J. Wang, Pitch-based ribbon-shaped carbon-fiber-reinforced one-dimensional carbon/carbon composites with ultrahigh thermal conductivity, Carbon. N. Y. 68 (2014) 413–425.
- [14] Z.H. Feng, Z. Fan, Q. Kong, X. Xiong, B.Y. Huang, Effect of high temperature treatment on the structure and thermal conductivity of 2D carbon/carbon composites with a high thermal conductivity, New Carbon Mater. 29 (2014) 357–362.
- [15] D. Huang, R. Tan, L. Liu, C. Ye, S. Zhu, Z. Fan, P. Zhang, H. Wu, F. Han, H. Liu, J. Liu, Preparation and properties of the three-dimensional highly thermal conductive carbon/carbon-silicon carbide composite using the mesophase-pitch- based carbon fibers and pyrocarbon as thermal diffusion channels, J. Eur. Ceram. Soc. 41 (2021) 4438–4446.

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
