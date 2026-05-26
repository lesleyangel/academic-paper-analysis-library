# The determination of physical dimensions of a hypersonic three-stage compression system considering panel vibration effects

## 0. 读取说明

本文拆解基于 `801/文本/txt/The-determination-of-physical-dimensions-of-a-hypersonic_2023_Aerospace-Scie.txt` 的全文抽取，并参考 `801/文本/metadata/The-determination-of-physical-dimensions-of-a-hypersonic_2023_Aerospace-Scie.json` 的目录。metadata 中 title/author 字段为空，但全文首页和 toc 给出题名、作者与期刊信息。txt 存在双栏串栏，尤其是 Fig. 14-22 与 Table 7 附近，图题、正文和表格混排明显；涉及压力/速度云图、模态振型、频域曲线、三维流动图像和表格数值处均标注“需要 PDF 图像复核”。本文不复述长段原文，只对 shock-on-lip、Oswatitsch criterion、panel vibration、total pressure recovery、mass flow coefficient 等关键词做分析。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 The hypersonic vehicle and multi-stage compression system, 3 Numerical models, 4 Results and discussions, 5 Conclusions。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：The determination of physical dimensions of a hypersonic three-stage compression system considering panel vibration effects。
- 作者：Jian-Jun Gou, Shu-Zhen Jia, Jin-Xing Li, Shuang Xiao, Chun-Lin Gong。
- 期刊与年份：Aerospace Science and Technology, 140, 2023, Article 108431。
- DOI：10.1016/j.ast.2023.108431。
- 关键词：Three-stage compression；Intake performance；Panel vibration；Hypersonic vehicle。
- 论文类型：高超声速进气道/外压缩坡道设计方法论文，结合结构模态、强迫振动流场和流固耦合仿真。
- 研究对象：Mach 6、24 km 高度条件下，具有三段外压缩坡道 CI、CII、CIII 的二维高超声速进气系统。
- 核心方法：shock-on-lip 与 Oswatitsch criterion 确定构型参数；黏性效应 CFD 修正；面板模态分析；强迫振动流场仿真；流固耦合仿真；以总压恢复系数和质量流量系数评估进气性能。
- 主要证据：2-30 mm 面板厚度的自然频率；0-0.11 m 振幅与 10-250 Hz 频率扫描；不同面板厚度下 FSI 位移、频率和进气性能波动；最终给出 CI/CII/CIII 厚度下限 5.5/6.0/6.5 mm。
- 目标读者：高超声速进气道设计、气动弹性/流固耦合、冲压发动机总体和薄壁结构设计研究者。

这篇论文的身份是“把结构振动带回进气道几何/尺寸设计”的工程方法论文。它不是单纯研究某个振动现象，而是试图回答设计问题：在外压缩坡道构型参数已经由气动准则给定后，面板厚度等物理尺寸如何同时满足结构和进气性能约束。

## 2. 摘要与核心信息提取

一句话主张：高超声速进气道的薄面板压缩坡道会受流固耦合、发动机推力变化和噪声激励而振动，进气系统设计不能只确定 shock angles、compression angles 和 ramp lengths，还必须通过结构模态、强迫振动和 FSI 分析确定可用物理尺寸。

摘要的叙事很清晰：先说 panel vibration 对 air-breathing hypersonic vehicle intake performance 有决定性影响，但清晰设计路径仍 absent；随后给出三段压缩系统设计条件 Mach 6、24 km；接着说明构型参数由 shock-on-lip、Oswatitsch 和黏性修正确定；然后用面板厚度 0.002-0.03 m 做模态分析；再用振幅 0-0.11 m、频率 10-250 Hz 做强迫振动流场；最后用流固耦合分析确定外压缩坡道的 available physical dimensions。

