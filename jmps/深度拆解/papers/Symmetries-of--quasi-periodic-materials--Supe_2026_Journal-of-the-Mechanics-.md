# Symmetries of (quasi)periodic materials: Superposability vs. Indistinguishability

## 0. 读取说明
- 源 PDF：`jmps\文献\Symmetries-of--quasi-periodic-materials--Supe_2026_Journal-of-the-Mechanics-.pdf`
- 源 TXT：`jmps\文本\txt\Symmetries-of--quasi-periodic-materials--Supe_2026_Journal-of-the-Mechanics-.txt`
- 是否需要结合 PDF 图像核查：需要。TXT 能支持全文语义、图注、章节和公式附近文字，但不能可靠判断曲线细节、误差条、颜色条、三维形态和局部图像。
- 本文类型：常规 JMPS 研究论文；本文件按 0-19 深度模板拆解。上一轮 `jmps/拆解/papers` 仅作为事实校验底稿，本轮重新组织为“细致拆解 + 写作素材”。

## 1. 基本信息与论文身份
- 题名：Symmetries of (quasi)periodic materials: Superposability vs. Indistinguishability
- 作者/机构：Markus Husert 等；完整机构见 PDF 首页。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 213 (2026) 106620. doi:10.1016/j.jmps.2026.106620
- DOI：10.1016/j.jmps.2026.106620
- 关键词：Quasiperiodicity,Symmetry,Indistinguishability,Fourier transform,Architectured materials,Image processing
- 研究对象：周期与准周期 architectured materials 的对称性判据，尤其是 superposability 与 indistinguishability 的差别
- 研究尺度：从具体材料/结构/图像对象进入机制、模型或设计规则；章节标题包括：1 A rotation of order 𝑛 is a rotation by an angle 2𝜋∕𝑛.；1. Symmetry of periodic heterogeneous materials；1.1. On the notion of periodicity；3 It is only a subgroup of the full symmetry group of 𝑓 since the latter may contain other elements for instance the cen；5 This structure is often referred to as a ℤ-module. An R-module is a generalisation of the notion of vector space, in w；6 It is important to distinguish the lattice group from the lattice point set, the latter being the geometrical expressi；1.2. Heterogenous periodic material；7 The Fourier transform is introduced and used here in a formal manner. Strictly speaking, one should distinguish betwee；1.3. Superposability-based symmetry；8 Since 𝐱 and 𝑓(𝐱) belong to diﬀerent vector spaces, the group action of 𝐠∈Euc(𝑑) on each of them are necessarily diﬀere；9 A distinction is introduced here between arbitrary translations 𝐯∈ℝ𝑑 and translations that are elements of the lattice；2. Symmetry of quasiperiodic heterogeneous materials；2.1. Heterogeneous quasiperiodic material；2.2. On the notion of indistinguishability；10 Incommensurate here means that the ratio between the frequencies is irrational.；11 In crystallography, the holohedry is deﬁned as the symmetry group of the lattice point set. In the quasiperiodic case；12 The vectors 𝐤(𝑖) denote arbitrary elements of  and should not be confused with the fundamental frequencies 𝐤𝑖.；13 This result links the Fourier-based and hyperspace descriptions of quasicrystals (Duneau and Katz, 1985), which are n；2.3. Indistinguishability-based symmetry；14 For periodic materials, the phase function reads Φ𝐐(𝐤) = −(𝐐𝐤) ⋅𝐯 for each element (𝐐| 𝐯) of the space group .；15 The ⋆ notation has been chosen since the weak symmetry operations are deﬁned with respect to values in the reciprocal；3. Numerical determination of space group properties；3.1. Calculation of Fourier coeﬃcients；3.1.1. Fourier transform of an image；3.1.2. Selection of spatial frequencies to study；16 The factor  1 allows to have a consistent deﬁnition of the Fourier coeﬃcient regardless of the resolution of the stud；3.2. Determination of space group properties；3.2.1. Detection of the point group；17 The limitation 𝑙 on the number of fundamental frequencies used to index the detected peaks corresponds to a truncatio；18 The generators of a group are deﬁned as a subset of its elements such that any other element can be expressed as a co；3.2.2. Detection of symmorphism；4. Results；4.1. Periodic heterogeneous materials；4.1.1. Inﬂuence of shift；4.1.2. Comparison of square lattice heterogeneous materials
- 方法类型：自相关函数、Fourier 空间表示、点群检测、gauge function 与 symmorphism 判断、合成 2D tiling 图像验证
- 证据类型：周期 square tiling、Penrose、generalised Penrose、Ammann-Beenker、Fibonacci-squares 的 Fourier peaks 和 deviation measures；图像本体需结合 PDF 核查
- 目标读者：JMPS 中关注材料机制、本构建模、结构稳定性、图像判据、软物质或工程设计诊断的读者。
- JMPS 风格定位：这篇不是孤立应用报告，而是把一个具体对象提升为可验证的力学问题，并试图输出可迁移的 benchmark、机制解释、判据或设计规则。

