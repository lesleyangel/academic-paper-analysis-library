# Finite deformation theory for growth-inspired conformal integration with programmable stress state

## 0. 读取说明
- 源 PDF：`jmps/文献/Finite-deformation-theory-for-growth-inspired-co_2026_Journal-of-the-Mechani.pdf`
- 源 TXT：`jmps/文本/txt/Finite-deformation-theory-for-growth-inspired-co_2026_Journal-of-the-Mechani.txt`
- 元数据：`jmps/文本/metadata/Finite-deformation-theory-for-growth-inspired-co_2026_Journal-of-the-Mechani.json`
- 读取范围：基于 TXT 中的题名、摘要、关键词、Introduction、方法/理论/模型、结果、讨论/结论、图题图注、附录与参考文献线索进行拆解。
- 图像核查：本文所有涉及曲线形状、图像纹理、颜色尺度、误差带、场分布细节的判断，均需后续结合 PDF 图像核查；本文件只基于 TXT 中可读图注和正文描述。
- 本文类型：有限变形理论与逆向设计论文。它把曲面贴合中的几何映射问题和应力状态设计问题统一起来，服务于曲面电子、软材料贴合和生长启发形变。

## 1. 基本信息与论文身份
- 题名：Finite deformation theory for growth-inspired conformal integration with programmable stress state
- 作者/机构：Yingchao Zhang; Wei Jian; Xue Feng。机构为清华大学航天航空学院/工程力学系与柔性电子技术全国重点实验室。
- 期刊/年份/卷页：Journal of the Mechanics and Physics of Solids, 213 (2026) 106619; DOI: 10.1016/j.jmps.2026.106619
- 关键词：Conformal integration; finite deformation theory; conformal mapping; quasi-conformal mapping; stress programming; interfacial traction; membrane resultant
- 研究对象：平面薄体/有限厚度体贴合到不可展曲面，典型算例为 disc-to-sphere attachment；核心变量为 QC dilatation K、areal stretch A、界面牵引和膜合力。
- 方法类型：有限变形运动学、morphoelastic multiplicative decomposition、Kirchhoff-Love 轴对称假设、Neo-Hookean 不可压材料、共形/准共形/等面积/graded-QC 映射解析、应力相图。
- 证据类型：Fig.1-2 给构型和映射类；Fig.3-9 展示四类映射的角度-面积权衡和增长场；Fig.10-12 给界面压缩、膜张力和相图；关键公式包括 K 与 A 不变量、总变形分解 F=FeFg、平衡方程、应力边界和相图边界。
- 目标读者：JMPS 的材料力学、连续介质力学、实验力学、计算力学或交叉方法读者；他们关心的不是单个现象是否有趣，而是现象能否被变量、方程、图表和边界条件闭合。
- JMPS 风格定位：这篇文章的价值不是把一个对象介绍一遍，而是把对象放进可验证的力学机制链条中。它具备 JMPS 偏好的三个要素：问题具体、变量可定义、证据能对应 claim。对于写作者而言，最值得关注的是作者如何把“现象”变成“可争辩但可检验的力学命题”。

## 2. 摘要与核心信息提取
- 摘要功能拆解：摘要先交代领域问题和旧方法不足，再用一两个方法动词声明本文做了什么，随后列出最能支撑贡献的结果，最后把意义回收到机制、预测或设计能力上。它不是背景综述式摘要，而是高度压缩的论证链。
- 背景句承担：把研究对象放到更大力学问题中，使读者知道这不是孤立算例。
- gap 句承担：指出已有知识、方法或实验中缺少的关键环节，通常是“已经能观察/模拟/讨论 A，但还不能解释/预测/量化 B”。
- 方法句承担：给出本文的身份标签，说明是实验、理论、数值、贝叶斯、热力学还是量子映射等哪类贡献。
- 结果句承担：用最少的变量表达最强发现，避免把所有图表结果平均铺开。
- 意义句承担：把发现从个案推回到机制理解、设计原则、可计算框架或实验判据。
- 一句话主张：通过生长启发的有限变形框架，可以把平面到曲面的局部映射和应力状态分开设计：共形、准共形、等面积和 graded-QC 各自控制角度与面积失真，而应力可通过厚度和设计参数形成界面压缩/膜内张力的稳定区域。
- 核心关键词：对象变量、状态变量、机制判据、验证闭环、适用边界。
- 摘要可学点：摘要中的强 claim 都有后文图表或公式对应；没有把“重要”写成口号，而是通过可测指标、可推导变量和对照组来体现重要性。