核心信息不是“振动会影响进气性能”这一常识，而是“将尺寸设计分成三条约束路径”：避免结构应力过高、避免结构共振、维持进气性能。文章最终将这些约束合并成 design path，并给出 CI、CII、CIII 面板厚度下限。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/The-determination-of-physical-dimensions-of-a-hypersonic_2023_Aerospace-Scie.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/The-determination-of-physical-dimensions-of-a-hypersonic_2023_Aerospace-Scie.md`。

中文译文：

> 文章历史记录： 接收日期 2023年1月9日 收到修订版 2023年5月4日 接受日期 2023年6月1日 在线发布 2023年6月7日 通讯人：Yu Lv
>
> 流固耦合、发动机推力变化和噪声激发的进气系统面板振动对吸气式高超声速飞行器的性能具有决定性影响。此类进气系统的设计应包含考虑流动和结构振动的结构参数和物理尺寸的确定，目前尚缺乏明确的设计路径。本文设计了马赫数为6、飞行高度为24 km的三级外压缩坡道进气系统，并根据唇上冲击准则、Oswatisch准则和粘性效应修正确定了构型参数。分析了面板厚度为0.002~0.03 m的外部压缩坡道的模态振动特性，通过固定四个侧边界的约束条件，并附加更真实的强化内部边界约束，获得了合适的固有频率。
>
> 对压缩坡道强制面板振动的进气系统流场进行了仿真，明确了0～0.11 m振幅和10～250 Hz频率对进气性能即总压恢复系数和质量流量系数的影响。通过流固耦合仿真研究了高超声速流振动对压缩坡道结构和进气性能的影响。最后，确定了外部压缩坡道的可用物理尺寸，并通过考虑结构和进气性能来制定进气系统的设计路径。 © 2023 Elsevier Masson SAS。版权所有。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题来源是高超声速吸气式飞行器的进气系统脆弱性。外压缩进气道通常采用多级薄板压缩坡道，以减重并与机身一体化；但薄板在高超声速气流、发动机推力变化、噪声和非定常压力下容易振动。振动会改变近壁流场、冲击波位置、边界层和溢流状态，进而影响 combustor 入口所需的总压恢复和质量流量。

作者把大问题收束成“物理尺寸确定”而非“振动现象分析”。传统构型设计已能通过 shock-on-lip 获得无溢流最大捕获流量，通过 Oswatitsch criterion 获得较高总压恢复，并通过 CFD 修正黏性影响。但这些主要决定角度和长度等 configurational parameters，并没有回答面板厚度、刚度和自然频率是否满足工作要求。

选题价值有三层。工程价值：避免 intake unstart、combustor choking 或结构失效。方法价值：把结构模态、强迫振动气动响应和真实 FSI 响应串成设计路径。写作价值：将“进气道设计”从纯气动几何问题拓展为气动-结构-性能共同约束的尺寸设计问题。

这个选题的好处是边界具体：二维三段外压缩系统，Mach 6，24 km，高度和外形参数清楚。这样的限定让仿真参数扫描可执行，也让结论可落到明确厚度数值；缺点是泛化到轴对称或三维内转进气道时需要重新验证。

## 4. 领域位置与文献版图

Introduction 先把 intake system 按构型分为 axisymmetric、two-dimensional planar 和 three-dimensional，并举 HRE、GTX、SABRE、X-43A、X-51A、Strutjet、Rectangular-to-Elliptical-Shape-Transition 等例子。这个分类的作用是说明本文选择二维平面多级压缩进气道有明确工程背景，适合 lifting body vehicle 与机身一体化。

随后作者讨论外压缩构型参数的经典设计准则：shock-on-lip criterion 保证冲击波汇聚到 cowl lip、无溢流并接近最大质量流量；Oswatitsch criterion 指向最大总压恢复；黏性影响则需 CFD 修正。这里作者不是推翻经典气动设计，而是承认它们解决了 configurational parameters。

第三部分文献转向 hypersonic FSI/aeroelastic/aerothermoelastic/shock-boundary-layer interaction 等复杂现象。作者用这些文献说明薄板形变和振动已被重视，但 time-consuming CFD/FSI 使设计路径不清楚，尤其是结构尺寸如何同时考虑多振动源、高不确定性和进气性能。

本文站位是：继承经典气动构型设计，用结构动力学和 FSI 补上 physical dimensions 的设计约束。它不是基础流固耦合理论论文，而是面向工程设计路径的综合仿真研究。

## 5. Gap 制造机制

文章制造的 gap 很具体：高超声速压缩进气系统设计通常关注 shock angles、compression angles、ramp length projections 等构型参数，但 thin-panel compression ramps 的厚度、刚度和振动特性对实际进气性能有显著影响，而清晰的 structural design path 仍然缺失。

gap 可以拆成三类。第一是对象 gap：已有气动设计准则主要面向静态几何和无振动流场，未充分处理振动边界。第二是方法 gap：现有静气动弹性、动气动弹性和热气动弹性研究往往计算成本高，难以直接转化为尺寸设计流程。第三是评价 gap：进气道尺寸不仅要满足结构强度和共振限制，还要保持 total pressure recovery coefficient 与 mass flow coefficient，这两个指标需要被放进同一设计判据。

这个 gap 的说服力较强，因为作者没有笼统说“振动重要”，而是明确提出三个 branch paths：避免 too high stress、averting resonance、maintaining intake performance。这样 gap 直接指向后文三个证据模块。

## 6. 创新性判断

作者声明的创新包括：在 Mach 6、24 km 条件下设计三段外压缩系统；分析 2-30 mm 面板厚度的模态振动特性；阐明振幅 0-0.11 m 与频率 10-250 Hz 对进气性能的影响；通过 FSI 分析确定可用物理尺寸；最终总结设计路径。

真实创新属于“设计流程整合 + 尺寸判据”。shock-on-lip、Oswatitsch、模态分析、CFD 和 FSI 都不是新工具，新意在于将它们串成从构型参数到面板厚度下限的流程，并把自然频率与 operational frequency 的交叉关系作为厚度判据。

创新强度：中等。对于基础 FSI 研究者，它不是新算法；对于高超声速进气道设计者，它提供了可操作的工程路径。最终给出 CI=5.5 mm、CII=6.0 mm、CIII=6.5 mm 的厚度下限，是文章最有工程指向的贡献。

潜在争议是：激励源被简化为强迫振动与特定 FSI 条件，发动机推力变化、噪声谱和热应力等实际激励未完全进入模型。因此“available physical dimensions”更像给定条件下的设计参考，而非普适准则。

## 7. 论证链条复原

全文论证链如下：

1. 高超声速吸气式飞行器进气道性能决定发动机入口条件，压缩系统通常采用多级薄板坡道。
2. 经典气动准则可确定冲击角、压缩角和长度投影，但不能保证薄板结构在振动下仍满足进气性能。
3. 薄板坡道受流固耦合、发动机和噪声激励，会引起面板振动，可能导致总压恢复和质量流量下降或波动。
4. 因此设计应包括结构模态、强迫振动流场和 FSI 三类分析。
5. 面板厚度越大，自然频率和刚度总体提高，振动位移和性能波动减小，但重量和集成代价增加。
6. 强迫振动分析说明振幅和频率会影响 shock/flow field，并改变总压恢复和质量流量。
7. FSI 分析给出真实气流诱导振动下的位移、主频和进气性能波动。
8. 通过比较 natural frequency 与 operational frequency，并结合 intake performance，确定 CI/CII/CIII 厚度下限和设计路径。

这条链的关键闭合点在 Fig. 21 和 Fig. 22：前者把自然频率与运行频率随厚度变化的趋势放在一起，后者把流程总结成 design path。没有这两张图，文章就只是参数研究；有了它们，参数研究被转化成工程设计方法。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：Thus, for the design of a compression system, it is essential to obtain vibration characteristics of compression ramps and clarify their effects on the intake performance. * Corresponding authors. Aerospace Science and Technology 140 (2023) 108431 with additional strengthened internal boundary using certain number of rivets. (2) For the three-stage compression ramps CI, CII and CIII, the natural frequency increases with the increase of panel thickness; the available upper bound of operational vibration frequencies in real conditions increases from 16.8 to 249 Hz, 17.76 to 259 Hz, and 17.12 to 251 Hz, respectively, when the panel thickness increases from 2 to 30 mm. (3) The consideration of panels’ fluid-structural interaction will lead to the reduction and fluctuation of total pressure recovery and mass flow coefficients; the intake performance fluctuation range decreases with the increasing panel thickness and greater stiffness, and increases when the fluid-structural interaction source transfers from the fuselage leading edge to the intake lip. (4) The natural frequency increases while the operational frequency decreases with the increase of panel thickness; the lower bound of panel thickness for CI, CII and CIII that studied in this work (two-dimensional intake system with three-stage compression ramps under Mach number of 6 and altitude of 24 km) can be considered as 5.5, 6.0 and 6.5 mm, respectively. (5) For the design of thin-panel-structural compression system, the consideration of resonance limit is essential.
- 已有研究不足/GAP：However, the thin-panel structure is liable to be excitated by various vibration sources such as hypersonic flow (fluid-structural interaction), engine (thrust variation) and noise, and the induced panel vibration has significant effect on the performance of air intake system.
- 本文解决方式：Finally, the available physical dimensions of external compression ramps are determined and a design path of intake system is developed by considering both the structural and intake performance. © 2023 Elsevier Masson SAS.
- 学术或工程增量：需结合 Results/Conclusion 的量化结果复核。
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

方法首先是气动构型设计。三段外压缩坡道在 Mach 6、24 km 条件下设计，第一、第二、第三 shock angles 分别约 13.6°、15.2°、16.9°，compression angles 约 4.5°、5.0°、5.5°，CI/CII/CIII 的 x 方向长度投影约 3.4、2.1、2.9 m。该部分确定“如果结构刚性理想，进气道应该长什么样”。

第二是结构模态分析。作者建立 CI、CII、CIII 面板模型，考虑固定四边边界以及更现实的 strengthened internal boundary，厚度从 2 到 30 mm，求解自然频率和模态振型。约束条件的处理很重要，因为完全四边固支可能过强，附加内边界更接近实际加强结构。

第三是流场分析。用 RANS/CFD 模拟带振动结构边界的流场，评价 outlet total pressure recovery coefficient σ 和 mass flow coefficient φ。时间步受到振动频率和流动穿越时间约束，文中提到 250 Hz 下时间步不应大于 0.0002 s。评价指标分别代表总压损失和捕获流量。

第四是 FSI 分析。结构节点位移和流体压力通过映射方法交换，使用 Bucket Surface 和 General Grid 进行非保守/保守信息传递。结果包括面板位移时域/频域、压力/速度场和性能波动。最终通过厚度变化下自然频率上升、运行频率下降的趋势确定厚度下限。

## 9. 证据系统与 Claim-Evidence 表

证据系统按“模型可靠性 -> 结构规律 -> 振动对性能影响 -> FSI 下尺寸判据”推进。作者先做网格无关性和文献对比验证，再做模态与强迫振动参数研究，最后用 FSI 接近真实工况。

| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 经典构型设计不足以确定进气道物理尺寸 | Introduction、Section 2 | shock-on-lip/Oswatitsch 只确定角度和长度，不能处理薄板振动 | 设计逻辑 | 强 | 需进一步量化“传统设计”与本文设计差异 |
| 面板厚度增加会提高自然频率和刚度 | Section 4.1、Fig. 9、Fig. 10 | CI/CII/CIII 第一阶自然频率随 2-30 mm 厚度从约 16-17 Hz 增至约 249-259 Hz | 模态计算 | 强 | 模态边界条件需 PDF/模型复核 |
| 振动振幅会降低或波动进气性能 | Section 4.2.1、Fig. 12-Fig. 14 | 0-0.11 m 振幅下，总压恢复和质量流量系数的均值/波动变化 | 强迫振动 CFD | 中强 | 0.11 m 振幅工程现实性需讨论 |
| 振动频率影响 shock/flow field 和性能波动 | Section 4.2.2、Fig. 15-Fig. 16 | 10-250 Hz 下压力/速度场与 σ、φ 均值/波动范围变化 | 参数扫描 | 中强 | 频率谱来自何种实际激励仍简化 |
| FSI 会导致总压恢复与质量流量下降和波动 | Section 4.3、Table 7 | FSI 条件下 σ、φ 小于强迫振动部分，σ 波动大于 φ；性能波动随厚度增加降低 | 流固耦合仿真 | 强 | 三维效应、湍流模型和网格耦合需复核 |
| CI/CII/CIII 厚度下限可取 5.5/6.0/6.5 mm | Conclusion、Fig. 21 | 自然频率随厚度上升而 operational frequency 下降，交叉/安全关系给出下限 | 综合判据 | 中强 | 仅对二维三段进气道、Mach 6/24 km 成立 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核说明 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 车辆与进气系统示意 | 研究对象具体化 | 外压缩段分 CI/CII/CIII，振动影响近壁流场 | 需要 PDF 图像复核 |
| Fig. 2/Table 1 | 构型参数 | 经典气动设计给出基本几何 | shock angles、compression angles、长度投影 | 表格需 PDF 复核 |
| Eq. (1) | 无阻尼振动方程 | 模态分析基础 | M、K、位移向量决定自然频率 | 公式需 PDF 复核 |
| Fig. 3/Fig. 7/Fig. 8 | 面板模型与模态振型 | 边界条件影响自然频率 | CoA/CoB 下模态形态不同 | 需要 PDF 图像复核 |
| Fig. 4/Table 5/Fig. 5-Fig. 6 | 流场网格与模型验证 | CFD/FSI 可信度 | 网格无关性和压力/位移对比验证 | 需要 PDF 图像复核 |
| Fig. 9/Fig. 10 | 厚度-自然频率/刚度关系 | 厚度提高结构抗振能力 | 自然频率随厚度显著上升 | 需要 PDF 图像复核 |
| Fig. 11 | 气动力下位移云图 | 静态结构响应 | 高压区域引起坡道位移 | 需要 PDF 图像复核 |
| Fig. 12-Fig. 14 | 振幅影响 | 振幅改变性能均值和波动 | 总压恢复和质量流量随振幅变化 | 需要 PDF 图像复核 |
| Fig. 15-Fig. 16 | 频率影响 | 不同振动频率下性能变化 | σ、φ 的波动范围与频率相关 | 需要 PDF 图像复核 |
| Fig. 17-Fig. 20/Table 7 | FSI 响应 | 真实流固耦合下厚度影响性能 | 位移、频率、压力/速度场和性能表 | 需要 PDF 图像复核 |
| Fig. 21 | 自然/运行频率随厚度变化 | 厚度下限判据 | natural frequency 上升、operational frequency 下降 | 需要 PDF 图像复核 |
| Fig. 22 | 设计路径 | 将研究转化为流程资产 | 构型设计 -> 性能分析 -> 评价迭代 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

真实章节为：1 Introduction；2 The hypersonic vehicle and multi-stage compression system；3 Numerical models；4 Results and discussions；5 Conclusions。Section 3 下分 mode analysis 与 flow field analysis，后者含 governing equations、computational region、boundary conditions、mesh independence 和 validation。Section 4 下分 mode analysis、effects of forced vibration、FSI effects 和 design path。

结构非常“设计路径化”：第 2 章固定对象并给出构型参数，第 3 章把三类仿真模型交代清楚，第 4 章逐步增加复杂度：先结构自身、再强迫振动、再流固耦合、最后设计路径。这样的布局适合让读者看到“为什么最后的厚度下限不是拍脑袋”。

标题命名偏工程功能型，例如 “Effects of vibration amplitude”“Effects of vibration frequency”“Design path of compression system”。标题直接对应证据模块，有利于审稿人检查每个 claim 是否被验证。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.2: 2 The hypersonic vehicle and multi-stage compression system（对象/模块/过渡章节）
- L2 p.2: 3 Numerical models（方法/模型/算法）
  - L3 p.2: 3.1 Mode analysis（对象/模块/过渡章节）
    - L4 p.2: 3.1.1 Vibration differential equation（对象/模块/过渡章节）
    - L4 p.3: 3.1.2 Meshed models and constraint conditions（方法/模型/算法）
  - L3 p.4: 3.2 Flow field analysis（对象/模块/过渡章节）
    - L4 p.4: 3.2.1 Governing equations（对象/模块/过渡章节）
    - L4 p.4: 3.2.2 Computational region, boundary conditions and mesh independence（对象/模块/过渡章节）
    - L4 p.5: 3.2.3 Validation of the numerical method（方法/模型/算法）
- L2 p.5: 4 Results and discussions（结果/验证/讨论）
  - L3 p.5: 4.1 Mode analysis（对象/模块/过渡章节）
  - L3 p.6: 4.2 Effects of the forced vibration of compression ramps（对象/模块/过渡章节）
    - L4 p.6: 4.2.1 Effects of vibration amplitude（对象/模块/过渡章节）
    - L4 p.8: 4.2.2 Effects of vibration frequency（对象/模块/过渡章节）
  - L3 p.9: 4.3 Fluid-structural interaction effects（对象/模块/过渡章节）
    - L4 p.9: 4.3.1 Structural vibration of compression ramps（对象/模块/过渡章节）
    - L4 p.10: 4.3.2 Effects of vibration on the intake performance（对象/模块/过渡章节）
  - L3 p.10: 4.4 Design path of compression system（对象/模块/过渡章节）
- L2 p.12: 5 Conclusions（结论/贡献回收）
- L2 p.14: Declaration of competing interest（尾部材料）
- L2 p.14: Data availability（尾部材料）
- L2 p.15: Acknowledgements（尾部材料）
- L2 p.15: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 The hypersonic vehicle and multi-stage compression system | 2 | 2 | 对象/模块/过渡章节 |
| 3 Numerical models | 2 | 2 | 方法/模型/算法 |
| 3.1 Mode analysis | 2 | 3 | 对象/模块/过渡章节 |
| 3.1.1 Vibration differential equation | 2 | 4 | 对象/模块/过渡章节 |
| 3.1.2 Meshed models and constraint conditions | 3 | 4 | 方法/模型/算法 |
| 3.2 Flow field analysis | 4 | 3 | 对象/模块/过渡章节 |
| 3.2.1 Governing equations | 4 | 4 | 对象/模块/过渡章节 |
| 3.2.2 Computational region, boundary conditions and mesh independence | 4 | 4 | 对象/模块/过渡章节 |
| 3.2.3 Validation of the numerical method | 5 | 4 | 方法/模型/算法 |
| 4 Results and discussions | 5 | 2 | 结果/验证/讨论 |
| 4.1 Mode analysis | 5 | 3 | 对象/模块/过渡章节 |
| 4.2 Effects of the forced vibration of compression ramps | 6 | 3 | 对象/模块/过渡章节 |
| 4.2.1 Effects of vibration amplitude | 6 | 4 | 对象/模块/过渡章节 |
| 4.2.2 Effects of vibration frequency | 8 | 4 | 对象/模块/过渡章节 |
| 4.3 Fluid-structural interaction effects | 9 | 3 | 对象/模块/过渡章节 |
| 4.3.1 Structural vibration of compression ramps | 9 | 4 | 对象/模块/过渡章节 |
| 4.3.2 Effects of vibration on the intake performance | 10 | 4 | 对象/模块/过渡章节 |
| 4.4 Design path of compression system | 10 | 3 | 对象/模块/过渡章节 |
| 5 Conclusions | 12 | 2 | 结论/贡献回收 |
| Declaration of competing interest | 14 | 2 | 尾部材料 |
| Data availability | 14 | 2 | 尾部材料 |
| Acknowledgements | 15 | 2 | 尾部材料 |
| References | 15 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 的节奏是：先讲进气系统重要性，再讲二维多级压缩系统的构型设计准则，然后转入薄板振动风险，最后指出尺寸设计路径缺失。这个节奏很有效，因为它先承认现有气动设计成熟，再指出其没覆盖结构振动。

方法段落采用“仿真任务清单”式推进：mode analysis、flow field with vibrational structural boundaries、FSI analysis。每个模型都先给公式/边界/网格，再给评价指标。这样写的好处是工程可复现性强，缺点是文本较密，公式和图表多，读者需要频繁对照。

结果段落节奏是“厚度 -> 振幅 -> 频率 -> FSI -> design path”。它不是随机扫参，而是从结构变量到激励变量，再到耦合真实变量。结论段则将结果压成五条，最关键的是自然频率/运行频率关系和厚度下限。

## 13. 文笔画像与语言习惯

文笔是典型 Aerospace Science and Technology 工程仿真论文：句子偏长，名词组合多，强调 design path、available thickness、structural and intake performance。高频词包括 compression ramps、panel vibration、intake performance、total pressure recovery coefficient、mass flow coefficient、fluid-structural interaction、natural frequency、operational frequency。

作者常用 “from the structural and flow point of views”“it can be found that”“in this work” 等表达。主动语态用于提出流程和判断，被动语态用于仿真设置。结果解释多用因果句，如振动使 shock wave spill out、three-dimensional effects 导致性能下降、stiffness 增加使波动降低。

文章语气总体稳健，结论中主动限定“specific results and data only available for the two-dimensional intake system with three-stage compression ramps under Mach 6 and altitude 24 km”，这对审稿风险控制很重要。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：31428
- 高频词：vibration(65)；compression(59)；intake(58)；panel(54)；flow(46)；performance(39)；system(38)；cii(31)；ciii(31)；thickness(30)；work(27)；ramps(26)；should(26)；frequency(25)；conditions(22)；fluid-structural(22)；design(22)；structural(22)；effects(20)；coefficient(19)
- 高频名词化/学术名词：vibration(65)；compression(59)；performance(39)；thickness(30)；interaction(18)；pressure(18)；fluctuation(14)；structure(12)；stiffness(10)；influence(9)；variation(7)；displacement(6)；condition(6)；consideration(5)；characteristics(5)
- 高频学术动词：analyzed(9)；indicated(6)；developed(3)；indicate(3)；evaluated(2)；presented(2)；compared(1)；enable(1)；reveal(1)；provide(1)
- 高频形容词：fluid-structural(22)；structural(22)；coefficient(19)；hypersonic(18)；total(14)；natural(13)；boundary(11)；internal(9)；real(9)；operational(8)；numerical(7)；essential(6)；physical(6)；external(6)；additional(6)
- 高频副词：finally(8)；widely(2)；closely(1)；commonly(1)；actually(1)；numerically(1)；relatively(1)；uniformly(1)；specifically(1)；obviously(1)；sequentially(1)；mainly(1)
- 高频二词短语：intake system(26)；cii ciii(26)；intake performance(23)；panel thickness(23)；compression ramps(22)；fluid-structural interaction(15)；compression system(12)；total pressure(12)；mass flow(12)；gou jia(12)；flow coefficient(11)；pressure recovery(10)
- 高频三词短语：total pressure recovery(10)；mass flow coefficient(8)；pressure recovery coefficient(6)；air-breathing hypersonic vehicle(5)；recovery coefficient mass(5)；coefficient mass flow(5)；time step should(5)；cii ciii vibrations(5)；increase panel thickness(5)；fluid-structural interaction engine(4)；interaction engine thrust(4)；engine thrust variation(4)
- 被动语态估计：114；`we + 动作动词` 主动句估计：0
- 一般现在时线索：179；一般过去时线索：224；现在完成时线索：0；情态动词线索：48

分章节正文词频：

- 1 Introduction: intake(35)；compression(24)；system(23)；performance(18)；vibration(15)；flow(14)；hypersonic(13)；design(12)
- 2 The hypersonic vehicle and multi-stage compression system: compression(5)；ramps(5)；vibration(4)；simulations(3)；cii(2)；ciii(2)；obtained(2)；criterion(2)
- 3 Numerical models: fixed(16)；work(14)；vibration(12)；mesh(12)；flow(11)；rivets(11)；time(11)；should(10)
- 4 Results and discussions: vibration(30)；panel(28)；cii(20)；ciii(20)；thickness(19)；flow(17)；compression(15)；frequency(15)
- 5 Conclusions: compression(8)；panel(8)；intake(7)；system(5)；frequency(5)；increases(5)；thickness(5)；vibration(4)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

高频术语：shock-on-lip criterion、Oswatitsch criterion、viscous effects modification、panel thickness、mode analysis、forced vibration、fluid-structural coupling、total pressure recovery coefficient、mass flow coefficient、operational frequency。

可复用 gap 句式：`A clear design path considering various vibration sources, high uncertainty and complex design objectives is essential while still absent.` 适合写工程流程缺失。

可复用方法句式：`The structural design path should have three branch paths: avoiding too high stress, averting resonance, and maintaining intake performance.` 适合多约束尺寸设计。

可复用结果句式：`The consideration of panels' fluid-structural interaction will lead to the reduction and fluctuation of total pressure recovery and mass flow coefficients.` 适合描述 FSI 对性能指标的影响。

