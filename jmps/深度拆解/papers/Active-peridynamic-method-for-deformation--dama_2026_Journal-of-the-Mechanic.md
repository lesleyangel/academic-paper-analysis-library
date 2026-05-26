# Active peridynamic method for deformation, damage and healing analysis of cell monolayers

## 0. 读取说明
- 源 PDF：`jmps/文献/Active-peridynamic-method-for-deformation--dama_2026_Journal-of-the-Mechanic.pdf`
- 源 TXT：`jmps/文本/txt/Active-peridynamic-method-for-deformation--dama_2026_Journal-of-the-Mechanic.txt`
- 元数据：Journal of the Mechanics and Physics of Solids, 213 (2026) 106608, DOI: 10.1016/j.jmps.2026.106608。
- 是否需要结合 PDF 图像核查：需要。本文涉及生物裂纹图像、细胞单层裂纹/愈合图、Drosophila dorsal closure 形态、病变皮肤裂纹模式等，当前只能从 txt 与图注判断图表功能，不能确认图像细节、曲率测量和实验对照强度。
- 本文类型：生物断裂问题的多尺度主动 peridynamics 方法论文，兼具机制建模和代表性数值算例。

## 1. 基本信息与论文身份
- 题名：Active peridynamic method for deformation, damage and healing analysis of cell monolayers。
- 作者/机构：Shiyuan Chu; Jinshuai Bai; Guozheng Kang; Qunyang Li; Xi-Qiao Feng。机构主要为清华大学、Mechano-X Institute 和西南交通大学。
- 关键词：Peridynamics; Cell monolayer; Cracking; Healing; Intercellular interface; Mechano-chemo-biological coupling。
- 研究对象：细胞单层中的变形、细胞-细胞界面键断裂、裂纹扩展、愈合，以及 RhoA/actomyosin 等生化信号与力学反馈。
- 研究尺度：细胞单层组织尺度、cell-cell interfacial bonds (CCIBs)、catch-slip bond、非局部 peridynamic material points。
- 方法类型：classical peridynamic theory + catch-slip bond constitutive law + displacement-based cohesive failure + biochemical active deformation + diffusion/inhibition feedback。
- 证据类型：上皮单层 indentation test、Drosophila embryogenesis dorsal closure、diseased skin microcracking patterns 三类数值例子，与实验观察/文献图像进行对照。
- 目标读者：生物力学、断裂力学、peridynamics、组织形态发生、细胞力学生物学和计算组织工程读者。
- JMPS 风格定位：将“生物裂纹”从现象图谱提升为一个能同时处理大变形、断裂、愈合和生化反馈的非局部力学框架。

## 2. 摘要与核心信息提取
摘要先把 fracture 写成生物系统中的普遍现象，跨 embryogenesis、disease progression、engineered tissues 和 organoids。随后提出核心方法：multiscale mechano-chemo-biological peridynamic framework，将 catch-slip bond model 与 peridynamic theory 集成。中间用关键机制支撑方法必要性：intercellular connections 被建模为 CCIBs，constitutive relation 含 catch-slip behavior，bond failure 用 displacement-based cohesive criterion，active deformation 受 actomyosin/RhoA 等信号调控，而信号又通过 deformation-dependent diffusion/inhibition 接收力学反馈。结果句说明该框架可模拟 large deformation、cracking、healing，并在病理条件下捕捉裂纹图案时空演化和曲率效应。

一句话主张：细胞单层的裂纹与愈合可被视为由细胞-细胞界面键断裂/重连、catch-slip adhesion 和 RhoA-actomyosin 反馈共同驱动的主动 peridynamic 过程。

核心关键词：active peridynamics；CCIB；catch-slip bond；damage-healing；RhoA-actomyosin feedback；biological fracture。

摘要写作最值得学习的是把多尺度机制压缩得很有层次：界面键给离散力学单元，catch-slip 给微观黏附本构，cohesive criterion 给断裂，biochemical signals 给主动变形，feedback 给时空耦合。

