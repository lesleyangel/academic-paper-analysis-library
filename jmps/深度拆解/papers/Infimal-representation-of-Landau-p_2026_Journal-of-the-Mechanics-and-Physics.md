# Infimal representation of Landau potentials

## 0. 读取说明
- 源 PDF：`jmps/文献/Infimal-representation-of-Landau-p_2026_Journal-of-the-Mechanics-and-Physics.pdf`
- 源 TXT：`jmps/文本/txt/Infimal-representation-of-Landau-p_2026_Journal-of-the-Mechanics-and-Physics.txt`
- 是否需要结合 PDF 图像核查：需要。本文公式、路径图、自由能曲线、微结构颜色和附录导数需结合 PDF。
- 本文类型：大变形相变理论/自由能势构造论文。

## 1. 基本信息与论文身份
- 题名：Infimal representation of Landau potentials
- 作者/机构：Christophe Denoual, Nicolas Bruzy；CEA DAM / Universite Paris-Saclay。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 214 (2026) 106653。
- DOI：10.1016/j.jmps.2026.106653
- 关键词：Martensitic phase transformation; Phase transition; Transformation graph
- 研究对象：稳定/亚稳态集合下的 Landau 型自由能势、马氏体/孪晶等位移型相变、路径图和 infimal convolution。
- 研究尺度：晶格稳定态、有限应变、自由能地形、路径图、塑性耦合、多变体微结构。
- 方法类型：理论推导、infimal convolution、Moreau regularization、路径图、有限应变热力学、示例计算。
- 证据类型：闭式推导、概念图、自由能/压力曲线、Ce/Fe 相变示例、迟滞和微结构模拟、附录应力导数。
- 目标读者：相变理论、相场模型、有限变形热力学、高压材料和理论力学读者。
- JMPS 风格定位：典型理论 JMPS 论文，先构造一般框架，再用物理示例说明框架不是形式游戏。

## 2. 摘要与核心信息提取
- 摘要的功能拆解：先提出为任意稳定/亚稳态集合定义大应变自由能势；再说明势基于 stable states graph 与 continuous transformations；随后指出自由能由弹性二次势和 transformation potential 的下确界卷积组成；最后强调非耗散相变、相依赖弹性、非凸过渡态、应力闭式表达和示例。
- 背景句承担什么：把 displacive transitions、martensitic transformation、twinning 引入为需要非凸自由能势的对象。
- gap 句承担什么：说明已有 Landau/GL/PF-RP 模型难以同时处理任意多稳定态、有限应变、相依赖弹性和非耗散表示。
- 方法句承担什么：交代 graph of pathways、infimal convolution、Moreau regularization、isoinfimal projection。
- 结果句承担什么：说明可得到 stress/stiffness 等闭式表达，并能描述 nonlinear elasticity、Fe 相变迟滞和塑性耦合。
- 意义句承担什么：把数学表示回收到 intense loading、复杂相变和多变体微结构模拟。
- 一句话主张：位移型相变的 Landau 势可以通过“弹性能 + 转变势”的下确界表示和路径图来构造，从而在有限应变下获得仅依赖总/塑性应变的非耗散自由能、应力和刚度表达。
- 3-5 个核心关键词：infimal convolution; Landau potential; graph of pathways; Moreau regularization; displacive phase transition。

## 3. 选题层深拆
- 问题来源：马氏体和重构相变包含多稳定态、多路径、非凸能量和快速位移型演化，传统内部变量动力学不总是理想。
- 问题为什么重要：自由能势决定相变路径、迟滞、微结构和应力响应；势构造不合理会导致错误刚度、错误压力-体积关系和不可控分支。
- 问题为什么现在值得做：冲击铁相变、高压 EOS、多变体路径图和 PF-RP 的前期发展共同要求更可控的有限应变势函数。
- 问题边界：本文主要考虑变形依赖势，温度依赖留给未来；路径和映射有构造性成分，示例用于展示框架能力。
- 选题的 JMPS 味道：不是解一个具体工程算例，而是重写相变势函数的基本表示。
- 选题可迁移性：可迁移为“把复杂内部变量过程转化为能量极小化表示”的理论选题。