## 2. 摘要与核心信息提取
- 摘要的功能拆解：摘要通常按“背景/传统理解 -> 未解决 gap -> 本文方法 -> 关键发现 -> 意义”推进。它的强处是让读者在第一页就知道本文改变了什么判断。
- 背景句承担什么：建立对象的重要性，给读者一个进入 JMPS 问题的理由，而不是泛泛科普。
- gap 句承担什么：指出现有测试、模型、判据或实验只能看到一部分，不能回答本文真正关心的状态、路径、局部场或统计性质。
- 方法句承担什么：说明作者如何隔离变量、构造模型、扫描参数或提取图像特征，使 gap 变成可回答问题。
- 结果句承担什么：用少量定量结果或清晰转变支撑主张，让 contribution 不停留在“提出方法”。
- 意义句承担什么：把结果翻译成更广义的本构、设计、分类或机制价值。
- 一句话主张：从判据层面重写问题，而不是只改算法。
- 3-5 个核心关键词：Quasiperiodicity,Symmetry,Indistinguishability,Fourier transform,Architectured materials,Image processing

## 3. 选题层深拆
- 问题来源：- 问题来源：architectured materials 通常被粗分为随机/周期，但准周期结构有长程有序和非晶格对称，传统叠合判据不够。 - 为什么重要：材料均匀化、失稳模式、波传播和结构设计都依赖对称性分类。 - 研究边界：主要是 2D 合成图像；检测 Fourier 空间中的离散 peaks；部分步骤仍需人工选择频率/识别 gauge function。 - JMPS 取向：把凝聚态物理的不可区分性概念迁移到力学 architectured materials，并给出可操作算法。
- 问题为什么重要：重要性不只来自对象本身，还来自该对象暴露出的通用困难：常规实验混合多个过程，结构失稳路径难以控制，本构变量和微机制脱节，传统判据过强，或全局性能无法揭示局部风险。
- 问题为什么现在值得做：当前实验、数值、图像处理和物理约束学习工具足以把过去只能定性描述的现象转成可度量证据。
- 问题边界：边界被限定在本文材料、结构、加载、图像或数据窗口中。这个边界让证据链闭合，也意味着不能无条件外推到所有同类系统。
- 选题的 JMPS 味道：把一个具体系统写成“机制/模型/判据/设计规则”问题，而不是只报告工程性能。
- 选题可迁移性：可学的是重新切分对象和证据的动作：先找被传统观察遮蔽的层次，再设计能直接暴露该层次的实验或模型。