## 3. 选题层深拆
- 问题来源：现有生长力学多做 forward morphology 或简化板壳逆设计，计算几何多优化映射失真但不处理应力；曲面电子等实际系统既需要几何贴合，也需要避免起皱和脱粘。因此缺少一个同时 co-design local map and stress state 的有限变形框架。
- 为什么重要：该问题牵动的是“局部机制如何决定整体响应”或“复杂对象如何进入连续/可计算/可实验框架”的 JMPS 核心关切。如果不能解决，领域只能停留在经验描述、单次模拟或不可外推的观察。
- 为什么现在值得做：已有文献已经积累了足够的现象、工具和基准，使作者可以把问题收束到一个清晰缺口；同时实验、计算或理论手段已经成熟到足以提供证据闭环。
- 问题边界：本文没有试图解决整个领域全部问题，而是把边界限定在 平面薄体/有限厚度体贴合到不可展曲面，典型算例为 disc-to-sphere attachment；核心变量为 QC dilatation K、areal stretch A、界面牵引和膜合力。。这种边界感很重要，因为它让最强结论有明确适用条件。
- JMPS 味道：选题不是“把新工具用到老问题”，而是工具和问题互相需要。方法的复杂度来自缺口本身，而不是为了制造高阶感。
- 可迁移性：如果自己的论文也有类似选题，可以学习其收束方式：先列出已有研究已经做到什么，再指出仍缺哪个变量、哪种边界条件、哪类观测或哪条机制链，最后把本文限定为补上这一个环节。
- 潜在审稿追问：这个 gap 是否真的没有被最近文献处理？本文边界是否过窄以至于意义不足？方法复杂度是否与问题难度匹配？

## 4. 领域位置与文献版图
文献版图由 3D 曲面电子/仿生器件、生长力学/非欧几里得板壳、计算几何的 conformal/QC mapping 三块组成。作者通过对比指出：器件文献有应用需求，生长文献有力学框架，图形学文献有几何工具，但缺少有限厚度、可编程应力和贴合可靠性之间的桥梁。

- 作者如何划分已有研究：通常不是按时间简单排队，而是按功能分组：提供基本理论的文献、提供现象证据的文献、提供方法工具的文献、提供最接近对照的文献。
- 每类研究解决了什么：基础理论给术语和守恒/本构/几何合法性；实验或模拟文献证明现象存在；方法文献提供可继承工具；最近工作制造本文 novelty 的直接参照。
- 每类研究留下什么不足：旧理论可能太理想，实验可能只能观察结果，数值可能缺解析或物理解释，跨领域工具可能没有纳入力学边界。
- 本文站在哪条线上：它不是推翻前人，而是在前人交叉处补一个缺少的中介变量、机制判据或可执行框架。
- 是否公平处理前人：从 TXT 可见作者总体采取温和姿态，先承认已有贡献，再指出“not yet address / remains unclear / limited by”这类边界。这样的写法比直接说前人错误更容易被 JMPS 审稿人接受。

## 5. Gap 制造机制
- 显式 gap：现有生长力学多做 forward morphology 或简化板壳逆设计，计算几何多优化映射失真但不处理应力；曲面电子等实际系统既需要几何贴合，也需要避免起皱和脱粘。因此缺少一个同时 co-design local map and stress state 的有限变形框架。
- 隐含 gap：读者不仅需要知道“还没有人做”，还需要知道“为什么已有工具不能自然解决”。本文的隐含 gap 往往在于缺少能把观测、变量、理论和图表连接起来的中间层。
- gap 类型：方法 gap、机制 gap、尺度桥接 gap、验证 gap 或设计 gap 的组合。强度来自组合后仍然足够窄：它不是泛泛说领域复杂，而是锁定一个可处理的关键变量。
- gap 证据来源：引言中的文献分类、方法部分对旧框架边界的说明、结果部分与基线或对照组的差异共同支撑 gap。
- gap 是否足够窄：足够窄。作者没有声称解决所有材料/结构/算法/物理系统，而是围绕 平面薄体/有限厚度体贴合到不可展曲面，典型算例为 disc-to-sphere attachment；核心变量为 QC dilatation K、areal stretch A、界面牵引和膜合力。 建立闭环。
- gap 是否足够重要：重要性来自该 gap 会影响解释、预测、设计或不确定性判断。如果没有本文补充，后续研究会缺少可复用判据或变量。
- 审稿人可能追问：最接近前人是谁？本文与它相比增量在哪里？这个 gap 是概念缺口、数据缺口还是实现缺口？如果只是组合已有工具，组合后的新知识是什么？

