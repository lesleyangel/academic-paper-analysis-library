# An integrated optimization method of multi-hierarchy variables for rudder structures with radial force transfer paths

## 0. 读取说明

- 文本来源：`801/文本/txt/An-integrated-optimization-method-of-multi-hierarchy-va_2024_Aerospace-Scien.txt`，PyMuPDF 抽取，10 页。
- 拆解依据：当前 txt 全文抽取；图 1-16 的细节仅来自题注和正文叙述，梁分布、云图和曲线细节均需要 PDF 图像复核。
- 读法提醒：本文不是单纯做结构优化算例，而是把“径向梁方向”从拓扑变量里拆出来，证明多层级变量一体化优化比传统拓扑-尺寸优化更有效。

## 1. 基本信息与论文身份

- 题名：An integrated optimization method of multi-hierarchy variables for rudder structures with radial force transfer paths。
- 作者：Jian-Jun Gou, Shu-Zhen Jia, Hai-Tao Tian, Jia-Xin Hu, Chun-Lin Gong。
- 期刊：Aerospace Science and Technology，148，2024，109115。
- 领域：飞行器结构优化、舵面结构、拓扑/尺寸/形状层级变量、静气动弹性。
- 论文类型：方法论文 + 工程算例验证。
- 研究对象：带径向梁式传力路径的舵结构。
- 方法组合：多层级变量分解、Gray code 统一编码、遗传算法、静力有限元、气动压力/升力曲线斜率约束下的静气动弹性优化。
- 证据类型：优化过程曲线、梁保留/删除与角度/尺寸演化、位移/应力云图、二层级与三层级模型对比。
- 目标读者：飞行器结构优化研究者、舵/翼类梁式结构设计者、使用启发式算法做多变量结构优化的工程研究者。

## 2. 摘要与核心信息提取

本文的核心主张是：对于径向梁传力结构，仅用拓扑和尺寸两个层级会把梁方向变化“压缩”进梁删除/保留问题，导致 ground structure 必须足够密、优化成本高；把角度作为隐式方向变量独立成第三层级，并与拓扑、尺寸统一编码后，可以在相同或相近变量规模下获得更轻、更低气动弹性影响的舵结构。

摘要的说服路径很直接：先说梁式传力路径优化依赖层级分解和交互效应；再提出常规层级为 topology/size，新增非常规层级 angle；随后给出统一编码和遗传算法；最后用两个问题闭环：静力质量最小化、静气动弹性影响量最小化。关键结果是三层级模型相对二层级模型质量降低 18.9%，气动弹性影响量降低 4.3%。

## 3. 选题层深拆

选题来自飞行器舵面结构的工程瓶颈：舵结构需要清晰传力路径，同时受质量、强度、位移和气动弹性性能约束。传统 ground structure 方法适合梁/桁架结构，但其“可选梁越密，潜在最优越好；梁越密，变量和计算成本越高”的矛盾非常突出。

作者把大问题收束为一个具体可验证的问题：径向梁结构中，梁的疏密和方向不仅取决于是否保留梁，也取决于梁相对初始角度的偏移；如果角度不作为变量，集中到高载荷区的梁只能通过更密的初始梁集合间接实现。这个问题具有明确边界：舵面径向梁、拓扑/尺寸/角度三类变量、两个优化目标场景。

选题价值主要是方法价值和工程价值叠加。方法上，它把“层级变量交互”从一般说法落到可编码、可交叉、可变异的优化模型；工程上，它减少为了获得密集局部传力路径而扩大 ground structure 的需求。

## 4. 领域位置与文献版图

Introduction 的文献版图分成四组：

- 飞行器结构优化背景：质量、静强度、动强度等约束下的结构设计。
- 拓扑优化方法：连续型密度/SIMP 方法适合无预设传力路径结构，但对梁式结构容易产生灰度边界和后处理重构成本。
- 离散型 ground structure 方法：适合桁架/梁，但依赖初始梁集，梁数不足会错过最优，梁数过多会降低效率。
- 多层级/一体化优化：已有材料-形状-拓扑、拓扑-建造方向、材料-纤维-铺层等集成优化，但径向梁方向变量没有被单独拆出。

本文站位是“继承 ground structure 和遗传算法，修正其对径向梁方向表达不足”。它没有挑战拓扑优化主流框架，而是在特定结构类型中提出更合适的变量表达。

## 5. Gap 制造机制

作者制造 gap 的方式是“传统方法能做，但代价不合理”：

1. 拓扑变量能表达梁删除/保留，却不能高效表达局部梁聚集方向。
2. 尺寸变量能调整承载能力，却不能改变传力路径几何方向。
3. 若靠更密的初始 ground structure 来获得高载区梁聚集，会造成过多变量和高优化成本。
4. 顺序式 topology -> shape/size 优化忽略层级间交互，可能错过匹配的拓扑、角度和尺寸组合。