## 4. 领域位置与文献版图
- 作者如何划分已有研究：- 既有版图：周期材料用空间群和可叠合性；准晶/准周期物质用长程有序、衍射和 indistinguishability；力学超材料中准周期结构逐渐增多。 - 作者制造的 gap：力学/材料图像处理中缺少一个能从 mesostructure 图像识别周期与准周期材料空间群属性的统一方法。 - gap 类型：概念 gap + 方法 gap。 - gap 是否成立：成立，尤其是对“准周期不是随机与周期之间的模糊地带，而有自己的对称性定义”这一点说服力强。
- 主要研究流派/方法路线：可分为经典理论或经验观察、现代实验/数值/图像工具、以及应用牵引的设计或预测需求三类。
- 每类研究解决了什么：经典文献提供概念和基本方程；方法文献提供实现路径；近年应用文献提供为什么需要更强预测能力的动机。
- 每类研究留下什么不足：不足通常在交叉处：已有研究能解释现象 A 或预测量 B，但不能隔离本文关心的状态、局部场、相图边界、统计判据或 feature 依赖。
- 本文站在哪条线上：本文站在已有工具之后，强调把工具组织成一个能回答具体 gap 的闭环。
- 最接近前人工作：上一轮底稿指出了相邻经典和近年工作；深度阅读时应重点核查 Introduction 中最接近方法是否被公平比较。
- 是否公平处理前人：总体是“继承 + 补足”的写法，很少直接贬低前人，这符合 JMPS 对累积性贡献的偏好。

## 5. Gap 制造机制
- 明示 gap：力学/材料图像处理中缺少一个能从 mesostructure 图像识别周期与准周期材料空间群属性的统一方法。
- 隐含 gap：如果不引入本文框架，读者只能得到现象描述或经验拟合，无法知道背后的状态变化、稳定性拓扑、微结构竞争、对称判据、成分调制或局部风险。
- gap 类型：对象 gap、机制 gap、方法 gap、数值 gap、判据 gap 或设计诊断 gap。
- gap 证据来自哪里：来自文献分组、baseline 对比、方法必要性和图表结果的递进。
- gap 是否足够窄：较窄；它被收束到具体材料、结构、参数、图像或器件，而非泛泛宣称领域空白。
- gap 是否足够重要：足够重要，因为解决后能产生可迁移的模型、实验基准、相图、图像指标或设计 workflow。
- 如果我是审稿人会如何追问：最可能追问最接近前人是否遗漏、参数窗口是否太小、机制证据是否直接、图像和误差是否支撑强 claim。

## 6. 创新性判断
- 作者声称的贡献：引入 indistinguishability 判据；用 Fourier coefficients 的幅值和 gauge-linear phase 条件定义对称；提出图像处理流程判断 point group 和 symmorphism。
- 我判断的真实创新：把抽象的 quasicrystal 对称性转成材料图像可计算的 deviation measure，并用 Penrose D10/D5 争议展示价值。
- 创新类型：理论迁移 + 算法表达 + 概念澄清。
- 创新强度：中高。偏理论和方法，力学结果不是重点。
- 创新必要性：必要性来自 gap：没有本文的隔离、调谐、正则化、判据或局部场解析，就无法支撑主张。
- 创新与证据匹配度：核心 claim 有图表支撑；外推性意义需要按作者给出的边界理解。
- 容易被挑战的创新点：频率选择和 gauge function 仍人工；合成图像验证多，真实材料噪声和有限尺寸效应未充分展开。

## 7. 论证链条复原
用 `背景 -> 文献 -> gap -> 问题 -> 方法 -> 证据 -> 发现 -> 机制 -> 意义` 复原：architectured materials 需要内部结构组织原则 -> 传统随机/周期二分忽略准周期长程有序 -> 周期材料可用 superposability 和空间群，但准周期没有平移晶格，不能照搬 -> 引入 indistinguishability：如果统计自相关/傅里叶系数满足幅值相等和 gauge-linear phase 条件，则视为同一对称 -> 从图像 Fourier transform 提取 peaks 和 fundamental frequencies -> 计算 point group deviation，再判断 symmorphism -> 在周期和准周期 tilings 上验证 -> 得出经典 Penrose 在不可区分性意义下为 D10。