## 6. 创新性判断
- 作者声称的贡献：创新在双重解耦：用 K 和 A 组织几何映射，用应力相图组织力学可靠性；同时提出 graded-QC 作为在角度保真和面积均匀之间折中的解析策略。文章贡献不是某个单一公式，而是把计算几何语言、morphoelasticity 和界面力学放入同一套可设计变量。
- 我判断的真实创新：真实创新在于把一个分散问题重新组织成可检验结构，而不只是提出一个新名词。最有力的部分是 claim、变量、图表和边界条件之间能互相对上。
- 创新类型：理论/模型创新、方法工作流创新、实验可视化创新、机制判据创新或跨领域映射创新，具体取决于本文主题。
- 创新强度：中高。它不一定在每个子模块上都是世界首次，但在本文组合方式、论证闭环和写作定位上形成了清晰增量。
- 创新必要性：必要性由 gap 支撑。若不引入本文框架，旧研究要么只能给现象描述，要么只能给局部模拟，要么无法处理不确定性/应力/边界/分布等关键环节。
- 创新与证据匹配度：核心创新与图表、公式和验证基本匹配；更广泛的工程外推需要谨慎。
- 容易被挑战的创新点：如果审稿人认为最接近前人已包含类似变量或判据，作者必须证明本文在适用范围、可解释性、验证强度或实际可执行性上有实质增量。

## 7. 论证链条复原
背景：领域中存在一个已被广泛观察或迫切需要解决的力学问题。 -> 文献：已有理论、实验、模拟或算法分别解决了部分环节。 -> gap：现有生长力学多做 forward morphology 或简化板壳逆设计，计算几何多优化映射失真但不处理应力；曲面电子等实际系统既需要几何贴合，也需要避免起皱和脱粘。因此缺少一个同时 co-design local map and stress state 的有限变形框架。 -> 问题：本文把这个缺口收束为 平面薄体/有限厚度体贴合到不可展曲面，典型算例为 disc-to-sphere attachment；核心变量为 QC dilatation K、areal stretch A、界面牵引和膜合力。 的可研究命题。 -> 方法：有限变形运动学、morphoelastic multiplicative decomposition、Kirchhoff-Love 轴对称假设、Neo-Hookean 不可压材料、共形/准共形/等面积/graded-QC 映射解析、应力相图。 -> 证据：Fig.1-2 给构型和映射类；Fig.3-9 展示四类映射的角度-面积权衡和增长场；Fig.10-12 给界面压缩、膜张力和相图；关键公式包括 K 与 A 不变量、总变形分解 F=FeFg、平衡方程、应力边界和相图边界。 -> 发现：通过生长启发的有限变形框架，可以把平面到曲面的局部映射和应力状态分开设计：共形、准共形、等面积和 graded-QC 各自控制角度与面积失真，而应力可通过厚度和设计参数形成界面压缩/膜内张力的稳定区域。 -> 机制：作者把结果解释为变量、边界、几何、本构、能量、概率或流体反馈之间的耦合。 -> 意义：该框架为后续设计、预测、实验判据或跨领域计算提供可迁移模板。

这条链的优点是闭合度较高：方法不是孤立技术，图表也不是结果堆砌，而是逐一服务于主张。最薄弱环节通常在外推处：文内证据可以支撑特定对象和条件下的结论，但若推广到更复杂材料、真实工程系统或任意几何/边界，需要更多验证。

