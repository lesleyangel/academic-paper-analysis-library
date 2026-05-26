# Three-dimensional third medium contact model for hyperelastic contact and pneumatically actuated systems

## 0. 读取说明
- 源 PDF：`jmps/文献/Three-dimensional-third-medium-contact-model-for-_2026_Journal-of-the-Mechan.pdf`
- 源 TXT：`jmps/文本/txt/Three-dimensional-third-medium-contact-model-for-_2026_Journal-of-the-Mechan.txt`
- 元数据：Journal of the Mechanics and Physics of Solids, 213 (2026) 106617, DOI: 10.1016/j.jmps.2026.106617。
- 是否需要结合 PDF 图像核查：需要。本文证据包括 third medium 概念图、有限元离散图、自接触盒体、gap/regularization 参数图、punch problem、气动盒体和软机器人执行器变形图；当前依据 txt 和图注拆解，所有变形形貌、应力云图、网格质量和图中参数需 PDF 核查。
- 本文类型：计算接触力学方法论文，扩展 third medium contact 到三维超弹性接触和气动驱动系统。

## 1. 基本信息与论文身份
- 题名：Three-dimensional third medium contact model for hyperelastic contact and pneumatically actuated systems。
- 作者/机构：Bing-Bing Xu, Tianju Xue, Peter Wriggers；Hong Kong University of Science and Technology、Leibniz University Hannover。
- 关键词：Contact; Third medium contact; Regularization。
- 研究对象：3D hyperelastic contact、self-contact、third medium layer、pneumatic loading、incremental-rotation-gradient regularization。
- 研究尺度：三维盒体自接触、旋转自接触、punch problem、pneumatically actuated box、soft robot actuator。
- 方法类型：third medium as hyperelastic barrier + modified strain energy density + new regularization term based on incremental rotation gradient + weak form/linearization + higher-order FE implementation + benchmark simulations。
- 证据类型：不同 regularization term 下 gap、收敛和 time cost；3D box displacement/rotation self-contact；punch contact deformation/stress；pneumatic suction/inflation examples；soft robot actuator simulation。
- 目标读者：计算接触力学、软机器人、超弹性有限元、IGA/meshless 方法和多体大变形模拟读者。
- JMPS 风格定位：典型计算方法论文。它的 JMPS 价值在于把接触界面搜索和不等式约束转化为连续介质能量问题，并给出三维弱式、线性化和复杂算例。

## 2. 摘要与核心信息提取
摘要先指出复杂 hyperelastic solids 和 pneumatically actuated systems 中接触/自接触建模困难。传统接触算法需要 discretization of contact interface、contact search 和 constraint enforcement。本文采用 third-medium formulation：在潜在相互作用物体之间嵌入第三介质，使 contact/self-contact 变成统一的有限变形问题。

方法贡献有三点。第一，提出适用于三维问题的新 regularization term，保证 third medium 元素质量。第二，由于 regularization 需要 higher-order elements，论文详细推导有限元线性化和 tangent stiffness。第三，引入 pneumatic term 表示 pressure/suction，使内部充气导致的接触可在同一框架中处理。

一句话主张：本文把三维复杂接触从“界面搜索 + 不等式约束”改写为“在潜在接触区填充 third medium 的标准有限变形问题”，并通过新的增量旋转梯度正则化提升第三介质网格质量和稳定性。

## 3. 选题层深拆
问题来源：软材料、软机器人和气动执行器常发生大变形接触、自接触、内腔闭合和局部挤压。传统 node-to-node、node-to-segment、mortar、penalty、Lagrange multiplier、augmented Lagrangian、Nitsche 等方法虽然成熟，但需要接触面搜索、投影和不等式约束，在复杂自接触中实现繁琐。

问题为什么重要：软机器人/柔性机构的设计依赖准确预测内部压力驱动下的变形和接触。如果接触算法不稳定，仿真难以作为设计工具。third medium contact 的吸引力在于不显式处理接触界面，而是把不可穿透条件编码进介质能量。