可复用边界句式：`The specific results and data are available only for the studied configuration and flight condition.` 适合在结论中主动控制适用范围。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：Thus, for the design of a compression system, it is essential to obtain vibration characteristics of compression ramps and clarify their effects on the intake performance. * Corresponding authors.
  可迁移模板：Thus, for the design of a compression system, it is essential to obtain vibration characteristics of compression ramps and clarify their effects on the intake performance. * Corresponding authors.
- 原句：However, in real conditions, the viscous effect will lead to the reduction of intake performance, thus viscosity corrections by corresponding CFD simulations are essential subsequent steps.
  可迁移模板：However, in real conditions, the viscous effect will lead to the reduction of intake performance, thus viscosity corrections by corresponding METHOD simulations are essential subsequent steps.
- 原句：A clear structural design path of external compression and intake system considering the various vibration sources, high uncertainty and complex design objectives and constraints is essential while still absent at present.
  可迁移模板：A clear structural design path of external compression and intake system considering the various vibration sources, high uncertainty and complex design objectives and constraints is essential while still absent at present.
#### Gap/转折句
- 原句：However, the thin-panel structure is liable to be excitated by various vibration sources such as hypersonic flow (fluid-structural interaction), engine (thrust variation) and noise, and the induced panel vibration has significant effect on the performance of air intake system.
  可迁移模板：However, the thin-panel structure is liable to be excitated by various vibration sources such as hypersonic flow (fluid-structural interaction), engine (thrust variation) and noise, and the induced panel vibration has significant effect on the performance of air intake system.