## 8. 方法/理论/模型细拆
- 方法总框架：理论从参考构型 R0、虚拟生长构型 Rg、目标贴合构型 Rt 开始，用 F=FeFg 把非弹性增长和弹性松弛分开。局部映射用两个不变量描述：K 衡量主伸长比即角度各向异性，A 衡量面积伸长。Disc-to-sphere 算例使问题可解析：共形映射保持角度但面积在极点集中；constant-QC 用固定各向异性转移面积需求；constant-area 保持面积但角度失真向边缘增长；graded-QC 用参数控制 K 的径向分布以折中。应力部分在充分条件下与选定平面映射解耦，作者用 M 与 t 的相图给出界面压缩和膜张力区域。
- 关键概念：研究对象、状态变量、控制参数、基线模型、对照条件、响应指标和适用边界。
- 关键变量/参数：来自正文的核心变量通常会直接进入图表，而不是只停留在公式中。阅读时应追踪每个变量是否出现在结果图、敏感性分析或验证表中。
- 核心假设：包括材料模型、几何边界、加载方式、统计表示、噪声模型、守恒条件或实验类比条件。假设是本文 claim 成立的地基，不能只当方法细节。
- 边界条件：本文对边界条件的处理决定了结果能否外推。边界越理想化，结论越应写成机制启发而不是工程定律。
- 方法步骤：先定义对象和指标，再建立理论/实验/算法框架，然后设置基线与对照，最后通过多组图表验证主张。
- 复现信息：TXT 中可读出较多样品、参数、算法或公式信息，但完整复现仍需核查 PDF、补充材料、代码/数据可用性以及图像细节。
- 方法复杂度是否合理：总体合理，因为复杂度直接服务于 gap；若移植到自己论文，应确保每个模块都能服务一个明确 claim。
- 方法与 gap 的对应关系：本文最可学的是每个方法模块都有任务分工：有的解决定义问题，有的解决验证问题，有的解决对照问题，有的解决边界问题。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 纯等距贴合平面到非零高斯曲率曲面不可行，必须接受度量变化 | 引言/2.1 | Gauss 定理和 K/A 定义 | 强 | 属于经典几何事实 |
| K 与 A 可作为局部映射设计的两个核心不变量 | 摘要/2.1 | 公式定义与四类映射贯穿 | 强 | 适用于轴对称/Kirchhoff-Love 设置 |
| 共形映射保角但造成显著面积非均匀 | 4.1 | Fig.3-4 | 强 | 具体分布依赖 disc-to-sphere |
| graded-QC 能在角度保真和面积均匀之间取得更优折中 | 4.4 | Fig.8-9 与 equal-extrema 规则 | 中强 | “最优”限于设定指标 |
| 应力状态可与选定平面映射解耦并独立编程 | 5 | 应力公式、Fig.10-12 相图 | 中强 | 依赖充分条件和材料模型 |
| 存在界面压缩且膜内张力的设计区域，有助于抗起皱/抗脱粘 | 5.3/结论 | phase diagram | 中 | 需要实验验证 |

- 证据系统总评：本文证据不是单一类型，而是由定义、公式、实验/模拟、参数对照、图表和讨论共同构成。强 claim 通常有多重证据；较弱 claim 多出现在意义外推或工程启发处。
- 证据链写法：先给基线，再给新方法/新现象，再解释差异，最后回到机制。这样的顺序可以避免读者觉得结果只是偶然图形。
- 需要特别警惕：如果某个 claim 只由一张图支持，且该图依赖图像颜色或复杂曲线，则必须在后续 PDF 核查中确认图像本体。

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig.1 | 生长启发贴合与映射类别 | 一图建立 isometry/conformal/QC 和 Fg/Fe 分解 | 需核查示意符号 |
| Fig.3-4 | 共形映射面积变化和增长场 | 说明角度保真代价是面积非均匀 | 需核查极点/边缘趋势 |
| Fig.5 | constant-QC 面积重分布 | 展示 K0 如何把面积需求从极点转向外环 | 曲线峰值需看图 |
| Fig.6-7 | constant-area 的角度失真和增长场 | 支撑面积均匀会带来边缘角度失真的 trade-off | 需核查 K 增长 |
| Fig.8-9 | graded-QC 折中策略 | 体现本文最可迁移的设计思想：有界角度失真 + 面积调节 | 需核查参数 η/ε |
| Fig.10-12 | 界面牵引、膜张力和相图 | 把几何设计升级为可靠性设计 | 相图边界需 PDF 核查 |

