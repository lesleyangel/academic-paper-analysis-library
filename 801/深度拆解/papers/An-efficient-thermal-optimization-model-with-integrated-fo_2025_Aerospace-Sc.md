## 0. 读取说明

本文依据 `801/文本/txt/An-efficient-thermal-optimization-model-with-integrated-fo_2025_Aerospace-Sc.txt` 的全文抽取进行拆解。抽取文本包含摘要、结构路径设计、变量分层、遗传算法、RBF 代理筛选、算例边界条件、约束、质量/气动弹性影响优化结果和结论。部分路径图、温度/应力/位移云图、拓扑演化图需要依赖 PDF 视觉检查，本文均标注“需要 PDF 图像复核”。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 The integrated heat-force path and fully decomposed variable hierarchies, 3 Hybrid genetic optimization algorithm and population reduction method, 4 The ground path and optimization model, 5 Results and discussions, 6 Conclusions。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：An efficient thermal optimization model with integrated force paths, fully-decomposed hierarchies and hybrid genetic operations for a flight wing
- 期刊：Aerospace Science and Technology, 158 (2025) 109950
- 作者：Jian-Jun Gou, Hao-Dong Niu, Shu-Zhen Jia, Jia-Xin Hu, Xiao-Wei Wang, Chun-Lin Gong
- 关键词：High speed vehicle; Thermal optimization; Hybrid optimization; Heat-force integration

论文身份是面向高速飞行器机翼热防护/承载一体化路径的结构优化方法论文。它不只是优化隔热厚度或单一热传导路径，而是把“热传输路径”和“I 型力传输路径”预设计为集成路径，再通过多层级变量和混合遗传操作优化质量与气动弹性影响。

## 2. 摘要与核心信息提取

摘要信息可以归纳为四句话：

1. 高速飞行器机翼热防护系统轻量化是关键问题，而热路径与力路径一体化有潜力。
2. 现有热优化面对热/力传递路径不一致、多层级变量混杂等问题，优化复杂度高。
3. 本文预设计 I 型力路径，并在其两侧布置矩形热传输路径，提出 topology、angle、heat width、force width、width factor、height factor 六层级完全分解变量。
4. 通过二进制/Gray 编码混合遗传操作和 RBF 代理预筛选，最终实现质量降低 35.7%、气动弹性影响降低 19.3%。