## 4. 领域位置与文献版图
- 作者如何划分已有研究：Landau/Ginzburg-Landau 理论、Khachaturyan/Levitas 多变体相变、PF-RP 反应路径模型、Moreau/Legendre 数学工具、高压 Fe/Ce 相变实验与模拟。
- 主要研究流派/方法路线：经典 Landau 势、多相场/GL 动力学、反应路径相场、变分能量极小化、EOS 高压模型。
- 每类研究解决了什么：Landau 提供序参量语言；相场提供微结构演化；PF-RP 提供路径势；Moreau 提供正则化和 infimal 工具。
- 每类研究留下什么不足：内部变量常带耗散动力学；多路径重构相变分支复杂；相依赖弹性和压力-体积关系难以同时精确保持。
- 本文站在哪条线上：继承 PF-RP，但把转变变量由耗散内部变量转为下确界 argmin。
- 最接近前人工作：Denoual/Vattre/Bruzy 的 PF-RP，Levitas 多变体 Landau 理论，Moreau regularization。
- 是否公平处理前人：作者明确承认本文建立在 previous modeling 上，是从耗散版本转向 infimal/non-dissipative 版本。

## 5. Gap 制造机制
- 明示 gap：缺少一种能在有限应变下处理任意稳定/亚稳态图、保持相依赖弹性并给出应力闭式表达的 infimal Landau 势。
- 隐含 gap：若转变梯度作为独立耗散内部变量，会引入额外动力学参数；若只用局部势，难以组织多路径分支。
- gap 类型：理论 gap、表示 gap、热力学一致性 gap。
- gap 证据来自哪里：Introduction 对 GL/PF-RP 的回顾，Sections 2-6 的数学构造需求，Examples 对迟滞和微结构的展示。
- gap 是否足够窄：足够窄，集中在自由能势的 infimal 表示、路径图和导数。
- gap 是否足够重要：重要，因为势函数是后续相场/动力学模拟的核心。
- 如果我是审稿人会如何追问：路径图和投影映射是否唯一？ad hoc 构造会不会改变物理预测？无耗散假设适用边界在哪里？

## 6. 创新性判断
- 作者声称的贡献：定义任意稳定/亚稳态集合的自由能势；提出路径图和 infimal convolution；给出 Moreau 正则化、isoinfimal projection、应力/刚度闭式表达；展示非线性弹性和 Fe 相变示例。
- 我判断的真实创新：把 PF-RP 的反应路径思想改写成下确界自由能，使转变梯度不再作为独立耗散变量，而由总变形下的能量极小确定。
- 创新类型：理论表示创新 + 热力学框架创新 + 示例验证。
- 创新强度：高，但阅读门槛高。
- 创新必要性：必要，若要处理复杂图结构相变，需要比单路径序参量更强的表示。
- 创新与证据匹配度：数学推导充分，示例能说明物理现象；定量实验验证不是本文主线。
- 容易被挑战的创新点：投影/路径构造的非唯一性，参数校准难度，复杂公式实现成本。

## 7. 论证链条复原
`背景 -> 文献 -> gap -> 问题 -> 方法 -> 证据 -> 发现 -> 机制 -> 意义`：

1. 背景：位移型相变具有多稳定态、非凸能量、快速演化和微结构。
2. 文献：GL、Landau、PF-RP、Levitas 等模型提供基础，但仍有表示和耗散问题。
3. gap：如何在有限应变下为任意路径图构造可求导的自由能？
4. 问题：如何用 infimal operation 消除独立转变变量，同时保留相变路径信息？
5. 方法：infimum transform -> 有限应变模型 -> Clausius-Duhem -> graph of pathways -> isoinfimal projection -> stress/stiffness。
6. 证据：Fig. 1-3 概念和一维势；Fig. 6-11 例子；附录导数。
7. 发现：infimal 势可产生压力-体积关系、迟滞和多变体微结构。
8. 机制：给定总变形后，系统通过自由能下确界自动选择路径位置；塑性和残余应力影响迟滞。
9. 意义：为复杂相变提供可扩展势函数构造。