- 图表顺序如何服务论证：前几张图通常建立对象、装置、基线或概念；中间图承担模型/机制推导；后几张图负责验证、比较或相图总结。这种排序使读者先相信问题存在，再相信方法必要，最后相信结论有边界。
- 公式功能：公式不是为了展示数学复杂度，而是定义变量、约束边界、连接能量/应力/概率/几何或给出可计算判据。拆解时应问：该公式是否最终进入某张图或某个 claim？如果没有，它可能只是铺垫。
- 结果叙事：结果段落通常不复述图面细节，而是告诉读者图中哪一类趋势支持哪一个 claim。可迁移写法是“Fig. X shows A; compared with B, this indicates C under condition D”。

## 11. 章节结构与篇章布局
文章结构是理论构造型：引言把应用需求、自然启发和几何工具三线汇合；2-3 节建立运动学和本构；4 节逐个比较映射族；5 节把应力编程从几何映射中解耦出来；6 节收束到设计指南。最值得模仿的是先给不变量，再给代表性设计模式，而不是直接堆公式。

- Abstract：问题-方法-结果-意义四段压缩，避免过多背景。
- Introduction：用文献分类制造缺口，而不是简单堆引用。
- Method/Theory/Model：先给框架和变量，再进入公式或实验细节。
- Results：围绕少数核心 claim 排图，每个小节最好只服务一个主张。
- Discussion/Conclusion：把最稳的结果写成结论，把外推写成启发，把未覆盖内容写成未来工作或边界。
- 章节之间如何过渡：作者常用“having established / to address / we next / finally”等阶段性句子，让读者知道论证推进到哪一层。
- 最值得模仿的章节：引言中的 gap 收束和结果中的图表分工。最可能存在结构风险的是方法细节多、跨领域术语多时，读者可能在进入核心 claim 前被公式消耗。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Finite-deformation-theory-for-growth-inspired-co_2026_Journal-of-the-Mechani.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：15
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Framework and local map invariants | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 2.3 Total deformation mapping | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.4 Growth and elastic relaxation | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Constitutive relation and equilibrium | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1 Constitutive model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2 Equilibrium equations and static pressure | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.3 Boundary conditions and stress components | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4 Representative in-plane mapping modes | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.4 Graded quasi-conformal mapping | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5 Programming stress state | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5.1 Program interface stress state | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5.2 Program membrane resultant state | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 5.3 Joint design map and phase diagram | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
引言段落层次非常工程化：自然 3D 功能 -> 平面制造约束 -> 高斯曲率导致的失配 -> 生长启发 -> 逆设计缺口 -> 计算几何缺口 -> 本文框架。理论段落常以“Having established...”开头推进，给读者明确阶段感。结果段落不是描述图形好看，而是解释某个 mapping mode 的代价。

- Introduction 段落推进：背景段负责扩大意义，文献段负责分类，gap 段负责收束，贡献段负责声明本文做什么，路线图段负责降低阅读成本。
- Method 段落推进：定义对象和变量，再解释参数、边界、假设和流程。好的方法段不是实验记录或公式清单，而是告诉读者为什么这些设置足以回答问题。
- Results 段落推进：每段开头通常点名本段要验证的 claim，中间引用图表和对照，结尾解释趋势的机制含义或引出下一变量。
- Discussion/Conclusion 段落推进：先重述最稳结论，再说明机制意义，最后写边界和未来工作。
- 常见段落开头方式：To investigate..., To quantify..., Having established..., Compared with..., These results suggest...。
- 常见段落收束方式：回到核心变量、指出机制、标注边界或引出下一节。
- 可复用段落模板：背景事实 2-3 句 -> 已有方法 2 句 -> 具体不足 1 句 -> 本文动作 1 句 -> 可验证贡献 1 句。

## 13. 文笔画像与语言习惯
文笔是“几何-力学桥接型”：高频词是 mapping、growth、stress、interface、membrane、conformal、quasi-conformal。语气稳健，强调 framework establishes、provides guidelines，而较少宣称直接实现工程器件。长句多，但结构清晰，经常用 apposition 解释术语。

