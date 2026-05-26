# A novel mechanical-thermal-electrical thermal protection system concept and its multi-scale performance evaluation for hypersonic launch vehicles

## 0. 读取说明

本拆解基于 `801/文本/txt/A-novel-mechanical-thermal-electrical-thermal-protection-syste_2021_Composit.txt` 的全文抽取结果。抽取文本能确认题名、摘要、章节、材料、模型流程、主要数值结论和图表标题；但 Fig. 7-Fig. 16 中大量云图、曲线、节点位置和颜色分布只能从文字说明间接判断，涉及空间位置、色标和局部极值的细节均标注为“需要 PDF 图像复核”。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 The vehicle and the MTPS, 3 Numerical model, 4 Results and discussions, 5 Conclusion。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：A novel mechanical-thermal-electrical thermal protection system concept and its multi-scale performance evaluation for hypersonic launch vehicles
- 作者：Ge Gao, Jian-Jun Gou, Chun-Lin Gong, Jia-Xin Hu, Rui-Chao Gao
- 期刊与年份：Composite Structures, 268, 2021, 113962
- 机构：Northwestern Polytechnical University, School of Astronautics
- 领域：高超声速飞行器热防护系统、多功能结构、热电转换、有限元多尺度分析
- 论文类型：工程概念设计 + 多尺度数值模拟 + 热-力-电性能评估
- 研究对象：安装在高超声速运载器二级压缩面的 MTPS，宏观为 8 块 MTPS plate，细观为 288 个 MTPS unit。
- 方法组合：整机载荷分析、MTPS 板级位移边界插值、MTPS 单元热-力耦合有限元、热电输出后处理。
- 主要证据：整机/板/单元三级应力云图，单元温度场，TE 材料节点温度与应力曲线，电性能曲线，质量与电输出表格。

这篇论文的身份不是单纯材料性能论文，而是“把热防护结构变成能承载、隔热、发电的系统方案”的工程构型论文。它的贡献重心在概念完整性和边界条件传递，而非单个热电材料性能刷新。

## 2. 摘要与核心信息提取

摘要的说服结构很清楚：先指出 MTPS 具有热电转换和承载附加功能；再说明该概念在宏观上是板、在细观上是单元；然后把单元拆成 TE module 与 gap TPS；最后用多尺度分析证明载荷边界准确性和三功能可行性。

一句话主张：作者提出一种包含两级 TE 层、承载框架、蜂窝芯、嵌入导电片和低模量胶层的机械-热-电一体化热防护系统，并用整机-板-单元多尺度有限元证明它可同时承担承载、隔热和供电功能。

核心信息：