## 8. 方法/理论/模型细拆
- 方法总框架：先介绍 infimum/Legendre/Moreau 工具；再在有限应变下定义运动学分解和热力学不等式；随后构建路径图；再定义沿路径和路径邻域的自由能；最后推导导数并加入塑性。
- 关键概念：Landau potential、infimal convolution、transformation graph、pathway、Moreau regularization、isoinfimal projection、Clausius-Duhem。
- 关键变量/参数：总变形梯度 F、Cauchy-Green 张量 C、转变梯度 Ft、塑性梯度 Fp、路径参数 s/t、弹性能 ψe、转变势 ψt、体积比 v/v0。
- 核心假设：路径可由稳定态和连续转变段近似；某些映射可构造成足够光滑；温度依赖暂不处理；无塑性时相变非耗散。
- 边界条件：有限应变运动学、稳定态点群旋转、弹性张量、路径 stretch tensor、EOS 数据、加载循环。
- 方法步骤：数学变换工具 -> 有限应变 infimal 模型 -> 路径图 -> 自由能定义 -> 应力/刚度 -> 塑性扩展 -> 示例。
- 复现信息：公式和附录较充分，但必须核查 PDF 公式排版和符号。
- 方法复杂度是否合理：合理。复杂度来自多态相变本身，不是装饰性数学。
- 方法与 gap 的对应关系：infimal 表示回答“如何不用独立耗散变量仍描述转变路径”；路径图回答“如何组织多稳定态分支”；闭式导数回答“如何作为本构使用”。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 任意稳定/亚稳态集合可由路径图组织成自由能势 | 摘要/4-5 | graph of pathways 与沿路径势定义 | 理论构造 | 强 | 路径选择非唯一 |
| infimal convolution 使势只依赖总/塑性应变 | 摘要/3-5 | 下确界定义和有限应变分解 | 推导 | 强 | 唯一最小假设需讨论 |
| Moreau regularization 可控制过渡态刚度 | 2/5/8 | Fig. 2-3、Fig. 6-7 | 数学+示例 | 中强 | 参数选择敏感 |
| 可得到应力和刚度闭式表达 | 6/附录 C | First Piola-Kirchhoff stress 导数 | 推导 | 强 | 实现复杂 |
| Fe 示例中迟滞可由能量地形和体积-偏应变耦合产生 | 8.2 | Fig. 9-10 | 示例模拟 | 中强 | 示例代表性有限 |
| 残余应力是循环迟滞的重要贡献者 | 8.2.4/结论 | 多路径微结构 Fig. 11 | 模拟 | 中 | 需实验校准 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 最小能量路径、路径图和 Bain 转换投影 | 多态相变可图结构化 | 给抽象理论直观入口 | 是 |
| Fig. 2-3 | Moreau 正则化和一维 infimal 势 | infimal transform 控制非凸势 | 解释数学工具物理功能 | 是 |
| Fig. 6-7 | EOS 和 Fe 路径自由能 | 稳定态弹性和过渡态势可同时表示 | 展示构造可落地 | 是 |
| Fig. 8-9 | 载荷与压力-体积迟滞 | 模型产生相变迟滞 | 连接理论与可观测曲线 | 是 |
| Fig. 10-11 | 能量地形与微结构 | 迟滞、塑性和变体相互作用 | 机制解释 | 是 |
| 关键公式组 | ψ=inf(ψe+ψt)、Clausius-Duhem、P=dψ/dF | 热力学一致与应力输出 | 使势函数成为可计算本构 | 需核查公式排版 |