- 整体语气：克制、机制导向、证据优先。即使题材新，也尽量通过变量和图表表达新意，而不是形容词堆叠。
- claim 强度：核心结果处用 demonstrate/show/reveal，机制解释处常用 suggest/indicate/can be attributed to，外推处使用 may/could/potentially 控制范围。
- 谨慎表达：作者会在实验条件、模型假设、参数范围、类比系统或硬件噪声处主动加限定。
- 问题表达：常见模式是“X is important, but Y remains unresolved because Z”。
- 贡献表达：常见模式是“we develop/formulate/introduce/demonstrate a framework that...”。
- 对比表达：常用 in contrast、compared with、at variance with、unlike prior approaches。
- 术语密度：较高，但术语围绕核心变量聚集；没有明显为了显得高深而引入无关术语。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：rim(130)；mapping(65)；growth(59)；sin(55)；conformal(53)；out(40)；in-plane(38)；stress(35)；area(35)；angle(34)；pole(31)；deformation(30)；metric(30)；areal(30)；local(29)；change(27)；distortion(27)；design(26)；zhang(25)；map(24)
- 高频学术名词：deformation(60)；condition(40)；stress(35)；distortion(27)；thickness(22)；framework(21)；integration(19)；guration(15)；traction(14)；through-thickness(13)；analysis(12)；curvature(12)；section(12)；interface(11)；compatibility(11)；conditions(9)
- 高频学术动词：shows(8)；develop(3)；shown(3)；derived(3)；developed(3)；formulated(2)；compare(2)；compared(2)；solve(2)；derive(1)；investigate(1)；evaluate(1)；show(1)；predicted(1)
- 高频形容词：local(58)；conformal(53)；elastic(40)；metric(30)；areal(30)；boundary(23)；constant(17)；spherical(17)；critical(16)；geometric(15)；cient(15)；interfacial(12)；radial(12)；non-elastic(11)；normal(11)；analytical(10)
- 高频副词/连接副词：therefore(11)；monotonically(11)；radially(5)；strongly(4)；analytically(4)；however(4)；respectively(4)；family(4)；initially(3)；explicitly(3)；finally(3)；exactly(3)；directly(3)；generally(2)；globally(2)；approximately(2)
- 高频二词短语：angle distortion(18)；con guration(15)；out out(15)；rim tan(15)；stress state(12)；areal change(12)；sin sin(12)；tan rim(12)；areal stretch(11)；rim rim(11)；conformal mapping(10)；sin cos(9)；sin rim(9)；area change(8)；total deformation(8)；elastic relaxation(8)
- 高频三词短语：out out out(8)；rim tan rim(6)；tan rim tan(6)；sin sin cos(5)；rim sin rim(5)；angle distortion areal(4)；nite deformation framework(4)；cos sin sin(4)；sin sin sin(4)；dilatation measures angle(3)；measures angle distortion(3)；distortion areal stretch(3)

**主动、被动与句法**

- 被动语态估计次数：62
- `we + 动作动词` 主动句估计次数：8
- 名词化表达估计次数：767
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：181
- 一般过去时线索：6
- 现在完成时线索：5
- 情态动词线索：17
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：conformal(6)；integration(6)；stress(4)；geometric(4)；local(4)；deformation(3)；theory(3)；state(3)
- 1. Introduction：growth(16)；mapping(12)；conformal(11)；stress(10)；con(8)；local(7)；framework(7)；guration(7)
- 2.1. Framework and local map invariants：sin(15)；mapping(13)；deformation(12)；cos(11)；metric(8)；con(7)；growth(7)；elastic(7)
- 2.3. Total deformation mapping：mapping(5)；sin(3)；deformation(2)；principal(2)；directions(2)；in-plane(2)；total(1)；map(1)
- 2.4. Growth and elastic relaxation：growth(4)；elastic(4)；metric(3)；contact(3)；geometry(3)；mapping(2)；basis(2)；axisymmetric(2)
- 3. Constitutive relation and equilibrium：无明显高频项
- 3.1. Constitutive model：tensor(4)；elastic(3)；strain(2)；energy(2)；stress(2)；contravariant(2)；components(2)；hyperelastic(1)
- 3.2. Equilibrium equations and static pressure：sin(11)；pressure(4)；cient(4)；cot(3)；cos(3)；eqs(3)；equilibrium(2)；covariant(2)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
以下只提取短语和句式骨架，不大段复制原文。