- 原句：However, in real conditions, the viscous effect will lead to the reduction of intake performance, thus viscosity corrections by corresponding CFD simulations are essential subsequent steps.
  可迁移模板：However, in real conditions, the viscous effect will lead to the reduction of intake performance, thus viscosity corrections by corresponding METHOD simulations are essential subsequent steps.
- 原句：As discussed above, there are several vibration sources like the fluid-structural interaction, engine thrust variation and so on for a hypersonic vehicle, from the structural point of view the available thickness of compression ramp panels should be determined by considerations of all the vibration sources, which is actually difficult to realize.
  可迁移模板：As discussed above, there are several vibration sources like the fluid-structural interaction, engine thrust variation and so on for a hypersonic vehicle, from the structural point of view the available thickness of compression ramp panels should be determined by considerations of all the vibration sources, which is actually difficult to realize.
#### 方法提出句
- 原句：A clear structural design path of external compression and intake system considering the various vibration sources, high uncertainty and complex design objectives and constraints is essential while still absent at present.
  可迁移模板：A clear structural design path of external compression and intake system considering the various vibration sources, high uncertainty and complex design objectives and constraints is essential while still absent at present.
- 原句：Aerospace Science and Technology 140 (2023) 108431 is determined by fluid-structural analysis from the structural and flow point of views and a design path of compression system is developed by considering both the structural and intake performance.
  可迁移模板：Aerospace Science and Technology X(X) Xis determined by fluid-structural analysis from the structural and flow point of views and a design path of compression system is developed by considering both the structural and intake performance.