## 3. 选题层深拆
问题来源很有 JMPS 的跨界味道：生物系统中 fracture 既可能是生理过程，如胚胎形态发生、皮肤/器官结构形成，也可能是病理过程，如 pemphigus、ichthyosis、aortic dissection 等。传统材料断裂主要由外部载荷诱发，而生物组织能主动产生内力、通过生化信号调节粘附和收缩，并具有愈合能力。

问题为什么重要：如果不能把 mechanical fracture、biochemical signaling 和 healing 放在同一框架里，就难以解释为什么有些裂纹是发育程序的一部分，有些裂纹是疾病进展的结果，也难以预测 tissue engineering/organoid 中的破裂风险。

问题为什么现在值得做：peridynamics 已经成熟到能处理裂纹萌生和扩展，无需传统局部微分方程在 crack tip 的奇异性；cell biology 也积累了 catch-slip bonds、RhoA、actomyosin、cell-cell junction 等机制知识，可以转化为可计算状态变量。

问题边界：本文面向 cell monolayers，而非三维多组分组织；每个 cell 近似为单个 material point；细胞内部变形、ECM、vasculature、真实免疫反应等都未完整纳入。

选题可迁移性：非常适合写“传统工程理论进入生命系统”的论文。关键是不要简单套用工程断裂，而要指出生物系统新增的 active deformation、healing 和 biochemical feedback。

## 4. 领域位置与文献版图
作者把文献组织成四类。第一类是生物断裂现象文献，覆盖胚胎、皮肤、疾病、动物 survival strategies 和 tissue engineering。第二类是 continuum mechanics 模型，可描述组织整体软化或曲率耦合，但 crack tip stress singularity 会破坏局部微分方程适用性。第三类是 cell-based/vertex/discrete particle models，可避免奇异性、描述细胞尺度交互，但 fracture criteria 常依赖经验阈值，缺少 fracture toughness/energy dissipation。第四类是 peridynamics，它以 integral form 表述非局部相互作用，可自然处理裂纹萌生与扩展，并能引入 energy release rate。

本文站在 peridynamics 与 cell biology 交叉处：继承 peridynamic fracture 的非局部断裂能力，同时加入 catch-slip intercellular adhesion、active biochemical deformation 和 healing rule，使其从被动材料断裂扩展到主动生物组织。

最接近前人：Silling peridynamics、细胞离散模型、catch-slip bond 模型、RhoA/actomyosin feedback 研究，以及作者团队关于生物皮肤/曲面裂纹的工作。

是否公平处理前人：总体公平，承认 continuum 和 cell-based 模型的贡献，再指出它们各自缺失：一个有奇异性，一个缺 fracture mechanics 参数。风险是本文的 displacement-based cohesive criterion 与 energy-based PD fracture 的关系需要解释清楚。

## 5. Gap 制造机制
明示 gap：现有 continuum models 受 crack-tip singularity 限制；cell-based models 常用经验长度/应力阈值，不能反映 fracture toughness 或 energy dissipation；传统 PD 又缺少细胞界面主动生化机制。

隐含 gap：生物组织裂纹不是单向破坏，常伴随 healing、cell migration、actomyosin contraction 和 signal redistribution；若只处理 bond breaking，无法解释闭合、愈合和病理裂纹图案演化。

gap 类型：方法 gap + 机制 gap + 多尺度 gap。方法上需要非局部断裂；机制上需要 catch-slip 和 biochemical feedback；多尺度上需要从细胞界面键到单层组织图案。

gap 证据来自引言中对 continuum/cell-based/PD 的逐层比较。作者没有把 gap 写成“没人做过”，而是写成“每类工具都缺一个关键能力”，从而使集成式方法合理。

审稿追问：APD 是否真正比已有 cell-based cohesive models 多出可验证预测；catch-slip 参数和生化参数来自何处；healing criterion 是否经验化；病理皮肤图案对照是否只是形貌相似。