深度拆解看，这条链的关键是“每一步让下一步不可避免”。背景给重要性，文献给已有能力，gap 给必要性，方法给可验证路径，图表给证据，Discussion 再把证据转成机制或设计语言。写作时可以模仿这种递进，但不能省略 baseline，否则创新会显得悬空。

## 8. 方法/理论/模型细拆
- 方法总框架：定义周期/准周期材料 -> 定义 superposability/indistinguishability -> Fourier coefficient 条件 -> 图像 FFT 和 peak selection -> point group 检测 -> symmorphism gauge 检测 -> 案例验证。
- 关键概念：Quasiperiodicity,Symmetry,Indistinguishability,Fourier transform,Architectured materials,Image processing
- 关键变量/参数：从 TXT 可见的变量包括章节标题、公式附近符号、图注中的控制参数和输出指标；完整符号表需结合 PDF 核查。
- 核心假设：材料图像可代表 mesostructure；Fourier peaks 足够清楚；选择的有限频率子集能代表空间群特征。
- 边界条件：本文只对其测试/模拟/图像/数据范围内的 claim 最可靠。
- 方法步骤：先定义对象和 baseline，再引入本文方法，随后做对比、参数扫描或验证，最后讨论机制与边界。
- 复现信息：TXT 足以提取方法逻辑，但完整复现需要 PDF 图、参数表、补充材料、代码/数据可用性说明。
- 方法复杂度是否合理：合理，因复杂度对应 gap；但写作时要防止公式或网络/数值细节压倒问题主线。
- 方法与 gap 的对应关系：本文方法不是装饰，而是为了看见传统路径看不到的那一层证据。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 从判据层面重写问题，而不是只改算法。 | 摘要/结论 | 摘要主张、核心图表、Discussion 收束共同支撑 | 综合证据 | 中强 | 算法手动环节和噪声鲁棒性；有限窗口图像对无限准周期结构的代表性。 |
| 把抽象的 quasicrystal 对称性转成材料图像可计算的 deviation measure，并用 Penrose D10/D5 争议展示价值。 | Introduction/Results | 方法设计与 baseline 对比显示本文并非单纯重复已有工作 | 方法+对比 | 中强 | 需确认最接近前人是否充分比较 |
| 本文的结果链能够从现象推进到机制或设计规则 | Results/Discussion | 图表按 baseline、核心结果、参数/机制、意义展开 | 图表叙事 | 中强 | 机制有时是推断而非直接观测 |
| 方法复杂度与 gap 基本匹配 | Method/Theory | 实验、数值、理论或网络模块分别对应隔离、预测、分类、调谐或筛查任务 | 方法论证 | 中 | 参数与复现细节需查 PDF |
| 作者主动控制外推边界 | Discussion/Conclusion | 结尾列出材料、载荷、图像、模型或数据窗口限制 | 边界说明 | 强 | 摘要和标题的强表述仍需正文支撑 |
| 图表系统承担主要说服功能 | Figures/Tables | 图注和正文显示多图共同完成对象、方法、结果、机制、应用的分工 | 视觉证据 | 中强 | 图像本体必须核查 |

这张表说明：核心 claim 通常由多种证据共同支撑，而不是只靠一张图。写作时应避免把 Discussion 中的机制推断写成与实验观察同等强度的事实。

## 10. 图表、公式与结果叙事提取

| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig./Table | Fig. 1. Characteristic scales of an architectured material. | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 2. Laser cut disk of Penrose honeycomb used for Brazilian test (Somera, 2022). | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 3. Illustration of the mismatch of the Penrose tiling for a 2𝜋10 rotation combined with a translation. On ﬁgure (a) two ﬁve-pointed stars with | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 3b represents in red a rotated Penrose tiling by a rotation of 2𝜋 superposed to the original Penrose tiling after a translation. One | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 4. Examples of point sets of periodic lattices in ℝ2 together with their basis vectors , and their associated unit cell . | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 5. Two tilings with diﬀerent space groups but identical point group D4. denotes centres of rotation of order 4, centres of rotation of order | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 6. Illustrative example of a quasiperiodic function 𝑓qp(𝑥) = cos 2 𝜋𝑥+ sin 2 𝜋𝑥. The two incommensurate periods are (𝑇1 = 1, 𝑇2 = 2) and | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 7. Gauge equivalence relationships. | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 8. The proposed two-step procedure that determines the point group and symmorphic character of an image of a mesostructure. | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 9. Amplitudes of the Fourier transform of a periodic image: (a) Values of diﬀraction diagram | ̂𝜌𝑘𝑙| above threshold of 𝜏= 0.01. A derived ﬁrst | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 10. Centred (a) and generic (b) images of the same periodic tiling. The red cross indicates the centre of the image. | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 11. Computed Fourier coeﬃcients for the (a) centred and (b) generic images of the same periodic tiling shown in Fig. 10. | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |

图表顺序服务于论证节奏：先交代对象和方法，再给 baseline，随后展示核心变化，最后用参数图、机制图、误差图或风险图把结果变成可复用规律。由于 TXT 只能读图注，涉及图像本体的判断必须回到 PDF。

## 11. 章节结构与篇章布局
- Abstract：压缩整篇论证，突出反转或新能力。
- Introduction：从广背景快速收束到具体 gap，文献按能力组织。
- Related Work/Background：若没有独立小节，则嵌入 Introduction 与 Method。
- Method/Theory/Model：承担“为什么本文能回答 gap”的技术可信度。
- Results：按 baseline、核心结果、参数/机制、意义推进。
- Discussion：- Introduction：从增材制造和 architectured materials 的组织问题切入，再过渡到准晶革命和 Penrose。 - Section 1：先讲周期材料和 superposability，建立传统基线。 - Section 2：转入准周期材料和 indistinguishability，完成概念扩展。 - Section 3：给数值算法，衔接理论与图像。 - Section 4：用周期和准周期案例演示。 - Conclusion：总结方法、Penrose D10 结论和自动化/真实图像/3D 扩展。
- Conclusion：把发现收束成可迁移贡献，同时限制外推。
- 章节之间如何过渡：过渡靠问题链，而不是机械地介绍下一节。
- 哪一节最值得模仿：Results 到 Discussion 的转换最值得学，因为它把图表事实变成机制/设计语言。
- 哪一节可能存在结构风险：方法密集小节可能让非本领域读者失去主线，需要流程图和主题句。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Symmetries-of--quasi-periodic-materials--Supe_2026_Journal-of-the-Mechanics-.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：20
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：实验/材料型, 描述型, 方法/模型型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Symmetry of periodic heterogeneous materials | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 高 | 是 | 保留具体变量/对象 |
| 1.1 On the notion of periodicity | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 1.2 Heterogenous periodic material | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 1.3 Superposability-based symmetry | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Symmetry of quasiperiodic heterogeneous materials | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 高 | 是 | 保留具体变量/对象 |
| 2.1 Heterogeneous quasiperiodic material | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 On the notion of indistinguishability | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.3 Indistinguishability-based symmetry | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Numerical determination of space group properties | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3.1.1 Fourier transform of an image | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.1.2 Selection of spatial frequencies to study | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.2 Determination of space group properties | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.2.1 Detection of the point group | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.2.2 Detection of symmorphism | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
- Introduction 段落推进：对象重要性 -> 既有研究能力 -> 未解 gap -> 本文策略和贡献。
- Method 段落推进：对象定义 -> 变量/方程/实验/算法 -> 实现细节 -> 验证路线。
- Results 段落推进：每段围绕一个图或一个 claim，先给趋势，再给机制解释。
- Discussion/Conclusion 段落推进：先整合结果，再对照文献，最后给边界和迁移价值。
- 常见段落开头方式：`To isolate...`、`We first...`、`Having established...`、`These results suggest...`。
- 常见段落收束方式：用 `Together`、`This indicates`、`These findings` 把事实收束到机制。
- 可复用段落模板：`传统理解/基线 -> 本文操作 -> 图中差异 -> 机制解释 -> 对模型或设计的启发`。