#### 结果呈现句
- 原句：The “shock-on-lip” criterion means all the shock waves are converged to the cowl lip with no spillage and indicates the maximum mass flow coefficient (should be 100%), while the Oswatitsch criterion indicates the maximum total pressure recovery [15].
  可迁移模板：The “shock-on-lip” criterion means all the shock waves are converged to the cowl lip with no spillage and indicates the maximum mass flow coefficient (should be X), while the Oswatitsch criterion indicates the maximum total pressure recovery [X].
#### 贡献/增量句
- 原句：The additional compression and turning processes in such three-dimensional intake system contribute to the improvement of compression efficiency.
  可迁移模板：The additional compression and turning processes in such three-dimensional intake system contribute to the improvement of compression efficiency.
- 原句：A great number of researches about complex fluid-structural phenomena, e.g., turbulent boundary layers [16,17], aeroelastic effects [18,19], dynamic aeroelastic effects [20,21], aerothermoelastic effects [22,23], shock-wave-boundarylayer interactions [24–27] and involved thermochemical [28] and high temperature non-equilibrium effects [29,30] also contribute to the cognition of viscous effects and the effective design of intake system.
  可迁移模板：A great number of researches about complex fluid-structural phenomena, e.g., turbulent boundary layers [X,X], aeroelastic effects [X,X], dynamic aeroelastic effects [X,X], aerothermoelastic effects [X,X], shock-wave-boundarylayer interactions [X–X] and involved thermochemical [X] and high temperature non-equilibrium effects [X,X] also contribute to the cognition of viscous effects and the effective design of intake system.