## 6. 创新性判断
作者声称的贡献是 multiscale active peridynamic method，用于 cell monolayers 的 deformation、damage 和 healing。真实创新在于把三套机制放进一个可计算框架：PD nonlocal bonds 处理裂纹；CCIB catch-slip constitutive law 处理细胞间黏附强度随力变化；RhoA/actomyosin feedback 处理 active deformation 与 biochemical signaling；damage/healing criteria 处理断裂和重连。

创新类型：方法创新 + 生物机制整合 + 应用验证。强度中高。PD 不是新的，catch-slip 不是新的，但把它们用于细胞单层裂纹与愈合，并通过三个代表生物场景展示，是明显的整合创新。

创新必要性：强。没有 PD，裂纹萌生和复杂裂纹网络难以自然模拟；没有 active biochemical coupling，模型只能描述被动破坏，无法解释由疾病或发育信号驱动的裂纹/闭合。

创新与证据匹配度：示例覆盖 indentation、dorsal closure 和 diseased skin，说明框架有广泛适应性；但每个例子验证深度有限，更多是 representative demonstration。

容易被挑战处：每个 cell 单点化会忽略细胞内部形变；三维组织和 ECM 未纳入；生化网络简化可能影响真实疾病机制解释。

## 7. 论证链条复原
背景：生物系统中的 fracture 普遍存在，且既有生理功能也有病理后果。 -> 文献：continuum models 能描述组织层力学但受裂尖奇异性困扰；cell-based models 能描述细胞连接但 fracture criteria 经验化；PD 能处理断裂但缺少主动生物机制。 -> gap：需要一个同时处理 cell-cell adhesion、fracture energy、active biochemical feedback 和 healing 的非局部框架。 -> 问题：如何模拟 cell monolayers 的大变形、裂纹、愈合和生化信号耦合。 -> 方法：用 PD material points 表征细胞，CCIB 表征界面键，引入 catch-slip law、cohesive failure、healing states、RhoA-actomyosin feedback。 -> 证据：Fig. 2-7 模型机制图，Fig. 8 indentation，Fig. 9 dorsal closure，Fig. 10 diseased skin cracks。 -> 发现：模型可再现 epithelial monolayer hardening、dorsal closure bridging effect、病变皮肤裂纹时空演化，以及局部曲率半径与皮肤碎片尺寸的反比关系。 -> 意义：为生理形态发生、病理裂纹和组织工程提供可扩展计算工具。

链条闭合度较好，尤其是文献 gap 与方法模块对应。最薄弱处在“实验观察一致”到“生物机制被证明”之间，当前更像形态和趋势一致，不是完全机制识别。

## 8. 方法/理论/模型细拆
方法总框架由五层组成。第一层是 peridynamic theory：将连续体离散为 material points，通过 horizon 内 bonds 相互作用，避免传统裂纹尖端奇异。第二层是 CCIB constitutive law：细胞间界面键承受相对位移，分解为 mode-I 和 mode-II 分量，并采用 catch-slip 行为描述黏附强度随拉伸/加载变化。第三层是 damage and healing criteria：过大拉伸导致 CCIB rupture，卸载或信号调节可促进 healing/reconnection。第四层是 molecular mechanisms：E-cadherin、linkers、actomyosin contraction 和 RhoA 信号调控界面主动变形。第五层是 mechano-chemo-biological framework：RhoA、actomyosin 和 CCIB stretch 构成反馈系统，含 deformation-dependent diffusion 和 inhibition。

关键变量：cell-cell bond stretch、mode-I/II displacement components、bond damage state、healing state、RhoA concentration、actomyosin concentration、active deformation、diffusion coefficient、inhibition term。

关键假设：细胞单层可由点-键网络代表；细胞内部变形可忽略；界面键主导断裂；生化信号网络可简化为 RhoA-actomyosin-stretch 三组分反馈；fracture/healing 可由局部 CCIB 状态规则描述。

复现信息：公式和图注给出主要框架，算例设置需结合 PDF 和补充材料核查。尤其是参数值、网格/horizon、时间步、boundary conditions、皮肤图像曲率提取方法，需要原文表格和图像确认。