这个 gap 是方法 gap，不是数据 gap。它真实且重要，但其普适性受限于“径向梁式、节点受边界约束、梁方向可用角度隐式表达”的结构族。

## 6. 创新性判断

- 作者声称的创新：新增 angle 层级，提出拓扑/角度/尺寸统一编码，构建二层级和三层级模型并对比。
- 我判断的真实创新：变量表达创新强于算法创新。遗传算法、Gray code、罚函数和随机通用抽样并非新工具，真正贡献在于把径向梁方向从拓扑中剥离，使梁分布密集化不依赖初始梁数。
- 创新强度：中等偏强。对特定结构很有用，但不是通用结构优化理论突破。
- 可信度：两个算例支撑了效率提升和性能提升，但只在一个舵面模型上验证，尚不足以证明对所有径向梁结构稳定有效。
- 易被挑战处：二层级模型 ground structure 的梁数、变量数和优化代数设置是否公平；GA 随机性是否需要多次独立运行统计。

## 7. 论证链条复原

背景：飞行器舵/翼类结构需要梁式传力路径优化。

已有方法：连续拓扑优化有重构问题；ground structure 有初始梁密度与效率矛盾；拓扑和尺寸顺序优化忽略交互。

缺口：径向梁结构中，梁角度代表局部传力方向，但传统模型没有把角度作为独立层级。

方法：将变量分解为 XT 拓扑、XA 角度、XS 尺寸；用 Gray code 统一离散和连续变量；对三类基因分别选择、交叉、变异；用罚函数处理约束。

验证：建立静力质量最小化和静气动弹性影响量最小化两个优化模型，并与二层级拓扑-尺寸模型对比。

结论：三层级模型在演化一定代数后表现出增长优势，最终质量和气动弹性指标更好。

最薄弱环节：从单一舵结构和单一 GA 参数设置推广到“一般更有效”时证据略少。

## 8. 方法/理论/模型细拆

方法输入包括 ground structure、梁数量、拓扑上下界、角度上下界、尺寸上下界、应力/位移/质量约束和气动弹性响应计算。输出是保留梁集合、梁角度偏移、梁截面尺寸和目标函数值。

模型 1 是二层级：Find XT, XS，Min M(XT, XS)，约束为 gi 小于限值，XT 为 0/1，XS 为连续尺寸。模型 2 是三层级：Find XT, XA, XS，新增角度变量 XA。模型 3/编码层把 XT 直接表示为 0/1，XA 与 XS 由 Gray code 表示，避免普通二进制的 Hamming cliff。

优化算子上，选择采用 stochastic universal sampling；交叉采用三类变量相互独立的单点交叉，避免拓扑、角度、尺寸基因错位交换；变异采用 simple mutation，概率为 0.7/染色体长度。适应度由目标函数排序转换，并通过外罚函数处理应力、位移和质量等不等式约束。

两个具体优化问题：静力问题最小化结构质量，约束应力 225 MPa、位移 27 mm；静气动弹性问题最小化升力曲线斜率相对降低量，约束质量、应力和位移。每代 25 个个体，100 代作为主要比较成本。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 角度变量可提高径向梁结构优化效率 | 摘要/方法/结果 | 三层级模型相对二层级模型质量降低 18.9%、气动弹性影响量降低 4.3% | 中强 | 对比是否受 GA 随机种子和初始梁数影响，需要统计复核 |
| 三层级静力优化能显著减重 | 5.1 | 质量从第 4 代 1.78 kg 降到第 100 代 0.87 kg；相对 ground structure 降低 77.0% | 强 | ground structure 质量定义排除了蒙皮和舵轴，需要边界清楚 |
| 优化过程呈初期快速、后期缓慢、偶发突降 | 5.1/5.2/结论 | 静力过程 4-22 代快速下降、23-57 代慢降、58-100 代渐降；气动弹性也分三阶段 | 中强 | 曲线细节需要 PDF 图像复核 |
| 角度变化承担了承载能力补偿功能 | 5.1 | 多数梁尺寸减小，但角度非单调调整以补偿承载能力 | 中 | 依赖图 10/11 梁角度和云图，需要 PDF 图像复核 |
| 静气动弹性目标也受益于三层级表达 | 5.2 | 气动弹性影响量从 8.83% 降到 5.48%，最终相对初始结构降低 37.9% | 强 | 只验证静气动弹性，未覆盖动态气动弹性/颤振 |
| 三层级优势在一定代数后出现并扩大 | 5.3 | 静力约第 23 代后、静气动弹性约第 46 代后三层级曲线优于二层级 | 中强 | 需要多次 GA 运行排除偶然性 |

## 10. 图表、公式与结果叙事提取