#### 限制/边界句
- 原句：The design of such type of intake system should contain the determination of configurational parameters and physical dimensions by considering both flow and structural vibrations, and a clear design path is still absent.
  可迁移模板：The design of such type of intake system should contain the determination of configurational parameters and physical dimensions by considering both flow and structural vibrations, and a clear design path is still absent.
- 原句：A compression system, take the multi-stage planar one for instance, is formed by several compression ramps, which commonly adopt thin-panel structures in consideration of the low-weight requirement.
  可迁移模板：A compression system, take the multi-stage planar one for instance, is formed by several compression ramps, which commonly adopt thin-panel structures in consideration of the low-weight requirement.
- 原句：The design of such type of intake system should contain the determination of configurational parameters and physical dimensions by considering both flow and structural vibrations, and a clear design path is still absent.
  可迁移模板：The design of such type of intake system should contain the determination of configurational parameters and physical dimensions by considering both flow and structural vibrations, and a clear design path is still absent.
- 原句：The “shock-on-lip” criterion means all the shock waves are converged to the cowl lip with no spillage and indicates the maximum mass flow coefficient (should be 100%), while the Oswatitsch criterion indicates the maximum total pressure recovery [15].
  可迁移模板：The “shock-on-lip” criterion means all the shock waves are converged to the cowl lip with no spillage and indicates the maximum mass flow coefficient (should be X), while the Oswatitsch criterion indicates the maximum total pressure recovery [X].