方法复杂度合理，因为每一层对应生物裂纹的一项必要特征：非局部裂纹、界面黏附、主动收缩、化学反馈、愈合。若移植到其他组织，需要重估 CCIB law 和生化网络。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 生物裂纹需要 mechano-chemo-biological coupling 而非单纯被动断裂 | Introduction/Fig. 1 | 胚胎、疾病、动物 survival、组织工程多类 fracture phenomena | 文献图谱 | 中强 | 图谱广泛但不等于同一机制 |
| APD 可将 cell-cell interface bonds 与 PD fracture 结合 | Method/Fig. 2-3 | CCIB 模型、相对位移分解、peridynamic formulation | 理论建模 | 强 | 参数标定需核查 |
| catch-slip 和 cohesive criterion 可描述界面损伤 | Method/Fig. 6 | damage/healing states、过大 tensile loading 断裂、卸载后修复 | 模型规则 | 中强 | healing 规则可能经验化 |
| RhoA-actomyosin-stretch 反馈可驱动主动裂纹/愈合 | Method/Fig. 7 | 三组分 feedback system、deformation-dependent diffusion/inhibition | 机制模型 | 中 | 生化网络简化较强 |
| APD 可再现 epithelial monolayer indentation hardening | Example 3.1/Fig. 8 | indentation device 和 simulation/experimental trend 对照 | 数值-实验对照 | 中强 | 需看曲线误差 |
| APD 可捕捉 Drosophila dorsal closure bridging effect | Example 3.2/Fig. 9 | dorsal closure 几何和 loading condition，模拟闭合过程 | 生物过程算例 | 中 | 真实细胞迁移/增殖未完整纳入 |
| 病变皮肤裂纹曲率效应与实验观察一致 | Example 3.3/Fig. 10 | ichthyosis 皮肤裂纹图与模拟 microcracking patterns 对比 | 图像形貌对照 | 中 | 需要 PDF 图像和定量曲率核查 |

证据系统的优势是覆盖从机制到应用的不同层次；不足是每个应用例子验证深度有限，更多证明框架“能表达”，不完全证明“唯一正确”。

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 生物断裂现象总览 | fracture 在生物中普遍且多功能 | 制造选题重要性 | 是 |
| Fig. 2 | intercellular junction model | CCIB 是力学生物桥梁 | 把细胞界面物理化 | 是 |
| Fig. 3 | relative displacement decomposition | mode-I/II 界面位移可定义 | 为本构 law 铺垫 | 否/部分 |
| Fig. 6 | CCIB damage and healing states | 断裂与愈合可由状态转移描述 | 建立可计算 state machine | 是 |
| Fig. 7 | RhoA-actomyosin-stretch feedback | 生化信号与力学反馈闭环 | 体现 active PD 的“active” | 是 |
| Fig. 8 | epithelial monolayer indentation | 模型可预测硬化行为 | 第一个验证算例 | 是 |
| Fig. 9 | dorsal closure | APD 可表达发育闭合/bridging | 生理应用验证 | 是 |
| Fig. 10 | diseased skin microcracking | 模拟病理裂纹图案 | 最具视觉冲击的应用证据 | 是 |
| PD integral equations | 非局部相互作用 | 避免 crack-tip singularity | 方法合法性 | 否 |
| Cohesive/displacement failure rule | CCIB rupture | 连接 fracture criterion 与 cell bond | 关键内部规则 | 否 |

图表顺序非常有教学价值：先用 Fig. 1 建立现象宇宙，再用 Fig. 2-7 建立模型零件，最后用 Fig. 8-10 放入三个生物场景。这个顺序适合复杂多机制方法论文。