## 11. 章节结构与篇章布局
- Abstract：问题、图结构、infimal 势、非耗散、闭式应力和示例。
- Introduction：从位移型相变和 GL/PF-RP 传统进入，分条说明本文要解决的建模组件。
- Related Work/Background：嵌入 Introduction，引用密集且理论谱系明显。
- Method/Theory/Model：2-7 节全部是理论构造，从数学工具到塑性。
- Results：8 Examples 承担结果功能。
- Discussion：分散在示例和结论中。
- Conclusion：回收 infimal decomposition、Moreau、路径图、闭式表达和 Fe 迟滞。
- 章节之间如何过渡：数学工具 -> 有限应变 -> 路径图 -> 能量 -> 导数 -> 塑性 -> 示例。
- 哪一节最值得模仿：5-6 节，把抽象自由能构造落到 stress/stiffness 输出。
- 哪一节可能存在结构风险：5-6 节公式密集，非领域读者容易失去主线。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Infimal-representation-of-Landau-p_2026_Journal-of-the-Mechanics-and-Physics.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：22
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Transformation of potentials | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1 Kinematic composition | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.3 Clausius-Duhem inequality | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4 Graph of pathways | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.2 Invariance of the free energy for any rotation of the PGr | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.2.1 Rotation of a pathway | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.2.2 Rotation of a pathway around a deformation gradient (state) | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.2.3 Building a graph of pathways | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 5 Free energy function | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5.2 Free energy in the vicinity of a pathway | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 5.3 Interpolation between pathways | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 6 Energy and derivatives | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 6.1 Interpolation between pathways | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
- Introduction 段落推进：现象和理论传统 -> 前人 PF-RP -> 本文 infimal 版本 -> 后文路线。
- Method 段落推进：定义符号，给变换，解释性质，再进入更高维/更一般情形。
- Results 段落推进：先简单一维/非线性弹性，再复杂 Fe α-ε 相变。
- Discussion/Conclusion 段落推进：强调非耗散、路径图、闭式表达和塑性/残余应力效应。
- 常见段落开头方式：`We define...`; `The proposed developments are based on...`; `For a single pathway...`; `The extension is then...`。
- 常见段落收束方式：以公式性质、映射定义或示例现象作为段尾。
- 可复用段落模板：理论论文可用“existing formulation -> limiting assumption -> new transform -> property -> example”。

## 13. 文笔画像与语言习惯
- 整体语气：理论密集、定义驱动、低修辞。
- claim 强度：对数学框架 claim 强，对物理示例的普遍性较谨慎。
- 谨慎表达：ad hoc、example、particular attention、could be derived 等表达控制边界。
- 问题表达：强调 arbitrary set、large strain、non-dissipative、graph。
- 贡献表达：`is defined`, `is proposed`, `closed-form expression is presented`。
- 机制表达：迟滞来自能量拓扑、体积-偏应变耦合和残余应力。
- 对比表达：dissipative PF-RP vs infimal/non-dissipative version。
- 限定边界表达：温度依赖、唯一性、未来扩展。
- 术语密度：很高，且符号系统复杂。
- 长句/短句习惯：理论长句多，结论句较压缩。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：energy(113)；pathway(110)；deformation(88)；function(78)；strain(73)；potential(68)；free(67)；denoual(63)；transition(61)；inf(61)；fe-(56)；pathways(55)；transformation(54)；mal(53)；phase(53)；along(52)；evolution(48)；nition(48)；section(47)；ned(46)
- 高频学术名词：deformation(176)；transition(122)；energy(113)；function(78)；strain(73)；transformation(54)；evolution(48)；nition(48)；section(47)；pressure(40)；ness(37)；model(36)；reference(32)；stress(31)；elasticity(31)；plasticity(26)
- 高频学术动词：proposed(18)；derived(5)；estimate(5)；estimated(4)；shows(4)；solved(3)；show(3)；compared(2)；demonstrated(2)；derive(1)；demonstrate(1)；shown(1)；propose(1)；indicates(1)；developed(1)；investigated(1)
- 高频形容词：elastic(68)；potential(68)；denoual(63)；plastic(56)；mal(53)；stable(48)；gradient(40)；transformational(38)；derivative(29)；variable(27)；quadratic(22)；deviatoric(22)；internal(21)；possible(19)；displacive(17)；local(16)
- 高频副词/连接副词：therefore(20)；generally(10)；however(9)；numerically(8)；strongly(4)；experimentally(4)；usually(4)；possibly(3)；purely(3)；solely(3)；approximately(2)；markedly(2)；plastically(2)；easily(2)；strictly(2)；spatially(1)
- 高频二词短语：free energy(55)；sti ness(37)；deformation gradient(35)；denoual bruzy(34)；along pathway(28)；cauchy-green strain(23)；graph pathways(19)；inf inf(18)；energy along(17)；isoin mal(16)；moreau regularization(16)；internal variable(15)；fe- fe-(15)；volume variation(13)；phase transition(12)；stable states(11)
- 高频三词短语：isoin mal projection(10)；energy along pathway(10)；free energy along(9)；inf inf inf(6)；fe- fe- transition(6)；gpa elasticity components(6)；elasticity components fe-(6)；denoual vattr vattr(5)；vattr vattr denoual(5)；minimum energy path(5)；part deformation gradient(5)；adams gpa elasticity(5)