- 原句：Thus, the structural design of intake system should consider objectives and constraints in two perspectives, i.e., the structural and intake performance.
  可迁移模板：Thus, the structural design of intake system should consider objectives and constraints in two perspectives, i.e., the structural and intake performance.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用策略有三层。第一层是进气道构型与经典设计准则，引用 axisymmetric、two-dimensional、three-dimensional intake 的代表项目和 shock-on-lip/Oswatitsch 设计理论。第二层是复杂高超声速流动和气动弹性现象，包括 turbulent boundary layers、aeroelastic effects、dynamic aeroelastic effects、aerothermoelastic effects、shock-wave-boundary-layer interactions、thermochemical/high-temperature non-equilibrium effects。第三层是用于模型验证的参考算例，包括压力系数和动态压力位移对比。

这种引用组织的作用是把本文放在“成熟气动设计之后、结构振动约束之前”的位置。作者不是说前人错，而是说前人解决的是构型参数，本文补 physical dimensions。

引用风险在于 FSI/振动激励源的真实谱可能没有充分文献约束。若审稿人要求发动机推力变化或噪声激励的谱特征，本文的强迫振动参数范围可能被认为是工程假设而非充分实测输入。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：73
- Introduction 引文簇数量估计：22
- References 条目数：36
- 可识别年份条目数：38
- 2021 年及以后文献数：19
- 2010 年前经典文献数：8
- 同刊引用数（按 subject 粗匹配）：0
- 高频来源期刊：Aerospace Science and Technology(1)
- 引文簇样例：[3], [1,2], [4], [5], [6], [7], [8,9], [10], [11], [12,13], [14], [15]