## 11. 章节结构与篇章布局
- Abstract：压缩现象、框架、机制、算例和意义。
- Introduction：大范围生物 fracture 图景 -> continuum/cell-based/PD 文献比较 -> 本文框架定位。
- Method：从 PD theory 开始，再到 constitutive law、damage/healing criteria、molecular mechanisms、完整 coupling framework，层次明确。
- Examples：三个场景按“工程/实验 benchmark -> 发育过程 -> 病理过程”递进，覆盖范围逐渐扩大。
- Conclusions：先总结方法，再总结三个算例的对应发现，最后主动承认 3D tissues、ECM、vasculature、single material point per cell 等局限。

最值得模仿的是 Method 章节的模块化标题。它没有把所有机制混在一个大框架里，而是让读者逐步认识 PD、CCIB、本构、损伤、分子机制和反馈。

结构风险：Results/Examples 数量不多且每个例子较大，若图像对照不够定量，读者可能觉得“应用面广但验证浅”。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Active-peridynamic-method-for-deformation--dama_2026_Journal-of-the-Mechanic.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：12
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 机制/讨论型, 结论/展望型, 背景/引言型, 问题/机制型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Method | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Peridynamic theory | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Constitutive law | 问题/机制型 | 围绕变量关系或机制问题组织读者预期 | 高 | 是 | 保留具体变量/对象 |
| 2.3 Damage and healing criteria | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.4 Molecular mechanisms | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.5 Mechano-chemo-biological peridynamic framework | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Examples | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1 Indentation test of epithelial monolayers | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.2 Dorsal closure in drosophila embryogenesis | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.3 Skin damage during disease progression | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4 Conclusions | 结论/展望型 | 收束贡献、边界和未来工作 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
Introduction 第一段用大量例子证明 fracture 在生物中不是边缘现象。第二段强调生物断裂与传统材料不同：生物系统能主动产生内力并调节裂纹/愈合。第三到第五段开始比较模型路线，逐步把读者带到 PD。

Method 段落通常遵循“生物概念 -> 力学等效 -> 数学状态变量”。例如 intercellular junction 先有 E-cadherin/actomyosin 图像，再等效为 CCIB；RhoA 和 actomyosin 先是生化信号，再进入 diffusion/inhibition 方程。

Examples 段落遵循“场景介绍 -> 几何/边界 -> 结果现象 -> 与实验观察对照”。这种结构可迁移到任何多算例方法论文。

可复用段落模板：`In contrast to passive materials, biological tissues can [active process]. To capture this feature within a fracture framework, we represent [biological connection] as [mechanical element] whose state evolves according to [mechanical criterion] and [biochemical feedback].`

## 13. 文笔画像与语言习惯
文笔具有“宽背景 + 机制密集”的特点。Introduction 中用 ubiquitous, dualistic, physiological, pathological 等词拓展问题重要性；Method 中则切换到 represented by, incorporates, described by, regulated by, feedback through 等工程化表达。

claim 强度适中。作者在摘要中说 robust demonstrated, good agreement, reliable computational tool，但结论中也清楚写出模型可扩展方向和当前限制，降低审稿阻力。