- 问题：传统 TPS 只耗散或阻挡气动热，无法复用热能，且既有 TE-TPS 结构细节和气动力载荷考虑不足。
- 方法：将整机气动力/热流映射到 MTPS plate，再把 plate 位移边界传给 unit，形成更真实的单元级热-力边界。
- 创新：两级高温/中温 TE 层、细观结构完整化、热应力释放设计、多尺度位移边界传递。
- 主要结果：单元平均输出功率 0.88 W、平均转换效率 0.51%，整套 288 单元约 253.44 W；TE 转换效率相对前作从 0.237% 提高到 0.51%。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/A-novel-mechanical-thermal-electrical-thermal-protection-syste_2021_Composit.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/A-novel-mechanical-thermal-electrical-thermal-protection-syste_2021_Composit.md`。

中文译文：

> 本文为高超音速运载火箭开发了一种具有热电（TE）转换和承载附加功能的多功能热保护系统（MTPS）概念。这个概念是宏观尺度上的板块和中尺度上的单位。介观单元由TE模块和TPS间隙组成。 TE模块由氧化铝陶瓷层和纤维隔热层组成，用于消散一定量的气动热；高温和中温TE层，用于将气动热有效地转化为电能；承载框架和蜂窝芯，以提高承载能力；TE材料中嵌入导电板和低模量高温粘合剂，以缓解热应力。基于飞行器、MTPS板和MTPS单元的多尺度分析，评估了MTPS的机械热电性能，并建立了不同尺度之间机械边界条件的传递方法。结果表明，多尺度分析对于保证边界条件的准确性至关重要，所开发的MTPS概念具有承载、热防护和供电等多重有效功能。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题来自三个工程矛盾叠加。第一，Hypersonic launch vehicle 面临强气动热，TPS 是刚需；第二，传统 TPS 的热是被浪费的，从能源利用角度低效；第三，热电模块可以复用热，但如果直接贴到 TPS 上，会引入结构承载、热应力集中、边界条件失真等问题。

作者把大问题收束为一个可建模问题：在一个特定高超声速运载器二级压缩面上，设计一个可装配的 MTPS unit，并在整机真实载荷路径下验证它的机械、热和电性能。这个收束很有效，因为它避免泛泛讨论“热电热防护是否有前途”，而是把问题转成：几何、材料、边界、热流、应力、电输出能否闭合。

选题价值主要是工程价值和方法价值：工程上尝试把 TPS 从“被动防热”升级为“承载 + 防热 + 供电”；方法上强调多尺度边界传递，回应很多单胞分析只用简化边界的问题。它也有明显应用牵引：如果数百瓦级热电输出成立，可替代部分机载电源，节省内部空间。

## 4. 领域位置与文献版图

Introduction 的文献版图按系统类型组织，而不是按时间线组织：

- ITPS：能兼顾承载与热防护，但存在 thermal short-circuit effect。
- ATPS：主动冷却能力强，但需要冷却剂和复杂附属系统，成本高。
- UHTC：适合最严苛热载荷位置，但韧性不足。
- Ablative TPS：可带走热量，但一次性使用且改变外形。
- TE conversion/TE generator：可回收热能，已有多级 TE、三维耦合模型和高超声速应用探索。
- 作者前作：已有 TE module-based MTPS，但仅一级高温 TE、细节不足、热力分析未考虑气动力载荷。

本文站位是“继承前作 + 修正边界 + 完整化结构”。它不是推翻 ITPS/ATPS，而是把它们的不足转化为本文 gap：既有系统缺热复用，既有 TE-TPS 缺细观结构和真实载荷链。

## 5. Gap 制造机制

作者制造 gap 的方式很典型：先列出传统 TPS 类型并逐项指出局限，再转向 TE 技术的机会，最后回到作者前作的三个不足。

关键 gap：

- 功能 gap：现有 TPS 多数只防热或冷却，不能复用气动热。
- 结构 gap：前作三层结构只示意，没有导电片、承载框、蜂窝芯、胶层等可装配细节。
- 性能 gap：单级高温 TE 层导致转换效率偏低。
- 边界 gap：前作热机械分析只考虑热应力，没有考虑气动力载荷及其从整机到单元的传递。

这个 gap 比较可信，因为作者没有只说“缺少 MTPS”，而是把“为什么前作还不够”拆成结构、效率、载荷三个可验证维度。风险在于文献对“最接近的多功能 TPS/TE-TPS”覆盖可能仍偏向作者团队体系，需复核是否遗漏同期多级 TE/TPS 方案。

## 6. 创新性判断

作者声明的创新主要有三项：两级 TE 层提高效率；细观结构细节被纳入；嵌入导电片和低模量胶层等热应力释放设计。另一个隐含创新是多尺度边界传递方法。

真实创新判断：

- 构型创新：中等偏强。把 TE layer、load-bearing frame、honeycomb cores、gap TPS、adhesives 组合成可分析单元。
- 方法创新：中等。整机-板-单元的边界传递更像工程建模策略，不是新的数学方法，但对该问题必要。
- 证据创新：中等。给出 21 页较完整的有限元链条，但缺实验验证。
- 应用创新：较强。把热电转换放入高超声速运载器局部热防护板，面向明确工况。

创新可信度来自与作者前作的直接对比：平均转换效率由 0.237% 到 0.51%，且在结构中引入两级 TE 和缓释应力设计。但它仍容易被审稿人追问：额外质量 1156.97 g/单元是否抵消供电收益？理想 Tie 约束是否高估结构可靠性？

## 7. 论证链条复原

论文论证链条如下：

高超声速气动热严重，传统 TPS 低效且不能热复用 -> TE 转换可利用温差发电，但需要和 TPS、承载结构集成 -> 作者前作存在一级 TE、结构示意化、缺气动力载荷三个不足 -> 本文提出两级 TE MTPS unit，并部署到具体运载器二级压缩面 -> 用整机分析获取气动力和位移边界，用 plate 分析传递到 unit，用 unit 分析验证热-力-电性能 -> 得出 MTPS 可承载、防热并输出电能。

逻辑闭合度较高。最强环节是“gap 对方法”的对应：每个前作不足都有结构或分析上的补丁。最薄弱环节是“数值可行性到工程可用性”的跳跃：装配、疲劳、热循环、界面退化、TE 材料长期高温稳定性没有充分证据。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed MTPS concept has multi effective functions of load bearing, heat protection and power supply. The structural design points of the MTPS unit are obtained based on the analysis of the whole vehicle, and the proper displacement boundary conditions are essential to obtaining reasonable results. 2.
- 已有研究不足/GAP：需结合 Introduction 的文献转折句复核。
- 本文解决方式：In this paper, a multifunctional thermal protection system (MTPS) concept with additional functions of thermoelectric (TE) conversion and load bearing is developed for a hypersonic launch vehicle. The mechanical‐thermal‐electrical performance of the MTPS is evaluated based on the multi‐scale analysis of the flight vehicle, MTPS plate and MTPS unit, and the transfer method of mechanical boundary conditions between different scales is developed. The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed MTPS concept has multi effective functions of load bearing, heat protection and power supply.
- 学术或工程增量：The TE module consists of an alumina ceramic layer and a fiber insulation layer to dissipate certain amount of the aerodynamic heat, a high‐temperature and a mid‐temperature TE layers to efficiently convert aerodynamic heat into electric energy, a load‐bearing frame and honeycomb cores to improve the load bearing capacity, embedded electricity conducting plates in TE materials and low‐modulus high‐temperature adhesives to alleviate the thermal stress. The improvement of the TPS and the development of heat reusing technologies become the key points of thermal management of hypersonic vehicles. Lin et al. [9] proposed a series of ITPS with different gradient hollows to improve the structural efficiency.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

方法是三级多尺度数值链：

1. Vehicle scale：用 MSC Patran/Nastran 分析整机在典型轨迹上的气动力作用，提取二级压缩面的载荷和位移。
2. Plate scale：建立 1 m2 MTPS plate，使用整机位移插值作为板边界，确定局部 MTPS 单元的结构设计点。
3. Unit scale：基于 CAD 的 MTPS unit 模型，在 ABAQUS 中用 C3D8T 热-力耦合单元分析温度场和应力场，再由 TE 材料温差和 Seebeck 系数计算电性能。

关键模型假设：

- 焊接和胶接界面用 Tie 约束模拟，认为界面理想。
- 气动热流沿用作者前作数据，机械载荷由整机/板传递。
- 热-力耦合考虑材料非线性和热边界非线性，但电性能更多是后处理计算。
- 位移边界通过非线性插值获取，强调边界比简化周期/固定边界更合理。

复现信息较充分：给出几何尺寸、材料选择、质量、软件、网格规模、关键方程和边界传递流程。缺口是材料温度依赖参数、界面失效准则和 TE 电路连接细节仍需 PDF/附表复核。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 多尺度分析对获得准确机械边界是必要的 | 摘要、4.2、结论 | 整机应力、plate 位移插值、unit 边界传递；Fig. 7-Fig. 10 | 中-强 | 缺少与简化边界的系统误差量化，图像细节需要 PDF 图像复核 |
| 两级 TE 层比前作单级结构更高效 | 摘要、4.3.2、结论 | 平均功率 0.88 W，效率 0.51%；前作效率 0.237%；同一结构中若中温层使用高温材料则 0.82 W/0.45% | 中 | 对比不一定完全等工况；TE 性能计算依赖材料参数 |
| 嵌入导电片和低模量胶可缓解热应力集中 | 2、4.3.1、结论 | 结构设计解释；TE 材料和胶层应力被控制，结论称承载部件 <650 MPa、TE 材料 <150 MPa | 中 | Tie 约束和理想界面可能低估真实界面应力 |
| MTPS 具有承载、防热、供电三功能 | 摘要、结论 | 温度场最高 927/665/368 K 时序，应力场在可承受范围，电输出曲线和 Table 6 | 中-强 | 没有实验、疲劳和寿命验证 |
| 整套 MTPS 可提供约 253.44 W 平均功率 | 4.3.2 | 单元平均 0.88 W × 288 units | 中 | 串联电路、负载匹配、实际热流非均匀、电接触损失需复核 |
| 该构型的质量仍需后续优化 | 2 | MTPS unit 1156.97 g，其中 TE module 904.10 g，TE layer 733.0 g | 强 | 该风险被作者承认，但未纳入性能-质量权衡指标 |

## 10. 图表、公式与结果叙事提取

- Fig. 1：整机与 MTPS 布置，承担“应用场景落地”功能，说明不是孤立单胞。需要 PDF 图像复核。
- Fig. 2：MTPS unit 的 CAD、截面和 3D 打印模型，是全文最关键结构证据，支撑“细节完整化”和“可装配性”。需要 PDF 图像复核。
- Table 1：单元质量分解，支撑工程可行性和重量风险讨论。
- Table 2：相关材料物性，支撑热-力电多材料建模；需复核温度依赖参数是否完整。
- Fig. 3：整机-板-单元分析流程，承担方法框架图功能。
- Fig. 4-Fig. 6：三级模型、网格、边界和载荷，支撑复现性。
- Fig. 7/Table 5：整机应力分布和二级压缩面最大应力，说明设计点选择依据。
- Fig. 8-Fig. 10：plate 位移边界与 unit 位移边界，支撑“多尺度边界传递”的核心 claim。
- Fig. 11-Fig. 13：温度场、应力场和节点曲线，构成热-力安全性主证据。云图色标和局部集中位置需要 PDF 图像复核。
- Fig. 14-Fig. 16/Table 6：TE 材料选择、温度分布、电性能、输出功率/效率，构成发电能力证据。
- 公式 (1)-(4)：平衡方程、应变-位移关系、热弹性方程和本构方程，作用是把 ABAQUS 热-力耦合问题放到连续介质力学框架中。

## 11. 章节结构与篇章布局

真实章节顺序：1 Introduction -> 2 The vehicle and the MTPS -> 3 Numerical model -> 4 Results and discussions -> 5 Conclusion。

结构不是标准 IMRaD 的实验论文，而是“背景/gap -> 工程对象与构型 -> 多尺度模型 -> 分尺度结果 -> 结论”。第 2 节先给 vehicle 和 MTPS，避免方法节悬空；第 3 节再给控制方程和三级模型；第 4 节按 vehicle、plate、unit 递进，和方法尺度一一对应。

标题命名偏好是描述型和对象型：Vehicle、MTPS plate、MTPS unit、Thermal-mechanical performance、Electrical performance。优点是路线清楚；弱点是标题不直接暴露发现，例如 `4.2 MTPS plate` 可改成 `Boundary transfer and stress response of MTPS plate`，信息量更高。

章节推进节奏：

- Introduction：大背景 -> TPS 类型分类 -> TE 技术机会 -> 作者前作不足 -> 本文目标。
- Section 2：先宏观部署，再细观结构，再材料和质量。
- Section 3：从通用方程到整机、板、单元模型。
- Section 4：从整机边界来源到板级筛选，再到单元热力电性能。
- Conclusion：按边界、多级 TE、应力缓解、结构尺寸和整体功率收束。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.2: 2 The vehicle and the MTPS（对象/模块/过渡章节）
- L2 p.3: 3 Numerical model（方法/模型/算法）
  - L3 p.3: 3.1 Governing and constitutive equations（对象/模块/过渡章节）
  - L3 p.3: 3.2 Vehicle（对象/模块/过渡章节）
  - L3 p.5: 3.3 MTPS plate（对象/模块/过渡章节）
  - L3 p.7: 3.4 MTPS unit（对象/模块/过渡章节）
- L2 p.7: 4 Results and discussions（结果/验证/讨论）
  - L3 p.7: 4.1 Vehicle（对象/模块/过渡章节）
  - L3 p.9: 4.2 MTPS plate（对象/模块/过渡章节）
  - L3 p.9: 4.3 MTPS unit（对象/模块/过渡章节）
    - L4 p.9: 4.3.1 Thermal-mechanical performance（对象/模块/过渡章节）
    - L4 p.17: 4.3.2 Electrical performance（对象/模块/过渡章节）
- L2 p.18: 5 Conclusion（结论/贡献回收）
- L2 p.20: CRediT authorship contribution statement（尾部材料）
- L2 p.20: Declaration of Competing Interest（尾部材料）
- L2 p.20: Acknowledgements（尾部材料）
- L2 p.20: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 The vehicle and the MTPS | 2 | 2 | 对象/模块/过渡章节 |
| 3 Numerical model | 3 | 2 | 方法/模型/算法 |
| 3.1 Governing and constitutive equations | 3 | 3 | 对象/模块/过渡章节 |
| 3.2 Vehicle | 3 | 3 | 对象/模块/过渡章节 |
| 3.3 MTPS plate | 5 | 3 | 对象/模块/过渡章节 |
| 3.4 MTPS unit | 7 | 3 | 对象/模块/过渡章节 |
| 4 Results and discussions | 7 | 2 | 结果/验证/讨论 |
| 4.1 Vehicle | 7 | 3 | 对象/模块/过渡章节 |
| 4.2 MTPS plate | 9 | 3 | 对象/模块/过渡章节 |
| 4.3 MTPS unit | 9 | 3 | 对象/模块/过渡章节 |
| 4.3.1 Thermal-mechanical performance | 9 | 4 | 对象/模块/过渡章节 |
| 4.3.2 Electrical performance | 17 | 4 | 对象/模块/过渡章节 |
| 5 Conclusion | 18 | 2 | 结论/贡献回收 |
| CRediT authorship contribution statement | 20 | 2 | 尾部材料 |
| Declaration of Competing Interest | 20 | 2 | 尾部材料 |
| Acknowledgements | 20 | 2 | 尾部材料 |
| References | 20 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 段落节奏是“问题分类 + 局限递进 + 本文补位”。第一段用高超声速气动热和能量浪费提出工程压力；第二段列 ITPS/ATPS/UHTC/ablative TPS；第三段逐项说局限；第四段转向 TE conversion；第五段承认作者前作不足；最后一段给本文任务。

方法段落节奏偏工程说明：先给模型对象，再给边界条件，再给软件与网格，最后给方程。结果段落常以 `Fig. X is/shows...` 起手，随后按时间点或部件列数值，最后提炼一句机制或设计含义。

可学习的段落套路：在复杂工程构型论文中，作者没有一上来堆公式，而是先把对象和结构讲清楚，再让公式服务模型。这种“构型先行、方程后置”的顺序适合多功能结构设计类论文。

## 13. 文笔画像与语言习惯

整体语气是工程可行性证明型。强 claim 使用 `developed`, `essential`, `multi effective functions`；结果描述大量使用 `maximum`, `average`, `respectively`, `reaches`，强调数值边界。谨慎性主要体现在承认质量较高、实验研究有限和进一步优化空间。

主动/被动偏好：贡献和设计动作多用主动 `we developed`, `we established`；模型和仿真步骤多用被动或无主句，如 `is used`, `is established`, `is assumed`。时态上，引言综述用现在完成时和一般过去时，方法用一般现在时，结果用一般现在时描述图表、过去时描述建模操作。

高频术语集中在 `MTPS`, `stress`, `materials`, `unit`, `heat`, `layer`, `load-bearing`, `boundary`, `power`，说明语言中心与贡献中心一致。形容词多为工程限定词：`multi-functional`, `high-temperature`, `low-modulus`, `non-uniform`, `accurate`。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：31537
- 高频词：mtps(66)；heat(46)；stress(43)；thermal(38)；load(37)；vehicle(37)；temperature(34)；unit(34)；mechanical(32)；layer(29)；aerodynamic(28)；tps(26)；bearing(25)；materials(24)；analysis(24)；plane(21)；maximum(21)；boundary(19)；conditions(19)；displacements(18)
- 高频名词化/学术名词：temperature(34)；performance(16)；protection(13)；structure(13)；conversion(11)；electricity(10)；compression(8)；insulation(6)；displacement(6)；equipment(6)；position(5)；concentration(5)；expansion(4)；correlation(4)；capacity(3)
- 高频学术动词：developed(10)；evaluated(6)；analyzed(2)；provide(2)；presented(1)；optimized(1)；derived(1)；compared(1)；validated(1)；derive(1)
- 高频形容词：thermal(38)；mechanical(32)；aerodynamic(28)；boundary(19)；ceramic(16)；hypersonic(10)；structural(8)；adhesive(7)；electrical(6)；displacement(6)；equipment(6)；sic(5)；electric(5)；numerical(5)；resistant(4)
- 高频副词：mainly(9)；gradually(7)；supply(5)；rapidly(4)；efficiently(2)；relatively(2)；severely(2)；extremely(1)；especially(1)；widely(1)；actively(1)；usually(1)；currently(1)；schematically(1)；effectively(1)
- 高频二词短语：mtps unit(31)；load bearing(24)；boundary conditions(19)；bearing frame(17)；mtps plate(15)；alumina ceramic(14)；heat flux(14)；aerodynamic heat(13)；ceramic layer(12)；high temperature(10)；mechanical boundary(10)；displacements nodes(10)
- 高频三词短语：load bearing frame(17)；alumina ceramic layer(11)；mechanical boundary conditions(10)；electricity conducting plates(7)；displacements nodes plane(7)；nodes plane along(7)；mechanical thermal electrical(6)；second stage compression(6)；stage compression surface(6)；plane along displacements(6)；along displacements nodes(6)；sides load bearing(5)
- 被动语态估计：91；`we + 动作动词` 主动句估计：0
- 一般现在时线索：163；一般过去时线索：195；现在完成时线索：1；情态动词线索：35

分章节正文词频：

- 1 Introduction: tps(17)；thermal(16)；heat(16)；mtps(12)；temperature(11)；hypersonic(10)；protection(10)；aerodynamic(9)
- 2 The vehicle and the MTPS: mtps(15)；plate(8)；mechanical(7)；obtained(5)；materials(4)；structure(4)；properties(4)；unit(4)
- 3 Numerical model: vehicle(19)；mtps(16)；heat(15)；plane(13)；mechanical(12)；aerodynamic(11)；system(11)；analysis(10)
- 4 Results and discussions: stress(35)；layer(22)；load(18)；maximum(17)；temperature(16)；ceramic(14)；alumina(13)；heat(11)
- 5 Conclusion: mtps(14)；unit(8)；power(5)；average(5)；tps(4)；load(4)；bearing(4)；thermal(4)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

可复用问题句：

- `Although the above TPS have their own advantages, some limitations have to be stated...`
- 模仿：虽然已有 X 方案分别解决了 A/B/C，但在 Y 维度仍留下不可忽略的工程缺口。

可复用 gap 句：

- `This leaves some rooms for this work.`
- 模仿：这些不足为本文在结构细节、边界条件和性能验证方面的进一步推进留下空间。

可复用方法句：

- `The mechanical-thermal-electrical performance is evaluated based on the multi-scale analysis of...`
- 模仿：本文基于系统级、部件级和单元级的多尺度分析评估 X 的耦合性能。

可复用结果句：

- `The results show that the multi-scale analysis is essential to ensure...`
- 模仿：结果表明，若不显式传递上级边界，单元级响应会失去工程可信度。

常用词组：`load bearing`, `thermal protection`, `power supply`, `aerodynamic heat`, `thermal stress concentration`, `displacement boundary conditions`, `TE conversion efficiency`。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed MTPS concept has multi effective functions of load bearing, heat protection and power supply.
  可迁移模板：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed METHOD concept has multi effective functions of load bearing, heat protection and power supply.
- 原句：With the development of hypersonic engineering, thermal protection system (TPS) [5–8] encounters great challenges, especially from the point of view of energy utilization, the large amount of aerodynamic heat is wasted by the heat resistant and dissipation technologies and thus TPS is low‐efficiency.
  可迁移模板：With the development of hypersonic engineering, thermal protection system (METHOD) [X–X] encounters great challenges, especially from the point of view of energy utilization, the large amount of aerodynamic heat is wasted by the heat resistant and dissipation technologies and thus METHOD is low‐efficiency.
- 原句：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed MTPS concept has multi effective functions of load bearing, heat protection and power supply. designed a novel ITPS, which was consisted of C/SiC composite corrugated core sandwich plane and insulated aerogel.
  可迁移模板：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed METHOD concept has multi effective functions of load bearing, heat protection and power supply. designed a novel METHOD, which was consisted of C/SiC composite corrugated core sandwich plane and insulated aerogel.
- 原句：The structural design points of the MTPS unit are obtained based on the analysis of the whole vehicle, and the proper displacement boundary conditions are essential to obtaining reasonable results. 2.
  可迁移模板：The structural design points of the METHOD unit are obtained based on the analysis of the whole vehicle, and the proper displacement boundary conditions are essential to obtaining reasonable results. X.
#### Gap/转折句
- 未在摘要/引言/结论中稳定识别；正式使用时从对应章节人工补足。
#### 方法提出句
- 原句：In this paper, a multifunctional thermal protection system (MTPS) concept with additional functions of thermoelectric (TE) conversion and load bearing is developed for a hypersonic launch vehicle.
  可迁移模板：In this paper, a multifunctional thermal protection system (METHOD) concept with additional functions of thermoelectric (METHOD) conversion and load bearing is developed for a hypersonic launch vehicle.
- 原句：The mechanical‐thermal‐electrical performance of the MTPS is evaluated based on the multi‐scale analysis of the flight vehicle, MTPS plate and MTPS unit, and the transfer method of mechanical boundary conditions between different scales is developed.
  可迁移模板：The mechanical‐thermal‐electrical performance of the METHOD is evaluated based on the multi‐scale analysis of the flight vehicle, METHOD plate and METHOD unit, and the transfer method of mechanical boundary conditions between different scales is developed.
- 原句：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed MTPS concept has multi effective functions of load bearing, heat protection and power supply.
  可迁移模板：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed METHOD concept has multi effective functions of load bearing, heat protection and power supply.
- 原句：With the development of hypersonic engineering, thermal protection system (TPS) [5–8] encounters great challenges, especially from the point of view of energy utilization, the large amount of aerodynamic heat is wasted by the heat resistant and dissipation technologies and thus TPS is low‐efficiency.
  可迁移模板：With the development of hypersonic engineering, thermal protection system (METHOD) [X–X] encounters great challenges, especially from the point of view of energy utilization, the large amount of aerodynamic heat is wasted by the heat resistant and dissipation technologies and thus METHOD is low‐efficiency.
- 原句：The improvement of the TPS and the development of heat reusing technologies become the key points of thermal management of hypersonic vehicles.
  可迁移模板：The improvement of the METHOD and the development of heat reusing technologies become the key points of thermal management of hypersonic vehicles.
#### 结果呈现句
- 原句：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed MTPS concept has multi effective functions of load bearing, heat protection and power supply.
  可迁移模板：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed METHOD concept has multi effective functions of load bearing, heat protection and power supply.
- 原句：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed MTPS concept has multi effective functions of load bearing, heat protection and power supply. designed a novel ITPS, which was consisted of C/SiC composite corrugated core sandwich plane and insulated aerogel.
  可迁移模板：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed METHOD concept has multi effective functions of load bearing, heat protection and power supply. designed a novel METHOD, which was consisted of C/SiC composite corrugated core sandwich plane and insulated aerogel.
- 原句：The structural design points of the MTPS unit are obtained based on the analysis of the whole vehicle, and the proper displacement boundary conditions are essential to obtaining reasonable results. 2.
  可迁移模板：The structural design points of the METHOD unit are obtained based on the analysis of the whole vehicle, and the proper displacement boundary conditions are essential to obtaining reasonable results. X.
#### 贡献/增量句
- 原句：The improvement of the TPS and the development of heat reusing technologies become the key points of thermal management of hypersonic vehicles.
  可迁移模板：The improvement of the METHOD and the development of heat reusing technologies become the key points of thermal management of hypersonic vehicles.
- 原句：Lin et al. [9] proposed a series of ITPS with different gradient hollows to improve the structural efficiency.
  可迁移模板：Lin et al. [X] proposed a series of METHOD with different gradient hollows to improve the structural efficiency.
- 原句：TE conversion technology [24] is a promising technology in energy reusing, by integrating TE module into TPS, a MTPS [25] can be established.
  可迁移模板：METHOD conversion technology [X] is a promising technology in energy reusing, by integrating METHOD module into METHOD, a METHOD [X] can be established.
- 原句：Xiao et al. [29] established a TE module based on low‐temperature and mid‐temperature TE materials.
  可迁移模板：Xiao et al. [X] established a METHOD module based on low‐temperature and mid‐temperature METHOD materials.
- 原句：Chen et al. [30] established a two‐ stage semiconductor TE generator model with external heat exchange and analyzed the performance of the generator.
  可迁移模板：Chen et al. [X] established a two‐ stage semiconductor METHOD generator model with external heat exchange and analyzed the performance of the generator.
#### 限制/边界句
- 原句：Although the above TPS have their own advantages, some limitations have to be stated: for ITPS, it has thermal short‐circuit effect; for ATPS, it needs additional complicated system to supply consuming coolant and has high‐cost; for UHTC, it has low toughness; for ablative TPS, it can only be used once and has the problem of aerodynamic shape change after ablation.
  可迁移模板：Although the above METHOD have their own advantages, some limitations have to be stated: for METHOD, it has thermal short‐circuit effect; for METHOD, it needs additional complicated system to supply consuming coolant and has high‐cost; for METHOD, it has low toughness; for ablative METHOD, it can only be used once and has the problem of aerodynamic shape change after ablation.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用主要服务四个功能：

1. 背景合法化：用 [1-8] 支撑 hypersonic heating 和 TPS 重要性。
2. 类型分类：用 ITPS、ATPS、UHTC、ablative TPS 文献构造领域版图。
3. 技术转向：用 TE materials、TE generator、热电耦合模型文献说明热复用可行。
4. 前作衔接：用作者前作 [38] 制造最直接 gap，并提供热流数据来源。

引用姿态整体温和：对前人先承认优势，再列局限。最有力的引用策略是把“传统 TPS 的局限”和“作者前作的局限”分开，前者说明研究方向重要，后者说明本文改进必要。

风险：文献图谱较偏工程系统与作者团队技术线，若目标期刊审稿人来自热电材料方向，可能会要求更系统比较多级 TE generator 和高温 TE 材料长期稳定性。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：85
- Introduction 引文簇数量估计：26
- References 条目数：51
- 可识别年份条目数：56
- 2021 年及以后文献数：2
- 2010 年前经典文献数：12
- 同刊引用数（按 subject 粗匹配）：0
- 高频来源期刊：Composite Structures(1)
- 引文簇样例：[13], [14], [15], [16], [17], [9], [18], [10], [19], [11], [12], [20]

带引文的 gap/转折句样例：

- With the development of hypersonic engineering, thermal protection system (TPS) [5–8] encounters great challenges, especially from the point of view of energy utilization, the large amount of aerodynamic heat is wasted by the heat resistant and dissipation technologies and thus TPS is low‐efficiency.
- The authors also proposed a TE module based on the MTPS concept and evaluated its mechanical‐thermoelectric performance in [38], however, the three limitations of the structure and analysis should be mentioned here: 1st, the structure has only one TE stage of high‐temperature TE materials, which leads to low TE conversion efficiency; 2nd, the three‐layer structure is only schematically described and no more details are involved; 3rd, in the thermo‐ mechanical analysis, only the thermal stress is simulated, and the influence of aerodynamic force loads is not considered.

References 解析样例（前 8 条）：

- [1] Qu F, Chen J, Sun Di, Bai J, Zuo G. A grid strategy for predicting the space plane’s hypersonic aerodynamic heating loads. Aerosp Sci Technol 2019;86:659–70.
- [2] Xiao H, He QJ. Aero-heating in hypersonic continuum and rarefied gas flows. Aerosp Sci Technol 2018;82-83:566–74.
- [3] Shahverdi H, Khalafi V. Bifurcation analysis of FG curved panels under simultaneous aerodynamic and thermal loads in hypersonic flow. Compos Struct 2016;146:84–94.
- [4] Uyanna O, Najafi H. Thermal protection systems for space vehicles: A review on technology development, current challenges and future prospects. Acta Astronaut 2020;176:341–56.
- [5] Blosser ML, Chen RR, Schmidt IH, Dorsey JT, Poteet CC, Bird RK. Advanced metallic thermal protection system development. 40th AIAA Aerosp Sci Meet Exhib 2002.
- [6] Pichon T, Barreteau R, Soyris P, Foucault A, Parenteau JM, Prel Y, et al. CMC thermal protection system for future reusable launch vehicles: Generic shingle technological maturation and tests. Acta Astronaut 2009;65(1-2):165–76.
- [7] Behrens B, Müller M. Technologies for thermal protection systems applied on reusable launcher. Acta Astronaut 2004;55(3-9):529–36.
- [8] Glass DE. Ceramic matrix composite (CMC) thermal protection systems (TPS) and hot structures for hypersonic vehicles. 15th AIAA Int Sp Planes Hypersonic Syst Technol Conf 2008::1–36.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

- 实验缺失：3D 打印模型只验证装配理性，不能验证热-力-电性能。
- 界面理想化：Tie 约束忽略胶层老化、脱粘、接触热阻和电接触损失。
- 重量收益比：单元质量 1156.97 g，整机 288 单元质量显著，需和 253.44 W 平均功率做系统权衡。
- 电性能后处理：实际串联、电阻、负载匹配、温度非均匀、导线可靠性没有充分展开。
- 载荷覆盖有限：典型轨迹和特定二级压缩面不能代表更宽 flight envelope。
- 强 claim 风险：`power supply` 容易被理解为独立供电，实际上更像部分替代或补充供电。
- PDF 复核点：所有云图最大值位置、节点曲线、导电片嵌入几何和色标需要复核。

## 17. 可复用资产

- 选题套路：从“传统系统低效”切入，再引入“多功能集成”作为改进方向。
- Gap 套路：先列已有类型优缺点，再列自己前作不足，形成双层 gap。
- 方法套路：整机级载荷 -> 板级边界 -> 单元级性能，适合任何多尺度工程结构分析。
- 图表资产：构型图 + 分析流程图 + 网格边界图 + 分尺度结果云图 + 关键性能表。
- 结果表达：把最大值、平均值、对比前作提升和工程尺寸放在同一结论中。
- 风险控制：主动承认质量偏大和需要进一步结构优化，降低审稿人对过度乐观的反感。

## 18. 对我写论文的启发

如果写多功能结构或热管理论文，可以学习它的“工程对象具体化”：不要只说提出一种结构，而要马上说明安装位置、面积、单元数量、尺寸、质量和载荷来源。

另一个启发是 contribution 要和前作缺陷一一对应。本文前作有三点不足，本文正好给三项改进，这会让审稿人很容易判断“为什么需要这篇新论文”。

需要谨慎模仿的是数值证明的强度。没有实验时，最好在标题、摘要和结论里用 `concept`, `evaluation`, `potential` 控制边界，不要把仿真可行性写成工程成熟度。

## 19. 最终浓缩

这篇论文最值得学习的是：把一个多功能热防护概念拆成可部署、可建模、可计算的三级工程系统，并用前作不足驱动结构改进。

最大风险是：结论依赖理想界面和数值仿真，真实装配、热循环、界面退化和质量收益比尚未被实验闭合。

可迁移的三件事：

1. 用“现有系统功能缺失 + 前作模型不足”制造强 gap。
2. 用“整机-部件-单元”的多尺度链条提高边界条件可信度。
3. 用图表顺序还原设计逻辑：应用场景、结构细节、分析流程、边界传递、性能结果。
