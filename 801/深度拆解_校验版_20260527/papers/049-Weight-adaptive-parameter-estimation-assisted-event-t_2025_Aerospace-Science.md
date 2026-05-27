# 论文深度拆解：Weight-adaptive parameter estimation assisted event-triggered model predictive guidance for reentry

> 生成依据：`801/cleantext/049-Weight-adaptive-parameter-estimation-assisted-event-t_2025_Aerospace-Science`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`049-Weight-adaptive-parameter-estimation-assisted-event-t_2025_Aerospace-Science`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\Weight-adaptive-parameter-estimation-assisted-event-t_2025_Aerospace-Science.pdf`
- 页数：13
- clean body 字符数：56966
- 摘要字符数：1356
- 参考文献条数：79
- 图题数：27
- 表题数：6
- 表格文件数：6
- 公式候选数：238
- 提取质量分：0.96
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "35 formula(s) need manual review."}]

## 1. 身份层

- 标题：Weight-adaptive parameter estimation assisted event-triggered model predictive guidance for reentry
- 年份：2025
- 期刊/来源：Aerospace Science
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：方法/算法 + 数值验证型
- 研究对象：Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints. However, both strategies have limitations: the former requires substantial computing resources and demands constant high sensitivity from the entire navigation, guidance, and control system, while the latter is constrained by confl icting relationships between guidance cycle duration, TO efficiency, and guidance accuracy. In addition, it is important to comprehen
- 主要方法：Communicated by Xingqun Zhan This paper proposes an event-triggered model predictive guidance (ET-NM PG) method assisted by weight adaptive parameter estimation (WAPE) and applies it to reentry guidance. Guidance methods based on online trajectory optimization (TO) often face a trade-off between guidance accuracy and the efficiency of guidance command computation when dealing with complex problems. However, the actual model parameter values often deviate from the reference values, leading to an excessively high event trigger frequency and potentially rendering the trajectory optimization unfeasible.
- 主要证据：图表 33 个标题、公式 238 个候选、参考文献 79 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints. However, both strategies have limitations: th”，可以通过“Communicated by Xingqun Zhan This paper proposes an event-triggered model predictive guidance (ET-NM PG) method assisted by weight adaptive parameter estimation (WAPE) and applies it to reentry guidance. Guidance methods”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：By using state deviation exceeding a threshold as an event-triggering condition, it is possible to effectively reduce computational resource consumption while ensuring a certain level of guidance accuracy. The numerical simulation results cofirm the effectiveness of the proposed method. This results in a wide range of state dispersion during and at the end of the reentry fl ight, which is not conducive to safe landing and reuse of the vehicle.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints. However, both strategies have limitations: the former requires substantial computing resources and demands constant high sensitivity from the entire navigation, guidance, and control system, while the latter is constrained by confl icting relationships between guidance cycle duration, TO efficiency, and guidance accuracy. In addition, it is important to comprehensively consider the sources and magnitudes of uncertainties based on the actual situation.
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
- 作者声明或文本中可见 gap：However, the actual model parameter values often deviate from the reference values, leading to an excessively high event trigger frequency and potentially rendering the trajectory optimization unfeasible. Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints. However, people believe that as technology continues to advance, winged vehicles will eventually regain their relevance in space transportation [2].
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- However, people believe that as technology continues to advance, winged vehicles will eventually regain their relevance in space transportation [2].
- However, most model identifi cation is carried out offline for modeling purposes and cannot be directly used for real-time guidance [34].

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：Communicated by Xingqun Zhan This paper proposes an event-triggered model predictive guidance (ET-NM PG) method assisted by weight adaptive parameter estimation (WAPE) and applies it to reentry guidance. Guidance methods based on online trajectory optimization (TO) often face a trade-off between guidance accuracy and the efficiency of guidance command computation when dealing with complex problems. However, the actual model parameter values often deviate from the reference values, leading to an excessively high event trigger frequency and potentially rendering the trajectory optimization unfeasible.
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
| Communicated by Xingqun Zhan This paper proposes an event-triggered model predictive guidance (ET-NM PG) method assisted by weight adaptive parameter estimation (WAPE) and applies it to reentry guidance. | 摘要/引言/结论候选 | 图：Fig. 1. Coordinate system and states notations. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| To address this issue, we propose updating the model parameters online using WAPE within the general ET-NMPG framework, thereby enhancing guidance accuracy and reducing guidance frequency. | 摘要/引言/结论候选 | 图：Fig. 2. 𝐶𝐷contour and a 𝑣−𝛼curve. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The numerical simulation results cofirm the effectiveness of the proposed method. | 摘要/引言/结论候选 | 图：Fig. 3. Relationship between 𝑚Δ𝑡∕𝑇𝑟𝑒𝑓and [𝜌𝑙𝑠𝑞,𝑊𝑑𝑎𝑡𝑎]. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| This results in a wide range of state dispersion during and at the end of the reentry fl ight, which is not conducive to safe landing and reuse of the vehicle. | 摘要/引言/结论候选 | 表：Table 1 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| With the rapid development of embedded computing capabilities, computational guidance and control (CG&C) technology based on complex online computing is gradually replacing traditional guidance methods [7]. | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Since various pseudospectral methods [14] have begun to demonstrate excellent performance in solving trajectory optimization problems (TOP), many researchers have been trying to apply them to actual fl ight control [15-- 17] rather than simply using them as an | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.64, 697.18, 359.67, 714.46)]] https://doi.org/10.101 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Coordinate system and states notations. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 2. 𝐶𝐷contour and a 𝑣−𝛼curve. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 3. Relationship between 𝑚Δ𝑡∕𝑇𝑟𝑒𝑓and [𝜌𝑙𝑠𝑞,𝑊𝑑𝑎𝑡𝑎]. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4. Comparison diagram of different NMPG strategies. (For interpretation of the colors in the figure(s), the reader is referred to the web version of this a | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 7. 𝑣−𝐻curves of FC-NMPG and ET-NMPG. 𝐻𝑟 min and 𝐻𝑜 min represent the altitude lower bound corresponding to the initial and relaxed dynamic pressure and hea | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 5. 𝑣−𝐻curves of FLG and NMPGs. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 8. 𝑣−𝐻curves of ET-NMPG and WAPE-assisted ET-NMPG. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 6. Ground tracks of FLG and NMPGs. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 9. Ground tracks of ET-NMPG and WAPE-assisted ET-NMPG. Fig. 10. Guidance commands of ET-NMPG and WAPE-assisted ET-NMPG. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. Parameter estimation results. Aerodynamic coefficients have been converted to correspond to the true mass as described in Section 4.2. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. Terminal position errors. If the terminal position error exceeds 5 km, the guidance is considered to have failed, and only successful guidance results  | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 13. The relationship between estimation error of parameters and the PE times. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 14. Scatter plot of parameter estimation error with different time. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 15. 𝑣−𝐻curves with in-flight faults. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 16. Guidance commands with in-flight faults. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.64, 697.18, 359.67, 714.46)]] https://doi.org/10.1016/j.ast.2025.109938  | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (320.4, 489.24, 358.69, 509.03)]] d𝑟 d𝑡 = 𝑣sin𝛾 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (320.33, 509.98, 379.74, 530.5)]] d𝑡 = 𝑣cos𝛾sin𝜓 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (319.81, 532.91, 381.14, 553.42)]] d𝑡 = 𝑣cos𝛾cos𝜓 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (320.39, 554.37, 356.74, 574.17)]] d𝑡 = -𝐷 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (320.39, 577.41, 363.91, 597.21)]] d𝑡 = 𝐿cos𝜎 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (319.36, 616.81, 364.51, 636.61)]] d𝑡 = 𝐿sin𝜎 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (340.22, 599.32, 545.09, 611.19)]] + 2𝜔𝑣cos𝜙sin𝜓+ 𝑟𝜔2 cos𝜙(cos𝛾cos𝜙+ sin𝛾sin𝜙cos𝜓) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> Communicated by Xingqun Zhan
> This paper proposes an event-triggered model predictive guidance (ET-NM PG) method assisted by weight adaptive parameter estimation (WAPE) and applies it to reentry guidance. Guidance methods based on online trajectory optimization (TO) often face a trade-off between guidance accuracy and the efficiency of guidance command computation when dealing with complex problems. By using state deviation exceeding a threshold as an event-triggering condition, it is possible to effectively reduce computational resource consumption while ensuring a certain level of guidance accuracy. However, the actual model parameter values often deviate from the reference values, leading to an excessively high event trigger frequency and potentially rendering the trajectory optimization unfeasible. To address this issue, we propose updating the model parameters online using WAPE within the general ET-NMPG framework, thereby enhancing guidance accuracy and reducing guidance frequency. Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints. Additionally, we designed a change point detection step to avoid data contamination in the case of i-flight faults (parameter mutations). The numerical simulation results cofirm the effectiveness of the proposed method.

### 7.4 摘要中文翻译

> 詹兴群通讯 本文提出了一种权重自适应参数估计（WAPE）辅助的事件触发模型预测制导（ET-NM PG）方法，并将其应用于再入制导。基于在线轨迹优化（TO）的制导方法在处理复杂问题时常常面临制导精度和制导命令计算效率之间的权衡。通过将状态偏差超过阈值作为事件触发条件，可以在保证一定的制导精度的同时，有效减少计算资源消耗。然而，实际模型参数值经常偏离参考值，导致事件触发频率过高，并可能导致轨迹优化不可行。为了解决这个问题，我们建议在通用 ET-NMPG 框架内使用 WAPE 在线更新模型参数，从而提高制导精度并降低制导频率。重要的是，对于再入过程，这种方法可以进一步确保飞行状态保持在可接受的路径限制内。此外，我们设计了一个变化点检测步骤，以避免 i-flight 故障（参数突变）情况下的数据污染。数值模拟结果验证了该方法的有效性。

### 7.5 结论完整摘录

识别到的结论位置：7. Conclusions

> This paper proposes a WAPE-assisted ET-NMPG method for reentry guidance. Unlike most guidance methods based on online optimization (i.e., NMPG) that use time-triggered strategies, the ET-NMPG with an event-triggered mechanism achieves a better balance between guidance accuracy and computational resource consumption. Building on this, we incorporated a parameter estimation step into the ET-NMPG process to improve model prediction accuracy, thereby further reducing the number of guidance cycles, enhancing guidance precision, and ensuring flight safety. Simulation results demonstrate that WAPE-assisted ET-NMPG offers greater application potential compared to existing methods such as UI-NMPG, FC-NMPG, and ET-NMPG. Further research is warranted to address various sources of deviation in actual fl ight processes and to enhance online parameter estimation using more comprehensive sensor data. In addition, it is important to comprehensively consider the sources and magnitudes of uncertainties based on the actual situation. On this basis, the method for selecting the event-triggered threshold and the potential need for introducing robust NMPG should be explored in more detail.

### 7.6 结论中文翻译

> 本文提出了一种WAPE辅助的ET-NMPG再入引导方法。与大多数使用时间触发策略的基于在线优化的制导方法（即NMPG）不同，具有事件触发机制的ET-NMPG在制导精度和计算资源消耗之间实现了更好的平衡。在此基础上，我们在ET-NMPG过程中加入了参数估计步骤，以提高模型预测精度，从而进一步减少制导周期数，提高制导精度，保证飞行安全。仿真结果表明，与 UI-NMPG、FC-NMPG 和 ET-NMPG 等现有方法相比，WAPE 辅助的 ET-NMPG 具有更大的应用潜力。需要进一步的研究来解决实际飞行过程中的各种偏差来源，并使用更全面的传感器数据来增强在线参数估计。此外，还要根据实际情况综合考虑不确定性的来源和大小。在此基础上，应更详细地探讨选择事件触发阈值的方法以及引入鲁棒NMPG的潜在需求。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 8656 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. Problem formulation | 方法建构 | 340 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 3 | 2.1. Standard motion equations | 对象/条件/子问题展开 | 1926 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 2.2. Deviations and disturbances | 对象/条件/子问题展开 | 1991 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 2.3. Reentry guidance problem | 对象/条件/子问题展开 | 1922 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 3. The ET-NMPG method | 方法建构 | 406 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 7 | 3.1. Definition of TOP | 对象/条件/子问题展开 | 3824 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 3.2. Process of ET-NMPG | 对象/条件/子问题展开 | 1080 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 3.3.1. Mesh refi nement or not | 对象/条件/子问题展开 | 1443 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 3.3.2. Mesh scheme and initial value | 对象/条件/子问题展开 | 1206 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 3.3.3. State prediction before NMPG | 对象/条件/子问题展开 | 2366 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 4. WAPE and change point detection | 对象/条件/子问题展开 | 436 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 4.1. PE for atmosphere | 对象/条件/子问题展开 | 1161 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 4.2. PE for aerodynamics | 对象/条件/子问题展开 | 10149 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 15 | 4.3. Change point detection | 对象/条件/子问题展开 | 2002 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 16 | 5. The guidance framework | 对象/条件/子问题展开 | 2259 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 17 | 6. Simulation results and discussion | 结果验证/讨论 | 1166 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 18 | 6.1. Comparison of different methods | 方法建构 | 3814 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 19 | 6.2. Monte Carlo simulation | 对象/条件/子问题展开 | 5216 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 20 | 6.3. Results with in-fl ight faults | 结果验证/讨论 | 3218 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 21 | 7. Conclusions | 主张回收/边界说明 | 1186 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 22 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 402 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：right(139)；left(138)；guidance(101)；big(49)；state(48)；pmb(47)；parameter(43)；array(42)；mathrm(42)；ight(41)；et-nmpg(41)；estimation(41)；data(34)；displaystyle(34)；frac(32)；parameters(31)；epsilon(31)；reentry(30)；nmpg(30)；tag(30)
- 高频学术名词/术语：guidance(101)；estimation(41)；deviation(16)；section(16)；simulation(16)；performance(15)；reference(14)；optimization(14)；motion(12)；detection(9)；density(9)；function(8)；solution(6)；mutation(6)；acceleration(5)
- 高频学术动词：obtained(7)；estimate(6)；estimated(5)；demonstrate(3)；introduce(3)；compared(3)；presented(3)；compare(3)；propose(2)；constructed(2)；optimized(2)；obtain(2)；introduced(2)；construct(1)；predicted(1)
- 高频形容词：aerodynamic(19)；terminal(17)；initial(17)；dynamic(12)；event(12)；atmospheric(12)；coefficient(10)；subsequent(9)；table(9)；cal(8)；actual(7)；predictive(7)；interval(7)；optimal(7)；constant(7)
- 高频副词：relatively(6)；specifically(5)；respectively(5)；significantly(5)；usually(4)；primarily(4)；slightly(4)；finally(4)；accurately(4)；early(4)；highly(3)；directly(3)
- 高频二词短语：left right(81)；parameter estimation(24)；right right(23)；pmb left(22)；begin array(21)；end array(21)；epsilon big(19)；guidance law(18)；right left(17)；ight state(14)；reentry guidance(13)；big big(13)；wape-assisted et-nmpg(13)；big epsilon(12)；array tag(11)
- 高频三词短语：left right right(16)；pmb left right(16)；end array tag(11)；left begin array(9)；end array right(9)；left right left(8)；right left right(8)；delta epsilon big(8)；epsilon big epsilon(8)；displaystyle cal left(8)；cal left right(8)；right end array(7)
- 被动语态估计：86
- `we + 动作动词` 主动句估计：5
- 一般现在时线索：207
- 一般过去时线索：257
- 现在完成时线索：2
- 情态动词线索：51

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints.
  - 可迁移句型：{object}, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints.
- 原句：Glide reentry does not have the same flexible fl ight control capability as a powered cruise vehicle, which makes it necessary to leave enough performance redundancy in the reference trajectory design.
  - 可迁移句型：{object} reentry does not have the same flexible fl ight control capability as a powered cruise vehicle, which makes it necessary to leave enough performance redundancy in the reference trajectory design.
- 原句：However, both strategies have limitations: the former requires substantial computing resources and demands constant high sensitivity from the entire navigation, guidance, and control system, while the latter is constrained by confl icting relationships between guidance cycle duration, TO efficiency, and guidance accuracy.
  - 可迁移句型：{object}, both strategies have limitations: the former requires substantial computing resources and demands constant high sensitivity from the entire navigation, guidance, and control system, while the latter is constrained by confl icting relationships betwee
- 原句：Finally, we will outline the reentry guidance problem that is considered in this work, along with some necessary assumptions.
  - 可迁移句型：{object}, we will outline the reentry guidance problem that is considered in This study, along with some necessary assumptions.
### gap/转折句
- 原句：However, the actual model parameter values often deviate from the reference values, leading to an excessively high event trigger frequency and potentially rendering the trajectory optimization unfeasible.
  - 可迁移句型：{object}, the actual model parameter values often deviate from the reference values, leading to an excessively high event trigger frequency and potentially rendering the trajectory optimization unfeasible.
- 原句：Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints.
  - 可迁移句型：{object}, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints.
- 原句：However, people believe that as technology continues to advance, winged vehicles will eventually regain their relevance in space transportation [2].
  - 可迁移句型：{object}, people believe that as technology continues to advance, winged vehicles will eventually regain their relevance in space transportation [2].
- 原句：However, both strategies have limitations: the former requires substantial computing resources and demands constant high sensitivity from the entire navigation, guidance, and control system, while the latter is constrained by confl icting relationships between guidance cycle duration, TO efficiency, and guidance accuracy.
  - 可迁移句型：{object}, both strategies have limitations: the former requires substantial computing resources and demands constant high sensitivity from the entire navigation, guidance, and control system, while the latter is constrained by confl icting relationships betwee
### 方法提出句
- 原句：Communicated by Xingqun Zhan This paper proposes an event-triggered model predictive guidance (ET-NM PG) method assisted by weight adaptive parameter estimation (WAPE) and applies it to reentry guidance.
  - 可迁移句型：{object} by Xingqun Zhan This study proposes an event-triggered model predictive guidance (ET-NM PG) method assisted by weight adaptive parameter estimation (WAPE) and applies it to reentry guidance.
- 原句：Guidance methods based on online trajectory optimization (TO) often face a trade-off between guidance accuracy and the efficiency of guidance command computation when dealing with complex problems.
  - 可迁移句型：{object} methods based on online trajectory optimization (TO) often face a trade-off between guidance accuracy and the efficiency of guidance command computation when dealing with complex problems.
- 原句：However, the actual model parameter values often deviate from the reference values, leading to an excessively high event trigger frequency and potentially rendering the trajectory optimization unfeasible.
  - 可迁移句型：{object}, the actual model parameter values often deviate from the reference values, leading to an excessively high event trigger frequency and potentially rendering the trajectory optimization unfeasible.
- 原句：To address this issue, we propose updating the model parameters online using WAPE within the general ET-NMPG framework, thereby enhancing guidance accuracy and reducing guidance frequency.
  - 可迁移句型：{object} address this issue, we propose updating the model parameters online using WAPE within the general ET-NMPG framework, thereby enhancing guidance accuracy and reducing guidance frequency.
### 结果证明句
- 原句：The numerical simulation results cofirm the effectiveness of the proposed method.
  - 可迁移句型：{object} numerical simulation results cofirm the effectiveness of the proposed method.
- 原句：This results in a wide range of state dispersion during and at the end of the reentry fl ight, which is not conducive to safe landing and reuse of the vehicle.
  - 可迁移句型：{object} results in a wide range of state dispersion during and at the end of the reentry fl ight, which is not conducive to safe landing and reuse of the vehicle.
- 原句：Since various pseudospectral methods [14] have begun to demonstrate excellent performance in solving trajectory optimization problems (TOP), many researchers have been trying to apply them to actual fl ight control [15-- 17] rather than simply using them as an offline fl ight performance evaluation tool.
  - 可迁移句型：{object} various pseudospectral methods [14] have begun to demonstrate excellent performance in solving trajectory optimization problems (TOP), many researchers have been trying to apply them to actual fl ight control [15-- 17] rather than simply using them as
- 原句：5 and 6 show the $v - H$ curves and ground tracks of the simulation results.
  - 可迁移句型：5 and 6 show the $v - {object}$ curves and ground tracks of the simulation results.
### 贡献收束句
- 原句：By using state deviation exceeding a threshold as an event-triggering condition, it is possible to effectively reduce computational resource consumption while ensuring a certain level of guidance accuracy.
  - 可迁移句型：{object} using state deviation exceeding a threshold as an event-triggering condition, it is possible to effectively reduce computational resource consumption while ensuring a certain level of guidance accuracy.
- 原句：For a long time, the main goal of related research has been to improve the efficiency of trajectory optimization (TO), such as the sequential convex optimization (SCP) method and its many improved versions [17-- 19].
  - 可迁移句型：{object} a long time, the main goal of related research has been to improve the efficiency of trajectory optimization (TO), such as the sequential convex optimization (SCP) method and its many improved versions [17-- 19].
- 原句：We cannot expect the NMPG to provide guidance commands in real-time like traditional algorithms, and current research has primarily employed two strategies for generating guidance commands through TO: the uninterrupted NMPG (UI-NMPG) strategy [24], which immediately carries out TO after completing the previous one; and the fi xed cycle NMPG (FC-NPMGP) strategy [25,26], which establishes a longer interval to ensure optimal guidance law generation within that period.
  - 可迁移句型：{object} cannot expect the NMPG to provide guidance commands in real-time like traditional algorithms, and current research has primarily employed two strategies for generating guidance commands through TO: the uninterrupted NMPG (UI-NMPG) strategy [24], which
- 原句：In this section, we fi rst defi ne the reentry TOP under consideration and then provide some tips to enhance the performance of the trajectory optimization solution.
  - 可迁移句型：{object} this section, we fi rst defi ne the reentry TOP under consideration and then provide some tips to enhance the performance of the trajectory optimization solution.
### 边界/谨慎句
- 原句：In addition, since the reentry dynamics system is an underactuated system, only one to three state variables can be selected for tracking (e.g., drag acceleration, altitude, latitude, and longitude) when performing tracking guidance [5,6].
  - 可迁移句型：{object} addition, since the reentry dynamics system is an underactuated system, only one to three state variables can be selected for tracking (e.g., drag acceleration, altitude, latitude, and longitude) when performing tracking guidance [5,6].
- 原句：As depicted in Fig. $^ {7 ,}$ due to the fi xed nature of FC-NMPG’s guidance cycle, a failure to update the guidance commands promptly when the fl ight state is approaching the path constraints may lead to subsequent violations of these constraints, resulting in guidance failure.
  - 可迁移句型：{object} depicted in Fig. $^ {7 ,}$ due to the fi xed nature of FC-NMPG’s guidance cycle, a failure to update the guidance commands promptly when the fl ight state is approaching the path constraints may lead to subsequent violations of these constraints, resu
- 原句：It should be noted that since the focus of this paper is on the guidance algorithm itself, we consider all the above deviations to be uniformly distributed within the set interval.
  - 可迁移句型：{object} should be noted that since the focus of This study is on the guidance algorithm itself, we consider all the above deviations to be uniformly distributed within the set interval.
- 原句：On this basis, the method for selecting the event-triggered threshold and the potential need for introducing robust NMPG should be explored in more detail.
  - 可迁移句型：{object} this basis, the method for selecting the event-triggered threshold and the potential need for introducing robust NMPG should be explored in more detail.

## 9. 引用风险层

- 正文引用簇估计：33
- 参考文献条数：79
- 可识别年份条目数：64
- 2021 年及以后参考文献数：27
- 2010 年以前经典文献数：7
- 高频来源粗略识别：Sci. Technol(7)；J. Aeronaut(2)；Aerosp. Electron. Syst(2)；Aerosp. Sci(1)；Guid. Control Dyn(1)；Autom. Control(1)；Clean. Prod(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- Bentley, Spaceplanes: From Airport to Spaceport, Springer, New York, NY, 2009. [3] Z. Liu, G.
- Zheng, B.
- Zhang, J.
- Wei, H.
- Huang, J.
- Yan, Predictor-corrector reentry guidance for hypersonic glide vehicles based on high-precision analytical solutions, Aerosp. Sci. Technol. (2024) 109545, https://doi.org/10.1016/j.ast.2024.109545. [4] R.
- Chai, A.
- Tsourdos, A.
- Savvaris, S.
- Chai, Y.
- Xia, C.
- Chen, Review of advanced guidance and control algorithms for space/aerospace vehicles, Prog. Aerosp. Sci. 122 (2021) 100696, https://doi.org/10.1016/j.paerosci.2021.100696. [5] P. Lu, Regulation about time-varying trajectories: precision entry guidance illus trated, J. Guid. Control Dyn. 22 (6) (1999) 784--790, https://doi.org/10.2514/2. 4479. [6] A. Vitiello, E.M. Leonardi, M. Pontani, Multiple-sliding-surface guidance and control for terminal atmospheric reentry and precise landing, J. Spacecr
- Chen, L.
- Cui, S.
- Chai, G.

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