**主动、被动与句法**

- 被动语态估计次数：247
- `we + 动作动词` 主动句估计次数：11
- 名词化表达估计次数：1546
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：366
- 一般过去时线索：44
- 现在完成时线索：10
- 情态动词线索：54
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：potential(8)；states(6)；stable(5)；graph(5)；transformation(4)；mal(3)；martensitic(3)；transition(3)
- 1. Introduction：evolution(16)；section(15)；deformation(14)；energy(14)；transformation(13)；denoual(13)；variable(12)；transitions(11)
- 2. Transformation of potentials：transform(17)；energy(16)；function(15)；deformation(11)；pathway(11)；transformational(10)；sti(10)；potential(10)
- 3.1. Kinematic composition：strain(8)；inf(6)；deformation(5)；bruzy(5)；variable(5)；tensor(5)；denoual(4)；see(4)
- 3.3. Clausius-Duhem inequality：stress(2)；det(2)；tensor(1)；inf(1)；function(1)；two(1)；variables(1)；leads(1)
- 4. Graph of pathways：pathway(9)；frame(7)；deformation(6)；states(5)；noted(5)；nition(4)；transformational(4)；graph(4)
- 4.2. Invariance of the free energy for any rotation of the PGr：pathway(7)；reference(4)；any(3)；rotation(3)；must(3)；node(3)；set(2)；pathways(2)
- 4.2.1. Rotation of a pathway：rotation(5)；pathway(1)；set(1)；corresponding(1)；operations(1)；functions(1)；type(1)；rotated(1)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 原文表达模式：`A free energy potential for an arbitrary set of stable or metastable states is defined...`
- 可复用句型骨架：`A [quantity/model] for an arbitrary set of [states] is constructed to describe [process].`
- 中文启发：理论论文可以直接以“定义一个对象”作为摘要开头。

### 14.2 方法与框架表达
- 原文表达模式：`This potential is based on...`
- 可复用句型骨架：`The construction is based on [structure A] and [operation B], where [component C] encodes [information].`
- 中文启发：说明每个数学部件存储什么物理信息。

### 14.3 结果与趋势表达
- 原文表达模式：`A closed-form expression for stress... is presented.`
- 可复用句型骨架：`The proposed formulation yields an explicit expression for [observable], enabling [use].`
- 中文启发：理论贡献要落实到可计算输出。

### 14.4 机制解释表达
- 原文表达模式：`hysteresis is due to the topology of the energy potential...`
- 可复用句型骨架：`The observed hysteresis can be interpreted as a consequence of [energy topology/coupling].`
- 中文启发：把现象归因于能量地形，而非只描述曲线。