| 图/公式 | 论证功能 | 对应 claim | 关键信息 | 复核需求 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 把 ground structure 与潜在优化结构视觉化 | 传统拓扑删除难以表达局部梁聚集 | 低载区稀疏、高载区密集；角度变量有必要 | 需要 PDF 图像复核 |
| Eq. (1)-(3) | 从二层级模型过渡到三层级模型和统一编码 | 角度是新增层级，不是后处理 | XT 为 0/1，XA/XS 用 Gray code | 文本足够 |
| Fig. 2/3 | 展示三层级基因独立交叉和简单变异 | 遗传算子需适应层级变量 | 防止拓扑、角度、尺寸错位交换 | 需要 PDF 图像复核 |
| Eq. (6)/(7) | 定义两个工程优化问题 | 方法能覆盖静力和静气动弹性 | 质量最小化；升力曲线斜率影响量最小化 | 文本足够 |
| Fig. 9/12 | 展示目标函数随代数下降 | 优化过程有效且分阶段 | 静力质量、气动弹性影响量均下降 | 需要 PDF 图像复核 |
| Fig. 10/13 | 梁分布、位移、应力云图 | 约束满足且结构形态随优化变化 | 最大位移在舵尖，应力在舵轴附近 | 需要 PDF 图像复核 |
| Fig. 15/16 | 与二层级模型对比 | 三层级更有效 | 静力 18.9%、气动弹性 4.3% 改善 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

真实章节顺序是：1 Introduction；2 The optimization problem with multi-hierarchy variables；3 The multi-hierarchy integrated optimization algorithm；4 The optimization and numerical models；5 Results and discussions；6 Conclusions。

结构是典型方法论文布局，但中间两章分工清楚：第 2 章负责“为什么需要新变量层级”和数学问题定义；第 3 章负责“怎样用 GA 编码与操作”；第 4 章把通用方法落到舵面静力/气动弹性模型；第 5 章用结果曲线和对比证明方法优势。