问题为什么现在值得做：二维 TMC 已有基础，三维大变形软体系统需求增长，higher-order FE、automatic differentiation 和弱式推导可支撑更复杂正则化。本文把 TMC 推向 3D hyperelastic contact 和 pneumatic applications。

问题边界：本文处理 frictionless contact；third medium 区域需要预先定义；参数选择影响 gap 和稳定性；没有系统讨论摩擦、磨损、真实实验验证和自动潜在接触域生成。

## 4. 领域位置与文献版图
文献先覆盖 classical computational contact mechanics：接触离散、约束 enforcement 和自接触处理。随后引入 Wriggers et al. 的 third medium contact 思路：通过在接触体之间加入各向异性第三介质，避免显式界面处理。

本文站位：继承 TMC 的“barrier medium”思想，但补上三维公式、element quality regularization、pneumatic loading 和多个应用算例。它强调不是单纯多一个算例，而是给出 weak form and linearization，使方法可被 FE 实现。

文献处理策略稳健：先承认传统接触算法成熟，再说明其复杂性；再承认二维 TMC 已有基础，最后指出三维正则化和气动系统是本文增量。

## 5. Gap 制造机制
明示 gap：existing third medium contact 主要集中于二维或有限场景，三维 third medium 元素质量和稳定性需要新的 regularization；气动驱动系统中的压力/吸力和接触诱导变形需要统一能量项。隐含 gap：若没有完整线性化和 tangent stiffness，方法很难进入工程有限元实现。

gap 类型：维度 gap + 数值稳定 gap + 应用 gap + 实现 gap。维度 gap 是从 2D 到 3D；稳定 gap 是 third medium element overlap；应用 gap 是 pneumatic soft systems；实现 gap 是 weak form/tangent matrix 细节。

审稿人追问：third medium 区域如何自动选取；参数 γ、αr、αθ 对结果敏感性如何；与 mortar/penalty 等传统方法的定量误差和成本比较是否足够；frictional contact 如何扩展。

## 6. 创新性判断
创新包括三维 third-medium strain energy、pneumatic part、incremental rotation gradient regularization、完整弱式和线性化、二阶导 shape function 实现。它的贡献偏“工程数值实现型”：把一个有潜力的思想补成可跑复杂 3D 算例的公式体系。

创新强度：中高。TMC 思想不是首次提出，但三维化和新正则化是实质性工作。尤其是新 regularization term 在 gap 控制和 computational efficiency 上优于旧项，是本文最直接的技术亮点。

创新必要性：强。没有正则化，third medium 可能发生元素重叠或网格质量恶化；没有 pneumatic term，软体气动系统仍需要外部载荷/接触耦合技巧。

## 7. 论证链条复原
背景：大变形软材料和气动系统接触复杂。 -> 文献：传统接触算法需要搜索和约束；TMC 可避免界面处理但三维实现仍需发展。 -> gap：三维第三介质元素质量、弱式线性化和 pneumatic loading 未系统闭合。 -> 问题：如何构建适用于 3D hyperelastic contact/self-contact/pneumatic systems 的 TMC FE 框架。 -> 方法：定义第三介质能量、加入新 regularization 和 pneumatic term，推导 weak form、linearization、discrete FE matrices。 -> 证据：box self-contact、rotation self-contact、punch、pneumatic box、soft robot actuator。 -> 发现：新正则化可更好避免 element overlap，并提高稳定性和效率。 -> 意义：为软机器人和复杂柔性机构接触仿真提供统一框架。

## 8. 方法/理论/模型细拆
主体和 third medium 都在有限变形框架下表示，基本超弹性能量采用 Neo-Hookean 形式。TMC 的思想是：third medium 未接触时非常软，对主体变形影响小；当两体接近时，third medium stiffness 快速增加，阻止穿透。

传统正则化可基于 deformation gradient 或 gradient of deformation gradient。本文新增 incremental rotation gradient regularization，用来改善三维 third medium element quality。由于涉及高阶导数，FE 实现需要二阶 shape-function derivatives，并在弱式中推导 residual 与 tangent stiffness。