高频词族：fracture, damage, healing, cell monolayer, intercellular, bond, active, biochemical, RhoA, actomyosin, peridynamic, crack, curvature。文中不断用“mechanical-biochemical feedback”把多学科词汇粘合起来。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：cell(57)；model(34)；fracture(32)；chu(29)；mechanical(27)；method(25)；biological(25)；apd(24)；cells(23)；peridynamic(22)；deformation(22)；actomyosin(22)；tissue(22)；healing(21)；material(21)；damage(20)；active(19)；systems(18)；biochemical(18)；energy(18)
- 高频学术名词：deformation(44)；model(34)；fracture(32)；method(25)；material(21)；energy(18)；closure(17)；analysis(16)；failure(15)；curvature(15)；transition(14)；displacement(14)；stress(12)；simulation(12)；interface(11)；framework(11)
- 高频学术动词：proposed(11)；capture(7)；simulate(6)；demonstrated(6)；shows(4)；predict(3)；compare(3)；validate(2)；formulated(2)；investigate(2)；show(2)；demonstrate(2)；develop(2)；shown(2)；derived(2)；simulated(2)
- 高频形容词：mechanical(27)；biological(25)；peridynamic(22)；material(21)；critical(20)；active(19)；biochemical(18)；dorsal(16)；cohesive(14)；displacement(14)；theoretical(12)；local(12)；experimental(12)；dynamic(10)；numerical(10)；epithelial(10)
- 高频副词/连接副词：respectively(13)；furthermore(8)；moreover(5)；notably(4)；typically(4)；specifically(4)；accurately(4)；therefore(3)；however(3)；effectively(3)；consequently(2)；experimentally(2)；systematically(2)；actively(2)；finally(2)；sufficiently(2)
- 高频二词短语：cell cell(17)；dorsal closure(14)；biological systems(13)；apd method(12)；cell monolayers(9)；mechanical feedback(9)；catch slip(8)；biochemical signals(8)；closure drosophila(8)；carlson mahadevan(8)；damage healing(7)；active deformation(7)；material points(7)；drosophila embryogenesis(7)；adjacent cells(7)；exp exp(7)
- 高频三词短语：dorsal closure drosophila(8)；closure drosophila embryogenesis(7)；cell cell interface(7)；behaviors cell monolayers(5)；cell cell interfacial(4)；cell interfacial bonds(4)；displacement-based cohesive criterion(4)；catch slip bond(4)；slip bond model(4)；cohesive zone model(4)；pathway distance bound(4)；distance bound transition(4)

**主动、被动与句法**

- 被动语态估计次数：107
- `we + 动作动词` 主动句估计次数：4
- 名词化表达估计次数：581
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：140
- 一般过去时线索：29
- 现在完成时线索：13
- 情态动词线索：40
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：cell(6)；engineering(4)；cracking(4)；deformation(3)；monolayers(3)；university(3)；china(3)；fracture(3)
- 1. Introduction：fracture(26)；biological(12)；systems(10)；cell(9)；chu(8)；tissues(7)；tissue(7)；continuum(7)
- 2. Method：active(3)；systems(3)；peridynamic(2)；based(1)；classical(1)；method(1)；here(1)；formulate(1)
- 2.1. Peridynamic theory：point(8)；cell(8)；kon(8)；cells(7)；linker(7)；force(6)；state(6)；rate(6)
- 2.3. Damage and healing criteria：cell(16)；cohesive(10)；energy(9)；interface(9)；exp(9)；critical(7)；mixed-mode(7)；mode-i(7)
- 2.4. Molecular mechanisms：actomyosin(11)；mechanical(8)；stretch(7)；feedback(7)；rhoa-gtp(7)；yin(6)；cells(6)；rhoa(5)
- 2.5. Mechano-chemo-biological peridynamic framework：tissue(5)；scale(5)；cell(4)；criterion(4)；apd(3)；ccibs(3)；model(3)；ccib(3)
- 3. Examples：model(2)；biological(2)；section(1)；effectiveness(1)；accuracy(1)；proposed(1)；apd(1)；evaluated(1)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 句型骨架：`Damage and fracture are ubiquitous in [systems], spanning processes from [A] to [B].`
- 句型骨架：`A key limitation remains: [method] cannot capture [essential feature].`

### 14.2 方法与框架表达
- 句型骨架：`We develop a multiscale [coupled] framework that integrates [model A] with [theory B].`
- 句型骨架：`[Connections] are modeled as [mechanical elements], whose constitutive relation incorporates [biophysical behavior].`

### 14.3 结果与趋势表达
- 句型骨架：`Simulations capture the spatiotemporal evolution of [pattern], revealing a tight coupling between [signal] and [mechanical feedback].`

### 14.4 机制解释表达
- 句型骨架：`Active deformation of [element] is regulated by [biochemical signals], which in turn receive mechanical feedback through [mechanism].`

### 14.5 贡献与意义表达
- 句型骨架：`This work provides a computational tool for analyzing [class of problems] in [diverse contexts].`

### 14.6 局限与未来工作表达
- 句型骨架：`The model could be extended by incorporating more physiological and pathological features, including [A], [B], and [C].`

