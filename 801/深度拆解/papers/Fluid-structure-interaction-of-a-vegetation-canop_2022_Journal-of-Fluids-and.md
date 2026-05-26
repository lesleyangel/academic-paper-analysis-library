# Fluid-structure interaction of a vegetation canopy in the mixing layer

## 0. 读取说明

本拆解基于 `801/文本/txt/Fluid-structure-interaction-of-a-vegetation-canop_2022_Journal-of-Fluids-and.txt` 的全文抽取。文本抽取包含正文、公式、图题和结论，但不包含可直接判读的图像细节；涉及涡结构形态、颜色区域、参数图边界等视觉判断时，均按文本描述分析，细节标注“需要 PDF 图像复核”。

## 1. 基本信息与论文身份

- 题名：Fluid-structure interaction of a vegetation canopy in the mixing layer。
- 作者：Zhe Fang、Chunlin Gong、Alistair Revell、Joseph O'Connor。
- 期刊：Journal of Fluids and Structures，109，2022，103467。
- 领域：植被冠层流、流固耦合、混合层不稳定性、柔性结构动力学。
- 论文类型：数值模拟 + 机理解释型论文。
- 研究对象：浅淹没植被冠层与冠层顶部混合层之间的双向流固耦合。
- 主要方法：LBM 求解流场，非线性 FEM 求解植被梁变形，IBM 处理流固界面，强耦合 block Gauss-Seidel 隐式迭代稳定耦合。
- 核心变量：弯曲刚度 K、冠层密度 Phi、响应频率、KH 不稳定频率、自然频率、阻力系数、植被尖端偏转角。
- 目标读者：流固耦合数值模拟研究者、植被冠层流研究者、流动控制/生态流体力学读者。

## 2. 摘要与核心信息提取

论文的核心主张是：植被冠层的动态响应不是单纯由 KH 混合层不稳定性决定，也不是单纯由植被固有频率决定，而是由冠层密度、弯曲刚度、混合层强度和结构自然频率共同耦合产生；在 KH 频率与结构自然频率交叉区域会出现 lock-in，表现为混合层对植被摆动频率的“吸引”。

摘要里的信息压缩方式很典型：先说现象，即 submerged vegetation canopy 的 waving motion 与冠层顶部 coherent vortices 相关；再制造不足，即此前多用显著建模假设简化系统，混合层与冠层的双向影响仍 underexplored；再给方法，即 fully coupled fluid-structure modeling；然后给结果分类，即 static、flapping、dual、regular waving、irregular waving 五种状态；最后给频率机制，即 lock-in 出现在混合层不稳定频率与植被自然频率 crossover region。

## 3. 选题层深拆

选题来自两个交叉需求：一是生态/工程问题，植被冠层通过流固相互作用影响沉积物输运、作物损伤、空气/水质和栖息地；二是流体力学问题，冠层顶部速度剖面的拐点会诱发类似 mixing layer 的 KH 不稳定性，但柔性冠层又会反过来改变流场。

作者把大问题收束成一个可计算问题：在固定 Re=100、质量比 M=1 的二维浅淹没冠层中，系统改变弯曲刚度和冠层密度，观察行为图谱、涡结构、频率关系和 lock-in 机制。这个收束很稳，因为它避免了“真实植被太复杂”的泛化陷阱，把论文变成参数空间中的机理识别。

选题价值主要有三层：理论上解释混合层不稳定性和结构自然频率之间的控制权；方法上展示 fully coupled FSI 在冠层流中的作用；应用上把 flapping 状态中的垂向输运与沙化/风蚀联系起来，并提出混种不同刚度植被保护脆弱作物的初步策略。

## 4. 领域位置与文献版图

文献版图被组织成三条线。第一条是植被冠层流与 mixing layer 类比：Ghisalberti、Nepf、Raupach 等工作说明冠层顶部阻力不连续导致速度剖面拐点和 KH 不稳定。第二条是植被动力学：Finnigan、Py 等实验指出摆动频率接近植被自然频率，从而挑战“完全由 KH 控制”的解释。第三条是数值建模：早期连续冠层/刚体植被/分段线性速度剖面模型简化较多，近年的 O'Connor、Revell、Zhang 等 fully coupled FSI 模型更能解析单根植被柔性动力学。

本文的站位是“继承 mixing layer 模型，但修正其单向解释”。作者没有否定 KH 不稳定，而是把 KH 频率、真空/流体自然频率、实际摆动频率同时放进比较框架中，试图解释前人结论为什么不一致。

## 5. Gap 制造机制

作者制造 gap 的方式不是简单说“没人研究”，而是说已有研究的结论彼此冲突：有的认为 canopy waving 由 KH instability dominated，有的发现主频接近 free-vibration frequency，还有的 lock-in 解释依赖不同 KH 频率定义。冲突的根源又被追溯到模型假设差异：简化流场、连续冠层、刚体植被、少量 flap 等都可能改变频率关系。

真实 gap 是：缺少一个 fully coupled、能同时改变弯曲刚度和冠层密度、并把涡结构与频率响应连起来的参数化研究。这个 gap 是成立的，因为论文后文确实用行为图谱、涡结构、速度梯度、KH 频率估计和自然频率比较逐层回应。

风险在于：二维、Re=100、无重力/浮力/接触模型使 gap 的“真实植被适用性”被削弱；作者在讨论中承认了这些边界。

## 6. 创新性判断

作者声明的创新包括：使用直接流固耦合模型研究冠层与混合层相互作用；在弯曲刚度和冠层密度空间中识别五种行为状态；解释涡结构如何随状态改变；观察 lock-in，并将其解释为混合层对植被频率的吸引效应。

真实创新强度属于中高。方法本身是已有 LBM-IBM-FEM 框架的应用和组合，不是全新数值方法；但问题拆解和证据组织有新意，特别是把行为模式、涡中心位置、剪切载荷、KH 频率、自然频率放入一条机制链。

最可能被挑战的是“lock-in 机制解释”和“沙化/作物保护应用延伸”。前者依赖后验频率估计和二维模拟；后者从无颗粒、无重力/浮力模型外推到 sediment/sandification，启发性强但证据链偏间接。

## 7. 论证链条复原

论证链条如下：

1. 植被冠层流具有速度剖面拐点，可能产生 KH 型 mixing layer instability。
2. 柔性植被并非被动响应，植被自然频率和运动会反过来影响流场。
3. 既有研究对主导频率和 lock-in 的解释不一致，原因之一是模型简化不同。
4. 因此需要 fully coupled FSI 模型，在参数空间中同时考察弯曲刚度和冠层密度。
5. LBM-IBM-FEM 强耦合模型给出五种行为状态，并显示状态边界依赖 K 与 Phi。
6. 涡结构比较解释行为转换：涡中心低于植被尖端时产生 mode-two flapping；涡中心上移后转为 mode-one waving；生产/耗散失衡导致 irregular waving。
7. 冠层密度改变速度剖面拐点与速度梯度，从而改变混合层强度和不稳定性起始位置。
8. 频率比较显示 waving branch 近似一阶自然频率，flapping branch 近似二阶自然频率，KH 频率在交叉区吸引实际频率形成 lock-in。
9. 结论回扣开头：动态行为由混合层和结构属性耦合控制，而非单一机制。