pneumatic term 被加入 third medium strain energy density，用 pressure/suction 表示气动加载，并可诱导内部膨胀和接触。算例从简单自接触到气动执行器，展示框架覆盖范围。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| third medium 可把接触不等式约束转化为标准有限变形问题 | Section 2/Fig.1 | 第三介质填充潜在接触区、能量项随接近变硬 | 理论构造 | 强 | 潜在接触区域仍需人为预估 |
| 新的 incremental rotation gradient regularization 能改善第三介质元素质量 | Section 2.3/Fig.5/Table 2 | 不同参数下 gap 更小、不收敛点减少 | 数值对比 | 中强 | 参数选择仍影响结果 |
| 完整弱式、线性化和 tangent stiffness 支持三维 FE 实现 | Section 3-4 | hyperelastic body 与 third medium 分别推导、B1/B2 矩阵、二阶导 shape functions | 公式推导 | 强 | 公式复杂，复现需代码细节 |
| 三维 box 自接触和旋转自接触可稳定模拟 | Fig.3-9 | deformed configuration、von-Mises stress、rotation angle increments | benchmark | 中强 | 视觉证据需 PDF 核查 |
| punch problem 可作为外部接触 benchmark | Fig.10-12 | punch geometry、deformed configurations、stress contours | benchmark | 中 | 缺少与经典接触法定量误差表 |
| pneumatic term 使模型可处理气动盒体和软机器人执行器 | Fig.13-18 | suction/inflation deformation、soft actuator example | 应用演示 | 中强 | 气动材料/压力实验验证不足 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig.1 | 两体之间嵌入 third medium 的概念图 | 方法定义 | 替代传统界面接触的核心图 | 需结合 PDF 图像核查 |
| Fig.2 | 有限元离散示意 | 实现 claim | 将连续体问题落到 element 级 | 需结合 PDF 图像核查 |
| Fig.3-6/Table 1-3 | 3D box 自接触、regularization 对比 | 稳定性 claim | 用 gap/time cost 说明新正则化有效 | 需结合 PDF 表格核查 |
| Fig.7-9 | 旋转导致的 3D box 自接触 | 复杂 self-contact claim | 展示大旋转鲁棒性 | 需结合 PDF 云图核查 |
| Fig.10-12 | punch problem | 外部接触 benchmark | 展示非自接触场景 | 需结合 PDF 图像核查 |
| Fig.13-14 | pneumatically actuated box | 气动项 claim | 把 pressure/suction 纳入同一框架 | 需结合 PDF 图像核查 |
| Fig.15-18 | pneumatic soft robot actuator | 应用潜力 claim | 面向软机器人场景 | 需结合 PDF 图像核查 |
| 公式组 | strain energy、regularization、weak form、linearization、FE matrices | 方法闭合 | 从概念到可实现 tangent stiffness | 不涉及图像本体 |

## 11. 章节结构与篇章布局
Introduction 说明传统接触算法痛点和 TMC 前史。Section 2 给 governing equations：continuum model、third medium strain energy、新 regularization、pneumatic term。Section 3 推导 weak form and linearization。Section 4 进入 FE implementation，包括 conventional/new regularization discrete formulation 和 shape functions 二阶导。Section 5 用五类 numerical examples 展示稳定性和适用性。Conclusion 总结并指出可扩展到 IGA、virtual element、meshless，以及未来 frictional contact。

结构非常“方法论文”：先物理思想，再变分公式，再离散矩阵，最后 benchmark。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Three-dimensional-third-medium-contact-model-for-_2026_Journal-of-the-Mechan.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：20
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Governing equations for contact mechanics using a third medium | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.1 Continuum model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Strain energy density for the third medium | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.3 Incremental rotation gradient regularization | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.4 Pneumatic term | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Weak form and linearization | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1 Weak form and linearization for the hyperelastic body | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.2 Weak form and linearization for the third medium | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.3 Weak form and linearization for the new regulization term | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4 Finite element implementation | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.1 Discrete formualtion based on the conventional regulization | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.2 Discrete formualtion based on the new regulization | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 5 Numerical examples | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
Introduction 节奏：应用场景 -> 传统算法 -> TMC 思想 -> 现有不足 -> 本文三维/正则化/气动贡献。Governing equations 段落不断解释能量项的功能，避免公式孤立。