标题偏好是描述型，不追求结果前置。优点是工程读者容易定位；缺点是小节标题没有暴露最关键发现，如 5.3 可以更强地命名为“Three-hierarchy model outperforms two-hierarchy model after sufficient evolution”。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `801/文本/txt/An-integrated-optimization-method-of-multi-hierarchy-va_2024_Aerospace-Scien.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：6
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 结果/验证型, 结论/展望型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction                                                  The variable optimization of different hierarchies always proceeds in | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 高 | 是 | 保留具体变量/对象 |
| 4.1 The optimization model and the implicit angle variable | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 5 Results and discussions | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 5.1 Statics problem | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 100 In general, the optimization process has decreasing optimization | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 6 Conclusions | 结论/展望型 | 收束贡献、边界和未来工作 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 节奏是“工程对象 -> 方法分类 -> 传统缺陷 -> 多层级已有进展 -> 径向梁特殊 gap -> 本文贡献”。段落较长，常用 while/however/thus 做转折。方法段落先定义变量，再解释物理含义，随后补一个“为什么这样设”的合理性说明。

结果段落节奏高度稳定：先说明图显示什么，再按代数分阶段描述数值变化，最后解释结构变化与性能变化的关系。它不是先给大结论再展示图，而是沿着图推进读者接受结论。

## 13. 文笔画像与语言习惯

整体语气工程化、克制，claim 强度多用 “can be found”“it should be noted”“in general”“to some extent”。作者偏好被动和无主句，但在贡献段会使用 “In this work”。时态上，Introduction 用一般现在时描述领域事实，方法用一般现在时定义模型，结果用过去/现在混合描述图中观察。

高频名词围绕 optimization、topology、size、angle、beam、structure、generation、aeroelastic。形容词偏功能性，如 integrated、multi-hierarchy、radial、static、implicit。副词常用于限制或推进，如 theoretically、respectively、specifically、relatively。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：optimization(133)；size(57)；structural(55)；topology(54)；structure(53)；beam(51)；beams(46)；respectively(46)；angle(43)；problem(42)；mass(38)；process(38)；method(36)；aeroelastic(35)；variable(33)；variables(32)；generation(32)；ground(30)；structures(26)；work(26)
- 高频学术名词：optimization(133)；structure(106)；method(36)；generation(32)；structures(26)；model(23)；displacement(21)；stress(20)；influence(19)；analysis(18)；distribution(18)；function(18)；quantity(17)；results(16)；simulation(16)；reduction(16)
- 高频学术动词：shown(23)；show(12)；shows(11)；indicates(9)；developed(9)；indicate(6)；solved(5)；compared(4)；proposed(2)；predicted(1)；reveal(1)；solve(1)；validated(1)；derived(1)
- 高频形容词：structural(55)；static(42)；aeroelastic(35)；variable(33)；objective(22)；genetic(21)；displacement(21)；optimal(20)；numerical(14)；different(12)；element(9)；initial(9)；general(9)；material(8)；individual(8)；positive(8)
- 高频副词/连接副词：respectively(46)；tively(7)；theoretically(6)；closely(5)；however(4)；actually(4)；specifically(4)；widely(3)；occasionally(3)；globally(2)；firstly(2)；inherently(2)；relatively(2)；newly(2)；randomly(2)；fully(1)
- 高频二词短语：ground structure(26)；optimization process(23)；structural mass(20)；static aeroelastic(16)；optimization method(14)；statics problem(14)；one find(14)；aeroelastic problem(13)；integrated optimization(12)；topology size(12)；angle size(12)；genetic algorithm(12)；objective function(12)；aerospace science(11)；science technology(11)；stress displacement(11)
- 高频三词短语：aerospace science technology(11)；static aeroelastic problem(9)；gou aerospace science(9)；integrated optimization method(8)；aeroelastic influence quantity(8)；aerosp sci technol(7)；force transfer paths(6)；problem objective minimum(6)；mass stress displacement(6)；topology angle size(6)；objective function value(6)；method multi-hierarchy variables(5)

**主动、被动与句法**

- 被动语态估计次数：145
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：657
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：258
- 一般过去时线索：32
- 现在完成时线索：2
- 情态动词线索：57
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：optimization(6)；variables(5)；topology(4)；size(4)；aerospace(3)；integrated(3)；multi-hierarchy(3)；rudder(3)
- 1. Introduction                                                  The variable optimization of different hierarchies always proceeds in：optimization(45)；size(34)；topology(33)；beam(32)；structure(28)；beams(24)；variable(23)；variables(22)
- 4.1. The optimization model and the implicit angle variable：optimization(20)；respectively(15)；generation(13)；obtained(11)；number(10)；work(9)；statics(9)；aeroelastic(9)
- 100. In general, the optimization process has decreasing optimization：optimization(58)；structural(23)；generation(19)；problem(19)；aeroelastic(19)；one(18)；two-hierarchy(18)；mass(17)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

- 背景句式：For a flight vehicle, the structure with force transfer paths is always designed by...
- gap 句式：It is difficult to obtain the matched optimal topology, shape and size by sequential optimization.
- 方法句式：A new variable is decomposed from X and creates a new hierarchy.
- 贡献句式：An integrated optimization method of multi-hierarchy variables is developed based on...
- 结果句式：The results show that the proposed model is more efficient than...
- 谨慎限定：to some extent, under this condition, in general, it should be noted that。
- 可改写模板：对于具有某种结构约束的 X，传统 Y 方法只能通过增加初始候选集间接表达 Z；本文将 Z 显式/隐式变量化，并与已有层级一体优化。

## 15. 引用策略与文献使用

引用主要服务于四个功能：证明飞行器结构优化目标多样；区分连续拓扑优化和离散 ground structure；说明集成优化已有基础；为遗传算法选择提供依据。作者对前人态度是“承认有效但指出场景限制”，不是强批判。

gap 的引用构造方式是：先用拓扑优化文献说明密度法成熟，再用 ground structure 文献说明梁式结构常用路径，最后用集成优化文献说明多层级变量不是孤立想法。本文位置被放在这些工作之后：不是发明优化框架，而是发明适合径向梁方向的变量层级。

## 16. 审稿人视角风险

- 随机算法可靠性：GA 结果是否做多随机种子统计？文中主要展示单条曲线，可能被质疑偶然性。
- 对比公平性：二层级模型设 18 梁、三层级设 12 梁且变量数同为 36，但几何搜索空间并不完全等价。
- 泛化边界：只验证一个舵结构，不能直接推广到所有 wing/rudder 或其他 beam-like 结构。
- 气动弹性模型深度：静气动弹性影响量是否足以代表真实舵面气动弹性风险，动态约束未覆盖。
- 图像依赖：核心形态证据依赖梁分布和云图，需要 PDF 图像复核。
- 参数敏感性：交叉率、变异率、代数、个体数对结论影响未系统讨论。

## 17. 可复用资产

- 选题套路：把传统方法中“隐含在某变量中的物理含义”拆成独立变量层级。
- gap 套路：传统方法可以解决，但需要更密候选集/更高成本/更多后处理，因此不够高效。
- 方法资产：统一编码不同类型变量，然后为不同层级设计非干扰遗传算子。
- 结果资产：用“同变量数/同代数成本”的对比强化效率 claim。
- 图表资产：优化路径图 + 结构形态演化图 + 关键变量柱状图 + 竞品模型对比曲线。

## 18. 对我写论文的启发

如果自己的研究也面对“变量耦合但传统模型分开做”的问题，可以学习本文的表达：不要笼统说“考虑耦合”，而要指出哪一个物理量被旧变量错误代表，然后把它拆出来并证明拆出来后搜索空间更合适。

此外，方法论文的结果不必只报最终最优值。本文把 4/22/57/100 代、1/29/55/100 代等中间结构拿出来，说明优化路径如何发生，这种“过程证据”对启发式算法尤其有说服力。

## 19. 最终浓缩

这篇论文最值得学的是：用变量层级重构来解决工程优化中的表达瓶颈。它的最强 claim 是 angle 作为隐式梁方向变量能让径向传力路径在较小 ground structure 下实现局部聚集；最关键证据是静力减重 18.9% 和静气动弹性影响量降低 4.3% 的二/三层级对比。最大风险是验证结构和随机优化统计仍偏单薄，后续应复核 PDF 图像并关注多随机种子、更多结构样本和动态气动弹性约束。

<!-- REAUDIT-2026-05-26 START -->

## 20. 复核增强：严格抽取、翻译、引文与句型

> 本区块由 `tools/upgrade_801_deep_analysis.py` 基于 `801/文本/txt/An-integrated-optimization-method-of-multi-hierarchy-va_2024_Aerospace-Scien.txt` 与 `801/文本/metadata/An-integrated-optimization-method-of-multi-hierarchy-va_2024_Aerospace-Scien.json` 重新抽取生成；用于修正旧报告中章节未全、引文缺失、摘要/结论未完整摘录的问题。双栏 PDF 抽取仍可能存在断行，引用和公式编号以 PDF 版面为最终准绳。

### 20.1 严格章节树（按 PDF/metadata TOC）

- L2 p.1: 1 Introduction （背景/领域定位）
- L2 p.2: 2 The optimization problem with multi-hierarchy variables （对象/问题/模块）
  - L3 p.2: 2.1 Optimization problem （对象/问题/模块）
  - L3 p.2: 2.2 General models （方法/模型）
- L2 p.3: 3 The multi-hierarchy integrated optimization algorithm （对象/问题/模块）
  - L3 p.3: 3.1 Unified chromosome encoding with gray code （对象/问题/模块）
  - L3 p.3: 3.2 Selection, crossover and mutation operators （对象/问题/模块）
  - L3 p.4: 3.3 Fitness function （对象/问题/模块）
- L2 p.4: 4 The optimization and numerical models （方法/模型）
  - L3 p.4: 4.1 The optimization model and the implicit angle variable （方法/模型）
  - L3 p.5: 4.2 The numerical model （方法/模型）
  - L3 p.6: 4.3 The optimization path （对象/问题/模块）
- L2 p.6: 5 Results and discussions （结果/讨论/验证）
  - L3 p.6: 5.1 Statics problem （对象/问题/模块）
  - L3 p.8: 5.2 Static aeroelastic problem （对象/问题/模块）
  - L3 p.8: 5.3 Comparison with two-hierarchy optimization （对象/问题/模块）
- L2 p.8: 6 Conclusions （结论）
- L2 p.10: CRediT authorship contribution statement （对象/问题/模块）
- L2 p.10: Declaration of competing interest （对象/问题/模块）
- L2 p.10: Data availability （对象/问题/模块）
- L2 p.10: Acknowledgments （对象/问题/模块）
- L2 p.10: References （参考文献）

### 20.2 章节名功能分析

| 章节/小节名 | 页码 | 层级 | 类型 | 复核说明 |
| --- | ---: | ---: | --- | --- |
| 1 Introduction | 1 | 2 | 背景/领域定位 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2 The optimization problem with multi-hierarchy variables | 2 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.1 Optimization problem | 2 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2 General models | 2 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3 The multi-hierarchy integrated optimization algorithm | 3 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.1 Unified chromosome encoding with gray code | 3 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2 Selection, crossover and mutation operators | 3 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.3 Fitness function | 4 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4 The optimization and numerical models | 4 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.1 The optimization model and the implicit angle variable | 4 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2 The numerical model | 5 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.3 The optimization path | 6 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5 Results and discussions | 6 | 2 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.1 Statics problem | 6 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.2 Static aeroelastic problem | 8 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.3 Comparison with two-hierarchy optimization | 8 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 6 Conclusions | 8 | 2 | 结论 | 来自 metadata TOC，正式分析按此章节点名复核 |
| CRediT authorship contribution statement | 10 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Declaration of competing interest | 10 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Data availability | 10 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Acknowledgments | 10 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| References | 10 | 2 | 参考文献 | 来自 metadata TOC，正式分析按此章节点名复核 |

### 20.3 摘要完整摘录（本地证据）

抽取状态：成功

> 公开库不直接展示完整英文摘要原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/An-integrated-optimization-method-of-multi-hierarchy-va_2024_Aerospace-Scien.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/An-integrated-optimization-method-of-multi-hierarchy-va_2024_Aerospace-Scien.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.4 摘要中文翻译

> 飞行器类梁力传递路径结构的优化密切依赖于变量的层次分解和相互作用效应。在这项工作中，径向梁舵结构的变量被分解为传统的拓扑和尺寸层次结构和新的非常规角度层次结构，这是一个具有径向梁方向隐式表达的表征变量。提出了离散变量拓扑和连续变量角度、尺寸的统一编码形式，并基于遗传算法提出了多层次变量的集成优化方法，并充分考虑了不同层次之间的相互作用影响。然后分别构建了拓扑和尺寸的两级优化模型和拓扑、尺寸和角度的三级优化模型。求解了以最小结构质量为目标、受应力、位移约束的静力学问题和以最小影响量为目标、受结构质量、应力、位移约束的静力气动弹性问题。结果表明，三层次优化模型比两层次优化模型效率更高，结构质量减少了18.9%，气动弹性影响量减少了4.3%。

### 20.5 结论完整摘录（本地证据）

结论章节识别：6 Conclusions；状态：独立结论章节

> 公开库不直接展示完整英文结论原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/An-integrated-optimization-method-of-multi-hierarchy-va_2024_Aerospace-Scien.json` 的 `conclusion` 字段，以及 `801/深度拆解/local_full_reports/An-integrated-optimization-method-of-multi-hierarchy-va_2024_Aerospace-Scien.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.6 结论中文翻译

> 在这项工作中，开发了一种具有径向力传递路径的舵结构的多层次变量集成优化方法。将径向梁舵的优化变量分解为拓扑和尺寸两级，拓扑、尺寸和角度三级，分别构建二级和三级优化模型。提出了基于遗传算法的多层次变量综合优化方法。目标最小的静力学问题 图 12 气动弹性问题的优化过程。 J.-J。郭等人。求解了结构质量及应力、位移约束，以及以最小影响量为目标的静气动弹性问题及质量、应力、位移约束，结果表明如下。 (1)综合多层次优化过程总体上表现为初始阶段进展较快，后续阶段进展缓慢，偶尔会出现几次突然进展。 (2) 对于三层次优化求解的静力学问题
> 
> 化方法，优化结构的质量减少
> 
> 航天科技148(2024)109115
> 
> 与地面和第一合格相比分别为77.0%和51.1%。
> 
> (3)对于采用三层次优化方法求解的静气动弹性问题，优化结构的气动弹性影响量降低了37.9%。 (4)与两层级模式相比，三层级模式经过一定世代的演进后，会产生积极的效应和优势。 (5) 三层次优化比两层次优化效率更高，结构质量减少了 18.9%
> 
> J.-J。郭等人。静力学问题和气动弹性问题 静态气动弹性问题的影响量减少 4.3%。

### 20.7 论文逻辑脉络复核

- 提出的问题：需结合 Introduction 首段复核。
- 旧方法/已有研究不足：需结合 Introduction 的文献转折句复核。
- 本文解决方式：In this work, the variable of a rudder structure with radial beams is decomposed into conventional hierarchies of topology and size and a new unconventional hi erarchy of angle, which is a representational variable with implicit expression for radial beam direction. A unified code form is proposed for discrete variable, i.e., topology and continuous variables, i.e., angle and size, and then an integrated optimization method of multi-hierarchy variables is developed based on the genetic al gorithm and the interaction effects between different hierarchies are fully considered. A two-hierarchy optimi zation model of topology and size and a three-hierarchy optimization model of topology, size and angle are then constructed, respectively.
- 学术/工程增量：需结合 Results/Conclusion 的量化结果复核。
- 复核判断：正式阅读时应检查 Introduction 的 gap 是否与 Method 的输入输出、Results 的评价指标和 Conclusion 的 claim 完全闭合；若摘要中的强 claim 没有在结果图表或结论中回收，应在审稿风险中标注。

### 20.8 引文分析补全

- 全文引用簇数量（估计）：60
- Introduction 引用簇数量（估计）：17
- References 条目数（解析）：40
- 可识别年份条目数：41
- 近五年/近年文献（2021+）数量：14
- 经典文献（2010年前）数量：10
- 同刊引用数量（按 subject 粗略匹配）：1
- 高频来源期刊（粗略）：Aerospace Science and Technology(1)；Composite Structures(1)
- 引用簇样例：[11], [12], [13,14], [11], [15], [32,33], [33,34], [33], [25], [26], [27], [28]

带引用的 gap/转折句样例：

- Such method is mostly appropriate to structures without any prespecified force transfer paths, while for beam-like structures, its element deleting process will lead to unsmooth beam boundaries (gray densities between white and black [15]) and needs complex beam reconstructions.
- It was found that in general, the particle swarm algorithm has similar effectiveness while higher efficiency when handling continuous problems, however, the genetic algorithm performs greater effectiveness for problems involving discrete variables [33].

References 解析样例（前12条）：

- [1] K. Liang, Z. Yin, Investigation on nonlinear buckling performance of the optimized wing structure under the realistic flight cases, Aerosp. Sci. Technol. 139 (2023) 108416.
- [2] P.D.R. Santos, et al., Effect of design parameters on the mass of a variable-span morphing wing based on finite element structural analysis and optimization, Aerosp. Sci. Technol. 80 (2018) 587–603.
- [3] O. Dababneh, T. Kipouros, Influence of high fidelity structural models on the predicted mass of aircraft wing using design optimization, Aerosp. Sci. Technol. 79 (2018) 164–173.
- [4] D.J. Munk, J.D. Miller, Topology optimization of aircraft components for increased sustainability, AIAA J. 60 (1) (2021) 445–
- 460. Vol. 60, No. 1.
- [5] S. Chintapalli, et al., The development of a preliminary structural design optimization method of an aircraft wing-box skin-stringer panels, Aerosp. Sci. Technol. 14 (3) (2010) 188–198.
- [6] M. Saporito, et al., Robust multidisciplinary analysis and optimization for conceptual design of flexible aircraft under dynamic aeroelastic constraints, Aerosp. Sci. Technol. 138 (2023)
- 108349.
Aerospace Science and Technology 148 (2024) 109115
- [7] D. Li, et al., Aeroelastic global structural optimization using an efficient CFD-based reduced order model, Aerosp. Sci. Technol. 94 (2019) 105354.
- [8] D. Sarojini, D. Mavris, Structural analysis and optimization of wings subjected to dynamic loads, AIAA Journal 60 (2) (2022) 1013–1023.
- [9] E. Jonsson, et al., High-fidelity gradient-based wing structural optimization including geometrically nonlinear flutter constraint, AIAA J. 0 (0) (2023) 1–17.
- [10] E. Jonsson, et al., Flutter and post-flutter constraints in aircraft design optimization, Progress Aerospace Sci. 109 (2019) 100537.

### 20.9 常用词、词类、语态与时态

- 高频词：optimization(125)；size(56)；topology(53)；structure(52)；beam(51)；fig(51)；structural(50)；beams(46)；respectively(46)；angle(43)；problem(42)；process(38)；mass(36)；aeroelastic(34)；variable(33)；variables(32)；generation(32)；ground(30)；work(26)；one(26)
- 高频名词化/学术名词：optimization(125)；structure(52)；generation(32)；displacement(21)；statics(19)；influence(18)；distribution(18)；function(18)；quantity(17)；reduction(16)；science(12)；tion(10)；fitness(10)；variation(9)；pressure(9)
- 高频学术动词：developed(9)；optimized(7)；indicate(6)；compared(4)；indicated(3)；reveal(1)；derived(1)；validated(1)
- 高频形容词：structural(50)；aeroelastic(34)；variable(33)；objective(22)；displacement(21)；static(21)；optimal(20)；genetic(18)；initial(9)；general(9)；element(8)；material(8)；individual(8)；positive(8)；aerodynamic(8)
- 高频副词：respectively(46)；tively(7)；closely(5)；actually(4)；specifically(4)；theoretically(3)；widely(3)；occasionally(3)；firstly(2)；only(2)；inherently(2)；relatively(2)；newly(2)；randomly(2)；fully(1)
- 高频二词短语：ground structure(26)；optimization process(23)；structural mass(20)；static aeroelastic(16)；statics problem(14)；one find(14)；aeroelastic problem(13)；integrated optimization(12)；topology size(12)；angle size(12)；objective function(12)；aerospace science(11)
- 高频三词短语：aerospace science technology(11)；static aeroelastic problem(9)；page gou aerospace(9)；gou aerospace science(9)；aeroelastic influence quantity(8)；force transfer paths(6)；problem objective minimum(6)；mass stress displacement(6)；topology angle size(6)；objective function value(6)；fig optimization process(6)；angle size variables(5)
- 被动语态估计：130；`we + 动作动词` 主动句估计：0
- 一般现在时线索：258；一般过去时线索：308；现在完成时线索：1；情态动词线索：57

章节词频：

- Abstract: optimization(4)；topology(4)；size(4)；variables(3)；variable(3)；angle(3)；structural(3)；mass(3)
- Introduction: optimization(29)；topology(26)；size(21)；structural(17)；beam(17)；variable(16)；structure(14)；hierarchies(13)
- Conclusion: optimization(8)；problem(7)；aeroelastic(6)；three-hierarchy(5)；mass(4)；integrated(3)；multi-hierarchy(3)；statics(3)

### 20.10 句型库扩充（每类多句）

#### 背景句
- 未在抽取文本中稳定识别，需人工从对应章节补充。
#### Gap句
- 原句/结构：Such method is mostly appropriate to structures without any prespecified force transfer paths, while for beam-like structures, its element deleting process will lead to unsmooth beam boundaries (gray densities between white and black [15]) and needs complex beam reconstructions.
  可迁移模板：Such method is mostly appropriate to structures without any prespecified force transfer paths, while for beam-like structures, its element deleting process will lead to unsmooth beam boundaries (gray densities between white and black [X]) and needs complex beam reconstructions.
- 原句/结构：The performance and efficiency of such optimization process are closely related with the scale of variable set, i.e., the optimal structure can only be obtained from the ground structure with sufficient number of beams, however, exces sive beams will lead to high cost and low efficiency of optimizations.
  可迁移模板：The performance and efficiency of such optimization process are closely related with the scale of variable set, i.e., the optimal structure can only be obtained from the ground structure with sufficient number of beams, however, exces sive beams will lead to high cost and low efficiency of optimizations.
- 原句/结构：However, it is difficult to obtain the matched optimal topology, shape and size by the sequential optimization, i.e., the topology hierarchy is also influenced by the shape and size hierarchy.
  可迁移模板：However, it is difficult to obtain the matched optimal topology, shape and size by the sequential optimization, i.e., the topology hierarchy is also influenced by the shape and size hierarchy.
#### 方法句
- 原句/结构：In this work, the variable of a rudder structure with radial beams is decomposed into conventional hierarchies of topology and size and a new unconventional hi erarchy of angle, which is a representational variable with implicit expression for radial beam direction.
  可迁移模板：In this work, the variable of a rudder structure with radial beams is decomposed into conventional hierarchies of topology and size and a new unconventional hi erarchy of angle, which is a representational variable with implicit expression for radial beam direction.
- 原句/结构：A unified code form is proposed for discrete variable, i.e., topology and continuous variables, i.e., angle and size, and then an integrated optimization method of multi-hierarchy variables is developed based on the genetic al gorithm and the interaction effects between different hierarchies are fully considered.
  可迁移模板：A unified code form is proposed for discrete variable, i.e., topology and continuous variables, i.e., angle and size, and then an integrated optimization method of multi-hierarchy variables is developed based on the genetic al gorithm and the interaction effects between different hierarchies are fully considered.
- 原句/结构：A two-hierarchy optimi zation model of topology and size and a three-hierarchy optimization model of topology, size and angle are then constructed, respectively.
  可迁移模板：A two-hierarchy optimi zation model of topology and size and a three-hierarchy optimization model of topology, size and angle are then constructed, respectively.
#### 结果句
- 原句/结构：The results show that the three-hierarchy optimization model is more efficient than the two-hierarchy one with structural mass reduction of 18.9 % and aeroelastic influence quantity reduction of 4.3 %.
  可迁移模板：The results show that the three-hierarchy optimization model is more efficient than the two-hierarchy one with structural mass reduction of X and aeroelastic influence quantity reduction of X.
- 原句/结构：The topology to some extent indicates the presence or absence of structural constituents, while the size indicates the specific width, length, thickness or cross-sectional area of the constituent.
  可迁移模板：The topology to some extent indicates the presence or absence of structural constituents, while the size indicates the specific width, length, thickness or cross-sectional area of the constituent.
- 原句/结构：The results show that the three-hierarchy optimization model is more efficient than the two-hierarchy one with structural mass reduction of 18.9 % and aeroelastic influence quantity reduction of 4.3 %.
  可迁移模板：The results show that the three-hierarchy optimization model is more efficient than the two-hierarchy one with structural mass reduction of X and aeroelastic influence quantity reduction of X.
#### 贡献句
- 原句/结构：Under some circumstances, the beam presence and absence are deter mined by its size, i.e., smaller than a specified value reveals beam absence and vice versa, thus, the topology and size optimizations are always conducted simultaneously or sequentially and iteratively [19,21, 22].
  可迁移模板：Under some circumstances, the beam presence and absence are deter mined by its size, i.e., smaller than a specified value reveals beam absence and vice versa, thus, the topology and size optimizations are always conducted simultaneously or sequentially and iteratively [X,X, X].
- 原句/结构：In such methods, the key step is the decomposition of the variable into different hierarchies, and the above studies reveal that more hierarchies will bring about higher efficiency with more complex optimization models.
  可迁移模板：In such methods, the key step is the decomposition of the variable into different hierarchies, and the above studies reveal that more hierarchies will bring about higher efficiency with more complex optimization models.
#### 限制/边界句
- 原句/结构：The optimization should consider variables of different hierarchies such as the basic ones, i.e., structural topology and size.
  可迁移模板：The optimization should consider variables of different hierarchies such as the basic ones, i.e., structural topology and size.
- 原句/结构：In this method, the ground structure should be considered as the initial structure, certain trusses or beams should be specified firstly J.-J.
  可迁移模板：In this method, the ground structure should be considered as the initial structure, certain trusses or beams should be specified firstly J.-J.
- 原句/结构：The performance and efficiency of such optimization process are closely related with the scale of variable set, i.e., the optimal structure can only be obtained from the ground structure with sufficient number of beams, however, exces sive beams will lead to high cost and low efficiency of optimizations.
  可迁移模板：The performance and efficiency of such optimization process are closely related with the scale of variable set, i.e., the optimal structure can only be obtained from the ground structure with sufficient number of beams, however, exces sive beams will lead to high cost and low efficiency of optimizations.

### 20.11 抽取失败与人工复核提示

- 摘要抽取：正常
- 结论抽取：正常
- 引文解析：正常
- 章节树：正常
- 路径复核：本次增强区统一使用 `801/文本/txt` 与 `801/文本/metadata` 作为可追溯来源。

<!-- REAUDIT-2026-05-26 END -->