带引文的 gap/转折句样例：

- 未稳定识别带引文的 gap 转折句；需要回到 Introduction 人工核对。

References 解析样例（前 8 条）：

- [1] F-Y. Zuo, S. Mölder, Hypersonic wavecatcher intakes and variable-geometry turbine based combined cycle engines, Prog. Aerosp. Sci. 106 (2019) 108–144.
- [2] S. Luo, Y. Sun, J. Liu, J. Song, W. Cao, Performance analysis of the hypersonic vehicle with dorsal and ventral intake, Aerosp. Sci. Technol. 131 (2022) 107964.
- [3] O. Musa, G. Huang, Z. Yu, Assessment of new pressure-corrected design method for hypersonic internal waverider intake, Acta Astronaut. 201 (2022) 230–246.
- [4] E.T. Curran, Scramjet engines: the first forty years, J. Propuls. Power 17 (6) (2001) 1138–1148.
- [5] C.J. Trefny, J.M. Roche, Performance Validation Approach for the GTX AirBreathing Launch Vehicle, NASA/TM–2002-211495, 2002.
- [6] U.B. Mehta, M.J. Aftosmis, J.V. Bowles, S.A. Pandya, Skylon aerodynamics and SABRE plumes, in: 20th AIAA International Space Planes and Hypersonic Systems and Technologies Conference, American Institute of Aeronautics and Astronautics, 2015.
- [7] J.A. Medina, H. Patel, B. Chudoba, Inlet sizing of hypersonic vehicles for conceptual design, in: ASCEND 2021, American Institute of Aeronautics and Astronautics, 2021.
- [8] C. Yunseok, M. Yost, E. Lerner, J.F. Driscoll, Model of a JP-7-fueled generic X51 vehicle: effects of varying scramjet flowpath, in: AIAA Scitech 2021 Forum, American Institute of Aeronautics and Astronautics, 2021.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. 激励源简化：强迫振动振幅和频率范围未必能覆盖真实发动机、噪声和气动压力谱。
2. 工况单一：Mach 6、24 km 是关键点，但进气道全飞行包线下厚度下限可能不同。
3. 二维模型限制：作者承认结果不适用于轴对称或三维进气道，实际高超声速进气多有三维效应。
4. 热效应不足：aerothermoelastic 和热应力可能进一步改变刚度、频率和结构强度，本文主要关注机械/流固振动。
5. 材料与制造约束：厚度下限只考虑性能/频率，未深入重量、加工、连接、加强筋布局和疲劳寿命。
6. 评价指标有限：总压恢复和质量流量重要，但进气道稳定性、畸变、边界层分离、unstart margin 未充分展开。
7. 图表复核：模态图、压力/速度云图、Table 7 数值和 Fig. 21 交叉点需要 PDF 图像复核。

## 17. 可复用资产

- 选题资产：把“构型参数设计”之后的“物理尺寸设计”作为 gap，非常适合工程系统论文。
- 方法资产：经典设计准则 + CFD 修正 + 结构模态 + 强迫振动 + FSI 的多层验证路径。
- 证据资产：先扫结构厚度，再扫激励振幅/频率，最后做耦合仿真，证据逐层逼近真实。
- 图表资产：把 natural frequency 与 operational frequency 随厚度变化画在一起，直接形成尺寸判据。
- 写作资产：主动在结论中限定适用范围，降低外推风险。
- 指标资产：用 σ 和 φ 同时衡量进气性能，比只看一个指标更稳。

## 18. 对我写论文的启发

如果研究工程设计问题，可以把“已有方法已经能决定 A，但还不能决定 B”作为强 gap。本文就是：已有气动准则能决定冲击角和压缩角，但不能决定薄板厚度。这种 gap 比笼统说“研究不足”更精准。

另一个启发是设计路径要有从低成本到高保真的层级。先做模态筛选，再做强迫振动 CFD，再做 FSI，是合理的计算经济性安排。自己的论文如果涉及复杂耦合，也可以采用“先分解、后耦合、再综合判据”的证据组织。

第三点是结论要落到可用数值。本文最终给出 5.5、6.0、6.5 mm，这让读者感觉研究完成了设计任务，而不是只展示仿真现象。

## 19. 最终浓缩

这篇论文的核心是：高超声速三段外压缩进气道不能只按 shock-on-lip 和 Oswatitsch 准则确定角度与长度，还必须把薄面板振动带入物理尺寸设计。作者通过模态分析、强迫振动流场和 FSI 仿真，证明面板厚度影响自然频率、位移和总压/流量波动，并给出 CI/CII/CIII 厚度下限 5.5/6.0/6.5 mm。最值得学习的是“构型参数 -> 物理尺寸 -> 性能约束”的设计链条；最需要复核的是 Fig. 14-22 的曲线细节、Table 7 的 FSI 性能数值和厚度判据的图像依据。
