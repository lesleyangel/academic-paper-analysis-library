# A sparse reconstruction method of physical field via multi-source sensors for flight vehicle

## 0. 读取说明

本拆解基于 `801/文本/txt/A-sparse-reconstruction-method-of-physical-field-via_2025_Aerospace-Science-.txt` 和对应 metadata。文本可确认摘要、方法流程、公式结构、表格数值、传感器数量结论和重构误差；但 Fig. 7-Fig. 16 的 POD 模态、传感器位置、重构云图和噪声对比曲线需要 PDF 图像复核。本文图像承担较强论证功能，文字拆解无法替代视觉复核。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 Methods, 3 Test case, 4 Conclusions。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：A sparse reconstruction method of physical field via multi-source sensors for flight vehicle
- 作者：Xiaobing Ma, Xuyi Jia, Chunna Li, Chunlin Gong
- 期刊与年份：Aerospace Science and Technology, 167, 2025, 110685
- DOI：10.1016/j.ast.2025.110685
- 领域：飞行器物理场重构、传感器优化、POD、RBFNN、差分进化、降阶模型
- 类型：数据驱动方法论文 + 再入舱压力/热流场案例验证
- 研究对象：在飞行器表面用有限多源传感器同时重构多个物理场，本例为 reentry capsule 的压力场和热流场。
- 方法组合：POD 提取低维模态，RBFNN 建立多源传感器测量到多物理场模态系数的映射，DE 优化传感器位置与类型，系统可观测性分析确定最少传感器数量。

这篇论文的身份是“多源传感器稀疏重构方法论文”。它的核心不在于提出新的 CFD 数据，而在于证明压力传感器与热流传感器的信息可以共享，从而减少传感器总数并提高多物理场重构精度。

## 2. 摘要与核心信息提取

摘要的结构是：稀疏传感器重构可服务设计、控制和维护 -> 同时测压力/热流会导致多类传感器数量增加 -> 不同物理场在相同流动条件下相关 -> 提出利用多源传感器信息的稀疏重构方法 -> 理论分析最少传感器数 -> POD-RBFNN-DE 三步实现 -> 再入舱案例验证。

一句话主张：通过把多种传感器测量作为共享输入，POD-RBFNN-DE 方法能以更少传感器同时重构压力和热流场，并在同等传感器数量下显著降低重构误差。

核心结果：