## 15. 引用策略与文献使用
引用密度在 Introduction 极高，功能分明。第一组文献支撑“生物 fracture 普遍存在”，覆盖 zebrafish nostril、mouse limbs、crocodile skins、perioral dermatitis、bone fracture、aortic dissection、snake shedding、lizard autotomy、planarian fission、organoids 和 dental implants。第二组文献支撑“生物裂纹由 mechano-chemo-biological coupling 控制”。第三组对比 continuum/cell-based/peridynamics 方法。

引用姿态：对 continuum 和 cell-based 模型是“承认贡献 + 指出限制”，对 PD 是“引入适合性 + 扩展不足”。这使本文看起来不是随意混合，而是沿方法版图自然推进。

references 暗示的研究共同体包括生物力学、细胞黏附、peridynamic fracture、组织形态发生和皮肤裂纹。引用风险是跨学科范围大，任何一侧若引用不全都可能被专业审稿人追问。

## 16. 审稿人视角风险
最大攻击面：生物真实性与模型简化。每个 cell 一个 material point 忽略了细胞内部结构、形变、极性和迁移；真实组织三维、含 ECM 和 vasculature，本文只处理 monolayer。

claim 是否过强：若说“reliable tool for diverse biological contexts”，需要注意当前只展示三个 representative examples，且很多参数可能场景特定。

证据是否不足：病变皮肤裂纹图案对比若没有定量指标，容易被认为只是视觉相似；dorsal closure 的真实生物机制包含细胞迁移、增殖、apoptosis 等，APD 只覆盖力学-生化一部分。

方法复现风险：catch-slip 参数、生化扩散参数、healing threshold、horizon size、mesh sensitivity 都需要明确。

替代解释：裂纹曲率与碎片尺寸的关系可能来自几何约束、材料非均匀性或皮肤多层结构，而不完全来自本文 RhoA-actomyosin feedback。

## 17. 可复用资产
- 可复用选题角度：把传统工程断裂理论推广到主动生命系统，并明确新增机制。
- 可复用 gap 制造：continuum 有奇异性，cell-based 经验化，PD 缺生化机制；本文站在三者交叉处。
- 可复用论证链：生物现象图谱 -> 方法版图比较 -> 非局部框架 -> 生物界面键 -> 生化反馈 -> 多场景验证。
- 可复用图表设计：一张现象总览图 + 多张模型模块图 + 三个应用算例图。
- 可复用句型：`This differs essentially from [traditional system], where [passive mechanism]; in contrast, [biological system] can [active mechanism].`
- 不宜直接模仿处：不要在只做二维单层模型时对三维组织疾病作过强机制结论。

## 18. 对我写论文的启发
如果我要写生物力学模型论文，可以学习本文怎样“先尊重生物复杂性，再做力学抽象”。最好的写法不是把生物组织当普通材料，而是明确传统材料缺少哪些主动过程，然后逐一把它们变成模型模块。

Introduction 可学：用生理、病理、工程三类例子共同证明问题重要。Method 可学：每个生物机制都要有一个力学等效对象。Results 可学：用代表性场景展示框架可扩展，但在结论里主动承认尚未处理的真实复杂性。

需要避免的问题：不要把模型模块堆得太多却没有对应验证；不要把图像相似当作充分机制证明；不要忽略参数来源和敏感性。

## 19. 最终浓缩
这篇论文最值得学的是：如何将 peridynamic fracture、cell-cell adhesion、catch-slip bonds、RhoA-actomyosin feedback 和 healing state 整合成一个能表达生物裂纹时空演化的主动非局部框架。

最大风险是：细胞和组织的生物真实性被简化较多，三维组织、ECM、细胞内变形和真实愈合机制仍未纳入。

三个可迁移动作：1. 用方法版图比较制造集成式创新的必要性；2. 把每个生物机制转成清晰的力学状态变量；3. 用多个代表性场景展示框架，但严格区分形貌一致、趋势一致和机制验证。