Weak form/FE implementation 段落密集但功能明确：给实现者 residual/tangent 所需的所有矩阵。Numerical examples 从简单盒体自接触开始，再加入旋转、punch、气动盒体和软机器人执行器，复杂度逐步增加。

可复用节奏：计算方法论文要把“能跑”拆成公式可推、矩阵可组、算例可收敛三件事。

## 13. 文笔画像与语言习惯
整体语气工程实现导向，常用 “we derive”“we introduce”“it can be seen that”“the results show” 推进。与纯理论论文相比，本文更重视 implementation details 和 numerical examples。

claim 强度适中：对新正则化的 gap/efficiency claim 较明确，对软机器人应用则说 “potential applications”。文本中有少量拼写错误如 regulization/formualtion，但不影响主线。

术语稳定：third medium contact、regularization term、incremental rotation gradient、pneumatic term、weak form、linearization、tangent stiffness。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：third(73)；medium(72)；contact(68)；regularization(55)；term(52)；box(36)；element(34)；energy(33)；gradient(30)；rotation(29)；deformation(28)；erent(28)；shown(27)；problem(25)；pneumatic(24)；model(23)；pneumatically(23)；tensor(23)；actuated(22)；strain(22)
- 高频学术名词：deformation(56)；regularization(55)；element(34)；energy(33)；simulation(32)；rotation(29)；model(23)；strain(22)；density(19)；stress(18)；pressure(18)；function(17)；displacement(16)；parameters(15)；framework(15)；linearization(12)
- 高频学术动词：shown(27)；proposed(21)；compared(4)；investigate(3)；demonstrate(3)；propose(3)；indicates(3)；developed(3)；simulate(2)；derived(2)；derive(1)；show(1)；simulated(1)；predicted(1)；investigated(1)；solve(1)
- 高频形容词：element(34)；gradient(30)；erent(28)；pneumatic(24)；hyperelastic(16)；displacement(16)；potential(14)；incremental(14)；material(11)；three-dimensional(9)；internal(9)；numerical(8)；computational(8)；initial(8)；tangent(8)；large(7)
- 高频副词/连接副词：pneumatically(23)；however(6)；newly(5)；generally(4)；analytically(4)；therefore(4)；successfully(4)；highly(4)；ectively(4)；directly(3)；automatically(3)；completely(3)；strongly(2)；potentially(2)；naturally(2)；finally(2)
- 高频二词短语：third medium(71)；regularization term(35)；pneumatically actuated(22)；strain energy(21)；energy density(19)；medium contact(16)；nite element(14)；density function(14)；actuated systems(12)；con guration(12)；incremental rotation(12)；potential energy(11)；von-mises stress(11)；regularization terms(10)；deformation gradient(10)；second order(10)
- 高频三词短语：strain energy density(19)；third medium contact(16)；energy density function(14)；pneumatically actuated systems(12)；proposed regularization term(9)；erent regularization terms(7)；incremental rotation gradient(7)；pneumatically actuated box(7)；density function third(6)；function third medium(6)；variation potential energy(6)；deformed con guration(6)

**主动、被动与句法**