- 相比传统 single-source 方法，同等精度下总传感器数量约减少 50%。
- 同等总传感器数量下，稀疏重构误差降低约 16%-99%。
- 压力场和热流场的理论最少多源传感器数均为 3。
- 3 个多源传感器通常配置为 1 个 pressure sensor + 2 个 heat flux sensors。
- 噪声分析显示在不同噪声水平下最少多源传感器数量保持稳定。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/A-sparse-reconstruction-method-of-physical-field-via_2025_Aerospace-Science-.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/A-sparse-reconstruction-method-of-physical-field-via_2025_Aerospace-Science-.md`。

中文译文：

> 依靠表面稀疏安装的传感器进行物理场重建可以为飞行器的设计、控制和维护提供更有价值和更详细的信息。当需要同时测量压力、热通量等多种物理特性时，需要针对相应的特性安装不同的传感器，从而增加了传感器的数量，导致测量复杂度和成本。鉴于相同流动条件下不同物理场的相关性，提出了一种利用不同类型传感器信息的稀疏重建方法，以减少传感器数量并提高重建精度。同时，进行了理论分析，确定了该方法实现目标重建精度所需的最少多源传感器数量。该方法通过三个步骤实现。首先，通过适当的正交分解算法，识别并提取各个物理场的模式。然后，通过使用径向基函数神经网络，创建从多源传感器的测量到多个物理场的模式系数的映射。最后，对于给定的传感器总数，建立优化模型以确定传感器的最佳位置和类型，并通过差分进化算法求解。
>
> 作为验证案例，重建了高超声速再入舱的压力场和热流场。结果表明，与传统的单源重建方法相比，在相同精度水平下，该方法可减少传感器总数约50%，且在传感器总数相同的情况下，稀疏重建误差可减少16%~99%。 CS起源于信号处理，利用信号稀疏性从有限的观测中重建完整信号，并已广泛用于高维物理场数据的稀疏重建[7,8]。白等人。 [9]利用CS重建粒子图像测速流数据。类似地，CS被用来重建空化水翼周围的非定常流场[10]。然而，CS需要优化来求解基系数，并且本质上是NP难的，这对确保稀疏重建精度提出了挑战。为了解决这个问题，Sha 等人。 [11]提出了一种改进的CS方法，该方法结合了全连接神经网络来细化基系数的求解过程。然而，这种改进也导致模型复杂性增加和计算效率降低。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题来自飞行器表面分布载荷测量的现实限制：压力、热流等物理场对气动设计、热防护、健康监测和控制很重要，但飞行器表面传感器安装位置有限。传统每个物理场各自布置传感器，会增加数量、复杂度、成本和空间冲突。

作者把问题收束为：如何利用同一流动条件下多个物理场的相关性，让压力传感器和热流传感器共同服务多个场的重构，而不是分别重构各自物理场。

选题价值很明确：它直接服务“少装传感器但多拿信息”的飞行器智能感知目标。方法价值在于把 sensor type 和 sensor location 一起优化，而非只优化位置。

## 4. 领域位置与文献版图

Introduction 的文献版图分三层：

- 稀疏重构模型：早期 compressed sensing 可从有限观测恢复高维场，但求解 NP-hard 且模型复杂。
- 回归式重构模型：deep learning model 可直接映射稀疏测量到高维场，精度高但训练复杂、优化传感器位置时代价大。
- ROM-based surrogate model：POD 等 ROM 先降维，再用 RBFNN/MLP 映射到模态系数，效率较高。
- 传感器布置：已有 heuristic optimization、greedy、GA、Lichtenberg 等用于优化位置，但多集中在单源场数据。

本文站位是“ROM-based surrogate + multi-source sensor optimization”。它不是重新发明 POD 或 RBFNN，而是把多源测量作为共享输入，并提出最少多源传感器数量分析。

## 5. Gap 制造机制

作者制造 gap 的关键句是：既有稀疏重构和传感器位置优化研究较成熟，但主要聚焦 single-source field data reconstruction，对 multi-source field data 探索有限。

具体 gap：

- 对象 gap：多物理场同时重构不足。
- 信息利用 gap：传统方法分别使用各物理场自己的传感器测量，没有利用跨场相关性。
- 数量 gap：有限传感器条件下，如何理论确定满足精度的最少多源传感器数仍需分析。
- 优化 gap：传感器位置和类型应联合优化，而非先验固定类型。

gap 可信，因为飞行器压力与热流来自同一 Ma、攻角、高度等流动条件，理论上存在共享低维参数驱动。风险是这种相关性在更复杂非定常、分离流或强局部热化学效应下可能减弱。

## 6. 创新性判断

作者声明的贡献三条：提出多源传感器物理场稀疏重构方法；理论分析最少多源传感器数量；在再入舱压力/热流案例中验证减少传感器和提高精度，并验证噪声鲁棒性。

真实创新判断：

- 问题创新：中等偏强。把 single-source 稀疏重构推进到 multi-source。
- 方法创新：中等。POD、RBFNN、DE 都是成熟组件，创新在组合方式和多源输入定义。
- 理论贡献：中等。用 rank/observability 解释最少传感器数，增强方法可信度。
- 应用验证：较强。给出压力和热流两个场的重构、传感器类型分配、噪声分析。

创新风险：方法在两个物理场、三个流动参数的样本中验证，尚不清楚扩展到更多场、更多参数和非定常数据时是否仍保持 50% 传感器减少。

## 7. 论证链条复原

论证链条：

飞行器表面物理场测量重要但传感器数量受限 -> 同时测多个物理场会进一步增加复杂度 -> 多物理场受相同流动条件驱动，因此具有相关性 -> 建立多源传感器共享输入的稀疏重构系统 -> 用 POD 将各物理场降阶，用 RBFNN 从多源测量映射到多个场模态系数，用 DE 联合优化传感器位置和类型 -> 用 rank/observability 推导最少传感器数 -> 再入舱压力/热流场验证精度、传感器数量和噪声鲁棒性 -> 得出多源方法比 single-source 更省传感器且更准。

逻辑闭合度高。最强环节是理论最少传感器数与实际优化结果一致：rank(X)=3，压力/热流 rank 均为 3，最终 3 个多源传感器可准确重构。薄弱环节是对物理场相关性的边界条件讨论不足。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：When various physical properties, such as pressure and heat flux, need to be measured simultaneously, different sensors will be installed for corresponding properties, which increases the number of sensors, leading to measuring complexity and cost. However, CS requires optimization to solve basis coefficients and is inherently NP-hard, posing challenges for ensuring sparse reconstruction accuracy. Measuring distributed loads of physical fields like force and heat on surface is essential for aerodynamic design, integrated thermal protec tion system analysis, health monitoring, and flight control of flight vehicle [1–3].
- 已有研究不足/GAP：Originating in signal processing, CS leverages signal sparsity to recon struct complete signals from limited observations and has been widely used for sparse reconstruction of high-dimensional physical field data [7,8]. However, CS requires optimization to solve basis coefficients and is inherently NP-hard, posing challenges for ensuring sparse reconstruction accuracy. However, this improvement also led to increased model complexity and reduced computational efficiency.
- 本文解决方式：Given that different physical fields under the same flow conditions are correlated, a sparse reconstruction method utilizing information from different types of sensors is proposed to reduce the number of sensors and improve reconstruction accuracy. Meanwhile, a theoretical analysis is conducted to determine the minimum number of multi-source sensors required by the proposed method to achieve target reconstruction accuracy. The method is achieved by three steps.
- 学术或工程增量：The physical field reconstruction depending on sensors installed sparsely on the surface can provide more valuable and detailed information for design, control, and maintenance of flight vehicles. Given that different physical fields under the same flow conditions are correlated, a sparse reconstruction method utilizing information from different types of sensors is proposed to reduce the number of sensors and improve reconstruction accuracy. Meanwhile, a theoretical analysis is conducted to determine the minimum number of multi-source sensors required by the proposed method to achieve target reconstruction accuracy.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

方法由三步组成：

1. 数据库生成：对流动条件 x = [Ma, alpha, H] 采样，获得压力场 P 和热流场 q。
2. POD-RBFNN 重构模型：对每个物理场做 POD，选取满足误差阈值的模态数；以多源传感器测量 D 作为 RBFNN 输入，预测多个物理场模态系数，再重构完整场。
3. 传感器优化：在给定传感器总数下，构建目标函数，DE 同时决定传感器位置和类型。

最少传感器数分析：

- 通过物理场数据与流动参数之间的 rank 关系判断系统可观测性。
- 本例流动条件有 Ma、攻角、高度 3 个参数，rank(X)=3。
- 对任意压力或热流场，至多对应一组流动条件，因此 rank(P)=rank(q)=3。
- 单源和多源重构理论最少传感器数均为 3，但多源的 3 个传感器可共享信息，同时重构两个场。

模型细节：

- 压力场选取 6 个 POD modes，热流场选取 12 个 POD modes。
- 热流场更复杂，需要更多模态，优化结果因此分配更多热流传感器。
- RBFNN 选择理由是输入/输出维度较低、非线性拟合强、结构简单、建模效率高。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 多源方法可减少传感器数量约 50% | 摘要、3.3、Table 3 | single-source 至少需 6 个传感器准确重构两个场；proposed method 用 3 个多源传感器 | 强 | “准确”阈值依赖本文误差定义 |
| 同等传感器数量下多源方法显著降低误差 | 摘要、Table 3 | 3 传感器时压力误差 119.12 -> 13.03，热流误差 115.96 -> 25.88；6 传感器时压力/热流误差降低 16.27%/44.99% | 强 | 表格中 E 为无量纲综合误差，需解释给读者 |
| 最少多源传感器数量可由可观测性/rank 分析确定 | 2.2、3.2 | rank(X)=3，rank(P)=rank(q)=3，理论最少传感器数为 3，实际优化也得到 3 | 中-强 | 对噪声和模型误差下 rank 稳定性讨论有限 |
| 优化位置具有物理意义 | 3.3、Fig. 11 | 1 个压力传感器位于压力梯度大的鼻部，2 个热流传感器位于热流梯度明显的过渡区域 | 中 | 位置和梯度需 PDF 图像复核 |
| 热流重构比压力更难 | 3.2、3.3 | 热流场需 12 个 modes，压力场需 6 个 modes；热流最大误差可达 10.29%，高于压力 1.40% | 强 | 仍需更复杂流动案例验证 |
| 方法对传感器噪声保持有效 | 3.4、Fig. 15-Fig. 16、结论 | 不同噪声水平下，3 个多源传感器仍有可比精度；最少传感器数稳定 | 中 | 噪声类型主要为模拟随机噪声，真实漂移/失效更复杂 |

## 10. 图表、公式与结果叙事提取

- Fig. 1：多源传感器物理场重构示意图，是方法概念图，说明多源测量如何共享输入。
- Fig. 2：确定最少多源传感器数量流程，承担理论分析图功能。
- Fig. 3：整体方法流程，串联数据库、重构模型和传感器优化。
- Fig. 4：RBFNN 结构，说明从多源测量到模态系数的非线性映射。
- Fig. 5：多源传感器位置优化流程，展示 DE 在闭环中更新位置与类型。
- Fig. 6：再入舱几何和尺寸，给出验证对象。
- Fig. 7-Fig. 8：压力和热流 POD 主模态，支撑“低维结构可提取”。需要 PDF 图像复核。
- Fig. 9：POD modes 数量与重构误差，支撑压力 6 模态、热流 12 模态选择。
- Fig. 10/Table 3：single-source vs multi-source 误差对比，是核心定量证据。
- Fig. 11：10 次优化得到的最优多源传感器位置，支撑鲁棒性和物理意义。
- Fig. 12-Fig. 13/Table 4：最差/最好测试样本的重构云图和误差，展示局部误差分布。需要 PDF 图像复核。
- Fig. 14-Fig. 16：传感器冗余机制、噪声下误差比较和重构结果，支撑噪声鲁棒性。
- 公式 (1)-(3)：single-source 与 multi-source 重构模型对比，是问题重定义核心。
- 公式 (20) 等：由均值、POD modes 和预测模态系数重构完整场。
- 优化目标公式：服务传感器位置与类型联合优化。

## 11. 章节结构与篇章布局

真实章节：1 Introduction -> 2 Methods -> 3 Test case -> 4 Conclusions。第 2 节进一步分为 multi-source method、minimum number、ROM-based surrogate、DE sensor optimization；第 3 节分为 physical model、modeling parameters、reconstruction results、sensor noise。

结构是“方法集中 + 案例验证集中”的 AST 风格。Introduction 末尾直接列贡献，Methods 把所有算法组件拆开，Test case 再按建模参数、结果、噪声逐步加证据。

标题命名偏方法模块型：`Sparse reconstruction method via multi-source sensors`, `Minimum number`, `Sensor location optimization using DE algorithm`。优点是模块边界清晰；不足是 `Test case` 标题较泛，可改为 `Reentry capsule pressure and heat-flux reconstruction`。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.3: 2 Methods（方法/模型/算法）
  - L3 p.3: 2.1 Sparse reconstruction method via multi-source sensors（方法/模型/算法）
  - L3 p.4: 2.2 Minimum number of the multi-source sensors（对象/模块/过渡章节）
    - L4 p.4: 2.2.1 Determine the rank of physical field data（对象/模块/过渡章节）
    - L4 p.4: 2.2.2 Determine the minimum number of sensors（对象/模块/过渡章节）
  - L3 p.5: 2.3 Sparse reconstruction model using rom-based surrogate（方法/模型/算法）
  - L3 p.6: 2.4 Sensor location optimization using de algorithm（方法/模型/算法）
- L2 p.6: 3 Test case（结果/验证/讨论）
  - L3 p.6: 3.1 Description of physical model（方法/模型/算法）
  - L3 p.6: 3.2 Modeling parameters analysis（方法/模型/算法）
  - L3 p.8: 3.3 Reconstruction results（结果/验证/讨论）
  - L3 p.10: 3.4 Analysis of sensor noise（对象/模块/过渡章节）
- L2 p.11: 4 Conclusions（结论/贡献回收）
- L2 p.12: CRediT authorship contribution statement（尾部材料）
- L2 p.12: Declaration of competing interest（尾部材料）
- L2 p.12: Acknowledgments（尾部材料）
- L2 p.12: Appendix. Additional information of test cases（结果/验证/讨论）
- L2 p.12: Data availability（尾部材料）
- L2 p.12: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 Methods | 3 | 2 | 方法/模型/算法 |
| 2.1 Sparse reconstruction method via multi-source sensors | 3 | 3 | 方法/模型/算法 |
| 2.2 Minimum number of the multi-source sensors | 4 | 3 | 对象/模块/过渡章节 |
| 2.2.1 Determine the rank of physical field data | 4 | 4 | 对象/模块/过渡章节 |
| 2.2.2 Determine the minimum number of sensors | 4 | 4 | 对象/模块/过渡章节 |
| 2.3 Sparse reconstruction model using rom-based surrogate | 5 | 3 | 方法/模型/算法 |
| 2.4 Sensor location optimization using de algorithm | 6 | 3 | 方法/模型/算法 |
| 3 Test case | 6 | 2 | 结果/验证/讨论 |
| 3.1 Description of physical model | 6 | 3 | 方法/模型/算法 |
| 3.2 Modeling parameters analysis | 6 | 3 | 方法/模型/算法 |
| 3.3 Reconstruction results | 8 | 3 | 结果/验证/讨论 |
| 3.4 Analysis of sensor noise | 10 | 3 | 对象/模块/过渡章节 |
| 4 Conclusions | 11 | 2 | 结论/贡献回收 |
| CRediT authorship contribution statement | 12 | 2 | 尾部材料 |
| Declaration of competing interest | 12 | 2 | 尾部材料 |
| Acknowledgments | 12 | 2 | 尾部材料 |
| Appendix. Additional information of test cases | 12 | 2 | 结果/验证/讨论 |
| Data availability | 12 | 2 | 尾部材料 |
| References | 12 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 的段落推进是：物理场测量重要 -> 稀疏重构模型分类 -> 传感器数量和位置问题 -> single-source 研究不足 -> 本文贡献。每段都有“先定义一类方法，再指出不足”的结构。

Methods 叙事以流程图和公式驱动：先给传统 single-source 公式，再给 multi-source 公式，形成直接对比。随后用 rank 分析提供理论支撑，再用 POD-RBFNN 和 DE 讲实现。

Results 叙事是逐层加证据：先证明 POD 模态选择合理，再证明最少传感器数，再给误差表，再给最优位置，再展示最好/最差样本，最后加噪声鲁棒性。这个节奏很稳，避免只展示平均误差。

## 13. 文笔画像与语言习惯

整体语气是数据驱动方法型。常用 `proposed`, `constructed`, `optimized`, `validated`, `demonstrate`, `significantly reducing`。claim 强度较高，但通常紧跟表格数值。

主动/被动：方法贡献多用主动或无主句，实验/验证多用被动 `is validated`, `is determined`, `is constructed`。时态稳定：方法定义现在时，结果解释现在时，已有研究现在完成时。

高频词：`reconstruction`, `sparse`, `sensor`, `multi-source`, `physical field`, `pressure`, `heat flux`, `POD`, `RBFNN`, `optimization`, `accuracy`。限定词使用较多，如 `limited`, `minimum`, `optimum`, `same accuracy level`，说明作者在控制 claim 边界。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：25590
- 高频词：reconstruction(96)；sparse(87)；physical(62)；sensor(56)；field(52)；model(50)；data(46)；number(39)；multi-source(39)；sensors(37)；rank(36)；method(27)；locations(22)；flow(22)；measurements(19)；minimum(18)；function(17)；optimization(17)；multiple(16)；accuracy(15)
- 高频名词化/学术名词：reconstruction(96)；function(17)；optimization(17)；location(11)；section(8)；pressure(5)；information(4)；turbulence(4)；observability(4)；tion(3)；complexity(3)；decomposition(3)；measurement(3)；ensure(3)；relationship(3)
- 高频学术动词：achieve(5)；validated(5)；construct(3)；compared(3)；constructed(3)；developed(2)；achieved(2)；provided(2)；predicted(2)；provide(1)；indicate(1)；optimized(1)；optimize(1)；derived(1)；analyzed(1)
- 高频形容词：physical(62)；neural(7)；total(6)；objective(6)；different(4)；theoretical(4)；high-dimensional(4)；various(3)；traditional(3)；computational(3)；measurement(3)；ni-dimensional(3)；thermal(2)；orthogonal(2)；radial(2)
- 高频副词：generally(4)；subsequently(4)；directly(3)；additionally(3)；effectively(3)；significantly(3)；theoretically(3)；commonly(2)；firstly(2)；widely(2)；similarly(2)；fully(2)；successfully(2)；specifically(2)；finally(2)
- 高频二词短语：sparse reconstruction(77)；physical field(42)；field data(36)；reconstruction model(27)；sensor locations(20)；multi-source sensor(20)；number sensors(19)；minimum number(17)；sensor measurements(14)；multiple physical(14)；flow conditions(13)；reconstruction method(12)
- 高频三词短语：physical field data(28)；sparse reconstruction model(25)；sparse reconstruction method(10)；number multi-source sensors(9)；sensor location optimization(9)；multiple physical field(9)；minimum number multi-source(8)；minimum number sensors(8)；sparse reconstruction models(7)；multi-source sensor measurements(6)；multi-source sensor locations(6)；ith physical field(6)
- 被动语态估计：73；`we + 动作动词` 主动句估计：1
- 一般现在时线索：84；一般过去时线索：206；现在完成时线索：2；情态动词线索：36

分章节正文词频：

- 1 Introduction: reconstruction(49)；sparse(45)；physical(24)；sensor(23)；model(23)；field(21)；data(21)；sensors(20)
- 2 Methods: reconstruction(36)；rank(36)；sparse(35)；physical(32)；field(28)；sensor(26)；model(22)；data(22)
- 3 Test case: reconstruction(3)；physical(3)；flow(3)；conditions(3)；reentry(3)；capsule(3)；sparse(2)；field(2)
- 4 Conclusions: reconstruction(8)；method(8)；sensor(7)；sparse(5)；sensors(5)；multi-source(4)；number(4)；physical(3)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

背景句：

- `Measuring distributed loads of physical fields ... is essential for...`
- 模仿：测量 X 的分布式物理场对设计、控制和维护具有基础作用。

Gap 句：

- `previous research ... mainly focuses on single-source field data reconstruction`
- 模仿：已有研究主要关注单一数据源/单一物理量，对多源耦合信息利用不足。

方法句：

- `The method is achieved by three steps. Firstly... Then... Lastly...`
- 模仿：所提方法由三步实现：先降维提取主模态，再建立传感器到模态系数映射，最后优化传感器类型和位置。

结果句：

- `compared with traditional single-source reconstruction method, the proposed method...`
- 模仿：与传统单源方法相比，所提方法在相同精度下减少传感器数量，并在相同传感器预算下降低重构误差。

风险控制句：

- `Introducing a nonlinear reduced-order model ... may improve...`
- 模仿：未来可引入更强的非线性降阶模型以改善复杂物理场的局部重构精度。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：However, CS requires optimization to solve basis coefficients and is inherently NP-hard, posing challenges for ensuring sparse reconstruction accuracy.
  可迁移模板：However, METHOD requires optimization to solve basis coefficients and is inherently METHOD-hard, posing challenges for ensuring sparse reconstruction accuracy.
- 原句：Measuring distributed loads of physical fields like force and heat on surface is essential for aerodynamic design, integrated thermal protec tion system analysis, health monitoring, and flight control of flight vehicle [1–3].
  可迁移模板：Measuring distributed loads of physical fields like force and heat on surface is essential for aerodynamic design, integrated thermal protec tion system analysis, health monitoring, and flight control of flight vehicle [X–X].
- 原句：However, the limited sensor locations on the fight vehicle surface poses challenges in obtaining complete field data.
  可迁移模板：However, the limited sensor locations on the fight vehicle surface poses challenges in obtaining complete field data.
- 原句：However, CS requires optimization to solve basis coefficients and is inherently NP-hard, posing challenges for ensuring sparse reconstruction accuracy.
  可迁移模板：However, METHOD requires optimization to solve basis coefficients and is inherently METHOD-hard, posing challenges for ensuring sparse reconstruction accuracy.
- 原句：Unlike CS, which requires optimizing basis coefficients, these models directly map sparse sensor measurements to physical field data.
  可迁移模板：Unlike METHOD, which requires optimizing basis coefficients, these models directly map sparse sensor measurements to physical field data.
#### Gap/转折句
- 原句：Originating in signal processing, CS leverages signal sparsity to recon struct complete signals from limited observations and has been widely used for sparse reconstruction of high-dimensional physical field data [7,8].
  可迁移模板：Originating in signal processing, METHOD leverages signal sparsity to recon struct complete signals from limited observations and has been widely used for sparse reconstruction of high-dimensional physical field data [X,X].
- 原句：However, CS requires optimization to solve basis coefficients and is inherently NP-hard, posing challenges for ensuring sparse reconstruction accuracy.
  可迁移模板：However, METHOD requires optimization to solve basis coefficients and is inherently METHOD-hard, posing challenges for ensuring sparse reconstruction accuracy.
- 原句：However, this improvement also led to increased model complexity and reduced computational efficiency.
  可迁移模板：However, this improvement also led to increased model complexity and reduced computational efficiency.
- 原句：However, the limited sensor locations on the fight vehicle surface poses challenges in obtaining complete field data.
  可迁移模板：However, the limited sensor locations on the fight vehicle surface poses challenges in obtaining complete field data.
- 原句：To address this issue, researchers have developed sparse reconstruction methods to reconstruct physical filed data from limited sensor measurements.
  可迁移模板：To address this issue, researchers have developed sparse reconstruction methods to reconstruct physical filed data from limited sensor measurements.
#### 方法提出句
- 原句：Given that different physical fields under the same flow conditions are correlated, a sparse reconstruction method utilizing information from different types of sensors is proposed to reduce the number of sensors and improve reconstruction accuracy.
  可迁移模板：Given that different physical fields under the same flow conditions are correlated, a sparse reconstruction method utilizing information from different types of sensors is proposed to reduce the number of sensors and improve reconstruction accuracy.
- 原句：Meanwhile, a theoretical analysis is conducted to determine the minimum number of multi-source sensors required by the proposed method to achieve target reconstruction accuracy.
  可迁移模板：Meanwhile, a theoretical analysis is conducted to determine the minimum number of multi-source sensors required by the proposed method to achieve target reconstruction accuracy.
- 原句：Lastly, for given total number of sensors, the optimization model to determine the optimum locations and types of sensors is built, and solved by differential evolution algorithm.
  可迁移模板：Lastly, for given total number of sensors, the optimization model to determine the optimum locations and types of sensors is built, and solved by differential evolution algorithm.
- 原句：The results indicate that, compared with traditional single-source reconstruction method, the proposed method can decrease the total sensor number by about 50% with the same accuracy level, and with the same total number of sensors, the sparse reconstruction error can be reduced by 16% to 99%.
  可迁移模板：The results indicate that, compared with traditional single-source reconstruction method, the proposed method can decrease the total sensor number by about X with the same accuracy level, and with the same total number of sensors, the sparse reconstruction error can be reduced by X to X.
- 原句：To address this, Sha et al. [11] proposed an improved CS method that incorporates a fully connected neural network to refine the solution process of basis coefficients.
  可迁移模板：To address this, Sha et al. [X] proposed an improved METHOD method that incorporates a fully connected neural network to refine the solution process of basis coefficients.
#### 结果呈现句
- 原句：Meanwhile, a theoretical analysis is conducted to determine the minimum number of multi-source sensors required by the proposed method to achieve target reconstruction accuracy.
  可迁移模板：Meanwhile, a theoretical analysis is conducted to determine the minimum number of multi-source sensors required by the proposed method to achieve target reconstruction accuracy.
- 原句：The results indicate that, compared with traditional single-source reconstruction method, the proposed method can decrease the total sensor number by about 50% with the same accuracy level, and with the same total number of sensors, the sparse reconstruction error can be reduced by 16% to 99%.
  可迁移模板：The results indicate that, compared with traditional single-source reconstruction method, the proposed method can decrease the total sensor number by about X with the same accuracy level, and with the same total number of sensors, the sparse reconstruction error can be reduced by X to X.
- 原句：Meanwhile, a theoretical analysis is conducted to determine the minimum number of multi-source sensors required by the proposed method to achieve target reconstruction accuracy.
  可迁移模板：Meanwhile, a theoretical analysis is conducted to determine the minimum number of multi-source sensors required by the proposed method to achieve target reconstruction accuracy.
- 原句：The results indicate that, compared with traditional single-source reconstruction method, the proposed method can decrease the total sensor number by about 50% with the same accuracy level, and with the same total number of sensors, the sparse reconstruction error can be reduced by 16% to 99%.
  可迁移模板：The results indicate that, compared with traditional single-source reconstruction method, the proposed method can decrease the total sensor number by about X with the same accuracy level, and with the same total number of sensors, the sparse reconstruction error can be reduced by X to X.
- 原句：Fukami et al. [15] employed convolutional neural networks to achieve sparse reconstruction of the 2D cylinder wake and sea surface temperature field.
  可迁移模板：Fukami et al. [X] employed convolutional neural networks to achieve sparse reconstruction of the METHOD cylinder wake and sea surface temperature field.
#### 贡献/增量句
- 原句：The physical field reconstruction depending on sensors installed sparsely on the surface can provide more valuable and detailed information for design, control, and maintenance of flight vehicles.
  可迁移模板：The physical field reconstruction depending on sensors installed sparsely on the surface can provide more valuable and detailed information for design, control, and maintenance of flight vehicles.
- 原句：Given that different physical fields under the same flow conditions are correlated, a sparse reconstruction method utilizing information from different types of sensors is proposed to reduce the number of sensors and improve reconstruction accuracy.
  可迁移模板：Given that different physical fields under the same flow conditions are correlated, a sparse reconstruction method utilizing information from different types of sensors is proposed to reduce the number of sensors and improve reconstruction accuracy.
- 原句：To address this, Sha et al. [11] proposed an improved CS method that incorporates a fully connected neural network to refine the solution process of basis coefficients.
  可迁移模板：To address this, Sha et al. [X] proposed an improved METHOD method that incorporates a fully connected neural network to refine the solution process of basis coefficients.
- 原句：However, this improvement also led to increased model complexity and reduced computational efficiency.
  可迁移模板：However, this improvement also led to increased model complexity and reduced computational efficiency.
- 原句：Given that different physical fields under the same flow conditions are correlated, a sparse reconstruction method utilizing information from different types of sensors is proposed to reduce the number of sensors and improve reconstruction accuracy.
  可迁移模板：Given that different physical fields under the same flow conditions are correlated, a sparse reconstruction method utilizing information from different types of sensors is proposed to reduce the number of sensors and improve reconstruction accuracy.
#### 限制/边界句
- 原句：Originating in signal processing, CS leverages signal sparsity to recon struct complete signals from limited observations and has been widely used for sparse reconstruction of high-dimensional physical field data [7,8].
  可迁移模板：Originating in signal processing, METHOD leverages signal sparsity to recon struct complete signals from limited observations and has been widely used for sparse reconstruction of high-dimensional physical field data [X,X].
- 原句：However, the limited sensor locations on the fight vehicle surface poses challenges in obtaining complete field data.
  可迁移模板：However, the limited sensor locations on the fight vehicle surface poses challenges in obtaining complete field data.
- 原句：To address this issue, researchers have developed sparse reconstruction methods to reconstruct physical filed data from limited sensor measurements.
  可迁移模板：To address this issue, researchers have developed sparse reconstruction methods to reconstruct physical filed data from limited sensor measurements.
- 原句：In early studies, compressed sensing [6] (CS) was commonly used to construct sparse reconstruction models. * Corresponding author.
  可迁移模板：In early studies, compressed sensing [X] (METHOD) was commonly used to construct sparse reconstruction models. * Corresponding author.
- 原句：Originating in signal processing, CS leverages signal sparsity to recon struct complete signals from limited observations and has been widely used for sparse reconstruction of high-dimensional physical field data [7,8].
  可迁移模板：Originating in signal processing, METHOD leverages signal sparsity to recon struct complete signals from limited observations and has been widely used for sparse reconstruction of high-dimensional physical field data [X,X].
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用主要服务三类功能：

- 稀疏重构背景：CS、PIV、流场重构、wind tunnel/flight applications。
- 模型分类：deep learning-based model 与 ROM-based surrogate model 的优缺点对比。
- 传感器优化：PSO、greedy、GA、Lichtenberg、DE 等位置优化方法。

作者评价前人的方式是“分类-优缺点-本文选择”：DNN 精度强但训练/优化成本高，ROM-based surrogate 效率好，因此本文选 POD-RBFNN。引用策略对方法选择服务很直接。

风险：多源传感器相关工作的引用可能较少，若审稿人熟悉 multi-modal sensing 或 multi-fidelity data fusion，可能要求更广文献版图。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：82
- Introduction 引文簇数量估计：26
- References 条目数：51
- 可识别年份条目数：79
- 2021 年及以后文献数：65
- 2010 年前经典文献数：2
- 同刊引用数（按 subject 粗匹配）：1
- 高频来源期刊：Aerospace Science and Technology(1)；Composite Structures(1)
- 引文簇样例：[7,8], [9], [10], [11], [4,5], [12,13], [6], [27], [14], [15], [28,29], [5]

带引文的 gap/转折句样例：

- Originating in signal processing, CS leverages signal sparsity to recon struct complete signals from limited observations and has been widely used for sparse reconstruction of high-dimensional physical field data [7,8].
- This poses significant challenges for space-constrained applications, such as smart micro aerial vehicles [28,29].

References 解析样例（前 8 条）：

- 5. The simulation results for these four meshes under the given flow conditions (Ma = 10.0, α = −25∘, H = 50.0km) are shown in the Fig.
- 17. It can be observed that the calculated heat flux obtained with mesh I and mesh II are sufficiently similar. Thus, the mesh II is adopted in this case. The total grid size is approximately 1.39 million, with the surface discretized using triangles and quadrilateral elements, totaling 17,125 grids.
Fig.
- 17. Results of the grid independence test: (a) surface pressure-coefficients at position Z = 0mand (b) surface heat flux at position Z = 0m.
References
- [1] W. Xiong, C. Zhu, D. Guo, C. Hou, Z. Yang, Z. Xu, L. Qiu, H. Yang, K. Li, Y. Huang, Bio-inspired, intelligent flexible sensing skin for multifunctional flying perception, Nano Energy 90 (2021) 106550, https://doi.org/10.1016/j.nanoen.2021.106550.
- [2] Y. Huang, C. Zhu, W. Xiong, Y. Wang, Y. Jiang, L. Qiu, D. Guo, C. Hou, S. Jiang, Z. Yang, B. Wang, L. Wang, Z. Yin, Flexible smart sensing skin for “fly-by-feel” morphing aircraft, Sci. China Technol. Sci. 65 (1) (2022) 1–29, https://doi.org/ 10.1007/s11431-020-1793-0.
- [3] M.N. Mowla, D. Asadi, T. Durhasan, J.R. Jafari, M. Amoozgar, Recent advancements in morphing applications: architecture, artificial intelligence integration, challenges, and future trends-a comprehensive survey, Aerosp. Sci. Technol. 161 (2025) 110102, https://doi.org/10.1016/j.ast.2025.110102.
- [4] P. Dubois, T. Gomez, L. Planckaert, L. Perret, Machine learning for fluid flow reconstruction from limited measurements, J. Comput. Phys. 448 (2022) 110733, https://doi.org/10.1016/j.jcp.2021.110733.
- [5] J.E. Santos, Z.R. Fox, A. Mohan, D.O. Malley, H. Viswanathan, N. Lubbers, Development of the Senseiver for efficient field reconstruction from sparse observations, Nat. Mach. Intell. 5 (2023) 1317–1325, https://doi.org/10.1038/ s42256-023-00746-x.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

- 数据来源单一：只在再入舱 CFD/仿真物理场上验证，缺真实风洞或飞行传感器数据。
- 场景范围有限：流动条件只有 Ma、攻角、高度三个参数，复杂非定常姿态或局部激波/分离未覆盖。
- 多源相关性假设：压力与热流相关性在本例成立，但对更多物理场或强非平衡热化学未必稳定。
- 噪声模型简化：随机噪声不能完全代表传感器漂移、滞后、失效和热防护安装误差。
- 误差指标解释：E(P)、E(T) 为无量纲综合误差，工程可接受阈值需进一步解释。
- 图像复核：POD 模态、传感器位置和重构误差热点必须查 PDF。

## 17. 可复用资产

- 选题资产：从“传感器数量受限”切入，提出多源信息共享。
- 方法资产：POD 降维 + RBFNN 快速映射 + DE 优化位置/类型。
- 理论资产：用 rank/observability 解释最少传感器数，避免纯经验调参。
- 图表资产：方法示意图、最少传感器流程图、POD 模态图、误差-传感器数量曲线、最优位置图、噪声鲁棒性图。
- 结果表达资产：用“相同精度减少数量”和“相同数量降低误差”两个维度表达优势。

## 18. 对我写论文的启发

多源/多物理场论文要先证明“为什么可以共享信息”。本文用相同 flow conditions 和 rank 分析提供了一个很干净的逻辑支点。若只说“多源数据更丰富”，说服力会弱很多。

另一个启发是结果对比要公平：作者既比较同等精度下传感器数，也比较同等传感器数下误差，这比只报一个百分比提升更稳。

## 19. 最终浓缩

最值得学习：把多物理场重构从“各自传感器各自重构”改写成“多源测量共享输入”，并用可观测性理论解释最少传感器数。

最大风险：验证仍是单一再入舱仿真案例，真实多源传感器噪声、安装误差和非定常复杂流动尚未充分覆盖。

可迁移三点：

1. 用 single-source 公式和 multi-source 公式并排展示问题重定义。
2. 用理论最小数量 + 优化结果一致性增强方法可信度。
3. 从数量、误差、位置物理意义和噪声鲁棒性四个角度组织结果。