## 13. 文笔画像与语言习惯
- 整体语气：- 整体语气：概念澄清型，带数学定义，强调“criterion”“condition”“space group properties”。 - 常用问题表达：`how should this architecture be organised?`, `overly rigid classification` - 常用贡献表达：`generalises the conventional criterion`, `propose a method that first extracts...` - 常用机制/方法表达：`equal amplitudes`, `complex phases differing by a gauge function`, `deviation measure` - 常用限定表达：`currently requires the user to manually identify`, `care should be taken` - 可复用句式：先指出传统二分“not entirely inaccurate, but overly rigid”，再引入更精细概念。
- claim 强度：核心范围内强，外推处谨慎。
- 谨慎表达：常用 `suggest`, `consistent with`, `over the explored range`, `relative`, `first-order`, `requires further validation`。
- 问题表达：强调“现有方法遮蔽/无法解析/判据不适用”，比简单说“缺少研究”更高级。
- 贡献表达：把贡献写成能力，如 isolate、recast、reshape、capture、detect、predict、screen、enable。
- 机制表达：常通过 transition、competition、coupling、state、landscape、hotspot、feature dependency 组织。
- 对比表达：baseline 对比是文笔骨架。
- 限定边界表达：Discussion/Conclusion 主动承认限制。
- 术语密度：高，但围绕少数核心术语重复。
- 长句/短句习惯：方法段长句多，结果主题句较短。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：group(165)；point(98)；symmetry(93)；space(83)；fourier(79)；periodic(74)；function(72)；tiling(57)；functions(56)；coe(51)；image(50)；lattice(49)；materials(47)；cients(45)；material(44)；phase(44)；indistinguishability(41)；set(40)；ned(39)；quasiperiodic(39)
- 高频学术名词：function(72)；materials(47)；material(44)；indistinguishability(41)；condition(34)；notion(28)；properties(27)；analysis(26)；rotation(24)；invariance(22)；density(22)；section(21)；translation(17)；procedure(15)；structure(14)；superposability(14)
- 高频学术动词：proposed(15)；shown(14)；shows(5)；evaluated(3)；indicates(3)；developed(3)；formulated(2)；reveal(2)；revealed(2)；compared(2)；evaluate(2)；demonstrate(2)；derived(2)；investigated(2)；validated(1)；suggest(1)
- 高频形容词：periodic(74)；heterogeneous(62)；material(44)；quasiperiodic(39)；fundamental(30)；symmorphic(26)；invariant(21)；primitive(17)；numerical(16)；reciprocal(15)；non-symmorphic(14)；rotational(13)；erent(13)；horizontal(13)；classical(12)；physical(12)
- 高频副词/连接副词：however(23)；consequently(20)；therefore(9)；directly(8)；respectively(8)；moreover(6)；accordingly(6)；precisely(5)；necessarily(5)；generally(4)；cantly(4)；previously(4)；furthermore(3)；strictly(3)；solely(3)；similarly(3)
- 高频二词短语：point group(61)；fourier coe(45)；coe cients(44)；space group(36)；lattice group(27)；penrose tiling(26)；fundamental frequencies(21)；gauge function(20)；phase functions(17)；unit cell(16)；fourier space(14)；heterogeneous materials(14)；fourier transform(13)；density function(13)；primitive unit(13)；heterogeneous material(13)
- 高频三词短语：fourier coe cients(39)；primitive unit cell(10)；lattice point set(6)；fourier coe cient(6)；canonical penrose tiling(6)；reciprocal lattice group(5)；amplitudes fourier coe(4)；space group symmorphic(4)；space group material(4)；periodic heterogeneous materials(4)；elements point group(4)；point group realised(4)