- **问题/gap**：`Existing geometric mappings control distortion, whereas mechanical stability is often treated only as an outcome rather than a design target.`  中文启发：把相邻领域的不足写成设计目标缺失。
- **方法**：`We formulate the inverse design through two invariants: A, which measures..., and B, which quantifies....`  中文启发：定义双不变量的高复用句。
- **结果**：`This strategy reduces the peak of A while keeping B bounded within the prescribed range.`  中文启发：适合 trade-off 结果。
- **意义**：`The phase diagram links local design knobs to mechanically desirable regions.`  中文启发：把公式图转化为设计指南。
- **局限**：`The analysis is derived for an axisymmetric disc-to-sphere setting and should be generalized before use in arbitrary geometries.`  中文启发：主动限制算例外推。

### 14.1 问题与 gap 表达
- 骨架：`Despite extensive studies on X, how Y controls Z under A remains unclear.`
- 中文启发：不要只说“研究不足”，而要说哪个控制关系、哪个条件、哪个尺度或哪个观测仍未闭合。

### 14.2 方法与框架表达
- 骨架：`To address this gap, we combine A with B to construct C.`
- 中文启发：方法句要同时交代输入、核心动作和输出，不要只报工具名。

### 14.3 结果与趋势表达
- 骨架：`Compared with the baseline, the proposed/observed system shows A, indicating B.`
- 中文启发：图表结果要和 baseline 绑定，否则趋势没有解释力。

### 14.4 机制解释表达
- 骨架：`This behavior can be attributed to A, which modifies B and thereby changes C.`
- 中文启发：机制句最好是三段式：原因、作用对象、宏观后果。

### 14.5 贡献与意义表达
- 骨架：`The framework provides a quantitative route for linking A-scale mechanisms to B-scale response.`
- 中文启发：贡献要写成可检验动作或能力，而不是抽象价值。

### 14.6 局限与未来工作表达
- 骨架：`The present analysis is limited to A; future work should examine whether B persists when C is relaxed.`
- 中文启发：局限不是自我削弱，而是告诉读者结论在哪里可靠、下一步如何扩展。

## 15. 引用策略与文献使用
引用策略是跨领域拼接：曲面电子和 bio-interface 文献说明应用痛点，Gauss/非欧几里得板壳/生长力学文献说明理论根基，计算几何文献说明 conformal/QC 工具已有但偏几何。引用姿态温和，不批评某一领域，而是说各领域各解决一半问题。

- 引用密度：引言最高，方法基础次之，结果段最低。这样的分布符合 JMPS 常见写法：先用文献建立问题位置，后用本文证据推进主张。
- 经典文献用途：提供术语、守恒律、本构、几何、贝叶斯或断裂理论的合法性。
- 近年文献用途：说明问题仍在前沿，制造与本文最接近工作的差异。
- 方法文献用途：证明工具不是凭空发明，并交代为什么旧工具仍不够。
- 对比/批判性引用：语气通常温和，强调“valuable but limited under...”而非直接否定。
- gap 如何靠引用搭建：先说明已有研究解决 A，再说明 B 仍缺，最后把本文放在 A 与 B 的交界处。
- 引用风险：若遗漏最接近的竞争工作，novelty 会被直接挑战；若过多自引或只引支持文献，gap 会显得人为。

## 16. 审稿人视角风险
最大风险是解析框架建立在轴对称 disc-to-sphere、Kirchhoff-Love、不可压 Neo-Hookean 和充分条件上，实际器件的开孔、走线、厚度梯度和材料粘弹性会破坏简洁解耦。第二，phase diagram 尚缺实验验证。第三，graded-QC 的最优性依赖选定指标。第四，界面牵引符号与真实粘附失效之间还需要界面断裂模型。