### 14.5 贡献与意义表达
- 原文表达模式：`making this method particularly suitable for intense loading.`
- 可复用句型骨架：`This feature makes the formulation suitable for [regime] where [constraint] must be preserved.`
- 中文启发：意义句要指出适用 regime。

### 14.6 局限与未来工作表达
- 原文表达模式：`We defer to future developments...`
- 可复用句型骨架：`The dependence on [factor] is deferred to future developments.`
- 中文启发：理论论文可明确把某些物理因素留给后续版本。

## 15. 引用策略与文献使用
- 引用密度：Introduction 和示例背景处很高。
- 引用主要集中位置：Landau/GL、马氏体相变、PF-RP、Moreau、Fe/Ce 高压实验。
- 经典文献用途：Landau 1937、Moreau 1965、Ball-James、Christian、Nishiyama 等提供理论根。
- 近年文献用途：Arbib、Lemaire、Merkel、Hwang 等证明问题前沿性。
- 方法文献用途：PF-RP 和 finite strain plasticity 提供直接谱系。
- 对比/批判性引用：重点不是批判，而是把本文作为 previous modeling 的 infimal extension。
- gap 如何靠引用搭建：先建立相变理论传统，再说明 dissipative internal variable 的限制。
- references 暗示的研究共同体：相变理论、相场、变分微结构、高压铁、冲击物理。
- 引用风险：需要确保与 Levitas 和近年 reconstructive phase transformation 理论的差异足够清楚。

## 16. 审稿人视角风险
- 最大攻击面：框架一般性和投影/路径构造非唯一性之间的张力。
- claim 是否过强：数学构造 claim 强；物理预测 claim 需要更多材料验证。
- 证据是否不足：推导充分，实验 benchmark 较少。
- 方法是否可复现：公式足够多，但实现复杂，需 PDF 和附录。
- 对比是否充分：与 PF-RP 谱系清楚，与其他数值相场模型的性能对比不足。
- 边界条件是否清晰：温度依赖和耗散机制边界有说明。
- 替代解释是否排除：迟滞机制解释较有说服力，但仍可有材料特定因素。
- 图表是否需要进一步核查：需要，尤其 Fig. 1、Fig. 10、Fig. 11。

## 17. 可复用资产
- 可复用选题角度：把已有理论中的内部变量改写为能量极小化对象。
- 可复用 gap 制造方式：`Existing models introduce A as an internal variable; here A is determined by an infimal operation.`
- 可复用论证链：数学工具 -> 热力学一致 -> 图结构 -> 导数输出 -> 示例。
- 可复用图表设计：概念路径图、一维示意势、压力-体积曲线、能量地形、微结构图。
- 可复用段落结构：定义对象 -> 说明性质 -> 说明物理含义 -> 给示例。
- 可复用句型骨架：`The proposed construction preserves [property] while allowing [extension].`
- 可复用引用组织：经典理论奠基，作者前作承接，最新实验给应用场景。
- 不宜直接模仿之处：如果论文没有足够数学贡献，不宜模仿这种高密度符号推进。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学：把理论贡献拆成“变换、模型、图结构、导数、示例”。
- 可迁移到 Introduction：用分条方式提前告诉读者本文要构造哪些部件。
- 可迁移到 Method：每个定义后说明物理意义。
- 可迁移到 Results/Discussion：理论论文也要给足够示例，不然会显得空转。
- 需要避免的问题：避免公式连续出现而没有概念图；避免在结论中夸大示例普适性。

## 19. 最终浓缩
- 这篇论文最值得学：理论建模论文如何从数学操作一路落到应力、刚度和物理示例。
- 这篇论文最大风险：infimal/pathway 构造的唯一性、可校准性和实现复杂度。
- 三个可迁移动作：
  1. 用概念图把抽象理论先可视化。
  2. 每个数学对象都说明存储的物理信息。
  3. 用简单示例和复杂示例双层验证理论。

最终判断：这是一篇理论密度很高的 JMPS 论文。它最适合作为理论框架论文的结构样本，而不是普通应用论文的写法样本。