薄弱环节是第 8 步：KH 频率由速度剖面和动量厚度估计，实际 lock-in 的因果证据还需要更多控制实验或 3D 验证。

## 8. 方法/理论/模型细拆

模型由三部分组成。流场用 LBM-BGK 方程和 Guo forcing term，优势是规则网格、高并行性、适合与 IBM 耦合。结构用非线性 FEM，把每根植被离散为 Euler-Bernoulli 梁，用 Newmark-beta 与 Newton-Raphson 求解大变形动力学。界面用 IBM，在 Eulerian 流体点和 Lagrangian 结构标记点之间通过插值和 spreading 交换速度与力。

耦合策略是方法可信度的关键。作者指出低结构/流体密度比下显式 partitioned 方法会有界面边界条件 mismatch，因此加入强耦合 block Gauss-Seidel 隐式子迭代，并用 Aitken relaxation 动态调整松弛因子。这给“fully coupled”的说法提供了数值稳定性支撑。

参数设置上，通道高 H=3h，冠层长 Lc=64h，总长 Lt=104h，入口为无拐点抛物线速度剖面，用于观察混合层如何由冠层产生而不是入口预置。Re=100，M=1.0，K 取 12 个数量级分布值，Phi 取 0 到 0.1。每根植被 50 个 IBM markers、20 个 FEM elements，并附录做网格独立性。

方法边界：二维、浅淹没、无植被接触、无重力/浮力、固定 Re 和 M。作者用讨论小节主动限定这些条件，降低过度外推风险。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 冠层行为可分为 static、flapping、dual、regular waving、irregular waving 五类 | 4.1 | Fig. 3 快照、Fig. 4 参数图谱 | 强 | 状态分类依赖视觉判读，需要 PDF 图像复核 |
| 行为模式受弯曲刚度和冠层密度共同控制 | 4.1 | K0-K11 与 Phi0-Phi10 参数图，动态区集中在中间参数范围 | 强 | 参数范围固定于 Re=100、M=1 |
| flapping 中涡中心低于植被尖端，导致强剪切和 mode-two deformation | 4.2 | Fig. 5b 流线/竖向速度，Fig. 6 阻力系数，文字描述涡旋穿透冠层 | 中强 | 涡中心位置需 PDF 图像复核 |
| waving 中涡旋上移，植被由 mode-two 转为 mode-one | 4.2 | Fig. 5c-5e 与 Fig. 6，作者比较涡旋尺度和阻力幅值 | 中强 | mode 判别依赖形态图 |
| 冠层密度增加会降低冠层内外垂向交换、提高顶部速度梯度并提前 KH 不稳定起始 | 4.3 | Fig. 9-11，速度剖面和 ∂ux/∂y 随密度变化 | 强 | 速度剖面来自单一 x=26 静态区域 |
| 动态响应频率由结构自然频率主导，但受混合层 KH 频率吸引 | 4.4 | Fig. 12-14，一阶/二阶自然频率、KH 频率、实际频率平台 | 中强 | lock-in 因果性主要由相关趋势支持 |
| flapping 中存在冠层到混合层的自发垂向输运，可能关联沙化 | 4.2/结论 | Fig. 5b 中诱导涡上移描述 | 中 | 无颗粒输运、重力/浮力模型，应用外推较强 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核备注 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 建立冠层速度剖面、混合层与 wavelike motion 的概念图 | 冠层顶部混合层驱动 monami/honami | 视觉化“速度拐点-涡-波动”链条 | 需要 PDF 图像复核 |
| Eq. 1-7 | 给出 LBM 流场控制与 forcing | 方法可解析受力流场 | 外力项进入动量更新 | 文本可确认 |
| Eq. 8-10 | 给出植被梁动力学与 Newmark 求解 | 单根植被柔性动力学被解析 | 内力、外力、质量矩阵闭合 | 文本可确认 |
| Eq. 11-16 | IBM 插值/扩散与界面力计算 | 流固界面数据交换 | Eulerian-Lagrangian 两套网格耦合 | 文本可确认 |
| Fig. 3-4 | 行为分类和参数图谱 | 五种行为状态 | dynamic/static 区域随 K、Phi 成带状分布 | 需要 PDF 图像复核 |
| Fig. 5-7 | 用涡结构、阻力和偏转角解释 flapping/waving | 涡中心位置决定变形模态 | flapping 有冠层穿透与 mode-two，应力更强 | 需要 PDF 图像复核 |
| Fig. 9-11 | 解释冠层密度对混合层起始的作用 | 密度调节速度梯度和不稳定性 | inflection point 上移，速度梯度峰值增大 | 需要 PDF 图像复核 |
| Eq. 25-28 | 估计自然频率和 KH 频率 | 频率竞争/lock-in | KH 与自然频率交叉区出现 plateau | 文本可确认 |
| Fig. 12-14 | 频率证据核心 | mixing layer 对频率有 attraction effect | waving branch 近一阶，flapping branch 近二阶 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

真实章节顺序是：Introduction -> Mathematical model -> Numerical settings and parameter space -> Results and discussion -> Conclusions。结构不是严格 IMRaD，而是“模型方法 + 参数空间 + 机理结果”型。

Introduction 先铺生态和冠层流背景，再引出 KH 不稳定与自然频率冲突，最后说明模型选择。Method 章节按 LBM、FEM、IBM、coupling 分模块展开，服务于“fully coupled”可信度。Numerical settings 把物理问题转为可扫参数的计算设计。Results 章节内部节奏清楚：先分类，再解释涡结构，再讨论冠层密度，再讨论 lock-in，最后讨论其他参数边界。Conclusion 三段回收：行为/涡结构、密度机制、频率机制，并附未来工作。