**主动、被动与句法**

- 被动语态估计次数：243
- `we + 动作动词` 主动句估计次数：6
- 名词化表达估计次数：946
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：394
- 一般过去时线索：36
- 现在完成时线索：15
- 情态动词线索：91
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：symmetry(23)；materials(21)；periodic(18)；group(12)；order(12)；space(11)；invariance(11)；indistinguishability(10)
- 1. Symmetry of periodic heterogeneous materials：periodic(5)；function(5)；space(4)；structures(3)；section(3)；symmetry(3)；notion(2)；object(2)
- 1.1. On the notion of periodicity：group(16)；lattice(14)；function(13)；point(11)；periodic(8)；set(8)；basis(7)；vectors(7)
- 1.2. Heterogenous periodic material：periodic(8)；density(8)；function(8)；material(6)；ned(4)；heterogeneous(4)；domain(4)；fourier(4)
- 1.3. Superposability-based symmetry：group(49)；point(22)；space(21)；lattice(11)；elements(10)；groups(8)；mirror(8)；primitive(8)
- 2. Symmetry of quasiperiodic heterogeneous materials：quasiperiodic(2)；materials(2)；function(2)；based(1)；classical(1)；notion(1)；symmetry(1)；periodic(1)
- 2.1. Heterogeneous quasiperiodic material：function(8)；quasiperiodic(7)；coe(7)；group(6)；cients(5)；lattice(5)；periodic(4)；fourier(4)
- 2.2. On the notion of indistinguishability：functions(14)；properties(7)；correlation(7)；indistinguishability(7)；condition(7)；gauge(7)；periodic(6)；density(6)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 原文表达模式：先承认已有进展，再指出关键对象仍被混淆、不可测、不可控或判据不适用。
- 可复用句型骨架：`Although X has been extensively studied, Y remains unresolved because Z.`
- 中文写作启发：gap 要写“为什么现有方法看不到”，不要只写“研究较少”。
### 14.2 方法与框架表达
- 原文表达模式：`To decouple/capture/detect/control X, we combine A with B.`
- 可复用句型骨架：`We first establish a baseline, then introduce X to quantify Y.`
- 中文写作启发：方法模块要和 gap 一一对应。
### 14.3 结果与趋势表达
- 原文表达模式：先总体趋势，再关键定量，再与 baseline 比较。
- 可复用句型骨架：`Increasing X shifts the response from A to B, while C remains nearly unchanged.`
- 中文写作启发：结果要提炼成转变、边界或权衡。
### 14.4 机制解释表达
- 原文表达模式：`This behavior can be attributed to...` / `These observations suggest...`
- 可复用句型骨架：`The competition between X and Y governs the transition from A to B.`
- 中文写作启发：机制推断要和证据强度匹配。
### 14.5 贡献与意义表达
- 原文表达模式：贡献被写成新能力，而非仅“提出模型”。
- 可复用句型骨架：`This work recasts X from Y into Z and provides a framework for A.`
- 中文写作启发：让读者知道读完后能做什么。
### 14.6 局限与未来工作表达
- 原文表达模式：主动限定窗口、模型和数据。
- 可复用句型骨架：`The present study focuses on X; extending it to Y requires Z.`
- 中文写作启发：局限写得好，会保护主 claim。

## 15. 引用策略与文献使用
- 引用密度：- 引用密度：Introduction 和理论定义段较高。 - 文献组织：architectured materials/metamaterials -> crystallography and symmetry -> quasicrystals and aperiodic order -> homogenization/tiling mechanics。 - 引用姿态：对凝聚态文献是继承，对材料力学领域是迁移和补充。 - 引用偏好：经典群论/准晶文献与近年 architectured materials 文献混合，增强跨学科合法性。
- 引用主要集中位置：Introduction、Method 选择依据和 Discussion 机制对照。
- 经典文献用途：建立概念合法性和理论基线。
- 近年文献用途：说明应用需求与当前技术窗口。
- 方法文献用途：支撑实验规范、数值方法、图像算法、网络结构或本构模型。
- 对比/批判性引用：多用温和转折，少用直接否定。
- gap 如何靠引用搭建：把已有研究分成“能解决什么/不能解决什么”。
- references 暗示的研究共同体：本文通常跨越固体力学、材料科学、计算方法和具体应用社群。
- 引用风险：若缺少最接近 competitor，审稿人会质疑 gap。