核心定位：它是一篇“路径结构 + 变量编码 + 优化效率”的方法论文，目标是让热-力集成路径在实际翼结构优化中更轻、更可算。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/An-efficient-thermal-optimization-model-with-integrated-fo_2025_Aerospace-Sc.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/An-efficient-thermal-optimization-model-with-integrated-fo_2025_Aerospace-Sc.md`。

中文译文：

> 热系统轻量化是高速车辆的关键问题，而热力传递路径的集成优化是最有前途的技术之一。然而，不一致的传输路径和多层次变量导致了复杂且耗时的优化问题。在这项工作中，为高速机翼预先设计了在力网两侧具有I型力路径和矩形热传输路径的集成路径。为了形成大的优化空间，将变量充分分解为拓扑、角度、热宽度、力宽度、宽度因子和高度因子六个层次，并补充二、三、五层次模型来验证其对优化性能的增强效果。由于多个层次之间错综复杂的相关性，提出了一种基于遗传算法的混合策略来代替传统的顺序策略，其中采用二进制编码方案来统一描述离散变量和连续变量，并在遗传优化过程中同时操作不同层次的选择、交叉和变异。
>
> 针对多变量层次导致的种群规模过大和优化成本高等问题，基于RBF神经网络代理模型对个体的预评价和筛选，构建了一种有效损失有限的种群缩减方法。最后以最小质量和最小气动弹性影响量为目标对机翼进行了优化，分别达到了35.7%和19.3%的大幅目标降低，验证了模型的有效性。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

高速飞行器翼面同时承受强气动热和气动力。传统设计中，热防护层、承力结构和热传输构件往往分开设计，容易出现重量冗余：热路径只管降温，力路径只管承载，二者没有共享结构功能。若能让热流和力流在翼内沿集成路径传递，则可能用更少材料同时满足温度、应力、位移和气动弹性约束。

选题的难点在于集成路径并不是一个简单几何变量。路径是否存在、路径角度、热路径宽度、力路径宽度、相对位置和截面比例同时影响温度场、应力场和刚度场。变量既有离散拓扑，也有连续尺寸；既有热设计变量，也有结构设计变量。若直接用传统 GA 或单层级拓扑优化，搜索空间会很大，且容易出现编码混乱。

因此本文的选题本质是：在高速机翼热-力耦合约束下，如何把复杂路径设计转化为可编码、可搜索、可高效筛选的优化问题。这个切口比“提出一种热路径”更进一步，因为它关心路径结构如何被系统优化。

## 4. 领域位置与文献版图

文献版图大致包括三类：

第一类是高速飞行器热防护与热管理设计。这些研究提供问题背景：气动热通量高、热防护重量大、局部热集中严重。

第二类是热路径或高导热通道设计。它们说明用高导热材料把热量从热点转移到热沉可以降低温度，但多数研究偏热传导目标，未充分集成承载路径。

第三类是结构优化和遗传算法。这里涉及拓扑优化、多层级变量、混合编码、代理模型和种群筛选。本文借用 GA 的全局搜索能力，同时用 RBFNN 降低昂贵仿真调用次数。

本文的位置在三者交叉处：用结构优化的语言组织热-力集成路径，用热防护问题定义约束，用代理筛选和混合编码提高效率。

## 5. Gap 制造机制

本文制造 gap 的方式是强调“路径不一致”和“变量层级不清”。

一方面，热路径和力路径若独立设计，会产生材料重复和传递效率低的问题。热流要去热沉，力流要去力轴，两者在翼内方向和截面需求不同，若没有集成设计，就难以兼顾轻量化与多物理约束。

另一方面，集成路径的设计变量并非同质变量。拓扑是路径是否存在；角度决定路径方向；热宽和力宽分别影响导热和承载；宽度因子和高度因子决定截面耦合形态。若把这些变量混在一个粗粒度编码里，优化器难以有效搜索。作者通过 two/three/five hierarchy 对比证明，层级越充分分解，优化结果越好。

第三个 gap 是计算效率。热-力-结构路径每个候选都要有限元/热分析，单纯大种群 GA 成本高。本文引入 RBF 代理预评估，删除 50% 低适应度个体，以保持类似精度同时降低仿真次数。

## 6. 创新性判断

较强创新点：

- 提出 I 型力路径与两侧矩形热传输路径的集成热-力路径预设计，用于翼面热/力共同传递。
- 将变量完全分解为六个层级：topology、angle、heat width、force width、width factor、height factor，使复杂路径优化可编码。
- 用二进制与 Gray 编码混合处理离散/连续变量，并在 GA 中对各变量段执行遗传操作。
- 引入 RBFNN 代理预筛选种群，保留高潜力个体、降低直接仿真量。

中等创新点：

- 通过 two/three/five hierarchy 对比，证明变量细分对质量和气动弹性影响优化有实际收益。
- 同时以结构质量和 aeroelastic influence 为目标/评价指标，展示热-力集成路径不只影响温度和强度。

创新边界：

- 集成路径形态是预定义的 I 型/矩形路径，并非完全自由拓扑。
- GA 与 RBFNN 都是已有算法，创新在组合和问题适配。
- 算例集中于单一翼面、单一飞行条件和一组材料设定。

## 7. 论证链条复原

全文论证链可复原如下：

1. 高速机翼轻量热防护需要同时管理热流和力流。
2. 热路径与力路径分离会带来传递路径不一致和重量冗余。
3. 预设计 I 型力路径 + 两侧矩形热路径可以把热传输和力传递集成在同一结构单元内。
4. 集成路径包含多种层级变量，必须充分分解，否则优化器无法有效表达设计空间。
5. 二进制/Gray 混合编码可同时处理路径拓扑和连续尺寸变量。
6. RBFNN 预筛选可减少昂贵仿真次数，同时保持种群搜索能力。
7. 在机翼算例中，五层级/六变量分解优于二层级和三层级。
8. 集成路径质量优化相对初始合格路径降低 35.7%，气动弹性影响降低 19.3%。
9. 与 force-only 路径相比，集成路径还能通过减少隔热需求降低系统总质量。

这条链条用“路径设计合理性 + 变量层级必要性 + 算法效率 + 工程结果”构成闭环。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：The surface thermal radiation can only dissipate part of the heat, and it is essential to manage the considerable heat that enters the airframe, especially the heat in high-temperature regions that needs to be transported to low-temperature regions within a very short time.
- 已有研究不足/GAP：However, the inconsistent transfer paths and multi-hierarchy variables lead to a complex and time-consuming optimization problem. To address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by RBF neural network surrogate model. However, the inconsistent transfer paths and multi-hierarchy variables lead to a complex and time-consuming optimization problem.
- 本文解决方式：In order to form a great optimization space, the variable is fully decomposed into six hierarchies of topology, angle, heat width, force width, width factor and height factor, and the two-, threeand five-hierarchy models are supplemented to verify its enhancing effect on the optimization perfor mance. Due to the intricate relevance among multiple hierarchies, a hybrid strategy based on the genetic al gorithm is developed instead of the conventional sequential strategy, in which a binary coding scheme is adopted to uniformly describe the discrete and continuous variables, and the selection, crossover and mutation of different hierarchies are operated simultaneously during the genetic optimization. To address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by RBF neural network surrogate model.
- 学术或工程增量：需结合 Results/Conclusion 的量化结果复核。
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

结构对象是一个高速飞行翼：根弦 1000 mm，尖弦 360 mm，展长 540 mm。外部气动热和压力由 Fluent 在 4 Ma、攻角 10°、高度 15 km 条件下计算，热流在迎风面约 350 kW/m2，背风面约 10 kW/m2，前缘约 1200 kW/m2；压力迎风面约 35 kPa、背风面约 5 kPa、前缘约 65 kPa。

集成路径设计包括：

- force path：I 型力传输路径，材料为铝合金，承担力传递。
- heat path：布置在力路径 web 两侧的矩形 C/C 高导热路径，负责热量输运。
- insulation：隔热层，材料密度和导热率较低，控制温度。

变量层级包括：

- `XT`：拓扑变量，决定候选路径是否存在。
- `XA`：角度变量，决定路径方向。
- `XW`：力路径宽度。
- `XWH`：热路径宽度。
- `XWF`：宽度因子，`XWF=XWW/XW`。
- `XHF`：高度因子，`XHF=XHH/H`。

算法采用混合遗传操作：

- 拓扑用二进制编码，连续变量用 Gray 编码。
- 选择方式为 stochastic universal sampling，选择压力 SP=2。
- 交叉为单点交叉，概率 0.8。
- 变异为 simple mutation，概率与染色体长度相关。
- RBFNN 代理先预测适应度，删除 50% 低适应度个体，再对保留个体做真实路径分析。

约束包括最高温度不超过 550 K，平均温度不超过 450 K，应力不超过 225 MPa，位移不超过 27 mm。优化目标包括总质量和 aeroelastic influence，后者定义为弹性升力曲线斜率与刚性升力曲线斜率之差。

## 9. 证据系统与 Claim-Evidence 表

| Claim | Evidence | 论证功能 | 潜在限制 |
|---|---|---|---|
| RBF 预筛选能显著减少计算成本 | force-only 五层级中 O40 benchmark 质量 0.646；O40-R20 质量 0.647，仅高 0.2%，总仿真次数 3000 vs 6000，成本降低 50% | 证明代理筛选效率高且损失小 | 代理误删优秀个体的风险未系统量化 |
| 变量层级越充分，质量优化越好 | force-only 质量优化中五层级最终 0.65，二层级 0.95，三层级 0.77；五层级分别降低 31.6% 和 15.6% | 支撑“fully-decomposed hierarchies”的必要性 | 对比是否完全公平需看变量总数和约束设置 |
| 集成路径质量优化有效 | integrated mass optimization 中质量从首个合格路径 2.80 kg 降至 1.80 kg，相对首个合格路径降低 35.7%，相对 Ground 3.14 kg 降低 42.7% | 证明方法能在热/力约束下显著减重 | 单一工况，结果对热边界敏感 |
| 约束被主动利用而非保守满足 | 最终 Tmax 接近 550 K，应力近固定端接近 225 MPa，翼尖位移小于 27 mm | 说明优化结果逼近约束边界，材料利用率高 | 需要云图复核局部热点和应力集中 |
| aeroelastic influence 优化也受益于分层变量 | force-only 中五层级 aeroelastic influence 从 9.37% 降到 5.85%，二/三/五层级最终为 6.62%、6.24%、5.85% | 支撑变量分解不只改善质量目标 | aeroelastic influence 是简化指标 |
| integrated path 可降低气动弹性影响 | integrated aeroelastic optimization 从首个合格路径 6.24% 降至 5.18%，降低 19.3% | 证明热-力路径能影响结构刚度和气动弹性行为 | 未展示完整颤振/动态响应 |
| 集成热-力设计可降低总系统质量 | force-only 加隔热后总质量约 1.94-3.40 kg；integrated path 约 1.86 kg，降低 0.08-1.54 kg | 证明集成热路径减少额外隔热负担 | 隔热厚度和温度目标设定影响大 |

## 10. 图表、公式与结果叙事提取

| 类型 | 内容 | 论证功能 | 复核备注 |
|---|---|---|---|
| Wing geometry 图 | 根弦 1000 mm、尖弦 360 mm、展长 540 mm 的翼面模型 | 定义优化对象 | 需要 PDF 图像复核 |
| Integrated path 示意图 | I 型力路径 + 两侧矩形热路径 | 展示本文路径创新 | 需要 PDF 图像复核 |
| Eq. 1 | `XWF=XWW/XW`、`XHF=XHH/H` | 定义宽度/高度因子 | 公式符号需 PDF 核对 |
| 变量层级表 | topology、angle、heat width、force width、width factor、height factor | 说明 fully-decomposed hierarchies | 表格细节需复核 |
| 编码/遗传操作图 | 二进制/Gray 编码、选择、交叉、变异 | 说明算法如何处理混合变量 | 需要 PDF 图像复核 |
| RBF 预筛选流程图 | 代理预测适应度并删除 50% 个体 | 证明计算效率来源 | 需要 PDF 图像复核 |
| Fluent 热流/压力云图 | 4 Ma、AOA 10°、15 km 下热/力边界 | 提供真实载荷输入 | 云图细节需要 PDF 图像复核 |
| O40/O20/O40-R20 表 | 种群策略对质量和仿真次数的影响 | 证明代理筛选可行 | 数值来自文本抽取 |
| two/three/five hierarchy 对比图 | 不同层级下质量或 aeroelastic influence 收敛 | 证明变量分解收益 | 曲线需 PDF 图像复核 |
| Integrated mass 收敛图 | 质量从 2.80 到 1.80 kg 的三阶段下降 | 展示优化过程 | 曲线阶段需图像复核 |
| 温度/应力/位移云图 | Tmax、固定端应力、翼尖位移接近约束 | 证明最终设计满足多物理约束 | 需要 PDF 图像复核 |
| 路径拓扑演化图 | 第 8/37/150 代路径删除和保留情况 | 展示拓扑如何被优化 | 需要 PDF 图像复核 |

结果叙事是典型“算法有效性 -> 变量必要性 -> 工程设计收益”的三段式。作者先用种群策略证明 RBF 筛选不会明显牺牲结果，再用分层对比证明变量拆分有意义，最后展示集成路径在质量和 aeroelastic influence 上的最终收益。

## 11. 章节结构与篇章布局

文章结构可分为五大块：

1. Introduction：高速翼热防护轻量化、热-力路径集成潜力、现有优化难点。
2. Integrated heat-force path model：翼面、力路径、热路径、层级变量和材料设置。
3. Hybrid genetic optimization model：编码方式、遗传操作、RBF 预筛选和整体流程。
4. Numerical examples：载荷边界、约束、force-only 对比、integrated path 质量优化和 aeroelastic influence 优化。
5. Conclusions：总结质量降低、气动弹性影响降低和算法效率。

篇章布局偏“工程方法论文”：方法介绍较长，算例和结果占据主体。其中特别重视对比实验，包括种群策略对比、层级数量对比、force-only 与 integrated 对比。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.2: 2 The integrated heat-force path and fully decomposed variable hierarchies（对象/模块/过渡章节）
- L2 p.4: 3 Hybrid genetic optimization algorithm and population reduction method（方法/模型/算法）
  - L3 p.4: 3.1 Unified chromosome encoding of discrete and continuous variables（对象/模块/过渡章节）
  - L3 p.4: 3.2 Hybrid genetic operators of multi-hierarchy variables（对象/模块/过渡章节）
  - L3 p.6: 3.3 The population size reduction method（方法/模型/算法）
  - L3 p.6: 3.4 The optimization process（对象/模块/过渡章节）
- L2 p.7: 4 The ground path and optimization model（方法/模型/算法）
  - L3 p.7: 4.1 The ground path and numerical models（方法/模型/算法）
    - L4 p.7: 4.1.1 Ground path and mesh（对象/模块/过渡章节）
    - L4 p.7: 4.1.2 Governing equations（对象/模块/过渡章节）
    - L4 p.7: 4.1.3 Boundary conditions（对象/模块/过渡章节）
  - L3 p.7: 4.2 Mathematical description of optimization model（方法/模型/算法）
- L2 p.9: 5 Results and discussions（结果/验证/讨论）
  - L3 p.9: 5.1 The path mass minimum problem（问题定义）
    - L4 p.9: 5.1.1 The force-only path optimization（对象/模块/过渡章节）
    - L4 p.11: 5.1.2 The heat-force integrated path optimization（对象/模块/过渡章节）
  - L3 p.13: 5.2 The aeroelastic influence quantity minimum problem（问题定义）
    - L4 p.13: 5.2.1 The force-only path optimization（对象/模块/过渡章节）
    - L4 p.13: 5.2.2 The heat-force integrated path optimization（对象/模块/过渡章节）
  - L3 p.14: 5.3 Effectiveness of integrated path optimization（对象/模块/过渡章节）
- L2 p.15: 6 Conclusions（结论/贡献回收）
- L2 p.16: CRediT authorship contribution statement（尾部材料）
- L2 p.16: Declaration of competing interest（尾部材料）
- L2 p.16: Acknowledgments（尾部材料）
- L2 p.16: Data availability（尾部材料）
- L2 p.16: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 The integrated heat-force path and fully decomposed variable hierarchies | 2 | 2 | 对象/模块/过渡章节 |
| 3 Hybrid genetic optimization algorithm and population reduction method | 4 | 2 | 方法/模型/算法 |
| 3.1 Unified chromosome encoding of discrete and continuous variables | 4 | 3 | 对象/模块/过渡章节 |
| 3.2 Hybrid genetic operators of multi-hierarchy variables | 4 | 3 | 对象/模块/过渡章节 |
| 3.3 The population size reduction method | 6 | 3 | 方法/模型/算法 |
| 3.4 The optimization process | 6 | 3 | 对象/模块/过渡章节 |
| 4 The ground path and optimization model | 7 | 2 | 方法/模型/算法 |
| 4.1 The ground path and numerical models | 7 | 3 | 方法/模型/算法 |
| 4.1.1 Ground path and mesh | 7 | 4 | 对象/模块/过渡章节 |
| 4.1.2 Governing equations | 7 | 4 | 对象/模块/过渡章节 |
| 4.1.3 Boundary conditions | 7 | 4 | 对象/模块/过渡章节 |
| 4.2 Mathematical description of optimization model | 7 | 3 | 方法/模型/算法 |
| 5 Results and discussions | 9 | 2 | 结果/验证/讨论 |
| 5.1 The path mass minimum problem | 9 | 3 | 问题定义 |
| 5.1.1 The force-only path optimization | 9 | 4 | 对象/模块/过渡章节 |
| 5.1.2 The heat-force integrated path optimization | 11 | 4 | 对象/模块/过渡章节 |
| 5.2 The aeroelastic influence quantity minimum problem | 13 | 3 | 问题定义 |
| 5.2.1 The force-only path optimization | 13 | 4 | 对象/模块/过渡章节 |
| 5.2.2 The heat-force integrated path optimization | 13 | 4 | 对象/模块/过渡章节 |
| 5.3 Effectiveness of integrated path optimization | 14 | 3 | 对象/模块/过渡章节 |
| 6 Conclusions | 15 | 2 | 结论/贡献回收 |
| CRediT authorship contribution statement | 16 | 2 | 尾部材料 |
| Declaration of competing interest | 16 | 2 | 尾部材料 |
| Acknowledgments | 16 | 2 | 尾部材料 |
| Data availability | 16 | 2 | 尾部材料 |
| References | 16 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

引言段落节奏是：高速飞行器热问题 -> 轻量化需求 -> 热路径/力路径集成概念 -> 优化变量复杂 -> 本文方案。每段都在缩小问题范围。

方法段落多为定义型。作者先定义路径几何，再定义变量，再定义编码和 GA 操作。这样读者可以从物理结构逐步进入优化算法。

结果段落采用强对比节奏。几乎每个小节都回答一个问题：RBF 筛选是否省时？五层级是否必要？质量能降多少？气动弹性影响能降多少？集成路径相对 force-only 有何额外收益？这种问答式结构使复杂优化结果不至于散乱。

## 13. 文笔画像与语言习惯

本文语言偏工程优化论文，关键词高度重复：integrated path, hierarchy, hybrid genetic operation, mass reduction, aeroelastic influence, qualified path。句式上常用 “is proposed”, “is decomposed into”, “is optimized by”, “compared with”。

文笔特点：

- 喜欢用分层词汇组织复杂变量，如 hierarchy、fully-decomposed、topology、angle。
- 结果表达偏百分比化，突出 reduction。
- 对算法步骤使用过程性动词，如 encode, select, crossover, mutate, screen, analyze。
- 对路径结构使用强名词化表达，如 force path, heat transport path, integrated heat-force path。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：41867
- 高频词：path(117)；optimization(83)；heat(68)；width(52)；variables(38)；force(37)；mass(37)；thermal(36)；model(36)；population(31)；factor(30)；work(29)；variable(29)；paths(27)；individuals(27)；integrated(25)；hierarchies(25)；angle(22)；value(22)；generation(22)
- 高频名词化/学术名词：optimization(83)；population(31)；generation(22)；reduction(21)；temperature(18)；influence(17)；quantity(16)；fitness(13)；insulation(13)；function(10)；effectiveness(9)；pressure(9)；relevance(8)；conductivity(7)；mutation(7)
- 高频学术动词：optimized(6)；developed(5)；constructed(4)；reveal(4)；indicate(3)；indicated(3)；compared(3)；optimize(2)；provide(2)；achieved(2)；predicted(2)；evaluated(1)；evaluate(1)；presented(1)
- 高频形容词：thermal(36)；variable(29)；aerodynamic(19)；individual(16)；aeroelastic(15)；genetic(14)；different(14)；continuous(9)；total(9)；optimal(8)；objective(7)；displacement(7)；effective(6)；original(6)；essential(5)
- 高频副词：force-only(13)；especially(7)；finally(7)；fully(5)；simultaneously(5)；widely(5)；usually(3)；uniformly(3)；effectively(3)；separately(2)；closely(2)；relatively(2)；radiatively(2)；tively(2)；extremely(1)
- 高频二词短语：height factor(16)；integrated path(15)；width factor(14)；aeroelastic influence(14)；heat width(13)；influence quantity(13)；force width(12)；factor height(12)；insulation layer(12)；path optimization(11)；heat transport(10)；force path(10)
- 高频三词短语：aeroelastic influence quantity(13)；width factor height(12)；angle force width(8)；force width heat(8)；minimum aeroelastic influence(7)；thermal insulation layer(7)；lower upper limits(7)；heat transport path(5)；heat-force integrated path(5)；integrated path optimization(5)；variable fully decomposed(4)；fully decomposed six(4)
- 被动语态估计：155；`we + 动作动词` 主动句估计：0
- 一般现在时线索：276；一般过去时线索：355；现在完成时线索：0；情态动词线索：42

分章节正文词频：

- 1 Introduction: optimization(27)；heat(23)；path(23)；thermal(13)；hierarchies(10)；vehicles(8)；cooling(8)；variables(8)
- 2 The integrated heat-force path and fully decomposed variable hierarchies: path(22)；width(15)；heat(13)；optimization(12)；force(9)；variable(9)；height(7)；hierarchies(6)
- 3 Hybrid genetic optimization algorithm and population reduction method: population(19)；individuals(18)；width(17)；variables(14)；fitness(13)；individual(13)；model(12)；crossover(11)
- 4 The ground path and optimization model: path(20)；heat(18)；thermal(12)；force(11)；aerodynamic(11)；temperature(11)；maximum(10)；width(9)
- 5 Results and discussions: path(29)；optimization(22)；generation(22)；mass(14)；paths(13)；increases(11)；reduction(10)；force-only(9)
- 6 Conclusions: path(12)；optimization(9)；mass(9)；quantity(7)；minimum(6)；aeroelastic(6)；influence(6)；integrated(4)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

可复用关键词：

- integrated heat-force path
- fully-decomposed hierarchies
- hybrid genetic operation
- radial path
- heat transport path
- force transmission path
- RBF surrogate pre-evaluation
- qualified path
- aeroelastic influence
- lightweight thermal protection system

可复用句式：

- “The optimization difficulty originates from the coexistence of discrete topology variables and continuous geometric variables.”
- “To improve the search efficiency, the design variables are fully decomposed into several hierarchical groups.”
- “A surrogate pre-evaluation strategy is used to filter out low-fitness individuals before expensive numerical analyses.”
- “The optimized design tends to approach the active constraints, indicating a higher utilization of structural and thermal capacity.”
- “Compared with the force-only design, the integrated heat-force path reduces the additional insulation demand.”

中文可复用表达：

- “热路径和力路径的一体化不是简单并置，而是让导热能力与承载能力共享结构体积。”
- “变量层级拆分的意义在于把优化器看不见的工程结构逻辑显式编码进染色体。”

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：The surface thermal radiation can only dissipate part of the heat, and it is essential to manage the considerable heat that enters the airframe, especially the heat in high-temperature regions that needs to be transported to low-temperature regions within a very short time.
  可迁移模板：The surface thermal radiation can only dissipate part of the heat, and it is essential to manage the considerable heat that enters the airframe, especially the heat in high-temperature regions that needs to be transported to low-temperature regions within a very short time.
- 原句：A large number of gray elements with median values will be created in such optimization process, thus very complex post-processing is essential.
  可迁移模板：A large number of gray elements with median values will be created in such optimization process, thus very complex post-processing is essential.
- 原句：Thus, a fast and effective genetic optimization algorithm with well individual screening and population size reduction strategy is essential.
  可迁移模板：Thus, a fast and effective genetic optimization algorithm with well individual screening and population size reduction strategy is essential.
#### Gap/转折句
- 原句：However, the inconsistent transfer paths and multi-hierarchy variables lead to a complex and time-consuming optimization problem.
  可迁移模板：However, the inconsistent transfer paths and multi-hierarchy variables lead to a complex and time-consuming optimization problem.
- 原句：To address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by RBF neural network surrogate model.
  可迁移模板：To address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by METHOD neural network surrogate model.
- 原句：However, the inconsistent transfer paths and multi-hierarchy variables lead to a complex and time-consuming optimization problem.
  可迁移模板：However, the inconsistent transfer paths and multi-hierarchy variables lead to a complex and time-consuming optimization problem.
- 原句：To address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by RBF neural network surrogate model.
  可迁移模板：To address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by METHOD neural network surrogate model.
- 原句：However, the high den sity and low service temperature of above metal-based composites lead to their limited application in flight vehicles.
  可迁移模板：However, the high den sity and low service temperature of above metal-based composites lead to their limited application in flight vehicles.
#### 方法提出句
- 原句：In order to form a great optimization space, the variable is fully decomposed into six hierarchies of topology, angle, heat width, force width, width factor and height factor, and the two-, threeand five-hierarchy models are supplemented to verify its enhancing effect on the optimization perfor mance.
  可迁移模板：In order to form a great optimization space, the variable is fully decomposed into six hierarchies of topology, angle, heat width, force width, width factor and height factor, and the two-, threeand five-hierarchy models are supplemented to verify its enhancing effect on the optimization perfor mance.
- 原句：Due to the intricate relevance among multiple hierarchies, a hybrid strategy based on the genetic al gorithm is developed instead of the conventional sequential strategy, in which a binary coding scheme is adopted to uniformly describe the discrete and continuous variables, and the selection, crossover and mutation of different hierarchies are operated simultaneously during the genetic optimization.
  可迁移模板：Due to the intricate relevance among multiple hierarchies, a hybrid strategy based on the genetic al gorithm is developed instead of the conventional sequential strategy, in which a binary coding scheme is adopted to uniformly describe the discrete and continuous variables, and the selection, crossover and mutation of different hierarchies are operated simultaneously during the genetic optimization.
- 原句：To address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by RBF neural network surrogate model.
  可迁移模板：To address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by METHOD neural network surrogate model.
- 原句：Finally, the wing is optimized with objectives of the minimum mass and minimum aeroelastic influence quantity, and the model effectiveness is verified by the great objective reductions of 35.7 % and 19.3 %, respectively.
  可迁移模板：Finally, the wing is optimized with objectives of the minimum mass and minimum aeroelastic influence quantity, and the model effectiveness is verified by the great objective reductions of X and X, respectively.
- 原句：In order to form a great optimization space, the variable is fully decomposed into six hierarchies of topology, angle, heat width, force width, width factor and height factor, and the two-, threeand five-hierarchy models are supplemented to verify its enhancing effect on the optimization perfor mance.
  可迁移模板：In order to form a great optimization space, the variable is fully decomposed into six hierarchies of topology, angle, heat width, force width, width factor and height factor, and the two-, threeand five-hierarchy models are supplemented to verify its enhancing effect on the optimization perfor mance.
#### 结果呈现句
- 原句：For the continuous opti mization [35–38], a density-like variable with value between 0 and 1 is used to represent the path presence or absence, and the value close to 1 indicates the presence while close to 0 indicates the absence.
  可迁移模板：For the continuous opti mization [X–X], a density-like variable with value between Xand Xis used to represent the path presence or absence, and the value close to Xindicates the presence while close to Xindicates the absence.
- 原句：After the topology optimization, the optimization of additional hierarchies, e.g., the path profile size and shape should be further conducted to obtain better results.
  可迁移模板：After the topology optimization, the optimization of additional hierarchies, e.g., the path profile size and shape should be further conducted to obtain better results.
- 原句：However, the population should contain plentiful enough individuals to acquire optimal results, thus the population size is always large and leads to enormous computational cost, especially for problems with variables of multiple hierarchies.
  可迁移模板：However, the population should contain plentiful enough individuals to acquire optimal results, thus the population size is always large and leads to enormous computational cost, especially for problems with variables of multiple hierarchies.
- 原句：Some conclusions are obtained: (1) The fully-decomposed variable hierarchy results into great opti mization performance.
  可迁移模板：Some conclusions are obtained: (X) The fully-decomposed variable hierarchy results into great opti mization performance.
#### 贡献/增量句
- 原句：For high-speed flight vehicles, the integrated heat-force design can improve the path effi ciency and reduce the system mass in theory.
  可迁移模板：For high-speed flight vehicles, the integrated heat-force design can improve the path effi ciency and reduce the system mass in theory.
#### 限制/边界句
- 原句：To address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by RBF neural network surrogate model.
  可迁移模板：To address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by METHOD neural network surrogate model.
- 原句：The surface thermal radiation can only dissipate part of the heat, and it is essential to manage the considerable heat that enters the airframe, especially the heat in high-temperature regions that needs to be transported to low-temperature regions within a very short time.
  可迁移模板：The surface thermal radiation can only dissipate part of the heat, and it is essential to manage the considerable heat that enters the airframe, especially the heat in high-temperature regions that needs to be transported to low-temperature regions within a very short time.
- 原句：To address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by RBF neural network surrogate model.
  可迁移模板：To address the excessive population size and high optimization cost caused by multiple variable hierarchies, an efficient population reduction method with limited effectiveness loss is constructed based on the individual pre-evaluation and screening by METHOD neural network surrogate model.
- 原句：However, the high den sity and low service temperature of above metal-based composites lead to their limited application in flight vehicles.
  可迁移模板：However, the high den sity and low service temperature of above metal-based composites lead to their limited application in flight vehicles.
- 原句：However, the heat and force path are closely dependent on aerodynamic heat and pressure distributions, respectively, thus the efficient integrated path should be obtained based on massive calculations and corresponding optimizations.
  可迁移模板：However, the heat and force path are closely dependent on aerodynamic heat and pressure distributions, respectively, thus the efficient integrated path should be obtained based on massive calculations and corresponding optimizations.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

本文引用策略围绕三个支撑点展开：

1. 高速飞行器热防护文献：证明轻量热设计是重要问题。
2. 热路径/热传输结构文献：证明高导热路径能够降低热集中，但现有工作与承力路径集成不足。
3. 优化算法文献：证明 GA、Gray 编码、代理模型和多层级变量处理有方法基础。

引用的主要功能不是铺陈全部历史，而是为本文的三个关键词提供合法性：integrated path 为什么需要，fully-decomposed hierarchy 为什么合理，hybrid genetic operation 为什么可行。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：62
- Introduction 引文簇数量估计：18
- References 条目数：46
- 可识别年份条目数：45
- 2021 年及以后文献数：15
- 2010 年前经典文献数：12
- 同刊引用数（按 subject 粗匹配）：1
- 高频来源期刊：Aerospace Science and Technology(1)
- 引文簇样例：[1], [2,3], [4], [5], [6,7], [8,9], [10], [14], [15,16], [17,18], [19], [23,24]

带引文的 gap/转折句样例：

- Such Ground path method is widely used in the optimization of beam- and truss-type force-bearing struc tures [39,40], while the application in heat path and heat-force inte grated path is very limited.
- However, the mutual influence among different hierarchies of variables is not considered in such sequential optimization method, and the so-called hybrid optimization method is a more effective alternate [41,42].

References 解析样例（前 8 条）：

- [1] J. Liu, X. Zhou, H. xin, High-Si reinforced Al matrix composites prepared by powder semi-solid squeeze, J. Alloys Compd. 726 (2017) 772–778.
- [2] J. Xie, J. Ma, M. Liao, W. Guo, L. Huang, P. Gao, H. Xiao, Reinforcement of thermally-conductive SiC/Al composite with 3D-interpenetrated network structure by various SiC foam ceramic skeletons, Ceram. Int. 47 (2021) 30869–30879.
- [3] Z. Zhang, Z. Wei, Z. Li, B. Hou, R. Xue, H. Xia, Z. Shi, SiC honeycomb reinforced Al matrix composite with improved tribological performance, Ceram. Int. 47 (2021) 23376–23385.
- [4] C. Yan, W. Lifeng, R. Jianyue, Multi-functional SiC/Al composites for aerospace applications, Chin. J. Aeronaut. 21 (2008) 578–584.
- [5] Z. Shen, G. Ji, J.-F. Silvain, From 1D to 2D arrangements of graphite flakes in an aluminium matrix composite: impact on thermal properties, Scr. Mater. 183 (2020) 86–90.
- [6] C. Zhang, R. Wang, Z. Cai, C. Peng, Y. Feng, L. Zhang, Effects of dual-layer coatings on microstructure and thermal conductivity of diamond/Cu composites prepared by vacuum hot pressing, Surf. Coat. Technol. 277 (2015) 299–307.
- [7] E.A. Ekimov, N.V. Suetin, A.F. Popovich, V.G. Ralchenko, Thermal conductivity of diamond composites sintered under high pressures, Diam. Relat. Mater. 17 (2008) 838–843.
- [8] Q. Cui, C. Chen, C. Yu, T. Lu, H. Long, S. Yan, A.A. Volinsky, J. Hao, Effect of molybdenum particles on thermal and mechanical properties of graphite flake/ copper composites, Carbon. N. Y. 161 (2020) 169–180.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. 路径形态预设风险：I 型力路径和矩形热路径可能限制设计空间，未必代表真正最优拓扑。
2. 单一工况风险：4 Ma、10° AOA、15 km 的热/力边界不能代表完整飞行包线。
3. 代理筛选风险：RBF 删除 50% 低适应度个体可能在早期误删潜在优秀拓扑，尤其适应度面多峰时。
4. 随机优化稳定性风险：GA 结果是否对随机种子、种群大小、变异率敏感，文中未充分展示多次运行统计。
5. aeroelastic influence 指标简化：只用升力曲线斜率差可能不足以代表完整气动弹性安全性，如颤振、瞬态响应等。
6. 制造实现风险：复杂内嵌热-力路径的制造、连接和热接触可靠性需要额外工程验证。

## 17. 可复用资产

可复用问题拆法：

- 将复杂多物理结构优化拆成“物理路径设计”和“变量层级设计”两件事。
- 先预设计一个工程可制造的路径单元，再围绕该单元做拓扑和尺寸优化。
- 用代理模型筛选候选，而不是直接替代最终仿真，以降低审稿人对代理精度的担忧。

可复用验证矩阵：

- 种群策略对比：大种群、小种群、代理筛选种群。
- 层级变量对比：二层级、三层级、五/六层级。
- 目标对比：质量目标、气动弹性影响目标。
- 结构策略对比：force-only 与 integrated heat-force。
- 约束检查：温度、平均温度、应力、位移。

可复用图表：

- 变量编码图。
- 优化流程图。
- 收敛曲线。
- 约束云图。
- 拓扑演化图。

## 18. 对我写论文的启发

这篇论文的一个重要启发是：优化论文的创新可以来自“如何表达设计空间”。很多时候算法本身不是新的，但如果变量分解能显著改善工程搜索能力，仍然可以构成有效贡献。

第二个启发是要给效率方法设计公平对比。作者没有只说 RBF 筛选快，而是用 O40、O20、O40-R20 对比说明“同等大种群效果 + 半数仿真次数”。这种对比比单独报时间更有说服力。

第三个启发是多物理结构优化要展示约束利用。最终结果的温度、应力、位移接近但不超过限制，说明优化不是保守减重，而是在约束边界附近寻找设计。

## 19. 最终浓缩

本文提出一种高速飞行翼热-力集成路径优化模型：以 I 型力路径和两侧矩形热路径为基础，将路径拓扑、角度、热宽、力宽、宽度因子和高度因子分解为多层级变量，并用二进制/Gray 混合遗传算法和 RBF 代理预筛选提升搜索效率。算例显示，充分变量分解优于二层级/三层级设计，代理筛选可在几乎不损失质量结果的情况下减少约 50% 仿真量。最终集成路径相对首个合格路径质量降低 35.7%，气动弹性影响降低 19.3%，并相对 force-only 方案减少额外隔热需求。论文的核心价值是把热路径与力路径的一体化设计变成一个可编码、可优化、可验证的工程流程。
