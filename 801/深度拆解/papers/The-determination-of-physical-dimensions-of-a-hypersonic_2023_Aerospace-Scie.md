# The determination of physical dimensions of a hypersonic three-stage compression system considering panel vibration effects

## 0. 读取说明

本文拆解基于 `801/文本/txt/The-determination-of-physical-dimensions-of-a-hypersonic_2023_Aerospace-Scie.txt` 的全文抽取，并参考 `801/文本/metadata/The-determination-of-physical-dimensions-of-a-hypersonic_2023_Aerospace-Scie.json` 的目录。metadata 中 title/author 字段为空，但全文首页和 toc 给出题名、作者与期刊信息。txt 存在双栏串栏，尤其是 Fig. 14-22 与 Table 7 附近，图题、正文和表格混排明显；涉及压力/速度云图、模态振型、频域曲线、三维流动图像和表格数值处均标注“需要 PDF 图像复核”。本文不复述长段原文，只对 shock-on-lip、Oswatitsch criterion、panel vibration、total pressure recovery、mass flow coefficient 等关键词做分析。

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

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/The-determination-of-physical-dimensions-of-a-hypersonic_2023_Aerospace-Scie.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：6
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 机制/讨论型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 3.1 Mode analysisable thickness of compression ramp panels should be determined | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.1.1 Vibration differential equation | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2.2 Computational region, boundary conditions and mesh | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.2.1 Governing equations | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.2.2 Effects of vibration frequency | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.4 Design path of compression system | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 的节奏是：先讲进气系统重要性，再讲二维多级压缩系统的构型设计准则，然后转入薄板振动风险，最后指出尺寸设计路径缺失。这个节奏很有效，因为它先承认现有气动设计成熟，再指出其没覆盖结构振动。

方法段落采用“仿真任务清单”式推进：mode analysis、flow field with vibrational structural boundaries、FSI analysis。每个模型都先给公式/边界/网格，再给评价指标。这样写的好处是工程可复现性强，缺点是文本较密，公式和图表多，读者需要频繁对照。

结果段落节奏是“厚度 -> 振幅 -> 频率 -> FSI -> design path”。它不是随机扫参，而是从结构变量到激励变量，再到耦合真实变量。结论段则将结果压成五条，最关键的是自然频率/运行频率关系和厚度下限。

## 13. 文笔画像与语言习惯

文笔是典型 Aerospace Science and Technology 工程仿真论文：句子偏长，名词组合多，强调 design path、available thickness、structural and intake performance。高频词包括 compression ramps、panel vibration、intake performance、total pressure recovery coefficient、mass flow coefficient、fluid-structural interaction、natural frequency、operational frequency。

作者常用 “from the structural and flow point of views”“it can be found that”“in this work” 等表达。主动语态用于提出流程和判断，被动语态用于仿真设置。结果解释多用因果句，如振动使 shock wave spill out、three-dimensional effects 导致性能下降、stiffness 增加使波动降低。

文章语气总体稳健，结论中主动限定“specific results and data only available for the two-dimensional intake system with three-stage compression ramps under Mach 6 and altitude 24 km”，这对审稿风险控制很重要。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：panel(88)；vibration(83)；intake(75)；compression(70)；system(51)；performance(48)；pressure(48)；cii(48)；ciii(48)；coe(44)；respectively(43)；thickness(43)；frequency(42)；hypersonic(40)；work(37)；design(30)；ramps(30)；effects(29)；conditions(29)；total(29)
- 高频学术名词：vibration(83)；system(51)；performance(48)；pressure(48)；thickness(43)；analysis(40)；conditions(29)；uctuation(26)；structure(24)；displacement(24)；results(23)；deformation(22)；interaction(22)；condition(20)；simulation(18)；science(17)
- 高频学术动词：shown(15)；show(12)；shows(11)；simulated(6)；indicates(5)；simulate(4)；indicate(4)；developed(4)；compared(3)；evaluated(2)；validate(1)；reveal(1)；captured(1)
- 高频形容词：hypersonic(40)；total(29)；cient(29)；numerical(26)；uid-structural(26)；structural(26)；displacement(24)；natural(21)；boundary(19)；different(18)；available(17)；internal(15)；dynamic(14)；operational(13)；static(12)；external(12)
- 高频副词/连接副词：respectively(43)；nally(6)；however(3)；tively(3)；spectively(3)；numerically(2)；finally(2)；closely(2)；widely(2)；relatively(2)；commonly(1)；actually(1)；uniformly(1)；obviously(1)；sequentially(1)；cally(1)
- 高频二词短语：cii ciii(38)；panel thickness(34)；intake system(31)；coe cient(27)；total pressure(23)；pressure recovery(22)；compression ramps(20)；intake performance(20)；mass coe(19)；aerospace science(16)；science technology(16)；coe cients(16)；panel thicknesses(15)；recovery coe(15)；gou jia(14)；jia aerospace(14)
- 高频三词短语：total pressure recovery(20)；aerospace science technology(16)；gou jia aerospace(14)；jia aerospace science(14)；recovery coe cient(12)；pressure recovery coe(10)；mass coe cient(9)；mass coe cients(9)；pressure recovery mass(8)；recovery mass coe(8)；different panel thicknesses(8)；increase panel thickness(8)

**主动、被动与句法**

- 被动语态估计次数：142
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：600
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：283
- 一般过去时线索：40
- 现在完成时线索：2
- 情态动词线索：81
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：intake(45)；compression(39)；system(35)；vibration(28)；performance(19)；hypersonic(18)；structural(18)；ramps(18)
- 3.2.1. Governing equations：panel(71)；vibration(55)；pressure(43)；cii(42)；ciii(42)；coe(39)；respectively(38)；frequency(38)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

高频术语：shock-on-lip criterion、Oswatitsch criterion、viscous effects modification、panel thickness、mode analysis、forced vibration、fluid-structural coupling、total pressure recovery coefficient、mass flow coefficient、operational frequency。

可复用 gap 句式：`A clear design path considering various vibration sources, high uncertainty and complex design objectives is essential while still absent.` 适合写工程流程缺失。

可复用方法句式：`The structural design path should have three branch paths: avoiding too high stress, averting resonance, and maintaining intake performance.` 适合多约束尺寸设计。

可复用结果句式：`The consideration of panels' fluid-structural interaction will lead to the reduction and fluctuation of total pressure recovery and mass flow coefficients.` 适合描述 FSI 对性能指标的影响。

可复用边界句式：`The specific results and data are available only for the studied configuration and flight condition.` 适合在结论中主动控制适用范围。

## 15. 引用策略与文献使用

引用策略有三层。第一层是进气道构型与经典设计准则，引用 axisymmetric、two-dimensional、three-dimensional intake 的代表项目和 shock-on-lip/Oswatitsch 设计理论。第二层是复杂高超声速流动和气动弹性现象，包括 turbulent boundary layers、aeroelastic effects、dynamic aeroelastic effects、aerothermoelastic effects、shock-wave-boundary-layer interactions、thermochemical/high-temperature non-equilibrium effects。第三层是用于模型验证的参考算例，包括压力系数和动态压力位移对比。

这种引用组织的作用是把本文放在“成熟气动设计之后、结构振动约束之前”的位置。作者不是说前人错，而是说前人解决的是构型参数，本文补 physical dimensions。

引用风险在于 FSI/振动激励源的真实谱可能没有充分文献约束。若审稿人要求发动机推力变化或噪声激励的谱特征，本文的强迫振动参数范围可能被认为是工程假设而非充分实测输入。

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