- 最大攻击面：核心 claim 是否被足够多条件验证，或者是否只是特定设置下成立。
- claim 是否过强：文内最强结论通常可接受，但摘要和结论中的广泛意义需要限定在研究对象和方法假设内。
- 证据是否不足：主要不足往往不是没有证据，而是证据覆盖的参数、几何、材料或样本范围有限。
- 方法是否可复现：TXT 提供了公式和部分参数，但完整复现仍需 PDF、补充材料、代码/数据或实验细节。
- 对比是否充分：审稿人会要求与最接近前人同条件比较，而不是只和弱基线比较。
- 边界条件是否清晰：需要把每个主要 claim 与材料、几何、加载、噪声、守恒或类比条件绑定。
- 替代解释是否排除：若机制解释存在其他可能，需要用对照、消融、敏感性分析或谨慎措辞处理。
- 图表是否需进一步核查：需要。尤其是颜色场、误差带、图像序列、相图边界、硬件噪声和拟合曲线均应结合 PDF 图像核查。

## 17. 可复用资产
可复用的是“双不变量 + 代表性模式 + 相图指南”的写法。写复杂设计理论时，不要先给全部方程，而是先定义读者能理解的两个坐标，再展示几个极端策略和折中策略，最后用相图把数学变成可操作区域。

- 可复用选题角度：从一个被观察到但未被机制闭合的现象切入，或从一个被使用但未被充分验证的工具切入。
- 可复用 gap 制造方式：承认旧研究贡献，指出其边界，再把本文变量放在边界之外但仍可验证的位置。
- 可复用论证链：背景 -> 文献分类 -> 具体 gap -> 新变量/框架 -> 基线验证 -> 对照/参数扫描 -> 机制解释 -> 边界。
- 可复用图表设计：概念/装置图、变量定义图、基线对照图、参数响应图、验证图、相图或流程图。
- 可复用段落结构：主题句先提出本段 claim，中间用图表和公式支撑，结尾解释对主线的意义。
- 可复用句型骨架：`To isolate the role of X, we compare A and B under otherwise identical conditions.`；`The observed transition from A to B indicates that C becomes dominant.`；`This result should be interpreted within the limits of D.`
- 可复用引用组织：经典文献管合法性，最新文献管前沿性，最接近文献管 novelty，应用文献管意义。
- 不宜直接模仿之处：若自己没有同等强度的图表、实验、推导或对照，不宜模仿过强标题和广泛外推。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学习：把贡献写成“补上某个闭环”，而不是“提出一个方法”。闭环包括变量定义、方法执行、证据验证、机制解释和边界控制。
- 可迁移到 Introduction 的写法：先把领域问题讲成读者关心的力学矛盾，再用文献分类制造窄 gap，最后明确本文只解决其中一个可验证问题。
- 可迁移到 Method 的写法：先讲总体框架和变量，后讲公式/实验/算法细节；让方法复杂度与 gap 一一对应。
- 可迁移到 Results/Discussion 的写法：每张关键图服务一个 claim；先说明图证明了什么，再解释为什么能支持机制。
- 需要避免的问题：不要让图表变成结果清单；不要在摘要中许诺正文没有验证的普适性；不要把模型内趋势写成真实世界定律；不要让引用只证明自己想证明的 gap。
- 对中文论文写作的启发：中文写作容易把“意义”写大，把“边界”写弱。本文提醒我们，高水平论文的可信度常来自主动限定条件，而不是无条件扩大贡献。

## 19. 最终浓缩
- 这篇论文最值得学：这篇最值得学的是把跨学科工具统一成设计变量：K/A 管几何，牵引/膜力管可靠性。最大风险是算例理想化和实验缺口。三个可迁移动作：先抽象不变量，再比较极端方案，最后用相图给设计边界。
- 最核心的一句话：通过生长启发的有限变形框架，可以把平面到曲面的局部映射和应力状态分开设计：共形、准共形、等面积和 graded-QC 各自控制角度与面积失真，而应力可通过厚度和设计参数形成界面压缩/膜内张力的稳定区域。
- 最大风险：文内证据支撑特定对象和条件下的结论，但外推到更复杂系统时需要额外验证。
- 三个可迁移动作：
  1. 把 gap 写成具体变量、机制或边界缺口，而不是泛泛的“研究不足”。
  2. 让每个方法模块对应一个 claim，让每张图表承担明确说服功能。
  3. 在结论中区分“本文已经证明的”“本文提示的”“需要后续核查的”。
- 后续人工核查：应结合 PDF 检查图像本体、曲线尺度、误差带、颜色场、公式编号和补充材料；TXT 足以支持结构和写作拆解，但不应替代视觉核查。