## 16. 审稿人视角风险
- 最大攻击面：- 最容易被质疑：算法手动环节和噪声鲁棒性；有限窗口图像对无限准周期结构的代表性。 - claim 与证据匹配：Penrose D10 在所用判据下匹配；不能误读为几何可叠合意义下 D10。 - 方法风险：Fourier peak threshold、fundamental frequencies 选择会影响 deviation measure。 - 需进一步核查：图 16-21 的 deviation 数值和 Fourier peak 分布需结合 PDF 图像确认。
- claim 是否过强：核心范围内可接受；标题和摘要中的广义意义需靠正文限定。
- 证据是否不足：宏观或数值证据较足，微观/真实工况/长期循环/多材料泛化可能不足。
- 方法是否可复现：需要 PDF、补充材料和参数表进一步核查。
- 对比是否充分：baseline 有，但最接近前人对比需重点检查。
- 边界条件是否清楚：正文通常清楚，摘要较强。
- 替代解释是否排除：部分机制仍可能存在替代解释。
- 图表是否需要进一步核查：需要，尤其所有图像本体。

## 17. 可复用资产
- 可复用选题角度：- 可复用选题角度：把其他学科成熟概念迁移到材料图像和均匀化问题中。 - 可复用论证套路：传统判据的适用边界 -> 更弱/更一般判据 -> Fourier 可计算化 -> 争议案例验证。 - 可复用写法：用一个反直觉案例（Penrose D10 vs D5）作为整篇方法价值的锚点。 - 可复用图表：概念对比图；Fourier peak selection；deviation measure 热图/条图；判据流程图。 - 不宜直接模仿：如果没有清晰数学定义，不要把“统计相似”泛化为“对称”。
- 可复用 gap 制造方式：从传统方法遮蔽的层次入手。
- 可复用论证链：baseline -> intervention/framework -> evidence -> mechanism -> boundary。
- 可复用图表设计：对象图、方法图、核心曲线、参数/相图、机制示意、边界/风险图。
- 可复用段落结构：主题句 + 图中事实 + 机制解释 + 下一步引导。
- 可复用句型骨架：`X is often viewed as Y; here we show that Z.`
- 可复用引用组织：文献按能力分组。
- 不宜直接模仿之处：没有直接证据时不要模仿强反转标题。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学什么：- 最值得学习：从判据层面重写问题，而不是只改算法。 - 最大风险：真实材料图像、3D 和非离散 Fourier 谱的可用性仍未完全证明。 - 可迁移三件事：先定义判据；再给可计算指标；最后用一个概念争议案例证明指标有必要。
- 可以迁移到 Introduction 的写法：先把大问题收窄到一个可测/可算/可判定 gap。
- 可以迁移到 Method 的写法：每个方法模块都对应一个 claim。
- 可以迁移到 Results/Discussion 的写法：Results 讲证据，Discussion 讲机制和边界。
- 需要避免的问题：不要把特定系统结论外推成普遍定律；不要让复杂方法掩盖问题链。

## 19. 最终浓缩
- 这篇论文最值得学：从判据层面重写问题，而不是只改算法。
- 这篇论文最大风险：真实材料图像、3D 和非离散 Fourier 谱的可用性仍未完全证明。
- 三个可迁移动作：建立 baseline；设计直接对准 gap 的方法；把图表结果翻译成机制、判据或设计规则，并明确边界。