标题命名偏好是描述型，几乎每个小节直接暴露变量或机制，如 “The influence of canopy density on mixing layer instability” 和 “Lock in effect”。这种命名适合工程/流体期刊，因为读者能快速定位变量-现象关系。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `801/文本/txt/Fluid-structure-interaction-of-a-vegetation-canop_2022_Journal-of-Fluids-and.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：13
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 机制/讨论型, 结果/验证型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Mathematical model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Lattice Boltzmann method | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Finite element method | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3 Immersed boundary method | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Numerical settings and parameter space | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 4 Results and discussion | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 4.1 Dynamic behaviors of vegetation canopy | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.2 Vortical structures in different vegetation behaviors | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.3 The influence of canopy density on mixing layer instability | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 高 | 是 | 保留具体变量/对象 |
| 4.4 Lock in effect | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.5 Discussion on the effects of other parameters | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 高 | 是 | 保留具体变量/对象 |
| 5 Conclusions | 结论/展望型 | 收束贡献、边界和未来工作 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 的段落节奏是：生态功能 -> 冠层顶部混合层 -> 频率争议 -> 模型争议 -> 本文方案。每段末尾都有自然转折，通常用 “However” 或 “Considering” 把已有认识推向不足。

Results 的段落多采用“图示观察 -> 物理解释 -> 参数含义 -> 应用/机制外推”。例如 flapping 段先读 Fig. 5b，再解释涡旋穿透和剪切力，再联系 Fig. 6/7 的阻力与偏转，最后提出垂向输运和沙化启发。

Discussion on other parameters 的功能是控边界。作者没有把二维低 Re 结果硬推到真实冠层，而是分别讨论 Re、M、gravity/buoyancy、2D approximation，属于主动防审稿风险的段落。

## 13. 文笔画像与语言习惯

整体语气偏机制解释型，claim 强度中等偏强。作者喜欢用 “it can be seen/observed/indicated” 从图表引出结论，再用 “as a result/therefore/while” 给出因果链。强动词包括 investigate、explore、indicate、demonstrate、reveal、suppress、enhance、attract。

时态上，Introduction 综述用现在完成时和一般过去时；方法用一般现在时；结果读图常用一般现在时和被动结构；结论用一般现在时回收贡献。被动语态较多，如 “is solved by”、“is handled by”、“is observed”，但在机制解释处也会用主动结构，如 “the mixing layer acts to attract”。

形容词/副词习惯：coherent、dynamic、regular、irregular、representative、dominant、noticeable、spontaneous、gradually、slightly、significantly。作者会用 hedging 控制外推，如 “is expected to”、“may carry”、“one possible compromise”。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：vegetation(272)；canopy(212)；layer(124)；mixing(123)；flow(92)；waving(91)；frequency(91)；instability(70)；behavior(58)；density(58)；velocity(57)；fluid(56)；bending(51)；vortices(49)；natural(49)；frequencies(48)；rigidity(46)；flapping(46)；revell(40)；present(38)
- 高频学术名词：vegetation(272)；instability(140)；structure(62)；behavior(58)；density(58)；velocity(57)；rigidity(46)；structures(32)；motion(31)；deflection(26)；element(26)；model(25)；mechanism(24)；intensity(24)；influence(18)；section(18)
- 高频学术动词：shown(17)；investigated(15)；indicates(8)；compared(7)；investigate(7)；estimated(6)；predicted(6)；demonstrated(6)；solved(5)；shows(4)；proposed(4)；show(3)；demonstrate(2)；capture(2)；reveal(1)；simulate(1)
- 高频形容词：dynamic(66)；natural(49)；static(42)；present(38)；coherent(37)；different(31)；vertical(27)；element(26)；coefficient(26)；dual(23)；small(17)；boundary(15)；previous(13)；aquatic(12)；terrestrial(11)；dominant(10)
- 高频副词/连接副词：however(15)；respectively(10)；gradually(10)；generally(8)；slightly(8)；therefore(7)；finally(6)；relatively(5)；fully(5)；clearly(5)；significantly(4)；approximately(4)；numerically(4)；widely(4)；highly(4)；rapidly(4)
- 高频二词短语：mixing layer(121)；vegetation canopy(49)；bending rigidity(43)；canopy density(43)；layer instability(40)；natural frequency(38)；coherent vortices(35)；drag coefficient(25)；fluids structures(23)；fang gong(21)；gong revell(21)；revell fluids(21)；fluid structure(18)；vegetation element(18)；irregular waving(17)；frequency vegetation(17)
- 高频三词短语：mixing layer instability(40)；fang gong revell(21)；gong revell fluids(21)；revell fluids structures(21)；intensity mixing layer(14)；mean drag coefficient(11)；bending rigidity canopy(10)；vacuum natural frequency(10)；rigidity canopy density(9)；amplitude drag coefficient(9)；regular waving irregular(8)；waving irregular waving(8)

**主动、被动与句法**

- 被动语态估计次数：245
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：1487
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：396
- 一般过去时线索：116
- 现在完成时线索：21
- 情态动词线索：74
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：vegetation(9)；mixing(9)；layer(9)；canopy(7)；interaction(4)；waving(4)；flow(4)；structures(3)
- 1. Introduction：canopy(31)；vegetation(23)；flow(19)；frequency(18)；fluid(15)；model(14)；structure(11)；waving(11)
- 2. Mathematical model：无明显高频项
- 2.1. Lattice Boltzmann method：fluid(12)；time(4)；velocity(4)；force(4)；represents(4)；given(3)；particles(3)；distribution(3)
- 2.2. Finite element method：vegetation(8)；method(6)；ext(5)；represents(5)；element(4)；discretized(3)；written(3)；matrix(3)
- 2.3. Immersed boundary method：structure(11)；fluid(9)；coupling(6)；boundary(5)；lagrangian(5)；interface(4)；given(4)；density(4)
- 3. Numerical settings and parameter space：vegetation(31)；canopy(12)；channel(8)；density(8)；velocity(7)；given(5)；present(5)；values(5)
- 4. Results and discussion：无明显高频项

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

- 背景句式：X are abundant in nature and play an important role in... 可复用为“对象广泛存在 + 功能重要”开场。
- Gap 句式：The interaction between X, as well as its influence on Y, remain relatively underexplored. 适合双向耦合类 gap。
- 冲突句式：This finding conflicted with the X model in which... 用于制造理论张力。
- 方法句式：A fully coupled fluid-structure modeling approach is used to investigate... 适合方法-问题直接对应。
- 结果句式：The behavior can be classified into five modes... 适合参数扫描后的分类贡献。
- 机制句式：This can be attributed to... / As a result... / On the one hand... on the other hand... 适合多因素竞争机制。
- 边界句式：Although further insight is obtained, several areas remain for further investigation. 适合结尾收束。

可复用关键词组：mixing layer instability、coherent vortices、bending rigidity、canopy density、dynamic response、lock-in effect、natural frequency、momentum thickness、vertical transport、parameter map。

## 15. 引用策略与文献使用

引用策略是“综述背景 + 对立结论 + 模型选择背书”。生态功能引用用于证明问题重要；Ghisalberti/Nepf/Raupach 用于建立 mixing layer/KH 传统解释；Finnigan/Py/Gosselin/O'Connor/Zhang 用于建立频率解释冲突；LBM/IBM/FEM 相关文献用于证明数值框架可靠。

作者对前人态度比较克制：不是直接批判，而是说 simplified assumptions、differing conclusions、different modeling approaches。这样既保留前人贡献，又为 fully coupled 模型腾出必要性。

引用的 gap 制造方式很值得学：先展示 A 类文献认为 KH 控制，再展示 B 类文献认为自然频率重要，再说两类文献模型不同，所以本文要用更完整耦合模型统一解释。

## 16. 审稿人视角风险

1. 二维模型对真实冠层的外推有限，尤其在高 Re 下三维涡、横向 coherent vortices、kinking/pairing 可能改变结论。
2. Re=100 接近作者前作中能出现 waving instability 的低限，不代表自然水生/陆生冠层的典型范围。
3. lock-in 的“attraction effect”主要来自频率曲线对比，缺少更直接的因果干预，例如固定结构频率或人工改变速度剖面。
4. flapping 与沙化/风蚀联系没有颗粒输运模型支持，属于应用假说。
5. 混种不同刚度作物保护策略只做一个 preliminary test，缺少间距、比例、成本和真实植物参数敏感性。
6. 植被接触、碰撞、重力/浮力和三维渗透性均未进入主模型，可能影响高密度/大偏转区域。
7. 网格独立性有附录，但状态分类边界对数值分辨率和时间长度的敏感性仍需复核。

## 17. 可复用资产

- 选题套路：从“前人结论冲突”而不是“空白”切入，显得 gap 更真实。
- 参数图谱资产：用二维参数空间把复杂行为分类，是机制论文非常强的证据组织方式。
- 图表链条：行为快照 -> 参数 map -> 力/偏转量化 -> 速度剖面 -> 频率图，层层从现象推到机制。
- 讨论边界资产：单独设置 “effects of other parameters” 小节，主动处理 Re、mass ratio、gravity、2D approximation。
- 写法资产：每个结果小节都用“物理观察 + 量化指标 + 机制解释 + 更大意义”的节奏。

## 18. 对我写论文的启发

如果自己的研究也有“模型解释不一致”的领域，可以模仿本文：不要只宣称方法更复杂，而要说明复杂模型能解决哪个解释冲突。最值得迁移的是参数空间图和频率对照图：一个负责分类，一个负责机制。

另一个启发是，应用外推可以写，但要放在机制证据之后，并用谨慎措辞。本文把沙化和作物保护作为“indicates/inspired by/preliminary”的层级，而不是把它包装成已完成工程方案。

## 19. 最终浓缩

这篇论文的核心价值在于把植被冠层 waving/flapping 从单一 KH 不稳定解释推进到“混合层-结构属性耦合控制”解释。它最值得学习的是：用 fully coupled FSI 模型扫参数空间，用涡结构解释行为类别，用自然频率与 KH 频率比较解释 lock-in。最大风险是二维低 Re 结果和应用外推仍需 PDF 图像与更真实物理模型复核。

<!-- REAUDIT-2026-05-26 START -->

## 20. 复核增强：严格抽取、翻译、引文与句型

> 本区块由 `tools/upgrade_801_deep_analysis.py` 基于 `801/文本/txt/Fluid-structure-interaction-of-a-vegetation-canop_2022_Journal-of-Fluids-and.txt` 与 `801/文本/metadata/Fluid-structure-interaction-of-a-vegetation-canop_2022_Journal-of-Fluids-and.json` 重新抽取生成；用于修正旧报告中章节未全、引文缺失、摘要/结论未完整摘录的问题。双栏 PDF 抽取仍可能存在断行，引用和公式编号以 PDF 版面为最终准绳。

### 20.1 严格章节树（按 PDF/metadata TOC）

- L2 p.1: Introduction （背景/领域定位）
- L2 p.3: Mathematical model （方法/模型）
  - L3 p.3: Lattice Boltzmann method （方法/模型）
  - L3 p.4: Finite element method （方法/模型）
  - L3 p.4: Immersed boundary method （方法/模型）
  - L3 p.5: Fluid–structure#xcoupling （对象/问题/模块）
- L2 p.5: Numerical settings and parameter space （对象/问题/模块）
- L2 p.6: Results and discussion （结果/讨论/验证）
  - L3 p.6: Dynamic behaviors of vegetation canopy （对象/问题/模块）
  - L3 p.8: Vortical structures in different vegetation behaviors （对象/问题/模块）
  - L3 p.12: The influence of canopy density on mixing layer instability （对象/问题/模块）
  - L3 p.15: Lock in effect （对象/问题/模块）
  - L3 p.18: Discussion on the effects of other parameters （结果/讨论/验证）
- L2 p.20: Conclusions （结论）
- L2 p.21: CRediT authorship contribution statement （对象/问题/模块）
- L2 p.21: Declaration of competing interest （对象/问题/模块）
- L2 p.21: Acknowledgments （对象/问题/模块）
- L2 p.21: Appendix. Grid independence test （附录）
- L2 p.22: References （参考文献）

### 20.2 章节名功能分析

| 章节/小节名 | 页码 | 层级 | 类型 | 复核说明 |
| --- | ---: | ---: | --- | --- |
| Introduction | 1 | 2 | 背景/领域定位 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Mathematical model | 3 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Lattice Boltzmann method | 3 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Finite element method | 4 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Immersed boundary method | 4 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Fluid–structure#xcoupling | 5 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Numerical settings and parameter space | 5 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Results and discussion | 6 | 2 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Dynamic behaviors of vegetation canopy | 6 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Vortical structures in different vegetation behaviors | 8 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| The influence of canopy density on mixing layer instability | 12 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Lock in effect | 15 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Discussion on the effects of other parameters | 18 | 3 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Conclusions | 20 | 2 | 结论 | 来自 metadata TOC，正式分析按此章节点名复核 |
| CRediT authorship contribution statement | 21 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Declaration of competing interest | 21 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Acknowledgments | 21 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Appendix. Grid independence test | 21 | 2 | 附录 | 来自 metadata TOC，正式分析按此章节点名复核 |
| References | 22 | 2 | 参考文献 | 来自 metadata TOC，正式分析按此章节点名复核 |

### 20.3 摘要完整摘录（本地证据）

抽取状态：成功

> 公开库不直接展示完整英文摘要原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/Fluid-structure-interaction-of-a-vegetation-canop_2022_Journal-of-Fluids-and.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/Fluid-structure-interaction-of-a-vegetation-canop_2022_Journal-of-Fluids-and.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.4 摘要中文翻译

> 水下植被冠层的波动运动与冠层顶部相干涡流的产生有关，这是混合层不稳定性的表现。混合层上方的不稳定流之间的相互作用及其对植被冠层本身的影响仍然相对未得到充分探索，大多数先前的研究都采用重要的建模假设来简化系统。在本文中，采用完全耦合的流体-结构建模方法来研究植被冠层与其上方出现的混合层之间的相互作用机制。探讨了植被行为对弯曲刚度和冠层密度的依赖性，观察了植被的五种代表性行为状态：静态、扑动、双重、规则波动和不规则波动。比较了在与每个状态相关的混合层中观察到的涡流结构，并研究了冠层密度对混合层发展的影响，特别关注与植被相关的流动特征。此外，在混合层不稳定频率与植被固有频率的交叉区域观察到锁定效应，这表明混合层对植被波动频率的吸引作用。 © 2021 爱思唯尔有限公司
> 
> 版权所有。

### 20.5 结论完整摘录（本地证据）

结论章节识别：Conclusions；状态：独立结论章节

> 公开库不直接展示完整英文结论原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/Fluid-structure-interaction-of-a-vegetation-canop_2022_Journal-of-Fluids-and.json` 的 `conclusion` 字段，以及 `801/深度拆解/local_full_reports/Fluid-structure-interaction-of-a-vegetation-canop_2022_Journal-of-Fluids-and.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.6 结论中文翻译

> 根据上述研究结果，有必要进一步研究冠层流的锁定效应，确定冠层固有频率、纯/重/耦合KH频率和波动频率之间的关系。此外，值得注意的是，上述研究结论的差异部分是由于它们使用的建模方法不同所致。在 Py 等人的研究中。 （2006年、2004年）
> 
> Z.Fang、C.Gong、A.Revell 等。流体与结构学报109(2022)103467
> 
> 2 数学模型
> 
> 2.1.格子玻尔兹曼法
> 
> Ωf = 1
> 
> τ ( f (eq) −f )
> 
> 其中 f (eq) 表示分布函数 f 的平衡状态，τ 是与流体运动粘度 υ 相关的弛豫时间参数，它们的关系为：
> 
> ）
> 
> ν = ( τ -1
> 
> cs 是声格速度。经过时间和空间离散化后，方程中的每个流体粒子： (1) 分配有限个离散速度值，用下标α表示，则相应的平衡分布函数f(eq)可写为：
> 
> c2 s + (eα · v)2
> 
> 1 + eα · v
> 
> 2c4 s −v2
> 
> [
> 
> ]
> 
> f (eq) α = ρwα
> 
> 2c2秒
> 
> 式中外强迫项F的离散化形式(1) 是由Guo等人提出的。
> 
> (2002)，其中外力对流体动量和动量通量都有影响，其表达式可写为：
> 
> [ eα -v
> 
> c2 s + eα · v
> 
> Fα = (
> 
> ) wα
> 
> 1 −1
> 
> c4 s eα
> 
> 2τ
> 
> Gosselin 和 Langre (2009) 简化了流体和结构求解器，其中流动的速度剖面被视为分段线性，整个植被冠层被视为连续体，并且假设每个植被元素是刚性的。而 O’Connor 和 Revell (2019) 以及Zhang 等人。 （2020）使用了完全耦合的流体结构模型，其中单个植被是灵活的并且它们的动力学得到了完全解决。相对而言，O’Connor 和 Revell (2019) 以及Zhang 等人使用的流体-结构模型。 (2020)更适用，更能反映植被冠层的真实行为。本文采用O'Connor和Revell（2019）中使用的二维（2-D）流固模型，其中流体场采用格子玻尔兹曼法（LBM）求解，植被动态运动采用有限元法（FEM）计算，流体与植被之间的相互作用采用浸入边界法（IBM）处理。此外，该模型还引入了强耦合隐式方案，以提高算法的稳定性和准确性。
> 
> 近年来，现有的流固模型已广泛应用于许多FSI模拟中，例如柔性颗粒悬浮（Krüger等，2011）、被动流动控制（Fang等，2019）、能量收集（Dong等，2016）、弹性层振荡（De Rosis等，2014a）和扑翼飞行研究（De Rosis等，2014）等。 2014b）。这些研究也证明了本模型的准确性和可靠性，主要从以下三个方面：首先，本模型中使用的LBM因其简单的公式、高效率和高水平的并行性而被证明是纳维-斯托克斯（N-S）求解器的可行替代品（Shan等人，2006）。其次，IBM中的流体网格不需要符合结构边界，因此本模型中的网格生成比传统的任意拉格朗日欧拉（ALE）方法（Peskin，2002）快得多，并且在固定规则流体网格上非常有效地求解流动控制方程。第三，本模型中的有限元法具有很强的处理复杂结构非线性变形的能力，因此具有广泛的适用性（Felippa and Haugen，2005）。由于上述两个优点，当前的流固模型特别适合解决高变形结构的流固耦合问题。
> 
> 本文研究了雷诺数100下不同弯曲刚度和冠层密度的浅水植被冠层的动态响应，研究了混合层中的详细涡流结构及其对植被行为的影响。还探讨了混合层不稳定频率与植被固有频率之间的锁定效应。在本文的其余部分中，简要描述了流固耦合的数学模型，然后介绍了案例设置和相关参数空间。最后对结果和主要发现进行分析并得出结论。本文中的流场通过格子玻尔兹曼方程求解（Chen and Doolen，1998），给出为：
> 
> ∂f ∂t + e·∇xf + F·∇ef = Ωf (1)
> 
> 其中 t 是时间，x 和 e 是流体粒子在时间 t 时的位置和速度。 f是流体粒子的分布函数，力项F表示施加到流体上的外力。
> 
> Ωf 表示流体粒子的碰撞算子，可以使用 Bhatnagar、Gross 和 Krook (BGK) 方法进行简化 (Bhatnagar et al., 1954)，Ωf 的表达式为
> 
> (2)
> 
> c2 s (3)
> 
> (4)
> 
> 其中ρ为流体密度，eα和wα分别表示流体粒子上的离散速度和相应的权系数。 v 是宏观流体速度。 ]·f (5)
> 
> Z.Fang、C.Gong、A.Revell 等。流体与结构学报109(2022)103467
> 
> 其中 f 表示作用在流体上的力密度。则宏观流体量可由下式获得：
> 
> ρ = Σ
> 
> α eαfα + 1
> 
> 2 fδt = ρv*+ 1
> 
> ρv = Σ
> 
> 这里 v* 称为预测速度。 2.2.有限元法
> 
> 其中M是植被的质量矩阵，U和¡U分别是植被位移和加速度。 F int 表示植被的内力，F ext 表示作用于植被的外力。根据牛顿第三定律，F ext 的表达式可以写为：
> 
> ∫
> 
> F ext = − Σ
> 
> 米
> 
> [ K i T,t+Δt + c0M] ΔU i+1 = F ext,t+Δt −F i int,t+Δt −M [ c0 ( U i t+Δt −U t ) −c1 ˙U t −c2 ¡U t ]
> 
> 2.3.浸入边界法
> 
> Φ(X) = Π[Φ(x)] = Σ
> 
> φ(x) = Ψ [Φ(X)] = Σ
> 
> 代入等式。将（13）和（14）代入等式。 (7) 并转换方程。
> 
> (7) 代入拉格朗日坐标系为：
> 
> Π[ρ(x, t)]V(X, t) = Π [ ρv*(x, t)] + Δt
> 
> α fα (6)
> 
> 2 fδt (7)
> 
> 个体植被的动态通过非线性有限元方法计算，其中每个植被单元由一系列两节点欧拉-伯努利梁单元离散化。植被动态方程可写为：
> 
> M ¡U (t) + F int (U) −F ext (t) = 0 (8)
> 
> VmNT f′dV (9)
> 
> 其中 Vm 是第 m 个梁单元的体积。 N表示形函数矩阵，f'表示作用在单元上的力密度，其表达式见2.3节。等式。 (8)可以对时间进行离散化，并使用Newmark-β方法和Newton-Raphson方法进行求解，因此其离散形式可以写为：
> 
> (10)
> 
> 式中，Δt 为 Newmark-β 法中的时间步长，i 为 Newton-Raphson 法中的迭代步长，K T 为植被切线刚度矩阵，c0 ∼c2 为根据 Newmark-β 法精度和稳定性要求确定的变量。有关方程式的更多详细信息。 (10) 可以在 Doyle 和 Desantiago (2001) 中找到。流与植被之间的界面数据交换采用浸没边界法处理，其中流体场由一组固定欧拉点离散化，而植被由多个拉格朗日标记离散化。
> 
> 这两个网格之间的数据交换由两个算子实现：插值算子 Π 和扩展算子 Ψ ，它们的表达式为：
> 
> Ω φ(x)～δ(x −X)ΔxΔyΔz (11)
> 
> Λ Φ(X)~δ(x −X)ϵΔqΔrΔs (12)
> 
> 其中 φ 和 Φ 分别是欧拉框架和拉格朗日框架中定义的量。 x = (x, y, z) 是欧拉点的位置，而 X = (q, r, s) 是拉格朗日标记的位置。 Ω代表计算域，而Г代表结构边界。 ϵ 是 Π 和 Ψ 之间互易的比例因子。 ~δ 是 Peskin (2002) 中定义的三点离散狄拉克 δ 函数。正如李等人所描述的。 (2016)，LBM 中获得的笛卡尔网格点 x 处的流体速度 v 可以插值到坐标 X 的拉格朗日标记位置上，如下所示：
> 
> v(X,t) = Π(v(x,t)) (13)
> 
> 根据非滑移边界条件，该插值速度必须等于 FEM 中计算的边界速度 V (X, t)，如下所示：
> 
> V(X, t) = v(X, t) (14)
> 
> 2 f′(X, t) (15)
> 
> Z.Fang、C.Gong、A.Revell 等。流体与结构学报109(2022)103467
> 
> f (x, t) = Ψ [ f ′ (X, t) ]
> 
> 最后，将得到的力密度f(x,t)带回式(1)中。 (7)更新流场。 2.4.
> 
> 流固耦合
> 
> 其中，ω 为松弛因子，U 为有限元法计算的结构位移，~U 和~U k−1 分别表示当前迭代和上一次迭代中结构的松弛位移。 ωk = −ωk−1 ( rk−1)T ( rk −rk−1)
> 
> 其中 rk 是残差向量，由下式给出
> 
> 目前的流固模型已经在我们之前的研究中得到了彻底的验证和使用（O’Connor和Revell，2019；Favier等，2017；Harwood等，2018），读者可以参考这些研究以了解更多详细信息。 3.数值设置和参数空间
> 
> 通道入口处的速度具有抛物线轮廓，由下式给出
> 
> u(0, y) = 1.5uy(2H −y)
> 
> 求解方程。 (15) 得到校正力密度f′，然后通过扩散算子Ψ将其变换到流体网格中为：
> 
> (16)
> 
> 本模型中流体和结构的耦合是通过分区方法处理的，其中流动和结构被顺序求解，并且流固界面处必要的界面数据在这两个求解器之间交换。然而，对于结构与流体密度比较低的问题，这种耦合策略可能会导致流体-结构界面处的边界条件不匹配，从而对解决方案的稳定性和准确性产生不利影响。关于这个问题的理论分析可以参见Zheng等人的论文。 （2010）。
> 
> 为了克服这个问题，本工作引入了强耦合块高斯-塞德尔隐式方案。在此耦合方案中，流体和结构求解器在单个时间步内迭代多次，直到满足界面兼容性条件。在每次内部迭代中，结构的位移基于前一次迭代进行松弛，由下式给出
> 
> ～U = ωU + (1 − ω) ～U k−1 (17)
> 
> 这里采用Aitken的Δ2松弛方法（Kuttler and Wall，2008）来加快上述耦合方案的收敛速度，其中松弛因子ω通过以下方式动态计算：
> 
> ⏐⏐rk−rk−1⏐⏐2 (18)
> 
> rk = U k −~U k−1 (19)
> 
> 通常，较低的结构与流体密度比需要更多的子迭代以确保耦合的收敛。尽管这种隐式子迭代方案增加了计算成本，但目前的FSI模拟框架比其他传统的显式方法具有更高的数值稳定性和算法鲁棒性。如图2所示，植被冠层高度为h，嵌入高度H=3h的矩形明渠中。冠层中的每个植被元素直立且具有相等的间距 ΔS。整个顶篷放置在通道的所谓顶篷部分中，固定长度为 Lc = 64h。
> 
> 为了限制通道边界对冠层行为的干扰，冠层部分距通道入口10h，距通道出口30h，因此通道总长度Lt=104h。水平2 (20)
> 
> 其中 u 是平均流速，而 1.5u 是最大流速。与 Py 等人使用的分段线速度剖面相比。 (2006) 以及 Gosselin 和 Langre (2009) 本身有一个拐点，即当前速度
> 
> Z.Fang、C.Gong、A.Revell 等。流体与结构学报109(2022)103467
> 
> j 0 0.25 0.5 0.75 1 2 3 4 5 6 7 8 9 10
> 
> 植被的材料特性由无量纲质量比 M 和弯曲刚度 K 描述，由下式给出：
> 
> M = ρsb
> 
> ρf h, K = EI
> 
> 其中 ΔS 是植被元素之间的间距。在本文中，空间密度的值选自 0 到 0.1，由下式给出：
> 
> 4 结果与讨论
> 
> 4.1. Dynamic behaviors of vegetation canopy
> 
> n 1 9 17 25 33 65 97 129 161 193 225 257 289 321
> 
> 这里使用的剖面没有拐点，只是用来模拟明渠水流。 This allows us to capture the detailed development process of the mixing layer instability.
> 
> 此外，入口速度设置为在短时间内从零开始非线性增加，然后保持恒定，这用于抑制LBM弱压缩性产生的密度波。通道出口设置固定压力边界条件，而通道的底部和顶部边界分别施加非滑移和自由滑移条件。根据平均入口速度和植被高度，当前流动条件组的雷诺数为 100。 ρf u2h3 (21)
> 
> 其中ρf和ρs分别为流体和植被密度，b代表植被厚度，E和I分别为植被杨氏模量和二阶面积矩。正如 O’Connor 和 Revell (2019) 中所述，植被无量纲质量比 M 的典型值范围从水生植被的 O(0.01) 到陆地植被的 O(10)。即便如此，水生和陆地植被的波动不稳定性的主要特征是相似的（Gosselin 和 Langre，2009）。由于植被质量比不是我们研究的重点，本文选取典型值M=1.0。
> 
> 物理上，M = 1.0 对应陆地植被冠层，其中空气密度为 ρf = 1.29 kg/m3，植被密度为 ρs = 64.5 kg/m3（非常接近 Ebeling 和 Jenkins，1985 年报道的麦秆密度 ρs = 65.0 kg/m3），植被高度为 h = 0.3 m，植被厚度为 b = 0.006米。植被的无因次弯曲刚度 K 对于水生植被测量为 O(0.01)，对于陆地植被测量为 O(0.1)。为了覆盖控制水生和陆地植被行为的大部分参数空间，在以下测试中测试了 12 个不同的 K 值（K0 ∼K11），这些值按 10 次方分布为
> 
> Ki = 5 × 10−3+(2(i−1)/9), i = 0 ∼11 (22)
> 
> 除了个体植被的材料特性外，植被冠层的空间密度也是需要研究的重要参数。一般来说，冠层密度由植被占据的固体体积分数来描述，对于二维情况，其表达式为：
> 
> Φ = b/ΔS (23)
> 
> Φj = j × 10−2, j = 0 ∼ 10 (24)
> 
> 初步测试表明，上述 Φ 范围足以得出各种真实水生植物的典型固体体积分数（Chandler 等，1996）。
> 
> 在我们的模型中，冠层中存在的植被元素数量通过 n = Lc/ΔS + 1 = LcΦ/b + 1 获得。这里 Φ = 0（或 j = 0）代表单个植被元素的情况，用于提供与较大冠层结果进行比较的基准。方程中 j 的值集。 (24) 列于表 1 中。在上述情况下，每个植被元素均使用 50 个 IBM 标记/格点 (Δx = 0.02h) 和 20 个 FEM 元素进行离散化。为了保证FSI模拟的结果与网格分辨率无关，进行了网格独立性测试

### 20.7 论文逻辑脉络复核

- 提出的问题：Vegetation canopies, such as seagrass meadow, crop field and dense forest, are abundant in nature and play an important role in a wide range of ecological services. Secondly, the fluid grid in the IBM does not need to conform to the structure boundary, so the grid generation in the present model becomes much faster than that of the traditional Arbitrary Lagrangian Eulerian (ALE) method (Peskin, 2002), and the flow governing equations are solved very efficiently on the fixed regular fluid grid. At each internal iteration, the displacement of structure is relaxed based on the previous iteration, given by ˜U = ωU + (1 −ω) ˜U k−1 (17) The Aitken’s ∆2 relaxation method (Kuttler and Wall, 2008) is adopted here to speed up the convergence rate of the above coupling scheme, in which the relaxation factor ω is calculated dynamically through: ⏐⏐rk −rk−1⏐⏐2 (18) rk = U k −˜U k−1 (19) Typically, a lower structure-to-fluid density ratio requires more sub-iterations to ensure the convergence of the coupling.
- 旧方法/已有研究不足：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system. The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system. However, for problems with a low structure-to-fluid density ratio, this coupling strategy can lead to a boundary condition mismatch at the fluid–structure interface, which can adversely impact the stability and accuracy of the solution.
- 本文解决方式：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system. In this paper a fully coupled fluid–structure modeling approach is used to investigate the interaction mechanism between the vegetation canopy and the mixing layer that arises above it. The dependence of vegetation behavior on the bending rigidity and canopy density is explored and five representative behavior states of vegetation are observed: static, flapping, dual, regular waving and irregular waving.
- 学术/工程增量：These canopies can provide habitats for wildlife (Carpenter and Lodge, 1986), capture suspended sediment (Palmer et al., 2004), adjust temperature (Karlsson, 2000) and improve water/air quality (Moore, 2004). In addition, a strong-coupling implicit scheme is also introduced in this model in order to improve the stability and accuracy of algorithm. The accuracy and reliability of the present model has also been demonstrated by these studies, mainly from the following three aspects: Firstly, the LBM used in the present model has been proven to be a feasible substitute over a Navier–Stokes (N–S) solver due to its simple formulations, high efficiency and high level of parallelizability (Shan et al., 2006).
- 复核判断：正式阅读时应检查 Introduction 的 gap 是否与 Method 的输入输出、Results 的评价指标和 Conclusion 的 claim 完全闭合；若摘要中的强 claim 没有在结果图表或结论中回收，应在审稿风险中标注。

### 20.8 引文分析补全

- 全文引用簇数量（估计）：0
- Introduction 引用簇数量（估计）：0
- References 条目数（解析）：97
- 可识别年份条目数：54
- 近五年/近年文献（2021+）数量：1
- 经典文献（2010年前）数量：34
- 同刊引用数量（按 subject 粗略匹配）：0
- 高频来源期刊（粗略）：Journal of Fluids and Structures(1)
- 引用簇样例：未识别

带引用的 gap/转折句样例：

- 未在 Introduction 中自动识别到带引用的 gap 句；需人工复核文献转折段。

References 解析样例（前12条）：

- 2012. The wind in the willows: flows in forest canopies in complex terrain. Annu. Rev. Fluid Mech. 44,
479–
- 504. Belcher, S., Jerram, N., Hunt, J.,
- 2003. Adjustment of a turbulent boundary layer to a canopy of roughness elements. J. Fluid Mech. 488, 369–
- 398. Berry, P.M., Sterling, M., Spink, J.H., Baker, C.J., Sylvester-Bradley, R., Money, S.J., Tams, A.R., Ennos, A.R., Sparks, D.L.,
- 2004. Understanding and reducing
lodging in cereals. Adv. Agron. 84, 217–
- 271. Bhatnagar, P.L., Gross, E.P., Krook, M.,
- 1954. A model for collision processes in gases. I. Small amplitude processes in charged and neutral
one-component systems. Phys. Rev. 94 (3), 511–
- 525. Carpenter, S.R., Lodge, D.M.,
- 1986. Effects of submersed macrophytes on ecosystem processes. Aquat. Bot. 26, 341–
- 370. Chandler, M., Colarusso, P., Buchsbaum, R.,
- 1996. A study of eelgrass beds in Boston Harbor and northern Massachusetts bays. In: Proj. Rep. Off. Res.
Dev. US EPA, Narragansett, RI. Chen, S., Doolen, G.D.,
- 1998. Lattice Boltzmann method for fluid flows. Annu. Rev. Fluid Mech. 30, 329–

### 20.9 常用词、词类、语态与时态

- 高频词：vegetation(78)；canopy(56)；fluid(39)；flow(31)；structure(25)；velocity(23)；frequency(21)；density(19)；layer(18)；revell(18)；waving(18)；mixing(16)；where(15)；instability(13)；given(13)；represents(13)；structures(11)；connor(11)；above(11)；lock-in(10)
- 高频名词化/学术名词：vegetation(78)；structure(25)；velocity(23)；density(19)；instability(13)；element(10)；motion(9)；influence(7)；addition(7)；interaction(6)；inflection(6)；function(5)；expression(5)；mechanism(4)；rigidity(4)
- 高频学术动词：indicated(5)；predicted(4)；compared(3)；estimated(1)；demonstrated(1)；presented(1)；validated(1)
- 高频形容词：natural(10)；aquatic(10)；boundary(10)；element(10)；journal(9)；terrestrial(9)；dynamic(7)；flexible(7)；coherent(4)；dual(4)；vertical(4)；material(4)；external(4)；displacement(4)；previous(4)
- 高频副词：respectively(6)；fully(3)；relatively(2)；numerically(2)；finally(2)；experimentally(1)；greatly(1)；synchronously(1)；recently(1)；partly(1)；widely(1)；mainly(1)；firstly(1)；secondly(1)；efficiently(1)
- 高频二词短语：vegetation canopy(17)；fluid structure(16)；mixing layer(15)；connor revell(9)；journal fluids(8)；fluids structures(8)；given where(7)；lock-in effect(6)；canopy density(6)；natural frequency(6)；vegetation canopies(6)；ghisalberti nepf(6)
- 高频三词短语：journal fluids structures(8)；page fang gong(6)；fang gong revell(6)；gong revell journal(6)；revell journal fluids(6)；mixing layer instability(4)；each vegetation element(4)；connor revell zhang(3)；fluids structures fig(3)；waving frequency canopy(3)；natural frequency canopy(3)；fluid structure interaction(2)
- 被动语态估计：76；`we + 动作动词` 主动句估计：0
- 一般现在时线索：126；一般过去时线索：202；现在完成时线索：0；情态动词线索：22

章节词频：

- Abstract: vegetation(8)；mixing(7)；layer(7)；canopy(6)；waving(4)；observed(3)；frequency(3)；associated(2)
- Introduction: canopy(31)；vegetation(21)；flow(18)；frequency(18)；waving(14)；layer(13)；mixing(11)；instability(10)
- Conclusion: vegetation(48)；fluid(33)；structure(20)；canopy(17)；velocity(15)；density(14)；where(13)；represents(13)

### 20.10 句型库扩充（每类多句）

#### 背景句
- 原句/结构：Vegetation canopies, such as seagrass meadow, crop field and dense forest, are abundant in nature and play an important role in a wide range of ecological services.
  可迁移模板：Vegetation canopies, such as seagrass meadow, crop field and dense forest, are abundant in nature and play an important role in a wide range of ecological services.
- 原句/结构：At each internal iteration, the displacement of structure is relaxed based on the previous iteration, given by ˜U = ωU + (1 −ω) ˜U k−1 (17) The Aitken’s ∆2 relaxation method (Kuttler and Wall, 2008) is adopted here to speed up the convergence rate of the above coupling scheme, in which the relaxation factor ω is calculated dynamically through: ⏐⏐rk −rk−1⏐⏐2 (18) rk = U k −˜U k−1 (19) Typically, a lower structure-to-fluid density ratio requires more sub-iterations to ensure the convergence of the coupling.
  可迁移模板：At each internal iteration, the displacement of structure is relaxed based on the previous iteration, given by ˜U = ωU + (X−ω) ˜U k−X(X) The Aitken’s ∆Xrelaxation method (Kuttler and Wall, X) is adopted here to speed up the convergence rate of the above coupling scheme, in which the relaxation factor ω is calculated dynamically through: ⏐⏐rk −rk−X⏐⏐X(X) rk = U k −˜U k−X(X) Typically, a lower structure-to-fluid density ratio requires more sub-iterations to ensure the convergence of the coupling.
- 原句/结构：In order to cover most of the parameter space that governs the behavior of both aquatic and terrestrial vegetation, twelve different values of K (K0 ∼K11) are tested in the following tests, which are distributed in powers of ten as Ki = 5 × 10−3+(2(i−1)/9), i = 0 ∼11 (22) Aside from the material properties of individual vegetation, the spatial density of the vegetation canopy is also an important parameter to be investigated.
  可迁移模板：In order to cover most of the parameter space that governs the behavior of both aquatic and terrestrial vegetation, twelve different values of K (K0 ∼K11) are tested in the following tests, which are distributed in powers of ten as Ki = X× X−X+(X(i−X)/X), i = X∼X(X) Aside from the material properties of individual vegetation, the spatial density of the vegetation canopy is also an important parameter to be investigated.
#### Gap句
- 原句/结构：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system.
  可迁移模板：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system.
- 原句/结构：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system.
  可迁移模板：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system.
- 原句/结构：However, it should be noted that when the vegetation canopy becomes sparse, the prominence of the inflection point in the mean velocity profile is reduced and the above KH instability will not be applicable anymore.
  可迁移模板：However, it should be noted that when the vegetation canopy becomes sparse, the prominence of the inflection point in the mean velocity profile is reduced and the above METHOD instability will not be applicable anymore.
#### 方法句
- 原句/结构：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system.
  可迁移模板：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system.
- 原句/结构：In this paper a fully coupled fluid–structure modeling approach is used to investigate the interaction mechanism between the vegetation canopy and the mixing layer that arises above it.
  可迁移模板：In this paper a fully coupled fluid–structure modeling approach is used to investigate the interaction mechanism between the vegetation canopy and the mixing layer that arises above it.
- 原句/结构：The dependence of vegetation behavior on the bending rigidity and canopy density is explored and five representative behavior states of vegetation are observed: static, flapping, dual, regular waving and irregular waving.
  可迁移模板：The dependence of vegetation behavior on the bending rigidity and canopy density is explored and five representative behavior states of vegetation are observed: static, flapping, dual, regular waving and irregular waving.
#### 结果句
- 原句/结构：In addition, the lock-in effect is observed in the crossover region between the frequency of the mixing layer instability and the natural frequency of the vegetation, which indicates an attraction effect of the mixing layer on the waving frequency of the vegetation. © 2021 Elsevier Ltd.
  可迁移模板：In addition, the lock-in effect is observed in the crossover region between the frequency of the mixing layer instability and the natural frequency of the vegetation, which indicates an attraction effect of the mixing layer on the waving frequency of the vegetation. © XElsevier Ltd.
- 原句/结构：In addition, the lock-in effect is observed in the crossover region between the frequency of the mixing layer instability and the natural frequency of the vegetation, which indicates an attraction effect of the mixing layer on the waving frequency of the vegetation. © 2021 Elsevier Ltd.
  可迁移模板：In addition, the lock-in effect is observed in the crossover region between the frequency of the mixing layer instability and the natural frequency of the vegetation, which indicates an attraction effect of the mixing layer on the waving frequency of the vegetation. © XElsevier Ltd.
- 原句/结构：In addition, such drag discontinuity also results in strong velocity shear at the top of the canopy, making the flow in this region roll up and form the coherent canopyscale vortices which propagate downstream through the canopy (Ghisalberti and Nepf, 2002).
  可迁移模板：In addition, such drag discontinuity also results in strong velocity shear at the top of the canopy, making the flow in this region roll up and form the coherent canopyscale vortices which propagate downstream through the canopy (Ghisalberti and Nepf, X).
#### 贡献句
- 原句/结构：These canopies can provide habitats for wildlife (Carpenter and Lodge, 1986), capture suspended sediment (Palmer et al., 2004), adjust temperature (Karlsson, 2000) and improve water/air quality (Moore, 2004).
  可迁移模板：These canopies can provide habitats for wildlife (Carpenter and Lodge, X), capture suspended sediment (Palmer et al., X), adjust temperature (Karlsson, X) and improve water/air quality (Moore, X).
- 原句/结构：The wavelike motion of vegetation canopy, called honami in terrestrial flow or monami in aquatic flow, provides the striking visualization of such propagations, as shown in Fig. 1.
  可迁移模板：The wavelike motion of vegetation canopy, called honami in terrestrial flow or monami in aquatic flow, provides the striking visualization of such propagations, as shown in Fig. X.
- 原句/结构：Here Φ = 0 (or j = 0) represents the case of a single vegetation element which is used to provide a benchmark for comparison with results for a larger canopy.
  可迁移模板：Here Φ = X(or j = X) represents the case of a single vegetation element which is used to provide a benchmark for comparison with results for a larger canopy.
#### 限制/边界句
- 原句/结构：However, it should be noted that when the vegetation canopy becomes sparse, the prominence of the inflection point in the mean velocity profile is reduced and the above KH instability will not be applicable anymore.
  可迁移模板：However, it should be noted that when the vegetation canopy becomes sparse, the prominence of the inflection point in the mean velocity profile is reduced and the above METHOD instability will not be applicable anymore.
- 原句/结构：This finding conflicted with the mixing layer model in which the main waving frequency of canopy should be dominated by the flow instability, and therefore indicated a noticeable influence of canopy motion on the flow dynamics.
  可迁移模板：This finding conflicted with the mixing layer model in which the main waving frequency of canopy should be dominated by the flow instability, and therefore indicated a noticeable influence of canopy motion on the flow dynamics.
- 原句/结构：Ghisalberti and Nepf (2006) then performed a flume experiment with both rigid and flexible model canopies to study the structure of vegetated shear flow, they found the waving motion of canopy could improve the vertical momentum transport within the canopy and noted that the deflection of the canopy was more than just a passive response to the coherent vortices.
  可迁移模板：Ghisalberti and Nepf (X) then performed a flume experiment with both rigid and flexible model canopies to study the structure of vegetated shear flow, they found the waving motion of canopy could improve the vertical momentum transport within the canopy and noted that the deflection of the canopy was more than just a passive response to the coherent vortices.

### 20.11 抽取失败与人工复核提示

- 摘要抽取：正常
- 结论抽取：正常
- 引文解析：正常
- 章节树：正常
- 路径复核：本次增强区统一使用 `801/文本/txt` 与 `801/文本/metadata` 作为可追溯来源。

<!-- REAUDIT-2026-05-26 END -->