- 被动语态估计次数：168
- `we + 动作动词` 主动句估计次数：6
- 名词化表达估计次数：518
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：191
- 一般过去时线索：45
- 现在完成时线索：8
- 情态动词线索：79
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：contact(11)；three-dimensional(5)；third(4)；medium(4)；hyperelastic(4)；pneumatically(3)；actuated(3)；systems(3)
- 1. Introduction：contact(24)；third(12)；medium(12)；problems(9)；wriggers(8)；term(8)；regularization(7)；systems(6)
- 2. Governing equations for contact mechanics using a third medium：无明显高频项
- 2.1. Continuum model：third(7)；medium(7)；contact(6)；con(4)；guration(4)；bodies(4)；deformation(3)；initial(3)
- 2.2. Strain energy density for the third medium：term(7)；regularization(7)；third(6)；medium(6)；bodies(4)；contact(4)；deformation(3)；two(3)
- 2.3. Incremental rotation gradient regularization：rotation(11)；gradient(8)；incremental(6)；eld(6)；regularization(4)；term(4)；tensor(4)；iteration(4)
- 2.4. Pneumatic term：pressure(5)；energy(3)；third(3)；medium(3)；pneumatically(2)；actuated(2)；systems(2)；strain(2)
- 3. Weak form and linearization：problem(2)；strain(2)；energy(2)；see(2)；based(1)；above(1)；analysis(1)；classical(1)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 骨架：Classical contact algorithms require contact search and constraint enforcement, which become cumbersome for complex self-contact.
- 启发：计算方法 gap 要写到实现痛点。

### 14.2 方法与框架表达
- 骨架：The contact problem is reformulated as a standard finite deformation problem by introducing a third medium.

### 14.3 结果与趋势表达
- 骨架：For the same parameters, the proposed regularization yields a smaller gap and improved convergence behavior.

### 14.4 机制解释表达
- 骨架：The third medium remains compliant before contact and stiffens rapidly as bodies approach, thereby preventing penetration.

### 14.5 贡献与意义表达
- 骨架：The framework enables a unified treatment of contact, self-contact and pneumatically induced contact in three dimensions.

### 14.6 局限与未来工作表达
- 骨架：Future work may extend the current frictionless formulation to frictional contact and first-order formulations.

## 15. 引用策略与文献使用
引用从接触力学经典教材和方法文献开始，如 Wriggers、Laursen、mortar、penalty、Nitsche 等，建立传统算法背景；随后引用 Wriggers et al. 的 third medium contact 作为直接前身；AD 和 FE 实现文献用于公式推导辅助。

gap 通过“传统方法成熟但复杂，TMC 简化界面但三维实现需完善”搭建。引用风险是与最新 3D TMC 或 phase-field/contact regularization 方法比较不足，可能被要求增加 baseline。

## 16. 审稿人视角风险
最大攻击面：third medium 区域需要人工预测；参数 γ、αr 对结果敏感；frictionless 假设限制应用；与传统接触算法缺少系统定量比较；气动算例偏演示，缺少实验验证。

claim 是否过强：适用于复杂 contact/self-contact 的 claim 有多个算例支持，但“robust”仍需在更多极端网格和材料参数下验证。方法是否可复现：公式详细，但实现高阶元素和二阶导不简单，代码会显著影响复现。

## 17. 可复用资产
- 可复用选题角度：把传统算法的实现痛点转化为连续介质能量模型。
- 可复用 gap：2D TMC 已有，但 3D regularization、linearization 和 pneumatic loading 未闭合。
- 可复用论证链：概念介质 -> 能量函数 -> 正则化 -> 弱式/线性化 -> FE 矩阵 -> benchmark ladder。
- 可复用图表：概念图、离散图、参数表、gap 曲线、变形/应力云图、应用算例。
- 不宜直接模仿：没有与传统算法对照时，不要过度声称全面优越。

## 18. 对我写论文的启发
计算方法论文可以学习本文的“公式到实现”完整度。提出新能量项后，必须给 weak form、linearization、discrete matrices 和 benchmark，不然方法难以被接触力学读者采用。

Introduction 可迁移“传统方法成熟但复杂”的写法；Method 可迁移“先连续体再弱式再离散”的层次；Results 可迁移“由简单到应用”的算例阶梯。

## 19. 最终浓缩
这篇论文最值得学：把接触界面问题转成 third medium 能量问题，并用三维正则化、线性化和 benchmark 让方法可实现。

这篇论文最大风险：潜在接触区和正则化参数仍需人为选择，且缺少与经典接触算法的大规模公平比较。

三个可迁移动作：
1. 写计算方法时同时交代物理思想、弱式和离散矩阵。
2. 用参数表和 gap/成本对比证明新正则化确实有效。
3. 用由简单到复杂的 benchmark ladder 展示适用范围，而不是只给应用图。
